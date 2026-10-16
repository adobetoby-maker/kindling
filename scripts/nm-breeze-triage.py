#!/usr/bin/env python3
"""Second, isolated ASR view of long-form flags. Never mutates accepted audio."""
import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT/'books/book-2680-national-measure/narration/breeze'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def words(text):
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text.lower().replace('’', "'"))


def targets(track, comparison):
    offset = 0
    ranges = []
    for segment in track['segments']:
        end = offset + len(words(segment['text']))
        ranges.append((offset, end, segment))
        offset = end
    if offset != comparison['expectedWords']:
        raise ValueError('Direction/ASR source token counts differ')
    selected = {}
    for flag in comparison['suspiciousOmissions'] + comparison['suspiciousAdditions']:
        start = flag.get('sourceWordStart', flag.get('sourceWordAfter'))
        end = start + max(1, len(words(flag.get('sourceWords', ''))))
        for left, right, segment in ranges:
            if right > start and left < end:
                selected[segment['id']] = segment
    return list(selected.values())


def main(number):
    from mlx_audio.stt.generate import generate_transcription
    from mlx_audio.stt.utils import load_model
    directory = QUEUE/f'chapter-{number:02d}'
    audit = json.loads((directory/'asr-audit.json').read_text())
    published = json.loads((directory/'published.json').read_text())
    source = ROOT/f'books/book-2680-national-measure/manuscript/chapter-{number:02d}.md'
    audio = directory/f'chapter-{number:02d}.breeze-calder.mp3'
    def check():
        if sha(source) != audit['sourceSha256'] or sha(audio) != audit['audioSha256']:
            raise ValueError('Published ASR inputs changed')
        if any(published[k] != audit[k] for k in ('sourceSha256', 'audioSha256')):
            raise ValueError('Publication binding differs from ASR')
    check()
    raw = Path(audit['rawReport'])
    if sha(raw) != audit['rawReportSha256']:
        raise ValueError('Whole-chapter screening report changed')
    track = json.loads((directory/'direction.json').read_text())
    if track['sourceSha256'] != audit['sourceSha256']:
        raise ValueError('Direction source changed')
    selected = targets(track, json.loads(raw.read_text()))
    model = load_model(audit['model']) if selected else None
    results = []
    for segment in selected:
        wav = directory/'breeze-directed'/f"{segment['id']}.wav"
        digest = sha(wav)
        stem = directory/'asr'/f"isolated-{segment['id']}-{digest[:12]}"
        result = generate_transcription(model=model, audio=str(wav),
                                        output_path=str(stem), format='json',
                                        language='en', word_timestamps=True,
                                        verbose=False)
        pieces = getattr(result, 'segments', None) or []
        transcript = ' '.join(str(p.get('text', '')).strip() for p in pieces).strip() or result.text
        expected, actual = words(segment['text']), words(transcript)
        matcher = difflib.SequenceMatcher(a=expected, b=actual, autojunk=False)
        changes = [{'operation': tag, 'expected': ' '.join(expected[i:j]),
                    'actual': ' '.join(actual[k:l])}
                   for tag, i, j, k, l in matcher.get_opcodes() if tag != 'equal']
        if sha(wav) != digest:
            raise ValueError('Isolated take changed during screening')
        results.append({'id': segment['id'], 'wavSha256': digest,
                        'expected': segment['text'], 'transcript': transcript,
                        'normalizedExactMatch': expected == actual,
                        'changes': changes})
    check()
    report = {k: audit[k] for k in ('sourceSha256', 'audioSha256', 'model', 'modelRevision', 'rawReportSha256')}
    report.update(state='localized-screened-review-pending', segments=results,
                  ownerListening='pending',
                  note='Isolated ASR corroboration, not human listening or automatic pickup authority. Review remaining differences; names/numbers and decoder errors may persist. No audio/source was changed.')
    pending = directory/'asr-isolated-review.json.pending'
    pending.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    pending.replace(directory/'asr-isolated-review.json')


if __name__ == '__main__':
    main(int(sys.argv[1]))
