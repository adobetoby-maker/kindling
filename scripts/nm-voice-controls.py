#!/usr/bin/env python3
"""Duration controls, long-passage windows and reset-neighbor identity checks."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess


def main(candidate_batch=None):
    spec = importlib.util.spec_from_file_location('nm_audio_worker',Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    root = worker.QUEUE/'voice-screen-v1'
    out = worker.QUEUE/(f'voice-pickup-batch-{candidate_batch}' if candidate_batch else 'voice-controls-v1')
    out.mkdir(exist_ok=True)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy():
            raise RuntimeError('Shared model slot occupied')
        if (out/'attempt.json').exists():
            raise RuntimeError('Bounded controls already attempted; preserve evidence')
        ledger = json.loads((root/'record.json').read_text())
        quality = json.loads((root/'voice-quality.json').read_text())
        palette = json.loads((root/'palette.json').read_text())
        reference = Path(next(iter(palette['performances'].values()))['referenceAudio'])
        if worker.sha(reference.read_bytes()) != ledger['referenceSha256']:
            raise RuntimeError('Locked reference changed')
        rows,origins = [],[]
        def add(path,role,origin):
            rows.append({'index':len(rows),'performance':role,'wav':str(path),'sha256':worker.sha(path.read_bytes())})
            origins.append({'index':rows[-1]['index'],**origin})
        audio,rate = worker.sf.read(reference,dtype='float32')
        duration = len(audio)/rate
        for seconds in (() if candidate_batch else (1.5,2.0,3.0,4.24,6.0)):
            for offset in (0.0,max(0,(duration-seconds)/2)):
                end = min(len(audio),int((offset+seconds)*rate))
                crop = out/f'reference-{seconds}-{offset:.3f}.wav'
                worker.sf.write(crop,audio[int(offset*rate):end],rate,subtype='PCM_16')
                add(crop,'known-reference-duration-control',{'type':'known-positive-reference-crop',
                    'sourceSha256':ledger['referenceSha256'],'startSec':offset,'durationSec':seconds})
        long = next(s for s in ledger['segments'] if s['performance']=='chapter-48' and s['segmentId']=='s112')
        if candidate_batch:
            trial_dir = worker.QUEUE/f'diagnostic-instruction-leak-v{candidate_batch}'
            trial = next(s for s in json.loads((trial_dir/'inputs.json').read_text()) if s['chapter']==48 and s['segmentId']=='s112')
            report = next(s for s in json.loads((trial_dir/'review.json').read_text())['reports'] if s['trialId']==trial['trialId'])
            source = worker.BOOK/'manuscript/chapter-48.md'
            if trial['oldTakeSha256'] != long['sha256'] or worker.sha(source.read_bytes()) != trial['sourceSha256']:
                raise RuntimeError('Candidate does not replace the reviewed original edition')
            long = {**long,'wav':str(trial_dir/'breeze-directed'/f"{trial['trialId']}.wav"),'sha256':report['wavSha256']}
        long_path = Path(long['wav'])
        if worker.sha(long_path.read_bytes()) != long['sha256']:
            raise RuntimeError('Long outlier changed')
        audio,rate = worker.sf.read(long_path,dtype='float32')
        starts = sorted(set([float(n) for n in range(0,int(len(audio)/rate)-5,6)]+[len(audio)/rate-6]))
        for offset in starts:
            crop = out/f'chapter-48-s112-{offset:.3f}.wav'
            worker.sf.write(crop,audio[int(offset*rate):int((offset+6)*rate)],rate,subtype='PCM_16')
            add(crop,'long-outlier-temporal-window',{'type':'chapter-48-s112-window',
                'sourceWavSha256':long['sha256'],'startSec':offset,'durationSec':6})
        # Check neighbors separately, not averaged with the short failure, so a
        # strong neighbor cannot silently wash out a different short voice.
        selected = set()
        for failure in ([] if candidate_batch else quality['failures']):
            index = failure['index']
            for adjacent in (index-1,index+1):
                if adjacent < 0 or adjacent >= len(ledger['segments']):
                    continue
                item = ledger['segments'][adjacent]
                if item['performance'] != failure['role'] or adjacent in selected:
                    continue
                path = Path(item['wav'])
                if worker.sf.info(path).duration < 5:
                    continue
                if worker.sha(path.read_bytes()) != item['sha256']:
                    raise RuntimeError('Neighbor checkpoint changed')
                selected.add(adjacent)
                add(path,'separate-reset-neighbor',{'type':'separate-reset-neighbor',
                    'originalLedgerIndex':adjacent,'chapter':item['performance'],'segmentId':item['segmentId'],
                    'adjacentFailedIndex':index})
        roles = sorted({r['performance'] for r in rows})
        worker.save(out/'palette.json',{'mode':'performance','performances':{
            role:{'referenceAudio':str(reference),'minVoiceSimilarity':.84} for role in roles}})
        worker.save(out/'record.json',{'performancePalette':str(out/'palette.json'),'performances':roles,
            'segments':rows,'origins':origins,'referenceSha256':ledger['referenceSha256'],
            'baseVoiceReportSha256':worker.sha((root/'voice-quality.json').read_bytes()),
            'scope':'Diagnostic control views, no production audio changes or lowered threshold',
            'published':False,'ownerListening':'pending'})
        worker.save(out/'attempt.json',{'state':'controls-running','published':False,'ownerListening':'pending'})
        env = dict(os.environ,HF_HOME=worker.QA_CACHE,HF_HUB_OFFLINE='1',HF_HUB_CACHE=worker.QA_CACHE+'/hub',
                   HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
        verifier = '/Users/drive/kindling-narrator-stage/scripts/verify-voice-identity.py'
        with (out/'screen.log').open('a') as log:
            result = subprocess.run([str(worker.PYTHON),verifier,str(out/'record.json'),
                    '--maximum-segments-per-role','1000','--output',str(out/'voice-quality.json')],
                    env=env,stdout=log,stderr=subprocess.STDOUT,timeout=2400)
        if result.returncode not in (0,1) or not (out/'voice-quality.json').exists():
            raise RuntimeError('Control checker failed; inspect log, no blind retry')
        if worker.sha(reference.read_bytes()) != ledger['referenceSha256'] or any(
                worker.sha(Path(r['wav']).read_bytes()) != r['sha256'] for r in rows):
            raise RuntimeError('Control inputs changed')
        worker.save(out/'attempt.json',{'state':'controls-complete-review-pending','published':False,
            'ownerListening':'pending','rawReportSha256':worker.sha((out/'voice-quality.json').read_bytes())})
        worker.log('Voice duration/temporal/reset controls complete; original failures retained')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate-batch',type=int,choices=[6])
    main(parser.parse_args().candidate_batch)
