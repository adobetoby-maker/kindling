#!/usr/bin/env python3
"""Freeze exact-edition residual listening clips; no production edits or approval."""
import hashlib
import json
from pathlib import Path
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT/'books/book-2680-national-measure'
QUEUE = BOOK/'narration/breeze'
MEDIA = Path('/Volumes/Drive 2/monroe-ai/national-measure/residual-review-v1')
TARGETS = [
    (30,'s113',"purse's/person's"),
    (32,'s044','at/it'),(32,'s046','drams/drums; original-context-only decoder tail'),
    (32,'s091','initial K omission'),
    (33,'s165','no/now'),(33,'s211','I/or in neighboring context only'),
    (33,'s212','seeding/seating'),(33,'s215','and/than'),
    (33,'s216','numeric rank recognition varies; includes punctuation-only candidate'),
    (37,'s038',"I'd/I'm and clause recognition"),(37,'s059',"who/who'd"),
    (37,'s100','I know/oh no'),(37,'s117','article a omission'),(37,'s171','it/him'),
    (41,'s144','a/the'),(47,'s091','the omission'),(47,'s131','extra of'),
    (47,'s149','uncorroborated decoder-tail token'),(48,'s010','crooked/crook'),
    (48,'s012','ledger zero/note-point'),
    (48,'s112','separate candidate identity improved; perceptual judgment pending')]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    out = QUEUE/'residual-review-v1'
    out.mkdir(exist_ok=True)
    MEDIA.mkdir(parents=True,exist_ok=True)
    if (out/'record.json').exists() or any(MEDIA.glob('*.wav')):
        raise RuntimeError('Preserve frozen/partial packet; no blind overwrite')
    chapters = {}
    for number in sorted({n for n,_,_ in TARGETS}):
        edition = 2 if number in (32,33,48) else 1
        directory = QUEUE/f'local-repair-candidates-v{edition}'/f'chapter-{number:02d}'
        technical = json.loads((directory/'technical-review.json').read_text())
        manifest = json.loads((directory/'take-manifest.json').read_text())
        source = BOOK/f'manuscript/chapter-{number:02d}.md'
        score_path = QUEUE/f'chapter-{number:02d}/direction.json'
        score = json.loads(score_path.read_text())
        if sha(source) != technical['sourceSha256'] or sha(score_path) != manifest['directionSha256']:
            raise RuntimeError('Canonical source/score differs from frozen edition')
        if hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest() != technical['bindingSha256']:
            raise RuntimeError('Manifest binding differs')
        master,audio = Path(technical['wavPath']),Path(technical['audioPath'])
        integrity = json.loads((directory/'assembly-integrity.json').read_text())
        if sha(master) != integrity['masterSha256'] or sha(audio) != technical['audioSha256']:
            raise RuntimeError('Frozen candidate master/audio changed')
        if integrity['audioSha256'] != technical['audioSha256']:
            raise RuntimeError('Integrity audit belongs to another edition')
        if [s['id'] for s in score['segments']] != [t['id'] for t in manifest['takes']]:
            raise RuntimeError('Score/manifest order differs')
        cursor = 0
        for take in manifest['takes']:
            info = sf.info(take['path'])
            if info.samplerate != 24000 or info.channels != 1:
                raise RuntimeError('Unexpected take format')
            take['startFrame'] = cursor
            cursor += info.frames+int(24*take['pauseAfterMs'])
            take['endFrame'] = cursor
        if sf.info(master).frames != cursor:
            raise RuntimeError('Frame layout differs from master')
        chapters[number] = (edition,directory,technical,manifest,score,master,integrity)
    rows = []
    for number,key,reason in TARGETS:
        edition,directory,technical,manifest,score,master,integrity = chapters[number]
        index = next(i for i,t in enumerate(manifest['takes']) if t['id']==key)
        takes = manifest['takes'][max(0,index-1):index+2]
        segments = score['segments'][max(0,index-1):index+2]
        if any(sha(Path(t['path'])) != t['sha256'] for t in takes):
            raise RuntimeError('Selected context checkpoint changed')
        start,end = takes[0]['startFrame'],takes[-1]['endFrame']
        name = f'chapter-{number:02d}-{key}'
        clip = MEDIA/f'{name}.wav'
        with sf.SoundFile(master) as input_file:
            input_file.seek(start)
            data = input_file.read(end-start,dtype='int16')
        if len(data) != end-start:
            raise RuntimeError('Truncated context')
        sf.write(clip,data,24000,subtype='PCM_16')
        rows.append({'id':name,'chapter':number,'segmentId':key,'hypothesisNotAudibleProof':reason,
            'edition':f'local-repair-candidates-v{edition}','sourceSha256':technical['sourceSha256'],
            'chapterAudioSha256':technical['audioSha256'],'masterSha256':integrity['masterSha256'],
            'bindingSha256':technical['bindingSha256'],'clipPath':str(clip),'clipSha256':sha(clip),
            'startFrame':start,'endFrame':end,'durationSec':len(data)/24000,
            'centerOffsetSec':(manifest['takes'][index]['startFrame']-start)/24000,
            'takeBindings':[{'id':t['id'],'sha256':t['sha256'],'replacement':t['replacement']} for t in takes],
            'expectedScoreText':'\n\n'.join(s['text'] for s in segments),
            'state':'targeted-review-pending','ownerListening':'pending','published':False})
        print(name,'exact frozen-edition context exported',flush=True)
    # Rehash original masters, not just short clips, after creating the packet.
    for _,_,technical,_,_,master,integrity in chapters.values():
        if sha(master) != integrity['masterSha256'] or sha(Path(technical['audioPath'])) != technical['audioSha256']:
            raise RuntimeError('Chapter input changed during export')
    (out/'record.json').write_text(json.dumps({'scope':'Selected unresolved hypotheses, not exhaustive full-book listen',
        'method':'Lossless contiguous complete checkpoint boundaries including existing authored rests; no new fades or time edits',
        'items':rows,'published':False,'ownerListening':'pending',
        'note':'ASR and identity hypotheses are not proven audible defects or automatic pickup authority'},indent=2)+'\n')


if __name__ == '__main__':
    main()
