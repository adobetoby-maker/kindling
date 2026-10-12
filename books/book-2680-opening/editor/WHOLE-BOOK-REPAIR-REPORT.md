# Kindling 2680 Book One — whole-book canon reconciliation report

> Built by TAC

Date: 2026-10-12
Brief performed: `editor/WHOLE-BOOK-REPAIR-BRIEF.md` (SHA-256 `e76223c2f06a42a8aa00c6c7875bc296df15788e3bbe0f7ce1e3c8175212fdc6`)
Author: Claude Opus 5.5 (`claude-opus-5-5`), the model that wrote the book. Claude Code session `0deb8efc-acbf-419b-8426-ea8a81183e21`, resumed; the same session made the Movement Six repair. No subagents, no workflow, no skill, no other model.

**Status: reconciled, not rechecked.** Five cross-movement seams were corrected at clause level, in nine manuscript lines across five chapters. The result was not reviewed, scored or measured, and the changed chapters were not reread end to end. The checks made afterward were mechanical: one match per edit, a line-by-line `diff` against the frozen edition, word counts and hashes. Nothing was committed, pushed, published or narrated. Book Two was not started.

## 1. What was read

In full, before any edit: the brief; `editor/WHOLE-BOOK-EDITORIAL.md` (SHA-256 `3565a9b2c317c722bef1004a53c5190c1389e9411664cca57ad8eef9a5ddd91f`, 526 lines); `editor/WHOLE-BOOK-COLD-READ.md` (SHA-256 `0091748bffd0c8f431460dfcb438f941b7db8de908c0b660ce789a33bdf2d5ae`, 199 lines).

The manuscript passages around every location, read from the current files:

| Seam | Passages read |
|---|---|
| 1 | Chapter 8, 291–319; chapter 31, 179–185; chapter 48, 193 |
| 2 | Prologue 1071; chapter 32, 225; chapter 48, 49–57 and 83–91 |
| 3 | Chapter 8, 269–299; chapter 23, 445 and 501–507; chapter 31, 181; chapter 44, 157 and 193–199 |
| 4 | Chapter 14, 100–124 and 160–200; chapter 24, 9–21, 165–195, 285–330, 375–392 and 533–539; chapter 31, 119; chapter 35, 365–369; chapter 44, 131; chapter 47, 55; and every later line that names the sealed reserve, by search (chapters 40, 41, 46, 47, 48) |
| 5 | Chapter 48, 463–481 |

The record lines that were candidates for change were read before they were touched: the lines found by searching `STATE_LEDGER.md`, `CHARACTERS.md` and the six continuity checkpoints for the card, the cast, the culvert, the reserve, Hart and the hall panel. For the hall-panel question the Movement One and Movement Two calendars were read (Classification Day to the exhibition) with chapters 36, 38 and 39.

Not reread: the rest of the manuscript. I read chapters 41–48 in full earlier in this session, during the Movement Six repair; chapters 1–40 I have seen only at the lines above and those listed in the Movement Six repair report.

## 2. Frozen edition

`editions/book-one-pre-whole-book-repair/` holds 49 manuscript files and `SHA256SUMS.txt`. All 49 matched the sums before the first edit and after the last record was written. The sums file itself is unchanged (SHA-256 `f2f0616d324faca1daf50719496a39d637e20361fe717ed1f70fd4ed679176c7`), and `git status` shows nothing under `editions/`. Before the first edit I compared eleven working files with their frozen copies and all were identical; after the edits a `diff` of all 49 shows only the nine lines in section 4, so the whole working manuscript began identical to the frozen edition.

## 3. Files changed

**Manuscript (five files, nine lines):** `manuscript/chapter-08.md`, `chapter-24.md`, `chapter-44.md`, `chapter-47.md`, `chapter-48.md`.

**Records (seven files):** `STATE_LEDGER.md` and `provenance/MOVEMENT-001-CONTINUITY.md` through `MOVEMENT-006-CONTINUITY.md`.

**Written or appended:** this report; one appended entry in `AUTHORSHIP.md`.

