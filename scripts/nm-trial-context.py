#!/usr/bin/env python3
"""Check bounded instruction-repair auditions in neighboring audio."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess


def main(batch=1):
    spec = importlib.util.spec_from_file_location(
        'nm_audio_worker', Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    out = worker.QUEUE/f'diagnostic-instruction-leak-v{batch}'
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy():
            raise RuntimeError('Shared model slot occupied')
        if (out/'context-attempt.json').exists():
            raise RuntimeError('Bounded context check already attempted; preserve evidence')
        inputs = json.loads((out/'inputs.json').read_text())
        review = json.loads((out/'review.json').read_text())
        reports = {r['trialId']: r for r in review['reports']}
        bindings, jobs = [], []
        for trial in inputs:
            directory = worker.QUEUE/f"chapter-{trial['chapter']:02d}"
            direction = directory/'direction.json'
            source = worker.BOOK/f"manuscript/chapter-{trial['chapter']:02d}.md"
            if worker.sha(direction.read_bytes()) != trial['directionSha256'] or worker.sha(source.read_bytes()) != trial['sourceSha256']:
                raise RuntimeError('Source/score changed since trial')
            track = json.loads(direction.read_text())
            index = next(i for i, s in enumerate(track['segments']) if s['id'] == trial['segmentId'])
            group = track['segments'][max(0,index-1):index+2]
            parts, takes = [], []
            for position, segment in enumerate(group):
                replacement = segment['id'] == trial['segmentId']
                path = out/'breeze-directed'/f"{trial['trialId']}.wav" if replacement else directory/'breeze-directed'/f"{segment['id']}.wav"
                digest = worker.sha(path.read_bytes())
                if replacement and digest != reports[trial['trialId']]['wavSha256']:
                    raise RuntimeError('Diagnostic take changed')
                pcm, rate = worker.sf.read(path, dtype='float32')
                if rate != 24000 or pcm.ndim != 1 or not worker.np.isfinite(pcm).all():
                    raise RuntimeError('Unexpected context take format')
                pcm = pcm.copy()
                edge = min(120, len(pcm)//2)
                if edge:
                    pcm[:edge] *= worker.np.linspace(0, 1, edge)
                    pcm[-edge:] *= worker.np.linspace(1, 0, edge)
                parts.append(pcm)
                pause = segment.get('pauseAfterMs',0) if position < len(group)-1 else 0
                if pause:
                    parts.append(worker.np.zeros(int(rate*pause/1000), dtype='float32'))
                takes.append({'id':segment['id'], 'path':str(path), 'sha256':digest,
                              'replacement':replacement, 'pauseAfterMsInAudit':pause})
            wav = out/f"context-{trial['trialId']}.wav"
            worker.sf.write(wav, worker.np.concatenate(parts), 24000, subtype='PCM_16')
            expected = out/f"context-{trial['trialId']}.expected.txt"
            expected.write_text(' '.join(s['text'] for s in group)+'\n')
            binding = {'trialId':trial['trialId'], 'sourceSha256':trial['sourceSha256'],
                       'directionSha256':trial['directionSha256'], 'takes':takes,
                       'contextSha256':worker.sha(wav.read_bytes()),
                       'note':'Exact neighboring takes plus diagnostic center, production five-ms fades and internal pauses; no final trailing authored pause, no time stretching'}
            bindings.append(binding)
            jobs.append((expected,wav,out/f"context-{trial['trialId']}.comparison.json"))
        worker.save(out/'context-inputs.json', bindings)
        worker.save(out/'context-attempt.json', {'state':'running', 'published':False})
        env = dict(os.environ, HF_HOME=worker.QA_CACHE, HF_HUB_OFFLINE='1',
                   HF_HUB_CACHE=worker.QA_CACHE+'/hub', HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
        with (out/'context.log').open('a') as log:
            for expected,wav,report in jobs:
                result = subprocess.run([str(worker.QA_PYTHON), str(worker.QA_SCRIPT),
                                         str(expected), str(wav), '--output', str(report)],
                                        env=env, stdout=log, stderr=subprocess.STDOUT, timeout=1200)
                if result.returncode not in (0,2) or not report.exists():
                    raise RuntimeError('Context verifier failed')
        for trial, binding, job in zip(inputs, bindings, jobs):
            directory = worker.QUEUE/f"chapter-{trial['chapter']:02d}"
            source = worker.BOOK/f"manuscript/chapter-{trial['chapter']:02d}.md"
            if worker.sha((directory/'direction.json').read_bytes()) != trial['directionSha256'] or worker.sha(source.read_bytes()) != trial['sourceSha256']:
                raise RuntimeError('Source/score changed during context check')
            if any(worker.sha(Path(t['path']).read_bytes()) != t['sha256'] for t in binding['takes']):
                raise RuntimeError('Context input take changed')
            binding['comparisonSha256'] = worker.sha(job[2].read_bytes())
        worker.save(out/'context-review.json', {'state':'context-supervisor-review-pending',
                    'published':False, 'ownerListening':'pending', 'bindings':bindings,
                    'note':'Objective ASR only; no human listening or production mutation'})
        worker.save(out/'context-attempt.json', {'state':'complete-review-pending', 'published':False})
        worker.log(f'{len(inputs)} bounded instruction-trial joins screened; production unchanged')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch', type=int, choices=[1,2], default=1)
    main(parser.parse_args().batch)
