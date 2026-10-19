#!/usr/bin/env python3
"""One selected isolated ASR pass to localize unresolved context additions."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess

TARGETS = {32:['s162','s163','s164'], 34:['s009','s123','s128'],
           35:['s042','s044'], 37:['s037','s038','s060'],
           38:['s069','s138'], 39:['s098','s099'],
           47:['s097'], 48:['s040']}


def main():
    spec = importlib.util.spec_from_file_location('nm_audio_worker',
                        Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for number, ids in TARGETS.items():
            if worker.busy() or any((worker.QUEUE/f'chapter-{n}'/'direction.ready').exists() for n in (47,48)):
                raise RuntimeError('Yield to model work or restored readiness')
            directory = worker.QUEUE/f'chapter-{number:02d}'
            audit = json.loads((directory/'asr-audit.json').read_text())
            request = directory/'asr-isolated-request-localize-003.json'
            report = directory/'asr-isolated-review-localize-003.json'
            wanted = {k:audit[k] for k in ('sourceSha256','audioSha256')}
            wanted.update(segmentIds=ids,reviewer='Codex',ownerListening='pending',
                          reason='Localize context-tail additions and numeric instruction-like speech; no automatic pickup authority')
            if request.exists() and json.loads(request.read_text()) != wanted:
                raise RuntimeError('Preserve existing different request')
            worker.save(request,wanted)
            if report.exists():
                if json.loads(report.read_text()).get('requestSha256') == worker.sha(request.read_bytes()):
                    continue
                raise RuntimeError('Preserve existing different report')
            args = [str(worker.QA_PYTHON),str(worker.ROOT/'scripts/nm-breeze-triage.py'),str(number),
                    '--isolated-request',request.name]
            if not (directory/'published.json').exists():
                args.append('--unpublished')
            env = dict(os.environ,HF_HOME=worker.QA_CACHE,HF_HUB_OFFLINE='1',
                       HF_HUB_CACHE=worker.QA_CACHE+'/hub',HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
            worker.log(f'chapter {number}: selected take localization starting')
            with (directory/'asr/localize-003.log').open('a') as output:
                subprocess.run(args,env=env,stdout=output,stderr=subprocess.STDOUT,
                               check=True,timeout=1200)
        worker.log('Selected take localization complete; supervisor review pending')


if __name__ == '__main__':
    main()
