#!/usr/bin/env python3
"""Hash-bound CPU-only delivery measurements; never modify or approve audio."""
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / 'books/book-2680-national-measure/narration/breeze'


def main():
    for directory in sorted(QUEUE.glob('chapter-[0-9][0-9]')):
        pub = directory / 'published.json'
        audio = directory / f'{directory.name}.breeze-calder.mp3'
        if not pub.exists() or not audio.exists():
            continue
        binding = json.loads(pub.read_text())
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
