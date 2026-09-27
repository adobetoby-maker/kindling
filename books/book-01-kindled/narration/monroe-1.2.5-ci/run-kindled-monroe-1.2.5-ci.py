#!/usr/bin/env python3
"""Codex-direct and locally render Kindled with Directed-Paced Fish/Calder."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from datetime import datetime, timezone


HERE = Path(__file__).resolve().parent
BOOK = HERE.parents[1]
PROFILE = HERE / "profile.json"
COACH = HERE / "director-coach.json"
DIRECTOR = Path("/Users/drive/kindling-narrator-stage/scripts/direct-tts-chapter.py")
RENDERER = Path("/Users/drive/kindling-narrator-stage/scripts/render-calder-narrator.sh")
PALETTE = Path(
    "/Users/drive/.local/share/monroe-tts/anchor-builds/"
    "calder-eleven-original-v1/calder-eleven-15.candidate-palette.json"
)
PYTHON = Path("/Users/drive/.local/share/monroe-tts/venv/bin/python")
RUN = Path(
    os.environ.get(
        "KINDLED_MONROE_CI_RUN",
        "/Volumes/Drive 2/monroe-ai/productions/"
        "kindled-monroe-1.2.5-ci-directed-paced",
    )
)
QUEUE = RUN / "queue.json"
QUEUE_LOCK = RUN / "queue.lock"
METHOD_ID = "monroe-1.2.5-ci-directed-paced"
MODEL = "gpt-5.6-sol"
DIRECTOR_EFFORT = "medium"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def clean_markdown(raw: str) -> str:
    """Mirror the production renderer's spoken-text normalization."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"\n---\s*\n(?:\*?End of Chapter.*)?\Z", "", text, flags=re.I | re.S)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*(?:---+|\*\*\*+|___+)\s*$", "", text, flags=re.M)
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?<!\w)[*_]{1,3}|[*_]{1,3}(?!\w)", "", text)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = re.sub(r"^\s*[-+*]\s+", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def save(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def load_queue() -> dict:
    return json.loads(QUEUE.read_text(encoding="utf-8"))


def initialize() -> None:
    RUN.mkdir(parents=True, exist_ok=True)
    if QUEUE.exists():
        return
    if sha(PROFILE) == "" or not PALETTE.is_file():
        raise RuntimeError("Production profile or Calder palette is missing")
    jobs = []
    for number in range(1, 54):
        source = BOOK / "revised" / f"chapter-{number:02d}.md"
        context = BOOK / "performance" / f"chapter-{number:02d}.context.md"
        if not source.is_file() or not context.is_file():
            raise RuntimeError(f"Missing canonical source/context for chapter {number}")
        jobs.append(
            {
                "chapter": number,
                "source": str(source),
                "sourceSha256": sha(source),
                "context": str(context),
                "contextSha256": sha(context),
                "status": "queued",
            }
        )
    save(
        QUEUE,
        {
            "schemaVersion": 1,
            "book": "Kindled — Book One",
            "process": "Monroe Book Narrator 1.2.5-CI",
            "methodId": METHOD_ID,
            "engine": "mlx-community/fish-audio-s2-pro-8bit",
            "voice": "Original Calder",
            "director": {"provider": "Codex", "model": MODEL, "effort": DIRECTOR_EFFORT},
            "profile": str(PROFILE),
            "profileSha256": sha(PROFILE),
            "palette": str(PALETTE),
            "paletteSha256": sha(PALETTE),
            "modelCachePolicy": "one shared Hugging Face download; one in-memory load per worker",
            "createdAt": now(),
            "publication": "Rolling PWA review publication begins at qa-cleared; owner full listen is still required before Finished",
            "jobs": jobs,
        },
    )