Not touched: the frozen edition, the other 44 manuscript files, both reviews, the brief, every prompt and packet, `BOOK_MAP.md`, `UNIVERSE_BIBLE.md`, `CHARACTERS.md`, and every movement-level review, report and recheck. An untracked file, `.wba-compact-state.json`, was in the working tree when this work began. It is not mine and I did not open or change it.

## 4. The five seams, before and after

A `diff` of every manuscript file against the frozen edition shows exactly these nine changed lines and no others.

### Seam 1 — Rhea's two-word card

| Location | Before | After |
|---|---|---|
| `chapter-08.md`:319 | `*Corran's disk.*` | `*Corran's. Mine.*` |

Chapter 31 ("They were the wrong two words") and chapter 48 ("One of the two was *mine*") are unchanged and now agree with it. Rhea's bounded offer and "I'd like you to notice that I can learn" are untouched.

### Seam 2 — the plaster cast's scale

| Location | Before | After |
|---|---|---|
| `chapter-48.md`:51 | "In it lay a disk the size of a penny, of a dull white," | "In it lay a disk the width of a palm, of a dull white," |

This matches the prologue ("about the width of Kiva's palm") and chapter 32 ("the width of her palm"). The rings, the flaw, the label, the Reader's recognition and the custody limit are unchanged.

### Seam 3 — Rhea's culvert date

| Location | Before | After |
|---|---|---|
| `chapter-44.md`:195 | "a culvert on the Ferren in the autumn of '64," | "a culvert on the Ferren in the spring of '57," |
| `chapter-44.md`:197 | "She had been glad of that for sixteen years." | "She had been glad of that for twenty-three years." |

The year follows from chapters 8, 23 and 31: nineteen, the spring floods, twenty-three years since, counted back from 2680. The rest of the cutaway is unchanged, including "She had been a casualty. The girl was not a casualty."

### Seam 4 — the two-dram medical reserve

| Location | Before | After |
|---|---|---|
| `chapter-24.md`:309 | "…lying on the table. "It stays ward. Nobody breathes on it."" | "…lying on the table. "And not this ash. I heard that seventh reed, and I'll not seal a thing that keeps time for somebody's nerve. The reserve's quarter of our own Sag Handful is still at the Wren House; I asked. Ward-trace and nothing else. Two of ours go into the casualty stock, and two of that come out to us, at par, on the book, where anybody can read it. It stays ward. Nobody breathes on it."" |
| `chapter-24.md`:385 | "*Sealed, medical, W: 2.0. Returned, Wren House infirmary…" | "*Sealed, medical, W: 2.0, changed at par at the Wren House for plain ward-trace of the Sag Handful's reserve. Returned, Wren House infirmary…" |
| `chapter-44.md`:131 | "a husk on the Sag in the fifth month, before any of this got into the ash." | "a husk on the Sag in the fourth month, before any of this got into the ash." |
| `chapter-47.md`:55 | "It came off a husk on the Sag in the fifth month." | "It came off a husk on the Sag in the fourth month." |

What this rests on, all already on the page:

- The Sag Handful graded Second, *W-trace,* with no induction. Its casualty reserve share was 2.6 drams (chapter 14, the ash-office slate), so two can come out of it.
- The Pit's rung graded *W, full. I, trace,* and all four of the team were in the grading room when the seventh reed tapped (chapter 24). Halloran's card is unchanged.
- The Sag license day is Sunday the 28th of the month before the Pit's, and chapters 38 and 39 call the Pit "the twenty-ninth of the fifth month." That makes the Sag husk the fourth month.

No total changed: the entry still sums to 9.6, with 2.0 sealed, and the later 1.2 drawn and 0.8 re-sealed stand. Jude asking aloud, Anwen's refusal, the comb's seventh reed lying still in chapter 47 and Aske's "first time that I've been glad you kept it" are unchanged. Jude's "It's sat under wax for five months" was left: from the 28th of the fourth month to the 4th of the tenth is five months and a few days.

### Seam 5 — Hart-card knowledge at the ending

