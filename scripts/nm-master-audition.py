#!/usr/bin/env python3
"""One separate two-pass delivery-master experiment; no pace/source/publication edits."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT/'books/book-2680-national-measure'
RECORDS = BOOK/'narration/breeze'
PROFILE = Path('/Users/drive/kindling-repo-stage/books/book-01-kindled/narration/kokoro-guided-calder/profile.production-default.json')
OUT = Path('/Volumes/Drive 2/monroe-ai/national-measure/master-audition-v1')
META = RECORDS/'master-audition-v1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path,data):
    pending = path.with_suffix('.pending')
    pending.write_text(json.dumps(data,indent=2)+'\n')
    pending.replace(path)


def measure(path,filter):
    result = subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',str(path),
                             '-af',filter+':print_format=json','-f','null','-'],
                            capture_output=True,text=True,check=True)
    matches = re.findall(r'\{\s*"input_i".*?\}',result.stderr,re.S)
    if not matches:
        raise RuntimeError('Missing loudness statistics')
    return json.loads(matches[-1])


def main():
    META.mkdir(exist_ok=True)
    OUT.mkdir(parents=True,exist_ok=True)
    if (META/'attempt.json').exists():
        raise RuntimeError('Bounded master audition already attempted; preserve evidence')
    profile = json.loads(PROFILE.read_text())
    approved = Path(profile['approvedMaster'])
    if sha(approved) != profile['approvedMasterSha256']:
        raise RuntimeError('Approved delivery reference changed')
    source = BOOK/'manuscript/chapter-39.md'
    record_path = RECORDS/'local-repair-candidates-v1/chapter-39/technical-review.json'
    record = json.loads(record_path.read_text())
    original,mp3 = Path(record['wavPath']),Path(record['audioPath'])
    if sha(source) != record['sourceSha256'] or sha(mp3) != record['audioSha256'] or record['maxSegmentPeak'] >= .9999:
        raise RuntimeError('Invalid input binding or possible railed source; do not conceal with mastering')
    binding = {'sourceSha256':record['sourceSha256'],'inputAudioSha256':record['audioSha256'],
               'inputWavSha256':sha(original),'profileSha256':sha(PROFILE),
               'approvedMasterSha256':sha(approved),'published':False,'ownerListening':'pending'}
    save(META/'attempt.json',{'state':'one-bounded-master-experiment-running',**binding})
    target = 'loudnorm=I=-20:TP=-3.5:LRA=7'
    approved_stats = measure(approved,target)
    stats = measure(original,target)
    save(META/'measurements-before.json',{'approvedReference':approved_stats,'candidateInput':stats,
                                         'targetIntegratedLufs':-20,'decodedTruePeakLimitDb':-3,
                                         'preEncodeCeilingDb':-3.5})
    filters = target+':'+':'.join(f'{key}={stats[value]}' for key,value in [
        ('measured_I','input_i'),('measured_TP','input_tp'),('measured_LRA','input_lra'),
        ('measured_thresh','input_thresh'),('offset','target_offset')])+':linear=true:print_format=json'
    wav = OUT/'chapter-39.master-audition.wav'
    audio = OUT/'chapter-39.master-audition.mp3'
    if wav.exists() or audio.exists():
        raise RuntimeError('Preserve existing mastering output')
    with (META/'mastering.log').open('a') as log:
        subprocess.run(['ffmpeg','-hide_banner','-nostats','-n','-i',str(original),'-af',filters,
                        '-ar','24000','-ac','1','-c:a','pcm_s16le',str(wav)],stdout=log,stderr=subprocess.STDOUT,check=True)
        before,after = sf.info(original),sf.info(wav)
        if before.frames != after.frames or before.samplerate != after.samplerate:
            raise RuntimeError('Mastering altered sample count/rate; preserve for diagnosis, not acceptance')
        subprocess.run(['ffmpeg','-v','error','-n','-i',str(wav),'-ac','1','-c:a','libmp3lame','-b:a','128k',str(audio)],
                       stdout=log,stderr=subprocess.STDOUT,check=True)
        subprocess.run(['ffmpeg','-v','error','-i',str(audio),'-f','null','-'],check=True,stdout=log,stderr=subprocess.STDOUT)
    if sha(original) != binding['inputWavSha256'] or sha(mp3) != binding['inputAudioSha256'] or sha(source) != binding['sourceSha256']:
        raise RuntimeError('Original input changed during master experiment')
    save(META/'record.json',{'output':str(audio),'targetLufs':-20,'truePeakDb':-3,
                           'sourceSha256':binding['sourceSha256'],'audioSha256':sha(audio),
                           'wavSha256':sha(wav),'frames':after.frames,'sampleRate':after.samplerate,
                           'timeStretch':False,'durationUnchanged':True,**binding})
    verifier = Path('/Users/drive/kindling-narrator-stage/scripts/verify-audio-master.py')
    result = subprocess.run(['/Users/drive/.local/share/monroe-tts/breeze/venv/bin/python',
                             str(verifier),str(META/'record.json'),'--output',str(META/'technical-master.json')])
    if result.returncode not in (0,1) or not (META/'technical-master.json').exists():
        raise RuntimeError('Technical verifier failed unexpectedly')
    save(META/'measurements-after.json',measure(audio,target))
    save(META/'attempt.json',{'state':'master-experiment-complete-review-pending',**binding,
                             'note':'Amplitude mastering only; no source/time/publication change. Coverage, pace, voice and human listening not approved.'})


if __name__ == '__main__':
    main()