def with_queue_lock(action):
    with QUEUE_LOCK.open("a", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        queue = load_queue()
        result = action(queue)
        save(QUEUE, queue)
        return result


def claim(worker: str, prepare_only: bool = False) -> dict | None:
    def operation(queue: dict) -> dict | None:
        for job in queue["jobs"]:
            eligible = {"queued"} if prepare_only else {"queued", "directed", "needs-pickups"}
            if job["status"] in eligible:
                if job["status"] == "needs-pickups":
                    plan = Path(str(job.get("pickupPlan", "")))
                    if not plan.is_file() or int(job.get("pickupAttempts", 0)) >= 3:
                        continue
                claim_kind = "pickup" if job["status"] == "needs-pickups" else "standard"
                job["status"] = "directing" if job["status"] == "queued" else "rendering"
                job["worker"] = worker
                job["claimedAt"] = now()
                claimed = dict(job)
                claimed["claimKind"] = claim_kind
                return claimed
        return None

    return with_queue_lock(operation)


def update(chapter: int, **changes) -> None:
    def operation(queue: dict) -> None:
        job = next(item for item in queue["jobs"] if item["chapter"] == chapter)
        job.update(changes)
        job["updatedAt"] = now()

    with_queue_lock(operation)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text.lower().replace("’", "'"))


def build_pickup_plan(chapter: int, output: Path, overwrite: bool = False) -> Path:
    """Map objective QA failures back to the smallest cached Fish segments."""
    chapter_dir = output.parent
    plan_path = chapter_dir / f"chapter-{chapter:02d}.pickup-plan.json"
    if plan_path.exists() and not overwrite:
        return plan_path
    record = read_json(output.with_suffix(".json"))
    verification = read_json(output.with_suffix(".verification.json"))
    naturalness = read_json(output.with_suffix(".naturalness.json"))
    identity = read_json(output.with_suffix(".voice-quality.json"))
    profile = read_json(PROFILE)
    ranges: list[tuple[int, int, int]] = []
    cursor = 0
    for item in record.get("segments", []):
        count = len(normalized_words(str(item.get("text", ""))))
        ranges.append((cursor, cursor + count, int(item["index"])))
        cursor += count

    def at(position: int) -> int | None:
        if not ranges:
            return None
        bounded = max(0, min(position, max(0, cursor - 1)))
        return next((index for start, end, index in ranges if start <= bounded < end), ranges[-1][2])

    text_segments: set[int] = set()
    for failure in verification.get("suspiciousOmissions", []):
        start = int(failure.get("sourceWordStart", 0))
        length = max(1, len(normalized_words(str(failure.get("sourceWords", "")))))
        for seg_start, seg_end, index in ranges:
            if seg_start < start + length and start < seg_end:
                text_segments.add(index)
        for position in (start - 1, start + length):
            index = at(position)
            if index is not None:
                text_segments.add(index)
    for failure in verification.get("suspiciousAdditions", []):
        position = int(failure.get("sourceWordAfter", 0))
        for nearby in (position - 1, position):
            index = at(nearby)
            if index is not None:
                text_segments.add(index)

    naturalness_segments = {
        int(item["index"])
        for item in naturalness.get("failures", [])
        if item.get("reason") == "naturalness-outlier"
    }
    floor = float(profile["targets"]["minimumVoiceSimilarity"])
    identity_segments = {
        int(item["index"])
        for item in identity.get("checkedSegments", [])
        if float(item.get("similarity", 1.0)) < floor
    }
    force_segments = sorted(text_segments | naturalness_segments | identity_segments)
    if not force_segments:
        raise RuntimeError(f"Chapter {chapter} failed QA without a segment-level pickup")
    save(
        plan_path,
        {
            "schemaVersion": 1,
            "chapter": chapter,
            "audioStatus": "needs-pickups",
            "preserveAcceptedSegments": True,
            "forceSegments": force_segments,
            "reasons": {
                "textCoverage": sorted(text_segments),
                "naturalnessOutlier": sorted(naturalness_segments),
                "voiceIdentityBelowFloor": sorted(identity_segments),
            },
            "notes": "Regenerate only the listed cached takes, rebuild, and rerun every objective check.",
        },
    )
    return plan_path


def adjudicate_word_evidence(output: Path, report: dict) -> dict:
    """Treat benign ASR substitutions as evidence, while omissions/additions still fail."""
    verification = read_json(output.with_suffix(".verification.json"))
    evidence_pass = (
        not verification.get("suspiciousOmissions")
        and not verification.get("suspiciousAdditions")
        and float(verification.get("orderedWordCoverage", 0.0)) >= 0.94
    )
    if evidence_pass and "words" in report.get("checks", {}):
        report["checks"]["words"]["pass"] = True
        report["checks"]["words"]["adjudication"] = (
            "No suspicious omission or addition; remaining ASR substitutions are non-gating evidence."
        )
    report["automatedPass"] = all(item.get("pass") is True for item in report.get("checks", {}).values())
    report["status"] = "awaiting-listening" if report["automatedPass"] else "needs-pickups"
    save(output.with_suffix(".narrator.json"), report)
    return report


