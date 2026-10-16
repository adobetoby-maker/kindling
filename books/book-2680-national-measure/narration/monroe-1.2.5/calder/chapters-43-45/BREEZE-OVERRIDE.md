# Owner-selected renderer for this run

The owner's completion request selects **local Breeze TTS 2 with Original Calder**.
The generated `run.json` and `book-narrator.prompt.md` were initialized from the
generic Calder registry, whose Fish renderer fields are defaults. Those renderer
fields do not select the engine for this book. Do not launch Fish from them.

Use the workflow's book/three-chapter understanding, paragraph clarity, word-locked
prepared prose, explicit direction and narrator resets. Complete these artifacts
before rendering. A copied source file or a ready marker alone is not evidence
that the direction pass happened.

Adapt the prepared direction to the existing Breeze track format:

- `segments`: ordered `id`, `text`, `instruct`, `pauseAfterMs`.
- Standalone performance notes go to `instruct`, never `text`.
- Keep the approved Calder reference identity, source hashes and checkpoints.
- Native generation; no waveform time stretching.
- Start from meaning-based thought landings; verify measured pacing and silent
  boundaries. Add brief edge fades to failed joins without clipping phonemes.
- One shared MLX renderer at a time; inspect the Book One queue first.

Existing renderer:
`/Users/drive/.local/share/monroe-tts/meridian-run/breeze_render_track.py`.

Model: `mlx-community/Breeze-TTS-2-mlx-8bit`, using the existing shared cache.

Status at initialization: **preparation pending; no Book Two audio rendered**.
Publish technically validated listening candidates progressively with actual
source/audio hashes. Owner listening remains pending until explicitly completed.
