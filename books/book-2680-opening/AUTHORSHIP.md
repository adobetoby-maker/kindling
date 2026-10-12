# Kindling 2680, Book One (title unset) — authorship record

Public byline: **Monroe Jackson**

## Prologue and Movement One — Three Doors

- Status: **drafted 2026-10-09; reviewed, repaired, and passed by targeted recheck
  2026-10-10 (one consolidated same-author repair).** See "Consolidated repair" and
  "Targeted recheck" below.
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
- Edition: Book One, Prologue + Movement One, consolidated repair (2026-10-10). The first
  draft (2026-10-09) is frozen at `editions/movement-001-pre-repair/`.
- Branch: `worktree-kindling-2680-prologue-m001-opus55`
- Continuity checkpoint: `provenance/MOVEMENT-001-CONTINUITY.md`
- Prior attempt, not used: an earlier draft of this book's opening exists on branch
  `worktree-kindling-2680-movement-001` (commit `40aeca6`, 2026-10-08), written before the
  current eleven-snapshot plan, the Unroofed Sky lock, and Tamar Vey. It was not read or
  reused in this run.

### Files

| File | Heading | Viewpoint | First draft (`wc -w`) | After repair (`wc -w`) |
|---|---|---|---:|---:|
| `manuscript/prologue.md` | Somebody Should Write It Down | eleven dated snapshots, 2080–2676 | 16,089 | 16,621 |
| `manuscript/chapter-01.md` | There Isn't a Column | Kiva | 5,419 | 5,547 |
| `manuscript/chapter-02.md` | A Cell Keeps What You Leave in It | Kiva; Mara cutaway | 4,527 | 4,650 |
| `manuscript/chapter-03.md` | Sequence, Not Stack | Kiva; Orla cutaway | 5,229 | 5,285 |
| `manuscript/chapter-04.md` | The Terrace Ring | Kiva; Kellan cutaway | 5,796 | 5,898 |
| `manuscript/chapter-05.md` | The Cellhouse | Kiva | 5,262 | 5,567 |
| `manuscript/chapter-06.md` | What the Cell Kept | Kiva; Kellan cutaway | 5,497 | 5,822 |
| `manuscript/chapter-07.md` | Fever | Kiva; Anwen cutaway | 4,822 | 4,957 |
| `manuscript/chapter-08.md` | The Lowest Defensible Place | Kiva; Rhea cutaway | 5,560 | 5,828 |
| | | **Movement One total** | **42,112** | **43,554** |

### Post-run measurement of the first draft (for movement review; not a gate)

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

## Consolidated repair — 2026-10-10

- Repair date: **2026-10-10**.
- Brief: `editor/MOVEMENT-001-REPAIR-BRIEF.md`, read in full and performed as one bounded
  repair of the prologue and chapters 1–8. Movement Two was not started.
- Actual model that wrote the repaired prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as
  reported by the runtime environment. Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- Same-author status: **same selected author and same model as the first draft.** Every
  changed manuscript sentence was written by this model. No subagents were used and no
  other model wrote, revised, or summarized prose.
- Session restart: the repair ran in a **new Claude Code session**, not the drafting
  session. The drafting transcript was not in context. The author re-read the complete
  manuscript, both reviews, the continuity checkpoint, and the updated canon and planning
  files before editing.
- Frozen pre-repair edition: `editions/movement-001-pre-repair/` (nine manuscript files
  plus `SHA256SUMS.txt`). Verified byte-identical to the working manuscript before the
  first edit and re-verified against its checksums after the repair. Not modified.
- Reviews the repair answers: `editor/MOVEMENT-001-EDITORIAL.md` (informed same-model
  editorial review, with metrics appendix) and `editor/MOVEMENT-001-COLD-READ.md`
  (fresh-context simulated cold read). Both dated 2026-10-10.
- Canon read for the repair, including the uncommitted 2026-10-10 updates:
  `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `STATE_LEDGER.md`, `CHARACTERS.md`,
  `PROLOGUE_PLAN.md`, `IDEA.md`, `SERIES_MAP.md`, `README.md`, `packets/MOVEMENT-001.md`,
  `packets/MOVEMENT-002.md`.
- Method: each of the nine manuscript files was rewritten in place by the author, keeping
  every scene, section break and viewpoint cutaway. Section counts are identical before
  and after (87 sections).
- Repair report: `editor/MOVEMENT-001-REPAIR-REPORT.md` (files changed, material
  decisions, old and new word counts, scene confirmation, target-against-observed
  numbers, and open items).
- Continuity checkpoint: `provenance/MOVEMENT-001-CONTINUITY.md`, reconciled to the
  repaired prose after the manuscript was corrected.
- Name change: prologue snapshot 8's installer is now **Femi Oduya** (was Bram Oduya;
  "Bram" collides with Kindled canon).

### Post-repair measurement (editorial review's script, unchanged; not a gate)

| Target (formula) | Goal | First draft, all 9 files | After repair, all 9 files |
|---|---|---:|---:|
| Mean sentence length | 14.6 | 8.30 | 10.33 |
| Median sentence length | 11 | 6 | 7 |
| Sentences ≤5 words | 27.7% | 45.1% | 41.5% |
| Sentences ≥40 words | 3.3% | 0.30% | 1.67% |
| Flesch Reading Ease | 72.3 | 92.4 | 90.4 |
| Flesch–Kincaid grade | 6.8 | 2.4 | 3.2 |
| Protagonist POV share, chapters 1–8 | ~87% | 87.2% | 87.3% |

The whole-text targets are **not met**. Narration alone moved from a 9.9-word mean and
35% short sentences to a 13.8-word mean and 27% short sentences (author's own
narration/speech split; reproduce before relying on it). Quoted speech, 41% of all
sentences, was left clipped on purpose and holds the remaining gap, together with plain
vocabulary (1.25 syllables per word, unchanged). Both are owner decisions.

### Post-repair status

**Passed by targeted recheck.** The owner accepted Ysra's formal set-aside and the
dram-spent Cellhouse board line. The recheck found no justification for a second repair
pass: the remaining whole-text formula gap comes from deliberately brief dialogue,
while narration independently measures close to the intended cadence.

## Targeted recheck — 2026-10-10

- Report: `editor/MOVEMENT-001-TARGETED-RECHECK.md`.
- Reviewer: a separate Claude Opus 5.5 review-only session, informed by the draft,
  reviews, repair brief and repaired manuscript. It did not write new story material.
- Verdict: **PASS** on continuity, read-aloud cadence, character voice, revelation
  timing, and aftermath differentiation. A second consolidated prose repair was not
  justified.
- Post-recheck corrections: five narrow mechanical fixes identified by the report were
  applied without altering story events—Kellan's remaining stair count and dry-ash
  surface, the description of his stair assignment, his description of Kiva's final call,
  one garden-path sentence in chapter 4, and one awkward dram sentence in chapter 5.
- Planning cleanup: the Movement Two packet now uses `Handful-yield`, and the disk's
  response is tied to the first correct deliberate cross-door sequence so the universe
  bible agrees with the Movement Three lock.
- Frozen pre-repair files remain unchanged and checksum-verifiable.

## Movement Two — The Crooked Lane (chapters 9–16)

- Status: **first draft, written 2026-10-10 as one continuous creative run. Not reviewed,
  not repaired, not scored, not committed.** Stopped for movement review.
- Seat: Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment of the authoring session. Every manuscript sentence in
  chapters 9–16 was written by this model in one Claude Code background session. No
  subagents were used, and no other model wrote, revised, or summarized prose.
- Provider: Anthropic, via Claude Code
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-002.prompt.md`
  (SHA-256 `39106d6cf25ff71f5fd11d3fa970eca4949b609c2ead46348946b3c120d980be`), read in
  full before drafting
