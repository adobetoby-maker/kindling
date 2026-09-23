# Hobb's Wall Monroe 1.3 substantive pass — summary

Status: **complete and ready for owner review**.

This is the first genuinely substantive Monroe 1.3 pass over the 26 retained
Hobb's Wall chapters in *Kindled — Book One*. Commit `2f42770` remains the frozen
assembly and punctuation-only baseline. The working edition is under
`books/book-01-kindled/revised/`; the original assembly under `chapters/` was
not changed.

## Measured result

| Movement | Compiled chapters | Before | After | Added | Removed | Net |
|---|---|---:|---:|---:|---:|---:|
| A | 09–14 | 19,103 | 19,083 | 86 | 106 | -20 |
| B | 26–33 | 27,419 | 27,437 | 63 | 45 | +18 |
| C | 39–44 | 26,794 | 26,756 | 208 | 246 | -38 |
| D | 45–50 | 24,341 | 24,336 | 117 | 122 | -5 |
| **Total** | **26 chapters** | **97,657** | **97,612** | **474** | **519** | **-45** |

Twenty-two chapters received material prose changes; four strong chapters were
deliberately kept. The near-flat net count does not mean the pass was
word-locked: 474 words were added and 519 were removed or replaced. The pass
used bounded revision rather than expansion for its own sake.

## What changed

- Rebuilt sentences and paragraphs whose action, agency, chronology, or spatial
  sequence could not be understood reliably on one reading or one hearing.
- Corrected counts and clocks: ammunition, hounds, people, bodies, Satori cases,
  training duration, elapsed nights, and family chronology.
- Reconciled the moving-metal Edge with its separately kindled working-edge
  light, including the culvert and final Breach sequence.
- Repaired the Homura explanation, Rook's demonstrated two-door status, and the
  distinction between a Breach creature and Barrel ash yield.
- Preserved the road arithmetic, dry humor, long-breath cadence where it works,
  Milo's sacrifice, grief aftermath, training plants/payoffs, and all outcomes.

## Still unresolved

1. The planned canon explanation for why Rook can use Vera's Satori and Dessa
   can briefly activate it is still intentionally withheld.
2. The compiled-book bible calls Vera `Satori Kess`, while the authoritative
   repository bible and manuscript call her `Vera Kess`. Synchronize the
   compiled context before another automated book pass.
3. `STATE_LEDGER.md` is still a pre-book ledger. Rebuild it from the accepted
   revised edition before Book Two continuity work.

## Gate result

- Frozen `chapters/` changed: **0 files**.
- Unexpected revised chapters changed: **0 files**.
- Narration markup inserted into prose: **none detected**.
- Markdown heading check: **passed**.
- `git diff --check`: **passed**.

Narration preparation remains held. After owner acceptance, create a new
word-locked narration copy from this revised prose; do not reuse the old
punctuation baseline as the spoken source.
