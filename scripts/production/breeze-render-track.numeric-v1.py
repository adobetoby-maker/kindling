"""Render a direction.json track with Breeze TTS 2 (MLX), cloned Calder reference.

usage: breeze_render_track.py DIR MODE [--first N] [--include-unconfirmed]
  MODE: directed  -> per-segment instruct + directed pauses
        plain     -> no instruct, fixed 650 ms pauses (baseline)
Segments are checkpointed as WAV files so a rerun resumes.
"""
import argparse, json, re, sys, time
from pathlib import Path
import numpy as np
import soundfile as sf
from mlx_audio.tts import load

REF = "/Users/drive/boundary-universe/public/private-benchmarks/voice-workshop/calder/calder-original-source.wav"
REF_TEXT = "The leak was just the announcement. The marriage was the problem. Dale set the wrench down and listened to the old house settle around him."
SR = 24000
LEX = Path("/Users/drive/boundary-universe/docs/audio-coaching/pronunciation-lexicon.v1.json")

ap = argparse.ArgumentParser()
ap.add_argument("dir", type=Path)
ap.add_argument("mode", choices=["directed", "plain"])
ap.add_argument("--first", type=int)
ap.add_argument("--include-unconfirmed", action="store_true")
a = ap.parse_args()

track = json.loads((a.dir / "direction.json").read_text())
segs = track["segments"] if isinstance(track, dict) else track
if a.first:
    segs = segs[: a.first]

entries = json.loads(LEX.read_text())["global"]
prop = a.dir / "lexicon-proposals.json"
if prop.exists():
    p = json.loads(prop.read_text())
    entries += p["entries"] if isinstance(p, dict) and "entries" in p else p
ok = {"owner-confirmed", "test-approved"} | ({"unconfirmed"} if a.include_unconfirmed else set())
entries = [e for e in entries if e.get("status") in ok and e.get("render") and e["render"] != e["written"]]
entries.sort(key=lambda e: -len(e["written"]))


def lex(text):
    for e in entries:
        text = re.sub(rf"(?<!\w){re.escape(e['written'])}(?!\w)", e["render"], text)
    return text


def numeric_frontend(segment):
    """Derived pronunciation of explicit decimals; never edits canonical text."""
    if not segment.get('numericPronunciation'):
        if segment.get('numericRenderText'):
            raise ValueError('Numeric render copy lacks a versioned protocol')
        return segment['text']
    if segment['numericPronunciation'] != 'decimal-digits-v1':
        raise ValueError('Unknown numeric pronunciation protocol')
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    def spell(match):
        raw = match.group()
        return 'twelfth' if raw == '12th' else ' '.join('point' if c == '.' else digits[int(c)] for c in raw)
    expected = re.sub(r'\b12th\b|\b[0-9]+\.[0-9]+\b', spell, segment['text'])
    if segment.get('numericRenderText') != expected:
        raise ValueError('Numeric render copy differs from deterministic value-preserving expansion')
    return expected


model = load("mlx-community/Breeze-TTS-2-mlx-8bit")
seg_dir = a.dir / f"breeze-{a.mode}"
seg_dir.mkdir(exist_ok=True)
parts, words, t0 = [], 0, time.time()
for s in segs:
    f = seg_dir / f"{s['id']}.wav"
    text = lex(numeric_frontend(s))
    if not f.exists():
        kw = dict(text=text, ref_audio=REF, ref_text=REF_TEXT, cfg_scale=4, voice="S0")
        if a.mode == "directed" and s.get("instruct"):
            kw["instruct"] = s["instruct"]
        audio = np.concatenate([np.asarray(r.audio, dtype=np.float32) for r in model.generate(**kw)])
        sf.write(f, audio, SR)
        print(s["id"], f"{len(audio)/SR:.1f}s", flush=True)
    audio, _ = sf.read(f, dtype="float32")
    pause = s.get("pauseAfterMs", 650) if a.mode == "directed" else 650
    parts += [audio, np.zeros(int(SR * pause / 1000), dtype=np.float32)]
    words += len(s["text"].split())

full = np.concatenate(parts)
out = a.dir / f"{a.dir.name}.breeze-{a.mode}.wav"
sf.write(out, full, SR)
dur = len(full) / SR
print(json.dumps(dict(out=str(out), minutes=round(dur / 60, 1), wpm=round(words / dur * 60, 1), gen_min=round((time.time() - t0) / 60, 1))))
