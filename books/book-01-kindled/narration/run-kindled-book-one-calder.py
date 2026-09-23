#!/usr/bin/env python3
"""Render the 53-chapter Kindled assembly with the proven Calder HQ pipeline.

This is a thin, book-specific adapter around the existing resumable Kindled
Calder renderer. It keeps large production artifacts on Drive 2 and treats the
revised manuscript hash as immutable once a chapter enters the queue.
"""

from __future__ import annotations

import argparse
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import subprocess


SCRIPT = Path(__file__).resolve()
BOOK = SCRIPT.parents[1]
STAGE = Path("/Users/drive/kindling-narrator-stage")
BASE_RUNNER = STAGE / "scripts/run-kindled-calder-refresh.py"
RUN = Path(
    os.environ.get(
        "KINDLED_BOOK_ONE_RUN",
        "/Volumes/Drive 2/monroe-ai/productions/"
        "kindled-book-one-calder-090-450-800-20260923",
    )
)

spec = importlib.util.spec_from_file_location("kindled_calder_refresh", BASE_RUNNER)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load Calder renderer: {BASE_RUNNER}")
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)

refresh.RUN = RUN


def initialize() -> None:
    RUN.mkdir(parents=True, exist_ok=True)
    if (RUN / "queue.json").exists():
        return

    profile = json.loads(refresh.PROFILE.read_text(encoding="utf-8"))
    anchor = STAGE / "public/audio/local/voices/monroe-australian-qwen.wav"
    if refresh.sha(anchor) != profile["referenceSha256"]:
        raise RuntimeError("Original Calder anchor hash mismatch")

    palette = json.loads(
        (
            STAGE
            / "public/audio/local/voices/"
            "monroe-australian-stable-performance-palette.json"
        ).read_text(encoding="utf-8")
    )
    palette.update(
        name=profile["name"], playbackRate=0.9, generationSpeed=1.0, mode="performance"
    )
    for entry in palette["performances"].values():
        entry["referenceAudio"] = str(anchor)
        entry["minVoiceSimilarity"] = 0.84
    refresh.save(RUN / "palette.json", palette)
    refresh.save(RUN / "profile.json", profile)

    coach = json.loads(
        (STAGE / "docs/audio-coaching/calder-delivery-coach.v1.json").read_text(
            encoding="utf-8"
        )
    )
    coach["ownerOverride"] = profile
    coach["directorPrompt"] = list(coach.get("directorPrompt", [])) + [
        "Preserve the standard original Calder identity across all three "
        "viewpoints. Read the supplied rolling window before directing the "
        "chapter. Ordinary commas receive 450 ms and sentence endings 800 ms "
        "in a separate waveform-safe alignment pass after a 0.90 tempo "
        "stretch. Never speak direction labels. Return every temporary "
        "character color to base Calder."
    ]
    refresh.save(RUN / "coach.json", coach)

    jobs = []
    for number in range(1, 54):
        source = BOOK / "revised" / f"chapter-{number:02d}.md"
        context = BOOK / "performance" / f"chapter-{number:02d}.context.md"
        if not source.is_file() or not context.is_file():
            raise RuntimeError(f"Missing revised source or performance context: chapter {number}")
        jobs.append(
            {
                "book": "kindled",
                "chapter": number,
                "source": str(source),
                "sourceSha256": refresh.sha(source),
                "status": "queued",
            }
        )
    refresh.save(
        RUN / "queue.json",
        {
            "profile": profile,
            "created": refresh.now(),
            "title": "Kindled — Book One",
            "jobs": jobs,
            "publication": (
                "not auto-published; objective gates and human listening must clear first"
            ),
        },
    )


def write_context(job: dict, target: Path) -> None:
    number = int(job["chapter"])
    bible = BOOK / "performance/book-performance-bible.md"
    chapter_context = BOOK / "performance" / f"chapter-{number:02d}.context.md"
    parts = [
        bible.read_text(encoding="utf-8"),
        "\n# Chapter-specific performance context\n",
        chapter_context.read_text(encoding="utf-8"),
        "\n# Canonical rolling three-chapter reading window\n",
    ]
    start = max(1, min(number - 1, 51))
    for item in range(start, start + 3):
        chapter = BOOK / "revised" / f"chapter-{item:02d}.md"
        parts.extend(
            [f"\n## Kindled chapter {item}\n", chapter.read_text(encoding="utf-8")]
        )
    parts.append(
        "\nThe manuscript is immutable during this render. Flag unclear wording; "
        "do not rewrite it in audio. Keep Callie, Jab, and Toren distinct by "
        "rhythm and attention while preserving one stable Calder narrator. "
        "Apply written punctuation only at waveform-safe silent boundaries.\n"
    )
    target.write_text("\n".join(parts), encoding="utf-8")


refresh.initialize = initialize
refresh.context = write_context


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--launch", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--retry-attention", action="store_true")
    parser.add_argument(
        "--safe-boundaries",
        action="store_true",
        default=True,
        help="Repair alignment and retain native delivery wherever a pause would cut speech.",
    )
    args = parser.parse_args()
    initialize()

    if args.status:
        queue = json.loads((RUN / "queue.json").read_text(encoding="utf-8"))
        print(
            json.dumps(
                [
                    {
                        "chapter": job["chapter"],
                        "status": job["status"],
                        "error": job.get("error"),
                    }
                    for job in queue["jobs"]
                ],
                indent=2,
            )
        )
        return 0

    if args.launch:
        with (RUN / "worker.log").open("a", encoding="utf-8") as log:
            command = [
                "/usr/bin/caffeinate",
                "-i",
                str(refresh.PYTHON),
                str(SCRIPT),
                "--safe-boundaries",
            ]
            if args.retry_attention:
                command.append("--retry-attention")
            process = subprocess.Popen(
                command,
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
        print(json.dumps({"pid": process.pid, "run": str(RUN), "log": str(RUN / "worker.log")}))
        return 0

    with (RUN / "worker.lock").open("w", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        queue = json.loads((RUN / "queue.json").read_text(encoding="utf-8"))
        if args.retry_attention:
            for job in queue["jobs"]:
                if job["status"] == "needs-attention":
                    job["status"] = "queued"
                    job.pop("error", None)
        completed = 0
        for job in queue["jobs"]:
            if job["status"] not in ("queued", "rendering"):
                continue
            job.update(status="rendering", started=refresh.now())
            refresh.save(RUN / "queue.json", queue)
            try:
                job.update(refresh.produce(job, safe_boundaries=True))
            except Exception as error:
                job.update(status="needs-attention", error=str(error))
                print(f"FAILED chapter {job['chapter']}: {error}", flush=True)
            job["updated"] = refresh.now()
            refresh.save(RUN / "queue.json", queue)
            completed += 1
            if args.limit and completed >= args.limit:
                break
    print("Queue pass finished; objective gates and human listening remain.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
