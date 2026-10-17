#!/usr/bin/env python3
"""Bounded, non-publishing diagnosis of short-input and numeral failures."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT/'books/book-2680-national-measure'
OUT = BOOK/'narration/breeze/diagnostic-short-and-ledger'
MODEL = 'mlx-community/Breeze-TTS-2-mlx-8bit'
REF = '/Users/drive/boundary-universe/public/private-benchmarks/voice-workshop/calder/calder-original-source.wav'
REF_TEXT = 'The leak was just the announcement. The marriage was the problem. Dale set the wrench down and listened to the old house settle around him.'


def save(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare():
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    def spell(match):
        raw = match.group()
        return 'twelfth' if raw == '12th' else ' '.join('point' if c == '.' else digits[int(c)] for c in raw)
    trials = []
    for name, n, ids, numeric in [('short-merged',9,['s253','s254'],False),
                                  ('ledger-spelled',13,['s245'],True)]:
        directory = BOOK/f'narration/breeze/chapter-{n:02d}'
        track = json.loads((directory/'direction.json').read_text())
        source = BOOK/f'manuscript/chapter-{n:02d}.md'
        if sha(source) != track['sourceSha256']:
            raise ValueError('Stale source')
        selected = [s for s in track['segments'] if s['id'] in ids]
        if [s['id'] for s in selected] != ids:
            raise ValueError('Unexpected order/selection')
        original = ' '.join(s['text'] for s in selected)
        text = re.sub(r'\b12th\b|\b[0-9]+\.[0-9]+\b', spell, original) if numeric else original
        trials.append({'name':name,'chapter':n,'sourceSha256':sha(source),
                       'directionSha256':sha(directory/'direction.json'),
                       'segmentIds':ids,'original':original,'text':text,
                       'instruct':selected[0]['instruct'],
                       'transformation':'Explicit numeric spelling, audition only' if numeric else 'Adjacent thought units concatenated in exact original word order'})
    return trials


def render():
    import numpy as np
    import soundfile as sf
    from mlx_audio.tts import load
    OUT.mkdir(parents=True, exist_ok=True)
    trials = prepare()
    # Bind the source/score and complete experimental inputs before inference.
    save(OUT/'inputs.json',trials)
    model = load(MODEL)
    results=[]
    for trial in trials:
        wav=OUT/(trial['name']+'.wav')
        pcm=np.concatenate([np.asarray(r.audio,dtype=np.float32) for r in model.generate(
            text=trial['text'],instruct=trial['instruct'],ref_audio=REF,
            ref_text=REF_TEXT,cfg_scale=4,voice='S0',seed=20261017)])
        sf.write(wav,pcm,24000,subtype='PCM_16')
        results.append({'name':trial['name'],'wavSha256':sha(wav),
                        'durationSec':len(pcm)/24000,'peak':float(np.max(np.abs(pcm))),
                        'nativeSpeed':True,'model':MODEL,'referenceSha256':sha(Path(REF))})
    if prepare()!=trials:
        raise ValueError('Source/score changed during diagnostic render')
    save(OUT/'render.json',results)


def verify():
    import difflib
    from mlx_audio.stt.generate import generate_transcription
    from mlx_audio.stt.utils import load_model
    trials=json.loads((OUT/'inputs.json').read_text())
    if prepare()!=trials:
        raise ValueError('Diagnostic source changed')
    renders=json.loads((OUT/'render.json').read_text())
    model=load_model('mlx-community/whisper-large-v3-turbo-asr-fp16')
    words=lambda t:re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'"))
    reports=[]
    for trial,rendered in zip(trials,renders):
        wav=OUT/(trial['name']+'.wav')
        if sha(wav)!=rendered['wavSha256']:
            raise ValueError('Diagnostic take changed')
        result=generate_transcription(model=model,audio=str(wav),output_path=str(OUT/(trial['name']+'-asr')),
                                      format='json',language='en',word_timestamps=True,verbose=False)
        pieces=getattr(result,'segments',None) or []
        text=' '.join(str(s.get('text','')).strip() for s in pieces).strip() or result.text
        expected,actual=words(trial['text']),words(text)
        changes=[{'operation':tag,'expected':' '.join(expected[i:j]),'actual':' '.join(actual[k:l])}
                 for tag,i,j,k,l in difflib.SequenceMatcher(a=expected,b=actual,autojunk=False).get_opcodes() if tag!='equal']
        reports.append({**rendered,'transcript':text,'changes':changes,'normalizedExactMatch':expected==actual})
    save(OUT/'review.json',{'state':'diagnostic-review-pending','published':False,
                           'ownerListening':'pending','reports':reports,
                           'note':'No production/canon change. Numeric input is a deliberate derived pronunciation audition, not the original word lock. Supervisor review required; ASR is not human listening.'})


if __name__=='__main__':
    {'render':render,'verify':verify}[sys.argv[1]]()
