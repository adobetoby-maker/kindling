#!/usr/bin/env python3
"""Check ASR alignment plausibility against verified authored zero-sample rests."""
import hashlib
import json
from pathlib import Path
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT/'books/book-2680-national-measure/narration/breeze'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    out = QUEUE/'residual-review-v1'
    target = out/'timing-audit.json'
    if target.exists():
        raise RuntimeError('Preserve existing timing audit')
    record_path = out/'record.json'
    record = json.loads(record_path.read_text())
    results = []
    for item in record['items']:
        raw = out/'asr'/f"{item['id']}.json"
        decoded = json.loads(raw.read_text())
        clip = Path(item['clipPath'])
        if sha(clip) != item['clipSha256']:
            raise RuntimeError('Clip changed')
        pcm,rate = sf.read(clip,dtype='int16')
        manifest = json.loads((QUEUE/item['edition']/f"chapter-{item['chapter']:02d}/take-manifest.json").read_text())
        by_id = {t['id']:t for t in manifest['takes']}
        rests,cursor = [],0
        for binding in item['takeBindings']:
            take = by_id[binding['id']]
            if take['sha256'] != binding['sha256']:
                raise RuntimeError('Take binding differs')
            frames = sf.info(take['path']).frames
            count = int(rate*take['pauseAfterMs']/1000)
            left,right = cursor+frames,cursor+frames+count
            if len(pcm[left:right]) != count or pcm[left:right].any():
                raise RuntimeError('Declared inserted rest is not exact zero PCM')
            rests.append({'after':take['id'],'startSec':left/rate,'endSec':right/rate})
            cursor = right
        if cursor != len(pcm):
            raise RuntimeError('Clip layout differs')
        words = [w for s in decoded.get('segments',[]) for w in s.get('words',[])]
        inside = []
        for word in words:
            start,end = float(word['start']),float(word['end'])
            rest = next((r for r in rests if start>=r['startSec'] and end<=r['endSec']),None)
            if rest:
                inside.append({**word,'zeroPcmRestAfter':rest['after']})
        results.append({'id':item['id'],'clipSha256':item['clipSha256'],'rawAsrSha256':sha(raw),
            'verifiedInsertedRests':rests,'totalTimestampedWords':len(words),
            'zeroDurationWords':sum(float(w['end'])<=float(w['start']) for w in words),
            'wordsWhollyAlignedToVerifiedZeroPcm':inside,
            'wordsOutsideClip':[w for w in words if float(w['start'])<0 or float(w['end'])>len(pcm)/rate+.01]})
    target.write_text(json.dumps({'scope':'Decoder alignment plausibility, not proof of every spoken word',
        'recordSha256':sha(record_path),'items':results,'published':False,'ownerListening':'pending',
        'note':'Words aligned to exact zero PCM expose invalid alignments; do not erase transcripts or automatically clear center discrepancies.'},indent=2)+'\n')
    print('Timestamp plausibility audited; no transcript/audio mutation',flush=True)


if __name__ == '__main__':
    main()
