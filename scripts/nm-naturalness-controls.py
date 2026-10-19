#!/usr/bin/env python3
"""Bounded, fixed-per-input-seed UTMOS controls; never promotes audio."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT/'books/book-2680-national-measure/narration/breeze'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, indent=2)+'\n')


def main():
    # One shared quality/model slot; no production records or audio are changed.
    with (QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        import importlib.util
        spec = importlib.util.spec_from_file_location('nm_worker', ROOT/'scripts/nm-breeze-audio.py')
        worker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(worker)
        if worker.busy():
            raise RuntimeError('Shared model slot occupied')
        out = QUEUE/'naturalness-controls-v1'
        out.mkdir(exist_ok=True)
        if (out/'attempt.json').exists():
            raise RuntimeError('Preserve existing bounded attempt; no blind retry')
        raw = QUEUE/'naturalness-screen-v1/naturalness.json'
        ledger_path = QUEUE/'voice-screen-v1/record.json'
        ledger = json.loads(ledger_path.read_text())
        report = json.loads(raw.read_text())
        by_index = {s['index']: s for s in ledger['segments']}
        palette = json.loads((QUEUE/'voice-screen-v1/palette.json').read_text())
        refs = {v['referenceAudio'] for v in palette['performances'].values()}
        if len(refs) != 1:
            raise RuntimeError('This diagnostic requires one identical reference')
        reference = Path(refs.pop())
        if sha(reference) != ledger['referenceSha256']:
            raise RuntimeError('Reference changed')
        inputs = [{'kind':'reference-repeat','path':str(reference)} for _ in range(3)]
        for failure in report['failures']:
            s = by_index[failure['index']]
            inputs.append({'kind':'original-screen-outlier', 'path':s['wav'],
                           'chapter':s['performance'], 'segmentId':s['segmentId'],
                           'originalScore':failure['mos'], 'originalFloor':failure['floor'],
                           'expectedSha256':s['sha256']})
        controls = json.loads((QUEUE/'voice-controls-v1/record.json').read_text())
        for s in controls['segments']:
            if s['performance'] == 'known-reference-duration-control':
                inputs.append({'kind':'known-reference-duration-control','path':s['wav'],
                               'expectedSha256':s['sha256']})
        original = next(s for s in ledger['segments'] if s['performance']=='chapter-48' and s['segmentId']=='s112')
        inputs.append({'kind':'original-48-s112','path':original['wav'],'expectedSha256':original['sha256']})
        candidate = QUEUE/'diagnostic-instruction-leak-v6/breeze-directed/c48-s112.wav'
        review = json.loads((candidate.parent.parent/'review.json').read_text())['reports'][0]
        inputs.append({'kind':'candidate-48-s112','path':str(candidate),'expectedSha256':review['wavSha256']})
        for s in inputs:
            s['sha256'] = sha(Path(s['path']))
            if s.get('expectedSha256',s['sha256']) != s['sha256']:
                raise RuntimeError('Input changed')
        save(out/'inputs.json', inputs)
        save(out/'attempt.json', {'state':'fixed-per-input-seed-controls-running',
             'rawReportSha256':sha(raw),'ledgerSha256':sha(ledger_path),
             'seed':42,'published':False,'ownerListening':'pending','pid':os.getpid()})
        import numpy as np
        import torch
        import utmosv2
        model = utmosv2.create_model(pretrained=True)
        results = []
        for s in inputs:
            random.seed(42)
            np.random.seed(42)
            torch.manual_seed(42)
            score = float(model.predict(input_path=s['path'],device='cpu',verbose=False))
            results.append({**s,'mos':score})
            print(s['kind'], s.get('chapter',''),s.get('segmentId',''),score,flush=True)
            save(out/'progress.json', {'results':results,'complete':False})
        if any(sha(Path(s['path'])) != s['sha256'] for s in inputs):
            raise RuntimeError('Input changed during scoring')
        reference_score = results[0]['mos']
        save(out/'review.json', {'state':'controls-complete-supervisor-review-pending',
             'seedReset':'42 before every predict; not a replacement of raw screen',
             'sharedReferenceMos':reference_score,'diagnosticFloor':max(3.15,reference_score-.45),
             'results':results,'published':False,'ownerListening':'pending',
             'note':'Outlier evidence only; identical reference repeats test order dependence. No automatic take acceptance.'})


if __name__ == '__main__':
    main()
