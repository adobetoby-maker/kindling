# Kindling 2680, Book Two — Movement One — consolidated repair

Date: 2026-10-14. Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0 (public byline Monroe Jackson).

## 0. Run

- **Runtime-reported model:** Claude Opus 5.5, model identifier `claude-opus-5-5`. The session
  states this; it cannot be independently verified from inside the session. No subagent,
  other model or delegated worker wrote or edited prose or records in this run.
- **Session:** Claude Code background job `7d93f063` (session
  `7d93f063-6603-4d32-a8ba-8f7d7e5a7141`); remote session `session_01DTjXDzNDrhqaQzUbAQMbjc`.
- **Brief:** delivered in-session. Its text matches `planning/OPUS-5.5-MOVEMENT-001-REPAIR.prompt.md`
  (SHA-256 `e64cce9167e44259832217a4d2d032883be83de33213dac438a84c1e6ac83489`) on inspection.
  No byte comparison of the delivered text was possible.
- **Evidence read before editing, in order:** `provenance/MOVEMENT-001-EDITORIAL-REVIEW.md`,
  `provenance/MOVEMENT-001-COLD-READ.md`, `STATE_LEDGER.md`, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`,
  then `manuscript/chapter-01.md` to `chapter-08.md` in full and in order. Before the first edit
  the working chapters were byte-identical to the frozen edition.
- **Isolation:** the project is not a git repository, so worktree isolation was not available.
  The work was done in place. Nothing was committed, pushed or published.
- **Measurement:** the editorial review's own script (§7 of that review), extracted verbatim and
  run with `python3 -I`, before and after. A second small script measured narration only (quoted
  spans removed) in the focus sections. Word counts are `wc -w`, headings included, as in
  `AUTHORSHIP.md`.

## 1. Files and sections changed

| File | Sections touched | Hunks |
|---|---|---:|
| `manuscript/chapter-01.md` | §1 (glosses), §2 (*since*; glosses), §4 (numeral), §5 (factor count; numerals), §7 (Perrin's count) | 9 |
| `manuscript/chapter-02.md` | §2 (tally), §3 (tally; entry; one join), §4 (Orla: sentence pass) | 22 |
| `manuscript/chapter-03.md` | §2–3 (sentence pass; *since*), §4 (*since*), §5 (drum twenty-nine) | 22 |
| `manuscript/chapter-04.md` | §1 (month; drum date; numeral; *since*), §2 (Mara: sentence pass), §4 (*since*; two joins) | 22 |
| `manuscript/chapter-05.md` | §1 (*since*; one join), §2 (*since* ×2), §5 (month; knock-on tally; one join) | 7 |
| `manuscript/chapter-06.md` | §1–2 (sentence pass; *since*), §3 (warrant arithmetic thinned), §6 (Kellan: articulation held back; sentence pass) | 26 |
| `manuscript/chapter-07.md` | §2 (spatial cues; numeral), §5 (*since*), §5 slate (*since*), §6 (*since*) | 6 |
| `manuscript/chapter-08.md` | §1 (night count; month; sentence pass), §2 (*since*; numeral; credit), §4 (ash-office restatement thinned) | 11 |
| `provenance/MOVEMENT-001-REPAIR.md` | this file, new | — |
| `AUTHORSHIP.md` | one entry appended | — |

No other file was written. `STATE_LEDGER.md`, `provenance/MOVEMENT-001-CONTINUITY.md`, the
bible, the map, the packets and the plans were read and not edited (see §6).

## 2. Factual corrections, with evidence

| # | Location | Before | After | Evidence |
|---|---|---|---|---|
| F1 | ch. 4 §1 | "November had gone by in small pieces." | "The eleventh month was going by in small pieces." | Numbered months everywhere else (ledger §1). The scene is the 20th of the eleventh month, so that month had not "gone by" (cold read §3 item 1). |
| F2 | ch. 5 §5 | "It's January." | "It's the first month." | Ledger §1; the night is Saturday the 9th of the first month. |
| F3 | ch. 8 §1 | "February," said Pike. | "The second month," said Pike. | Ledger §1 and M1.3 (two nights in the second month). |
| F4 | ch. 1 §5 | "seven numbers and five of them shake hands with a pump" | "six of them" | Mara's list is 5, 6, 8, 9, 10, 12, 14 and the pumps are 3, 7, 5. Only 8 shares no factor; 5, 6, 9, 10, 12 and 14 all do. |
| F5 | ch. 2 §2–3 | Pru: "three lost in five"; "On the fourth…"; entry "fifteen thrown, eleven sealed" | "four lost in six"; "On the next…"; "seventeen thrown, twelve sealed" | Recount from the page with no event changed. Bags 1–6 are sealed (54), slip, slip, slip, sealed (59), slip, so four are lost in six. Bag 7 is sealed (56). Then nine of the next ten. Thrown: 6 + 1 + 10 = 17. Sealed: 2 + 1 + 9 = 12. "On the fourth" became "On the next" so the count reads one way on a single pass. The spends (0.16 + 0.07 + 0.09 = 0.32) and the held figure (25.21) are unchanged. |
| F5a | ch. 5 §6 (knock-on) | "until I saw her lose three in the cold" | "lose four in the cold" | Follows F5. Kiva is describing the same Low Lane floor. |
| F6 | ch. 1 §7 | Perrin: "And four days." | "And three days." | The scene is Tuesday the 18th. Seventy-three days remain to Friday the 1st of the first month, which is ten weeks and three days. On Monday the 17th (ch. 1 §1) it was ten and four. |
| F7 | ch. 3 §5 | "The streets off the twenty-ninth drum had come off their boxes that morning, a month to the day" | "The streets off drum twenty-nine, which had been fouled on the night of the pump house and was never one of the seven, had come off their boxes…" | The original was correct but easy to misread: the seven drums are 19–21 and 25–28, and Mara's new prime counts included 29. Ledger §6 and §11.5 say twenty-nine is fouled, not stepped, with its streets on boxes for about a month from the 6th of the tenth month. M1.5 says they came off on the 6th of the eleventh. The date and event are unchanged. Ch. 1's spoken "Nine-and-twenty" also became "Twenty-nine" (§3 below), which removes the drum/count echo in the ear. |
| F8 | ch. 8 §1 | "on a wharf, three nights ago" | "on a wharf, the night before last" | The card came at ten on Friday night (ch. 7 §1). The call closed at twenty to two on Saturday (Rhea's slate). This scene is Sunday afternoon, so the wharf night is Friday night, the night before last. |
| F9 | ch. 8 §2 | Kiva's list: "A mark that wanted holding before it was tested." | "My own habit, that Brask was reading like a signpost." | ch. 6 §4–5: the held mark is Perrin's ("Test it under me"), and in ch. 8 §2 Kiva says "You thought of it. I didn't." What Kiva saw herself was that her own open testing was a signpost (ch. 6 §5). Jude's "four things" still counts four. |
| F10 | ch. 4 §1 (optional item) | "on the twenty-fifth of the month before" | "on the twenty-fourth" | ch. 1: "Seven drums. One a day," with nineteen on Tuesday the 18th and "Twenty tomorrow". One a day without a gap ends on Monday the 24th. Ledger M1.4 ("Seven drums out by the 25th of the tenth") stays true, so the ledger needs no change. No skipped day was invented. |

Nothing in the ash ledger moved. Re-checked after repair: 25.53 − 0.32 = 25.21 (ch. 2);
25.21 − 0.57 = 24.64 (ch. 6); − 15.0 = 9.64; − 4.0 − 1.8 = 3.84 (ch. 8). The sealed 0.8 is untouched.
The figures 0.32, 25.21, 0.57, 24.64, 15.0, 9.64, 3.84 and 0.8 all still appear where they did.
Every "That adds" remains (ch. 2, ch. 6, ch. 8).

## 3. Consolidation and clarity

**Warrant arithmetic: one full sum, where it belongs.**
- *ch. 8 §2 (the kitchen table):* unchanged in substance. It is still the one full spoken sum,
  carrying Kellan's motive ("so that he could be in the room"). One numeral was eased: "four-and-twenty
  and sixty-four hundredths" became "twenty-four and sixty-four hundredths".
- *ch. 6 §3 (the conditions):* reduced to what the scene needs: the warrant is three, not two;
  fifteen for five heads; the Marshal's floors push it further. "We hold five-and-twenty and
  twenty-one hundredths" became "Out of five-and-twenty". The "fifteen and four. That's nineteen…
  Out of five-and-twenty" line became "Nineteen at the least, before anybody's so much as bought a
  cord." No figure was changed; two restatements were removed.
- *ch. 8 §4 (the ash office):* the book entry keeps the ritual and the exact ledger figures
  (15.0, 9.64, 0.8, 3.84). The itemised spoken-for lines it repeated from the table became
  "Spoken for, as at the table: 5.8." The 5.8 equals ledger M1.2's 4.0 + 1.8.

**Kellan, ch. 6 §6.** His explicit motive was held back for ch. 8: wanting to know what he is,
the "weak corner", "I'll never learn that here". So were the duplicated rule ("Clean was under
trace on the seventh reed"), the count of nine rungs and nine red tags, and the "would matter a
great deal on a tidal flat" consequence. He still sees the red tag and puts two figures on his
cuff unspoken, so the cuff in ch. 8 is now a reveal. His decision ("You'll have my name"), the
sum weighed both ways, the jacket, "It had no shine on it whatever", "There was not one", and
Birch's "it wanted more nerve to stop where you were" / "I've looked. I haven't it" are kept. One
line duplicated word for word in ch. 8 ("He had seen Talley on a tenth knot") was removed from
the interior. In ch. 8, "I want to know what I am" and the whole table speech are unchanged and
are now the first time the reader hears the reason. Net −154 words in ch. 6.

**Ch. 7 far-edge turn: two spatial cues and no beat changed.**
- "Something moved at the bottom of the cloth" became "…at the bottom of the cloth, down the fall
  toward the river."
- Pike's knee is now "at the head of the cloth, uphill by the thing's legs". The rising line is
  "three paces below it, on the river side of the heap, under the middle of the canvas; from
  where he knelt it was the far edge of his own cloth, with the heap between".

The count, the shut teeth, "Nobody had it.", the reach, the haul by the collar, the fold opening
empty and "That's skin." are untouched, and nothing in the wharf was shortened.

**Opening glosses (ch. 1), in scene, with the mate exchange kept word for word.**
- *thimble:* "her Monday thimble, the half dram a week that was hers to work with" (ledger §3: Kiva's
  own weekly half dram).
- *doors:* "three doors, the hand and the Ember and the still, which were the three ways that
  she could take ash in and work it" (bible §1).
- *dark:* "being dark, which was the trade's word for having every door shut".
- *catcher:* "a catcher with her doors open was always a half count ahead of something, with a
  cloth to throw and a word to call before a kill's ash came down on it". This is how a catcher
  works in ch. 2 and ch. 5.

No other opening term was glossed. "Bench-passed" is explained by Mara's next clause, and
"Circuit band"/"Third Division" sit inside the protected exchange.

**Causal *since*.** Seventeen instances that could be heard as time were changed to *because*,
*as* or *now that*:

| Chapter | Location |
|---|---|
| ch. 1 | :95, :97 |
| ch. 3 | :89, :271, :275 ×2 |
| ch. 4 | :111, :383 |
| ch. 5 | :57, :131, :219 |
| ch. 6 | :133, :449 |
| ch. 7 | :501, :533, :587 |
| ch. 8 | :121 |

Unambiguous instances keep *since* as register. Measured rate: 28.4 → 24.5 per 10k.

**Archaic numerals.** Only the heaviest spoken clusters were eased. Total "-and-twenty" forms
fell from 24 to 16.
- ch. 1: "cells seventeen to four-and-twenty, at six-and-twenty minutes" → "seventeen to
  twenty-four, at six-and-twenty minutes".
- ch. 1: "Three-and-twenty. Nine-and-twenty. One-and-thirty." → "Twenty-three. Twenty-nine.
  Thirty-one."
- ch. 4: "on a count of one-and-thirty" → "thirty-one".
- ch. 6: two "five-and-twenty and twenty-one hundredths" restatements reduced to one "five-and-twenty".
- ch. 7: the narration's third "six-and-twenty years" → "twenty-six years".
- ch. 8: Kellan's table figure (above).

Single archaic forms in character voice remain, including Pike's and Rhea's "six-and-twenty".

## 4. Sentence-length range (narration only)

Joins were made only in narration, where adjacent declaratives formed one thought, using
semicolons and colons to show the structure. No dialogue was lengthened. Quoted written records
were left as written: book entries, the keeper's report, Hart's list, Yeo's letter. Short
terminal and turn beats were kept, for example:
- "There had been no roof."
- "That was his."
- "She had told nobody."
- "There was not one."
- "Nobody had it."

The wharf (ch. 7 §2–4), the kiln, the Old Yard and every fight or challenge passage got no
rhythm edits. Focus sections passed: ch. 2 §4; ch. 3 §2–3; ch. 4 §2; ch. 6 §1–2 and §6; ch. 8
§1. There were a few joins elsewhere in reflective narration (ch. 2 §3; ch. 4 §4; ch. 5 §1, §6).

| Measure (editorial script, all text) | Before | After | Formula target |
|---|---:|---:|---:|
| Sentences | 5,504 | 5,381 | — |
| Mean words | 8.76 | 8.95 | 14.6 |
| Median | 6 | 6 | 11 |
| Population SD | 7.42 | 7.85 | ~26 |
| ≤5 words | 43.4% | 43.4% | 27.7% |
| ≥40 words | 0.5% | 0.8% | 3.3% |
| Flesch Reading Ease / FK grade | 98.9 / 1.6 | 98.7 / 1.7 | 72.3 / 6.8 |

| Narration only (quoted spans removed) | Before | After |
|---|---:|---:|
| Focus sections: mean / ≤5 / ≥40 | 10.9 / 35.5% / 1.8% | **12.9 / 33.7% / 4.8%** |
| Whole movement: mean / ≤5 / ≥40 | 9.9 / 40.9% / 0.9% | 10.3 / 40.8% / 1.5% |

**Read honestly:** inside the passages it touched, the pass reached the editor's interim
direction (narration mean near 13, about a third short, and a real tail of long sentences). The
movement as a whole did **not** reach the interim direction of a mean of 11–12 and about 35%
short. The all-text short share did not move. Three things drive that:
1. Dialogue is 37% of the words at 58% short, and it was out of scope.
2. Many short narration sentences are action beats in developed scenes that were not to be
   rhythm-edited.
3. Many are quoted written records in the characters' own hands.

Getting further on narration alone would take a wholesale rewrite of scene prose, which this
brief excludes. The formula targets were not changed. Whether the sentence targets govern
dialogue is still the owner's call, as the editorial review recommended (its §4a).

## 5. Word counts (`wc -w`, headings included)

| Chapter | Before | After | Change |
|---|---:|---:|---:|
| 1 | 5,827 | 5,887 | +60 |
| 2 | 5,709 | 5,709 | 0 |
| 3 | 5,563 | 5,589 | +26 |
| 4 | 5,464 | 5,451 | −13 |
| 5 | 5,652 | 5,654 | +2 |
| 6 | 5,741 | 5,587 | −154 |
| 7 | 7,358 | 7,389 | +31 |
| 8 | 6,994 | 6,977 | −17 |
| **Movement One** | **48,308** | **48,243** | **−65** |

Viewpoint shares after repair (editorial script): Kiva 86.2%, Rhea 5.8%, Mara 3.2%, Kellan 2.5%,
Orla 2.3%. Progression vocabulary 52.7 per 10k (unchanged). Reserved terms ("Unroofed",
"Breach", "handed crossing"): 0. Real month names: 0.

## 6. Requested or optional items deliberately left unchanged

- **Off-page cuts in the ch. 2 entry** ("Renn, two cuts on the post, 0.07. Talley, three,
  0.09."). No small, evidence-backed edit exists. Showing a cut would add staged action that is
  not on the page. Relabelling or dropping the spends would change 0.32 and 25.21, which every
  later figure rests on. Left as a known off-page spend.
- **ch. 2 §1 (the Charter Board notice).** Not duplicated elsewhere in a way that needed thinning.
  The Hunt's small print already arrives at the moment Jude reacts. Moving clean yield or the
  captain rules to later chapters would be a structural move, not a repair, so it was left.
- **"Six in seven" on Kiva's card (editorial C7).** Not an error. The owner's call.
- **Scheduling tension of Rhea's "two the month after" (cold read item 5).** Not a contradiction.
  Plan territory.
- **Kiva knowing the surname Hart (cold read item 6).** Probably Book One canon. Not checkable from
  the evidence supplied for this run, so not touched.
- **Owner decisions named by both reviews:** Rhea's lens share, chapter titles over cutaway
  sections, catchphrase rationing, front-loading of progression vocabulary, and splitting ch. 8 §2.
- **Records outside this brief's write scope, now stale against the repaired prose.** These
  should be corrected from the surviving text by whoever next updates them. They were not
  edited here.
  - `provenance/MOVEMENT-001-CONTINUITY.md` line 37 ("Three bags lost to a cold cord") and line
    302 ("fifteen thrown, eleven sealed"). The prose now reads four lost in six; seventeen thrown,
    twelve sealed.
  - The same file, line 35 ("Wed 19th – Tue 25th … one a day … The last, twenty-eight, on the
    25th"), is internally short by a day: six drums one a day from Wednesday the 19th end on
    Monday the 24th, which the prose now says. `STATE_LEDGER.md` M1.4's "by the 25th" remains
    true and needs no change.
  - No `STATE_LEDGER.md` line contradicts the repaired prose.

## 7. Frozen edition

`editions/movement-001-first-draft/` was not modified. SHA-256 of all eight files was taken before
the first edit and re-verified after the last (`shasum -a 256 -c`: all eight OK):

```
fb8fa7e30a0aefd2b9d490c939c778248469723cefb51c8170f056fdc872227d  chapter-01.md
56adf40a2b28b17d327e2ae4e829acb06f33bd203ea6158e51afe3b9f5ee74ec  chapter-02.md
c40c084aae2f903a99d37feda0bee8064d15373c873d2755fbb0e3569efaedf6  chapter-03.md
b08fe5dbc93f7c3ee2d0489ce3cbd47c0d812108eb1181e03daf07013c564d60  chapter-04.md
cccb13228aee1e79f73232516602c4c01cdedf51807e3c366f15b3ea499b4db6  chapter-05.md
b6da97b3cdd32ece49ed5d57ee1a3034e82f42cc08e589b8084d7f794cb92bb5  chapter-06.md
1457575be0cc514e17cd2fa965b8ed0e4f4230cb7d619e81b7e3503b3d438490  chapter-07.md
ee7d7f93d8ecee31e78d40c3396fbb9f5a15a31ebae66d04a7b37e51845b8e56  chapter-08.md
```

## 8. Status

A same-author repair, done in place. It has not been rechecked, cold-read or accepted, and it
is not published or committed. Chapters 9–16 were not drafted.