def unique_suffix(text: str, end: int) -> str:
    """Return a unique selector ending exactly at a compiled pause boundary."""
    floor = max(0, end - 360)
    starts = [match.start() for match in re.finditer(r"(?<!\S)\S", text[floor:end])]
    for relative in reversed(starts):
        start = floor + relative
        selector = text[start:end]
        if len(selector) >= 18 and text.count(selector) == 1:
            return selector
    selector = text[floor:end]
    if text.count(selector) != 1:
        raise RuntimeError(f"Could not make a unique pause selector at character {end}")
    return selector


def written_scene_breaks(raw: str, clean: str) -> set[int]:
    positions: set[int] = set()
    marker = re.compile(r"^\s*(?:---+|\*\*\*+|___+)\s*$", re.M)
    for match in marker.finditer(raw):
        prefix = clean_markdown(raw[: match.start()])
        if prefix and clean.startswith(prefix) and len(prefix) < len(clean):
            positions.add(len(prefix))
    return positions


def compile_directed_pacing(source: Path, raw_track: Path, output: Path) -> None:
    raw = source.read_text(encoding="utf-8")
    clean = clean_markdown(raw)
    directed = json.loads(raw_track.read_text(encoding="utf-8"))
    scene_positions = written_scene_breaks(raw, clean)
    paragraph_positions = {
        match.start() for match in re.finditer(r"\n{2,}", clean) if 0 < match.start() < len(clean)
    }
    sentence_positions = set()
    for match in re.finditer(r"[.!?]+[\"'”’]*(?=\s|$)", clean):
        end = match.end()
        if end >= len(clean) or end in paragraph_positions:
            continue
        if clean[end:].startswith("\n\n"):
            continue
        sentence_positions.add(end)

    structural = {position: 1550 for position in sentence_positions}
    structural.update({position: 2100 for position in paragraph_positions})
    structural.update({position: 2700 for position in scene_positions})
    pauses = [
        {
            "after": unique_suffix(clean, position),
            "milliseconds": milliseconds,
            "reason": (
                "Written scene break and full restart."
                if milliseconds == 2700
                else "Prepared paragraph/speaker/subject reset."
                if milliseconds == 2100
                else "Prepared sentence or complete-thought landing."
            ),
        }
        for position, milliseconds in sorted(structural.items())
    ]

    used_preword: set[str] = set()
    preword_count = 0
    for item in directed.get("pauses", []):
        phrase = item.get("before")
        if not phrase or clean.count(phrase) != 1 or phrase in used_preword or preword_count >= 8:
            continue
        position = clean.index(phrase)
        if any(not clean[min(position, other):max(position, other)].strip() for other in structural):
            continue
        used_preword.add(phrase)
        preword_count += 1
        pauses.append(
            {
                "before": phrase,
                "milliseconds": 340 if preword_count % 3 == 0 else 320,
                "reason": item.get("reason", "Codex-selected pre-word preparation."),
                "kind": "pre-word preparation",
            }
        )

    result = dict(directed)
    result["source"] = str(source.resolve())
    result["sourceSha256"] = sha(source)
    result["methodId"] = METHOD_ID
    result["director"] = {
        **directed.get("director", {}),
        "role": "semantic performance direction",
        "pacingCompiler": "Monroe 1.2.5-CI",
    }
    result["pacing"] = {
        "speechSpeed": "native",
        "sentenceLandingMs": 1550,
        "paragraphSpeakerSubjectResetMs": 2100,
        "writtenSceneBreakMs": 2700,
        "preWordPreparationMs": [320, 340],
        "waveformTimeStretch": False,
    }
    result["pauses"] = pauses
    save(output, result)


