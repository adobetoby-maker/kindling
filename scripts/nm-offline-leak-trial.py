#!/usr/bin/env python3
"""Three exact-word diagnostic takes, no production edits or publication."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

TRIALS = [(35, 's043', 'Warm, restrained Australian narration. Quiet observational opening; clear and unhurried. Stay in the same adult narrator voice.'),
          (38, 's068', 'Warm, restrained Australian narration. Clear spatial narration, even register, clean clause boundaries. Stay in the same adult narrator voice.'),
          (41, 's056', 'Warm, restrained Australian narration. Quiet, exact statements with clear attribution. Stay in the same adult narrator voice.')]


def main(resume_cache_failure=False):
    spec = importlib.util.spec_from_file_location(
        'nm_audio_worker', Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy() or any((worker.QUEUE/f'chapter-{n}'/'direction.ready').exists()
                                for n in (47, 48)):
            raise RuntimeError('Yield to active model work or restored readiness')
        out = worker.QUEUE/'diagnostic-instruction-leak-v1'
        out.mkdir(exist_ok=True)
        if (out/'attempt.json').exists():
            if not (resume_cache_failure and not (out/'cache-recovery.json').exists()
                    and not any((out/'breeze-directed').glob('*.wav'))
                    and 'LocalEntryNotFoundError' in (out/'trial.log').read_text()):
                raise RuntimeError('One bounded trial already attempted; preserve evidence')
            worker.save(out/'cache-recovery.json', {
                'reason': 'Initial loader used ASR cache; failed before producing any take',
                'resolution': 'Use existing local Breeze cache offline; no model download',
                'productionAudioUnchanged': True})
        inputs, segments = [], []
        for number, key, instruct in TRIALS:
            directory = worker.QUEUE/f'chapter-{number:02d}'
            source = worker.BOOK/f'manuscript/chapter-{number:02d}.md'
            direction = directory/'direction.json'
            track = json.loads(direction.read_text())
            if worker.sha(source.read_bytes()) != track['sourceSha256']:
                raise ValueError('Stale diagnostic source')
            segment = next(s for s in track['segments'] if s['id'] == key)
            trial_id = f'c{number}-{key}'
            inputs.append({'chapter': number, 'segmentId': key,
                           'sourceSha256': track['sourceSha256'],
                           'directionSha256': worker.sha(direction.read_bytes()),
                           'oldTakeSha256': worker.sha((directory/'breeze-directed'/f'{key}.wav').read_bytes()),
                           'originalInstruction': segment['instruct'],
                           'trialId': trial_id, 'text': segment['text'], 'instruct': instruct})
            segments.append({**segment, 'id': trial_id, 'instruct': instruct})
        worker.save(out/'inputs.json', inputs)
        worker.save(out/'direction.json', {'segments': segments,
                    'diagnosticOnly': True, 'ownerListening': 'pending'})
        worker.save(out/'attempt.json', {'state': 'one-bounded-diagnostic-running',
                    'published': False, 'ownerListening': 'pending'})
        env = dict(os.environ, HF_HOME=worker.QA_CACHE, HF_HUB_OFFLINE='1',
                   HF_HUB_CACHE=worker.QA_CACHE+'/hub',
                   HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
        render_cache = '/Users/drive/.cache/huggingface'
        render_env = dict(os.environ, HF_HOME=render_cache, HF_HUB_OFFLINE='1',
                          HF_HUB_CACHE=render_cache+'/hub',
                          HUGGINGFACE_HUB_CACHE=render_cache+'/hub')
        with (out/'trial.log').open('a') as output:
            subprocess.run([str(worker.PYTHON), str(worker.RENDER), str(out), 'directed'],
                           env=render_env, stdout=output, stderr=subprocess.STDOUT,
                           check=True, timeout=2400)
            # Renderer has exited before each verifier loads Whisper.
            reports = []
            for item in inputs:
                key = item['trialId']
                expected = out/f'{key}.expected.txt'
                expected.write_text(item['text']+'\n')
                wav = out/'breeze-directed'/f'{key}.wav'
                raw = out/f'{key}.comparison.json'
                result = subprocess.run([str(worker.QA_PYTHON), str(worker.QA_SCRIPT),
                                         str(expected), str(wav), '--output', str(raw)],
                                        env=env, stdout=output, stderr=subprocess.STDOUT,
                                        timeout=1200)
                if result.returncode not in (0, 2) or not raw.exists():
                    raise RuntimeError('Diagnostic verifier failed; inspect trial log')
                pcm, rate = worker.sf.read(wav)
                reports.append({'trialId': key, 'wavSha256': worker.sha(wav.read_bytes()),
                                'durationSec': len(pcm)/rate,
                                'finite': bool(worker.np.isfinite(pcm).all()),
                                'samplePeak': float(worker.np.max(worker.np.abs(pcm))),
                                'comparisonSha256': worker.sha(raw.read_bytes())})
        for item in inputs:
            directory = worker.QUEUE/f"chapter-{item['chapter']:02d}"
            if worker.sha((directory/'direction.json').read_bytes()) != item['directionSha256'] or worker.sha(
                    (directory/'breeze-directed'/f"{item['segmentId']}.wav").read_bytes()) != item['oldTakeSha256']:
                raise RuntimeError('Original direction/take changed during diagnosis')
        worker.save(out/'review.json', {'state': 'diagnostic-supervisor-review-pending',
                    'published': False, 'ownerListening': 'pending', 'reports': reports,
                    'note': 'Short-instruction native-speed audition only. Canonical words and production audio untouched. ASR is not human listening or pickup acceptance.'})
        worker.log('Instruction-leak trial complete; no production take or publication changed')


if __name__ == '__main__':
    main('--resume-cache-failure' in sys.argv[1:])
