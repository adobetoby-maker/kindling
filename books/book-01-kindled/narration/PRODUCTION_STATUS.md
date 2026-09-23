# Kindled Book One narration status

## Locked choices

- Narrator: original Calder HQ.
- Engine lane: local Qwen3-TTS through Monroe Audio.
- Production tempo: 0.90.
- Punctuation timing targets: 450 ms at ordinary commas and 800 ms at
  sentence endings.
- Pause safety: repair alignment and retain native delivery wherever an
  inserted pause would cut speech; added space must be actual silence.
- Direction context: whole-book performance bible plus a rolling
  three-chapter reading window.

## Current state

- 53 chapter sources assembled under `chapters/`.
- 53 recoverable editorial copies under `revised/`.
- 53 chapter performance summaries and 53 narrator contexts complete.
- The book-level performance bible has been corrected to track all three
  protagonists and the actual Meridian convergence.
- The first Hobb's Wall/Toren listening pass is complete: 197 word-locked
  punctuation, capitalization, and paragraph-boundary repairs across the 26
  retained chapters.
- That pass is now the recoverable baseline. The owner has authorized a second,
  substantive Monroe 1.3 prose edit before narration is frozen.
- Full production audio is intentionally held until revised chapter hashes are
  frozen. This prevents spending hours rendering prose that is still changing.

## Callable renderer

```bash
python3 books/book-01-kindled/narration/run-kindled-book-one-calder.py --launch
```

The renderer is resumable, keeps large artifacts on Drive 2, never silently
reuses audio after a source hash changes, and leaves every completed chapter at
`awaiting-listening` until the owner hears it.
