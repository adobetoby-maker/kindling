#!/usr/bin/env python3
"""Adapt existing pause verifier to National Measure; measurement, no audio edits."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / 'books/book-2680-national-measure/narration/breeze'
VERIFIER = Path('/Users/drive/boundary-universe/scripts/audit-narration-pauses.py')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(number):
    directory = QUEUE / f'chapter-{number:02d}'
    publication = json.loads((directory / 'published.json').read_text())
    track = json.loads((directory / 'direction.json').read_text())
    mp3 = directory / f'chapter-{number:02d}.breeze-calder.mp3'
    master = directory / f'{directory.name}.edge-faded.wav'
    assert digest(mp3) == publication['audioSha256']
    assert track['sourceSha256'] == publication['sourceSha256']
    segments = []
    for index, segment in enumerate(track['segments']):
        wav = directory / 'breeze-directed' / f"{segment['id']}.wav"
        segments.append({'index': index, 'id': segment['id'], 'text': segment['text'],
                         'wav': str(wav), 'wavSha256': digest(wav),
                         'pauseAfterMs': segment.get('pauseAfterMs', 650)})
    record = {'master': str(master), 'masterSha256': digest(master),
              'sha256': publication['audioSha256'],
              'sourceSha256': publication['sourceSha256'],
              'directionSha256': digest(directory / 'direction.json'),
              'segments': segments}
    path = directory / 'pause-audit-input.json'
    path.write_text(json.dumps(record, indent=2) + '\n')
    subprocess.run([sys.executable, str(VERIFIER), str(path)], check=True)
    report = json.loads(path.with_suffix('.pauses.json').read_text())
    gaps = sorted(x['estimatedTotalGapMs'] for x in report['pauses']
                  if 'estimatedTotalGapMs' in x)
    authored = sum(x['pauseAfterMs'] for x in segments) / 1000
    duration = sf.info(master).duration
    summary = {'sourceSha256': publication['sourceSha256'],
               'audioSha256': publication['audioSha256'],
               'masterSha256': record['masterSha256'],
               'pauseReportSha256': digest(path.with_suffix('.pauses.json')),
               'allInsertedSilenceAndTotalLengthVerified': report['pass'],
               'segments': len(segments), 'authoredSilenceSec': authored,
               'uncompressedDurationSec': duration,
               'authoredSilenceFraction': authored / duration,
               'medianEstimatedJoinGapMs': gaps[len(gaps)//2],
               'p90EstimatedJoinGapMs': gaps[int((len(gaps)-1)*.9)],
               'scope': 'Exact zero inserted silence and total frame count; native edges threshold -50 dB, 10 ms resolution. Not speech coverage, waveform order proof, identity or pacing acceptance.',
               'ownerListening': 'pending'}
    (directory / 'pause-audit-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('chapter', type=int, nargs='?')
    selected = parser.parse_args().chapter
    if selected is not None:
        audit(selected)
    else:
        for number in range(1, 49):
            if (QUEUE / f'chapter-{number:02d}' / 'published.json').exists():
                audit(number)
