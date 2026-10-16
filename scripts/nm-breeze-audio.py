#!/usr/bin/env python3
"""Render prepared National Measure chapters and publish each immediately.

Preparation is a separate Codex reading/direction task. This worker never invents
direction, changes manuscript words, or marks owner listening complete.
"""
from __future__ import annotations

import base64
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.request

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-2680-national-measure"
QUEUE = BOOK / "narration/breeze"
PYTHON = Path('/Users/drive/.local/share/monroe-tts/breeze/venv/bin/python')
RENDER = Path('/Users/drive/.local/share/monroe-tts/meridian-run/breeze_render_track.py')
BOOK_ID = 'kindling-2680-book-02'
RENDER_ID = 'local-breeze-directors-cut-audition'
QA_PYTHON = Path('/Users/drive/.local/share/monroe-tts/venv/bin/python')
QA_SCRIPT = Path('/Users/drive/boundary-universe/scripts/verify-local-tts.py')
QA_CACHE = '/Volumes/Drive 2/monroe-ai/huggingface'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(path, data):
    temp = path.with_suffix(path.suffix + '.pending')
    temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    temp.replace(path)


def log(message):
    line = f'{dt.datetime.now(dt.timezone.utc).isoformat()} {message}'
    print(line, flush=True)
    with (QUEUE/'pipeline.log').open('a') as output:
        output.write(line + '\n')


def words(text):
    return re.findall(r"[^\W_]+(?:'[^\W_]+)*", text.lower().replace('’', "'"))


def api(method, endpoint, payload=None):
    cmd = ['gh', 'api', '--method', method, endpoint]
    if payload is not None:
        cmd += ['--input', '-']
    result = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                            text=True, capture_output=True)
    if result.returncode:
        if method == 'GET' and '(HTTP 404)' in result.stderr:
            return None
        raise RuntimeError(result.stderr[-1200:])
    return json.loads(result.stdout)


def get_file(repo, path):
    data = api('GET', f'repos/adobetoby-maker/{repo}/contents/{path}?ref=main')
    if data is None:
        return None, None
    if data.get('content'):
        return base64.b64decode(data['content']), data['sha']
    if data.get('download_url'):
        with urllib.request.urlopen(data['download_url'], timeout=120) as response:
            return response.read(), data['sha']
    raise RuntimeError(f'Contents API did not return bytes: {repo}/{path}')


def put_file(repo, path, data, message, previous_sha=None):
    payload = {'message': message, 'content': base64.b64encode(data).decode(), 'branch': 'main'}
    if previous_sha:
        payload['sha'] = previous_sha
    return api('PUT', f'repos/adobetoby-maker/{repo}/contents/{path}', payload)


