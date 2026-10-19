#!/usr/bin/env python3
"""Adapt existing pause verifier to National Measure; measurement, no audio edits."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / 'books/book-2680-national-measure/narration/breeze'
VERIFIER = Path('/Users/drive/boundary-universe/scripts/audit-narration-pauses.py')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(number, unpublished=False):
    directory = QUEUE / f'chapter-{number:02d}'
    binding_path = directory / ('technical-review.json' if unpublished else 'published.json')
    publication = json.loads(binding_path.read_text())
    if unpublished:
        assert publication['wordLock'] == 'passed' and publication['decode'] == 'passed'
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
    # Verify actual waveform order as well as silent gaps. Reproduce only the
    # documented edge edit, allowing a single PCM16 quantization step.
    max_error = 0.0
    with sf.SoundFile(master) as assembled:
        assert assembled.samplerate == 24000 and assembled.channels == 1
        for segment in segments:
            expected, rate = sf.read(segment['wav'], dtype='float32')
            assert rate == 24000 and expected.ndim == 1
            fade = min(120, len(expected)//4)
            expected[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
            expected[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
            expected[0] = expected[-1] = 0.0
            actual = assembled.read(len(expected), dtype='float32')
            assert len(actual) == len(expected)
            error = float(np.max(np.abs(expected - actual)))
            max_error = max(max_error, error)
            if error > 1/32768 + 1e-7:
                raise RuntimeError(f"{directory.name}: waveform order/edit differs at {segment['id']}: {error}")
            assembled.seek(int(rate * segment['pauseAfterMs'] / 1000), whence=1)
        assert assembled.tell() == assembled.frames
    gaps = sorted(x['estimatedTotalGapMs'] for x in report['pauses']
                  if 'estimatedTotalGapMs' in x)
    authored = sum(x['pauseAfterMs'] for x in segments) / 1000
    duration = sf.info(master).duration
    summary = {'sourceSha256': publication['sourceSha256'],
               'bindingRecord': binding_path.name,
               'publicationClaim': 'none; local technical candidate' if unpublished else 'see published.json for current publication state',
               'audioSha256': publication['audioSha256'],
               'masterSha256': record['masterSha256'],
               'pauseReportSha256': digest(path.with_suffix('.pauses.json')),
               'allInsertedSilenceAndTotalLengthVerified': report['pass'],
               'allOrderedTakeWaveformsAndFiveMsFadesVerified': True,
               'maximumPcm16QuantizationDifference': max_error,
               'segments': len(segments), 'authoredSilenceSec': authored,
               'uncompressedDurationSec': duration,
               'authoredSilenceFraction': authored / duration,
               'medianEstimatedJoinGapMs': gaps[len(gaps)//2],
               'p90EstimatedJoinGapMs': gaps[int((len(gaps)-1)*.9)],
               'scope': 'Ordered source-take waveforms plus five-ms fades within one PCM16 quantization step; exact inserted silence and total frame count. Native edges threshold -50 dB, 10 ms resolution. Not spoken-word coverage, identity or pacing acceptance.',
               'ownerListening': 'pending'}
    (directory / 'pause-audit-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('chapter', type=int, nargs='?')
    parser.add_argument('--unpublished', action='store_true')
    args = parser.parse_args()
    selected = args.chapter
    if args.unpublished and selected is None:
        parser.error('--unpublished requires an explicit chapter')
    if selected is not None:
        audit(selected, args.unpublished)
    else:
        for number in range(1, 49):
            if (QUEUE / f'chapter-{number:02d}' / 'published.json').exists():
                audit(number)
