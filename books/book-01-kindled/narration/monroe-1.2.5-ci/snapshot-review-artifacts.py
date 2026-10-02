#!/usr/bin/env python3
"""Snapshot stable Kindled review audio and objective-clearance evidence.

The queue lock makes the queue state and copied file hash one atomic decision.
Mutable jobs are skipped. Objective-cleared jobs additionally receive a release
record bound to the accepted source and audio hashes; all other stable jobs are
copied only as Draft QA Pending listening takes.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone


ROOT = Path("/Users/drive/kindling-repo-stage")
RUN = Path("/Volumes/Drive 2/monroe-ai/productions/kindled-monroe-1.2.5-ci-directed-paced")
QUEUE = RUN / "queue.json"
LOCK = RUN / "queue.lock"
METHOD = "monroe-1.2.5-ci-directed-paced"
AUDIO_ROOT = ROOT / "audio/book-01-kindled" / METHOD
EVIDENCE_ROOT = ROOT / "audio-production/book-01-kindled" / METHOD
STABLE_STATUSES = {"needs-attention", "qa-cleared"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=destination.parent, prefix=f".{destination.name}.", delete=False
    ) as handle:
        temporary = Path(handle.name)
    try:
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_json(payload: dict, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=destination.parent,
        prefix=f".{destination.name}.",
        delete=False,
    ) as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        temporary = Path(handle.name)
    try:
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def duration_seconds(path: Path) -> float:
    output = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    )
    return round(float(output.strip()), 3)


def chapter_title(source: Path, chapter: int) -> str:
    first = source.read_text(encoding="utf-8").splitlines()[0].strip()
    return first.lstrip("#").strip().removeprefix(f"Chapter {chapter} — ").strip()


def copy_evidence(job: dict, narrator: dict, destination: Path) -> dict[str, str]:
    checks = narrator["checks"]
    diagnostics = narrator.get("diagnostics", {})
    narrator_path = Path(job["narratorReport"])
    production_path = narrator_path.with_name(
        narrator_path.name.replace(".narrator.json", ".json")
    )
    sources = {
        "narrator": Path(job["narratorReport"]),
        "verification": Path(checks["words"]["report"]),
        "targetedWords": Path(checks["words"]["targetedReport"]),
        "mastering": Path(checks["mastering"]["report"]),
        "voiceIdentity": Path(checks["identity"]["report"]),
        "naturalness": Path(checks["naturalness"]["report"]),
        "dnsmos": Path(diagnostics["dnsmos"]["report"]),
        "direction": Path(job["direction"]),
        "production": production_path,
    }
    names = {
        "narrator": "narrator.json",
        "verification": "verification.json",
        "targetedWords": "targeted-words.json",
        "mastering": "mastering.json",
        "voiceIdentity": "voice-quality.json",
        "naturalness": "naturalness.json",
        "dnsmos": "dnsmos.json",
        "direction": "direction.json",
        "production": "production.json",
    }
    evidence: dict[str, str] = {}
    for key, source in sources.items():
        if not source.is_file():
            raise RuntimeError(f"missing {key} evidence for chapter {job['chapter']}: {source}")
        target = destination / names[key]
        atomic_copy(source, target)
        evidence[key] = str(target.relative_to(ROOT))
    return evidence


def release_payload(job: dict, narrator: dict, audio: Path, evidence: dict[str, str]) -> dict:
    chapter = job["chapter"]
    checks = narrator["checks"]
    words = checks["words"]
    pacing = checks["pacing"]
    return {
        "schemaVersion": 1,
        "status": "objective-cleared-awaiting-human-listening",
        "publishedAt": datetime.now(timezone.utc).isoformat(),
        "bookId": "book-01-kindled",
        "bookTitle": "Kindled — Book One",
        "chapter": chapter,
        "chapterTitle": chapter_title(Path(job["source"]), chapter),
        "source": str(Path(job["source"]).relative_to(ROOT)),
        "sourceSha256": job["sourceSha256"],
        "audio": str(audio.relative_to(ROOT)),
        "audioSha256": job["audioSha256"],
        "bytes": audio.stat().st_size,
        "durationSec": duration_seconds(audio),
        "writer": {
            "publicAuthor": "Monroe Jackson",
            "authorSeat": "Monroe 1.3 canonical assembly",
            "authorModel": "not recorded",
        },
        "reader": {
            "voice": "Original Calder",
            "engine": "Local Fish Audio S2 Pro 8-bit",
            "model": "mlx-community/fish-audio-s2-pro-8bit",
            "language": "Australian English",
            "pipeline": "Monroe Book Narrator 1.2.5-CI",
            "methodId": METHOD,
            "director": "Codex gpt-5.6-sol",
            "direction": "Codex-directed, Directed-Paced",
            "speechSpeed": "native",
            "timeStretch": False,
            "localOnly": True,
        },
        "pacing": {
            "sentenceLandingMs": 1550,
            "paragraphSpeakerSubjectResetMs": 2100,
            "writtenSceneBreakMs": 2700,
            "preWordPreparationMs": [320, 340],
            "measuredWpm": pacing["actualWpm"],
            "targetWpmRange": [pacing["target"]["minimum"], pacing["target"]["maximum"]],
        },
        "quality": {
            "objectivePass": True,
            "wordEvidence": words.get("adjudication", "whole-chapter objective word check passed"),
            "masteringPass": True,
            "voiceIdentityPass": True,
            "naturalnessPass": True,
            "pacingPass": True,
            "humanListening": "pending",
        },
        "evidence": evidence,
    }


def main() -> None:
    AUDIO_ROOT.mkdir(parents=True, exist_ok=True)
    results = {
        "drafts": [],
        "objectiveCleared": [],
        "skippedMutable": [],
        "skippedHashUnstable": [],
    }
    with LOCK.open("a", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        queue = json.loads(QUEUE.read_text(encoding="utf-8"))
        for job in queue["jobs"]:
            chapter = job["chapter"]
            status = job["status"]
            if status not in STABLE_STATUSES:
                results["skippedMutable"].append(chapter)
                continue
            if not job.get("audio") or not job.get("audioSha256"):
                continue
            source_audio = Path(job["audio"])
            expected_audio_hash = job["audioSha256"]
            if not source_audio.is_file() or sha256(source_audio) != expected_audio_hash:
                results["skippedHashUnstable"].append(chapter)
                continue
            source = Path(job["source"])
            if sha256(source) != job["sourceSha256"]:
                raise RuntimeError(f"chapter {chapter} canonical source hash changed")
            destination_audio = AUDIO_ROOT / f"chapter-{chapter:02d}.mp3"

            release_path = EVIDENCE_ROOT / f"chapter-{chapter:02d}" / "release.json"
            if status != "qa-cleared" and release_path.is_file():
                # A previously accepted review take always wins over a newer draft.
                continue

            atomic_copy(source_audio, destination_audio)
            if sha256(source_audio) != expected_audio_hash or sha256(destination_audio) != expected_audio_hash:
                raise RuntimeError(f"chapter {chapter} audio changed during snapshot")

            if status == "qa-cleared":
                narrator = json.loads(Path(job["narratorReport"]).read_text(encoding="utf-8"))
                if not narrator.get("automatedPass") or narrator.get("audioSha256") != expected_audio_hash:
                    raise RuntimeError(f"chapter {chapter} objective report does not bind accepted audio")
                if narrator.get("sourceSha256") != job["sourceSha256"]:
                    raise RuntimeError(f"chapter {chapter} objective report does not bind canonical source")
                if not all(check.get("pass") for check in narrator["checks"].values()):
                    raise RuntimeError(f"chapter {chapter} has an uncleared objective check")
                if narrator["checks"]["pacing"].get("waveformTimeStretch") is not False:
                    raise RuntimeError(f"chapter {chapter} violates native-speed publication policy")
                evidence_dir = release_path.parent
                evidence = copy_evidence(job, narrator, evidence_dir)
                existing_release = None
                if release_path.is_file():
                    existing_release = json.loads(release_path.read_text(encoding="utf-8"))
                if not (
                    existing_release
                    and existing_release.get("status")
                    == "objective-cleared-awaiting-human-listening"
                    and existing_release.get("sourceSha256") == job["sourceSha256"]
                    and existing_release.get("audioSha256") == expected_audio_hash
                ):
                    atomic_json(
                        release_payload(job, narrator, destination_audio, evidence), release_path
                    )
                results["objectiveCleared"].append(chapter)
            else:
                results["drafts"].append(chapter)
        fcntl.flock(lock, fcntl.LOCK_UN)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