| Location | Before | After |
|---|---|---|
| `chapter-48.md`:469 | "There was a pump-fitter on the south coast who knew a thing by his bad hand," | "There was a pump-fitter on the south coast, though she did not yet know it, who knew a thing by his bad hand," |

The card stays with Orla. Chapter 48 lines 449–468 (the juniors' run) and 470 to the end (including the final two paragraphs) are byte-identical to the frozen edition. Line 469 differs by that clause alone.

## 5. Record lines changed

Each was changed because one of the five corrections made it false, except where marked.

| File | Change |
|---|---|
| `provenance/MOVEMENT-001-CONTINUITY.md` | The private card's words, twice ("Corran's disk" to "Corran's. Mine."). |
| `provenance/MOVEMENT-002-CONTINUITY.md` | The same, twice. |
| `provenance/MOVEMENT-003-CONTINUITY.md` | The card's words, twice. The quoted team-book entry of the 2nd now carries the exchange. One new bullet under it states that the sealed 2.0 is Sag Handful reserve ash and not Pit ash. Item 16 notes chapter 24's 82 added words. |
| `provenance/MOVEMENT-004-CONTINUITY.md` | The card's words, once. |
| `provenance/MOVEMENT-005-CONTINUITY.md` | The hall panel's quenching: "the 13th of the fifth month" to "the 13th of the fourth month," with the reason. See below. |
| `provenance/MOVEMENT-006-CONTINUITY.md` | Section 9, item 20: the culvert is "the spring of 2657, at nineteen," not 2664. Item 19: the word count. One new paragraph in section 0 naming the five seams as this movement's chapters now have them. |
| `STATE_LEDGER.md` | One line in the Movement Three block: the sealed 2.0 is plain ward-trace of the Sag Handful's casualty reserve, changed at par. |

**The hall-panel date.** The brief allows this only if the replacement is exact. It is. The tag reads "QUENCHED 13TH" (chapter 36); the Movement One calendar puts that on Saturday the 13th, ten days after Classification Day on Wednesday the 3rd; the Movement Two calendar runs from there through Sunday the 28th and Wednesday the 1st to the exhibition on Saturday the 4th; and the Pit is Wednesday the 29th of that following month, which chapters 38 and 39 call the fifth. So Classification Day's month is the fourth. No manuscript line was changed for this.

**Two things in that paragraph of section 0 are completions, not corrections.** No record line gave the cast a size, and every record line about Hart's card was already true ("Kiva has not been told"). The brief names both topics for the records, so the Movement Six checkpoint's new paragraph states them once. No existing line about either was altered.

**Left as found, and worth the owner's eye.** The Movement Five checkpoint's calendar note (line 80) still says that "the month of Classification Day and the Pit is the fifth," and its item 1 asks a reviewer to check that. By the day chain that is wrong for Classification Day. The brief authorizes the hall-panel date only, so I changed that line and not these two. The checkpoint now disagrees with itself in that one respect. The Movement One checkpoint also gives Rhea Sorn's age as 41, where nineteen and twenty-three years make 42; no manuscript line I read states her age, and I left it.

## 6. Word counts and hashes

`wc -w`. "Before" equals the frozen edition.

| File | Words before | Words after | Change |
|---|---:|---:|---:|
| `manuscript/chapter-08.md` | 5,828 | 5,828 | 0 |
| `manuscript/chapter-24.md` | 8,571 | 8,653 | +82 |
| `manuscript/chapter-44.md` | 5,583 | 5,583 | 0 |
| `manuscript/chapter-47.md` | 6,368 | 6,368 | 0 |
| `manuscript/chapter-48.md` | 6,566 | 6,573 | +7 |
| **Book One, prologue and 48 chapters** | **305,042** | **305,131** | **+89** |

Movement Three is now 48,775 words (was 48,693) and Movement Six 51,684 (was 51,677). The other movements and the prologue are unchanged.

| File | SHA-256 before | SHA-256 after |
|---|---|---|
| `chapter-08.md` | `a7afe0d10e5fd278d37bf7dec767c8351534aa24b5028017efdf742b9513ef4f` | `94b38e2926462de2aa962fdc4fd84e3faf0319aa63f55d8048072baba8b947b6` |
| `chapter-24.md` | `d1abe20f486ae48cb295c77dcf955a6e1823e10b2fd08ac225f481268a6332f1` | `07bab974371fcb717dde47ee9e5661fd77fafa4cb9d3b392e7bb57528050a82d` |
| `chapter-44.md` | `0503075fb6cc278f86a93665542f8b358a82f5aafc8979456d48855427389010` | `71c3c9fafc001a1d377c87bbe53f981b01503a1044858456f5d9e0d53b4f863c` |
| `chapter-47.md` | `b649b15974082cbb31992cefe248597a8a7b90d70db74e76be290dbb400fb860` | `457397c3da6cdebce75fb75b022cd127f67c2d303ae93f24758855746c0b7ecd` |
| `chapter-48.md` | `b1b5835358b0fc77a1eb5d3567feadae5dcc5d1e24e19aea48f538ebd228d27b` | `a925832609fb5c13e3ef350ce79a8c4e6ecebc9fcccc41a96d35ea92717373b3` |

Records after reconciliation:

| File | SHA-256 |
|---|---|
| `STATE_LEDGER.md` | `26a516f172e9bf466a5d2cec3a19b734103cfc8593a47498075bee839b6ccd15` |
| `provenance/MOVEMENT-001-CONTINUITY.md` | `b6c89c498891cd8c242ac8bc3c8671c3eb58ce18c458c73acd72ca139fbcdf9b` |
| `provenance/MOVEMENT-002-CONTINUITY.md` | `48dbf24dbb699fef56e3f455ea6e2eebfdf0c2a92d9395a0416ecf1357fde409` |
| `provenance/MOVEMENT-003-CONTINUITY.md` | `7ea1155ff2e1976150f5c56b2eeda9c16eb6de8a08d95e8a440d97745346f012` |
| `provenance/MOVEMENT-004-CONTINUITY.md` | `14a7552e30818e49aa52bfe2ff84e8b8066a1843b376a03a2463079fe6f9a7db` |
| `provenance/MOVEMENT-005-CONTINUITY.md` | `13b42349c5590e8f8f5807e9aa78909bcfd9b730c1d843fea5c84fac03834781` |
| `provenance/MOVEMENT-006-CONTINUITY.md` | `d607fd15a9bf879d3ac9930ef7662ffdf5b3c6b0e429ab0d53a5cfc1d9f1c3b7` |

## 7. Optional notes: none acted on

No optional or future-edition note from either review was acted on. Specifically untouched: the prologue's placement; phrase frequency and refrains ("I want that said," negation-led beats, the "answer ready" labels); the lane-scoring explanation; the anniversary; the lid and filter theory; the Mars rumor; chapter headings; name clusters; the diction seam after Movement One; the third telling of the in-air sequence; the quench-box tag; Halden's claim; "pinned and locked, 2661"; the first-years on the hill; "suspended ten years, restored for eleven"; and Mara's "good skirt" against her "work skirt." The cold read suggests the last two "can ride along" with its first priority; the brief does not list them, so they were left.

## 8. Choices the owner should review

1. **Anwen's new lines in chapter 24** are the only new prose of any length (about 80 words). They add two facts: that the casualty reserve's quarter of the Sag Handful was still at the Wren House five weeks on, and that Anwen had asked.
2. **The team-book entry of the 2nd is entered before the exchange is carried out,** in the same way that the dram returned to the infirmary is entered in the same line.
3. **The year '57** is derived, not found on the page. It is 2680 less twenty-three.
4. **The marking clause** is "though she did not yet know it." It sits inside a passage that the Movement Six acceptance records as byte-identical to the first draft; that is no longer true of line 469.
5. **Earlier checkpoints were edited** for the card's wording (Movements One to Four). They are historical records, and the brief names card wording among the lines to update.

## 9. What is owed

A separate check of these nine lines and their joins, by a session that did not write them. Until then Book One is reconciled and unverified at these five seams.