def publish(number, source, mp3, duration, report):
    rel = f'audio/{BOOK_ID}/local-breeze-directors-cut/chapter-{number:02d}.mp3'
    audio = mp3.read_bytes()
    # Respect kindling's *.mp3 Git LFS policy without touching the author's index.
    cleaned = subprocess.run(['git', 'lfs', 'clean', rel], input=audio,
                             cwd=ROOT, capture_output=True, check=True).stdout
    if not cleaned.startswith(b'version https://git-lfs.github.com/spec/v1\n'):
        raise RuntimeError('Expected a Git LFS pointer for MP3 publication')
    subprocess.run(['git', 'lfs', 'push', '--object-id', 'origin', sha(audio)],
                   cwd=ROOT, check=True)
    for attempt in range(5):
        old, previous = get_file('kindling', rel)
        if old == cleaned:
            break
        try:
            put_file('kindling', rel, cleaned, f'Add National Measure chapter {number} Breeze listening candidate', previous)
            break
        except RuntimeError:
            if attempt == 4:
                raise
            time.sleep(5)
    render = {
        'render': RENDER_ID,
        'engine': 'Local Breeze TTS 2 8-bit MLX (mlx-community/Breeze-TTS-2-mlx-8bit)',
        'voice': "Original Calder clone · Codex-directed",
        'methodId': 'monroe-1.2.5-ci-breeze-calder-thought-sections',
        'finishState': 'technical-checks-passed-owner-listening-pending',
        'file': rel,
        'url': f'https://media.githubusercontent.com/media/adobetoby-maker/kindling/main/{rel}',
        'bytes': len(audio), 'durationSec': round(duration, 3),
        'sha256': sha(audio), 'sourceSha256': sha(source),
        'note': 'Local Breeze listening candidate. Codex clarity/direction; word-lock and technical decode checks passed. Source and audio hashes recorded. Full perceptual QA and owner listening pending. No waveform time stretching.',
    }
    path = 'public/audio/kindling-manifest.json'
    title = source.decode().splitlines()[0].lstrip('# ').strip()
    for attempt in range(6):
        raw, previous = get_file('boundary-universe', path)
        if raw is None:
            raise RuntimeError('PWA manifest missing; refusing to replace its library')
        manifest = json.loads(raw)
        book = next((b for b in manifest['books'] if b['id'] == BOOK_ID), None)
        if book is None:
            book = {'id': BOOK_ID, 'title': 'The National Measure', 'totalChapters': 48,
                    'renderedChapters': 0, 'chapters': []}
            manifest['books'].append(book)
        chapter = next((c for c in book['chapters'] if c['number'] == number), None)
        if chapter is None:
            chapter = {'number': number, 'title': title,
                       'manuscript': f'books/book-2680-national-measure/manuscript/chapter-{number:02d}.md', 'renders': []}
            book['chapters'].append(chapter)
        chapter['sourceSha256'] = render['sourceSha256']
        chapter['renders'] = [render] + [r for r in chapter.get('renders', []) if r['render'] != RENDER_ID]
        book['chapters'].sort(key=lambda c: c['number'])
        book['renderedChapters'] = sum(bool(c.get('renders')) for c in book['chapters'])
        manifest['generated'] = dt.datetime.now(dt.timezone.utc).isoformat()
        try:
            result = put_file('boundary-universe', path,
                              (json.dumps(manifest, indent=2, ensure_ascii=False)+'\n').encode(),
                              f'Publish National Measure chapter {number} Breeze audio', previous)
            report['pwaCommit'] = result['commit']['sha']
            report['render'] = render
            report['publicationState'] = 'pushed-awaiting-live-verification'
            return
        except RuntimeError:
            if attempt == 5:
                raise
            time.sleep(10)


def busy():
    for name in ['breeze_render_track.py', 'run_fractured.py', 'run_meridian.py',
                 'run-kindled-monroe-1.2.5-ci.py', 'calder-narrator.py', 'render-local-tts.py',
                 'verify-local-tts.py']:
        if subprocess.run(['pgrep', '-f', name], capture_output=True).returncode == 0:
            return True
    return False


