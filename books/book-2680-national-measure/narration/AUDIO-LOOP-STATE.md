# National Measure — local Breeze audio loop

## Current phase

Book context preparation for the sixteen accepted chapters. The book remains in
progress; refresh context when later accepted movements land.

- Started the existing `build-book-performance-bible.py` with the complete
  currently available chapters 1–16 and local `qwen3.5:35b-a3b-q4_K_M`.
- This local model creates context summaries and a provisional bible. It is not
  the final performance director. Codex must inspect the bible, read the selected
  three-chapter window, complete the paragraph clarity pass, and direct the score.
- Running command: `python3 -u /Users/drive/kindling-narrator-stage/scripts/build-book-performance-bible.py books/book-2680-national-measure/manuscript books/book-2680-national-measure/narration/performance-bible --model qwen3.5:35b-a3b-q4_K_M --title 'The National Measure' --audience adult`.
- Shell session at launch: `29401`; inspect the actual process and summary files
  before resuming. Summaries are checkpointed by chapter source hash.
- Output directory: `narration/performance-bible/`.
- Follow with `write-book-performance-contexts.py` to create the rolling chapter
  context files. Read and verify their contents against accepted prose before use.
- First narration unit: `monroe-1.2.5/calder/chapters-01-03/run.json`.
- Renderer override: `monroe-1.2.5/calder/chapters-01-03/BREEZE-OVERRIDE.md`.
- Model: local `mlx-community/Breeze-TTS-2-mlx-8bit`; Original Calder clone.
- No Book Two audio rendered yet. No performance-ready marker is authorized until
  Codex's clarity and direction artifacts exist and pass source word-lock checks.

## Shared resources

No Breeze/Fish renderer was running at context-preparation launch. Book One has
preparation directories and four saved prologue segment WAVs. Preserve them.
No Path Given remains deliberately stopped. Do not run a competing MLX renderer.
The local context model is using Metal; unload it after context preparation before
loading the Breeze renderer, so the two jobs do not contend for shared memory.

## Next action

Finish and validate the provisional bible; create contexts; Codex-read and direct
chapters 1–3; compile Breeze segment tracks with silent thought boundaries and
brief edge fades; render checkpointed audio and run technical/coverage checks;
publish each listening candidate to kindling and the PWA. Continue through the
accepted manuscript in rolling three-chapter units as writing progresses.

## Immediate publication loop — 2026-10-15

- Owner reiterated: publish audio immediately after each chapter is ready.
- Context builder completed successfully. The provisional sixteen-chapter bible
  and `narration/contexts/chapter-01.context.md` through chapter 16 are present.
- Codex full-unit clarity/direction task active: prompt
  `narration/DIRECT-OPENING-UNIT.prompt.md`, result
  `narration/DIRECT-OPENING-UNIT.result.md`; shell session `53043`, runtime reported
  `gpt-6.1-sol`, CLI PID 91827 at launch. Rediscover actual process before resuming.
- Render/publish worker active: `scripts/nm-breeze-audio.py`, shell session
  `78406`, PID 12344 at launch. It waits for Codex's word-locked direction.ready
  markers; synthesizes one chapter at a time; adds 5ms zero-edge fades to the
  assembled joins; encodes/decodes; uploads proper Git LFS media to kindling;
  updates the PWA kindling manifest immediately, with no full-book wait.
- Source/PWA publication uses per-file GitHub SHA checks and retry, leaving
  authoring worktrees and other voices untouched. No force updates.
- Each `published.json` records hashes, duration, technical checks and the PWA
  commit. Initial state is pushed-awaiting-live-verification. The supervising
  heartbeat must verify live manifest/audio and record that result.
- No ready audio existed at this update. First three-chapter direction is still
  in progress. Later accepted units remain queued for Codex preparation.

## Heartbeat — opening unit rendering

- Codex opening-unit task completed. All 697 prose paragraphs across chapters
  1–3 were reviewed; per-chapter word-lock, clarity coverage and harness validation
  passed. Inspect `DIRECT-OPENING-UNIT.result.md` and each chapter's
  `preparation-review.json` for exact evidence. One nonblocking headcount query is
  recorded for Writing Monroe; it did not require a spoken-text change.
- The one Breeze worker is actively synthesizing chapter 1. Last checked checkpoint
  was `chapter-01/breeze-directed/s012.wav`; render process PID 25944, supervising
  worker PID 12344. Rediscover rather than trusting those PIDs indefinitely.
- Chapters 2 and 3 have validated direction.ready markers and will follow without
  another owner instruction. No complete chapter recording is published yet.
- The next Codex unit, chapters 4–6, was initialized and launched as shell session
  `97456`; prompt `DIRECT-UNIT-04-06.prompt.md`, result
  `DIRECT-UNIT-04-06.result.md`. It prepares text/direction only and preserves the
  first unit and active render. Check it before launching more preparation.
- Writing showrunner and Movement Three repair are healthy. No intervention or
  duplicate writing/audio worker is required.

## Heartbeat — chapter 1 progressing; next units prepared

- The chapter 1 renderer remains healthy: 181/241 segment WAV checkpoints were
  present at inspection. One worker and one renderer; no complete MP3 yet.
- Chapters 4–6 finished Codex preparation. Independent harness validation passed
  for all 746 paragraph reviews, complete source word locks, and zero blockers.
  They are queued behind chapters 1–3 without a separate owner instruction.
- Chapters 7–9 are now being read/directed: prompt
  `DIRECT-UNIT-07-09.prompt.md`, result `DIRECT-UNIT-07-09.result.md`, shell session
  `66924`. Check this process before launching the next preparation unit.
- Writing: Movement Three is repaired/rechecked and published, bringing accepted
  text to chapters 1–24. Opus Movement Four drafting job `9f1bbf7e` is active under
  Sonnet showrunner `8491a39c`; no duplication or intervention is needed.

## Heartbeat — first chapter uploaded; publication repair

- Chapter 1 rendered: 241 segments, 2,518.7 seconds (41m 58.7s), approximately
  140.57 spoken words/minute. Input word-lock and full MP3 decode passed; peak
  0.98859; 5ms edge fades. Owner/perceptual listen remains pending.
- Upload initially failed because `git lfs clean` accepts a positional path,
  not `--filename`. Fixed the worker and uploaded the existing MP3 without
  regenerating it. Source/audio hashes match the review. The 30,225,357-byte
  public GitHub LFS media download was verified in full against SHA-256
  `1e2564541848a7bfbab01a6bb1cb3a502c34084808e05778e74c3171616dba27`.
- PWA manifest publication commit `3453a07663d160d1fb675dedb37620b619755d7c` is
  deploying. Verify live manifest before notifying first audio availability.
- Preserved the active chapter 2 renderer when replacing only its supervisor.
  New worker PID 29640, shell session 46110; chapter 2 renderer PID 97270.
- Chapter 7 is prepared. Chapters 8–9 are held for located wording issues;
  surgical Opus repair `9ab8514b` is active, prompt
  `planning/OPUS-AUDIO-CLARITY-08-09.prompt.md`. Report expected at
  `provenance/AUDIO-CLARITY-08-09-REPAIR.md`. Verify report/joins, publish exact
  repaired source, refresh prepared hashes and Codex recheck before readiness.
- Chapters 10–12 Codex preparation is active, shell session 53555, prompt
  `DIRECT-UNIT-10-12.prompt.md`, result `DIRECT-UNIT-10-12.result.md`.
