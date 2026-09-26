# Kokoro-Guided Calder — Production Default

This is the owner-approved production default for `Kindled — Book One`,
promoted from the controlled Chapter 1 audition on 2026-09-26.

- Kokoro is a delivery reference only. Its voice is not converted or mixed into
  the final take.
- The final narrator is original Calder, rendered locally with Fish S2 Pro.
- Codex read the book performance bible and Chapters 1–3, then authored the
  sparse scene direction in `chapter-01.performance.json`.
- The Kokoro control measured 222.7 overall WPM. Its useful pause distribution
  is retained: 530 ms median, 670 ms p75, and 900 ms p90.
- The approved Calder Chapter 1 master measures 208.8 WPM. That actual take,
  rather than the earlier theoretical 120–150 WPM range, is now the pace
  authority for this profile.
- Calder is synthesized at native speed. No finished-waveform time stretching
  is permitted.
- Ordinary syntax remains with the TTS engine. Explicit pauses are reserved for
  scene changes, tactical revelations, emphasis, and narrator resets.

Large rendered artifacts live on Drive 2 under:

`/Volumes/Drive 2/monroe-ai/auditions/kindled-book-one-kokoro-guided-calder/`

Use `profile.production-default.json` for new work. Preserve `profile.json` as
the exact profile provenance for the approved Chapter 1 master.
