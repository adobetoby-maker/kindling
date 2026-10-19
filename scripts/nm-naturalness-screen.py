#!/usr/bin/env python3
"""Sampled UTMOSv2 outlier screen using the existing isolated quality runtime."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess

PYTHON = Path('/Volumes/Drive 2/monroe-ai/voice-quality-venv/bin/python')
VERIFIER = Path('/Users/drive/kindling-narrator-stage/scripts/verify-speech-naturalness.py')


def main():
    spec = importlib.util.spec_from_file_location('nm_audio_worker',Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    out = worker.QUEUE/'naturalness-screen-v1'
    out.mkdir(exist_ok=True)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy():
            raise RuntimeError('Shared quality/model slot occupied')
        if (out/'attempt.json').exists():
            raise RuntimeError('Naturalness attempt already recorded; preserve evidence')
        record = worker.QUEUE/'voice-screen-v1/record.json'
        ledger = json.loads(record.read_text())
        record_sha = worker.sha(record.read_bytes())
        env = dict(os.environ,HF_HOME=worker.QA_CACHE,HF_HUB_OFFLINE='1',
                   HF_HUB_CACHE=worker.QA_CACHE+'/hub',HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
        metadata = json.loads(subprocess.check_output([str(PYTHON),'-c',
            'import importlib.metadata,json; d=importlib.metadata.distribution("utmosv2"); print(json.dumps({"version":d.version,"directUrl":d.read_text("direct_url.json")}))'],text=True))
        worker.save(out/'attempt.json',{'state':'sampled-naturalness-running','published':False,
            'ownerListening':'pending','recordSha256':record_sha,'verifierSha256':worker.sha(VERIFIER.read_bytes()),
            'runtimePython':str(PYTHON),'packageMetadata':metadata,
            'note':'Existing runtime/cache; CPU-only diagnostic outlier model, no TTS or human listening'})
        with (out/'screen.log').open('a') as log:
            result = subprocess.run([str(PYTHON),str(VERIFIER),str(record),
                    '--maximum-segments-per-role','24','--output',str(out/'naturalness.json')],
                    env=env,stdout=log,stderr=subprocess.STDOUT,timeout=10800)
        if result.returncode not in (0,1) or not (out/'naturalness.json').exists():
            worker.save(out/'failure.json',{'state':'failed-needs-diagnosis','exitCode':result.returncode,
                                           'published':False,'ownerListening':'pending'})
            raise RuntimeError('Naturalness checker failed; inspect log before retry')
        if worker.sha(record.read_bytes()) != record_sha or any(
                worker.sha(Path(s['wav']).read_bytes()) != s['sha256'] for s in ledger['segments']):
            raise RuntimeError('Frozen input ledger/takes changed during naturalness screening')
        worker.save(out/'completion.json',{'state':'sampled-naturalness-complete-review-pending',
            'published':False,'ownerListening':'pending',
            'rawReportSha256':worker.sha((out/'naturalness.json').read_bytes()),
            'note':'Sampled outlier evidence only; not full-book prosody or owner listening approval'})
        worker.log('Sampled UTMOSv2 naturalness screen complete; supervisor/owner review pending')


if __name__ == '__main__':
    main()
