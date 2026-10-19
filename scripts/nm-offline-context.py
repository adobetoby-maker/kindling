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
RESIDUALS = {33:['s118','s147','s216'],37:['s100','s171'],41:['s144'],
             47:['s149'],48:['s010','s012']}


def main(residuals=False):
    spec = importlib.util.spec_from_file_location(
        'nm_audio_worker', Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        label = 'residual-004' if residuals else 'coverage-002'
        for number, ids in (RESIDUALS if residuals else TARGETS).items():
            for held in (47, 48):
                if (worker.QUEUE/f'chapter-{held}'/'direction.ready').exists():
                    raise RuntimeError('Readiness restored; yield offline model work')
            if worker.busy():
                raise RuntimeError('Shared model slot occupied')
            directory = worker.QUEUE/f'chapter-{number:02d}'
            audit = json.loads((directory/'asr-audit.json').read_text())
            request = directory/f'asr-context-request-{label}.json'
            report = directory/f'asr-context-review-{label}.json'
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
            worker.log(f'chapter {number}: offline {label} context starting')
            with (directory/f'asr/context-{label}.log').open('a') as output:
                subprocess.run(args, env=env, stdout=output, stderr=subprocess.STDOUT,
                               check=True, timeout=1200)
        worker.log(f'Offline {label} contexts complete; supervisor review pending')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--residuals',action='store_true')
    main(parser.parse_args().residuals)
