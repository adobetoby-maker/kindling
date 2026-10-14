# Kindling 2680, Book Two — *The National Measure* — authorship record

Public byline: **Monroe Jackson**

## Planning checkpoint — 2026-10-12

- Status: **full-book architecture and Movement One packet prepared; no manuscript prose
  drafted.**
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- Intended prose author: Claude Opus 5.5 through the authenticated Anthropic subscription
  CLI. This entry does not claim that model has written prose.
- Book shape: six open-range movements of eight chapters, chapters 1–48, target
  285,000–315,000 words.
- Planning sources: accepted Book One manuscript, `STATE_LEDGER.md`, `BOOK_MAP.md`,
  `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `SERIES_MAP.md`, and `OWNER_BRIEF.md`.
- Movement One packet: `packets/MOVEMENT-001.md`.
- Compiled Movement One prompt: `planning/OPUS-5.5-MOVEMENT-001.prompt.md`, SHA-256
  `d4068109a72505532cab26ba5679edbc8f682d982775aa41766456181d325c80`.
- Movement One packet SHA-256:
  `e54040c90271bf874d43b8c32711a86584399b8173df97352b2cbccb86e7076a`.
- Planning prompts: `planning/OPUS-5.5-PLAN.prompt.md` and
  `planning/OPUS-5.5-PLAN-RUN.prompt.md`.
- Canon rule: Book One's accepted manuscript and ledger govern any disagreement. Planned
  Book Two events become canon only when they survive prose and review.

The first prose run must append the actual runtime-reported model, session identifier,
compiled-prompt hash, packet hash, chapter word counts, viewpoint allocation, continuity
checkpoint, and edition status here. Never infer the actual model from the requested alias.

## Movement One, first draft — 2026-10-13

- Status: **chapters 1–8 drafted in full as one continuous run. First draft. Not reviewed,
  not cold-read, not scored, not repaired, not committed, not published.**
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier
  `claude-opus-5-5`.** This is what the runtime states; it cannot be verified independently
  from inside the session. No subagent, other model, or delegated worker wrote or edited any
  prose or record.
- Session: Claude Code background job `8bd85d7e` (session file
  `8bd85d7e-2945-4e6a-b309-8a8a716cfe8c`); remote session
  `session_011TsUZ3yaVycAwMKd6nDxHb`. Launched by
  `scripts/run-kindling-2680-book-02-movement-001.sh`.
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-001.v2.prompt.md`, SHA-256
  `13a2e2da3a5ad945308256278c027ec42b618929fa7215c202f5c7d6f1e821e2` (matches the launcher's
  expected hash).
- Packet: `packets/MOVEMENT-001.md`, SHA-256
  `2baa0ee03753c0b7cbded232e14a049bebc500fe86450edfed8ed43aceed5ed4` as it stood at the run
  (after the Sonnet 5.5 showrunner pass; the planning checkpoint above records the earlier
  hash).
- Sources read beyond the appended prompt: targeted searches of the Book One manuscript for
  license steps, skins, the reading rigs, lane scoring, Hart's history, the Pryce laundry, and
  Graywater's crew; `universe/NAME_REGISTRY.md`; a collision search for each new minor name.
  Nothing from the research corpus.

### Word counts (whitespace-split, headings included)

| Chapter | Title | Words |
|---|---|---:|
| 1 | Kiva: A Count Already on the Water | 5,827 |
| 2 | Kiva: A Corner Any Warden Could Be | 5,709 |
| 3 | Kiva: In Her Own Copy | 5,563 |
| 4 | Kiva: A Needle with No Scale | 5,464 |
| 5 | Kiva: The Frame Again | 5,652 |
| 6 | Kiva: Seven Columns | 5,741 |
| 7 | Kiva: The Far Edge | 7,358 |
| 8 | Kiva: Under a Captain | 6,994 |
| | **Movement One** | **48,308** |

Forty-six sections; about 1,050 words a section.

### Viewpoint counts (by section)

| Lens | Sections | Words | Share |
|---|---:|---:|---:|
| Kiva Rowan | 41 | 41,526 | 86.0% |
| Rhea Sorn (chapter 7, two sections) | 2 | 2,786 | 5.8% |
| Mara Rowan (chapter 4) | 1 | 1,548 | 3.2% |
| Kellan Renn (chapter 6) | 1 | 1,322 | 2.7% |
| Orla Dane (chapter 2) | 1 | 1,126 | 2.3% |
| **Secondary, total** | 5 | 6,782 | 14.0% |

These are counts, not craft measurements. The formula's sentence-length distribution,
short/long shares, paragraph and scene proxies, readability, progression-vocabulary density
and development cadence were written toward and **have not been measured;** that belongs to
the editorial pass. Known before measurement: the secondary share is one point over the 13%
target, and Rhea's lens is above the 2.5–3.7% band for a single lens.

### Records written with the draft

- `provenance/MOVEMENT-001-CONTINUITY.md` (calendar, state, figures, records, ledgers, new
  names, sixteen departures and items for attention).
- `STATE_LEDGER.md`: a Movement One block appended from the prose as written.
- Corrections made during the run are listed in the checkpoint's section 0. They were
  exact-string fixes of blocking contradictions noticed while drafting, not a review.

### Edition status

No frozen edition exists for Movement One. The working tree is the first draft. Nothing was
committed or pushed by the author, on the launching instruction.
