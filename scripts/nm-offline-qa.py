#!/usr/bin/env python3
"""Drain hash-bound ASR screens only; never render, repair, or publish audio.

Use while the publication hold keeps the existing render worker idle. All model
subprocesses finish sequentially. Results remain supervisor-review pending.
"""
import fcntl
import importlib.util
from pathlib import Path


def main():
    path = Path(__file__).with_name('nm-breeze-audio.py')
    spec = importlib.util.spec_from_file_location('nm_audio_worker', path)
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        # Fail closed if publication/render readiness has been restored.
        for number in (47, 48):
            directory = worker.QUEUE/f'chapter-{number:02d}'
            if (directory/'direction.ready').exists() or not (
                    directory/'direction.ready.publication-held').exists():
                raise RuntimeError('Offline QA requires the existing publication hold')
        if worker.busy():
            raise RuntimeError('Shared model slot occupied; no QA started')
        for number in (47, 48):
            worker.audit_output(number, allow_unpublished=True)
        while worker.triage_backlog(allow_unpublished=True):
            pass
        while worker.context_backlog():
            pass
        worker.log('Offline ASR queue drained; publication unchanged; supervisor review pending')


if __name__ == '__main__':
    main()
