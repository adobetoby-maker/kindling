#!/usr/bin/env python3
"""Serialize isolated coverage corroboration for separate repaired editions."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess


def main():
    spec = importlib.util.spec_from_file_location('nm_audio_worker',
                        Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    root = worker.QUEUE/'local-repair-candidates-v1'
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX | fcntl.LOCK_NB)
        for directory in sorted(root.glob('chapter-*')):
            if worker.busy() or any((worker.QUEUE/f'chapter-{n}'/'direction.ready').exists() for n in (47,48)):
                raise RuntimeError('Yield to active model work or restored readiness')
            audit = json.loads((directory/'asr-audit.json').read_text())
            prior = directory/'asr-isolated-review.json'
            if prior.exists():
                if json.loads(prior.read_text()).get('audioSha256') == audit['audioSha256']:
                    continue
                raise RuntimeError('Preserve differing prior screening')
            env = dict(os.environ,HF_HOME=worker.QA_CACHE,HF_HUB_OFFLINE='1',
                       HF_HUB_CACHE=worker.QA_CACHE+'/hub',HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
            number = int(directory.name.split('-')[-1])
            worker.log(f'chapter {number}: separate candidate isolated flag checks starting')
            with (directory/'isolated.log').open('a') as output:
                subprocess.run([str(worker.QA_PYTHON),str(worker.ROOT/'scripts/nm-breeze-triage.py'),
                                str(number),'--candidate-root',str(root)],env=env,
                               stdout=output,stderr=subprocess.STDOUT,check=True,timeout=2400)
        worker.log('Separate candidate isolated screening complete; supervisor review pending')


if __name__ == '__main__':
    main()
