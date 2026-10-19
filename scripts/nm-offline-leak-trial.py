#!/usr/bin/env python3
"""Bounded exact-word diagnostic takes, no production edits or publication."""
import fcntl
import importlib.util
import json
import os
import re
from pathlib import Path
import subprocess
import sys

TRIALS = [(35, 's043', 'Warm, restrained Australian narration. Quiet observational opening; clear and unhurried. Stay in the same adult narrator voice.'),
          (38, 's068', 'Warm, restrained Australian narration. Clear spatial narration, even register, clean clause boundaries. Stay in the same adult narrator voice.'),
          (41, 's056', 'Warm, restrained Australian narration. Quiet, exact statements with clear attribution. Stay in the same adult narrator voice.')]

TRIALS_2 = [
    (30, 's115', 'Warm, restrained Australian narration. Preserve the deliberate repetition with clear, separate thought landings. Stay in the same adult narrator voice.'),
    (33, 's025', 'Warm, restrained Australian narration. Quiet factual observation, clear and unhurried. Stay in the same adult narrator voice.'),
    (33, 's193', 'Warm, restrained Australian narration. Brief, sincere reply with a clean final landing. Stay in the same adult narrator voice.'),
    (34, 's008', 'Warm, restrained Australian narration. Read the written ledger precisely, with clean thought boundaries and no added repetition. Stay in the same adult narrator voice.'),
    (34, 's122', 'Warm, restrained Australian narration. Preserve each deliberate repeated thought without rushing. Quiet fear beneath factual restraint. Stay in the same adult narrator voice.'),
    (34, 's127', 'Warm, restrained Australian narration. Read the formal message precisely, with clear clause boundaries and a clean signature landing. Stay in the same adult narrator voice.'),
    (35, 's002', 'Warm, restrained Australian narration. Quiet observational opening, clear and unhurried. Stay in the same adult narrator voice.'),
    (37, 's059', 'Warm, restrained Australian narration. Quiet observation of a crowded room, without announcer excitement. Stay in the same adult narrator voice.'),
    (38, 's139', 'Warm, restrained Australian narration. Quiet observational opening; restrained warmth, not sentimentality. Stay in the same adult narrator voice.'),
    (39, 's079', 'Warm, restrained Australian narration. Quiet adult recollection; precise chronology, clear attribution and clean thought landings. Stay in the same adult narrator voice.'),
    (39, 's098', 'Warm, restrained Australian narration. Quiet, exact narrative statement with a clean landing. Stay in the same adult narrator voice.'),
    (39, 's099', 'Warm, restrained Australian narration. Brief, level reassurance; keep reply and attribution together. Return to the same base narrator for attribution.'),
    (47, 's096', 'Warm, restrained Australian narration. Quiet scene opening; plain factual chronology and gently understated invitation. Stay in the same adult narrator voice.'),
    (48, 's039', 'Warm, restrained Australian narration. Plain factual observation followed by a single quiet final thought. Stay in the same adult narrator voice.')]

TRIALS_3 = [
    (32, 's163', 'Warm, restrained Australian narration. Brief, level answer with attribution attached. Return to the base narrator for attribution.'),
    (35, 's042', 'Warm, restrained Australian narration. Dry, thoughtful dialogue; preserve contracted tense clearly. Quiet narrator for actions and attribution.'),
    (37, 's037', 'Warm, restrained Australian narration. Brief, level reply with a clean final landing. Stay in the same adult narrator voice.'),
    (37, 's038', 'Warm, restrained Australian narration. Firm but unshowy reply; preserve the contracted tense and full thought clearly. Stay in the same adult narrator voice.'),
    (38, 's138', 'Warm, restrained Australian narration. Clear factual recollection; distinguish the changing tenses and keep attribution precise. Return to the base narrator for actions and attribution.')]
