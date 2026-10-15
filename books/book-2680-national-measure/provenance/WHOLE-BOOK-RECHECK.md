# The National Measure — whole-book targeted recheck of the consolidated repair

> Built by TAC

## 0. Who and how

- **Verifier, as the runtime reports it:** Claude Opus 5.5, model identifier `claude-opus-5-5`. I cannot verify this from
  inside the session.
- **Session:** Claude Code background job `59421479` (job directory `~/.claude/jobs/59421479`). The harness gives the
  session link https://claude.ai/code/session_01C7FJqMd8iTZho8JsUykd6r. Worktree `/Users/drive/kindling-2680-book-02`,
  branch `codex/kindling-2680-book-02`. HEAD was `0bb786a` at the start and `5bc1748` by the end. Another session committed
  narration files only (`narration/AUDIO-LOOP-STATE.md`, two `published.json` files and a prompt); no manuscript or record
  file changed. Prompt `planning/OPUS-5.5-WHOLE-BOOK-RECHECK.prompt.md`, SHA-256
  `1174bc1cb0a7daedd6f2eaece70d068c2ae42c3b6a66d8d88aeb056beb8c849c`. Date 2026-10-15.
- **This is a same-model-family, fresh-context check, not human review.** The book, the three whole-book reviews and the
  repair were all written by the same model family. This session is separate from the drafting, review and repair
  sessions. No subagent, no other model, no Skill tool, no Codex or OpenAI call was used.
- **Files written:** this one only. No manuscript, ledger, map, canon, continuity or authorship file was edited. Nothing was
  committed, pushed or published. Scratch scripts are in the job's `tmp/` directory, outside the repository.
- **Read in full:** `provenance/WHOLE-BOOK-REPAIR.md`; `WHOLE-BOOK-CONTINUITY-REVIEW.md`; `WHOLE-BOOK-PROMISES-REVIEW.md`;
  `WHOLE-BOOK-SEAMS-REVIEW.md`. **Read as diffs against `HEAD`:** `STATE_LEDGER.md`, `CHARACTERS.md`, `BOOK_MAP.md`,
  `AUTHORSHIP.md` and the six `provenance/MOVEMENT-00N-CONTINUITY.md` files. These were then grepped whole for stale facts.
  **Book One** (`books/book-2680-opening/`) was read at located points only: ch. 23:453 and 24:29, 24:111–113 (the Pit's
  morning and the same-night page); ch. 36:13–15 and 36:131–135 (the eighth-month tape); and its ledger for the Pit's date.
- **Method.**
  1. Every chapter was compared with its frozen copy by a paragraph-aligned word diff (`difflib`, paragraphs split on blank
     lines). This found 35 changed chapters and **112 changed hunks**, and every hunk was read.
  2. Each hunk was then read in its neighbouring paragraphs wherever a join, a referent, a date or a count depended on it.
  3. Scripted whole-book checks: blank-line and spacing damage, section and chapter endings, protected phrases, digit
     multisets per chapter, month names, "Breach", quote and italic parity, and the byte-identity of ch. 48's last section.
     Every count below is from those scripts, run over all 48 chapters of the working files and of the frozen edition.

## 1. Decision

**Defects requiring a bounded second repair.** The repair is accurate and well bounded:

- Nothing unlisted changed.
- W2 holds against the board.
- The rename is complete in the prose.
- Every habit cut joins cleanly.
- Chapter 48's last section is byte-identical.

Three located prose items and one record item survive. Each is a one-sentence or one-word fix (§8). One of them, D3,
needs the owner's nod because it sits outside the P4 decision's stated scope.

| Area | Result |
|---|---|
| 1. Nothing unlisted changed | **PASS** |
| 2. Every applied fix solves its defect | **FAIL**: W12 only partly fixed (D1); WB-04 survives at 42:207 (D2); P4 leaves 39:189 at 77 against 47's 76 (D3). Every other fix PASS. |
| 3. The habit edits keep the protected strengths and join cleanly | **PASS** |
| 4. No new defect introduced | **PASS**, with one exception: the 77/76 split between ch. 39 and ch. 47 is new (D3, counted once, under Area 2) |
| 5. Records and checks | Checksum **PASS** (48 OK). Records **FAIL** on three stale lines in `MOVEMENT-006-CONTINUITY.md` (D4) |

