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


def context_targets(track, ids):
    positions = {s['id']: i for i, s in enumerate(track['segments'])}
    if any(s not in positions for s in ids):
        raise ValueError('Context request references an absent segment')
    return [(key, track['segments'][max(0, positions[key]-1):positions[key]+2]) for key in ids]


def main(number, context=False):
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
    request = directory/'asr-context-request.json'
    if context:
        wanted = json.loads(request.read_text())
        if any(wanted[k] != audit[k] for k in ('sourceSha256', 'audioSha256')):
            raise ValueError('Context request is for a different edition')
        groups = context_targets(track, wanted['segmentIds'])
    else:
        groups = [(s['id'], [s]) for s in selected]
    model = load_model(audit['model']) if groups else None
    results = []
    for key, group in groups:
        take_paths = [directory/'breeze-directed'/f"{s['id']}.wav" for s in group]
        takes = [{'id': s['id'], 'sha256': sha(p)} for s, p in zip(group, take_paths)]
        if context:
            import numpy as np
            import soundfile as sf
            parts = []
            for s, path in zip(group, take_paths):
                pcm, rate = sf.read(path, dtype='float32')
                if rate != 24000 or pcm.ndim != 1:
                    raise ValueError('Unexpected contextual take format')
                parts.extend([pcm, np.zeros(int(rate*s.get('pauseAfterMs', 0)/1000), dtype=np.float32)])
            combined = np.concatenate(parts)
            digest = hashlib.sha256(json.dumps(takes, sort_keys=True).encode()).hexdigest()
            wav = directory/'asr'/f'context-{key}-{digest[:12]}.wav'
            sf.write(wav, combined, 24000, subtype='PCM_16')
            expected_text = ' '.join(s['text'] for s in group)
            mode = 'context'
        else:
            wav = take_paths[0]
            digest = takes[0]['sha256']
            expected_text = group[0]['text']
            mode = 'isolated'
        stem = directory/'asr'/f"{mode}-{key}-{digest[:12]}"
        result = generate_transcription(model=model, audio=str(wav),
                                        output_path=str(stem), format='json',
                                        language='en', word_timestamps=True,
                                        verbose=False)
        pieces = getattr(result, 'segments', None) or []
        transcript = ' '.join(str(p.get('text', '')).strip() for p in pieces).strip() or result.text
        expected, actual = words(expected_text), words(transcript)
        matcher = difflib.SequenceMatcher(a=expected, b=actual, autojunk=False)
        changes = [{'operation': tag, 'expected': ' '.join(expected[i:j]),
                    'actual': ' '.join(actual[k:l])}
                   for tag, i, j, k, l in matcher.get_opcodes() if tag != 'equal']
        if any(sha(p) != t['sha256'] for p, t in zip(take_paths, takes)):
            raise ValueError('Isolated take changed during screening')
        results.append({'id': key, 'takeBindings': takes, 'wavSha256': sha(wav),
                        'expected': expected_text, 'transcript': transcript,
                        'normalizedExactMatch': expected == actual,
                        'changes': changes})
    check()
    report = {k: audit[k] for k in ('sourceSha256', 'audioSha256', 'model', 'modelRevision', 'rawReportSha256')}
    report.update(state='context-screened-review-pending' if context else 'localized-screened-review-pending', segments=results,
                  ownerListening='pending',
                  note='Isolated ASR corroboration, not human listening or automatic pickup authority. Review remaining differences; names/numbers and decoder errors may persist. No audio/source was changed.')
    filename = 'asr-context-review.json' if context else 'asr-isolated-review.json'
    if context:
        report['requestSha256'] = sha(request)
    pending = directory/(filename+'.pending')
    pending.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    pending.replace(directory/filename)


if __name__ == '__main__':
    main(int(sys.argv[1]), '--context' in sys.argv[2:])
