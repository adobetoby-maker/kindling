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

## Movement Two, consolidated repair — 2026-10-14

- Status: **same-author repair of chapters 9–16, in place. Not rechecked, not cold-read after
  repair, not accepted, not committed, not published.** Chapter 17 was not drafted.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier
  `claude-opus-5-5`.** This cannot be verified independently from inside the session. No
  subagent, other model or delegated worker wrote or edited any prose or record. No codex or
  OpenAI call was made.
- Session: Claude Code background job `80479656` (session
  `80479656-0763-4f3d-9f66-f2642fb2b403`); remote session `session_01T4x7XmJ1EMJ7Cgi5u6Hx6E`.
- Brief: delivered in-session. On inspection its text matches
  `planning/OPUS-5.5-MOVEMENT-002-REPAIR.prompt.md`, SHA-256
  `fbd07ebfebb72d9e9e73a58eac3a22195ca128266fb69f955a72a9b4793c73b1`.
- Inputs, read in this order: `provenance/MOVEMENT-002-EDITORIAL-REVIEW.md`,
  `provenance/MOVEMENT-002-COLD-READ.md`, `provenance/MOVEMENT-002-CONTINUITY.md`,
  `STATE_LEDGER.md`, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, then chapters 9–16 in full.
  One Book One fact (the hill versus the Pit) was checked against the Book One context in
  `planning/OPUS-5.5-MOVEMENT-001.v2.prompt.md`.