TRIALS_4 = [(32,'s035','Warm, restrained Australian narration. Plain factual account of an administrative action; clean clause boundaries and a quiet final landing. Stay in the same adult narrator voice.')]
TRIALS_5 = [
    (33,'s118','Warm, restrained Australian narration. Read the written team listing precisely, including each rank. Clear factual register, no announcer excitement. Stay in the same adult narrator voice.'),
    (33,'s147','Warm, restrained Australian narration. Clear tactical narration, deliberate complete thought landings. Carry the final physical observation through to its quiet end. Stay in the same adult narrator voice.'),
    (33,'s216','Warm, restrained Australian narration. Read the written result and each team rank precisely; quiet factual delivery, no announcer excitement. Stay in the same adult narrator voice.')]
TRIALS_6 = [(48,'s112','Warm, restrained Australian narration in the locked adult Calder voice. Quiet observational prose with gentle human warmth, complete thought landings and no theatrical character imitation. Remain in the base narrator throughout.')]


def main(resume_cache_failure=False, batch=1):
    spec = importlib.util.spec_from_file_location(
        'nm_audio_worker', Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy() or any((worker.QUEUE/f'chapter-{n}'/'direction.ready').exists()
                                for n in (47, 48)):
            raise RuntimeError('Yield to active model work or restored readiness')
        out = worker.QUEUE/f'diagnostic-instruction-leak-v{batch}'
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
        for number, key, instruct in {1:TRIALS,2:TRIALS_2,3:TRIALS_3,4:TRIALS_4,5:TRIALS_5,6:TRIALS_6}[batch]:
            directory = worker.QUEUE/f'chapter-{number:02d}'
            source = worker.BOOK/f'manuscript/chapter-{number:02d}.md'
            direction = directory/'direction.json'
            track = json.loads(direction.read_text())
            if worker.sha(source.read_bytes()) != track['sourceSha256']:
                raise ValueError('Stale diagnostic source')
            segment = next(s for s in track['segments'] if s['id'] == key)
            text = segment['text']
            if batch == 5 and key in ('s118','s216'):
                text = re.sub(r'\(([0-9]+)\)',r'\1',text)
                if worker.words(text) != worker.words(segment['text']):
                    raise ValueError('Rank punctuation trial changed source words')
            trial_id = f'c{number}-{key}'
            inputs.append({'chapter': number, 'segmentId': key,
                           'sourceSha256': track['sourceSha256'],
                           'directionSha256': worker.sha(direction.read_bytes()),
                           'oldTakeSha256': worker.sha((directory/'breeze-directed'/f'{key}.wav').read_bytes()),
                           'originalInstruction': segment['instruct'],
                           'trialId': trial_id, 'text': text, 'originalText':segment['text'],
                           'transformation':'Remove rank parentheses only; exact words/digits/order retained' if text != segment['text'] else 'Instruction only; exact text retained',
                           'instruct': instruct})
            segments.append({**segment, 'id': trial_id, 'text':text, 'instruct': instruct})
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
            source = worker.BOOK/f"manuscript/chapter-{item['chapter']:02d}.md"
            if worker.sha(source.read_bytes()) != item['sourceSha256'] or worker.sha((directory/'direction.json').read_bytes()) != item['directionSha256'] or worker.sha(
                    (directory/'breeze-directed'/f"{item['segmentId']}.wav").read_bytes()) != item['oldTakeSha256']:
                raise RuntimeError('Original direction/take changed during diagnosis')
        worker.save(out/'review.json', {'state': 'diagnostic-supervisor-review-pending',
                    'published': False, 'ownerListening': 'pending', 'reports': reports,
                    'note': 'Short-instruction native-speed audition only. Canonical words and production audio untouched. ASR is not human listening or pickup acceptance.'})
        worker.log('Instruction-leak trial complete; no production take or publication changed')
        worker.save(out/'attempt.json', {'state':'complete-review-pending', 'published':False,
                                       'ownerListening':'pending'})


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume-cache-failure', action='store_true')
    parser.add_argument('--batch', type=int, choices=[1,2,3,4,5,6], default=1)
    args = parser.parse_args()
    main(args.resume_cache_failure, args.batch)