- Movement packet: `packets/MOVEMENT-002.md`
  (SHA-256 `0aaa91fdffa81ac9e04348f144f74dfb2204b3e373881d2d3b1da0c580f82287`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (re-hashed in this session; matches the hash recorded in the compiled prompt)
- Edition: Book One, Movement Two, first draft (2026-10-10). No frozen edition exists yet
  for this movement.
- Branch: `worktree-kindling-2680-prologue-m001-opus55` (working tree only; nothing
  committed or pushed in this run)
- Continuity checkpoint: `provenance/MOVEMENT-002-CONTINUITY.md`
- Session: a new Claude Code session, not the Movement One drafting or repair session.
  Read in full before drafting: the compiled prompt (which embeds chapter 8), manuscript
  chapters 1–7, `provenance/MOVEMENT-001-CONTINUITY.md`, `UNIVERSE_BIBLE.md`,
  `BOOK_MAP.md`, `STATE_LEDGER.md`, `CHARACTERS.md`, this file, and
  `universe/NAME_REGISTRY.md`. **The prologue was not re-read in this session**; its canon
  was taken from section 4 of the Movement One checkpoint. No prologue figure appears in
  these chapters.
- Premise and owner names: confirmed available before prose (Kiva Rowan, Mara Rowan, Orla
  Dane, Anwen Pryce, Perrin Cade, Kellan Renn, Noa Bexley, Ysra Crest, Rhea Sorn, Hollis
  Vane). No locked name was changed.

### Files

| File | Heading | Viewpoint | Words (`wc -w`) |
|---|---|---|---:|
| `manuscript/chapter-09.md` | Dark Hands | Kiva | 6,596 |
| `manuscript/chapter-10.md` | The Tin | Kiva; Orla cutaway (726); Anwen cutaway (919) | 6,734 |
| `manuscript/chapter-11.md` | Under Her Hand | Kiva | 5,939 |
| `manuscript/chapter-12.md` | Somebody's Blade | Kiva; Kellan cutaway (1,040) | 6,093 |
| `manuscript/chapter-13.md` | License Day | Kiva | 7,439 |
| `manuscript/chapter-14.md` | A Handful, Less a Pinch | Kiva; Noa cutaway (1,190) | 6,705 |
| `manuscript/chapter-15.md` | The Carry | Kiva; Perrin cutaway (785) | 5,475 |
| `manuscript/chapter-16.md` | What Carries | Kiva; Rhea cutaway (725) | 7,019 |
| | | **Movement Two total** | **52,000** |

Secondary-viewpoint sections total 5,385 words across six people (about 10.4%); Kiva
holds about 89.6%. That is a plain section word count, not a craft measurement.

### What was written

Chapters 9–13 are the connected spawn-kill preparation: Kiva's first day on the Crooked
Line third team; the Kennel warden's teaching of husk anatomy, the four declared roles,
the abort call, the sixty-count of open ash, printing and dark hands; the catch learned
one-handed with two dull fingers; the Old Yard tin drill and the no-shape drill; Orla's
sponsor's floor and her narrow written certification (recovery only); Team Seven's first
contained floor, printed by Kellan's lit blade and salted; a second floor with a skinned
husk and the team's first correct abort; and the supervised field Handful at a held tear
on the Sag Line under Hollis Vane, passed at 20.8 drams tinned. Chapter 14 grades the
yield (yield, grade, resonance), divides the share, and carries the team's decision.
Chapters 15–16 are the first sanctioned meet, a 9–7 loss to Stonehand Hall's third team,
Noa Bexley's first sanctioned measurements, and Ysra Crest's review.

Held back as the packet requires: the disk is cold throughout; no deliberate two-door
sequence is attempted or completed; the two fingers are still dull and still recovering;
the Unroofed Sky does not recur and is not named; the filter, the disk, the Makers and the
cause of the Fall are not explained. The cohort and the spawn season are shown as two
separate oddities that nobody on the page connects.

### Not done in this run

No editorial review, cold read, repair pass, metric scoring, commit or push. The formula's
sentence, paragraph, readability, progression-vocabulary and development-cadence targets
were written toward but **have not been measured** for these chapters. Nothing here should
be read as a passing score.

During drafting the author corrected continuity slips only, as the task allows: elapsed-day
phrases, two minor-name collisions (a walk-on first called Pryor, too close to Pryce; a
walk-on first called Hallam, too close to Halloran), spelling normalized to Movement One's
usage (color, practice, draft, story, curb), and three plot-logic lines in chapter 10 so
that Anwen's Team Eleven option falls on the same bell that calls Team Seven and Orla's
tin requirement is five nights running.

### Choices the owner should review

1. **Noa Bexley and Hollis Vane are written as men (he/him).** `CHARACTERS.md` gives no
   pronouns for either. This is the author's choice, made because the rest of the
   continuing cast skews heavily female; it is easy to reverse.
2. Hollis Vane's own door is never shown. He runs a four-person Home Line hold and carries
   a slate. He knew Orla Dane as a nineteen-year-old (she took him down his first culvert).
   He does not see or remark on the disk.
3. **School roster versus license team.** Kiva's roster place is the Crooked Line third
   team (captain Jude Talley; Pru Finch; Noa Bexley), which fights school meets. Team
   Seven (Renn, Pryce, Cade, Rowan) continues as a cross-school field-license team that
   holds the yield book. The first-step call order is trial-score order; Team Seven stood
   fortieth of forty.
4. New mechanics put on the page: the four roles (Kill, Hold, Carry, Catch); the abort
   word (*off*, three times); **the count** (fresh ash is open for about sixty counts);
   **dark hands** (nothing lit within three paces during the count; the catcher owns the
   floor and may call *dark*); **printing**; loose ash leaning toward the nearest worked
   pattern; **sweepings** (ash that settles untinned is Grade Third at best and does not
   count); a Handful is 24 drams by the book, a tin holds 6, and the pass mark is 20
   tinned at Grade Second or better with nothing printed, nothing fouled and nobody hurt.
5. Share arithmetic: civic half; casualty reserve a quarter of the remainder; schools half
   of what is left, by head; the team the rest. 20.8 drams gives 10.4 / 2.6 / 3.9 / 3.9.
   Any entry in the team book needs all four signatures.
6. **The ash-share decision:** 0.5 returned to the Wren House reference shelf; 1.0 sealed
   as medical reserve and kept ward-trace; 1.0 for a catch kit of the team's own; 1.4 for
   two Kennel floors. Nothing for a meet reserve, at Kiva's own request, and she nearly
   runs dry in the meet as a result.
7. **The spawn variation** is a "skin": a ward-like sheen over a Handful's front and
   shoulders that turns a lit blade and faces the brightest lit thing. Four on the Kennel
   floor in the month, none in sixty years of Kennel book before; one on the Sag Line; its
   ash reads **W-trace** on the resonance comb, where Handful ash has always read plain.
   Kiva can feel it through the pan without a door ("curved").
8. **The cohort sign:** median Hold 6.1 against forty years at 5.3–5.5; three Fire
   readings at seventeen against two in the previous ten years; three first-years beat a
   31-year-old Stonehand load plate in one afternoon. Perrin was withdrawn from that
   exhibition by his cracked ribs and tells Kiva not to write it in her book.
9. **Noa's finding:** Kiva's draw on the still door alone is about 0.93 on a sanctioned
   board (the bench gave 3.1 with all three doors woken), and a door she has shut cleanly
   recovers its Hold while she works another. Ash is one reserve; the doors tire
   separately. One day's readings; Ysra orders them continued with Kiva's monthly written
   consent. This plants rotation as the long-event advantage without any hand-off.
10. In the meet's third carry, Kiva's braced stance stops Lowen Brask and Jude Talley's
    touch lands in the stop. Orla names it a hand-off **across two people**, explicitly
    not Kiva's and not a sequence. It is intended as the felt reference for Movement
    Three's first true two-door sequence.
11. Mara's review: tuning is suspended, repair and reconciliation continue, hearing on the
    9th before Examiner Rusk. Mast six, which Mara declined to recalibrate, rang four
    minutes before masts five and seven on the 28th; Hollis Vane sent the Works a note
    saying so. Outcome left open.
12. The Flask qualifiers are moved up to the last week of the month after the meet; Team
    Seven stands seventeenth of thirty-one by yield.
13. The month is treated as having thirty days (the 30th is followed by the 1st). It is
    still not named on the page.

## Movement Two consolidated repair — 2026-10-10

- Repair date: **2026-10-10**.
- Brief: `editor/MOVEMENT-002-REPAIR-BRIEF.md`, read in full and performed as one bounded
  same-author repair of chapters 9–16. Movement Three was not started.
- Actual model that wrote the repaired prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as
  reported by the runtime environment. Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- Same-author status: **same selected author and same model as the first draft.** Every
  changed manuscript sentence was written by this model. No subagents were used and no
  other model wrote, revised, or summarized prose.
- Session: a **new Claude Code session**, not the drafting, review, or cold-read session.
  Read in full before the first edit: the brief; `editor/MOVEMENT-002-EDITORIAL.md`
  (including its metrics appendix); `editor/MOVEMENT-002-COLD-READ.md`;
  `packets/MOVEMENT-002.md`; `provenance/MOVEMENT-001-CONTINUITY.md`;
  `provenance/MOVEMENT-002-CONTINUITY.md`; `UNIVERSE_BIBLE.md`; `BOOK_MAP.md`;
  `STATE_LEDGER.md`; and `manuscript/chapter-09.md` through `chapter-16.md`. The prologue
  and chapters 1–8 were not re-read; their canon was taken from the Movement One
  checkpoint.
- Frozen pre-repair edition: `editions/movement-002-pre-repair/` (eight manuscript files
  plus `SHA256SUMS.txt`). This supersedes the earlier line in this file that says no
  frozen edition exists for Movement Two. Verified byte-identical to the working
  manuscript before the first edit and re-verified against its checksums after the
  repair. Not modified.
- Method: targeted in-place edits by the author, not a rewrite. All eight chapters, all
  chapter headings, all 71 sections and all six secondary cutaways remain. One section
  (Noa's corridor cutaway in chapter 14) was rewritten whole at about 70% of its length.
- Continuity checkpoint: `provenance/MOVEMENT-002-CONTINUITY.md`, reconciled to the
  repaired prose after the manuscript was corrected.
- Repair report: `editor/MOVEMENT-002-REPAIR-REPORT.md` (every material choice,
  unresolved items, and target-against-observed measurement).
- **Status: passed by targeted recheck.** The recheck found no justification for a
  second repair pass. Four phrase-level corrections identified by the verifier were
  applied afterward and checked mechanically; see the targeted-recheck record below.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `manuscript/chapter-09.md` | 6,596 | 6,764 | +168 |
| `manuscript/chapter-10.md` | 6,734 | 6,733 | −1 |
| `manuscript/chapter-11.md` | 5,939 | 6,121 | +182 |
| `manuscript/chapter-12.md` | 6,093 | 6,156 | +63 |
| `manuscript/chapter-13.md` | 7,439 | 7,838 | +399 |
| `manuscript/chapter-14.md` | 6,705 | 6,372 | −333 |
| `manuscript/chapter-15.md` | 5,475 | 5,608 | +133 |
| `manuscript/chapter-16.md` | 7,019 | 7,045 | +26 |
| **Movement Two total** | **52,000** | **52,637** | **+637** |

Secondary-viewpoint sections after the repair, by the editorial script's word count:
Orla 726, Anwen 918, Kellan 1,042, Noa 844, Perrin 785, Rhea 643. Kiva holds about 90.6%
(89.6% before). No viewpoint was added.

### Post-repair SHA-256

| File | SHA-256 |
|---|---|
| `manuscript/chapter-09.md` | `111d5b583d5b851a69b3de4b3eb6cf6d9395bd1480df3249275c2f0a22676841` |
| `manuscript/chapter-10.md` | `826c16323de4faf9d34ecdd0dec0678f5ffb04171d0d297f67b70d26254b513d` |
| `manuscript/chapter-11.md` | `0cbb663565f4202579aa04b3b90b1c35adc024cb8d239f9ad93325547b7af6cb` |
| `manuscript/chapter-12.md` | `ed94d8455fb3ffa67f5ae37bc1c9268c1c836aef4ac518b44f2431f91bd2cb98` |
| `manuscript/chapter-13.md` | `bd28a3bf64549425e76859aa03f2aefc3d21a684e02e8b73e8d679eca2910d23` |
| `manuscript/chapter-14.md` | `7330d86ddc9b41aa89ab3038f01ae5c2f8f00c6efb54b4403c05cf8c403cdc28` |
| `manuscript/chapter-15.md` | `51e43a03dee95b40fc8eaab70ff2ff53f846a179fb2ad606a563d9393ff77012` |
| `manuscript/chapter-16.md` | `43860ca36c1a8a4d6e2b8c853555bc1a3d0ad8a94489f40a161c547e2a168d98` |

### Post-repair measurement (editorial review's script, unchanged; not a gate)

| Target (formula) | Goal | First draft, ch. 9–16 | After repair, ch. 9–16 |
|---|---|---:|---:|
| Mean sentence length | 14.6 | 9.84 | 9.93 |
| Median sentence length | 11 | 7 | 7 |
| Sentences ≤5 words | 27.7% | 41.5% | 41.0% |
| Sentences ≥40 words | 3.3% | 1.52% | 1.63% |
| Flesch Reading Ease | 72.3 | 92.2 | 92.2 |
| Flesch–Kincaid grade | 6.8 | 2.8 | 2.9 |
| Narration only: mean / ≤5 / ≥40 | 14.6 / 27.7% / 3.3% | 12.95 / 29.0% / 2.94% | 13.09 / 28.2% / 3.06% |
| Protagonist POV share | ~87% | 89.6% | 90.6% |

The whole-text sentence and readability targets are still missed, by the same margin and
for the same reason as before: speech is 48% of sentences. Per the owner ruling carried in
the brief, dialogue was not lengthened to chase them.

### Material choices in the repair the owner should review

1. **Draw is defined as a ratio, lower is better.** Noa says it once in chapter 11: what a
   fighter burned on a piece of work, set against what the book says that work should
   cost. This keeps Movement One's direction (3.1 is bad, 0.82 is good). The brief's
   wording was "usable output relative to the relevant book/bench expectation"; the page
   keeps the ratio-against-expectation sense and does not reverse the direction.
2. **0.93 is kept, with its load correction stated.** Ysra reads "eleven hundredths and a
   hair on the tape, set against the book's twelve" for a four-minute contested hold.
   0.112 / 0.12 = 0.93. The board's 0.87 to 0.98 and Kellan's "eleven hundredths" stand.
3. **"Live-cell events" covers a held rift and the Kennel lattice**, said once by Kellan
   in chapter 9 as the Chair's clerk's reading.
4. **Team Eleven does not get its floor.** Vane shuts the tear after the early husk
   rather than seat a new hand-door in front of it. Had Anwen taken Mace's offer she
   would not have been licensed on the 28th. Nobody on the page says so.
5. **License-day count:** fourteen teams called (thirteen plus Team Nineteen, in the
   place of a team the warden had not passed fit), Team Seven fourteenth, Team Eleven a
   fifteenth waiting behind. Call positions no longer coincide with team numbers:
   Nineteen stood 18th, Eleven 9th; Kiva's log reads T33, T14, T26.
6. **The Home Line drops its wall** before the second husk is cut, so the experts keep
   the dark-hands rule.
7. **Friction added in three existing scenes:** the Kennel benches and floor (chapter 9),
   Selka Dray on the Sag Line (chapter 13), and the Stonehand gallery (chapter 15). None
   is answered or resolved.
8. **One authority stays unpersuaded:** the meet referee signs the card clean and writes
   on its back that a fighter who must be flagged between doors is "supervised," not
   safe. Ysra reads it without remark.
9. **Orla's second condition is shown met:** six seals of six with the bad hand on the
   24th, cited in the certificate.
10. **The escalation pairing** is remarked on once, by Noa. Rhea's card carries the tear
    count alone. Ysra cites both reports as grounds for the Flask change with no comment
    on their relation. "Strong year" appears twice; "dirty spring" once.

## Movement Two targeted recheck — 2026-10-10

- Report: `editor/MOVEMENT-002-TARGETED-RECHECK.md`.
- Reviewer: a separate Claude Opus 5.5 review-only session with the repaired and frozen
  editions, both reviews, the repair brief/report, both continuity checkpoints, and the
  governing canon. It did not write story material.
- Verdict: **PASS** on all three repair priorities. No second prose repair was justified.
- The verifier independently rebuilt the calendar, license-day clock and team count,
  meet score, Draw ratio, ash shares, Hold figures, and key geography. It confirmed the
  added school resistance reads as unresolved social pressure, the adult cadences are
  more distinct, the escalation remains a seed rather than a proof, and Chapter 14 now
  has forward pressure while preserving every protected element.
- Accepted canon: Draw is ash spent against the book expectation (`1.0` standard; lower
  is more efficient); twelve hundredths is the book expectation for the contested
  four-minute hold; Vane denied Team Eleven its live floor.
- Four post-recheck mechanical corrections were applied: Halloran's ambiguous pronoun,
  the month boundary in Ysra's report, the Home Line catch image, and the candidate
  headcount. The continuity checkpoint was updated for the catch image. No event,
  tactic, choice, score, or formula decision changed.
- Final Movement Two word count: **52,637** (`wc -w`). The frozen first draft remains
  **52,000** words and checksum-verifiable.

## Movement Three — First Season (chapters 17–24)

- Status: **first draft written 2026-10-11 as one continuous creative run; reviewed and
  given one consolidated same-author repair the same day; not yet rechecked.** See
  "Movement Three consolidated repair" below, which supersedes this section's statements
  that the movement is unreviewed and that no frozen edition exists. The rest of this
  section describes the first draft as it stood. Movement Four was not started.
- Seat: Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment of the authoring session ("powered by the model named Opus
  5.5; exact model ID `claude-opus-5-5`"). Every manuscript sentence in chapters 17–24 was
  written by this model in one Claude Code background session. **No subagents were used**,
  and no other model wrote, revised, or summarized prose.
- Provider: Anthropic, via Claude Code (background job)
- Session: Claude Code session `67896672-4c66-4e9a-83a8-812a6553d76f`
  (https://claude.ai/code/session_01Df5CKknpzFzEmLmc92es5S), a new session and not the
  Movement One or Movement Two drafting, repair, review, or recheck sessions. Drafting ran
  from about 14:22 to 15:15 MDT on 2026-10-11.
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-003.prompt.md`
  (SHA-256 `7237451c368efc3abd9faa574f5229a330be5730447cc82275e44aa62dcb2c35`), read in
  full (all 2,473 lines) before drafting. The prompt embeds chapter 16, `UNIVERSE_BIBLE.md`,
  `BOOK_MAP.md`, `STATE_LEDGER.md`, `CHARACTERS.md`, this file as it stood, and
  `provenance/MOVEMENT-002-CONTINUITY.md`; those were read there.
- Movement packet: `packets/MOVEMENT-003.md`
  (SHA-256 `33cd4372d4c1e0e42ecd65fcfefa93260c1975f563f81d52d3cb5f906546286f`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (re-hashed in this session; matches the hash recorded in the compiled prompt)
- Edition: Book One, Movement Three, first draft (2026-10-11). **No frozen edition exists
  for this movement.**
- Branch: `worktree-kindling-2680-prologue-m001-opus55` (working tree only; the eight
  chapter files, the packet, and the compiled prompt are untracked)
- Continuity checkpoint: `provenance/MOVEMENT-003-CONTINUITY.md`
- Also read in this session, beyond the compiled prompt:
  `provenance/MOVEMENT-001-CONTINUITY.md` (in full), `universe/NAME_REGISTRY.md` (in
  full), `editor/MOVEMENT-002-REPAIR-BRIEF.md` (in full), `manuscript/chapter-13.md` (in
  full), the first 140 lines of `manuscript/chapter-15.md`, lines 205–264 of
  `manuscript/chapter-07.md` (the fever and the dream), and line-level excerpts found by
  search in chapters 3, 4, 8, 9, 10, 11 and 14 (Orla's definition of a sequence, how a dram
  is settled, the posted ash prices, Healer Aske's instruction, Examiner Rusk).
- **Not read in this session:** the prologue; chapters 1–12 and 14 other than the excerpts
  above; the rest of chapter 15; the Movement One and Two editorial reviews, cold reads,
  repair reports and recheck reports. Their canon was taken from the two continuity
  checkpoints. A review should weigh that when it checks voice and small facts.
- Premise and owner names: confirmed available before prose (Kiva Rowan, Mara Rowan, Orla
  Dane, Anwen Pryce, Perrin Cade, Kellan Renn, Noa Bexley, Ysra Crest, Rhea Sorn, Hollis
  Vane, Lowen Brask, Selka Dray, Jude Talley, Pru Finch). No locked name was changed.
  New minor names were checked by search against this book's manuscript and provenance,
  `books/book-01-kindled`, `books/book-02-meridian`, and `universe/`; none matched.

### Files

| File | Heading | Viewpoint | Words (`wc -w`) | SHA-256 |
|---|---|---|---:|---|
| `manuscript/chapter-17.md` | Twenty Handfuls | Kiva; Mara cutaway (1,049) | 5,799 | `726322d43e6cd795e533c8f61ebf36383cfd5a9b44eb15adbfa49ee0c3aa0cec` |
| `manuscript/chapter-18.md` | A Gate to Lean On | Kiva; Anwen cutaway (575) | 5,070 | `1fbe95c1f5740681f6a473a9043b24f3dfce67d4f8fb6fd54dc84fe8fb325a42` |
| `manuscript/chapter-19.md` | Rule Nine | Kiva | 5,782 | `2457b74b030fac109a879451ecf60c5f1a1f6e095d96f4283b3a963ef1137e29` |
| `manuscript/chapter-20.md` | Mine, Yours | Kiva; Lowen Brask cutaway (860) | 6,301 | `4f33e7bf93fde4f5af6601c54e51f338ae0510ab0d596a6450c8f82232333992` |
| `manuscript/chapter-21.md` | The Pit | Kiva | 5,410 | `a344556323e2e93f3e89356e90626ba6a832c2c5d22e98240a27dc965b297554` |
| `manuscript/chapter-22.md` | Rung One | Kiva | 3,911 | `6067859c6af85675f7ef41b222e12a16eebf251e41deb68199f18516942e5ffd` |
| `manuscript/chapter-23.md` | Ember, to Still | Kiva; Perrin cutaway (967); Rhea cutaway (1,463) | 6,417 | `b6fa8396a47aee2e5e75f5e69af45c614eaaf4b7012cfcfe77d1364ee709e4cb` |
| `manuscript/chapter-24.md` | What Was Tinned | Kiva; Noa cutaway (933) | 6,319 | `45fb53afc01e4950bdea543839283fc38af70be80c48f998027c21dd12a4615c` |
| | | **Movement Three total** | **45,009** | |

Secondary-viewpoint sections total about 5,850 words across six people (Rhea 1,463, Mara
1,049, Perrin 967, Noa 933, Lowen 860, Anwen 575), about 13.0%; Kiva holds about 87.0%.
The eight chapters have 59 sections (about 760 words a section). These are plain section
word counts, not craft measurements.

### What was written

Chapters 17–18 open the Flask preparation: Kiva's first deliberate two-door attempts
(Stride into stance, one bound, six misses and an empty ration by Thursday); Warden Druce's
teaching of the Flask as a "string" of eight knots taken as a schedule by a four-team
company; Mara's hearing before Examiner Rusk; the first purchased Kennel floor (the purse
sheet); a brief lost meet at the Wren House; and a professional Graywater response to a
live Flask at the Ferren weir, watched from the bank. Chapters 19–20 are the return meet
against Lowen Brask's Stonehand third team at the Crooked Line's own court (9–8, won), in
which Kiva breaks her word to her sponsor, tries the sequence under home rule nine, and
wrecks her knee; the team's correction; the second Kennel floor; and attempts eleven to
fourteen. Chapters 21–23 are the Flask qualifier at the Pit: the fifth company's decision
to leave no gate lit, Team Seven's clean rung, the string taking the arena's bus, the
professional response, Kiva's first correct deliberate two-door sequence under a Home Line
field direction, the disk warming afterward, and a waking fragment of the dream. Chapter 24
is the easing, the grading, the board's ruling, the share, the investment vote, and the
evidence that opens Movement Four.

Held back as the packet requires: the disk warms once, only after the sequence has
finished, and does nothing else; the sequence is not repeated and is not certified; no
stable two- or three-door configuration is held; no rank changes; the two fingers are
eased back to where they were and are neither cured nor lost; the Unroofed Sky is not
named and supplies no tactic; the filter, the Makers, the disk's origin and the cause of
the Fall are not explained; the W-trace medical reserve is spent only on a healer's easing.

### Not done in this run

No editorial review, cold read, repair pass, metric scoring, frozen edition, commit or
push. The formula's sentence, paragraph, readability, progression-vocabulary and
development-cadence targets were written toward and **have not been measured** for these
chapters. Nothing here should be read as a passing score.

During drafting the author corrected continuity slips only, as the task allows: the
distance to the home line in the meet's first carry (sixteen paces); the score on the
board late in the third carry (eight to five); Jude's rung count in the third company (a
six-knot string); two elapsed-time phrases ("a fortnight"); one line in which Selka Dray
knew of the Rowan household filing (removed, with Kiva's two answering phrases); one
bulk-of-ash image in chapter 17; one phrase in chapter 24 that turned a nosebleed into a
split lip; and the keeper's shelf at the Pit, which first had a
chained gangway plank and now can be reached only through the keeper's door, with the
lever's four-hundredweight requirement stated in the same speech.

### Choices the owner should review

Full detail is in `provenance/MOVEMENT-003-CONTINUITY.md`, section 9. The largest:

1. **The sequence is Stride into stance** (Ember door shut at the top of the bound, a
   doorless fall "as long as it takes to say *two*," the still door set under the landing
   "like a pan"). It opens the Pit's sprung south link, a task that needs a Stride to
   reach and a still-door to hold. It lasts about nine seconds and costs 0.31 of a dram.
2. **It is done outside her certificate**, under a Home Line field direction given one
   minute after the foreman struck the event from the Circuit calendar. Orla refuses to
   certify it, states what she has seen, and takes the consequence on herself. The board
   rules that no sanctioned-event incident occurred. Orla's standard afterward: "Show me
   six."
3. **The new spawn expression:** the skin does not break when the top knot is cut; it
   slides to the next knot, and when the blind string is left with nothing lit it walks to
   the nearest pattern (the arena's bus), lets cords down through the gratings, closes its
   skin all round, stops reading people, and walks the bus toward the Ferren pump bank.
   Opening the link returns it to an ordinary skinned Flask. Rung-one ash reads **W, full;
   I, trace** (the comb's seventh reed, glossed as induction).
4. **The team's mistake is Kiva's own notion** (whole floor dark, taken from the meet's
   lesson), adopted by the company on a show of hands after the foreman said he would
   leave a gate. The board writes a new rule and grants a **"second step, attached."**
5. **Selka Dray**, who objected to Kiva's seat and has not changed her mind, is the
   second hand at the lever and keeps Kiva's count. **Lowen Brask** commands the Kiln's
   lid crew and uses the Crooked Line's count-in to bring it down on a second string.
6. **Three evidence hooks for Movement Four:** a T-0 entry in the Pit's branch book (every
   lamp on an isolated ring, once); a hand-copied 2446 register entry with a margin note in
   a retired record hand; and a Home Line bearer's book and reasons ledger that Orla has
   asked Hollis Vane to open. None is explained.
7. **Chapter 22 is short** (3,911 words) because the response continues without a break
   into chapter 23. The chapter boundary could move in review without rewriting.

## Movement Three consolidated repair — 2026-10-11

- Repair date: **2026-10-11**.
- Brief: `editor/MOVEMENT-003-REPAIR-BRIEF.md`, read in full and performed as one bounded
  same-author repair of chapters 17–24, limited to its three priorities. Movement Four was
  not started.
- Actual model that wrote the repaired prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as
  reported by the runtime environment of the repair session ("powered by the model named
  Opus 5.5; exact model ID `claude-opus-5-5`"). Seat: Monroe Jackson 1.3 Light / O'Connor
  1.3.0, as named in the brief.
- Same-author status: **same selected author and same model as the first draft.** Every
  changed manuscript sentence was written by this model. **No subagents were used**, and
  no other model wrote, revised, or summarized prose.
- Provider: Anthropic, via Claude Code (background job).
- Session: a **new Claude Code session**
  (https://claude.ai/code/session_01GHqh9rsECBoXj3rpGu7fqP), not the drafting, editorial
  or cold-read session. The drafting transcript was not in context. Session start-up
  injected a few lines of project status memory from earlier sessions (that the chapters
  had been drafted and a metrics pass run); nothing in them was used as canon.
- Read in full before the first edit: the brief; `editor/MOVEMENT-003-EDITORIAL.md`
  (including its metrics appendix and script); `editor/MOVEMENT-003-COLD-READ.md`;
  `packets/MOVEMENT-003.md`; `provenance/MOVEMENT-003-CONTINUITY.md`; `STATE_LEDGER.md`;
  `BOOK_MAP.md`; `UNIVERSE_BIBLE.md`; this file; and `manuscript/chapter-17.md` through
  `chapter-24.md`.
- Line-level lookups by search, for single facts: chapter 14 (Halloran's description and
  pronoun, Healer Aske, the ash office), chapter 15 (how the referee calls a half and a
  down), chapter 8 (the Chair's office), chapters 3 and 11 (the crooked post), chapter 13
  (Bettan), `CHARACTERS.md`, the Movement Two repair brief and report (the Aske ruling),
  and a name search across `universe/`, `books/book-01-kindled`, `books/book-02-meridian`,
  `books/book-03-wellspring` and this book's manuscript and provenance.
- **Not read in this session:** the prologue; chapters 1–16 as prose; the Movement One and
  Two continuity checkpoints, reviews and recheck reports. Their canon was taken from the
  Movement Three checkpoint, the two review reports and the lookups above.
- Frozen pre-repair edition: `editions/movement-003-pre-repair/` (eight manuscript files
  plus `SHA256SUMS.txt`, committed at `6057f6e`). Verified byte-identical to the working
  manuscript before the first edit (`cmp` and `shasum -c`) and re-verified against its
  checksums after the last edit. **Not modified.**
- Reviews the repair answers: `editor/MOVEMENT-003-EDITORIAL.md` (informed same-model
  editorial review) and `editor/MOVEMENT-003-COLD-READ.md` (fresh-context simulated cold
  read). Both dated 2026-10-11.
- Method: chapters 17–23 received targeted in-place edits. Chapter 24 was rewritten whole,
  in place, keeping every scene and every passage the brief protects, with one section
  break removed (the cart and the foot of the cart are now one section). The movement has
  58 sections (was 59). All six secondary cutaways remain, with the same viewpoints; none
  was added.
- Continuity checkpoint: `provenance/MOVEMENT-003-CONTINUITY.md`, reconciled to the
  repaired prose after the manuscript was corrected (its section 0 lists the changes).
- State ledger: `STATE_LEDGER.md`, new section "Movement Three carried state."
- Repair report: `editor/MOVEMENT-003-REPAIR-REPORT.md`.
- **Status: repaired and passed by targeted recheck.** The author did not review or score
  its own repair beyond re-running the editorial review's measurement script; a separate
  Claude Opus 5.5 review-only session then checked the repair and found no reason for a
  second prose pass. Nothing had been committed or pushed at the time of that recheck.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `manuscript/chapter-17.md` | 5,799 | 5,833 | +34 |
| `manuscript/chapter-18.md` | 5,070 | 5,106 | +36 |
| `manuscript/chapter-19.md` | 5,782 | 5,868 | +86 |
| `manuscript/chapter-20.md` | 6,301 | 6,413 | +112 |
| `manuscript/chapter-21.md` | 5,410 | 5,857 | +447 |
| `manuscript/chapter-22.md` | 3,911 | 3,961 | +50 |
| `manuscript/chapter-23.md` | 6,417 | 7,084 | +667 |
| `manuscript/chapter-24.md` | 6,319 | 8,571 | +2,252 |
| **Movement Three total** | **45,009** | **48,693** | **+3,684** |

Secondary-viewpoint sections after the repair, by the editorial script's word count: Rhea
1,580, Mara 1,058, Noa 975, Perrin 968, Brask 866, Anwen 603. Kiva holds 87.55% (86.99%
before).

### Post-repair SHA-256

| File | SHA-256 |
|---|---|
| `manuscript/chapter-17.md` | `3570bd1851ac8f93a505208dbc20cf404b55ab4ad6df41cc2d39b425af400db5` |
| `manuscript/chapter-18.md` | `0bf1d749668c2da0dc723a6f5647032efa48b17fc42056c2b6030cbaa97ffc76` |
| `manuscript/chapter-19.md` | `aca9492860991f38b3ec86cc1e95ed28c46f8bbafa72f37de1c8b2a105993eb6` |
| `manuscript/chapter-20.md` | `0b9566196b71f4f3e334832678e192e1ad7a2eaa04ba5de1f6fe1aa9d19e6b89` |
| `manuscript/chapter-21.md` | `ff0d4fbd39e55b79639c85bbfb9a0c4b2a74b4a530cd68cf68139d58f0782506` |
| `manuscript/chapter-22.md` | `39be7c07773973e8efb8c993055ce967e75ddf072d51fe2129a08d25c9e009fa` |
| `manuscript/chapter-23.md` | `df4cb223c776f70a6711b2e10e1bdd78db2be1a4399a864683d54999638cdb45` |
| `manuscript/chapter-24.md` | `d1abe20f486ae48cb295c77dcf955a6e1823e10b2fd08ac225f481268a6332f1` |

### Post-repair measurement (editorial review's script, unchanged; not a gate)

`metrics_m003.py` as printed in the editorial review's appendix (SHA-256
`e07e81fb233ead096c2350a892e0e162ff0c35fe1af4f56a65fc4e96911e7a59`), run against the frozen
text and again against the repaired text. The "before" column reproduces the review.

| Target (formula) | Goal | First draft, ch. 17–24 | After repair, ch. 17–24 |
|---|---|---:|---:|
| Mean sentence length | 14.6 | 8.46 | 9.03 |
| Median sentence length | 11 | 6 | 6 |
| Sentences ≤5 words | 27.7% | 44.6% | 43.8% |
| Sentences ≥40 words | 3.3% | 0.38% | 0.95% |
| Flesch Reading Ease | 72.3 | 94.7 | 94.2 |
| Flesch–Kincaid grade | 6.8 | 2.1 | 2.4 |
| Narration only: mean / ≤5 / ≥40 | 14.6 / 27.7% / 3.3% | 10.85 / 31.2% / 0.78% | 12.03 / 29.7% / 2.00% |
| Narration, chapter 24: mean / ≤5 / ≥40 | | 8.72 / 36.5% / 0.00% | 13.09 / 29.7% / 4.64% |
| Section mean (sections) | ~950 | 761 (59) | 838 (58) |
| Protagonist POV share | ~87% | 87.0% | 87.6% |
| "I want that understood" | | 4, four speakers | 0 |
| "want / like it said, noted, known, understood, written" | | 12 | 5 (Anwen 3, Perrin 2) |

Narration by chapter after the repair (mean / ≥40): 17: 12.59 / 4.17%. 18: 12.78 / 2.95%.
19: 11.77 / 2.07%. 20: 11.82 / 0%. 21: 13.06 / 1.87%. 22: 10.85 / 1.03%. 23: 11.01 /
0.62%. 24: 13.09 / 4.64%.

The whole-text targets are still missed, for the reason the owner has already ruled on:
speech is 49% of sentences and was left clipped. The brief's narration aim ("roughly a
thirteen-word mean and roughly three percent forty-word sentences" outside action) is
**met in chapter 24 and nearly met in the other three chapters that have no set piece (17,
18, 21); it is not met movement-wide** (12.03 and 2.00%), because the lane, the Pit and
the shelf were left at their fight cadence as the brief requires.

### Material choices in the repair the owner should review

Full detail, with before-and-after text, is in `editor/MOVEMENT-003-REPAIR-REPORT.md`.

1. **Healer Aske is "he"** (three words in chapter 24). The brief said to give a pronoun
   where the prose was avoiding one and did not say which. Easy to reverse.
2. **Three minor names changed:** Tolliver to **Gower**, Merrin to **Edda**, Warden Tilling
   to **Sedge**. Searched against the registry and canon; none matched.
3. **The race is raised on the terrace and honestly dismissed** by Bettan and Vane ("There's
   no pattern in a bar"). Kiva reads her own weir note against herself and is glad to have
   it answered. The company slate records the objection and the answer.
4. **Kiva's mark is set clear of gratings and benches**, not of "the board's feeder," so she
   no longer avoids copper in one scene and dismisses it in the next.
5. **One new observation on the Monday:** Kiva thinks she sees a heap lift toward a lit
   gate, and one such team comes out at forty-nine. She does not know that the gate cost
   the dram and writes no reason. This gives the dark floor a second honest motive; the
   owner may prefer it cut.
6. **Vane owns the link-before-lid trade** aloud and on the slate ("Pumps before doorway").
   The board's findings were left word for word and do not mention it.
7. **Costs now paid on the page:** Anwen's list and an exchange that is left unsettled;
   Gower at the table; Rhea owning the ward slide and going to Stroud; Stroud declining to
   say what she thinks of the dark floor; a catcher from Team Twenty-Eight at the
   standings; Perrin's answer to Vane.
8. **The infirmary healer's account is paid** (by Orla) and the knee's ban becomes Aske's
   fortnight, to the 13th. Kiva carries the crate.
9. **Removed from this movement:** Orla's remark about the superseded stacks, and the
   teaser about Rhea's two-word card. Both remain in the frozen edition if wanted back.
10. **Noa no longer knows of Kiva's register entries.** He has the keeper's remark and
    writes "Find out what a T-0 is." Noa stays he/him; the brief's "her" for Noa was read
    as a slip.
11. **Kiva tells Mara she will take the 2446 margin to the Library's reader herself.** A
    small decision of her own, in place of Orla's echo. It points at Movement Four without
    binding it.
12. **The Halden man reads the tape "on the first of next month."** That is thirty days
    from Friday the 1st on a thirty-day month, the only month length the book has stated.
13. **The countdown to the link now closes:** 22 and 16 on the hobble, 8 at the lip, and
    the cords at the head of the ramp as her count reaches one.
14. **Chapter 24 is 8,571 words** (was 6,319), the longest chapter in the book so far.
15. **Sixty-three narration joins outside chapter 24**, in quiet passages of chapters 17
    (14), 19 (17), 20 (14) and 21 (18), made under the brief's owner ruling on narration.
    No fact changes in them.

## Movement Three targeted recheck — 2026-10-11

- Report: `editor/MOVEMENT-003-TARGETED-RECHECK.md`.
- Reviewer: Claude Opus 5.5 (`claude-opus-5-5`) in a new review-only session. This was a
  same-model informed recheck, not a human read, cold read, or independent test.
- Coverage: repaired chapters 17–24, the frozen edition, both original reviews, repair
  brief and report, continuity checkpoint, state ledger, authorship record, and cited
  earlier-canon lookups. No subagents were used.
- Verdict: **PASS** on calendar/arithmetic/identity/knowledge, the dark-floor causal and
  relationship chain, and chapter 24's flow/read-aloud clarity. No second prose repair
  was justified.
- Required record correction: the Movement Three continuity checkpoint's left-knee row
  now carries the thirteenth, matching the manuscript and the rest of that checkpoint.
  No manuscript sentence changed after the recheck.

## Movement Four — What the Record Lost (chapters 25–32)

- Status: **first draft written 2026-10-11 as one continuous creative run. Unreviewed.** No
  editorial review, cold read, metric scoring, repair, recheck or frozen edition exists for
  this movement. Movement Five was not started.
- Seat: Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported by
  the runtime environment of the authoring session ("powered by the model named Opus 5.5; the
  exact model ID is `claude-opus-5-5`"). Every manuscript sentence in chapters 25–32 was
  written by this model in one Claude Code background session. **No subagents were used**, and
  no other model wrote, revised, or summarized prose.
- Provider: Anthropic, via Claude Code (background job `ccdfca4e`)
- Session: Claude Code session `ccdfca4e-2d30-4c07-a089-0fb6a299c322`
  (https://claude.ai/code/session_01Uk2nDZpFHjYqfewNnf9eJY), a new session and not any of
  the Movement One to Three drafting, review, repair or recheck sessions. The session ran
  from about 19:18 to 20:25 MDT on 2026-10-11; by file timestamps the eight chapters were
  written between 19:44 and 20:13.
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-004.prompt.md`
  (SHA-256 `75ddfeb195302c8747e800b2227730f40d2e64fd3155676ffe1d8b5a2ce99969`), read in full
  (all 2,463 lines) before drafting. The prompt embeds chapter 24, `CHARACTERS.md`,
  `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `STATE_LEDGER.md` and
  `provenance/MOVEMENT-003-CONTINUITY.md`; those were read there.
- Movement packet: `packets/MOVEMENT-004.md`
  (SHA-256 `490e1209d383a9a71026c1b82a9ae3b2a8b5e2abc95aff210b3881c445ff7a54`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (re-hashed in this session; matches the hash recorded in the compiled prompt)
- Edition: Book One, Movement Four, first draft (2026-10-11). **No frozen edition exists for
  this movement.**
- Branch: `worktree-kindling-2680-prologue-m001-opus55`. **The author made no commit and no
  push, as the owner instructed.** While the run was in progress another process, committing
  under the repository owner's name, committed each chapter file within seconds of its being
  written: nine commits, `016d4ba` (19:44) to `23458d5` (20:12), titled "Publish Kindling
  2680 chapter N" and "…continuity corrections." At about 20:20 the branch was level with `origin`
  and `git ls-remote` showed the remote head at `23458d5`, so those commits were pushed. The
  author noticed this only after the last chapter was finished and did not alter, revert or
  add to it. **Not in those commits** (working tree only at the end of the session): the
  final edits to `manuscript/chapter-29.md` (two added passages) and `manuscript/chapter-32.md`
  (the standings line; "last Thursday"; the name Pettit); this file; `STATE_LEDGER.md`; and
  the untracked continuity checkpoint. The hashes below are of the working-tree files and so
  differ from the committed blobs for chapters 29 and 32.
- Continuity checkpoint: `provenance/MOVEMENT-004-CONTINUITY.md`
- State ledger: `STATE_LEDGER.md`, new section "Movement Four carried state."
- Also read in this session, beyond the compiled prompt: `editor/MOVEMENT-003-TARGETED-RECHECK.md`
  (in full; the packet makes it govern if it records a required mechanical correction: its one
  required correction, R1, is to the Movement Three checkpoint's left-knee row and was already
  applied; it also notes that the keeper's "forty seconds" is an estimate, which this draft
  respects); `provenance/MOVEMENT-001-CONTINUITY.md` and `provenance/MOVEMENT-002-CONTINUITY.md`
  (in full); `universe/NAME_REGISTRY.md` (in full); the Movement Three sections of this file;
  prologue snapshots 8 and 10 and the opening of snapshot 11 (lines 699–828 and 955–1194 of
  `manuscript/prologue.md`); and line-level excerpts found by search in chapters 3, 7, 8, 13,
  17, 18, 19, 20 and 23 (Orla and the Annick card; the fever dream; the register lines; the
  closing crew; the first yard tries; the weir response; the Low Lane mast; the step; the
  successful sequence).
- **Not read in this session:** the rest of the prologue; chapters 1–23 other than the
  excerpts above; the Movement One to Three editorial reviews, cold reads, repair briefs and
  repair reports. Their canon was taken from the three continuity checkpoints. A review
  should weigh that when it checks voice and small facts.
- Disclosed: session start-up injected a few lines of project status memory and tool
  reminders; none was used as evidence for story facts.
- Premise and owner names: confirmed available before prose (Kiva Rowan, Mara Rowan, Orla
  Dane, Anwen Pryce, Perrin Cade, Kellan Renn, Noa Bexley, Ysra Crest, Rhea Sorn, Hollis Vane,
  Lowen Brask, Selka Dray, Jude Talley, Pru Finch). No locked name was changed. New minor
  names were checked by search against every book's manuscript and registry in this
  repository and `universe/`; none matched. One name was changed during drafting (the Halden
  team's Kill, first written "Marsden," now **Pettit**) for sitting too close by ear to a
  reserved canon surname.

### Files

| File | Heading | Viewpoint | Words (`wc -w`) | SHA-256 |
|---|---|---|---:|---|
| `manuscript/chapter-25.md` | Asked Nicely | Kiva | 5,623 | `1d86df8aabb386b1c2c8559d67ca1ac2e4753e3d29498b1a0ff8b2bce6a2e777` |
| `manuscript/chapter-26.md` | However Produced | Kiva; Noa cutaway (1,618) | 5,490 | `3ec69353d966655bff9c1087254bac2243a19be6916e8e5783d011ccce01a5cb` |
| `manuscript/chapter-27.md` | One Crossing | Kiva; Hollis Vane cutaway (1,021) | 5,157 | `ca62eebfb47bd0630b1b2c60f84c328f6cb8d3ea922f06e1a5f9f378fca273d3` |
| `manuscript/chapter-28.md` | The Cheap One | Kiva | 5,007 | `23407b9493b0dbe863a8d5695b984a13998731e94418389aa7689d8991e9f668` |
| `manuscript/chapter-29.md` | The Night Van | Kiva; Anwen cutaway (756) | 5,526 | `f427a1dfff1a02a267eed041802a1e0725cffa5bca28024736fde365badb9d8d` |
| `manuscript/chapter-30.md` | What's Behind You | Kiva; Rhea cutaway (1,650) | 5,951 | `0927e69af8755bfd06950087aff765a6953019fcf0a0a2b0ca7194498549771e` |
| `manuscript/chapter-31.md` | Come Back Clean | Kiva | 6,469 | `6c487c5f7c5803202750d13c9720c6c5b749c4ef906a6f8b6b7e73e04f2d4682` |
| `manuscript/chapter-32.md` | Held of the Line | Kiva; Orla cutaway (766) | 5,901 | `9f108691c6c71d92698823778b212afd197da998bad419fd5ee5031450e5592c` |
| | | **Movement Four total** | **45,124** | |

Secondary-viewpoint sections total 5,811 words across five people (Rhea 1,650, Noa 1,618,
Vane 1,021, Orla 766, Anwen 756), about 12.9%; Kiva holds about 87.1%. The eight chapters
have 41 sections (about 1,100 words a section). These are plain section word counts, not
craft measurements. Hollis Vane is a viewpoint for the first time.

### What was written

Chapters 25–26 turn the fortnight's stand-down into four separate searches. Kiva takes the
2446 margin to the Compact Library's reader, learns that the Even Hand asked about the lamps
that night, is shown what a disputed box costs to open, and finds her sponsor's name in the
request book sixteen years back. Noa learns what a T-0 is and that Kiva already had four,
finds a notch on all sixteen pens of the Pit's tape, and reads the Halden patent behind the
comb's seventh reed. Orla owns having cut a report to fit. Kiva puts the papers in front of
her team on Anwen's last night, and Anwen leaves unreconciled by her own choice. Chapter 27
has a Home Line ledger entry of 2471 read (a two-door woman, a "crossing," and a hand that
did not come back), the request made with Mara's hand, the travelling mast, Orla's six rules,
and the first sanctioned go: a called abort. Chapter 28 is the tries: one crossing on the
cross, one "stack" that lands softly at a third of the cost and is called a miss by Noa
against his own wishes, and a second crossing that leaves two fingers white for forty-one
counts. Chapters 29–30 are the Graywater shadow shift and the Weighbridge Street call: a
qualifier's habits fail when a student lure is read by a Flask; a professional is pinned;
shed workers lift on Perrin's count; roles and reasons are declared again; a first-year
walks a Flask down a street as a declared lamp; Team Seven takes a second husk the corrected
way; Kiva catches three rungs behind Pike. Chapter 31 is the reconciliation on the wharf (a
stepped bag withheld from a tenement on a catcher's word, a comb and a warden's four-century
rule), Rhea Sorn's slate and her one piece of guidance, and Kiva's reading of Hesper Annick's
fever entry under two observers. Chapter 32 is the claims on the bag, Kellan's choice, and
the bearer's book at the Home Line hall, in which Kiva reads Ilse Corran's reason and writes
the disk's one warmth into a column that has said "nothing" for five hundred years.

Held back as the packet requires: the disk stays cold through two sanctioned crossings and
the call, and neither it nor the dream supplies a tactic; no fever and no recurrence; the
dream is confirmed as shared imagery only, with no date, cause, meaning or use; the disk's
origin is a lost first book and "We do not know what it is for"; Kiva opens no door in the
field and stays inside her certificate; the tries stand at two of six; no rank changes; the
fingers are neither cured nor lost; the sealed W reserve is untouched; no new spawn expression
is introduced; Anwen is not on Team Seven after the 10th; the 10:24 pattern is measured more
closely and not explained.

### Not done in this run

No editorial review, cold read, repair pass, metric scoring, frozen edition or narration, and
no commit, push or publication by the author (see "Branch" above for what another process
did). The formula's sentence, paragraph, readability,
progression-vocabulary and development-cadence targets were written toward and **have not
been measured** for these chapters. Nothing here should be read as a passing score.

During drafting the author corrected continuity slips only, as the task allows, by small
in-place edits made directly after each chapter was written: elapsed-time phrases (Aske's
week; "a week after" the Pit; Mara's and Kiva's acquaintance with Orla; Noa's "Saturday";
"last Thursday"); what Orla's suspension covered and why she took Kiva on; who was in the Low
Lane on the 4th; that Mara's sealed record is one page, of the 29th; the count of earlier
jams and goes; the number of people in the yard; a Kennel-floor comparison; the third team's
record with Kiva; that Pru Finch is not a Wren House student; the bell codes; where Anwen's
line was working on the 23rd; the tear's times (2:14, 2:24, about 2:32); street geometry (the
mark fourteen paces above the tear, the lure two paces below the hem, the gate eight paces up,
the Pellow a dozen paces below); how long Agnes Roake waited for her pump; and a third
"nineteen years" that became twenty. Two changes were larger. **The Step:** the first wording
made every bank in Meridian a stepped bank, which contradicted the pump bank going "into
step" as an alarm in chapter 24; it now belongs to Halden's yards, refineries, lift yards and
big tram sheds, and municipal banks are unstepped. **The fifth husk:** the section in which
Team Seven declares its corrected plan was rewritten once so that the lure stands within
twelve paces of the husk and the cloth above the Pellow, and so that the officer's correction
is "who's watching the gap." Four short passages were added to chapter 29 after its first
write because the scene wanted them (Pike's cord grip; the two residents who cannot be moved;
Pike looking all the way round before he kneels; Anwen's earned wall). None of this was a
review or a scored pass.

### Choices the owner should review

Full detail is in `provenance/MOVEMENT-004-CONTINUITY.md`, section 10. The largest:

1. **The district is Weighbridge Street and the Pellow Building** from prologue snapshot 8.
   The building's cell book still carries the 2247 installer's reason on its first leaf and
   has lost his name; its warden applies it to the call's ash.
2. **The students' failure is their own first-step method.** A lure for a husk is a lamp for
   a Flask. Kiva gives the word, a Graywater blade's leg is broken, and Rhea Sorn takes the
   remark as the shift's. Team Seven stays attached.
3. **"Stepped" ash and the Halden patent** ("however produced"). The comb's seventh reed is
   tied to a foundation patent; the Flask's bottom two knots read I, full; the bag is withheld
   from the tenement and is now under three claims with a hearing on the 3rd. This is the
   movement's largest invention and the main engine handed to Movement Five.
4. **"A crossing"** is the Home Line's older word for a sequence, from a 2471 field direction
   to a two-door woman, Tansy Wold, whose left hand did not return. She is not a bearer.
5. **A "stack"** is a third kind of go: soft, a third of the cost, wrong, and nearly signed
   by Orla. Noa corrects both of them from the tape.
6. **Two of six**, with exactly enough ash for four more and a new healer's price of one go a
   week. The fingers stay away longer each time.
7. **Kellan accepts the Halden license team for the Regional** and stays on Team Seven's book.
8. **Rhea Sorn speaks to Kiva**, gives one bounded piece of guidance, tells her about Ilse
   Corran and the culvert, and says she will burn a card without saying what was on it.
9. **The bearer's book** in full, including a recall clause, Ilse's reason ("Will they put
   why?"), the Line's record that it overrode Mara in 2669, and **Kiva's own entry.**
10. **The reading** is done under two silent observers; Kiva counts through it, all three
    doors stir, and the sister of the Even Hand notices and has it recorded.
11. **Orla read the Annick notebook in 2664 and withheld it**; she owns that and refuses to
    tell Kiva what it says. Mara chooses not to read it and has her own page sealed and timed.
12. **Movement length is 45,124 words**, at the foot of the working range, with no chapter
    over 6,500.

## Movement Four consolidated repair — 2026-10-11

- Status: **one bounded same-author repair applied to chapters 25–32. Not rechecked.** The
  first draft is frozen, unchanged, at `editions/movement-004-pre-repair/` (its
  `SHA256SUMS.txt` verified before the first edit and again after the last). This section
  supersedes the first-draft section's statements that the movement is unreviewed and that no
  frozen edition exists; the rest of that section describes the first draft as it stood.
- Repairing model: **Claude Opus 5.5 (`claude-opus-5-5`)**, the same model that wrote the
  first draft, as reported by the runtime environment. **No subagents were used**, and no
  other model wrote or revised prose.
- Provider: Anthropic, via Claude Code (background job `ccdfca4e`)
- Session: https://claude.ai/code/session_01AwavyR1d14YWEeP9LCnTmn, a fork of the drafting
  session, so the drafting conversation was in context. The repair ran from about 20:49 to
  21:10 MDT on 2026-10-11.
- Instructions: `editor/MOVEMENT-004-REPAIR-BRIEF.md`
  (SHA-256 `fcfca2d63c879bf8fed16291218fd8f6996edf6e3c307e135008438977afcb6d`), read in full.
- Reviews the repair answers, both read in full: `editor/MOVEMENT-004-EDITORIAL.md`
  (SHA-256 `8995d340a4731ed3f474f4a772dc17ccea5b394ce0d17c1d5fe2b35915ed2690`; an informed
  same-model editorial review) and `editor/MOVEMENT-004-COLD-READ.md`
  (SHA-256 `2d0cf081d584d7bfc358fa54e3cb69f39f2b0cb7929a6dc07aed2fedce4d8a2c`; a simulated
  cold read). Neither is a human read.
- Also consulted, by line lookup only: chapter 7 (lines 281–300), the prologue (1215–1230),
  chapter 23 (249–256), chapter 16 (485–491), chapter 8 (113–127) and chapter 2 (57, 97), to
  make the repaired recollections agree with what is already on the page.
- Method: targeted in-place edits, 177 in all, each applied by exact-string replacement that
  fails unless it matches once. No chapter was rewritten whole. No scene, section break or
  viewpoint was added, cut or moved; the movement still has 41 sections and five cutaways.
- Records reconciled to the repaired prose: `provenance/MOVEMENT-004-CONTINUITY.md` (new
  section 0 lists the changes) and the Movement Four block of `STATE_LEDGER.md`.
- Repair report: `editor/MOVEMENT-004-REPAIR-REPORT.md`.
- **Not done:** no targeted recheck, no review or scoring of the repair by its author beyond
  mechanical verification, no commit, push, publication or narration, and no Movement Five.
  The working tree holds the repair uncommitted.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `manuscript/chapter-25.md` | 5,623 | 5,635 | +12 |
| `manuscript/chapter-26.md` | 5,490 | 5,564 | +74 |
| `manuscript/chapter-27.md` | 5,157 | 5,218 | +61 |
| `manuscript/chapter-28.md` | 5,007 | 4,964 | −43 |
| `manuscript/chapter-29.md` | 5,526 | 5,571 | +45 |
| `manuscript/chapter-30.md` | 5,951 | 6,075 | +124 |
| `manuscript/chapter-31.md` | 6,469 | 6,578 | +109 |
| `manuscript/chapter-32.md` | 5,901 | 5,975 | +74 |
| **Movement Four total** | **45,124** | **45,580** | **+456** |

Secondary-viewpoint sections after the repair: Rhea 1,654, Noa 1,622, Vane 1,021, Anwen 756,
Orla 735; 12.7% of the movement. Kiva holds 87.3%.

### Post-repair SHA-256

| File | SHA-256 |
|---|---|
| `manuscript/chapter-25.md` | `d090c6fdd2bb6512a04c3a440d4ec6921c7f1147c203bd4e38cdf1c0b25ae9d1` |
| `manuscript/chapter-26.md` | `68096648ee344869162ebef1887cd90122db18b7b1d9f0575300c3223a147315` |
| `manuscript/chapter-27.md` | `620b3d397066f9ab1e4dcdc2a63586a8cd3a9e3592935f742e0d9b885e8a5276` |
| `manuscript/chapter-28.md` | `5ac5909cdf857c29963880a4d8701b553296cba532997ada15bec847e3e5d941` |
| `manuscript/chapter-29.md` | `48271630582a1d62b5590367f538eaf086e8437c4e523bb130dca8e2f478b3d9` |
| `manuscript/chapter-30.md` | `cecad59a7d2a4e54a357909ec16773faaba64c13b1d9398d0a269a4deff36f81` |
| `manuscript/chapter-31.md` | `64017eaeaca52911fe23c77093d7205c6bd02ed3e9f563c695f9b9dc2c23dbe7` |
| `manuscript/chapter-32.md` | `8f24f93343724b85aa0eccbad737af1039e4776476745e08940b427b21cea188` |

### Material choices in the repair the owner should review

Full detail, with before-and-after text, is in `editor/MOVEMENT-004-REPAIR-REPORT.md`.

1. **The Annick reading now agrees with chapter 7.** "Paying attention" and the lamps going
   out or white are matches Kiva recognizes as her own words. One match is new and
   unprovable: a color with no word for it, which she has seen and never told anyone.
2. **Kiva corrects Aske about the wharf.** The hand was gone about fifteen hours, not an
   hour; she is tempted to let the kinder number stand and does not. Aske names the cord as
   the cause and does not change his ruling.
3. **Her still door at the rescue is now a kept boundary,** stated in three sentences.
4. **Dialogue pass.** The six younger speakers, and Pike, Nairn and Rhea, are plainer and
   shorter. The Reader, Mrs. Cobb, Orla, Aske, Stroud, the sister and Adlam are untouched.
   Mara, Vane, Lowen Brask, Brannock and Team Twenty-Eight's catcher, whom the brief does not
   name either way, were lightened a little. "I've no ham" was kept on purpose.
5. **Orla's Regional trial has no year** and falls, by her "four years," in 2660. The repair
   changed chapter 26's first-draft "three years" to "four years" to restore that earlier canon.
6. **Selka Dray's hearing has no date.** The first draft's "the second" was one of the
   calendar repetitions.
7. **The district table's last column is "not ranked."** One added line of Pike's.
8. **The Pit interval** is corrected in this movement's records only. Chapter 24's line, the
   Movement Three checkpoint, the Movement Three ledger block and the packet still say forty.

### Targeted recheck and final correction

- Fresh review-only session: Claude Opus 5.5 (`claude-opus-5-5`), background session
  `074f0aeb-0e37-475d-9ef3-f2749dfe2f57`, 2026-10-11.
- Prompt: `editor/MOVEMENT-004-TARGETED-RECHECK.prompt.md`; result:
  `editor/MOVEMENT-004-TARGETED-RECHECK.md`.
- Verdict: **PASS** on canon/body/knowledge/geometry/records, differentiated dialogue, and
  listener orientation/flow. No second broad repair was justified.
- Required final prose correction: chapter 31 now says Kiva read Brannock's name in the
  Tallis Street regulator's cell book at Mara's elbow, and felt his tuning in the drum. This
  restores chapter 2's source and object. Word count remains 6,578; Movement Four remains
  45,580 words.
- Required record corrections were made in `provenance/MOVEMENT-004-CONTINUITY.md`: Kellan's
  unprepared question, Mara's week-and-a-half interval, settled Old Yard/Brannock/Regional
  facts, and the first-draft three-to-four-year correction.
- Final chapter 31 SHA-256 after the bounded recheck correction:
  `42e0c0e9089e578efb697741d5174a7dd672af0e3c05813f5657fa22d5debbee`.

## Movement Five — The Regional Measure (chapters 33–40)

- Status: **first draft written 2026-10-11 as one continuous creative run. Unreviewed.** No
  editorial review, cold read, metric scoring, repair, recheck or frozen edition exists for
  this movement. Movement Six was not started.
- Seat: Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported by
  the runtime environment of the authoring session ("powered by the model named Opus 5.5. The
  exact model ID is `claude-opus-5-5`"). Every manuscript sentence in chapters 33–40 was
  written by this model in one Claude Code session. **No Task tool, workflow or subagent was
  used**, and no other model wrote, revised or summarized prose.
- Provider: Anthropic, via Claude Code (Claude Agent SDK), non-interactive session
- Session: Claude Code session `7646ad9d-72e6-445a-8ab0-1fcea7aed769` (the identifier in the
  session's own tool-result path; no web address for it was visible to the author). A new
  session, not any earlier drafting, review, repair or recheck session. It ran from about
  21:51 to 22:55 MDT on 2026-10-11; by file timestamps the eight chapters were written
  between about 22:05 and 22:42.
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-005.prompt.md`
  (SHA-256 `bece77d6065006b7e489128aa1581908e8a9f32a77e18920c663bf1d08f2e0b4`), read in full
  (all 1,910 lines) before drafting. The prompt embeds chapter 32,
  `provenance/MOVEMENT-004-CONTINUITY.md`, `STATE_LEDGER.md` and the owner-voice seed; those
  were read there.
- Movement packet: `packets/MOVEMENT-005.md`
  (SHA-256 `8d5a33b0a5c22388d148709432b03411689f59d5c2fd25062621e35a1255a8e8`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (re-hashed in this session; matches the hash recorded in the compiled prompt)
- Edition: Book One, Movement Five, first draft (2026-10-11). **No frozen edition exists for
  this movement.**
- Branch: `worktree-kindling-2680-prologue-m001-opus55`, at `2df90d4` ("Prepare Kindling 2680
  movement five") when the run began and when it ended. **The author made no commit and no
  push.** Unlike the Movement Four run, no other process committed anything while this run was
  in progress: at 22:48 `git log` still ended at `2df90d4`, the branch was level with its
  remote, and the eight chapters and the checkpoint were untracked in the working tree.
- Continuity checkpoint: `provenance/MOVEMENT-005-CONTINUITY.md`
  (SHA-256 at the time of this entry
  `5505453c06e3238982d56815c3615bea535caca6089a06cbb90d92a7aeb180d2`)
- State ledger: `STATE_LEDGER.md`, new section "Movement Five carried state."
- Also read in this session, beyond the compiled prompt: **repaired chapters 25–31 in full**
  (chapter 32 is in the prompt), as the packet requires; `provenance/MOVEMENT-001-CONTINUITY.md`,
  `provenance/MOVEMENT-002-CONTINUITY.md` and `provenance/MOVEMENT-003-CONTINUITY.md` (in
  full); `universe/NAME_REGISTRY.md`, `CHARACTERS.md`, `BOOK_MAP.md` and `UNIVERSE_BIBLE.md`
  (in full); the Movement Four sections of this file; and line-level excerpts found by search:
  chapter 8 (Jessamy Hart), chapters 10, 12, 13, 17, 19 and 24 (Selka Dray), chapters 9, 19
  and 21 (Jude Talley), chapters 1, 3 and 4 (the ward), chapter 12 (the sandbag), and every
  mention of the Regional and of numbered months in chapters 1–32.
- **Not read in this session:** the prologue; chapters 1–24 other than the excerpts above;
  the editorial reviews, cold reads, repair briefs, repair reports and rechecks of any
  movement. Their canon was taken from the four continuity checkpoints. A review should weigh
  that when it checks voice and small facts.
- Disclosed: session start-up injected project memory, including a note that an earlier
  session at about 21:30 to 21:46 had read the canon and written a planning notes file
  without drafting anything. No such file was found in the repository or in temporary storage,
  the working tree was clean at the start, and nothing from that session was used; this
  session read the canon again. Start-up memory was not used as evidence for story facts. The
  author kept one scratch file outside the repository
  (`/tmp/m5-scratch/m5-working-notes.md`: a route plan, a ledger and a running log) so that
  the run could survive a context limit. It is not manuscript, is not in the repository, and
  is superseded by the checkpoint.
- Premise and owner names: confirmed available before prose (Kiva Rowan, Mara Rowan, Orla
  Dane, Anwen Pryce, Perrin Cade, Kellan Renn, Noa Bexley, Ysra Crest, Rhea Sorn, Hollis Vane,
  Lowen Brask, Selka Dray, Jude Talley, Pru Finch). No locked name was changed. New minor
  names (Thirza Bly, Wilf Marten, Hesketh, Yarrow, Birch, Wace, Tibb, Stiles) were checked by
  search against every book's manuscript and registry in this repository and `universe/`;
  none matched. Two first choices were dropped for matching existing names: "Ivo" (book two)
  and "Orme" (this book's prologue).

### Files

| File | Heading | Viewpoint | Words (`wc -w`) | SHA-256 |
|---|---|---|---:|---|
| `manuscript/chapter-33.md` | Cause Written | Kiva; Hollis Vane cutaway (about 1,370) | 5,091 | `5281e17f923323e2caf6b0ec51c66acc46e46a20160210306bd039fd0fe845d7` |
| `manuscript/chapter-34.md` | On What Paper | Kiva; Kellan cutaway (986) | 5,844 | `3534b5522d932feee76e8b993a48d63b792592865b03bf15726285eee317cf32` |
| `manuscript/chapter-35.md` | Six | Kiva; Anwen cutaway (1,199) | 5,703 | `4d579032f3b4c527f8b4ab37129f7e25d43d5575d3e0725d3bc2a051808d8106` |
| `manuscript/chapter-36.md` | Catch, Carry, Plant | Kiva; Orla cutaway (758) | 5,764 | `feceff1a75401d58f1e4f5c361abc1d07e3cd552c8ee455e5c804fe69fa74ccd` |
| `manuscript/chapter-37.md` | Take a Corner | Kiva | 5,179 | `734f49c14cb94e2c402feb30ce1922f773db2ba321de2cd653c4e385bc8fd9d3` |
| `manuscript/chapter-38.md` | The Call | Kiva; Rhea cutaway (1,102) | 4,959 | `6da5913a77af4de57f94befcba77d5e6ca6407653c2826909fdfa933c4e2f9a3` |
| `manuscript/chapter-39.md` | Price First | Kiva; Perrin cutaway (836) | 6,384 | `b6fdda5700f577ee72028e1aa08b03c517cfe94d5b4084dc67ac9daf759a9b9d` |
| `manuscript/chapter-40.md` | Hand as Before | Kiva | 6,699 | `5a2c428f2c7bfd4a78b3ab7170eb8a0f4577b13da51e9a01f56c5e6e33a29371` |
| | | **Movement Five total** | **45,623** | |

Secondary-viewpoint sections total about 6,250 words across six people (Vane about 1,370,
Anwen 1,199, Rhea 1,102, Kellan 986, Perrin 836, Orla 758), about 13.7%; Kiva holds about
86.3%. Every one of the six has been a viewpoint in an earlier movement; none is new. The
eight chapters have 46 sections (about 990 words a section). These are plain section word
counts, not craft measurements.

### What was written

Chapter 33 settles two of the waiting matters and starts the count again. The Home Line watch
hears Kiva's entry, votes down a recall two to five, and writes that the plate is neither
equipment nor evidence; Hollis Vane takes that to Mara's kitchen and is given tea and no
forgiveness. Selka Dray brings the tape of the stack to the Chair; Kiva says "She's right" and
asks for a pen on every floor; the objection is upheld in one part. Ysra Crest watches the
third counted crossing from a folding stool and writes *I cannot tell.* Chapter 34 is the
hearing on the red-tagged bag (three seals, the street advanced its half, a general red-tag
rule for catchers, a ban on stepped ash on Circuit floors, the patent sent to a court) and the
ruling that no crossing counts without the tape. Kellan says in that room whose seal he is
entered under, and visits his mother's grading bench. The Order of the Even Hand offers a
year's rest and one door, and Kiva declines it knowing what it might have saved. The fourth
crossing is made on a hollow floor after a step that was not clean. Chapter 35 completes the
six with exactly a hundredth left in the glass, the last one made slowly when a stack would
have been thrift; Orla adds one bounded line to the certificate and states the three ways
three doors can be had. Anwen finishes her line, is asked rather than assumed, and takes the
Hold on terms. Perrin votes no to the three-door ash and is asked what he would buy instead.
Chapter 36 is the training: a jam caused by two fingers that could not feel a ward's rim, Pru
Finch's fold, a first hand-to-Ember crossing, an *off,* a stack that Kiva calls on herself
before her reader, and one clean sequence in the Old Yard; Perrin proposes the ash he refused,
with his own brake. Chapter 37 is the Regional's first day: a lane won against Lowen Brask's
"hold" by taking a corner, a lane lost to Halden when Kellan meets Kiva in the gap at the top
of her one permitted crossing, and a Bench that Seven stands without her. Chapters 38–39 are
the Pit: the Call, four husks that stand a hold round a tear no designer ordered, Selka Dray
pinned by its cord, the event struck, each remedy refused by the person who knows why, and a
three-door catch made under a field direction with the cost read out first. Perrin carries
Dray out; Kellan declares for Seven under rule nineteen and cuts a post with Jude and Gower on
Kiva's word; Anwen calls a student gate for a Flask; professionals close the tear and cut two
strings; Seven bags a rung with Pru's hands on the cord. Chapter 40 is the reckoning: a slate,
a pooled and fair ledger, a Regional read on three boards with Seven fourth, the Chair's entry
"because it occurred," the healer's verdict that the two fingers are not coming back, a grip
that depends on a word said to somebody else, and a pump bank that has been in step for nine
days and is walking a trunk toward the school.

Held back as the packet requires: the disk stays cold and neither it nor the dream supplies a
tactic; no fever and no recurrence; nothing explains the filter, the Makers, the disk's origin,
the stepped ash or the hold; the three-door configuration is done once in public, briefly,
under a direction, and is left uncertified, unclassified and unmastered; no rank changes; the
fingers are not restored by ash, rest, rank or result; every crossing is paid at 0.31 from the
glass at no more than one a week with the hand seen the next morning, and the last hundredth
is carried into the book; the sealed medical reserve is not opened; Kiva is seated outside
recovery in no sanctioned event; Kellan keeps his Halden pledge until the floor is struck;
Anwen serves out her line; no new secondary viewpoint is added.

### Not done in this run

No editorial review, cold read, repair pass, metric scoring, frozen edition or narration, and
no commit, push or publication. The formula's sentence, paragraph, readability,
progression-vocabulary and development-cadence targets were written toward and **have not been
measured** for these chapters. Nothing here should be read as a passing score. Word counts,
section counts and hashes above are mechanical facts for the record, not an assessment.

During drafting the author corrected continuity slips only, as the task allows, by small
exact-string edits made directly after each chapter was written and once more while the
records were compiled: Vane's age in 2669; what Ione Rowan died of in relation to "that Line";
Kiva's age when Mara burned her palm; the date of the first Great Floor attempt; one minor
name (Stiles); Kellan's "kneeling"; the count of Kiva's visits to the hall, Orla's years on
the Line, "a week ago," and how long the hall panel had been dark; the hour of the Bench;
lane calls that named schools where they should name teams; the third carry against Old Four,
which now ends with the litter home and not at time; Kellan's later rounds; when the feeling
returned on the Friday; the order of the first company on the board; how many purse sheets
Kiva has knelt at; how often Aske has eased her hand; the hour of the catch; how many times
Dray objected; who wrote the 2676 deferral; the Ferren's vote; Dray's leg a week on; Rhea's
count of rungs; Anwen's place being for next summer and not on leaving school; the trunk's
dates; and, last, **the number of three-door misses (three, not four) in chapters 36 and 39
and the number of mast crossings (seven, not nine) in chapter 37.** None of this was a review
or a scored pass. One planned element changed while drafting: the lane bracket was shortened
so that Seven meets Old Four first and Halden second, with no third round.

### Choices the owner should review

Full list in `provenance/MOVEMENT-005-CONTINUITY.md`, section 9. The largest:

1. **The stronger variety is "a hold":** four husks standing a square, in step, with a tear
   inside it and outside any lattice, echoing the Home Line's own held tears. Nobody says who
   showed them. This is the movement's largest invention.
2. **What three doors did in public was a catch:** hand, Ember, still, as catch, carry, plant;
   a loaded cord taken off a pinned rival, held as a corner for ten counts, and released on
   the same word as three student cuts. The one new claim about the gap, that work crosses it
   and a stepped count does not, is felt once and measured by nobody.
3. **The permanent finger loss follows three shown choices** (the Order's year declined; the
   week's crossing spent in a lane; two gaps the next day against a healer's card, price
   first) and is confirmed a week later as beyond ash or rest.
4. **An earlier bearer crossed.** Thirza Bly's line of the 2460s: warm once, after the first
   crossing; cold through nine more. No cause, door or use.
5. **Ysra Crest signed Jessamy Hart's entry in 2660** and stood on that Bench as a ward-holder.
   Orla has written to Hart.
6. **The hearing's seven rulings,** including a general red-tag rule and a Compact court.
7. **The Regional's design and result:** sixteen fours, four boards, the Great Floor, the Call;
   the Call struck; Halden first, Seven fourth, attached still, with no professional offer.
8. **Kellan declares for Seven on a struck floor** by rule nineteen; his return to Halden's
   yard is left open.
9. **The months are numbered on the page** for the first time (fifth to ninth).
10. **The hook into Movement Six** is a municipal pump bank stuck in step and the Step walking
    a trunk toward the Crooked Line's core house in about eighteen days.
11. **Movement length is 45,623 words,** at the foot of the working range; secondary viewpoint
    is about 13.7%, a little over the formula's 13%.

## Movement Five consolidated repair — 2026-10-11

- Status: **one bounded same-author repair applied to chapters 33–40, then targeted-rechecked.** The
  first draft is frozen, unchanged, at `editions/movement-005-pre-repair/` (its
  `SHA256SUMS.txt` verified before the first edit, after the last prose edit, and again after
  the records were written). This section supersedes the first-draft section's statements that
  the movement is unreviewed, unmeasured and has no frozen edition; the rest of that section
  describes the first draft as it stood.
- Repairing model: **Claude Opus 5.5 (`claude-opus-5-5`)**, the same model that wrote the
  first draft, as reported by the runtime environment. **No subagents, workflows or other
  models were used**, and no other model wrote or revised prose.
- Provider: Anthropic, via Claude Code (Claude Agent SDK), non-interactive session
- Session: Claude Code session `433a93b1-1ba4-4c05-9e32-7132cb480100` (the identifier in the
  session's own tool-result path). A new session, not the drafting, editorial or cold-read
  session. It began about 23:12 MDT on 2026-10-11. Its first turn read every required file,
  verified the frozen edition and extracted the earlier metric scripts, then was interrupted
  **before any file in the repository was touched**. The same session resumed at 23:26 and
  made every edit between about 23:35 and 23:49. This is one repair pass, not two.
- Instructions: `editor/MOVEMENT-005-REPAIR-BRIEF.md`
  (SHA-256 `93aa7e683d6794318c8370f27009555d4940b9d42208a71b32181fecf57fd2c9`), read in full.
- Reviews the repair answers, both read in full: `editor/MOVEMENT-005-EDITORIAL.md`
  (SHA-256 as read `0f29cc663050edb4c7c0108c62835cded92ec8397f449678fa5c33cf633ff7c6`; an
  informed same-model editorial review; it already showed as modified against `HEAD` when
  this session began, and this session did not edit it) and
  `editor/MOVEMENT-005-COLD-READ.md`
  (SHA-256 `820ba86d57da9381cd905232540e876001943f352027cf77a299d101f353824d`; a simulated
  cold read). Neither is a human read.
- Read in full before the first edit: the three files above; the frozen `SHA256SUMS.txt`;
  chapters 33–40 (the working chapters were byte-identical to the eight frozen files, checked
  with `cmp`, so one reading covered both); `provenance/MOVEMENT-005-CONTINUITY.md`;
  `STATE_LEDGER.md`; and the Movement Four and Movement Five sections of this file, with
  `editor/MOVEMENT-004-REPAIR-REPORT.md` for the report's form.
- Also consulted, by line lookup only, to anchor repaired references in what is already on
  the page: chapter 25 (lines 167, 199, 215: the record hand and the clerk R.), chapter 27
  (79–87, 201–207: the Reader's "somebody tidied the third away," said to Vane), chapter 28
  (369), chapter 30 (203–231, 419: Finch on the curb; Rhea's seconds), chapter 31 (181: the
  two-word card), chapter 32 (9–21, 341: the disk worn four years), chapters 3 and 8 (Jessamy
  Hart), the Movement Four checkpoint (the dates of the first four goes), and a count of how
  chapters 1–32 name "the Works."
- Method: targeted in-place edits, 72 in all, each an exact-string replacement that aborts
  unless it matches once. No chapter was rewritten whole. No scene, section break or
  viewpoint was added, cut or moved; the movement still has 46 sections and six cutaways.
  One short paragraph (the lamps on the dead rim) was moved earlier inside its own scene in
  chapter 39, as the brief's notch item requires.
- Records reconciled to the repaired prose: `provenance/MOVEMENT-005-CONTINUITY.md` (new
  section 0 lists the changes; SHA-256 after reconciliation
  `9f0c7f8e170435b6c461b1bfe05dca53e4b566da0f7e0fdcf38bacb0c46d297e`) and the Movement Five
  block of `STATE_LEDGER.md` only.
- Repair report: `editor/MOVEMENT-005-REPAIR-REPORT.md`.
- **Targeted recheck:** a fresh Claude Opus 5.5 review-only session read the repaired
  chapters and frozen comparison, passed all three priorities, and identified five
  clause-level prose corrections plus two record corrections. All seven were applied before
  acceptance; no second repair pass was opened. See
  `editor/MOVEMENT-005-TARGETED-RECHECK.md`.
- **Not done at this point:** no commit, push, publication or narration; no Movement Six.
  Neither review report was altered. The working tree holds the accepted repair uncommitted,
  on `worktree-kindling-2680-prologue-m001-opus55` at `a0922ea`.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `manuscript/chapter-33.md` | 5,091 | 5,211 | +120 |
| `manuscript/chapter-34.md` | 5,844 | 5,849 | +5 |
| `manuscript/chapter-35.md` | 5,703 | 5,715 | +12 |
| `manuscript/chapter-36.md` | 5,764 | 5,817 | +53 |
| `manuscript/chapter-37.md` | 5,179 | 5,238 | +59 |
| `manuscript/chapter-38.md` | 4,959 | 5,047 | +88 |
| `manuscript/chapter-39.md` | 6,384 | 6,555 | +171 |
| `manuscript/chapter-40.md` | 6,699 | 6,829 | +130 |
| **Movement Five total** | **45,623** | **46,261** | **+638** |

Nothing was cut for length. Every protected line named in the brief is present word for word.

### Post-repair SHA-256

| File | SHA-256 |
|---|---|
| `manuscript/chapter-33.md` | `a85120c11223b76906ec49d54ef6c6bcadafe9d2f90e8f32ef25db9ffb335b03` |
| `manuscript/chapter-34.md` | `92ccd37798c12cf65a2cd25202e6c32b01bf8b063d6a0f23fc14a29b30c20353` |
| `manuscript/chapter-35.md` | `2ca89608564470b1fc6602f6980904ede07d5ec3badd92720f871bac96d27cf3` |
| `manuscript/chapter-36.md` | `a7447f5e648b1cf7eceaa01620e36e9f4809d7aec1cb6ed0be127e5cd2fc89b3` |
| `manuscript/chapter-37.md` | `df3d4e59758cd08d5cdde2c3a0ab5c1426e2d8952743301387762979553475df` |
| `manuscript/chapter-38.md` | `38b1392ec4fcea2fd4f6256b0f806662b228aa7be26642b29c2c4d38914c27cd` |
| `manuscript/chapter-39.md` | `7ace9058c3849434bd458e5d8f06b980cc8efcf1df0faee699a1b7a5e9a55234` |
| `manuscript/chapter-40.md` | `cd92f4b78c121a6c3b388246c0ae8cf94dd8f140ba0f6324dba0df90f33e0d08` |

### Measurement (shared definitions of Movements One to Four; not a gate)

One stdlib script (`metrics_m005.py`, SHA-256
`39339c2a0c51e5678c4d370df9c8ac326a10ab13b224aec391afe706e1b3f67e`, kept outside the
repository and printed in the repair report) loads the Movement Three script's definitions
unchanged, so the word regex, sentence tokenizer, syllable estimator, Flesch formulas and
the narration / speech / ledger rule are the ones used for Movements One to Four. It was run
on the frozen files and on the repaired files. The first draft had not been measured before.

| Target (formula) | Goal | First draft, ch. 33–40 | After repair, ch. 33–40 |
|---|---|---:|---:|
| Mean sentence length | 14.6 | 9.06 | 9.12 |
| Median sentence length | 11 | 7 | 7 |
| Sentence spread (population s.d.) | ~26 | 7.67 | 7.69 |
| Sentences ≤5 words | 27.7% | 42.5% | 42.2% |
| Sentences ≥40 words | 3.3% | 0.40% | 0.39% |
| Flesch Reading Ease | 72.3 | 93.8 | 93.7 |
| Flesch–Kincaid grade | 6.8 | 2.4 | 2.5 |
| Narration only: mean / ≤5 / ≥40 | 14.6 / 27.7% / 3.3% | 11.64 / 30.8% / 0.84% | 11.69 / 30.5% / 0.84% |
| Written paragraphs: count / mean / median | — / 26.8 / 18 | 1,623 / 28.1 / 19 | 1,624 / 28.4 / 19 |
| Sections: count / mean words | — / ~950 | 46 / 990 | 46 / 1,004 |
| Protagonist share / secondary | ~87% / ~13% | 86.3% / 13.7% | 86.1% / 13.9% |

Secondary sections after the repair, by word tokens: Vane 1,462 (3.2%), Anwen 1,208 (2.6%),
Rhea 1,139 (2.5%), Kellan 988 (2.1%), Perrin 855 (1.9%), Orla 759 (1.6%).

The whole-text sentence and readability targets are missed by about the same margin as in
Movements One to Four, for the reason already ruled on: speech is 54.7% of sentences and was
left clipped. The repair did not chase them. Paragraph, section and viewpoint figures sit
near their targets; the paragraph and section targets are pause-derived and directional.

### Material choices in the repair the owner should review

Full detail, with before-and-after text, is in `editor/MOVEMENT-005-REPAIR-REPORT.md`.

1. **The corner is carried east, not south-east.** Carried along the diagonal, both walls of
   the hold would sweep across Dray and her two carriers. Carried four paces east along the
   line of the south side, the south wall stays where it stands and they are on its open
   side. It is still four paces outward.
2. **The knot clock is re-rated to a hundred counts a knot,** with Vane's budget at ten
   minutes, the set-up at two minutes and Dray under the cord about a quarter of an hour. No
   line of the consent, set-up, catch, carry or rescue was cut.
3. **The dead rim winks at the instant of "Back,"** which is where the page's own counts put
   eleven seconds after the second cliff. Noa and Adlam now describe sixteen pens "lit and
   dark alike."
4. **Rhea's stand "came too late to govern,"** and Vane states that a Torch keeping a floor
   safe may stand any student on it. The remark stays the event's.
5. **Anwen's forty minutes** runs from the fall of the hold to the closing of the tear.
6. **Perrin's clearance is dated to the end of the eighth month,** and Dray is his first
   person, not his first weight.
7. **An aggregate rule is stated for the first time:** each board marked by place, sixteen
   down to one, and added. Lane scoring (three for the litter, one for a down) is taken from
   the scores already on the page.
8. **Kellan takes Halden's husk and Pettit carries its dummy,** so that Pettit's move to
   Carry holds.
9. **Four knowledge paths are new on the page:** Marten and the Wren House for Dray; Noa's
   filed note for the Chair; Perrin at the Sag for Anwen; the Reader for Vane.
10. **"The Works" unqualified now means neither body by default.** Halden is named at first
    and ambiguous uses; the pump bank is the Municipal Works'. Inside the hearing, after the
    first "Halden Works," the short form is left in Adlam's and the Chair's mouths.
11. **Secondary viewpoint rose from 13.7% to 13.9%,** because the stake paragraph the brief
    asks for sits in Vane's cutaway.

### Movement Five targeted-recheck acceptance — 2026-10-12

- Rechecking model: **Claude Opus 5.5 (`claude-opus-5-5`)**, fresh review-only session
  `fab1091b-a955-49c9-916d-45ef045564f2`; no subagents or substitute model.
- Instructions: `editor/MOVEMENT-005-TARGETED-RECHECK.prompt.md`; report:
  `editor/MOVEMENT-005-TARGETED-RECHECK.md`.
- Verdict: **PASS on all three repair priorities.** Five clause-level prose corrections and
  two record corrections were required and applied without opening another repair pass.
- Accepted word count: **46,277** (`wc -w`), sixteen words above the repair report because
  the recheck explicitly placed Dray's free leg and named two listening referents.
- Accepted chapter SHA-256 values: 33 `0548ec039fd50c0eaafc808bbf6853ae76d3d1f2aa6d62beb608b474d196e4d7`;
  34 `92ccd37798c12cf65a2cd25202e6c32b01bf8b063d6a0f23fc14a29b30c20353`;
  35 `2ca89608564470b1fc6602f6980904ede07d5ec3badd92720f871bac96d27cf3`;
  36 `a7447f5e648b1cf7eceaa01620e36e9f4809d7aec1cb6ed0be127e5cd2fc89b3`;
  37 `f2537ee521190b8eeafd91352aebe44dc0ee8092ca82d01d6b89df9b4113d113`;
  38 `38b1392ec4fcea2fd4f6256b0f806662b228aa7be26642b29c2c4d38914c27cd`;
  39 `97e64284081811dd2925c949305a677491dbd89e097e9e4ba3eb2d5b17c9d893`;
  40 `cd92f4b78c121a6c3b388246c0ae8cf94dd8f140ba0f6324dba0df90f33e0d08`.
- Accepted continuity checkpoint SHA-256:
  `18f62e299615a1c602a1c772016c55648c29596f041faa76c37edbba90f8ff9d`.
- The frozen first draft still verifies against its manifest. This accepted edition is the
  canonical handoff to Movement Six.


## Movement Six — Why It Is Crooked (chapters 41–48)

- Status: **first draft written 2026-10-12 as one continuous creative run. Unreviewed.** No
  editorial review, cold read, metric scoring, repair, recheck or frozen edition exists for
  this movement. This movement completes the first draft of Book One. Book Two was not
  started.
- Seat: Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported by
  the runtime environment of the authoring session ("powered by the model named Opus 5.5. The
  exact model ID is claude-opus-5-5"). Every manuscript sentence in chapters 41–48 was written
  by this model in one Claude Code session. **No Task tool, workflow, skill or subagent was
  used**, and no other model wrote, revised or summarized prose.
- Provider: Anthropic, via Claude Code (Claude Agent SDK), non-interactive session
- Session: Claude Code session `79b5006a-0ec6-4a2d-b6cd-75ff1285a165` (the identifier in the
  session's own tool-result path; no web address for it was visible to the author). A new
  session, not any earlier drafting, review, repair or recheck session. By the machine's
  clock it ran from about 00:21 to about 01:25 MDT on 2026-10-12; by file timestamps the eight
  chapters were first written between 00:39 and 01:10 and last corrected by 01:16.
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-006.prompt.md`
  (SHA-256 `39e2fb7abbddd6c8a25b438be9ea2f0eff0b4b64f6d4fd83b8b34914dd886f66`), read in full
  (all 2,227 lines) before drafting. The prompt embeds chapter 40,
  `provenance/MOVEMENT-005-CONTINUITY.md`, `STATE_LEDGER.md` and the owner-voice seed; those
  were read there.
- Movement packet: `packets/MOVEMENT-006.md`
  (SHA-256 `2086f0b3fa92e5f525d8c49225a873d735a5633c2f208ed1c69f9a523f8b0073`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (re-hashed in this session; matches the hash recorded in the compiled prompt)
- Edition: Book One, Movement Six, first draft (2026-10-12). **No frozen edition exists for
  this movement.**
- Branch: `worktree-kindling-2680-prologue-m001-opus55`, at `1d8c9f0` ("Prepare Kindling 2680
  movement six") when the run began. **The author made no commit and no push.** Another
  process committed each chapter shortly after it was first saved: `3048a59` (41), `fb06b40`
  (42), `fe8ef85` (43), `adb81c3` (44), `9f01f10` (45), `9b9db38` (46), `5cb341b` (47) and
  `465d48b` (48), each titled "Draft Kindling 2680 chapter NN." **Those commits hold the text
  as first saved. The author afterward made continuity corrections and two additions in the
  working tree (listed under "Not done in this run"), so for chapters 43–48 the working tree,
  and the hashes in the table below, are ahead of what was committed.** Anything published
  from those commits should be refreshed from the working tree. At the time of this entry the
  six chapters, `STATE_LEDGER.md` and this file were modified and the checkpoint was untracked.
- Continuity checkpoint: `provenance/MOVEMENT-006-CONTINUITY.md`
  (SHA-256 at the time of this entry
  `11b53ca959675fe5a34c2c08a828c4fc4642d6df74b18c8e0815bd2d5fd0f427`)
- State ledger: `STATE_LEDGER.md`, new section "Movement Six carried state (chapters 41–48) —
  end of Book One."
- Also read in this session, beyond the compiled prompt: **accepted chapters 33–39 in full**
  (chapter 40 is in the prompt), as the packet requires; `universe/NAME_REGISTRY.md`,
  `BOOK_MAP.md`, `SERIES_MAP.md` and `CHARACTERS.md` (in full); and sections or line-level
  excerpts found by search: `UNIVERSE_BIBLE.md` (the Unroofed Sky; the energy history; the
  artifacts); the prologue (the reasons column and "the lane with the crooked posts"; the 2603
  committee and the superseded stacks; the 2247 compact core);
  `provenance/MOVEMENT-002-CONTINUITY.md` sections 4–5, `MOVEMENT-003-CONTINUITY.md` sections
  4–5 and `MOVEMENT-004-CONTINUITY.md` sections 4, 5, 7 and 8; every mention in chapters 1–40
  of the leaning post, the core house, a core, Barrel, Saltmere, the anniversary, the 2604
  entry, Rusk, Bettan, Doran Mace, Hendry Moss and Ostrey; the section headings of this file
  and its Movement Five entries.
- **Not read in this session:** chapters 1–32 other than the excerpts above;
  `provenance/MOVEMENT-001-CONTINUITY.md` beyond searched lines; `IDEA.md`, `README.md` and
  `PROLOGUE_PLAN.md`; the editorial reviews, cold reads, repair briefs, repair reports and
  rechecks of any movement. Their canon was taken from the checkpoints embedded in or cited by
  the prompt. A review should weigh that when it checks voice and small facts.
- Disclosed: session start-up injected project memory (a stale Movement One handoff, a
  recent-activity summary, and a list of earlier observations, one of which describes a
  48-chapter whole-book review that belongs to some other session or book). None of it was
  used as evidence for story facts, and no memory or work-state tool was called. The author
  kept no scratch file; the route was held in the session and is now superseded by the
  checkpoint.
- Premise and owner names: confirmed available before prose (Kiva Rowan, Mara Rowan, Orla
  Dane, Anwen Pryce, Perrin Cade, Kellan Renn, Noa Bexley, Ysra Crest, Rhea Sorn, Hollis Vane,
  Lowen Brask, Selka Dray, Jude Talley, Pru Finch). No locked name was changed. New minor
  names (Ansty, Lumb, Ned, Yeo, Garland, Admiral, Bettony; the place names Stopgate and the
  Kiln loop; the initial in "A. Renn") were checked by search against every book's manuscript
  and registry in this repository and `universe/`; none matched. One first choice was dropped:
  "Tam," too near Tamar Vey of the universe bible, became Ned. "Ostrey" was considered for a
  third Graywater blade and not used.

### Files

| File | Heading | Viewpoint | Words (`wc -w`) | SHA-256 |
|---|---|---|---:|---|
| `manuscript/chapter-41.md` | Not the Copper | Kiva | 7,250 | `5f8cb0aacec4f9f62e6d92b21cd641eddda2bbb3741547df045dd8da17001b1e` |
| `manuscript/chapter-42.md` | The Ninth Post | Kiva | 6,408 | `60cd5291f62137f77d94e668bb297ba847a8b852a35807367d6121a1c82d3a80` |
| `manuscript/chapter-43.md` | A Drain in a Box | Kiva; Kellan cutaway (1,035) | 6,853 | `3ab68ff5e796349b64b641506734e6c28873b6f61586a171e29fad7ab6200cb7` |
| `manuscript/chapter-44.md` | Two to the Bar | Kiva; Rhea cutaway (1,131) | 5,572 | `e0ef75033f437348d3b3e11c1873aa15c6a3cf170f7f1010a48fad43fa9c64c4` |
| `manuscript/chapter-45.md` | Paid Out | Kiva; Anwen cutaway (1,294) | 5,147 | `45209fc0e4abd57d83552fafaebfa685f96a148c40a7aa49614084276cfc0cf4` |
| `manuscript/chapter-46.md` | Call the Turn | Kiva; Perrin cutaway (863); Mara cutaway (1,730) | 7,175 | `7f154f83eeaf430b98fca1c2e49e4838b9d2fca0211fb967b9aeff96c72a34ed` |
| `manuscript/chapter-47.md` | Entered as Such | Kiva | 5,907 | `335e89f86a309ad3966ec5b5b0d9c52f1b5fcab272e2fe74e0c12b7ea1c062b9` |
| `manuscript/chapter-48.md` | Why It Is Crooked | Kiva; Orla cutaway (439) | 6,554 | `7902237b16c8dc5f882acac6cfe990abda96faff38f24958abfd3f7520753b39` |
| | | **Movement Six total** | **50,866** | |

Secondary-viewpoint sections total 6,492 words across six people (Mara 1,730; Anwen 1,294;
Rhea 1,131; Kellan 1,035; Perrin 863; Orla 439), about 12.8%; Kiva holds about 87.2%. Every
one of the six has been a viewpoint in an earlier movement; none is new. The eight chapters
have 44 sections (about 1,156 words a section). These are plain section word counts, not craft
measurements.

With the accepted counts already recorded in this file for the prologue and Movements One to
Five, this draft brings Book One to its 48 chapters. The whole-book total was not recomputed
in this run.

### What was written

Chapter 41 turns the inherited clock over. Three bells ring with no tear under them; the
Step is found to be walking the Ferren storm drain, not the copper, when drum twenty-five
falls in out of its turn; the Municipal Works tries a firebreak of two dry drums, and Mara
puts a dated prediction under the Chair's seal. Team Seven lends to the casualty reserve,
buys Pru Finch a sheet of her own, and hears that Kellan has taken the Halden yard. Perrin
holds 380 kilos. Chapter 42 is preparation: Mara's floats, Pike's yard (Pru catches, Kiva is a
corner and lists every handoff her hand needs), and Vane's evacuation walked in the dark,
where two litters strike the leaning post and Kiva has the bearers call it for themselves.
The drain plan turns out to have been tidied. Chapter 43 is the controlled drill in the
Halden license yard: a contained string ignores a lit gate for water that keeps time, a clean
cut cooks a bench bank, and the string goes on pumping the trough with the pump dead. Kiva
calls a slack with a hand that cannot hear and nips Pru's fingers. The Library and the Home
Line's lane sheet give the post's what and why; drum twenty-eight falls in on the day Mara
wrote down. Chapter 44 digs up the sluice, takes twenty-four pinches from the reference shelf
and refuses two other sources of ash, gives Rhea Sorn a sixth column and Selka Dray the count,
and ends with a tear lying down in Stopgate. Chapter 45 is the night's first half: the
evacuation, Rhea's two cuts and the discovery that the string is being paid out, Anwen's
walking wall, and the arm reaching the one hole that could not be planked. Chapter 46 is the
answer: the price first, the mark turned north, catch, carry and plant, the corner given to
three still-doors, two to the bar, twenty-four cells quenched and filled on twenty-four
counts, and *back.* Chapter 47 closes the ledger of the night: the sealed reserve opened for
Mara's reading hand, the keeper's book of 2604, the slate and the pot, the arm's return, and
Noa's three columns. Chapter 48 closes the book: the Line's roll, the School's plaster cast
and the Reader's recognition, "seated," Rhea Sorn's bounded card, the last entry, Jessamy
Hart's four lines, and fourteen juniors running the lane to the bar.

### Not done in this run

No editorial review, cold read, repair pass, metric scoring, frozen edition or narration, and
no commit, push or publication by the author. The formula's sentence, paragraph, readability,
progression-vocabulary and development-cadence targets were written toward and **have not been
measured** for these chapters. Nothing here should be read as a passing score. Word counts,
section counts and hashes above are mechanical facts for the record, not an assessment.

During drafting the author corrected continuity slips only, as the task allows, by small
exact-string edits made after a chapter was written and once more while the records were
compiled: a garbled line of Mara's and the hour of the *Held* notice (41); Hendry Moss, who is
not a first-year and not lanky, three counts of landings and scratches on the cross that the
page could not support, and "six hundred years" of students (42); Ruddock's presence at the
drill and the age of the lane sheet (43); who pulled Rhea Sorn from the culvert and Pike's
years (44); the spacing of the knots, changed from six paces to eight so that twelve fit the
hill (44); the count of knots after two cuts, the names of the later ones, and one minor name
(45); the number of still-doors on the corner, the length of time that they held it, and
**the notch, which the first text put at the instant of *back* and which now falls eleven
seconds after the second cliff, five minutes before the lamps** (46); Noa's first sight of the
plate, which the first text put in a movement where he does not appear (48); and two idioms.
**Two passages were added to complete what the packet requires and are not corrections:** in
chapter 47, Kiva's minute at the gateway (the last string on Anwen's wall and the Home Line's
closing crew at work) and Bettan's "Closed!"; in chapter 48, the last entry of the team book,
with Sorn's card put to the four. None of this was a review or a scored pass.

### Choices the owner should review

Full list in `provenance/MOVEMENT-006-CONTINUITY.md`, section 9. The largest:

1. **The Step walks a storm drain.** Three stepped pumps make the Ferren main rise and fall;
   drums fall in in the order the water reaches them. Shown by order, a sealed prediction and
   a bench trough; never stated as a law.
2. **The crooked post is the handle of a sluice gate,** on a lane laid over a drain that
   turns. The prologue's line (*because the road isn't straight. S.V.*) is unaltered; the
   method comes from a Home Line lane sheet. The street is called Stopgate.
3. **The new spawn expression has no name and no yield class:** a string laid on its side,
   paid out of a tear held by the drain, which pumps the main once it has an arm in water.
4. **Kiva's third three-door** is offered and not asked, carried across the haul to ground
   that she tested, and **handed to three other students at about nine.** The arm is lost for
   four days and returns; the fingers are as before.
5. **The sealed medical reserve is opened once, for Mara Rowan's reading hand.**
6. **The answer is local and provisional:** one bank out, seven drums waiting, one fouled,
   Saltmere's still in step.
7. **Kiva's place** is the Home Line's roll and the Chair's "seated"; the brackets come off
   Seven and Old Four.
8. **Rhea Sorn's offer** is two nights a month as a catcher's second, for three months.
9. **The disk** is recognized through the School's plaster cast, by the Reader, as the plate
   of the first teachers; it stays cold.
10. **The historical echo is a pump keeper's book of 2604,** not a Glory master's.
11. **Saltmere's bank fell in the same minute,** Jessamy Hart answers, and the first company
    goes to a National Measure at Saltmere in the third month of 2681.
