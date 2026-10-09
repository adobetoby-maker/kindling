# Kindling 2680, Book One (title unset) — authorship record

Public byline: **Monroe Jackson**

## Prologue and Movement One — Three Doors

- Status: **drafted (prologue + chapters 1–8), 2026-10-09. Stopped for movement review.
  No editorial pass, scoring gate, or repair has been run on the prose.**
- Seat: Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment. Every manuscript sentence was written by this model in one
  authoring session (Claude Code, background job). No subagents were used and no other
  model wrote, revised, or summarized prose.
- Provider: Anthropic, via Claude Code
- Compiled prompt: `planning/OPUS-5.5-PROLOGUE-MOVEMENT-001.prompt.md`
  (SHA-256 `4277990451319ec4542b2600d14863a5191a6bc7a002cdaa6cd068da78b181f1`), read in full
  before drafting
- Movement packet: `packets/MOVEMENT-001.md`
  (SHA-256 `6f421a1e247043a1beb7a63044ed17ecd44abd92c30308dfc94a5c2c83b09b15`)
- Prologue plan: `PROLOGUE_PLAN.md`
  (SHA-256 `0b0995b6c3f94ad9be8f8c27a28f8bb23044812e4c97a57b21c07e688d7b1c32`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (verified before drafting; matches the hash recorded in the compiled prompt)
- Canon read before drafting: `universe/UNIVERSE_BIBLE.md`,
  `books/book-01-kindled/UNIVERSE_BIBLE.md`, Meridian ch. 48 (Senna's crooked-post reason),
  `books/book-03-wellspring/POSTSCRIPT_PLAN.md` §4, and this book's planning files.
- Edition: Book One, Prologue + Movement One, first draft (2026-10-09)
- Branch: `worktree-kindling-2680-prologue-m001-opus55`
- Continuity checkpoint: `provenance/MOVEMENT-001-CONTINUITY.md`
- Prior attempt, not used: an earlier draft of this book's opening exists on branch
  `worktree-kindling-2680-movement-001` (commit `40aeca6`, 2026-10-08), written before the
  current eleven-snapshot plan, the Unroofed Sky lock, and Tamar Vey. It was not read or
  reused in this run.

### Files

| File | Heading | Viewpoint | Words (`wc -w`) |
|---|---|---|---:|
| `manuscript/prologue.md` | Somebody Should Write It Down | eleven dated snapshots, 2080–2676 | 16,089 |
| `manuscript/chapter-01.md` | There Isn't a Column | Kiva | 5,419 |
| `manuscript/chapter-02.md` | A Cell Keeps What You Leave in It | Kiva; Mara cutaway | 4,527 |
| `manuscript/chapter-03.md` | Sequence, Not Stack | Kiva; Orla cutaway | 5,229 |
| `manuscript/chapter-04.md` | The Terrace Ring | Kiva; Kellan cutaway | 5,796 |
| `manuscript/chapter-05.md` | The Cellhouse | Kiva | 5,262 |
| `manuscript/chapter-06.md` | What the Cell Kept | Kiva; Kellan cutaway | 5,497 |
| `manuscript/chapter-07.md` | Fever | Kiva; Anwen cutaway | 4,822 |
| `manuscript/chapter-08.md` | The Lowest Defensible Place | Kiva; Rhea cutaway | 5,560 |
| | | **Movement One total** | **42,112** |

### Post-run measurement (for movement review; not a gate)

Measured on 2026-10-09 with a regex sentence splitter and a heuristic syllable counter
(job-local script, not committed). Dialogue lines count as sentences. Treat as
directional, like the source's own proxies.

| Target (formula) | Goal | Prologue | Movement One |
|---|---|---:|---:|
| Mean sentence length | 14.6 | 8.7 | 8.1 |
| Median sentence length | 11 | 7 | 6 |
| Spread (pstdev) | ~26 | 6.9 | 7.0 |
| Sentences ≤5 words | 27.7% | 39.6% | 47.7% |
| Sentences ≥40 words | 3.3% | 0.2% | 0.3% |
| Paragraph median / mean | 18 / 26.8 | 16 / 26.2 | 15 / 25.9 |
| Words per scene section | ~950 | ~800 | ~626 |
| Flesch Reading Ease | 72.3 | 93.8 | 95.0 |
| Flesch–Kincaid grade | 6.8 | 2.3 | 2.0 |
| Protagonist POV share | ~87% | n/a | 87.2% |
| Secondary share / people | ~13% over 4–5 | n/a | 12.8% over 5 (Kellan 4.1%, Rhea 2.8%, Anwen 2.4%, Orla 2.1%, Mara 1.4%) |
| Progression vocabulary /10k | ~58 (first third ≈1.7×) | 90 | 178 |
| Reporting verbs /10k | ~41 | 100 | 107 |
| -ly adverbs /10k | ~161 (optional) | 29 | 44 |
| "that" /10k | ≤92 | 80 | 63 |
| Combat vocabulary /10k | ~22 | 8 | 49 |
| Development markers /10k (all characters) | 4.5 lead + supporting | 2.5 | 8.6 |

**Material drift, flagged for the editorial pass:** sentence rhythm. The prose is far
more clipped than the formula: mean and median sentence length are roughly half the
target, the short-sentence share is too high, the long-sentence share is about a tenth of
the target, and readability lands near grade 2 instead of 6.8. Paragraph length is close.
Dialogue-tag density is about 2.5× the target. The progression-vocabulary overshoot is
partly intended (front-loaded first sixth of the book) and partly a broad counter. The
focused same-author repair should lengthen and join narrative sentences (especially
interior and expository passages), reduce reporting-verb tags, and lengthen scene
sections, without changing events. Chapter lengths average 5,264 words; at this pace the
book would run about 253,000 words, below `BOOK_MAP.md`'s 270,000–315,000 working range.
The repair pass can recover much of that without padding.

### Choices the owner should review

1. Snapshot 4 is dated 2152, just past the plan's ~2135–2150 range.
2. The 2446 entry in the Transient Register sits inside Hesper Annick's notebook span
   (c. 2446–2450). Only the reader can make that link.
3. Tamar Vey is a former Home Line ward-holder (hand door) with a limp.
4. The Kennel bottle-rift's lattice was impressed by an unnamed Glory master about sixty
   years ago.
5. Kiva's left first two fingers are planted with a temporary numbness that leaves them
   "duller" at exit. Permanent loss is still reserved for Movement 5.
6. Rhea Sorn knew Ilse Corran and recognizes the disk, but keeps that note private.
