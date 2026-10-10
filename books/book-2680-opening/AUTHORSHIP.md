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