- Scope, in three priorities:
  - **Factual line fixes (seventeen, F1–F17 in the record):**
    - the comb: one "first", now at the Order; Pru blames the thin third
    - Pru's lost sheet and the grey double
    - Jude's five cuts and Pru's four cords
    - the countdown, 19/18
    - six days, a fortnight, and five days
    - "the feeling in two fingers"
    - Hesketh's "two"
    - Aske's colleague and the boot
    - the stray quote in ch. 14
    - the shed step, not the kitchen table
    - the Pit, not the hill
    - "since the autumn"
    - Jude's limp acknowledged
    - "a share" before Vane's weighing
    - one slip that I introduced during the repair and corrected before finishing
  - **Clarity:**
    - "Pit hands" for the people formerly called wards
    - "not a plank", with the unlike pair named
    - the ch. 10 "since" chain made into short sentences
    - the rung rule planted in ch. 10
    - one Coombe line on why a license floor differs from a demonstration
    - Noa's whole reading given before the Chair's sentence
    - fifteen causal "since" recast
    - four point-of-view sections anchored in their first sentence (Kellan's already was)
    - a narration-only sentence pass: about 100 split points in about 90 sentences, and about
      15 joins
  - **Thinning:**
    - "tied a knot" 21 → 7
    - "I'd like it known" returned to Perrin alone (11 → 10)
    - the corner-of-mouth tell kept for Kellan only
    - Vane given his slate instead of "thirty years"
    - "slowly" 39 → 26, "scratched his jaw" 10 → 4, "pale eyes" 8 → 3
    - the ch. 14 van scene opened partway
    - the ch. 16 month reading and Mara's ch. 14 share speech reduced

  No event, outcome, date, ash figure, power limit, injury, knowledge boundary or reserved
  disclosure was changed. Every ledger total is still on the page.
- Record: `provenance/MOVEMENT-002-REPAIR.md`, with every correction and its evidence, the
  before/after metrics, and the items deliberately left unchanged (for example, the open question
  of whether the Pit's mast read the floor).
- Word counts (`wc -w`): 59,623 → **59,234**. By chapter: ch. 9 8,917; ch. 10 6,225; ch. 11 7,891;
  ch. 12 7,350; ch. 13 7,315; ch. 14 6,129; ch. 15 8,375; ch. 16 7,032.
- Sentence measures (`provenance/tools/m2_metrics.py`, SHA-256 prefix `67e20cae24cf`).

  | Measure | Before | After |
  |---|---:|---:|
  | All text: mean | 10.84 | 10.72 |
  | All text: median | 6 | 6 |
  | All text: ≤5 words | 46.0% | 44.6% |
  | All text: ≥40 words | 4.6% | 3.6% |
  | All text: longest sentence | 96 | 78 |
  | Narration: median | 7 | 7 |
  | Narration: ≤5 words | 43.5% | 41.4% |
  | Narration: ≥40 words | 8.0% | 6.2% |

  The editorial waypoint for narration (median 8–9, about 38% short, 3–4% long) was **not**
  reached. The formula targets were not changed. Dialogue was not reshaped; that is pending an
  owner decision.
- Frozen edition `editions/movement-002-first-draft/` was not modified. `SHA256SUMS.txt` was
  verified for all eight files before and after. Chapters 1–8 were not touched.
- Records reconciled to the surviving prose: `provenance/MOVEMENT-002-CONTINUITY.md` (entries
  marked *(repair)*) and the Movement Two block of `STATE_LEDGER.md`.
- **Second repair (same day, job `fdbd4fb4`, runtime-reported `claude-opus-5-5`):** after the
  fresh-context recheck (job `7508774e`), ch. 16 l.135 now reads "in the Pit in the autumn" in place
  of "on a hill in the dark". Two continuity lines were corrected ("new this year" dropped; "two Pit
  hands"). The record is in `provenance/MOVEMENT-002-REPAIR.md` §10. This is not confirmed and not
  accepted.

## Movement Two, targeted recheck, second repair and acceptance — 2026-10-14

- Fresh-context targeted verifier: runtime-reported Claude Opus 5.5 (`claude-opus-5-5`), job `7508774e`
  (session `7508774e-cd8e-49b8-b08c-951d352d2aff`). Prompt
  `planning/OPUS-5.5-MOVEMENT-002-RECHECK.prompt.md`, SHA-256
  `31b5407644c795cb5264f67dce555cee8949e8d75f6b3d92ec77c605fe5b57bc`. Report
  `provenance/MOVEMENT-002-RECHECK.md`: seventeen factual corrections, the clarity edits and every
  changed line checked; one defect found (`manuscript/chapter-16.md:135`).
- Second repair by the same author seat: runtime-reported Claude Opus 5.5, job `fdbd4fb4`
  (session `fdbd4fb4-e073-4ad5-884b-c2c3b3436ee6`), resumed from repair job `80479656`'s context.
  Prompt `planning/OPUS-5.5-MOVEMENT-002-SECOND-REPAIR.prompt.md`, SHA-256
  `4e16ccf8770234538c91b5e18d73a347007790c765270a9f0c95e45770f58fad`. Three edits only.
  Showrunner (Sonnet 5.5) wrote no prose; it wrote the consolidated briefs, launched the children,
  froze the pre-repair edition, and wrote the records.
- First-repair prompt SHA-256 `fbd07ebfebb72d9e9e73a58eac3a22195ca128266fb69f955a72a9b4793c73b1`.
  Frozen first draft: `editions/movement-002-first-draft/` (`SHA256SUMS.txt`, read-only, verified OK).
- Final word count 59,234 (`wc -w`). Final hashes: `provenance/MOVEMENT-002-RECHECK-CONFIRMATION.md`.
- **Movement Two is accepted as editorial context for Movement Three.** All review, cold-read and
  recheck passes were simulated by the same model family; none is human reader feedback or independent
  testing. Formula sentence targets were not reached (see the confirmation file).

## Movement Three, first draft — 2026-10-14/15

- Status: **chapters 17–24 drafted in full as one continuous run. First draft. Not reviewed, not
  cold-read, not scored, not repaired, not committed, not pushed, not published.** Chapter 25 was not
  begun.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude
  Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier
  `claude-opus-5-5`.** This is what the runtime states; it cannot be verified independently from inside
  the session. No subagent, other model or delegated worker wrote or edited any prose or record. No codex
  or OpenAI call was made.
- Session: Claude Code background job `21a609b3` (job directory `~/.claude/jobs/21a609b3`); remote session
  `session_01BT5vnbR1vrfRhnEx9kWXaa`. Run began 2026-10-14 about 23:28 MDT and ended 2026-10-15.
- Brief: delivered in-session as the compiled Movement Three prompt. On inspection its text matches
  `planning/OPUS-5.5-MOVEMENT-003.prompt.md`, SHA-256
  `902d5abb0415d5085f422d4649df2e5797a28e6b27e5e96bb8ade94812d3d6b8` (formula source hash in the file
  `9f97e2f2…30c0b8`). No byte comparison of the delivered text was possible.
- Packet: `packets/MOVEMENT-003.md`, SHA-256
  `0222de7d30398320368842900b68307a6181655b55ed11ffb60e7026bdc85b85`.
- Edition: first draft. Isolation: worked in place in the git worktree
  `/Users/drive/kindling-2680-book-02` on branch `codex/kindling-2680-book-02`; no commit made.
- Sources read before and during drafting: chapter 16 (supplied); `STATE_LEDGER.md` (Movement One and Two
  blocks); `provenance/MOVEMENT-002-CONTINUITY.md` and `MOVEMENT-002-REPAIR.md` (opening sections);
  `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `OWNER_BRIEF.md` (as supplied in the brief);
  targeted reads of Book Two chapters 2–4 (Hart's cards, the Saltmere parcel), 13 (the license floor) and
  14 (the van night); targeted searches of the Book One manuscript (`books/book-2680-opening/manuscript`)
  for Hart's injury (ch. 8), the 2604 entries (chs. 8, 47), the patent and the notch (chs. 26, 32, 46),
  the watch's vote (chs. 32–33) and Dray's rule (chs. 40, 48). New names checked against both books'
  manuscripts, planning and provenance files and `universe/NAME_REGISTRY.md`. Nothing from the research
  corpus.
- A continuation checkpoint (`provenance/MOVEMENT-003-CHECKPOINT.md`) was written after chapter 18 as a
  precaution; no output limit intervened. It is superseded by `provenance/MOVEMENT-003-CONTINUITY.md`.

### Word counts (`wc -w`, headings included)

| Chapter | Title | Words |
|---|---|---:|
| 17 | Kiva: Thirty-Six Cells | 7,120 |
| 18 | Kiva: Laid | 8,055 |
| 19 | Kiva: The Fitter with the Watch | 7,577 |
| 20 | Kiva: Slack Water | 7,090 |
| 21 | Kiva: Read | 6,578 |
| 22 | Kiva: Six of Six | 5,810 |
| 23 | Kiva: The Proprietor | 6,517 |
| 24 | Kiva: Twelfth of Twenty-Four | 5,735 |
| | **Movement Three** | **54,482** |

Inside the packet's 50,000–56,000 working length. Seventy-nine sections; about 690 words a section.

### Viewpoint counts (by section)

| Lens | Section | Words | Share |
|---|---|---:|---:|
| Kiva | all other sections | 44,930 | 82.5% |
| Anwen Pryce | ch. 18, last section (the Ropewalk, with Maud Lyle) | 1,398 | 2.6% |
| Orla Dane | ch. 19, last two sections (the book; Hart) | 1,872 | 3.4% |
| Rhea Sorn | ch. 20, last two sections (Gannet Creek at dawn) | 2,022 | 3.7% |
| Mara Rowan | ch. 21, the outfall and the keeper's room | 2,429 | 4.5% |
| Kellan Renn | ch. 22, the Counting House | 1,831 | 3.4% |
| | **Cutaways** | **9,552** | **17.5%** |

Kiva 82.5% is inside the packet's 82–85%. **Cutaways are 52 words over the packet's 9,500 ceiling**;
recorded, not trimmed. Every cutaway opens with the lens's name and a cue only that person has. No new lens.

### Chapter hashes at the end of the run (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-17.md | 10ba1df428873aa4af1af6803c9b7a158a170a3fdbe5312fce300ef734c66eb6 |
| chapter-18.md | c127a92fe598bc7adbaa808ba79043639d2c63ceea21488dd5e99007bcec4e7f |
| chapter-19.md | 1bcae8cd72b0d3cfda26488bd0ab056fa1abbf8241bc589195522bdb65e1c469 |
| chapter-20.md | 060c1ed51019dafe20597748b5a251bdba520e714d52c69ab3d277cc60166170 |
| chapter-21.md | 0a553d0113deec7a0cb886fb06b4ac65a74844e3dbec1c694e2bb35deef57a5a |
| chapter-22.md | 791249a2fc7b3d25179f677b67c4962e551922d0b5e6b5820e1381824ae11997 |
| chapter-23.md | 08c050d7d770f8e42b80dd5a2f944a7ba39e6469c35ce25b3f34cb5a05c7a8d3 |
| chapter-24.md | 37b3f9017ce4a4ff3dc9c998f87fa933a03c6122b8bdf9f30f48cf18eb67cc68 |

### In-run corrections

Blocking contradictions only, by exact-string edit, listed in `provenance/MOVEMENT-003-CONTINUITY.md` §0
(Dray's rule origin; Hart's injury and Orla's knowledge; Kiva's silence on the coast night; two name
collisions found at the end, Admiral → Commodore and Bet → Wenna; small date and figure slips). None is a
review or repair.

### Formula

Written toward the owner's numerical formula (mid-band narration sentences, short beats, short paragraphs,
scene breaks, middle-third progression density, distributed development beats). **No measure was run in the
author run**, as instructed; compliance is for the movement review. Known before measurement: section breaks
run more frequent than the formula's ~950-word scenes.

### Plan departures (detail in the continuity file §14)

Crossings on Thursdays the 3rd and 10th (Aske's "soonest"); Pru caught lane 3 after Kiva's Friday fever; the
Proprietor states a 2604 fever (no dream); a second fever without a dream near a Glory master; the Hoop and a
2604 ring a hand high; the notch after a single cliff (seven, then six seconds); the Step quickening 48 → 57;
cutaways 52 words over ceiling.

## Movement Three, consolidated repair — 2026-10-15

- Status: **same-author repair of chapters 17–24, in place. Not rechecked, not cold-read after repair, not
  accepted, not committed, not pushed, not published.** Chapter 25 was not drafted. No Movement Four work.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.**
  This cannot be verified independently from inside the session. No subagent, other model or delegated worker
  wrote or edited any prose or record. No codex or OpenAI call was made.
- Session: Claude Code background job `8e3ee375` (job directory `~/.claude/jobs/8e3ee375`); remote session
  `session_01Qyomxormkxi2vUXobQ81Fh`. Worked in place in the worktree `/Users/drive/kindling-2680-book-02`,
  branch `codex/kindling-2680-book-02`; no commit made.
- Brief: delivered in-session. On inspection its text matches `planning/OPUS-5.5-MOVEMENT-003-REPAIR.prompt.md`,
  SHA-256 `c0ca27554b17df3e7dc9ee0d8036cd9555183e4cf1fc750019852dc8d1b380fb`.
- Inputs, read in this order before the first edit: `provenance/MOVEMENT-003-EDITORIAL-REVIEW.md`,
  `provenance/MOVEMENT-003-COLD-READ.md`, `provenance/MOVEMENT-003-CONTINUITY.md`, `STATE_LEDGER.md`,
  `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `packets/MOVEMENT-003.md`, then chapters 17–24 in full.
  One targeted search of chapters 10–16 checked how a lodger is killed (C20; it agrees, so it was not edited).
- Scope:
  - **Twenty factual and logic line fixes (F1–F20):**
    - the lane 2 tally by carry (6–4, board unchanged)
    - the catcher and the litter, stated as one rule of Seven's
    - Lyle's "yesterday" ×3 and the far-end walk
    - "three nights to go"
    - Rhea's second "since the first month"
    - seven bags
    - the Hoop's 6.33
    - Rhea's dawn at 6.10
    - Thursday's hand checks told in order
    - Seven at the Bench
    - Hart's line about Mara
    - the gate's boards
    - eleven days
    - Mara at the kitchen table
    - wired
    - "Maud told me"
    - Hart's question mark
    - the dividers
    - "without pumps"
    - *lying* flat
  - **Structure:**
    - twenty intra-scene `---` breaks removed (79 → 59 internal), including three short bridges folded
    - eight long set-piece sentences (43–55 words)
    - four reflective runs joined
    - the ch. 17 rule history split into three beats
    - footholds for *hand* and *Hold*
  - **Voices:**
    - "I'd want" 28 → 14 (Jude's, Anwen's and Aske's price speech kept)
    - "said nothing" 22 → 10
    - "did not say anything" 14 → 5
    - non-Pru blushes given their own tells
    - "in two stages" 5 → 2
    - "so that it's said" 3 → 2
    - causal *since* 5 → 0
    - the worst negation runs in ch. 21 and 23 recast
- Record: `provenance/MOVEMENT-003-REPAIR.md`. It has every correction with its evidence, the break list, the
  before/after measures and the items deliberately left unchanged. The owner items left are: the harbour clock
  (C12), the 41-minute hold (C13), the brown-ink line (C14), "my best machine" (C21), dialogue targets, and the
  front-load arithmetic.
- Word counts (`wc -w`): 54,482 → **54,610**. By chapter: ch. 17 7,158; ch. 18 8,132; ch. 19 7,611; ch. 20 7,091;
  ch. 21 6,562; ch. 22 5,784; ch. 23 6,511; ch. 24 5,761.
- Measures (`provenance/tools/m3_metrics.py`, unmodified, SHA-256 prefix `12036c794861`), before → after:
  - section mean 625 → 813
  - internal breaks per 10k 14.54 → 10.83
  - all-text median 7 → 7, ≤5 40.3% → 40.3%, ≥40 0.4% → 0.5%, SD 7.92 → 8.05
  - narration median 7 → 7, ≤5 37.3% → 37.1%, ≥40 0.6% → 0.8%

  The narration waypoint (median 8–9, about 33% short, 1.5–2.5% long) was **not** reached. Viewpoint is
  unchanged: Kiva 82.5%, cutaways 9,544 words, recounted with the script's section map renumbered.
- Frozen edition `editions/movement-003-first-draft/` was not modified. `SHA256SUMS.txt` verified OK for all eight
  files before and after. Chapters 1–16 were not touched.
- Records reconciled to the surviving prose: `provenance/MOVEMENT-003-CONTINUITY.md` (entries marked *(repair)*,
  new §16), the Movement Three block of `STATE_LEDGER.md` (status, M3.1–M3.8 lines marked *(repair)*, new M3.9),
  and a one-line dated note in `BOOK_MAP.md` §12 (C17). The Graving used as a seeding floor (C15) and the re-run
  slate (C16) are recorded as accepted departures in the continuity file §14, as the brief directed.
- **Second repair (same day, job `ca51c377`, runtime-reported `claude-opus-5-5`):** after the fresh-context
  recheck (job `a495af2f`, defect D1), `manuscript/chapter-23.md:195` now reads "The Proprietor was not what she
  had expected." in place of "He was not…"; one line only, recorded in `provenance/MOVEMENT-003-REPAIR.md` §9.

## Movement Three, review, repair, recheck and acceptance — 2026-10-15

- Reviews (both simulated, same model family, runtime-reported `claude-opus-5-5`): informed editorial and
  formula review, job `b4e11087` (prompt `planning/OPUS-5.5-MOVEMENT-003-EDITORIAL-REVIEW.prompt.md`, SHA-256
  `668b3816a353021879f149c54548717e5695e53fff52877df6097c42460098be`); manuscript-only cold read, job
  `884bf82e` (prompt `...-COLD-READ.prompt.md`, SHA-256 `bce5d1d1e4cadfd5dae3664e4dbfcb1ba9ee6a29fbcf03d758844b56b3f0bd58`).
  Neither is human reader feedback.
- Consolidated repair by the Opus 5.5 author seat, job `8e3ee375` (session `8e3ee375-4df3-42bf-aa79-6edab6a63c4c`),
  prompt `planning/OPUS-5.5-MOVEMENT-003-REPAIR.prompt.md`, SHA-256
  `c0ca27554b17df3e7dc9ee0d8036cd9555183e4cf1fc750019852dc8d1b380fb`. Record `provenance/MOVEMENT-003-REPAIR.md`.
- Fresh-context targeted recheck, job `a495af2f` (prompt SHA-256
  `d7e8eb4e60e2dabf086ca64e254a6e1fe221389fbfd2d0c9a2d5a09bfc1ec2c3`): one defect (ch. 23:195). Second repair, job
  `ca51c377` (resumed from the repair conversation; prompt SHA-256
  `e7a51af56f2753b465f6c8825c2468d96c5a25916105e1dcd54d0909ad2fad0a`): one sentence.
- Frozen first draft `editions/movement-003-first-draft/` (`SHA256SUMS.txt`, read-only, verified OK).
- Final word count 54,611 (`wc -w`). Final hashes: `provenance/MOVEMENT-003-RECHECK-CONFIRMATION.md`.
- The showrunner (Sonnet 5.5) wrote no prose. **Movement Three is accepted as editorial context for Movement
  Four.** Formula sentence targets were not reached (see the confirmation file).


## Movement Four, first draft — 2026-10-15

- Status: **chapters 25–32 drafted in full as one continuous run. First draft. Not reviewed, not
  cold-read, not scored, not repaired, not committed, not pushed, not published.** Chapter 33 was not
  begun.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude
  Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier
  `claude-opus-5-5`.** This is what the runtime states; it cannot be verified independently from inside
  the session. No subagent, other model or delegated worker wrote or edited any prose or record. No codex
  or OpenAI call was made.
- Session: Claude Code background job `9f1bbf7e` (job directory `~/.claude/jobs/9f1bbf7e`); remote session
  `session_01RgrcaqmvCrFTNm8ZWkvkri`. Run began 2026-10-15 at about 01:01 MDT and ended at about 02:00 MDT.
- Brief: delivered in-session as the compiled Movement Four prompt. On inspection its text matches
  `planning/OPUS-5.5-MOVEMENT-004.prompt.md` (3,322 lines), SHA-256
  `24f6ecfe39b64645f270926c4a854a97e05918cf38a408c4489ff8aebe696224` (formula source hash in the file
  `9f97e2f2…30c0b8`). No byte comparison of the delivered text was possible.
- Packet: `packets/MOVEMENT-004.md`, SHA-256
  `842810f4218893b212f789f64c852c455a1a2542a452cbbfc73e1bc7728d3f38`.
- Edition: first draft. Isolation: worked in place in the git worktree
  `/Users/drive/kindling-2680-book-02` on branch `codex/kindling-2680-book-02` (the EnterWorktree tool was
  not available in this session; prior movements worked in the same place); no commit made.
- Sources read before and during drafting: chapter 24, `STATE_LEDGER.md`, `provenance/MOVEMENT-003-CONTINUITY.md`,
  `MOVEMENT-003-REPAIR.md`, `MOVEMENT-003-RECHECK-CONFIRMATION.md`, `BOOK_MAP.md`, `CHARACTERS.md`,
  `UNIVERSE_BIBLE.md`, `OWNER_BRIEF.md` (as supplied in the brief); Book Two chapters 18 and 20 in full;
  targeted reads of chapters 7, 10, 11, 13, 17, 19, 21, 22 (Coombe's drills, the lodger, the coal wharf, the gate,
  Yeo and Jude, the Hoop, Halden's dinner) and chapter 12 (Halden License's roles); targeted searches of the Book
  One manuscript for the Regional Bench, Brask, and Perrin's *I mind*. New names checked against both books'
  manuscripts, planning and provenance files and `universe/NAME_REGISTRY.md`. Nothing from the research corpus.
- A continuation checkpoint (`provenance/MOVEMENT-004-CHECKPOINT.md`) was written after chapter 26 as a
  precaution; no output limit intervened. It is superseded by `provenance/MOVEMENT-004-CONTINUITY.md`.
- In-run corrections (blocking slips only, listed in the continuity file §0). Before the run closed, 22 `---`
  breaks that the draft had placed inside continuous scenes were removed, as the packet's craft notes direct, and
  two cutaway passages were tightened (about 140 words) to bring the viewpoint inside the packet's bounds. No
  editorial review was run.

### Word counts (`wc -w`, headings included)

| Chapter | Title | Words |
|---|---|---:|
| 25 | Kiva: One Water | 6,320 |
| 26 | Kiva: The Inner Lock | 5,110 |
| 27 | Kiva: Twenty-Two Rungs | 7,295 |
| 28 | Kiva: The Second Plant | 5,060 |
| 29 | Kiva: The Longshore | 6,195 |
| 30 | Kiva: Slack | 6,348 |
| 31 | Kiva: Nobody | 6,684 |
| 32 | Kiva: The Measure Goes On | 9,389 |
| | **Movement Four** | **52,401** |

Inside the packet's 50,000–57,000 working length. Fifty-two sections (44 internal breaks); about 1,010 words a
section; about 8.4 internal breaks per 10,000 words.

### Viewpoint counts (by section; whitespace token count, headings excluded)

| Lens | Section | Words | Share |
|---|---|---:|---:|
| Kiva | all other sections | 43,961 | 84.0% |
| Mara Rowan | ch. 26 (the outfall gallery, Monday night); ch. 32 (the bank gallery) | 2,274 | 4.3% |
| Kellan Renn | ch. 30, opening two sections (Skerry Pill) | 2,547 | 4.9% |
| Rhea Sorn | ch. 31, last section (the Company yard) | 1,432 | 2.7% |
| Anwen Pryce | ch. 32 (the Ropewalk, with Lyle and Carrow) | 1,159 | 2.2% |
| Orla Dane | ch. 32 (the Board's printer, with Coombe) | 975 | 1.9% |
| | **Cutaways** | **8,387** | **16.0%** |

Inside the packet's 6,500–8,500 cutaway words and 84–87% Kiva. Every cutaway opens on its lens by name with a cue
only that person has.

### Final hashes (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-25.md | 1667b92288d75c9a1a60e04c3fe18cfbb97a91918708ff079af653d252bbbca9 |
| chapter-26.md | 759d563af7d82b45247375150ea0b2e674bd5a3077bc6548c9e672c32b02b096 |
| chapter-27.md | d00c10cf06ebbc86a2d704fb372b13345166ed906b67aa070233a913fbec92a2 |
| chapter-28.md | ab304c343318c1703a9155ea4ab3019cc88a6525ab6558434c3352a71fa1c06e |
| chapter-29.md | 4c4015080fe646a6390eefc11365426cde5a1bd7c46148fd3de30865c49aa4e1 |
| chapter-30.md | 68adf8be9916736e4313cf21c71656200a6270f93fc510b8a7b229b698bc502c |
| chapter-31.md | 36a6b355de3ad948e8384d54b7f8c2858e50dba0d23a6cafc61a8e5fb164d3d4 |
| chapter-32.md | 1f137e9f86c09e1957d999c25ab1c72569eb07ec6c23e59dd55d4096eacabb04 |

- Formula measures (sentence distribution, paragraph proxy, readability, progression and combat density,
  development cadence) were written toward and **not measured** in the author run.
- Files written by this run: `manuscript/chapter-25.md` to `chapter-32.md`,
  `provenance/MOVEMENT-004-CHECKPOINT.md`, `provenance/MOVEMENT-004-CONTINUITY.md`, this entry, and the Movement
  Four block of `STATE_LEDGER.md`. No other file was edited.

## Movement Four, consolidated repair — 2026-10-15

- Status: **same-author repair of chapters 25–32, in place. Not rechecked, not cold-read after repair, not
  accepted, not committed, not pushed, not published.** Chapter 33 was not drafted. No Movement Five work.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.**
  This cannot be verified independently from inside the session. No subagent, other model or delegated worker
  wrote or edited any prose or record. No codex or OpenAI call was made.
- Session: Claude Code background job `647704f1` (job directory `~/.claude/jobs/647704f1`); remote session
  `session_017hq6UNUu29qY4gquWotNEW`. Worked in place in the worktree `/Users/drive/kindling-2680-book-02`,
  branch `codex/kindling-2680-book-02` (EnterWorktree not available); no commit made.
- Brief: delivered in-session. On spot comparison its text matches `planning/OPUS-5.5-MOVEMENT-004-REPAIR.prompt.md`
  (196 lines), SHA-256 `82226e2e2e3c91a71a338c3fe91fc5bd3ad5eda1089812d9c901dbbe03520c36`.
- Inputs, read in this order before the first edit: `provenance/MOVEMENT-004-EDITORIAL-REVIEW.md`,
  `provenance/MOVEMENT-004-COLD-READ.md`, `provenance/MOVEMENT-004-CONTINUITY.md`, `STATE_LEDGER.md` (Movement Four
  block), `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `packets/MOVEMENT-004.md`, then chapters 25–32 in full.
  One targeted search of chapter 24 (Trewin's Sunday, C16); chapters 1–24 were not edited.
- Scope:
  - **Eighteen factual and logic fixes (F1–F18):**
    - the Bench marking rule said before heat one, and the heat times made to obey it (unnamed steps 4:00, 3:00,
      4:00; the Tarn 5:10). Places 7–9 now follow from the page and every printed sheet sums; Seven stays ninth.
    - the rail minute in the Clerk's opening
    - the water's direction in the lock
    - Aske "heard it go from the lip"
    - Pru's reading
    - Kiva hears of Skerry Pill on the cart
    - the comb place
    - Penhale "told half the causeway"
    - Yeo's quarter past twelve and half an hour
    - sixty paces
    - Perrin's thimble
    - "but on its officer's word"
    - "wrote to the Works"
    - the Tuesday evening clock loosened around the fixed yes/no hour
    - Trewin's hand
    - Penhale's gust "this morning"
  - **Clarity (one sentence each):**
    - the Carry's 1:20
    - Carrow's doors
    - "I don't know why. Ours folded. It should."
    - the Tarn's far post on the west side of the bend, its sleeve swinging from downstream to inland over the
      west mud with the closed end named first
    - the quay's quiet moved to Trewin's planting
    - the Chair's hand
  - **Voices and shape:**
    - Jude's "I'd want it said" 13 → 5
    - "slowly" 43 → 28
    - "before the water" 8 → 4 (Noa's ledger the single formal record)
    - each repeated image given one home
    - Penhale's telegraphing halved
    - the aftermath's restatements cut to what is new
    - ch. 32's Dray and *Mercury* sections folded into the board scene (two breaks removed, every line kept)
    - narration joins in ch. 28 §0–§2, §5 and ch. 32 §1–§5, §9, §11
- Record: `provenance/MOVEMENT-004-REPAIR.md`, with every correction and its evidence, the full Bench re-ranking
  check, the before/after measures and the items left unchanged.
- Word counts (`wc -w`): 52,401 → **52,203**. By chapter: ch. 25 6,356; ch. 26 5,104; ch. 27 7,270; ch. 28 5,023;
  ch. 29 6,189; ch. 30 6,357; ch. 31 6,659; ch. 32 9,245.
- Measures (`provenance/tools/m4_metrics.py`, unmodified), before → after:
  - sections 52 → 50
  - internal breaks per 10k 8.41 → 8.06
  - all-text ≤5 46.1% → 45.8%, median 6 → 6
  - narration ≤5 42.2% → 41.7% (waypoint ~38% **not** reached), ≥40 2.6% → 2.7%
  - viewpoint (ch. 32 map keys shifted for the fold): Kiva 83.9%, cutaways 8,378 words
- Frozen edition `editions/movement-004-first-draft/` was not modified; `SHA256SUMS.txt` verified OK for all eight
  files before and after.
- Records reconciled to the surviving prose: `provenance/MOVEMENT-004-CONTINUITY.md` (entries marked *(repair)*;
  new §14) and the Movement Four block of `STATE_LEDGER.md` (status; lines marked *(repair)*; new M4.8 and M4.9).
- Owner items left untouched:
  - whether sentence targets govern dialogue
  - the progression-vocabulary trend
  - Perrin's lift against Aske's card (carried to Movement Five)
  - Penhale's ward as frost (C18)
  - Monday's "It was the neap"
  - Orla's "by sight for a fortnight"
  - the Movement Three open items

## Movement Four, review, repair, recheck and acceptance — 2026-10-15

- Reviews (both simulated, same model family, runtime-reported `claude-opus-5-5`): informed editorial and formula
  review, job `28d8a21c` (prompt `planning/OPUS-5.5-MOVEMENT-004-EDITORIAL-REVIEW.prompt.md`, SHA-256
  `ac40f08b84593764e799ba32eee30836b2985664d69ef842611b274422124924`); manuscript-only cold read, job `b4360b6b`
  (prompt `...-COLD-READ.prompt.md`, SHA-256 `4e866ccc9eb84e7a0155657915cc03f9f68048942f1e1f238dbc84d34ec10973`).
  Neither is human reader feedback.
- Consolidated repair by the Opus 5.5 author seat, job `647704f1`, prompt
  `planning/OPUS-5.5-MOVEMENT-004-REPAIR.prompt.md`, SHA-256
  `82226e2e2e3c91a71a338c3fe91fc5bd3ad5eda1089812d9c901dbbe03520c36`. Record `provenance/MOVEMENT-004-REPAIR.md`
  (eighteen factual corrections including the Bench re-ranking; clarity edits; catchphrase and aftermath fold).
- Fresh-context targeted recheck, job `e6a7d3ad` (prompt SHA-256
  `2201dd53392a389e809ed5256bcb192a6d16f4ba71371b4401e8f3bccb2b451b`): passed with no prose defect; four stale record
  lines, corrected by the showrunner.
- Frozen first draft `editions/movement-004-first-draft/` (`SHA256SUMS.txt`, read-only, verified OK).
- Final word count 52203 (`wc -w`). Final hashes: `provenance/MOVEMENT-004-RECHECK-CONFIRMATION.md`.
- The showrunner (Sonnet 5.5) wrote no prose. **Movement Four is accepted as editorial context for Movement Five.**
  Formula sentence targets were not reached (see the confirmation file).

## Movement Five, first draft — 2026-10-15

- Status: **chapters 33–40 drafted in full as one continuous run. First draft. Not reviewed, not cold-read, not
  scored, not repaired, not committed, not pushed, not published.** Chapter 41 was not begun.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This is
  what the runtime states; it cannot be verified independently from inside the session. No subagent, other model or
  delegated worker wrote or edited any prose or record. No codex or OpenAI call was made.
- Session: Claude Code background job `dd002b97` (job directory `~/.claude/jobs/dd002b97`); remote session
  `session_01KxhmHtfQaiCvup8hbYpRax`. Run began 2026-10-15 at about 02:45 MDT and ended at about 03:45 MDT.
- Brief: delivered in-session as the compiled Movement Five prompt. Its text matches
  `planning/OPUS-5.5-MOVEMENT-005.prompt.md` (3,653 lines), SHA-256
  `51978fba624c6b82380b320089fb5c955e616d54103578901354725dae05e904` (formula source hash in the file
  `9f97e2f2…30c0b8`). Checked by spot comparison, not byte for byte.
- Packet: `packets/MOVEMENT-005.md`, SHA-256 `48ad0c9f6b9bc7b66681c042c03182ac20c8e4e415204434864a0a636af43804`.
- Edition: first draft. Isolation: worked in place in the git worktree `/Users/drive/kindling-2680-book-02` on branch
  `codex/kindling-2680-book-02` (the EnterWorktree tool was not available in this session; prior movements worked in
  the same place); no commit made.
- Sources read before and during drafting: chapter 32 and the records as supplied in the brief (`STATE_LEDGER.md`
  Movement One to Four blocks, `provenance/MOVEMENT-004-CONTINUITY.md`, `MOVEMENT-004-REPAIR.md`,
  `MOVEMENT-004-RECHECK-CONFIRMATION.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `OWNER_BRIEF.md`); Book Two
  chapters 17, 18, 23 and 24 in full; targeted reads of chapters 16 (the Order's house, Thrale, the ferry dream), 21
  (the Saltmere keeper's 2604 entry), 25 (the Salt Hall, the Clerk) and 31 (Rhea's advice); Book One targeted reads:
  the prologue (Annick's entry), chapters 14, 15, 19 (lane rules: halves, declared counts; the hen), 24 (the night the
  page was written), 27 and 31 (the sealing, the Reader, L. Arkwright) and 47 (the Ferren keeper's line; the three
  sheets). New names checked against every manuscript, planning and provenance file in the repository and
  `universe/NAME_REGISTRY.md`. Nothing from the research corpus.
- A continuation checkpoint (`provenance/MOVEMENT-005-CHECKPOINT.md`) was written before chapter 33 with the private
  plan (bracket, scores, standings, ledger) and updated after each chapter; no output limit intervened. It is superseded
  by `provenance/MOVEMENT-005-CONTINUITY.md`.
- In-run corrections (blocking slips only; listed in the continuity file §0). Before the run closed, 38 `---` breaks
  placed inside continuous scenes were joined, as the packet's craft notes direct, and a handful of repeated idioms were
  varied (listed in §0). No editorial review was run.

### Word counts (`wc -w`, headings included)

| Chapter | Title | Words |
|---|---|---:|
| 33 | Kiva: The Week's Crossing | 8,547 |
| 34 | Kiva: Who Has It | 6,338 |
| 35 | Kiva: One Door Each | 6,000 |
| 36 | Kiva: The Three Sheets | 8,030 |
| 37 | Kiva: A Declared Count | 6,554 |
| 38 | Kiva: The Measure Is Read | 6,034 |
| 39 | Kiva: The Last Witness | 5,573 |
| 40 | Kiva: For Want of a Better | 8,142 |
| | **Movement Five** | **55,218** |

Inside the packet's 50,000–56,000 working length. Thirty-nine sections (31 internal breaks); about 1,415 words a
section; about 5.6 internal breaks per 10,000 words (below the formula's ~8.7: three lanes and three hearing sittings
are long continuous scenes kept unbroken, as the packet directs; recorded for review).

### Viewpoint counts (by section; whitespace token count)

| Lens | Section | Words | Share |
|---|---|---:|---:|
| Kiva | all other sections | 47,999 | 87.0% |
| Mara Rowan | ch. 34 (the keeper's room, the thirty-six, the two wires) | 1,977 | 3.6% |
| Orla Dane | ch. 39, opening two sections (the Chair; Hart on the gallery) | 1,573 | 2.9% |
| Kellan Renn | ch. 36, opening section (the technical office, his card) | 1,376 | 2.5% |
| Anwen Pryce | ch. 33 (the Ropewalk, teaching Lyle to lean) | 1,154 | 2.1% |
| Rhea Sorn | ch. 37, last section (the tiers with Pike; Anwen's card) | 1,108 | 2.0% |
| | **Cutaways** | **7,188** | **13.0%** |

Inside the packet's 6,500–8,500 cutaway words and 84–87% Kiva (at the upper bound). Every cutaway opens on its lens
by name with a cue only that person has. No new lens.

### Final hashes (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-33.md | 8912b98dd1ad0dce93ec384e78ce7c22d38f41d469eabc2f22a666bd6efcb6b7 |
| chapter-34.md | 7887460915affc5931743b9667c4dd9237595b203ff514f68314556538311a3f |
| chapter-35.md | ab0c4f161e316dcff37253a32b14371ad036104faf40103e3208f3624a44e35d |
| chapter-36.md | 772455ade509f93a0eb4770666dc435f6adc0768928f1eb3de44aa0c43ea4e57 |
| chapter-37.md | 202ecefdb693d5597f2d1fba6566a29c9604ef581b98cf58aafc64bc775453ba |
| chapter-38.md | 5926eed539ef7b52930d212629eb6f5bdd342e2afea8cd9b5af4d13951c3c9a4 |
| chapter-39.md | a2d8afcf2b8ec0800ca4f69d54dd9f2de00e806ac5fd658e26cbdf071a996b05 |
| chapter-40.md | e6d7be38ea313595ff085d0b14413cd2a2344084753d214be236e31677000e26 |

- Formula measures (sentence distribution, paragraph proxy, readability, progression and combat density, development
  cadence) were written toward and **not measured** in the author run.
- Files written by this run: `manuscript/chapter-33.md` to `chapter-40.md`, `provenance/MOVEMENT-005-CHECKPOINT.md`,
  `provenance/MOVEMENT-005-CONTINUITY.md`, this entry, and the Movement Five block of `STATE_LEDGER.md`. No other file
  was edited.

## Audio-clarity text repair, chapters 8–9 — 2026-10-15

- Commissioned by the audio supervisor (Codex) from the narration clarity findings for chapters 8 and 9; written by
  Claude Opus 5.5 (runtime-reported `claude-opus-5-5`), background job `9ab8514b`, brief
  `planning/OPUS-AUDIO-CLARITY-08-09.prompt.md`. Record: `provenance/AUDIO-CLARITY-08-09-REPAIR.md`. Frozen pre-repair copies:
  `editions/audio-clarity-08-09-pre-repair/` (read-only; `SHA256SUMS.txt` verified OK).
- Eight one- or two-word substitutions (two dates/counts in chapter 8, six finger and crossing counts in chapter 9). They
  were first-draft slips that survived the movement review, repair and recheck passes.
- **Hashes supersede the Movement One and Two confirmation tables for these two files only:** chapter 8
  `2cf6a1091908ef2c91b399da139ab3a5291856f922e804fcb16e62d09e1b858c` (was `da17e213…`); chapter 9
  `3a2316f2ef3e3e8f2f0da99b110d29cc27690b6c23d2610ef6f8740788728c0d` (was `60912ab0…`). Word counts: chapter 8 unchanged
  (6,977); chapter 9 8,918 (+1); Movement Two 59,235.
- Showrunner (Sonnet 5.5) verified the report's hashes against the files and committed exactly these files; it did not
  author the changes. This is a text repair only; nothing has been re-narrated or listened to.

## Movement Five, consolidated repair — 2026-10-15

- Status: **same-author line repair of chapters 33–40, in place. Not rechecked, not cold-read after repair, not
  accepted, not committed, not pushed, not published.** Chapter 41 was not begun. No Movement Six work.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This cannot
  be verified independently from inside the session. No subagent, other model or delegated worker read, wrote or edited
  any prose or record. No Codex or OpenAI call was made.
- Session: Claude Code background job `89938c88` (job directory `~/.claude/jobs/89938c88`). Worked in place in the
  worktree `/Users/drive/kindling-2680-book-02`, branch `codex/kindling-2680-book-02`; no commit made.
- Brief: delivered in-session; on spot comparison it matches `planning/OPUS-5.5-MOVEMENT-005-REPAIR.prompt.md` (188 lines),
  SHA-256 `f73100865d31d3558ece9bbcd194b5cd6a01fdf23fcddcf8274978ace111d9be`.
- Inputs, read in order before the first edit: `provenance/MOVEMENT-005-EDITORIAL-REVIEW.md`, `MOVEMENT-005-COLD-READ.md`,
  `MOVEMENT-005-CONTINUITY.md`, `STATE_LEDGER.md` (§1–§11 and the Movement Five block), `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`,
  `CHARACTERS.md`, `packets/MOVEMENT-005.md`, then chapters 33–40 in full. Targeted read-only checks of Book Two ch. 17–32
  (ch. 21 and 24) and Book One ch. 23–24.
- Scope (detail and evidence in `provenance/MOVEMENT-005-REPAIR.md`):
  - **Sums and evidence:**
    - Thursday's lane 7–2 everywhere it is spoken or printed (17 for, 12 against; Seven still ninth in the Lane, 16
      marks, 69, seventh by one mark; the unnamed eighth Lane four reconciled to +6)
    - Kiva's 1 p.m. sum made conditional on Old Four; Kellan's two fingers moved to after three
    - the Proprietor's question no longer cites the *Mercury*
    - the Pit added to every list of occasions
    - "the one piece of the dream she had words for and had kept"
    - "a week ago… the Tarn's first four"
    - the Measure's rows
    - "this morning"; "since the clerk drew it"; "a girl of seventeen"
    - Dray's fourteen cut
    - "your hurt four"
    - Thrale's 1.2 "in her four's sealed tin"
    - Mara's three twelves
    - the Proprietor's reading at twenty-seven
    - the closing survey anchored in Kiva's thought
    - Peverell's "great-grandfather's book" (an internal contradiction found during the repair)
  - **The Graving and the rules:**
    - the keepers in one sentence each
    - the Proprietor's re-read reduced to its new line, Kiva's answer and the reaction, and placed before the returns
      (the Clerk's announced order), so that the new Holloway wire is the peak
    - the old Holloway form in a clause in ch. 36
    - "and no change" given a stated cost, a point and the word, with Perrin's open mouth as his offer to bear it
    - Friday's change declared at the marshal's call
    - one early moment of opposition in the Salt Hall
  - **Mass and idiom:**
    - seven long hearing speeches broken once each, no words cut
    - three long chains split
    - "I'd sooner" 13 → 6
    - narration "table" restatements cut
    - the third "sent for" dropped
    - causal *since* 4 → 0
    - nineteen padding "that"
- Word counts (`wc -w`): 55,218 → **55,497**. By chapter:

  | Chapter | Words |
  |---|---:|
  | 33 | 8,542 |
  | 34 | 6,369 |
  | 35 | 6,023 |
  | 36 | 8,147 |
  | 37 | 6,636 |
  | 38 | 6,135 |
  | 39 | 5,585 |
  | 40 | 8,060 |
- Measures (`provenance/tools/m5_metrics.py`, unmodified; no section joined or split, so the viewpoint map was not
  remapped), before → after:
  - sentence median 7 → 7
  - ≤5 words 40.6% → 40.3%
  - ≥40 words 2.3% → 2.3%
  - longest sentence 88 → 73
  - paragraph median 25 → 25; over 60 words 23.6% → 23.6%
  - internal breaks per 10k 5.62 → 5.59
  - Flesch 93.8 → 93.8
  - Kiva 87.0% → 87.0%; cutaways 7,181 → 7,196
- Frozen edition `editions/movement-005-first-draft/` was not modified; `SHA256SUMS.txt` verified OK for all eight files
  before and after.
- Records reconciled to the surviving prose:
  - `provenance/MOVEMENT-005-CONTINUITY.md` (lines marked *(repair)*; new §15)
  - the Movement Five block of `STATE_LEDGER.md` (lines marked *(repair)*)
  - the ledger's §2 dream line (it omitted the Pit) and the §7 and M3.7 knowledge rows (Orla), by dated notes
- Chapters 1–32 were not edited.
- Owner items left untouched:
  - the colour's public existence
  - Thrale holding the fever down
  - whether sentence targets govern dialogue
  - the progression shape
  - section rhythm
  - the Movement Three and Four open items
- New owner items raised by this repair:
  - the "no change" penalty rule now on the page
  - the 2604 Saltmere keeper as Peverell's great-grandfather
- A fresh-context targeted recheck is owed before acceptance.
- Second repair (same session, job `89938c88`, brief `planning/OPUS-5.5-MOVEMENT-005-SECOND-REPAIR.prompt.md`):
  after the fresh-context recheck (`provenance/MOVEMENT-005-RECHECK.md`, job `01a5e43b`), two dropped reopening quotation
  marks were restored (ch. 36, ch. 40) and three continuity figures corrected, with a quote-parity scan returning zero
  odd paragraphs (`provenance/MOVEMENT-005-REPAIR.md` §11). Not accepted, committed or published.

## Movement Five, review, repair, recheck and acceptance — 2026-10-15

- Reviews (both simulated, same model family, runtime-reported `claude-opus-5-5`): informed editorial and formula review, job
  `887082aa` (prompt SHA-256 `8ab7d01f34c4dfcb743142817c2c9aaf7df1c0eefd7158e4ee3c22874ac69963`); manuscript-only cold read,
  job `165093a7` (prompt SHA-256 `3c273f45463b7ddb32cb0369ab12c6e8c733dfa2affaa0784a9738e89415e836`). Neither is human reader
  feedback.
- Consolidated repair by the Opus 5.5 author seat, job `89938c88`, prompt `planning/OPUS-5.5-MOVEMENT-005-REPAIR.prompt.md`, SHA-256
  `f73100865d31d3558ece9bbcd194b5cd6a01fdf23fcddcf8274978ace111d9be`. Record `provenance/MOVEMENT-005-REPAIR.md` (the Lane's
  7–2 and full bracket, the Proprietor's source, the Pit in every list, the compressed Graving evidence, the declaration rule,
  idiom and paragraph-mass passes).
- Fresh-context targeted recheck, job `01a5e43b` (prompt SHA-256 `a152bae12d9a8183cfcd4dfde3c725004e483fa9e40e196d5203b509e43d172d`):
  two one-character quotation-mark defects and three record lines. Second repair by the same author seat, job `f517a39f`
  (prompt SHA-256 `94c0b14cdfdea9810bfb6062654c33df626c3813cbf9fafc461a3a96a24a8272`): exactly those edits.
- Frozen first draft `editions/movement-005-first-draft/` (`SHA256SUMS.txt`, read-only, verified OK).
- Final word count 55497 (`wc -w`). Final hashes: `provenance/MOVEMENT-005-RECHECK-CONFIRMATION.md`.
- The showrunner (Sonnet 5.5) wrote no prose. **Movement Five is accepted as editorial context for Movement Six.** Formula sentence
  targets were not reached.

## Movement Six, first draft — 2026-10-15

- Status: **chapters 41–48 drafted in full as one continuous run. This is the book's last movement and its ending. First
  draft. Not reviewed, not cold-read, not scored, not repaired, not committed, not pushed, not published.** No Book Three work.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This is what the
  runtime states; it cannot be verified independently from inside the session. No subagent, other model or delegated worker
  wrote or edited any prose or record. No Codex or OpenAI call was made.
- Session: Claude Code background job `35fbff1b` (job directory `~/.claude/jobs/35fbff1b`); remote session
  `session_014CyfSGPCYGCxr6WtGuR8Db`. Run began 2026-10-15 at about 04:51 MDT and ended at about 05:50 MDT.
- Brief: delivered in-session as the compiled Movement Six prompt. Its text corresponds to
  `planning/OPUS-5.5-MOVEMENT-006.prompt.md` (3,692 lines), SHA-256
  `10b3d55e8bcefa6ce92dff274ef0c87e1ae0da5cd65f3cb48f6d25d904aa6feb` (formula source hash in the file `9f97e2f2…30c0b8`).
  Checked by spot comparison, not byte for byte.
- Packet: `packets/MOVEMENT-006.md`, SHA-256 `ca0980d41588d0614f45d59f0a011b31249dbbc5d1295973f1198a150ae380d9`.
- Edition: first draft. Isolation: worked in place in the git worktree `/Users/drive/kindling-2680-book-02` on branch
  `codex/kindling-2680-book-02` (the EnterWorktree tool was not available in this session; prior movements worked in the same
  place); no commit made. Chapters 11, 14, 15, 19 and 24 show as modified in `git status`; those edits belong to the parallel
  audio repairs and were in the tree before this run. This run read chapter 19 and did not edit it or any chapter before 41.
- Sources read before and during drafting: chapter 40 and the records as supplied in the brief (`STATE_LEDGER.md` through the
  Movement Five block, `provenance/MOVEMENT-005-CONTINUITY.md`, `MOVEMENT-005-REPAIR.md`,
  `MOVEMENT-005-RECHECK-CONFIRMATION.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `OWNER_BRIEF.md`); Book Two
  chapters 31, 34 and 39 in full; targeted reads of chapters 17 (Saltmere, the Graving), 19 (Hart's hand and method), 21 (the
  Hoop, the pump house, the 2604 entry), 23 (the sealed prediction's text) and 33 and 37 (Aske's price); roster checks across
  chapters 6–38 for the roll fours' doors; Book One chapters 13, 29 and 47 for name collisions and the ship's engineer's line.
  New names checked against every manuscript, planning and provenance file in the repository and `universe/NAME_REGISTRY.md`.
  Nothing from the research corpus.
- A continuation checkpoint (`provenance/MOVEMENT-006-CHECKPOINT.md`, SHA-256 `2255e99b…f58f`, after its closing status line) was written before chapter 41
  with the private plan (bearings, crews, clocks, ledgers) and ticked after each chapter; no output limit intervened. It is
  superseded by `provenance/MOVEMENT-006-CONTINUITY.md` (SHA-256 `bf108027…859e`).
- In-run corrections: blocking slips only, listed in the continuity file §0 (names that collided, distances, a head-count, a
  tide, a whistle's minute, Hart's history matched to ch. 19, a planted rule the climax cites). Idiom passes before close:
  "slowly" 29 → 14; Jude's "I'd want it said" 7 → 4. Quote-parity scan: 0 odd paragraphs. No editorial review was run.

### Word counts (`wc -w`, headings included)

| Chapter | Title | Words |
|---|---|---:|
| 41 | Kiva: A Full Bucket | 7,262 |
| 42 | Kiva: The Nearest Thing That Keeps Time | 6,911 |
| 43 | Kiva: Bearings | 5,742 |
| 44 | Kiva: Three in a Row | 8,350 |
| 45 | Kiva: Let Go | 7,275 |
| 46 | Kiva: What Was Written | 7,242 |
| 47 | Kiva: Its Own Count | 7,387 |
| 48 | Kiva: Either of Us | 6,400 |
| | **Movement Six** | **56,569** |

Inside the packet's 52,000–60,000 working length. Rehearsal (41–42) 14,173; the Slack (43–45) 21,367; after (46–48)
21,029. Fifty-five sections, 47 internal breaks (about 8.3 per 10,000 words; mean about 1,026 words a section).

### Viewpoint counts (by section; whitespace tokens; chapter headings excluded)

| Lens | Section | Words | Share |
|---|---|---:|---:|
| Kiva | all other sections | 48,213 | 85.4% |
| Kellan Renn | ch. 45 (by the chair: one hold, the lift; then the relinquishment) | 2,740 | 4.9% |
| Mara Rowan | ch. 45 (the landing: quench to let go; then salt to case nineteen) | 2,236 | 4.0% |
| Anwen Pryce | ch. 42 (the ward line learning Dray's count; Lyle's foot) | 1,420 | 2.5% |
| Orla Dane | ch. 46 (the line struck; Hart on the gallery) | 1,004 | 1.8% |
| Rhea Sorn | ch. 48 (writing Kiva's name under Coombe's hand) | 844 | 1.5% |
| | **Cutaways** | **8,244** | **14.6%** |

Inside the packet's 85–88% Kiva (at the lower bound) and 6,500–8,500 cutaway words. Every cutaway opens on its lens by name
with a cue only that person has. No new lens.

### Final hashes (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-41.md | 7fe37b1bab64806113e12d286c6f93d68fb58fdd1aba2e9d7b865dafdf2dc7a1 |
| chapter-42.md | 80ce66d148cbf96201b922c5ad22298d466d1b12d36ce01ad7980bb56a90cff4 |
| chapter-43.md | 285b5e53998a9f16dc519f42e34630271d4dea468e9bf0ec7597c1402600ad93 |
| chapter-44.md | c8afd331f9da46b8306866831e0079c6a277149ed8a5e739614c7fbc12bb252d |
| chapter-45.md | c0537f7582034164710bcb7d2c44bd4020277fe60e8e3d7beded83454b68e841 |
| chapter-46.md | c3de9336841046d43dcd861af31d9d6e1e47b471219f23a5d34cb8a059aaa81a |
| chapter-47.md | f6e80fd0836bc1a14fa915c6141599f4f0aa62362bb9887d42b385c58f6a00a7 |
| chapter-48.md | 1001dce252f525fe35b7c7e0954f15072016912c0a04dbcb5c013866098ea07b |

- Formula measures (sentence distribution, paragraph proxy, readability, progression and combat density, development
  cadence) were written toward and **not measured** in the author run.
- Files written by this run: `manuscript/chapter-41.md` to `chapter-48.md`, `provenance/MOVEMENT-006-CHECKPOINT.md`,
  `provenance/MOVEMENT-006-CONTINUITY.md`, this entry, and the Movement Six block of `STATE_LEDGER.md`. No other file was
  edited.

## Audio-clarity text repairs, chapters 11, 14, 15, 19, 24 — 2026-10-15

- Commissioned by the audio supervisor (Codex) from narration review findings and written by Claude Opus 5.5 (runtime-reported `claude-opus-5-5`)
  in three bounded passes, each with a frozen read-only pre-repair copy and `SHA256SUMS.txt`:
  1. hand counts (job `98c8ed9c`, `planning/OPUS-AUDIO-HAND-COUNTS.prompt.md`, `provenance/AUDIO-HAND-COUNTS-REPAIR.md`, chapters 11, 14, 15, 19, 24;
     ten "eight → three" substitutions: one hand has three reporting fingers and two impaired, thumbs counted as fingers as elsewhere in the book);
  2. spatial, cadence and digit counts (job `f842bac9`, `planning/OPUS-AUDIO-SPATIAL-15-19.prompt.md`, `provenance/AUDIO-SPATIAL-15-19-REPAIR.md`, chapters 15, 19);
  3. final (same author conversation; `planning/OPUS-AUDIO-FINAL-14-15.prompt.md`, `provenance/AUDIO-FINAL-14-15-REPAIR.md`, chapters 14, 15).
- Frozen editions: `editions/audio-hand-counts-pre-repair/`, `editions/audio-spatial-15-19-pre-repair/`, `editions/audio-final-14-15-pre-repair/` (all verified OK).
- The audio session's independent recheck `narration/FINAL-14-15-RECHECK.md` marks all five chapters ready for source publication.
- **Hashes supersede the earlier Movement Two, Three accepted tables for these files:**
  - chapter 11: `0e1e288bbdddf474ca8ac3afce7eee14c4fa53db4989251abb44a150e21f3a91`
  - chapter 14: `67950efe8ea329d1d1118bcf2e2ad733b6678a6ddc4db5df3d6b0d15a2ca044d`
  - chapter 15: `bbee01a321528b1c509c062eef91f9bd3d5a59a995128156115044815f667916`
  - chapter 19: `4a633ce44804458cadd5db1f6ef616ef12a3577ae75b504fd9b9f4ef6585b9c8`
  - chapter 24: `bf68b73a52ff1e62f35e523c2da1977bd6463d4529c33953740fde4d8e17f547`
- Text repairs only: nothing here has been listened to or re-narrated. The showrunner (Sonnet 5.5) verified the frozen manifests and the final hashes against the audio
  recheck's chain and committed exactly the five chapters, the three frozen editions and the three repair records; it did not author the changes.

## Movement Six, consolidated repair — 2026-10-15

- Status: **same-author line repair of chapters 41–48 (the book's ending), in place. Not rechecked, not cold-read after repair,
  not accepted, not committed, not pushed, not published.** No new book, chapter or scene; no Book Three work.
- Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author: Claude Opus 5.5.
- **Actual runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This cannot be
  verified independently from inside the session. No subagent, other model, Skill tool or delegated worker read, wrote or
  edited any prose or record. No Codex or OpenAI call was made.
- Session: Claude Code background job `3311fe04` (job directory `~/.claude/jobs/3311fe04`). Worked in place in the worktree
  `/Users/drive/kindling-2680-book-02`, branch `codex/kindling-2680-book-02`; no commit made.
- Brief: delivered in-session; its text matches `planning/OPUS-5.5-MOVEMENT-006-REPAIR.prompt.md` (164 lines), SHA-256
  `4b57c0f2cf4f76be845487c0e05fe1e08326ac747dd767d597df08031644891c`.
- Inputs, read in order before the first edit: `provenance/MOVEMENT-006-EDITORIAL-REVIEW.md`, `MOVEMENT-006-COLD-READ.md`,
  `MOVEMENT-006-CONTINUITY.md`, `STATE_LEDGER.md` (Movement Five and Six blocks), `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`,
  `CHARACTERS.md`, `packets/MOVEMENT-006.md`, then chapters 41–48 in full.
- Scope (detail and evidence in `provenance/MOVEMENT-006-REPAIR.md`):
  - **The climax's rules:** the Master waits on the outer quay sixty paces from the sill until the last plant is called; the
    4 ft 11 cask drawn at eye, chin and shoulder height; her one pace back priced and her overrun said first; Carrow and Dray's
    bearing; Kiva's doors "since the cut", forty-eight minutes; the second plant on the sill's tested granite with Wace's
    place stated; Kellan "after twenty-four"; Mara no longer hears Aske's unraised count; the first-crossing wall scene put
    in Kiva's afterward-knowledge; the seventh's cost folded into the eighth's; Jude's and Gower's knuckles.
  - **Sums, clocks and records:** Saturday's lane; C4a–k; twelve days; Hart's knowledge of the strike; the first line of the
    limits; the catchers' plank of four; the Thursday hour; the Chair's "sanctioned" wording; Hart's once/twice; "the man who
    held it before me"; Carrow–Kiva paid both ways; Peverell's seven columns in a clause.
  - **Voice:** 16 of 23 "I'd want" recast (Jude's four, Dray's "clear", Rhea's "every card", the Proprietor's "where it
    happened" kept); six closing restatements cut or shortened; ch. 48 "scarlet" 4 → 2; summary chains split; heavy speeches
    broken once; the three accounts at the box in one sentence; the sealed paper's re-reporting trimmed.
- Untouched: the frozen first draft (`editions/movement-006-first-draft/`, `shasum -a 256 -c` OK ×8); chapters 1–40; the last
  section, ch. 48 §6, from the ninth *no answer* to *The disk is cold.* (byte-identical).
- Words (`wc -w`): 56,569 → **56,373**. Viewpoint (whitespace tokens): Kiva 48,005 of 56,261 (85.33%); cutaways 8,256.
  Quote parity: 0 odd paragraphs.
- Files written: `manuscript/chapter-41.md` to `chapter-48.md`; `provenance/MOVEMENT-006-REPAIR.md` (new);
  `provenance/MOVEMENT-006-CONTINUITY.md` and the Movement Six block of `STATE_LEDGER.md` (reconciled); this entry.
- Second repair (2026-10-15, job `1a27a443`, same runtime-reported model): four bounded line fixes and two optional ones from the
  recheck (`provenance/MOVEMENT-006-RECHECK.md`) in ch. 41, 43, 44, 47 and 48, recorded with new hashes in
  `provenance/MOVEMENT-006-REPAIR.md` §12; the hash table below is from the first repair.

### Final hashes (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-41.md | 64313e5dec406d2fa60234334f3db212f7e21b5a72a09602fdcf2da182dd3a4e |
| chapter-42.md | 7ff5d82ec7129b91ba3f522673511034a7e73ca6bd5b44527a6bc97ac91386e6 |
| chapter-43.md | 6601ea020939c9f28b9b89a8b6020cd4de60a6cb91af7e8d611115ae4fd0194c |
| chapter-44.md | e55f88e1c57ff062f7df7cae669f2002b74e30c4c1a18672a4a449b6c4bc11a0 |
| chapter-45.md | f8467d4d06ab05d22f75c7efea3c034e8b4604f7f32700a22712dfa0410e1edd |
| chapter-46.md | 3de722446b1d292259b33607c851e83d1631251e7fbca8b6e2d3435641d2f582 |
| chapter-47.md | bbe72fb2c162acab9398c4a677be7bb006a12cd63de3bb416c4726ccd0f45ce4 |
| chapter-48.md | d4d03fbe91f9cc8b2dd16b2af542d402c26207caa524a7ec81d46ee3ef579d7a |

## Movement Six, review, repair, recheck and acceptance — 2026-10-15

- Reviews (both simulated, same model family, runtime-reported `claude-opus-5-5`): informed editorial and formula review, restarted as job `6e915e3e` after the first editorial child (`c89e8156`)
  was interrupted by a supervisor message ("Perform this editorial review yourself… Do not invoke penname-editor, Codex…") that was left unsent in its input (prompt SHA-256
  `7463489990ef200e67de8f422bcb95cc79cac622fb7184b31cdeda6c04c52c36`); manuscript-only cold read, job `2dcf4399` (prompt SHA-256 `f371296617bc54ae787714a20d8fb054e4e79059f1d6a518ea42575d0d2f989d`).
  Neither is human reader feedback. The Skill tool was disabled for child runs from this point (`scripts/nm-launch.sh`).
- Consolidated repair by the Opus 5.5 author seat, job `3311fe04`, prompt `planning/OPUS-5.5-MOVEMENT-006-REPAIR.prompt.md`, SHA-256 `4b57c0f2cf4f76be845487c0e05fe1e08326ac747dd767d597df08031644891c`.
  Record `provenance/MOVEMENT-006-REPAIR.md`.
- Fresh-context targeted recheck, job `22f7111d` (prompt SHA-256 `1fe13ff3bf45b4672a05fc7d7d06f0e84e12c6acd61cf4e363ca6970b55146c7`): four bounded line fixes and two optional. Second repair by the same
  author seat, job `1a27a443` (prompt SHA-256 `78cfa0abf43fa79d3f64408341fca008a429c8ddb8329f345a619d73825fc4c5`): exactly those edits.
- Frozen first draft `editions/movement-006-first-draft/` (`SHA256SUMS.txt`, read-only, verified OK). Final hashes: `provenance/MOVEMENT-006-RECHECK-CONFIRMATION.md`. Final word count 56384 (`wc -w`).
- The showrunner (Sonnet 5.5) wrote no prose. **Movement Six is accepted as editorial context for the whole-book review.** Formula sentence targets were not reached.

## Whole-book consolidated repair (located defects only) — 2026-10-15

- Author seat: Claude Opus 5.5, runtime-reported `claude-opus-5-5` (not verifiable from inside the session), background job
  `32af798e`, prompt `planning/OPUS-5.5-WHOLE-BOOK-REPAIR.prompt.md`, SHA-256
  `3bfd58b11cebcb2ebab2b865ab6928952697f2c393ac6c0e76ebdccdda202283`. No subagent, other model or Skill tool. Byline Monroe
  Jackson; seat Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- Inputs: the three simulated whole-book reviews (continuity, promises, seams; same model family, not human reader feedback),
  the repetition data, the ledgers and records, and Book One at located points.
- One bounded same-author repair of the located findings: W1–W18 (W4 deferred to the owner), P1–P5 (P6 left), WB-01–WB-22 with
  F01–F19 (F06 replaced by P1's wording), and R01–R50 (R37 declined). Showrunner decisions applied: the Hunt restated as
  4,647.2 / 4,181.2 / 466.0; Thrale's reach in the Graving (option b); the yes/no hour moves to the morning from Monday the 21st;
  Twenty-Eight's Hold renamed **Shapter**; the Barrel **686.4**; *plank* widened once; the movement-end refrain kept whole only
  at ch. 24.
- 35 chapters edited, 326,226 → 325,945 words (`wc -w`). The last section of ch. 48 is byte-identical. Quote parity: 0 new odd
  paragraphs. Frozen edition `editions/whole-book-pre-repair/` verified OK ×48 and not written.
- Records reconciled: `STATE_LEDGER.md`, the six movement continuity files, `BOOK_MAP.md` (one dated note), `CHARACTERS.md`
  (one dated note). Every disposition, before/after, hash and owner item: `provenance/WHOLE-BOOK-REPAIR.md`.
- Second repair, same day, from the fresh-context recheck (`provenance/WHOLE-BOOK-RECHECK.md`, job `59421479`): four located items only (D1 ch. 33:71 sentence cut; D2 ch. 42:207; D3 ch. 39:189 "seventy-six"; D4 three stale "Sedge" in `MOVEMENT-006-CONTINUITY.md`), recorded in `provenance/WHOLE-BOOK-REPAIR.md` §8.
- Not rechecked, not accepted, not committed, not published.

## Whole book, review, repair, recheck and acceptance — 2026-10-15

- Whole-book reviews (fresh context, read-only, same model family, runtime-reported `claude-opus-5-5`; simulated, not human): continuity, job `6f04bed8` (prompt SHA-256 `477357469ffac1bac980fcbef5dfa2a5e2410406a380e77d5e234cf9f233ebaf`);
  promises, job `26886465` (`d7e68d9eab6ee7e9cd07a36536eb8aab6a06600b30823a8de91ee65839d89e7e`); seams, job `ffc1e86f` (`5bc5b0afa3403eff4dd62330b9d29b8e743ad16d082519c69acc440a20c7db7d`, a partial read that says so).
- Whole-book repair by the Opus 5.5 author seat, job `32af798e`, prompt `planning/OPUS-5.5-WHOLE-BOOK-REPAIR.prompt.md` (SHA-256 `3bfd58b11cebcb2ebab2b865ab6928952697f2c393ac6c0e76ebdccdda202283`); record `provenance/WHOLE-BOOK-REPAIR.md`.
  Showrunner decisions on owner-level items are recorded in the brief §B and the repair report §1.
- Fresh-context targeted recheck, job `59421479` (prompt SHA-256 `1174bc1cb0a7daedd6f2eaece70d068c2ae42c3b6a66d8d88aeb056beb8c849c`): four items. Bounded second repair, job `0176bac3` (prompt SHA-256 `a341c3fb4d8f683d3a7e27455bf4a5adad1f78755ca4aa2559a587686adfe982`).
- Frozen pre-repair book: `editions/whole-book-pre-repair/` (48 chapters, `SHA256SUMS.txt`, read-only, verified OK). Final hashes and word counts: `provenance/WHOLE-BOOK-RECHECK-CONFIRMATION.md` (325,933 words).
- The showrunner (Sonnet 5.5) wrote no prose at any point in this book's second half. **The complete book, chapters 1–48, is accepted as editorial context for publication.** No human reader has read it; no narration has been approved; the owner's formula
  sentence-length targets were not reached.

### Narration-discovered clarity repairs — 2026-10-15

Opus5.5 (`claude-opus-5-5`, runtime-reported) authored bounded corrections26/27
(jobs c8ca0232 and6148611b) and33 (job95089cc9). Exact repair reports, separate
frozen editions and fresh Codex source/narration rechecks are retained. Codex
wrote no manuscript prose. Accepted hash supersession and +10-word total
(325943) are explicit in WHOLE-BOOK-RECHECK-CONFIRMATION.md's narration addendum.
No model-weight training, human reader feedback or listening approval is claimed.

Opus5.5 job7c9c2be6 subsequently corrected only chapter37's called names to match
the executed head/foot positions. Exact frozen source, repair and independent
Codex recheck are retained; placement acceptance addendum supersedes that hash,
with zero word-count change. Codex orchestrated/checked and wrote no novel prose.

Opus5.5 job64f974d4 authored the bounded physical-continuity corrections40/41.
Exact prior source, repair, independent Codex recheck and hash supersession
are retained; cumulative total325940. No Codex manuscript prose or human/audio
approval is implied. Separate44/45 findings are not accepted by this record.
