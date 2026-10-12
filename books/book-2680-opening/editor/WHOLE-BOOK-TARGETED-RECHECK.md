# Kindling 2680 Book One — targeted whole-book reconciliation recheck

> Built by TAC

Date: 2026-10-12. Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), review-only, no subagents.
Instructions: `editor/WHOLE-BOOK-TARGETED-RECHECK.prompt.md`.

## Verdict

All seven items pass. The nine changed manuscript lines do what the brief asked, join cleanly
to the unchanged text around them, and create no new contradiction on the page. One record
note in the Movement Five checkpoint is now false against the corrected chronology and is
owed as a mechanical record fix. No prose repair is owed.

| # | Item | Result |
|---|---|---|
| 1 | Rhea's card | PASS |
| 2 | Cast scale | PASS |
| 3 | Culvert | PASS |
| 4 | Medical reserve | PASS, with one optional one-word note |
| 5 | Hart knowledge | PASS |
| 6 | Records | PASS, with two mechanical record fixes owed |
| 7 | Scope and recovery | PASS |

## Independence and coverage

- **Not a fully independent session.** This is the session that wrote
  `editor/WHOLE-BOOK-EDITORIAL.md`. It did not write the repair brief, the repair, the report
  or the authorship entry. Items 3, 4 and 5 answer findings I raised myself, so I am
  predisposed to recognise them as fixed; items 1 and 2 came from the cold read and I had not
  found them. This is same-model verification, not a human read.
- **Read in full for this recheck:** the repair brief, the repair report, the cold read, the
  appended authorship entry, the frozen `SHA256SUMS.txt`, and the complete `git diff` of
  `STATE_LEDGER.md`, `AUTHORSHIP.md` and all six continuity checkpoints.
- **The five chapters.** I read chapters 8, 24, 44, 47 and 48 in full earlier in this session,
  in the text that is now the frozen edition, before a context compaction. For this recheck I
  did not reread them end to end. I verified by `diff` that each current chapter equals its
  frozen copy plus the listed lines, and reread the whole scene around every changed line and
  every passage it has to agree with (listed under each item).
- **Records.** `STATE_LEDGER.md` and the six checkpoints were read in full earlier in this
  session; here I read every changed hunk and searched all records for stale wording.
  `AUTHORSHIP.md`'s first-draft sections were not read at either time.
- `editor/WHOLE-BOOK-EDITORIAL.md` is unchanged from what I wrote (SHA-256 `3565a9b2…`, 526
  lines), so I did not reread it.

## 1. Rhea's card — PASS

- `manuscript/chapter-08.md`:319 now reads `*Corran's. Mine.*`. It is two words, as line 317
  says ("wrote on it only two words").
- It agrees with chapter 31:181 ("They were the wrong two words") and with chapter 48:193
  ("One of the two was *mine.* I'd had no business writing it").
- It fits the scene it closes. The paragraph before lists what the girl might be, ending on "a
  recruit, in five years"; a possessive is the natural wrong thing for Rhea to write next.
- Chapter 48's card ("either of us may say no. No seat is promised. R.S.") and "I'd like you
  to notice that I can learn" are byte-identical to the frozen edition.
- No other manuscript line names the card's words.

## 2. Cast scale — PASS

- `manuscript/chapter-48.md`:51 now reads "a disk the width of a palm," matching the prologue
  (line 1071, "about the width of Kiva's palm") and chapter 32:225 ("the width of her palm").
- It also suits the action that follows: she holds the plate "in her right palm" and sets it
  beside the box for a ring-for-ring comparison, which a penny-sized cast could not support.
- Unchanged and verified by `diff`: nine rings, the wider fifth ring, the flaw across the
  third at four o'clock and its raised thread in the plaster, the chip, the label word for
  word, the Reader's recognition, "No hand but the bearer's," and Noa's drawing.
- No other size word in chapter 48 conflicts.

## 3. Culvert — PASS

- `manuscript/chapter-44.md`:195 reads "the spring of '57" and line 197 "for twenty-three
  years."
