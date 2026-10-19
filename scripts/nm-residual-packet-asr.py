#!/usr/bin/env python3
"""One serialized decoder view of exact-edition residual review contexts."""
import difflib
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT/'books/book-2680-national-measure/narration/breeze'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value,indent=2)+'\n')


def words(text):
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",text.lower().replace('’',"'"))


def main():
    with (QUEUE/'offline-qa.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX | fcntl.LOCK_NB)
        spec = importlib.util.spec_from_file_location('nm_worker',ROOT/'scripts/nm-breeze-audio.py')
        worker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(worker)
        if worker.busy():
            raise RuntimeError('Shared model slot occupied')
        out = QUEUE/'residual-review-v1'
        if (out/'asr-attempt.json').exists():
            raise RuntimeError('Preserve bounded existing attempt; no blind repeat')
        record_path = out/'record.json'
        record_sha = sha(record_path)
        record = json.loads(record_path.read_text())
        model_id = 'mlx-community/whisper-large-v3-turbo-asr-fp16'
        ref = Path(os.environ['HF_HUB_CACHE'])/('models--'+model_id.replace('/','--'))/'refs/main'
        revision = ref.read_text().strip()
        if not re.fullmatch('[a-f0-9]{40}',revision):
            raise RuntimeError('Invalid cached revision')
        save(out/'asr-attempt.json',{'state':'exact-edition-context-ASR-running',
            'recordSha256':record_sha,'model':model_id,'modelRevision':revision,
            'pid':os.getpid(),'published':False,'ownerListening':'pending'})
        from mlx_audio.stt.generate import generate_transcription
        from mlx_audio.stt.utils import load_model
        model = load_model(model_id)
        (out/'asr').mkdir(exist_ok=True)
        results = []
        for item in record['items']:
            wav = Path(item['clipPath'])
            if sha(wav) != item['clipSha256']:
                raise RuntimeError('Review clip changed')
            stem = out/'asr'/item['id']
            result = generate_transcription(model=model,audio=str(wav),output_path=str(stem),
                 format='json',language='en',word_timestamps=True,verbose=False)
            pieces = getattr(result,'segments',None) or []
            transcript = ' '.join(str(p.get('text','')).strip() for p in pieces).strip() or result.text
            expected,actual = words(item['expectedScoreText']),words(transcript)
            matcher = difflib.SequenceMatcher(a=expected,b=actual,autojunk=False)
            changes = [{'operation':tag,'expected':' '.join(expected[i:j]),'actual':' '.join(actual[k:l])}
                for tag,i,j,k,l in matcher.get_opcodes() if tag!='equal']
            results.append({'id':item['id'],'edition':item['edition'],
                'sourceSha256':item['sourceSha256'],'chapterAudioSha256':item['chapterAudioSha256'],
                'clipSha256':item['clipSha256'],'takeBindings':item['takeBindings'],
                'expected':item['expectedScoreText'],'transcript':transcript,
                'normalizedExactMatch':expected==actual,'changes':changes})
            save(out/'asr-progress.json',{'complete':False,'items':results})
            print(item['id'],'context decoded; supervisor review pending',flush=True)
        if sha(record_path) != record_sha or ref.read_text().strip() != revision or any(
                sha(Path(x['clipPath'])) != x['clipSha256'] for x in record['items']):
            raise RuntimeError('Frozen inputs/revision changed during screening')
        save(out/'asr-review.json',{'state':'exact-edition-context-screened-review-pending',
            'recordSha256':record_sha,'model':model_id,'modelRevision':revision,'items':results,
            'published':False,'ownerListening':'pending',
            'note':'Fresh context of actual selected v1/v2 neighbors, not human listening, proven audible defects or automatic repair/acceptance'})


if __name__ == '__main__':
    main()
