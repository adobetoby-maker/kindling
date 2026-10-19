#!/usr/bin/env python3
"""CPU decoded-silence benchmark; no edits, alignment or perceptual approval."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT/'books/book-2680-national-measure/narration/breeze'
PROFILE = Path('/Users/drive/kindling-repo-stage/books/book-01-kindled/narration/kokoro-guided-calder/profile.production-default.json')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quantile(values, fraction):
    ordered = sorted(values)
    at = (len(ordered)-1)*fraction
    low = int(at)
    return ordered[low]+(ordered[min(low+1,len(ordered)-1)]-ordered[low])*(at-low) if ordered else None


def main():
    out = QUEUE/'pause-benchmark-v1'
    out.mkdir(exist_ok=True)
    if (out/'review.json').exists():
        raise RuntimeError('Preserve frozen benchmark; no blind overwrite')
    profile = json.loads(PROFILE.read_text())
    approved = Path(profile['approvedMaster'])
    if sha(approved) != profile['approvedMasterSha256']:
        raise RuntimeError('Approved master hash changed')
    inputs = [{'label':'approved-Calder-master','path':str(approved),'sha256':sha(approved),
               'sourceWords':None,'note':'Audio hash locked; no assumed source word count from historical path'}]
    for edition, chapter in ((1,39),(2,32),(2,33),(2,48)):
        directory = QUEUE/f'local-repair-candidates-v{edition}'/f'chapter-{chapter:02d}'
        technical = json.loads((directory/'technical-review.json').read_text())
        manifest = json.loads((directory/'take-manifest.json').read_text())
        audio = Path(technical['audioPath'])
        source = ROOT/f'books/book-2680-national-measure/manuscript/chapter-{chapter:02d}.md'
        if sha(source) != technical['sourceSha256'] or sha(audio) != technical['audioSha256']:
            raise RuntimeError('Candidate source/audio changed')
        if hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest() != technical['bindingSha256']:
            raise RuntimeError('Candidate manifest changed')
        inputs.append({'label':f'candidate-v{edition}-chapter-{chapter:02d}',
              'path':str(audio),'sha256':sha(audio),'source':str(source),'sourceSha256':sha(source),
              'sourceWords':len(source.read_text().split()),'wordCountMethod':'whitespace split, including chapter heading',
              'authoredInsertedRestSec':sum(t['pauseAfterMs'] for t in manifest['takes'])/1000})
    results = []
    for item in inputs:
        duration = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
                          '-of','default=noprint_wrappers=1:nokey=1',item['path']],text=True).strip())
        measurements = []
        for db in (-40,-50):
            process = subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',item['path'],
                '-af',f'silencedetect=noise={db}dB:d=0.15','-f','null','-'],capture_output=True,text=True,check=True)
            log = out/f"{item['label']}.{abs(db)}db.log"
            log.write_text(process.stderr)
            intervals, start = [],None
            for match in re.finditer(r'silence_(start|end):\s*([0-9.]+)',process.stderr):
                kind, at = match[1],float(match[2])
                if kind == 'start': start=at
                elif start is not None:
                    intervals.append((start,min(at,duration)))
                    start=None
            if start is not None: intervals.append((start,duration))
            internal = [end-start for start,end in intervals if start>.01 and end<duration-.01]
            silence = sum(end-start for start,end in intervals)
            measurements.append({'thresholdDb':db,'minimumQuietSec':.15,'internalPauseCount':len(internal),
                'internalPauseMedianMs':None if not internal else quantile(internal,.5)*1000,
                'internalPauseP75Ms':None if not internal else quantile(internal,.75)*1000,
                'internalPauseP90Ms':None if not internal else quantile(internal,.9)*1000,
                'detectedQuietSec':silence,'detectedQuietFraction':silence/duration,
                'logSha256':sha(log),
                'nonQuietWordRateProxy':None if item['sourceWords'] is None else item['sourceWords']/(duration-silence)*60})
        if sha(Path(item['path'])) != item['sha256']:
            raise RuntimeError('Input audio changed during measurement')
        results.append({**item,'durationSec':duration,
              'overallWordsPerMinute':None if item['sourceWords'] is None else item['sourceWords']/duration*60,
              'measurements':measurements})
        print(item['label'],'decoded silence measured',flush=True)
    report = {'scope':'Threshold-based decoded quiet, not linguistic pause alignment or actual articulation speed',
         'profileSha256':sha(PROFILE),'profileOverallWpm':profile['targets']['overallWordsPerMinute'],
         'results':results,'published':False,'ownerListening':'pending',
         'limits':['Quiet breaths and low-level speech may be counted; thresholds are not VAD',
                   'Inserted rests differ from native waveform quiet; no attribution from detector alone',
                   'Different books/content; approved source word count intentionally not inferred',
                   'No time stretch, silence removal, audio mutation, pace waiver or approval']}
    (out/'review.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