## 2. Area 1: nothing unlisted changed (PASS)

- `cmp` against the frozen edition: chapters **01 03 08 09 13 14 15 16 17 19 20 21 22 25 26 28 29 30 31 32 33 34 35 36 37 38
  39 40 41 42 43 44 46 47 48** differ (35). The other 13 match. For all 35, the before and after SHA-256 in the repair report's
  §4.1 table match the frozen file and the working file. Whole book by `wc -w`: **326,226 → 325,945**, as reported.
- Every one of the 112 hunks traces to a disposition (line numbers are the frozen copy's):

| Ch. | Hunks → disposition |
|---|---|
| 01 | 67 WB-17; 95 WB-11 |
| 03 | 149 W1 |
| 08 | 275 P5 |
| 09 | 27 W3 |
| 13 | 507 R26 |
| 14 | 243 R25 |
| 15 | 41 R23; 487 R24 |
| 16 | 69 R27; 85 R50; 221 W17; 353 W1 |
| 17 | 139 W6/WB-08; 295 W8 |
| 19 | 15 R42; 167 W14; 391 WB-14 |
| 20 | 173 WB-16; 351 WB-01 |
| 21 | 263 W1 |
| 22 | 243 R43 (22:47 unchanged: R37 declined) |
| 25 | 393 WB-02 |
| 26 | 63 WB-09 |
| 28 | 255 R44 |
| 29 | 49 R16; 53 W18 |
| 30 | 227 R45 |
| 31 | 227 WB-18; 321 R09; 345 R10; 365 WB-01; 401 WB-01 |
| 32 | 115 R12; 179 R11; 435 W9; 443 R13; 465 R14; 483 R15; 589 R07; 597 R01 |
| 33 | 71 W12 |
| 34 | 161 WB-04 |
| 35 | 35–37 R46 + R36; 71 R38; 351 R34 |
| 36 | 29 W2; 103 R32; 115 R18; 193 W2; 209 WB-02; 229 R31; 383 WB-10 |
| 37 | 137 W7; 143 W16 |
| 38 | 297 WB-04 |
| 39 | 59 WB-15 |
| 40 | 167 W5; 229 W5; 245 R33; 299 R04 + R05; 311 R03; 327 R02; 349 R20; 375 R08; 377 R06 |
| 41 | 3 W11; 7 W11; 113 WB-05; 125 W16; 249 WB-20; 291 WB-19 (extended); 301, 307 ×2, 311 ×2 W16; 319 WB-19 |
| 42 | 147 ×2, 151 W16; 179 W15; 297 R47; 359 W11 |
| 43 | 11 W16; 101 R48; 141 W16; 157 R30; 191 WB-03; 249 R28; 281 W16 |
| 44 | 5, 13, 241 W16; 495 WB-03 |
| 46 | 9 W13; 39 R39; 79 W10; 101 WB-12; 125 P3; 129 WB-13; 175 P1/WB-06; 191 WB-07; 259 R17 |
| 47 | 49 W11; 147 R40; 183 P4; 185 R49; 187 R19; 195 R22; 223 R29; 233 P4; 253 P2; 267 R35; 341 WB-03 |
| 48 | 89 R21; 107 WB-03; 245 R41 + WB-04 |

- No whitespace damage. In every chapter the counts of triple newlines, trailing spaces, double spaces and
  space-before-punctuation are unchanged, and each file ends as before.

## 3. Area 2: every applied fix against its defect (FAIL on three items)

| ID | Now on the page | Checked against | Result |
|---|---|---|---|
| **W1** | 21:263 "telling her what she had seen that morning in the Pit"; 3:149 "…with a fever after it, and once more in the Pit, in the fifth month."; 16:353 "when she was thirteen, and on Classification Day, and in the Pit," | Book One 23:453 ("the dead grey morning"), 24:29 ("this morning"), 24:111–113 (told at ten, "the same night"); Book Two 34:107, 36:325, 39:221, 39:261 (all list the Pit); ledger: the Pit is the 29th of the fifth month | **PASS.** The page now records the Pit, in the morning, in all three places. |
| **W2** | 36:29 "4,647.2 dr. combed… Red: 4,181.2. Clean: 466.0… The Measure to date: 4,181.2."; 36:193 the same spoken | Re-derived below | **PASS** |
| **W3** | 9:27 "I'll not count a thing you told the mast didn't count." | Book One 36:13–15 ("she said so aloud, for the mast… It doesn't count toward anything") | **PASS** |
| **W4** | Unchanged: 6:457, 12:29, 12:111, 41:313, 44:285 are byte-identical; "Pettit\|Yarrow" lines 124 before and 124 after | Repair §5.1; CHARACTERS dated note; ledger M6.10 pointer | **PASS** (deferred, and recorded as an owner item) |
| **W5** | 40:167 "Kiva's doors did not stir. They had lain down as the Master passed the bench, and had got up again, one at a time, as she walked on to the gate…"; 40:229 "the heat… which she had held off for an hour as she held her face, came up all at once, now that there was nothing left to hold it for" | 40:89 (Thrale at the gate, "three hundred paces off"); 41:227–231 (the forty-pace rule); 42:321; 44:421 | **PASS.** Doors are up at 300 paces, and the fever's hold now has its own cause. See O1 for a timing nuance. |
| **W6** | 17:139 "the night before" | 6:461 (the 28th, a day and a half); ch. 17 is Mon 30th | **PASS** |
| **W7** | 37:137 "on one stick at the gate, and that she was walking now on none" | 17:185 (the gate is in the timber pond); 17:143, 441, 467 (one stick) | **PASS** |
| **W8** | 17:295 "That's the third I've heard of since the new year." | 17:261 ("the first that's been silent on the seventh"); 36:189 (four silent) | **PASS** |
| **W9** | 32:435 "I held a card ten days" | 2:353 "sat on it for nine days while she decided"; Book One ch. 48 | **PASS** (speech rounding over a hand-over day; see O5) |
| **W10** | 46:79 "Pryce said it'd stay eight-tenths" | Book One 48:245 (Anwen); Perrin's "Pryce" at 12:199, 35:69 and elsewhere | **PASS** |
| **W11** | 41:3 adds "She meant to keep the morning's quarter to seven from now on; Sunday evening's had been Pru's, written for her."; 41:7, 42:359, 47:49 "every day" | Every quarter-to-seven line in ch. 24–48: evening 24:319 → 40:319 ("Written by Finch"); morning 41:9, 46:3–9; 48:273 "She had let the morning's go by"; ledger M3.1 records the hour once | **PASS** in all four places and the ledger |
| **W12** | 33:71 "Thirty-six hands would be on thirty-six glass cases." | 32:469–473 (Mara's Wednesday-night decision: "Thirty-six hands," said Mara. "Not mine."); ledger M4.5 knowledge boundary ("Mara's thirty-six: Peverell, Hart") | **FAIL, partly fixed (D1).** The cut removed "that were not her aunt's", but the number of hands is itself Mara's decision. Before it, the alternative on the page is Mara's one hand (32:469), which is what Kiva would expect. |
| **W13** | 46:9 "for the first time since the Hunt" | 33:469, 40:319, 41:9 | **PASS** |
| **W14** | 19:167 "spent a winter" | Fingers lost in the ninth month | **PASS** |
| **W15** | 42:179 "a square pale face" | 17:341, 33:177 | **PASS** |
| **W16** | "Shapter" ×16, at exactly the places listed (37:143; 41:125, 301, 307 ×2, 311 ×2; 42:147 ×2, 151; 43:11, 141, 281; 44:5, 13, 241). "Sedge" (any case) in Book Two's manuscript: 16 → **0**. | Both manuscripts: the only capitalised *Sh-* words are "Shapter" (16) and "Shutdown" (1). There is no "Shapter" in Book One, in `universe/` (including `NAME_REGISTRY.md`), or anywhere outside Book Two's prose and records. Pronoun "she", and "a tall fair girl", hold (42:151; 43:11). | **PASS** in the prose. Records: see D4. |
| **W17** | 16:221 "a fortnight" | Twelve days in Meridian | **PASS** |
| **W18** | 29:53 "with a new rope, half knotted already" | 21:57, 23:135, 24:363 (Perrin keeps Coombe's old rope); 32:443 "picked up her rope" | **PASS** |
| **P1** | 46:175 "on Wednesday night" | 35:50 (Yeo at the board on Wednesday night); 33:249–253; 48:57 (Carrow's "On Saturday" is a different card) | **PASS** |
| **P2** | 47:253 "I said no at his table, and I said no to counsel, on a card…" | 47:247 "You've said it to this house twice"; 22:267; 36:65–69 | **PASS** |
| **P3** | 46:125 "Six hundred and eighty-six drams… and four-tenths" | 2:71 (a Flask "the best part of five hundred"); 2:47 ("between a Flask and a Well"; no Well figure anywhere); ledger M6.3 and M6 continuity §8 now read 686.4 | **PASS** |
| **P4** | 47:183 and 47:233 "seventy-six years"; 47:225 left at seventy-seven (counted from the window) | 39:185 ("a year after the window… since I was twenty-seven"); **39:189 "I've been sure of it for seventy-seven years."** | **FAIL as a whole (D3).** Applied as decided, but the same arithmetic slip survives at 39:189. It sits four lines from its own premise, and now disagrees with 47's 76 for the same belief. Before the repair, ch. 39 and ch. 47 at least agreed. The repair recorded this as owner item §5.3.1. |
| **P5** | 8:275 "I've not said it to Birch. I thought that you might as well hear…" | — | **PASS** |
| **WB-01** | 20:351, 31:365, 31:401 "eleven years" | 3:217, 6:57, 7:311, 7:385, 11:133, 14:389. The remaining "six years" hits are all Pike's "twenty-six years" (5:523, 7:151, 12:339, 47:319). | **PASS** |
| **WB-02** | 25:393 "a pleasant man of forty or so with a narrow gold cord at his cuff"; 36:209 "Adlam's hand" | 21:403; Book One ch. 26 | **PASS** |
| **WB-03** | 43:191, 44:495, 47:341, 48:107 "square grey" | 3:265, 8:487, 8:557; "long brown" now occurs once, at 44:161 (water: "a long brown lip of it") | **PASS.** The payoff at 47:341 ("It went the whole way, this time") is intact. |
| **WB-04** | 34:161 keeps "She did not go red."; 38:297 and 48:245 cut | 10:451 "Kiva watched her go red, slowly, from the collar" | **FAIL, a surviving instance (D2).** 42:207 "Anwen read it. She did not go red, because she never did." makes the same claim in other words. The seams review searched for the exact sentence and listed only three places. |
| **WB-05** | 41:113 "who steadied the sheet with his left hand while he wrote *Talley,*" | 15:517, 33:139–141 | **PASS** |
| **WB-07** | 46:191 "I asked you what ash was for" | 19:253, 19:291 | **PASS** |
| **WB-09** | 26:63 "And Wednesday's the Longshore. If they go on Tuesday, you don't plant on Wednesday." | Mon 14th (26:75); the Carry Tue 15th; the Hunt "Wednesday the 16th" (32:109) | **PASS** |
| **WB-10** | 36:383 "on Wednesday night" | 32:449–471 (the gallery, Wed 16th) | **PASS** on the interval. See O2 on viewpoint. |
| **WB-11** | 1:95 "three of them besides" | The warden, the fitter, and Ned | **PASS** |
| **WB-12, 13** | 46:101 "had gone over"; 46:129 reordered | — | **PASS** |
| **WB-14, 15, 16, 18** | 19:391 "Orla"; 39:59 "Hart"; 20:173 "on the third line… let go of it"; 31:227 "a corner" | — | **PASS** |
| **WB-17** | 1:67 "eleven weeks and four days… ten weeks and four days" | — | **PASS** |
| **WB-19, WB-20** | 41:249 "three planks: like doors on one load, not two still doors on a patch of ground" (the first *plank* in Movement Six); 41:291 and 41:319 "board" | Every *plank* in ch. 41 is after 41:249 | **PASS** |

### W2 re-derived from the board

- **The rule** (29:49; 32:289): a four is marked on its quarter of its clean yield, less a dram for every remark. So a four's
  clean yield is 4 × (mark + remarks).
- **The places printed on the page** (32:291–297):

  | Place | Four | Mark | Remarks | Clean |
  |---:|---|---:|---:|---:|
  | 1 | Twenty-Eight | 11.80 | 0 | 47.2 |
  | 2 | Old Four | 10.40 | 0 | 41.6 |
  | 3 | Westerley second | 9.95 | 0 | 39.8 |
  | 6 | Halden | 8.20 | 1 | 36.8 |
  | 12 | Ropewalk first | 4.10 | 2 | 24.4 |
  | 15 | Seven | 3.15 | 0 | 12.6 |
  | 24 | Tarn first | 0 | — | 0 |
  | | **On-page sum** | | | **202.4** |

- **Floor from the printed board alone.** Each unprinted place's mark is at least the next printed mark below it, so its clean
  yield is at least 4 × that mark:
  - places 4–5: 2 × 32.8 = 65.6;
  - places 7–11: 5 × 16.4 = 82.0;
  - places 13–14: 2 × 12.6 = 25.2;
  - places 16–23: at least 0.

  Floor: 202.4 + 65.6 + 82.0 + 25.2 = **375.2**, the continuity review's "about 375".
- **Floor and ceiling with the Movement Four reconciliation** (places 4, 5, 7 and 8; records only, not on the page): floor
  **402.8**. The ceiling, assuming no remarks among the unprinted places, is **534.6**. Both match the repair's "about 403"
  and "about 534".
- **466.0 clean** lies inside both ranges. The repair's 24-place table sums to 466.0 (rows checked one by one; places 16–23
  are marks 11.85 in all, × 4 = 47.4), and its marks fall monotonically.
- **The other figures:**
  - 4,181.2 + 466.0 = 4,647.2.
  - Red is 89.97%, so "Nine-tenths" (36:29, 36:193) and the *Mercury*'s "Nine Bags in Ten" stand.
  - Seven's 3.15 = 12.6 ÷ 4, and 59.7 combed − 47.1 red = 12.6 (32:109): unchanged and consistent.
- **Nothing else quotes the old figures.** Searches for 412.4, 371.3, 41.1, "seventy-one and" and "forty-one and a tenth" find
  no prose hit in either book. The only changed digits anywhere in the 48 chapters are ch. 36's (412.4, 371.3 ×2 and 41.1 →
  4,647.2, 4,181.2 ×2 and 466.0). The live records (ledger M5.7, `MOVEMENT-005-CONTINUITY.md` §3) carry the new figures.
  The old ones survive only as dated history: `MOVEMENT-005-CHECKPOINT.md:18`, `MOVEMENT-005-EDITORIAL-REVIEW.md:265`, and
  the planning prompts.

## 4. Area 3: the habit edits (PASS)

- **Applied as listed.** R01–R50 are applied as the repair says, R37 is declined (22:47 is byte-identical), and the three
  modified edits are sound:
  - R02: "Nothing came," said Aske. (40:325) carries the speaker's name.
  - R13: "There was no answer to that. Orla sat…" (32:441) keeps the knee hers.
  - R20: "She read the top line again." (40:347) keeps "It was a name." on *THE UNROOFED SKY.*
- **Every join was read in context.** The whole-paragraph cuts are R12 (32:115), R23 (15:41), R24 (15:487) and R25
  (14:243); the next paragraph in each case carries its own tag ("said Pike", "said Jude", Vane's "Clean," he said) or is
  narration. The merged quotations are R04, R05, R16–R19, R31–R36 and R04/WB-04 at 38:297; each joins one speaker's speech
  with no orphaned tag. R21 ("She stopped." / "Then she wrote the last line…") and R29 ("Kiva waited." before the
  Proprietor's speech) read cleanly.
- **Protected strengths** (counts over all 48 chapters, frozen → working):
  - Call words: *Set.* 14 → 14; *Nobody.* 7 → 7; *Far edge.* 3 → 3 (my pattern includes the italic markers, so my absolute
    counts differ from the repair's 17/14/6; both scans show no change).
  - Card wording: "Then we look again, and either of us may say no." 4 → 4; "Not for a bank, a floor, a crossing or a sale."
    4 → 4.
  - *The disk is cold.* 1 → 1. "Breach" 0 → 0.
  - Ledger figures: the per-chapter multiset of digit strings is unchanged in every chapter except ch. 36 (W2).
  - **"nearly smiled": 10, all Pike's** (3:271, 5:511, 6:143, 7:579, 8:77, 19:35, 20:225, 24:265, 37:365; and 31:339, Yeo
    reporting "your old man").
  - **The town-count refrain** "Four and four. Fifty-seven to the minute, or faster." survives whole at **24:383**, the end
    of Movement Three, and at 41:7, which opens a chapter and closes nothing.
  - Ch. 32 still ends "*It keeps time.*" / "She did not write it down." Ch. 40 keeps its survey, "There were three days.",
    Rhea's card and "The unroofed sky had a name and no meaning."
- **Scene-ending beats.** The section and chapter endings touched are only:
  - 28:255 (R44); 31:321 (R09);
  - the end of ch. 32 (R01, the OD-1 decision);
  - 47:195 (R22); 47:267 (R35).

  Each keeps its final beat ("I'll not wait to see her land."; "She looked at the back of his head."; "She did not write it
  down."; "He had only wanted to hold something."; "Every time."). The one-line hook endings of ch. 8, 26, 29 and 43 are
  untouched. Ch. 32 is the only chapter whose last paragraph changed.
- **Ch. 48's last section is byte-identical.** Lines 246–341 of `chapter-48.md` match the frozen copy line for line. From the
  ninth *no answer* (48:277) to the end, SHA-256 is `221198fc5d9066bdb4050cb2bba742b9f477ad1e7eb6db5b5d274cf390653a34` in
  both copies, as the repair reported. From 48:275 ("No answer.") to *The disk is cold.* (48:339): `73cf755e…` in both.

## 5. Area 4: no new defect (PASS, with one exception: D3)

- **Quote parity.** I counted paragraphs with an odd number of `"` that do not open a multi-paragraph quotation: **3 before,
  3 after, 0 new.** These are the inch marks in Hart's slack log, ch. 26. The repair's "6" includes the three openers of
  multi-paragraph quotations. Italic-marker parity is unchanged in every chapter and in every edited paragraph. No curly
  quotes or tabs were introduced.
- **Month names.** None. The only hits are "May" as a verb (16:57, 22:121, 23:295), all unchanged.
- **"Breach":** 0.
- **Dates and weekdays touched by the edits** all check against the calendar: 17:139 (Sun 29th); 26:63 (Tue 15th / Wed 16th);
  36:383 and 46:175 (Wed 16th); 41:3 (Sun 20th / Mon 21st); 46:9 (the Hunt, Wed 16th); 37:137 (Tue 1st, the gate); 32:435
  (ten days).
- **Counts and sums touched by the edits:**
  - W2 and P3 hold (§3).
  - WB-11's three are the warden, the fitter and Ned.
  - WB-01's eleven agrees with six earlier passages.
  - W16's sixteen places are exactly sixteen.
  - **The exception is P4.** The split between 39:189 (seventy-seven) and 47:183 and 47:233 (seventy-six) is new to this
    repair. It is listed once, as D3.

## 6. Area 5: records and checks

```
$ cd books/book-2680-national-measure/editions/whole-book-pre-repair && shasum -a 256 -c SHA256SUMS.txt
chapter-01.md: OK
… (every line OK)
chapter-48.md: OK
exit 0
```

**48 OK, 0 failed.** `git status` shows nothing modified under `editions/`.

**Reconciliations that match the surviving prose:**

- `STATE_LEDGER.md`:
  - M3.1 records the hour once: evening from Sun 13th to Sun 20th, Sunday's written by Pru; morning from Mon 21st.
  - M4.4: Coombe's new rope.
  - M5.7: Thrale's reach in the Graving, and Kellan's 4,647.2 / 4,181.2 / 466.0.
  - M5.9: Shapter, with the reason.
  - M6.1: the crossings' numbering, and the morning hour.
  - M6.3: 686.4.
  - M6.10: a pointer to the repair.
- **Continuity files:**
  - `MOVEMENT-002` §8: Thrale's jars ("forty-one since… forty-four before").
  - `MOVEMENT-003`: the hour.
  - `MOVEMENT-004` §0 and §10: "ten days", the new rope.
  - `MOVEMENT-005` §3, §5, §12.
  - `MOVEMENT-006` §8: numbering, 686.4.
  - Each of the six has a closing reconciliation section, and its chapter-by-chapter notes match the diff.
- `CHARACTERS.md`: a dated note giving Pike, Adlam, Lyle and Shapter, with the W4 owner item.
- `BOOK_MAP.md`: a dated P4 note. It is accurate about ch. 47 and silent on 39:189 (see D3).
- `AUTHORSHIP.md`: the repair entry.
- **No record claims a recheck, an acceptance or a publication.** The only status lines added say "Not rechecked, not
  accepted, not committed, not published" (`AUTHORSHIP.md`) and "Repaired, not rechecked and not accepted"
  (`WHOLE-BOOK-REPAIR.md` §7).

**Stale lines:**

1. `provenance/MOVEMENT-006-CONTINUITY.md:121`: "Ward line A (Anwen, Edda, Hesketh, Sedge)". Should read Shapter.
2. `provenance/MOVEMENT-006-CONTINUITY.md:143`: "**Twenty-Eight** (Marten, Sedge, Bannock,". Should read Shapter.
3. `provenance/MOVEMENT-006-CONTINUITY.md:147`: "Planks: ward line A (Anwen, Edda, Hesketh, Sedge)". Should read Shapter.
   The file's own closing note (line 367) records the rename, but its rosters were not updated.
4. *(Minor, the repair's own record)* `provenance/WHOLE-BOOK-REPAIR.md` §4.2, the refrain row: "Four and four. Fifty-seven
   to the minute" "6 → 4". Scanned whole, that sentence occurs **4 → 2** (24:383, 41:7). Case-insensitive "fifty-seven to the
   minute" occurs 9 → 7. The claim it supports ("once at a movement end, 24:383") is true. Only the figures are off.
5. *(Historical, no action proposed)* `provenance/MOVEMENT-005-CHECKPOINT.md:18` keeps 412.4/371.3/41.1 as a dated snapshot.
6. *(Follows D1, if applied)* `provenance/MOVEMENT-005-CONTINUITY.md`, closing section: "ch. 33: 'Thirty-six hands would be
   on thirty-six glass cases' (W12…)". It would need to say what replaced the sentence.

## 7. Surviving or newly introduced defects, located

| # | Severity | Location | Quoted text | Problem |
|---|---|---|---|---|
| D1 | CONTRADICTION (knowledge; W12 not fully solved) | `manuscript/chapter-33.md:71` | "Thirty-six hands would be on thirty-six glass cases." | At 7 a.m. Thursday Kiva still knows the content of Mara's Wednesday-night decision ("Thirty-six hands," said Mara. "Not mine.", 32:473). Ledger M4.5 limits that knowledge to Peverell and Hart. Before the decision, the alternative on the page was Mara's own hand (32:469), which is what Kiva would expect. |
| D2 | CONTRADICTION (WB-04 survives) | `manuscript/chapter-42.md:207` | "Anwen read it. She did not go red, because she never did." | 10:451: "Kiva watched her go red, slowly, from the collar". This is the claim WB-04 removed from 34:161, 38:297 and 48:245, here in other words. |
| D3 | CONTRADICTION (P4 residue; new disagreement) | `manuscript/chapter-39.md:189` | "I'm sure of my reading," said the Proprietor. "I've been sure of it for seventy-seven years." | Four lines after "It came to me a year after the window, and I've had it since I was twenty-seven" (39:185). He is 103, so the reading is 76 years old, and 47:183 and 47:233 now say seventy-six for the same belief. 39:251 ("seventy-seven years not learning the difference") and 39:145 count from the window and can stay. |
| D4 | Record | `provenance/MOVEMENT-006-CONTINUITY.md:121, 143, 147` | "Sedge" ×3 | Stale after W16 (§6, items 1–3). |

## 8. Bounded second repair (located, minimal)

1. **D1**, `chapter-33.md:71`. Cut the sentence `Thirty-six hands would be on thirty-six glass cases. ` so that the paragraph
   reads "…the basin would go still for twenty minutes. Somewhere in it, if anybody asked her, she would be calling…". "it"
   still refers to the still basin. Then update the ch. 33 line in `MOVEMENT-005-CONTINUITY.md`'s closing section to match.
   If the owner prefers to keep a sentence, keep one that does not count the hands; "Somebody's hands" was the reviewer's
   version, and the repair rejected it because it reads as one person's.
2. **D2**, `chapter-42.md:207`. `She did not go red, because she never did.` → `She did not go red.`
3. **D3**, `chapter-39.md:189`. `I've been sure of it for seventy-seven years.` → `I've been sure of it for seventy-six years.`
   (one word). This is outside P4's stated scope, so it needs the owner's nod; the repair already raised it as §5.3.1. If
   the owner declines, the alternative is to accept 77 everywhere and revert 47:183 and 47:233. Either way, the book should
   give one figure for the age of the reading. Extend the `BOOK_MAP.md` P4 note to name the line chosen.
4. **D4**, `MOVEMENT-006-CONTINUITY.md:121, 143, 147`. "Sedge" → "Shapter". Optionally add one dated line to
   `WHOLE-BOOK-REPAIR.md` correcting the §4.2 refrain figures to 4 → 2.

None of these touches a ledger figure, a call word, card wording, a scene-ending beat, or ch. 48's last section. After they
are applied, a targeted recheck of these four items alone is enough.

## 9. Observations (not defects; no fix proposed)

- **O1. Thrale's entrance.** 40:19 has Kiva's doors lie down "at two", when the hush begins at the lip as Thrale appears. The
  new 40:167 says they "had lain down as the Master passed the bench". Read as a recap of the state while she passed, it holds,
  and W5's defect (doors down at 300 paces) is solved.
- **O2. Viewpoint at 36:383.** This section is in Kiva's viewpoint, and the simile now points to the Wednesday-night gallery
  (32:449ff., Mara's lens, with Kiva at Quiller's). The pre-repair "a fortnight ago" reached outside Kiva's sight in the same
  way, and the book's narrator already does so (32:587). Not a new kind of slip.
- **O3. Read-aloud.** "Shapter" collides with no name in either book. It sounds like "Chapter", which occurs only in headings.
  It is noted for the narrator only.
- **O4. The audio pipeline is outside this recheck, but it bears on publication.**
  - `narration/breeze/chapter-01/direction.json` still contains pre-repair text ("four of them besides", "eleven and four
    days"), and so does `chapter-03/direction.json` (the dream without the Pit).
  - `narration/breeze/pipeline.log` shows chapters being "published to PWA deployment queue" today.
  - Any audio for the 35 changed chapters needs to be rendered from the repaired text before final publication. Chapters
    2, 4, 5, 6 and 7 are unchanged by the repair.
- **O5. W9.** "ten days" (32:435) against "nine days while she decided" (2:353) is a speaker rounding across the hand-over
  day. Left.
- The repair's own owner items (§5) are carried unchanged, and this recheck makes no decision on them: W4; the colour; Vane;
  47:29 "the Regiment"; the Hunt's reconciled rows; the Well.

## 10. Limits

- Same model family as the author, the reviewers and the repairer. Fresh context, not independent testing, and not human
  reader evidence.
- I read every changed passage and its neighbourhood. I did not reread the book end to end. Unchanged passages were checked
  only by the searches named above (residues of each fixed fact, protected phrases, counts, parity). A contradiction worded in
  a way none of those searches anticipates could survive; D2 is an example of exactly that kind, found by widening one search.
- Book One was consulted at the located points in §0 only.
- Read-aloud effects are judged from the text. No audio was rendered or heard.