def direct(job: dict, chapter_dir: Path, log) -> Path:
    chapter = int(job["chapter"])
    raw_track = chapter_dir / f"chapter-{chapter:02d}.codex-raw.performance.json"
    performance = chapter_dir / f"chapter-{chapter:02d}.directed-paced.performance.json"
    started = time.monotonic()
    reusable = False
    if raw_track.exists():
        previous = json.loads(raw_track.read_text(encoding="utf-8"))
        reusable = (
            previous.get("sourceSha256") == job["sourceSha256"]
            and previous.get("director", {}).get("backend") == "codex"
        )
    if not reusable:
        effort = str(job.get("directorEffort", DIRECTOR_EFFORT))
        command = [
            str(PYTHON),
            str(DIRECTOR),
            job["source"],
            str(raw_track),
            "--backend",
            "codex",
            "--model",
            MODEL,
            "--effort",
            effort,
            "--audience",
            "adult",
            "--coach",
            str(COACH),
            "--book-context",
            job["context"],
        ]
        completed = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
        if completed.returncode:
            raise RuntimeError(f"Codex direction failed with exit code {completed.returncode}")
    else:
        print(f"Reuse hash-matched Codex direction: {raw_track}", file=log, flush=True)
    compile_directed_pacing(Path(job["source"]), raw_track, performance)
    update(
        chapter,
        status="directed",
        direction=str(performance),
        directionSha256=sha(performance),
        directionSeconds=round(time.monotonic() - started, 2),
    )
    return performance


def render(job: dict, chapter_dir: Path, performance: Path, log) -> tuple[Path, int, float]:
    chapter = int(job["chapter"])
    output = chapter_dir / f"chapter-{chapter:02d}.calder-directed-paced.mp3"
    command = [
        str(RENDERER),
        job["source"],
        str(output),
        "--engine",
        "fish-s2",
        "--profile",
        str(PROFILE),
        "--performance",
        str(performance),
        "--palette",
        str(PALETTE),
    ]
    if job.get("claimKind") == "pickup":
        plan = read_json(Path(job["pickupPlan"]))
        for index in plan.get("forceSegments", []):
            command.extend(["--force-segment", str(index)])
    started = time.monotonic()
    completed = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
    elapsed = round(time.monotonic() - started, 2)
    if completed.returncode not in {0, 2}:
        raise RuntimeError(f"Fish render failed with exit code {completed.returncode}")
    return output, completed.returncode, elapsed


def worker(name: str, limit: int | None, prepare_only: bool) -> int:
    completed_jobs = 0
    while limit is None or completed_jobs < limit:
        job = claim(name, prepare_only=prepare_only)
        if not job:
            break
        chapter = int(job["chapter"])
        chapter_dir = RUN / f"chapter-{chapter:02d}"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        log_path = chapter_dir / f"worker-{name}.log"
        try:
            if sha(Path(job["source"])) != job["sourceSha256"]:
                raise RuntimeError("Canonical source changed after the queue was initialized")
            with log_path.open("a", encoding="utf-8") as log:
                print(f"[{now()}] worker={name} chapter={chapter}", file=log, flush=True)
                if job["status"] == "directing":
                    performance = direct(job, chapter_dir, log)
                    if prepare_only:
                        completed_jobs += 1
                        continue
                    update(chapter, status="rendering")
                else:
                    performance = Path(job["direction"])
                output, result, render_seconds = render(job, chapter_dir, performance, log)
            report = output.with_suffix(".narrator.json")
            report_payload = json.loads(report.read_text(encoding="utf-8")) if report.exists() else {}
            report_payload = adjudicate_word_evidence(output, report_payload)
            status = "qa-cleared" if report_payload.get("automatedPass") else "needs-pickups"
            pickup_attempts = int(job.get("pickupAttempts", 0))
            pickup_plan: Path | None = None
            if status == "needs-pickups":
                if job.get("claimKind") == "pickup":
                    pickup_attempts += 1
                if pickup_attempts >= 3:
                    status = "needs-attention"
                else:
                    pickup_plan = build_pickup_plan(chapter, output, overwrite=True)
            update(
                chapter,
                status=status,
                audio=str(output),
                audioSha256=sha(output),
                narratorReport=str(report),
                automatedPass=bool(report_payload.get("automatedPass")),
                humanListening="pending",
                renderSeconds=render_seconds,
                pickupAttempts=pickup_attempts,
                pickupPlan=str(pickup_plan) if pickup_plan else job.get("pickupPlan"),
            )
        except Exception as error:
            update(chapter, status="needs-attention", error=str(error), log=str(log_path))
        completed_jobs += 1
    return 0


