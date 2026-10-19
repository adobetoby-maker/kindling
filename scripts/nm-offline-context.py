#!/usr/bin/env python3
"""One bounded, supervisor-selected contextual ASR pass; no audio mutation."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess

# Codex disposition after reading isolated transcripts and exact direction text.
TARGETS = {32: ['s163', 's164'], 34: ['s008', 's122', 's127'],
           35: ['s002', 's043'], 37: ['s038', 's059'],
           38: ['s068', 's139'], 39: ['s079', 's098', 's099'],
           41: ['s056'], 47: ['s096'], 48: ['s039']}


def main():
    spec = importlib.util.spec_from_file_location(
        'nm_audio_worker', Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for number, ids in TARGETS.items():
            for held in (47, 48):
                if (worker.QUEUE/f'chapter-{held}'/'direction.ready').exists():
                    raise RuntimeError('Readiness restored; yield offline model work')
            if worker.busy():
                raise RuntimeError('Shared model slot occupied')
            directory = worker.QUEUE/f'chapter-{number:02d}'
            audit = json.loads((directory/'asr-audit.json').read_text())
            request = directory/'asr-context-request-coverage-002.json'
            report = directory/'asr-context-review-coverage-002.json'
            wanted = {k: audit[k] for k in ('sourceSha256', 'audioSha256')}
            wanted.update(segmentIds=ids, reviewer='Codex',
                          reason='Corroborate isolated instruction leakage, repeated or missing words in neighboring audio; no automatic repair authority',
                          ownerListening='pending')
            if request.exists() and json.loads(request.read_text()) != wanted:
                raise RuntimeError('Preserve existing different request')
            worker.save(request, wanted)
            if report.exists():
                prior = json.loads(report.read_text())
                if prior.get('requestSha256') == worker.sha(request.read_bytes()):
                    continue
                raise RuntimeError('Preserve existing different report')
            args = [str(worker.QA_PYTHON), str(worker.ROOT/'scripts/nm-breeze-triage.py'),
                    str(number), '--context', '--context-request', request.name]
            if not (directory/'published.json').exists():
                args.append('--unpublished')
            env = dict(os.environ, HF_HOME=worker.QA_CACHE, HF_HUB_OFFLINE='1',
                       HF_HUB_CACHE=worker.QA_CACHE+'/hub',
                       HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
            worker.log(f'chapter {number}: offline coverage-002 context starting')
            with (directory/'asr/context-coverage-002.log').open('a') as output:
                subprocess.run(args, env=env, stdout=output, stderr=subprocess.STDOUT,
                               check=True, timeout=1200)
        worker.log('Offline coverage-002 contexts complete; supervisor review pending')


if __name__ == '__main__':
    main()