- This agrees with chapter 8:299 (nineteen, a probationary, "in the spring floods"), chapter
  23:505, chapter 31:181, and the four "twenty-three years" lines (8:277, 16:303, 23:445 and
  44:157 in the same cutaway). 2680 less twenty-three is 2657.
- It sits correctly against the other dated facts: Ilse Corran "dead for seven years" in
  chapter 8, and Orla's own 2664 reading, which is a different event and still stands.
- "She had been a casualty. The girl was not a casualty. She kept putting her in that column,
  and it was the wrong one" is unchanged.

## 4. Medical reserve — PASS

**The exchange is on the page and is clear.** `manuscript/chapter-24.md`:309 has Anwen refuse
to seal the Pit ash, name the reason (the seventh reed), name the source ("The reserve's
quarter of our own Sag Handful is still at the Wren House; I asked"), and state the swap in
both directions "at par, on the book, where anybody can read it." Line 385 enters it in the
team book.

**It rests on facts already established.**

- Chapter 14:113–115: the Sag Handful graded "Second. W-trace" and its casualty reserve share
  was 2.6 drams, "a quarter of the rest." Two can come out of 2.6.
- Chapter 24:153–183: all four of the team are in the grading room when the seventh reed taps,
  so Anwen did hear it. That scene precedes the table scene.
- Chapter 24:185–187: Halloran explains how a return "at par, on the team's own book, over
  four names" is written, in the same chapter, so the mechanism is not new.
- Chapter 24:17 and 537: the first sealed Sag dram is still spent on Kiva's hand. Nothing
  about that beat changed.

**Totals.** Chapter 24's entry still sums to 9.6 (2.0 + 1.0 + 3.0 + 2.0 + 1.6). Later lines
stand: 2.0 "Not opened" (41:381), 2.0 opened (47:83), 0.8 (48:243).

**Month.** Chapters 44:131 and 47:55 now say "the fourth month." By the page's day chain the
Sag license day is the 28th of the month before the Pit of "the twenty-ninth of the fifth
month" (38:159, 39:301), so the fourth is right. Jude's "five months" under wax, to the 4th of
the tenth, is right with it.

**Protected elements, all unchanged by `diff`.** Halloran's card "*W, full. I, trace*";
the seventh reed's tap in chapter 24 and its stillness in chapter 47:143; Jude asking aloud
and being thanked; Anwen's "It's medical… on a night that we haven't had yet"; Aske's "It's
the first time that I've been glad you kept it."

**Joins with the rest of the book.**

- Chapter 31:119, where Kiva says a dram of the Pit's ash "went to an infirmary for
  somebody's burned hands," still holds. The returned 1.0 is Pit ash; only the sealed 2.0 was
  exchanged.
- Chapter 40:279 (Aske: "two drams of ward-trace sealed at the ash office") and chapter
  35:367 are consistent.
- Jude's "came off a husk on the Sag… before any of this got into the ash" is now literally
  true, which it was not before.

**One optional note, not owed.** `manuscript/chapter-47.md`:143 says of the reserve, "The third
reed sang, thin and clear." Chapter 24:157 draws a distinction between a trace, which "hum[s]
faintly," and the Pit's full ward, which "sang." When the reserve was Pit ash, "sang" matched.
Now that it is Sag ward-trace, the verb leans the other way. A neck of two drams against a
pinch in a pan is a fair in-world reason for a louder note, and chapter 34:173 uses "a thin
clear note" for ordinary ash, so I do not count this as a contradiction. If the owner wants it
exact, the smallest change is one word: "sang" to "hummed." The brief did not list the third
reed and I do not hold the item on it.

## 5. Hart knowledge — PASS

- `manuscript/chapter-48.md`:469 now reads "a pump-fitter on the south coast, though she did
  not yet know it, who knew a thing by his bad hand." The clause marks the sentence as the
  narrator's. It matches the sentence after it, which already marks the keeper "whom she had
  never heard of."
- Nothing gives Kiva the card. Orla's cutaway and her putting the card away are unchanged.
- The juniors' run begins at line 395 ("Miss Dane says that we're to run it"), not at line 449
  as the repair report's range implies. That does not matter to the result: `diff` shows line
  469 as the only changed line anywhere after line 51, so the whole run and the final two
  paragraphs are byte-identical to the frozen edition apart from that clause.

## 6. Records — PASS, two mechanical fixes owed

**What follows the repaired prose correctly.**

- Card wording in the Movement One to Four checkpoints (seven places). No "Corran's disk"
  remains in any record.
- The Movement Three checkpoint's quoted team-book entry, its new bullet on the sealed 2.0,
  and its word count; the matching line in the Movement Three block of `STATE_LEDGER.md`.
- The Movement Six checkpoint's new section 0 paragraph, item 19 (51,684 words) and item 20
  (the culvert, spring of 2657).
- The Movement Five checkpoint's hall panel: "the 13th of the fourth month." This is exact.
  Classification Day is Wednesday the 3rd, the panel is quenched on the 13th of that month,
  and two month-ends pass before "the first of the seventh month" (chapter 48:69).
- `AUTHORSHIP.md`: 82 lines appended, none removed or altered. Its recorded hash for the
  repair report (`fb5378aa…`) matches the file. Every chapter and record hash in the report
  matches the current files, and every "before" hash matches the frozen sums.
- Hart: every record line already said Kiva has not been told, and still does.

**No fresh contradiction was created** in the state ledger, the checkpoints, the report or the
authorship entry. The remaining "2664" and "sixteen years" in `STATE_LEDGER.md`:261 and
`provenance/MOVEMENT-004-CONTINUITY.md`:635 are Orla's Annick reading and are correct.

**The Movement Five calendar note.** The repair report is right that it is still inconsistent.
`provenance/MOVEMENT-005-CONTINUITY.md`:81–82 says "the month of Classification Day and the
Pit is the **fifth**." Those are two different months on the page: the 28th, the 6th and the
7th all fall between them. The same file now says at line 271 that Classification Day's month
is the fourth. Item 1 at lines 628–630 still asks a reviewer to check "spring as the fifth
month," a question the reconciliation has answered. This is a record error, not a manuscript
problem: no chapter numbers Classification Day's month, and the numbered months on the page
are consistent with the fourth. **It is an owed mechanical record fix, not a new prose
priority.**

**Not owed.** The Movement One checkpoint gives Rhea Sorn's age as 41. No manuscript line
states her age, and nineteen in the spring of 2657 allows 41 or 42 depending on her birthday.
Leave it.

## 7. Scope and recovery — PASS

- `editions/book-one-pre-whole-book-repair/`: all 49 files verify against `SHA256SUMS.txt`;
  the sums file hashes to `f2f0616d…`, as the report records; `git status` shows nothing
  under `editions/`.
- A comparison of all 49 manuscript files with the frozen edition shows exactly five that
  differ: chapters 8, 24, 44, 47 and 48. The differences are the nine lines in the report and
  no others.
- Word counts check: chapter 24 at 8,653, chapter 48 at 6,573, the book at 305,131.
- No optional note was acted on. The prologue, chapter headings, the anniversary, the
  lid and Mars threads, lane scoring, Mara's skirt, "restored for eleven," the quench-box tag
  and every refrain are untouched, as the `diff` proves.
- Nothing was committed. The working tree is at `0417bbb` with the changes uncommitted.

## What this recheck did not do

It edited no manuscript, record, planning, frozen or authorship file. It did not score the
novel, reopen any optional note, commit, push, publish, narrate or draft Book Two. It wrote
this file only.

OVERALL: PASS — mechanical record fixes owed

1. `provenance/MOVEMENT-005-CONTINUITY.md`, lines 81–82: change "the month of Classification
   Day and the Pit is the **fifth**" so that Classification Day's month is the fourth
   (unnumbered on the page) and the Pit's is the fifth.
2. `provenance/MOVEMENT-005-CONTINUITY.md`, lines 628–630 (section 9, item 1): mark the check
   as done. Chapters 1 to 32 number no month, and the day chain makes Classification Day's
   month the fourth and the Pit's the fifth.
