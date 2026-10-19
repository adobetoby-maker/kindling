#!/usr/bin/env python3
"""Assemble separate provisional repair editions and screen them; never publish."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess

def main(edition=1):
    spec = importlib.util.spec_from_file_location('nm_audio_worker',
                        Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    records = worker.QUEUE/f'local-repair-candidates-v{edition}'
    media = Path(f'/Volumes/Drive 2/monroe-ai/national-measure/local-repair-candidates-v{edition}')
    records.mkdir(exist_ok=True)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy() or any((worker.QUEUE/f'chapter-{n}'/'direction.ready').exists() for n in (47,48)):
            raise RuntimeError('Yield to active model work or restored readiness')
        overrides = {}
        for batch in ((1,2,3) if edition == 1 else (1,2,3,4,5,6)):
            trial_dir = worker.QUEUE/f'diagnostic-instruction-leak-v{batch}'
            review = json.loads((trial_dir/'review.json').read_text())
            candidates = {r['trialId']:r for r in review['reports']}
            for trial in json.loads((trial_dir/'inputs.json').read_text()):
                key = (trial['chapter'],trial['segmentId'])
                if key in overrides:
                    raise ValueError('Duplicate repair selection; supervisor must resolve')
                candidate = candidates[trial['trialId']]
                wav = trial_dir/'breeze-directed'/f"{trial['trialId']}.wav"
                if worker.sha(wav.read_bytes()) != candidate['wavSha256']:
                    raise RuntimeError('Diagnostic candidate changed')
                overrides[key] = {**trial, 'candidatePath':str(wav),
                                  'candidateSha256':candidate['wavSha256'],
                                  'diagnosticBatch':batch}
        if edition == 2:
            # Only these chapter editions changed after frozen v1. Preserve the
            # other eight v1 editions rather than copying/re-screening them.
            overrides = {key:value for key,value in overrides.items() if key[0] in (32,33,48)}
        selection = {'reviewer':'Codex',
                    'state':'provisional-local-repair-edition-not-approved',
                    'published':False, 'ownerListening':'pending',
                    'knownUnresolved':['37 s038 clause/tense discrepancy','37 s059 who/who-d discrepancy',
                                      'context-tail decoder additions','other previously logged lexical residuals',
                                      'mastering, pace, voice/stability and owner listening'],
                    'overrides':list(overrides.values())}
        if edition == 2:
            selection['scope'] = 'Changed chapters32/33/48 only; frozen v1 retained elsewhere'
            selection['knownUnresolved'][:0] = ['33 s216 isolated number homophone uncertainty',
                                               '32 s035 Clerk/clique recognition']
        if (records/'selection.json').exists():
            if json.loads((records/'selection.json').read_text()) != selection:
                raise RuntimeError('Preserve frozen differing edition selection')
        else:
            worker.save(records/'selection.json', selection)
        for number in sorted({n for n,_ in overrides}):
            if worker.busy():
                raise RuntimeError('Yield to active model work')
            directory = worker.QUEUE/f'chapter-{number:02d}'
            destination = media/f'chapter-{number:02d}'
            destination.mkdir(parents=True,exist_ok=True)
            evidence_dir = records/f'chapter-{number:02d}'
            evidence_dir.mkdir(exist_ok=True)
            source = worker.BOOK/f'manuscript/chapter-{number:02d}.md'
            source_sha = worker.sha(source.read_bytes())
            direction = directory/'direction.json'
            direction_sha = worker.sha(direction.read_bytes())
            track = json.loads(direction.read_text())
            if source_sha != track['sourceSha256'] or worker.words(source.read_text()) != worker.words(' '.join(s['text'] for s in track['segments'])):
                raise RuntimeError('Canonical source/score word lock differs')
            take_manifest = []
            for segment in track['segments']:
                candidate = overrides.get((number,segment['id']))
                original = directory/'breeze-directed'/f"{segment['id']}.wav"
                original_sha = worker.sha(original.read_bytes())
                if candidate:
                    exact_text = candidate['text'] == segment['text']
                    rank_punctuation_only = (edition == 2 and candidate['diagnosticBatch'] == 5
                        and number == 33 and segment['id'] in ('s118','s216')
                        and candidate.get('originalText') == segment['text']
                        and candidate['text'] == worker.re.sub(r'\(([0-9]+)\)',r'\1',segment['text'])
                        and worker.words(candidate['text']) == worker.words(segment['text']))
                    if candidate['sourceSha256'] != source_sha or candidate['directionSha256'] != direction_sha or not (exact_text or rank_punctuation_only) or candidate['oldTakeSha256'] != original_sha:
                        raise RuntimeError('Repair evidence differs from original source/score/take')
                    path = Path(candidate['candidatePath'])
                    take_sha = worker.sha(path.read_bytes())
                    if take_sha != candidate['candidateSha256']:
                        raise RuntimeError('Candidate changed before assembly')
                else:
                    path, take_sha = original, original_sha
                take_manifest.append({'id':segment['id'],'path':str(path),'sha256':take_sha,
                                      'originalSha256':original_sha,'replacement':bool(candidate),
                                      'pauseAfterMs':segment.get('pauseAfterMs',650)})
            binding = {'sourceSha256':source_sha,'directionSha256':direction_sha,'takes':take_manifest}
            binding_sha = worker.sha(json.dumps(binding,sort_keys=True).encode())
            worker.save(evidence_dir/'take-manifest.json',binding)
            wav = destination/f'chapter-{number:02d}.edge-faded.wav'
            mp3 = destination/f'chapter-{number:02d}.breeze-calder.mp3'
            technical = evidence_dir/'technical-review.json'
            if not technical.exists():
                if wav.exists() or mp3.exists():
                    raise RuntimeError('Partial candidate exists; preserve and diagnose before resuming')
                peak, frames = 0.0,0
                with worker.sf.SoundFile(wav,mode='w',samplerate=24000,channels=1,subtype='PCM_16') as output:
                    for take in take_manifest:
                        pcm,rate = worker.sf.read(take['path'],dtype='float32')
                        if rate != 24000 or pcm.ndim != 1 or not len(pcm) or not worker.np.isfinite(pcm).all():
                            raise RuntimeError('Invalid checkpoint waveform')
                        peak = max(peak,float(worker.np.max(worker.np.abs(pcm))))
                        if peak >= .9999:
                            raise RuntimeError('PCM rail requires diagnosis, not normalization')
                        fade = min(120,len(pcm)//4)
                        if fade:
                            pcm[:fade] *= worker.np.linspace(0,1,fade,dtype=worker.np.float32)
                            pcm[-fade:] *= worker.np.linspace(1,0,fade,dtype=worker.np.float32)
                        pcm[0] = pcm[-1] = 0
                        pause_frames = int(24000*take['pauseAfterMs']/1000)
                        output.write(pcm)
                        output.write(worker.np.zeros(pause_frames,dtype='float32'))
                        frames += len(pcm)+pause_frames
                subprocess.run(['ffmpeg','-v','error','-n','-i',str(wav),'-ac','1','-c:a','libmp3lame','-b:a','96k',str(mp3)],check=True)
                subprocess.run(['ffmpeg','-v','error','-i',str(mp3),'-f','null','-'],check=True)
                if any(worker.sha(Path(t['path']).read_bytes()) != t['sha256'] for t in take_manifest):
                    raise RuntimeError('Checkpoint changed during assembly')
                if worker.sha(source.read_bytes()) != source_sha or worker.sha(direction.read_bytes()) != direction_sha:
                    raise RuntimeError('Source/score changed during assembly')
                worker.save(technical,{'sourceSha256':source_sha,'audioSha256':worker.sha(mp3.read_bytes()),
                    'bindingSha256':binding_sha,'audioPath':str(mp3),'wavPath':str(wav),
                    'durationSec':frames/24000,'segments':len(take_manifest),'maxSegmentPeak':peak,
                    'wordLock':'passed','decode':'passed','fadeMs':5,'timeStretch':False,
                    'published':False,'ownerListening':'pending','state':'local-provisional-QA-pending'})
            report = json.loads(technical.read_text())
            if report['bindingSha256'] != binding_sha or report['audioSha256'] != worker.sha(mp3.read_bytes()):
                raise RuntimeError('Existing provisional edition binding differs')
            audit = evidence_dir/'asr-audit.json'
            if audit.exists():
                prior = json.loads(audit.read_text())
                if prior.get('audioSha256') == report['audioSha256']:
                    continue
                raise RuntimeError('Preserve differing prior candidate ASR')
            raw = evidence_dir/'asr-comparison.json'
            env = dict(os.environ,HF_HOME=worker.QA_CACHE,HF_HUB_OFFLINE='1',
                       HF_HUB_CACHE=worker.QA_CACHE+'/hub',HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
            worker.log(f'chapter {number}: separate repaired local edition assembled; full ASR starting')
            with (evidence_dir/'asr.log').open('a') as output:
                result = subprocess.run([str(worker.QA_PYTHON),str(worker.QA_SCRIPT),str(source),str(mp3),'--output',str(raw)],
                                        env=env,stdout=output,stderr=subprocess.STDOUT,timeout=2400)
            if result.returncode not in (0,2) or not raw.exists():
                raise RuntimeError('Candidate ASR failed; inspect log')
            if worker.sha(source.read_bytes()) != source_sha or worker.sha(mp3.read_bytes()) != report['audioSha256']:
                raise RuntimeError('Candidate ASR input changed')
            comparison = json.loads(raw.read_text())
            worker.save(audit,{'sourceSha256':source_sha,'audioSha256':report['audioSha256'],
                        'rawReportSha256':worker.sha(raw.read_bytes()),
                        'orderedWordCoverage':comparison['orderedWordCoverage'],
                        'state':'screened-supervisor-review-pending','published':False,
                        'ownerListening':'pending','note':'ASR screen only, not acceptance or human listen'})
        worker.log('Separate repaired local editions screened; no publication or original mutation')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--edition',type=int,choices=[1,2],default=1)
    main(parser.parse_args().edition)
