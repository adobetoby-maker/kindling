#!/usr/bin/env python3
"""Second, isolated ASR view of long-form flags. Never mutates accepted audio."""
import difflib
import hashlib
import json
import os
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


def main(number, context=False, unpublished=False, context_request=None, isolated_request=None, candidate_root=None):
    from mlx_audio.stt.generate import generate_transcription
    from mlx_audio.stt.utils import load_model
    production_dir = QUEUE/f'chapter-{number:02d}'
    directory = production_dir
    if candidate_root:
        if Path(candidate_root).resolve() != (QUEUE/'local-repair-candidates-v1').resolve() or context or isolated_request:
            raise ValueError('Candidate mode supports only isolated screening of the separate local repair edition')
        directory = Path(candidate_root)/f'chapter-{number:02d}'
    audit = json.loads((directory/'asr-audit.json').read_text())
    binding_path = directory/'published.json'
    if not binding_path.exists() and (unpublished or candidate_root):
        binding_path = directory/'technical-review.json'
    published = json.loads(binding_path.read_text())
    if binding_path.name == 'technical-review.json' and any(
            published.get(k) != 'passed' for k in ('wordLock', 'decode')):
        raise ValueError('Unpublished candidate lacks word-lock/decode checks')
    source = ROOT/f'books/book-2680-national-measure/manuscript/chapter-{number:02d}.md'
    audio = Path(published['audioPath']) if candidate_root else directory/f'chapter-{number:02d}.breeze-calder.mp3'
    manifest = None
    revision_ref = None
    if candidate_root:
        audit['rawReport'] = str(directory/'asr-comparison.json')
        raw_meta = json.loads(Path(audit['rawReport']).read_text())
        audit['model'] = raw_meta['model']
        audit['modelRevision'] = 'not-recorded-by-candidate-verifier'
        cache = os.environ.get('HF_HUB_CACHE')
        if cache:
            revision_ref = Path(cache)/('models--'+audit['model'].replace('/','--'))/'refs/main'
            if revision_ref.exists():
                revision = revision_ref.read_text().strip()
                if not re.fullmatch(r'[a-f0-9]{40}',revision):
                    raise ValueError('Invalid cached model revision')
                audit['modelRevision'] = revision
            else:
                revision_ref = None
        manifest = json.loads((directory/'take-manifest.json').read_text())
        if hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest() != published['bindingSha256']:
            raise ValueError('Candidate take manifest differs from assembly binding')
        if sha(production_dir/'direction.json') != manifest['directionSha256']:
            raise ValueError('Candidate source score changed')
    def check():
        if revision_ref and revision_ref.read_text().strip() != audit['modelRevision']:
            raise ValueError('Cached model revision changed during screening')
        if sha(source) != audit['sourceSha256'] or sha(audio) != audit['audioSha256']:
            raise ValueError('Published ASR inputs changed')
        if any(published[k] != audit[k] for k in ('sourceSha256', 'audioSha256')):
            raise ValueError('Publication binding differs from ASR')
        current = json.loads(binding_path.read_text())
        if any(current[k] != audit[k] for k in ('sourceSha256', 'audioSha256')):
            raise ValueError('Binding record changed during ASR')
    check()
    raw = Path(audit['rawReport'])
    if sha(raw) != audit['rawReportSha256']:
        raise ValueError('Whole-chapter screening report changed')
    track = json.loads((production_dir/'direction.json').read_text())
    if track['sourceSha256'] != audit['sourceSha256']:
        raise ValueError('Direction source changed')
    selected = targets(track, json.loads(raw.read_text()))
    request = directory/(context_request or isolated_request or 'asr-context-request.json')
    if request.parent != directory or request.suffix != '.json':
        raise ValueError('Context request must be a chapter-local JSON filename')
    if context_request and not re.fullmatch(r'asr-context-request-[a-z0-9-]+\.json', context_request):
        raise ValueError('Named request must use asr-context-request-<name>.json')
    if isolated_request and not re.fullmatch(r'asr-isolated-request-[a-z0-9-]+\.json', isolated_request):
        raise ValueError('Named request must use asr-isolated-request-<name>.json')
    if context or isolated_request:
        wanted = json.loads(request.read_text())
        if any(wanted[k] != audit[k] for k in ('sourceSha256', 'audioSha256')):
            raise ValueError('Context request is for a different edition')
        if context:
            groups = context_targets(track, wanted['segmentIds'])
        else:
            segments = {s['id']:s for s in track['segments']}
            groups = [(key, [segments[key]]) for key in wanted['segmentIds']]
    else:
        groups = [(s['id'], [s]) for s in selected]
    model = load_model(audit['model']) if groups else None
    results = []
    (directory/'asr').mkdir(exist_ok=True)
    manifest_takes = {t['id']:t for t in manifest['takes']} if manifest else None
    for key, group in groups:
        take_paths = [Path(manifest_takes[s['id']]['path']) if manifest_takes else directory/'breeze-directed'/f"{s['id']}.wav" for s in group]
        takes = [{'id': s['id'], 'sha256': sha(p)} for s, p in zip(group, take_paths)]
        if manifest_takes and any(t['sha256'] != manifest_takes[t['id']]['sha256'] for t in takes):
            raise ValueError('Candidate checkpoint changed since assembly')
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
                  bindingRecord=binding_path.name,
                  publicationClaim=False if binding_path.name == 'technical-review.json' else None,
                  ownerListening='pending',
                  note='Isolated ASR corroboration, not human listening or automatic pickup authority. Review remaining differences; names/numbers and decoder errors may persist. No audio/source was changed.')
    filename = 'asr-context-review.json' if context else 'asr-isolated-review.json'
    if context and context_request:
        filename = request.stem.replace('request', 'review')+'.json'
    if isolated_request:
        filename = request.stem.replace('request', 'review')+'.json'
    if context or isolated_request:
        report['requestSha256'] = sha(request)
    pending = directory/(filename+'.pending')
    pending.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    pending.replace(directory/filename)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('chapter', type=int)
    parser.add_argument('--context', action='store_true')
    parser.add_argument('--unpublished', action='store_true')
    parser.add_argument('--context-request')
    parser.add_argument('--isolated-request')
    parser.add_argument('--candidate-root')
    args = parser.parse_args()
    if args.context_request and not args.context:
        parser.error('--context-request requires --context')
    if args.isolated_request and (args.context or args.context_request):
        parser.error('--isolated-request cannot be combined with context mode')
    main(args.chapter, args.context, args.unpublished, args.context_request, args.isolated_request, args.candidate_root)
