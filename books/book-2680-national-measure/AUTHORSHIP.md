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