def status() -> None:
    queue = load_queue()
    counts: dict[str, int] = {}
    for job in queue["jobs"]:
        counts[job["status"]] = counts.get(job["status"], 0) + 1
    print(json.dumps({"run": str(RUN), "counts": counts, "jobs": queue["jobs"]}, indent=2))


def launch_workers(count: int, limit: int | None, prepare_only: bool) -> None:
    processes = []
    for number in range(1, count + 1):
        name = f"w{number}"
        log_path = RUN / f"{name}.launcher.log"
        command = [sys.executable, str(Path(__file__).resolve()), "--worker", name]
        if limit is not None:
            command.extend(["--limit", str(limit)])
        if prepare_only:
            command.append("--prepare-only")
        with log_path.open("a", encoding="utf-8") as log:
            process = subprocess.Popen(
                ["/usr/bin/caffeinate", "-i", *command],
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
        processes.append({"worker": name, "pid": process.pid, "log": str(log_path)})
    print(json.dumps({"run": str(RUN), "workers": processes}, indent=2))


def defer_workers_until_current_renders_finish(count: int) -> None:
    """Keep the queue moving after a bounded concurrency benchmark."""
    log_path = RUN / "deferred-launch.log"
    command = [
        "/usr/bin/caffeinate",
        "-i",
        sys.executable,
        str(Path(__file__).resolve()),
        "--wait-and-launch",
        str(count),
    ]
    with log_path.open("a", encoding="utf-8") as log:
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    print(json.dumps({"pid": process.pid, "log": str(log_path), "workers": count}, indent=2))


def wait_and_launch(count: int) -> None:
    while True:
        queue = load_queue()
        # Start the pickup-capable workers only after the original render-only
        # processes have drained every queued/directed chapter and exited.
        if not any(job["status"] in {"queued", "directed", "directing", "rendering"} for job in queue["jobs"]):
            break
        time.sleep(30)
    launch_workers(count, None, False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--worker")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--launch-workers", type=int, choices=[1, 2])
    parser.add_argument("--defer-workers", type=int, choices=[1, 2])
    parser.add_argument("--wait-and-launch", type=int, choices=[1, 2], help=argparse.SUPPRESS)
    parser.add_argument("--limit-per-worker", type=int)
    parser.add_argument("--retry-attention", action="store_true")
    parser.add_argument("--retry-directing", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--plan-pickups", action="store_true")
    args = parser.parse_args()
    initialize()
    if args.retry_attention:
        def retry(queue: dict) -> None:
            for job in queue["jobs"]:
                if job["status"] == "needs-attention":
                    # Keep a completed direction pass when only Fish rendering
                    # failed. Re-directing would overwrite a repaired cue plan.
                    direction = Path(str(job.get("direction", "")))
                    render_failed = str(job.get("error", "")).startswith("Fish render failed")
                    job["status"] = "directed" if render_failed and direction.is_file() else "queued"
                    if str(job.get("error", "")).startswith("Codex direction failed"):
                        job["directorEffort"] = "low"
                    job.pop("error", None)
        with_queue_lock(retry)
    if args.retry_directing:
        def retry_directing(queue: dict) -> None:
            for job in queue["jobs"]:
                if job["status"] == "directing":
                    job["status"] = "queued"
                    job["directorEffort"] = "low"
                    job.pop("error", None)
        with_queue_lock(retry_directing)
    if args.plan_pickups:
        queue = load_queue()
        for job in queue["jobs"]:
            if job["status"] != "needs-pickups":
                continue
            chapter = int(job["chapter"])
            output = Path(job["audio"])
            try:
                plan = build_pickup_plan(chapter, output)
                update(chapter, pickupPlan=str(plan), pickupAttempts=int(job.get("pickupAttempts", 0)))
            except Exception as error:
                update(chapter, status="needs-attention", error=f"Pickup planning failed: {error}")
    if args.status:
        status()
        return 0
    if args.wait_and_launch:
        wait_and_launch(args.wait_and_launch)
        return 0
    if args.defer_workers:
        defer_workers_until_current_renders_finish(args.defer_workers)
        return 0
    if args.launch_workers:
        launch_workers(args.launch_workers, args.limit_per_worker, args.prepare_only)
        return 0
    return worker(args.worker or "foreground", args.limit, args.prepare_only)


if __name__ == "__main__":
    raise SystemExit(main())