def audit_output(number):
    """Screen rendered words, serialized with synthesis; flags are not pickups."""
    directory = QUEUE/f'chapter-{number:02d}'
    publication = directory/'published.json'
    if not publication.exists() or busy():
        return False
    published = json.loads(publication.read_text())
    binding = {'sourceSha256': published['sourceSha256'],
               'audioSha256': published['audioSha256']}
    marker = directory/'asr-audit.json'
    if marker.exists():
        old = json.loads(marker.read_text())
        if all(old.get(k) == v for k, v in binding.items()):
            return False  # including diagnosed failures; supervisor controls retries
    source = BOOK/f'manuscript/chapter-{number:02d}.md'
    audio = directory/f'chapter-{number:02d}.breeze-calder.mp3'
    evidence = {**binding, 'model': 'mlx-community/whisper-large-v3-turbo-asr-fp16',
                'modelRevision': '624c19c9af5603fa73b83bce14d4aeea96156d18',
                'ownerListening': 'pending', 'accentCertification': False,
                'note': 'ASR screening only. Names, numbers and decoder errors require contextual triage; never automatic rerecording or human-listening approval.'}
    try:
        if sha(source.read_bytes()) != binding['sourceSha256'] or sha(audio.read_bytes()) != binding['audioSha256']:
            raise RuntimeError('ASR source/audio differs from published binding')
        audit_dir = directory/'asr'
        audit_dir.mkdir(exist_ok=True)
        stem = f'national-measure-chapter-{number:02d}-{binding["audioSha256"][:12]}'
        alias = audit_dir/f'{stem}.mp3'
        if not alias.exists():
            alias.symlink_to(audio.resolve())
        elif not alias.is_symlink() or alias.resolve() != audio.resolve():
            raise RuntimeError('Refusing to overwrite ASR input alias')
        raw = audit_dir/f'{stem}.comparison.json'
        env = dict(os.environ, HF_HOME=QA_CACHE, HF_HUB_OFFLINE='1',
                   HF_HUB_CACHE=QA_CACHE+'/hub', HUGGINGFACE_HUB_CACHE=QA_CACHE+'/hub')
        log(f'chapter {number}: serialized Whisper output screening starting')
        with (audit_dir/f'{stem}.log').open('a') as output:
            result = subprocess.run([str(QA_PYTHON), str(QA_SCRIPT), str(source),
                                     str(alias), '--output', str(raw)], env=env,
                                    stdout=output, stderr=subprocess.STDOUT, timeout=2400)
        if result.returncode not in (0, 2) or not raw.exists():
            raise RuntimeError(f'Whisper verifier failed ({result.returncode}); inspect ASR log')
        comparison = json.loads(raw.read_text())
        if sha(source.read_bytes()) != binding['sourceSha256'] or sha(audio.read_bytes()) != binding['audioSha256']:
            raise RuntimeError('ASR inputs changed during screening')
        evidence.update(state='screened-review-pending', rawReport=str(raw),
                        rawReportSha256=sha(raw.read_bytes()),
                        orderedWordCoverage=comparison['orderedWordCoverage'],
                        heuristicPass=comparison['pass'],
                        suspiciousOmissions=len(comparison['suspiciousOmissions']),
                        suspiciousAdditions=len(comparison['suspiciousAdditions']))
    except Exception as error:
        evidence.update(state='failed-needs-diagnosis', error=str(error))
    save(marker, evidence)
    log(f'chapter {number}: output screening {evidence["state"]}')
    return True


def audit_backlog():
    for number in range(1, 49):
        if audit_output(number):
            return True
    return False


