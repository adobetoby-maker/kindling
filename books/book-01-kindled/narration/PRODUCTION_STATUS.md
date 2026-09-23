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
- That pass is now the recoverable baseline. The owner-authorized substantive
  Monroe 1.3 prose edit is complete across all 26 retained Hobb's Wall chapters:
  474 words added, 519 removed or replaced, net -45. It is awaiting owner
  review before narration is frozen.
- A targeted Monroe 1.3 expansion of Milo's death arc now supersedes the earlier
  text in Chapters 44–48. It adds a net 2,226 words, including a plain spatial
  map of the bridge and water channel, the full crossing and recovery, and the
  practical aftermath. Those chapter hashes changed again and require owner
  review before narration markup or rendering.
- Full production audio is intentionally held until revised chapter hashes are
  frozen. This prevents spending hours rendering prose that is still changing.

## Callable renderer

```bash
python3 books/book-01-kindled/narration/run-kindled-book-one-calder.py --launch
```

The renderer is resumable, keeps large artifacts on Drive 2, never silently
reuses audio after a source hash changes, and leaves every completed chapter at
`awaiting-listening` until the owner hears it.
