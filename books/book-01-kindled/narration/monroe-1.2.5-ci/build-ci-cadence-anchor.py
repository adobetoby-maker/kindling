#!/usr/bin/env python3
"""Build audited Original Calder cadence anchors from cleared Chapter 2 takes."""

from __future__ import annotations

import hashlib
import json
import re
import wave
from pathlib import Path


RUN = Path(
    "/Volumes/Drive 2/monroe-ai/productions/"
    "kindled-monroe-1.2.5-ci-directed-paced"
)
CHAPTER = 2
ANCHORS = (
    {
        "first": 91,
        "last": 98,
        "output": "calder-ci-cadence-v2",
        "purpose": "Slower local native-cadence conditioning after numeric Fish instructions plateaued.",
    },
    {
        "first": 282,
        "last": 294,
        "output": "calder-ci-cadence-v3",
        "purpose": "Slowest dialogue-rich native-cadence conditioning after the slower Calder anchor plateaued.",
    },
)
OUTPUT_ROOT = Path("/Users/drive/.local/share/monroe-tts/anchor-builds")


def digest(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def build_anchor(job: dict, record_path: Path, record: dict, specification: dict) -> dict:
    first = int(specification["first"])
    last = int(specification["last"])
    selected = [
        item for item in record["segments"] if first <= int(item["index"]) <= last
    ]
    expected = list(range(first, last + 1))
    if [int(item["index"]) for item in selected] != expected:
        raise RuntimeError("Cadence source segments are incomplete or out of order")

    parameters: tuple[int, int, int, str, str] | None = None
    frames: list[bytes] = []
    total_frames = 0
    for item in selected:
        wav_path = Path(item["wav"])
        if digest(wav_path) != item["audioSha256"]:
            raise RuntimeError(f"Cadence source segment {item['index']} changed on disk")
        with wave.open(str(wav_path), "rb") as reader:
            current = (
                reader.getnchannels(),
                reader.getsampwidth(),
                reader.getframerate(),
                reader.getcomptype(),
                reader.getcompname(),
            )
            if parameters is None:
                parameters = current
            elif current != parameters:
                raise RuntimeError("Cadence source WAV formats do not match")
            frames.append(reader.readframes(reader.getnframes()))
            total_frames += reader.getnframes()
        channels, sample_width, sample_rate, _, _ = current
        pause_frames = round(sample_rate * int(item["pauseAfterMs"]) / 1000)
        frames.append(b"\0" * pause_frames * channels * sample_width)
        total_frames += pause_frames

    assert parameters is not None
    channels, sample_width, sample_rate, compression, compression_name = parameters
    output = OUTPUT_ROOT / str(specification["output"])
    output.mkdir(parents=True, exist_ok=True)
    anchor = output / f"chapter-02-segments-{first:03d}-{last:03d}.wav"
    with wave.open(str(anchor), "wb") as writer:
        writer.setnchannels(channels)
        writer.setsampwidth(sample_width)
        writer.setframerate(sample_rate)
        writer.setcomptype(compression, compression_name)
        for block in frames:
            writer.writeframes(block)

    transcript = " ".join(str(item["text"]).strip() for item in selected)
    words = len(re.findall(r"\b[\w’'-]+\b", transcript))
    duration = total_frames / sample_rate
    metadata = {
        "schemaVersion": 1,
        "voice": "Original Calder",
        "engine": "Fish Audio S2 Pro",
        "sourceChapter": CHAPTER,
        "sourceChapterStatus": job["status"],
        "sourceChapterAudioSha256": job["audioSha256"],
        "sourceRecord": str(record_path),
        "sourceRecordSha256": digest(record_path),
        "segments": expected,
        "referenceText": transcript,
        "referenceAudio": str(anchor),
        "referenceAudioSha256": digest(anchor),
        "words": words,
        "durationSec": round(duration, 3),
        "wordsPerMinute": round(words * 60 / duration, 2),
        "nativeSpeech": True,
        "waveformTimeStretch": False,
        "purpose": specification["purpose"],
    }
    metadata_path = output / "anchor.json"
    temporary = metadata_path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    temporary.replace(metadata_path)
    return metadata


def main() -> int:
    queue = json.loads((RUN / "queue.json").read_text(encoding="utf-8"))
    job = next(item for item in queue["jobs"] if int(item["chapter"]) == CHAPTER)
    if job["status"] != "qa-cleared" or not job.get("automatedPass"):
        raise RuntimeError("The cadence source chapter is not objectively QA-cleared")
    chapter_dir = RUN / f"chapter-{CHAPTER:02d}"
    record_path = chapter_dir / f"chapter-{CHAPTER:02d}.calder-directed-paced.narrator.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    built = [build_anchor(job, record_path, record, item) for item in ANCHORS]
    print(json.dumps(built, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