def process(directory, number):
    source_path = BOOK / f'manuscript/chapter-{number:02d}.md'
    source = source_path.read_bytes()
    track = json.loads((directory/'direction.json').read_text())
    if track.get('sourceSha256') != sha(source):
        raise RuntimeError(f'chapter {number}: direction source is stale; preserve checkpoints and reprepare')
    if track.get('director') != 'Codex':
        raise RuntimeError('Codex reading/direction provenance missing')
    segments = track['segments']
    if words(source.decode()) != words(' '.join(s['text'] for s in segments)):
        raise RuntimeError(f'chapter {number}: spoken word sequence differs from canonical source')
    preparation = json.loads((directory/'preparation-review.json').read_text())
    if not preparation:
        raise RuntimeError('Preparation evidence missing')
    # A PCM-rail warning needs a new take, not gain reduction disguising it.
    # Preserve every accepted checkpoint and allow just one bounded pickup pass.
    for attempt in range(2):
        with (directory/'render.log').open('a') as output:
            subprocess.run([str(PYTHON), str(RENDER), str(directory), 'directed'],
                           stdout=output, stderr=subprocess.STDOUT, check=True)
        flagged = []
        for segment in segments:
            take = directory/'breeze-directed'/f"{segment['id']}.wav"
            audio, rate = sf.read(take, dtype='float32')
            if rate != 24000 or audio.ndim != 1 or not len(audio) or not np.isfinite(audio).all():
                raise RuntimeError(f'Invalid segment waveform: {take.name}')
            if float(np.max(np.abs(audio))) >= 0.9999:
                flagged.append(take)
        if not flagged:
            break
        if attempt == 1:
            raise RuntimeError('Possible clipping remains after one pickup: ' + ', '.join(p.name for p in flagged))
        held = directory/'held-takes'
        held.mkdir(exist_ok=True)
        stamp = time.time_ns()
        for take in flagged:
            take.rename(held/f'{take.stem}.possible-clipping-{stamp}.wav')
        log(f'chapter {number}: preserved {len(flagged)} peak-flagged takes; retrying only those segments')
    parts = []
    peak = 0.0
    for segment in segments:
        audio, rate = sf.read(directory/'breeze-directed'/f"{segment['id']}.wav", dtype='float32')
        if rate != 24000 or audio.ndim != 1 or not np.isfinite(audio).all() or len(audio) == 0:
            raise RuntimeError('Invalid segment waveform')
        peak = max(peak, float(np.max(np.abs(audio))))
        # Five-millisecond fades affect only the join edge; no time stretching.
        fade = min(120, len(audio)//4)
        audio[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
        audio[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
        audio[0] = audio[-1] = 0.0
        parts += [audio, np.zeros(int(24000*segment.get('pauseAfterMs', 650)/1000), dtype=np.float32)]
    joined = np.concatenate(parts)
    if peak >= 0.9999:
        raise RuntimeError(f'Possible clipping (peak {peak}); inspect before publishing')
    wav = directory/f'{directory.name}.edge-faded.wav'
    sf.write(wav, joined, 24000, subtype='PCM_16')
    mp3 = directory/f'chapter-{number:02d}.breeze-calder.mp3'
    subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-ac','1','-c:a','libmp3lame','-b:a','96k',str(mp3)],check=True)
    subprocess.run(['ffmpeg','-v','error','-i',str(mp3),'-f','null','-'],check=True)
    duration = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(mp3)]))
    if sha(source_path.read_bytes()) != sha(source):
        raise RuntimeError('Canonical source changed during synthesis; preserving audio without publishing')
    report = {'sourceSha256': sha(source), 'audioSha256': sha(mp3.read_bytes()),
              'segments': len(segments), 'durationSec': duration,
              'wordsPerMinute': round(len(words(source.decode()))/duration*60, 2),
              'maxSegmentPeak': peak, 'fadeMs': 5, 'wordLock': 'passed',
              'decode': 'passed', 'ownerListening': 'pending', 'perceptualReview': 'pending'}
    save(directory/'technical-review.json', report)
    publish(number, source, mp3, duration, report)
    save(directory/'published.json', report)
    log(f'chapter {number} published to PWA deployment queue ({duration/60:.1f} min)')


def main():
    QUEUE.mkdir(parents=True, exist_ok=True)
    lock = (QUEUE/'worker.lock').open('a')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit('A National Measure audio worker already owns this queue')
    log(f'audio worker started pid={os.getpid()}')
    while True:
        complete = 0
        for number in range(1,49):
            directory = QUEUE/f'chapter-{number:02d}'
            if (directory/'published.json').exists():
                complete += 1
                continue
            if not (directory/'direction.ready').exists() or busy():
                continue
            try:
                log(f'chapter {number}: render/publish starting')
                process(directory, number)
                # Publish immediately; screen in the same serialized owner only
                # after Breeze exits, then catch up one older chapter per unit.
                audit_output(number)
                audit_backlog()
                # Revisit earliest ready chapters after every publication so
                # revised opening pickups do not wait behind the entire book.
                break
            except Exception as error:
                log(f'chapter {number}: {type(error).__name__}: {error}')
                save(directory/'worker-error.json', {'error': str(error), 'time': dt.datetime.now(dt.timezone.utc).isoformat()})
                time.sleep(60)
        if complete == 48:
            if busy() or audit_backlog():
                time.sleep(60)
                continue
            log('all 48 uploads and ASR screening attempts complete; live, flag triage and perceptual checks remain in supervising heartbeat')
            return
        time.sleep(60)


if __name__ == '__main__':
    main()
