#!/usr/bin/env python3
"""Hash-bound sampled narrator identity screen, with the existing workflow tool."""
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess

PROFILE = Path('/Users/drive/kindling-repo-stage/books/book-01-kindled/narration/kokoro-guided-calder/profile.production-default.json')
REFERENCE = Path('/Users/drive/boundary-universe/public/private-benchmarks/voice-workshop/calder/calder-original-source.wav')
VERIFIER = Path('/Users/drive/kindling-narrator-stage/scripts/verify-voice-identity.py')


def main():
    spec = importlib.util.spec_from_file_location('nm_audio_worker',
                        Path(__file__).with_name('nm-breeze-audio.py'))
    worker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(worker)
    out = worker.QUEUE/'voice-screen-v1'
    out.mkdir(exist_ok=True)
    with (worker.QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX | fcntl.LOCK_NB)
        if worker.busy() or any((worker.QUEUE/f'chapter-{n}'/'direction.ready').exists() for n in (47,48)):
            raise RuntimeError('Yield to active model work or restored readiness')
        if (out/'attempt.json').exists():
            raise RuntimeError('Sampled identity attempt already recorded; preserve evidence')
        profile = json.loads(PROFILE.read_text())
        if worker.sha(REFERENCE.read_bytes()) != profile['referenceSha256']:
            raise RuntimeError('Locked Calder reference changed')
        roles,segments,bindings = {},[],[]
        for number in range(1,49):
            production = worker.QUEUE/f'chapter-{number:02d}'
            source = worker.BOOK/f'manuscript/chapter-{number:02d}.md'
            source_sha = worker.sha(source.read_bytes())
            score = json.loads((production/'direction.json').read_text())
            if score['sourceSha256'] != source_sha:
                raise RuntimeError('Source/direction changed')
            candidate = worker.QUEUE/'local-repair-candidates-v1'/production.name
            role = f'chapter-{number:02d}'
            roles[role] = {'referenceAudio':str(REFERENCE),
                           'minVoiceSimilarity':profile['targets']['minimumVoiceSimilarity']}
            if (candidate/'technical-review.json').exists():
                technical = json.loads((candidate/'technical-review.json').read_text())
                manifest = json.loads((candidate/'take-manifest.json').read_text())
                if worker.sha(json.dumps(manifest,sort_keys=True).encode()) != technical['bindingSha256']:
                    raise RuntimeError('Candidate manifest changed')
                takes = manifest['takes']
                audio = Path(technical['audioPath'])
                edition = 'separate-provisional-repair-v1'
            else:
                technical = json.loads((production/'technical-review.json').read_text())
                takes = [{'id':s['id'],'path':str(production/'breeze-directed'/f"{s['id']}.wav")}
                         for s in score['segments']]
                audio = production/f'chapter-{number:02d}.breeze-calder.mp3'
                edition = 'original-local-listening-candidate'
            if technical['sourceSha256'] != source_sha or worker.sha(audio.read_bytes()) != technical['audioSha256']:
                raise RuntimeError('Audio/source edition binding changed')
            for take in takes:
                path = Path(take['path'])
                digest = worker.sha(path.read_bytes())
                if take.get('sha256',digest) != digest:
                    raise RuntimeError('Checkpoint differs from candidate edition')
                segments.append({'index':len(segments),'performance':role,'wav':str(path),
                                 'sha256':digest,'segmentId':take['id']})
            bindings.append({'chapter':number,'sourceSha256':source_sha,
                             'audioSha256':technical['audioSha256'],'edition':edition})
        palette = out/'palette.json'
        worker.save(palette,{'mode':'performance','performances':roles,
                            'note':'All chapter labels are sampling strata of one locked narrator, not cast voices'})
        record = out/'record.json'
        worker.save(record,{'schemaVersion':1,'performancePalette':str(palette),
                            'performances':list(roles),'segments':segments,'bindings':bindings,
                            'referenceSha256':profile['referenceSha256'],'profileSha256':worker.sha(PROFILE.read_bytes()),
                            'state':'adapted-hash-bound-QA-ledger-not-new-render-provenance',
                            'published':False,'ownerListening':'pending'})
        worker.save(out/'attempt.json',{'state':'sampled-identity-running','published':False,
                                       'recordSha256':worker.sha(record.read_bytes()),
                                       'verifierSha256':worker.sha(VERIFIER.read_bytes())})
        # One shared local cache; allow the workflow verifier's public model to
        # populate it once if absent. No hosted inference or paid API is used.
        env = dict(os.environ,HF_HOME=worker.QA_CACHE,HF_HUB_OFFLINE='0',
                   HF_HUB_CACHE=worker.QA_CACHE+'/hub',HUGGINGFACE_HUB_CACHE=worker.QA_CACHE+'/hub')
        with (out/'screen.log').open('a') as output:
            result = subprocess.run([str(worker.PYTHON),str(VERIFIER),str(record),
                                     '--maximum-segments-per-role','24','--output',str(out/'voice-quality.json')],
                                    env=env,stdout=output,stderr=subprocess.STDOUT,timeout=3600)
        for segment in segments:
            if worker.sha(Path(segment['wav']).read_bytes()) != segment['sha256']:
                raise RuntimeError('Checkpoint changed during sampled identity screen')
        if result.returncode not in (0,1) or not (out/'voice-quality.json').exists():
            worker.save(out/'attempt.json',{'state':'failed-needs-diagnosis','exitCode':result.returncode,
                                           'published':False,'ownerListening':'pending'})
            raise RuntimeError('Identity checker failed; inspect preserved log, no automatic retry')
        worker.save(out/'attempt.json',{'state':'sampled-identity-complete-review-pending',
                                       'published':False,'ownerListening':'pending',
                                       'rawReportSha256':worker.sha((out/'voice-quality.json').read_bytes()),
                                       'scope':'Sampled identity only, not accent/naturalness/coverage or human listening approval'})
        worker.log('Sampled narrator identity screen complete; supervisor/owner review pending')


if __name__ == '__main__':
    main()
