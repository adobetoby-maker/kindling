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
