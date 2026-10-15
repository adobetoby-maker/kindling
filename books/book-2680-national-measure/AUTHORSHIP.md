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

## Movement One, consolidated repair — 2026-10-14

- Status: **same-author repair of chapters 1–8, in place. Not rechecked, not cold-read
  after repair, not accepted, not committed, not published.** Chapters 9–16 were not drafted.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier
  `claude-opus-5-5`.** Not independently verifiable from inside the session. No subagent,
  other model or delegated worker wrote or edited any prose or record.
- Session: Claude Code background job `7d93f063` (session
  `7d93f063-6603-4d32-a8ba-8f7d7e5a7141`); remote session `session_01DTjXDzNDrhqaQzUbAQMbjc`.
- Brief: delivered in-session; its text matches `planning/OPUS-5.5-MOVEMENT-001-REPAIR.prompt.md`,
  SHA-256 `e64cce9167e44259832217a4d2d032883be83de33213dac438a84c1e6ac83489`, on inspection.
- Inputs: `provenance/MOVEMENT-001-EDITORIAL-REVIEW.md`, `provenance/MOVEMENT-001-COLD-READ.md`,
  `STATE_LEDGER.md`, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, and chapters 1–8 in full, in that order.
- Scope: ten factual corrections (three month names; Mara's factor count; the Low Lane tally and
  entry, with one knock-on line in ch. 5; Perrin's day count; drum twenty-nine clarified; "three
  nights ago"; Kiva's credit for Perrin's held mark; the last drum on the 24th). Warrant arithmetic
  was thinned in ch. 6 §3 and ch. 8 §4, with the full sum kept at the ch. 8 table. Kellan's
  articulated motive and red-tag count were held back in ch. 6 for ch. 8. Two spatial cues were
  added at the ch. 7 far-edge turn, plus four opening glosses in ch. 1. Seventeen ambiguous causal
  *since* were changed and the heaviest archaic-numeral clusters eased. There was a narration-only
  sentence-length pass in the named sections. No event, outcome, date, ash figure, power limit or
  reserved disclosure was changed.
- Record: `provenance/MOVEMENT-001-REPAIR.md`, with every correction and its evidence,
  before/after metrics, and items deliberately left unchanged.
- Word counts (`wc -w`): 48,308 → **48,243** (ch. 1 5,887; ch. 2 5,709; ch. 3 5,589; ch. 4 5,451;
  ch. 5 5,654; ch. 6 5,587; ch. 7 7,389; ch. 8 6,977).
- Sentence measures (editorial script, all text): mean 8.76 → 8.95; ≤5 words 43.4% → 43.4%;
  ≥40 words 0.5% → 0.8%. Narration in the focus sections: mean 10.9 → 12.9; ≥40 words 1.8% → 4.8%.
  The movement-wide interim direction (mean 11–12, about 35% short) was **not** reached; the
  formula targets were not changed.
- Frozen edition `editions/movement-001-first-draft/` not modified; SHA-256 of all eight files
  verified before and after.
- Known stale records outside this run's write scope: `provenance/MOVEMENT-001-CONTINUITY.md`
  lines 35, 37 and 302 (drum date and Low Lane tally).

## Movement One, targeted recheck and acceptance — 2026-10-14

- Fresh-context targeted verifier: runtime-reported Claude Opus 5.5, job `fa4d3354`,
  remote session `session_01AP25iUkcaVx6RLEQMrjk5p`.
- Report: `provenance/MOVEMENT-001-RECHECK.md`. The factual, clarity, sentence-join,
  ledger, and frozen-edition checks passed except for one surviving ordinal in
  `manuscript/chapter-02.md`: the sixth bag was still called the fifth.
- The one-word defect was corrected (`fifth` → `sixth`) and verified by a diff limited
  to that line. No event, figure, outcome, or word count changed.
- The three stale first-draft continuity entries identified by the repair report were
  reconciled to the surviving manuscript: last drum on the 24th; four bags lost in
  the first six; seventeen thrown and twelve sealed.
- **Movement One is accepted as context for Movement Two.** Repaired chapters 1–8:
  48,243 words. This is an editorial-context acceptance, not publication or narration
  approval.

## Movement Two, first draft — 2026-10-14

- Status: **chapters 9–16 drafted in full as one continuous run. First draft. Not reviewed, not
  cold-read, not scored, not repaired, not committed, not published.** Chapter 17 was not begun.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier
  `claude-opus-5-5`.** This is what the runtime states; it cannot be verified independently from
  inside the session. No subagent, other model, or delegated worker wrote or edited any prose or
  record.
- Session: Claude Code background job `24aca0db` (session
  `24aca0db-e14e-45e1-8594-b6717861c2a3`); remote session `session_01X1ta1csHxE9rYwnpaLtrSi`.
- Brief: delivered in-session. On inspection its text matches
  `planning/OPUS-5.5-MOVEMENT-002.prompt.md`, SHA-256
  `df595a8b757dff58ddd49f035ee5fdb75ad55a259ae1138fab0abfa4fc2ce7a9` (the file carries the movement
  title and the formula source hash `9f97e2f2…30c0b8`). No byte comparison of the delivered text
  was possible.
- Packet: `packets/MOVEMENT-002.md`, SHA-256
  `5dcf56c5a1759de91856fbacb4bddbb2460fef2e358f7cebc93242e7a81971cf`.
- Sources read before drafting: repaired chapters 1–8 in full; `provenance/MOVEMENT-001-CONTINUITY.md`
  (as reconciled); `STATE_LEDGER.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`,
  `SERIES_MAP.md`, `OWNER_BRIEF.md`, the repair report and recheck confirmation (as supplied in the
  brief); targeted searches of the planning prompts for Book One context (the Order of the Even Hand,
  the Sag, the plank, *a crossing* of 2471, the Pit, Jude's door, the casualty reserve). The Book One
  manuscript and `universe/NAME_REGISTRY.md` were not present on this machine; new minor names were
  checked by search against every manuscript, planning and provenance file here. Nothing from the
  research corpus.
- Isolation: the project is not a git repository; work was done in place, as in Movement One.

### Word counts (`wc -w`, headings included)

| Chapter | Title | Words |
|---|---|---:|
| 9 | Kiva: The Near Gap | 8,929 |
| 10 | Kiva: Uphill | 6,233 |
| 11 | Kiva: A Stack with Four Legs | 7,919 |
| 12 | Kiva: A Count Everybody Can Hear | 7,383 |
| 13 | Kiva: In Its Own Right | 7,283 |
| 14 | Kiva: A Voice at the Hem | 6,357 |
| 15 | Kiva: Something Quiet | 8,366 |
| 16 | Kiva: The Even Hand | 7,153 |
| | **Movement Two** | **59,623** |

Sixty-seven sections; about 890 words a section. **The movement is over the 47,500–52,500 working
length by about 7,100 words.** No scene was compressed or padded to meet or exceed it.

### Viewpoint counts (by section)

| Lens | Sections | Words | Share |
|---|---:|---:|---:|
| Kiva Rowan | 63 | 55,562 | 93.2% |
| Anwen Pryce (ch. 10) | 1 | 1,297 | 2.2% |
| Kellan Renn (ch. 12) | 1 | 1,144 | 1.9% |
| Orla Dane (ch. 14) | 1 | 949 | 1.6% |
| Mara Rowan (ch. 16) | 1 | 671 | 1.1% |
| **Secondary, total** | 4 | 4,061 | 6.8% |

These are counts, not craft measurements. **Known before measurement:** Kiva's share is well above
the packet's "near or slightly above 87%," and the cumulative book is now about 90% Kiva; each
secondary lens is below the 2.5–3.7% band; no Rhea lens was used. The formula's sentence-length
distribution, paragraph and scene proxies, readability, progression and combat density, and
development cadence were written toward and **have not been measured;** that belongs to the
editorial pass.

### Recorded plan outcomes

- **Hand to Ember: four crossings** on the Circuit's mast (the 1st, 8th, 15th, 22nd; 0.31, 0.30,
  0.31, 0.30). Four of Orla's six; not certified. The fifth and sixth are entered by the Chair for the
  Saltmere gate mast. No sixth was manufactured.
- **Team book at exit: held 6.23; spoken for about 0.60; uncommitted 5.63. Sealed medical, plain:
  2.0** (0.8 + 1.2 given by the Order, bound "for a hand"). Full ledger in
  `provenance/MOVEMENT-002-CONTINUITY.md` §7.
- Flask license in Seven's own right (the 12th, one remark). Halden License beat Seven six to two
  (the 10th). The hunt at Cowl Edge: 59.2 clean, nothing plain. The dream returned with a fever on
  the ferry (the 27th); nobody new learned of it.

### Records written with the draft

- `provenance/MOVEMENT-002-CONTINUITY.md` (calendar, state, the handed crossing, Coombe's three
  problems, the hunt, ledgers, people, new names, departures).
- `STATE_LEDGER.md`: a Movement Two block appended from the prose as written.
- Corrections made during the run (four exact-string fixes of blocking contradictions) are listed in
  the checkpoint's section 0. They are not a review.

### Edition status

No frozen edition exists for Movement Two. The working tree is the first draft. Nothing was
committed or pushed by the author. The run stops here for movement review.
