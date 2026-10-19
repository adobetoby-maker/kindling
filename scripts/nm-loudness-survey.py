#!/usr/bin/env python3
"""Hash-bound CPU-only delivery measurements; never modify or approve audio."""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / 'books/book-2680-national-measure/narration/breeze'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--include-unpublished', action='store_true')
    parser.add_argument('--candidate-root', action='store_true',
                        help='Measure the separate local-repair-candidates-v1 editions')
    args = parser.parse_args()
    root = QUEUE/'local-repair-candidates-v1' if args.candidate_root else QUEUE
    for directory in sorted(root.glob('chapter-[0-9][0-9]')):
        pub = directory / 'published.json'
        if not pub.exists() and (args.include_unpublished or args.candidate_root):
            pub = directory / 'technical-review.json'
        audio = directory / f'{directory.name}.breeze-calder.mp3'
        if not pub.exists():
            continue
        binding = json.loads(pub.read_text())
        if args.candidate_root:
            audio = Path(binding['audioPath'])
        if not audio.exists():
            raise RuntimeError(f'{directory.name}: bound audio is missing')
        if pub.name == 'technical-review.json':
            assert binding['wordLock'] == 'passed' and binding['decode'] == 'passed'
        digest = hashlib.sha256(audio.read_bytes()).hexdigest()
        if digest != binding['audioSha256']:
            raise RuntimeError(f'{directory.name}: publication/audio hash mismatch')
        output = directory / 'delivery-loudness.json'
        if output.exists() and json.loads(output.read_text()).get('audioSha256') == digest:
            continue
        result = subprocess.run(
            ['ffmpeg', '-hide_banner', '-nostats', '-i', str(audio),
             '-af', 'ebur128=peak=true:framelog=verbose', '-f', 'null', '-'],
            capture_output=True, text=True, check=True)
        summary = result.stderr.rsplit('Summary:', 1)[-1]
        def number(pattern):
            match = re.search(pattern, summary)
            if not match:
                raise RuntimeError(f'{directory.name}: missing measurement {pattern}')
            return float(match.group(1))
        report = {
            'checkedAt': datetime.now(timezone.utc).isoformat(),
            'sourceSha256': binding['sourceSha256'], 'audioSha256': digest,
            'bindingRecord': pub.name,
            'publicationClaim': 'none; measurement only',
            'bytes': audio.stat().st_size, 'durationSec': binding['durationSec'],
            'tool': 'ffmpeg ebur128=peak=true:framelog=verbose; full decoded MP3',
            'integratedLufs': number(r'I:\s+([-\d.]+) LUFS'),
            'loudnessRangeLu': number(r'LRA:\s+([-\d.]+) LU'),
            'truePeakDbfs': number(r'Peak:\s+([-\d.]+) dBFS'),
            'state': 'measured-delivery-review-pending', 'ownerListening': 'pending',
            'note': 'Measurement only. No normalization, time stretching, publication change, or technical/perceptual approval.'}
        if json.loads(pub.read_text())['audioSha256'] != digest:
            raise RuntimeError(f'{directory.name}: publication changed during measurement')
        output.write_text(json.dumps(report, indent=2) + '\n')
        print(directory.name, report['integratedLufs'], report['truePeakDbfs'], flush=True)


if __name__ == '__main__':
    main()
