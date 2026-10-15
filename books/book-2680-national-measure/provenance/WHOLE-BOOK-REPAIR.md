# The National Measure — whole-book consolidated repair (located defects only)

> Built by TAC

## 0. Who and how

- **Author seat:** Claude Opus 5.5, model identifier `claude-opus-5-5`, as the runtime reports it. This cannot be verified from
  inside the session. Byline Monroe Jackson; seat Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- **Session:** Claude Code background job `32af798e` (job directory `~/.claude/jobs/32af798e`); the harness gives the session link
  https://claude.ai/code/session_01CPCUZ8t9DmXXrrenjxY1p2. Worktree `/Users/drive/kindling-2680-book-02`, branch
  `codex/kindling-2680-book-02`, starting from commit `c2b2fc1`.
- **Brief:** `planning/OPUS-5.5-WHOLE-BOOK-REPAIR.prompt.md`, SHA-256
  `3bfd58b11cebcb2ebab2b865ab6928952697f2c393ac6c0e76ebdccdda202283`.
- **No subagent, no other model, no Skill tool, no Codex or OpenAI call.** Nothing was committed, pushed or published. Nothing
  was rechecked or accepted; this record claims neither.
- **Inputs read, in the brief's order:** the three whole-book reviews in full (`WHOLE-BOOK-CONTINUITY-REVIEW.md`,
  `WHOLE-BOOK-PROMISES-REVIEW.md`, `WHOLE-BOOK-SEAMS-REVIEW.md`); `WHOLE-BOOK-REPETITION-DATA.md` in full; the affected
  blocks of `STATE_LEDGER.md` (M3.1, M4.1, M4.4, M5.1, M5.7, M5.9, M6.1, M6.3, M6.5, M6.9, M6.10), `CHARACTERS.md` in full,
  the touched lines of `BOOK_MAP.md` and of the six movement continuity files; and every chapter passage edited, each with its
  neighbouring paragraphs (several scenes more widely: the Graving hearing in ch. 40, the plan in ch. 41, the Hunt board in
  ch. 32, Kellan's figures in ch. 36, the yield scale in ch. 2). Book One (`books/book-2680-opening/`) was read at located
  points for the locks at issue: Pettit and Yarrow (ch. 32, 34, 37, 39, 42, 43, 45, 46 and its ledger), Pike's face (ch. 29,
  31, 34, 42, 43), Rhea's years (ch. 1, 8, 16, 23, 29), and the time of day of the Pit (ch. 22–24).
- **Method.** Every edit was an exact string replacement, applied by a script that refused to write anything unless each
  "before" string occurred exactly once in its chapter (`~/.claude/jobs/32af798e/tmp/edits.py`, with a JSON log of every
  before and after). Before editing I re-checked every review string against the working text: all 27 F-strings and all 50
  R-strings occurred on the cited line. Three needed care: **P4a** (the promises review quotes "*I believed…"; the italic
  opens earlier in the sentence, so I anchored on "I am not certain I was wrong. I believed for seventy-seven years");
  **R24** and **R29** (the sentence occurs twice in the chapter; I anchored on the cited line's neighbours, 15:487 and
  47:223). Record edits used the same exact-once check (`records.py`).
- **Frozen edition:** `editions/whole-book-pre-repair/` was never written. `cd editions/whole-book-pre-repair && shasum -a 256 -c
  SHA256SUMS.txt` → **48 OK, 0 failed** (run after all edits); `git status` shows no change under `editions/`.

## 1. The showrunner's decisions (§B), as applied

| Item | Decision | As applied |
|---|---|---|
| **W2** | Fix the figures, not the board | Kellan's Hunt: **4,647.2 combed; 4,181.2 red; 466.0 clean** (red 89.97%, "Nine-tenths" stays true). Claims line and "The Measure to date": **4,181.2**. Reconciled against the board in §3. The board, Seven's 3.15 and "Nine Bags in Ten" unchanged. No repetition in ch. 38 or 40 (grep for `371`, `412.4`, `41.1` and the spoken forms found only 36:29 and 36:193). Ledger M5.7 and `MOVEMENT-005-CONTINUITY` §3 corrected. |
| **W4** | Book One governs; smallest edit, or record if over about eight lines | **Not changed; recorded as an owner item** (§5.1). Every honest route exceeds the limit or adds an on-page event. |
| **W5** | Option (b) | 40:167: the doors "had lain down as the Master passed the bench, and had got up again, one at a time, as she walked on to the gate". 40:229: the heat is one "she had held off for an hour as she held her face", coming up "now that there was nothing left to hold it for". No rule added at ch. 41. |
| **W11** | 42:359 "every day"; one clause at 41:3; the hour recorded once in the ledger | Applied, plus the same slip at **41:7** and **47:49** (Hart: "You wrote *yes* every morning"), found by sense; both now "every day". 41:3 adds: "She meant to keep the morning's quarter to seven from now on; Sunday evening's had been Pru's, written for her." The hour is recorded once, in ledger M3.1, with a pointer in M6.1. |
| **W16** | Rename Twenty-Eight's Hold | **Shapter** (she), at all **sixteen** places (the review counted thirteen; the possessives and ch. 42–44 add three): 37:143; 41:125, 301, 307 ×2, 311 ×2; 42:147 ×2, 151; 43:11, 141, 281; 44:5, 13, 241. Search of every `.md`, `.json`, `.txt`, `.yaml`, `.csv` and `.py` file in both books (manuscripts, planning, provenance, packets, narration records; editions excluded) and in `universe/`: 0 hits for *Shapter*. No other name in either book begins *Sh-*; its consonants are unvoiced (sh, p, t), and it shares no first syllable with Book Two's cast in her scenes (Hesketh, Edda, Anwen, Marten, Bannock, Dray, Finch). |
| **P1 / WB-06** | "on Wednesday night" | Applied (46:175). |
| **P3** | Option (a) | 46:125 **"Six hundred and eighty-six drams… and four-tenths"** (686.4): above the Flask, "the best part of five hundred" (2:71), and, since the book gives no figure for a Well, below it by the column order of 2:47. Ch. 2 unchanged. Ledger M6.3 and `MOVEMENT-006-CONTINUITY` §8 corrected. No share depends on it. |
| **P4** | 47:183 and 47:233 → seventy-six; leave 47:225 | Applied. |
| **WB-20 / OD-5** | Option (a), and F19 | 41:249: "It's three planks: like doors on one load, not two still doors on a patch of ground." F19 at 41:319 ("a board"), and the same literal plank four paragraphs earlier at **41:291** ("they nailed a board across its bottom"), so the tun's board is never a *plank* in the scene that teaches the word. |
| **OD-1** | Yes, vary | R01, R06, R07, R08 applied. The full refrain ("Four and four. Fifty-seven to the minute, or faster.") closes Movement Three once (24:383). Ch. 32 still ends on *It keeps time.* and "She did not write it down."; ch. 40 keeps its survey of the town, the three days, Rhea's card and the name. |
| **OD-2, OD-3, OD-6–OD-9** | No action | None taken. OD-4: R02–R05 applied. |

## 2. Dispositions

Line numbers are the working files' before this repair. "Applied" means the reviewer's fix verbatim.

### 2.1 Continuity review (W1–W18)

| ID | Disposition | Chapter: before → after |
|---|---|---|
| W1 | **Modified** (one word of the reviewer's fix) | 21:263 "telling her what she had seen when she was thirteen and again on Classification Day." → "…telling her what she had seen that morning in the Pit." The reviewer wrote "that afternoon"; Book One sets the Pit in the morning ("the dead grey morning", ch. 23:453; "this morning", ch. 24:29). 3:149 "…on Classification Day, with a fever after it." → "…with a fever after it, and once more in the Pit, in the fifth month." (keeps the fever clause the reviewer's version dropped). 16:353 "when she was thirteen and on Classification Day," → "when she was thirteen, and on Classification Day, and in the Pit," |
| W2 | **Applied as decided** | 36:29 and 36:193 (three figures; claims line twice). See §1 and §3. |
| W3 | Applied | 9:27 "I'll not count a thing that I didn't see on a tape." → "I'll not count a thing you told the mast didn't count." |
| W4 | **Deferred: owner item** | No chapter changed (§5.1). |
| W5 | **Applied as decided (b)** | 40:167 and 40:229 (§1). |
| W6 = WB-08 | Applied once | 17:139 "three days before" → "the night before". |
| W7 | Applied | 37:137 "on two sticks a fortnight ago and onto the Long Quay on one, and that she was walking now on none." → "on one stick at the gate, and that she was walking now on none." |
| W8 | **Modified** | 17:295 "That's the third I've combed this morning." → "That's the third I've heard of since the new year." The reviewer's "seen this winter" would echo the next sentence ("It's everywhere, this winter") and "seen" still implies he combed them; "heard of" keeps him clear of the four silent tins (36:189). |
| W9 | Applied | 32:435 "I held a card a season," → "I held a card ten days," |
| W10 | Applied | 46:79 "and Rowan said it'd stay eight-tenths" → "and Pryce said it'd stay eight-tenths" (Perrin calls Anwen "Pryce" at 12:199, 12:291, 14:117, 18:297, 35:111). |
| W11 | **Applied as decided, extended** | 42:359, 41:7, 47:49 "every morning" → "every day"; 41:3 one sentence added (§1). |
| W12 | **Modified** | 33:71 "Thirty-six hands that were not her aunt's would be on thirty-six glass cases." → "Thirty-six hands would be on thirty-six glass cases." The reviewer's "Somebody's hands" reads as one person's; the cut removes only the knowledge she did not have. |
| W13 | Applied | 46:9 "for the first time since Sunday," → "for the first time since the Hunt," |
| W14 | Applied | 19:167 "spent a year" → "spent a winter". |
| W15 | Applied | 42:179 "a long pale face" → "a square pale face". |
| W16 | **Applied as decided** | Sedge → Shapter ×16 (§1). |
| W17 | Applied | 16:221 "near a Blaze for a month." → "…for a fortnight." |
| W18 | Applied | 29:53 "with her rope, and she began to tie a knot in it," → "with a new rope, half knotted already, and she began to tie a knot in it," (32:445 "picked up her rope" now reads as the new one). |

### 2.2 Promises review (P1–P6)

| ID | Disposition | Chapter: before → after |
|---|---|---|
| P1 | Applied as decided | 46:175 "Mrs. Yeo told me on Saturday." → "…on Wednesday night." |
| P2 | Applied | 47:253 "I said no to counsel twice. Twice to a card with a line on the back that said" → "I said no at his table, and I said no to counsel, on a card with a line on the back that said" |
| P3 | Applied as decided (a) | 46:125 "Two hundred and eighty-six drams" → "Six hundred and eighty-six drams" (686.4). |
| P4 | Applied as decided | 47:183 and 47:233 "seventy-seven years" → "seventy-six years". 47:225 left. |
| P5 | Applied (the cut) | 8:275 "I've not said it to Birch. I shall have to. I thought" → "I've not said it to Birch. I thought" |
| P6 | Left, as instructed | — |

### 2.3 Seams review (WB-01–WB-22; F01–F19)

| ID | Disposition | Chapter: before → after |
|---|---|---|
| WB-01 (F01a–c) | Applied | 20:351, 31:365, 31:401 "six years" → "eleven years". Book One does not state Rhea's officer years; Book Two's six earlier passages say eleven. |
| WB-02 (F02a–b) | Applied | 25:393 "a thin grey man with a stoop" → "a pleasant man of forty or so with a narrow gold cord at his cuff"; 36:209 "the old man's hand" → "Adlam's hand". |
| WB-03 (F03a–d) | Applied; direction checked | 43:191, 44:495, 47:341, 48:107 "long brown" → "square grey". Book One agrees ("Pike turned his square head", ch. 31:49; also ch. 29:245, 34:119, 42:185, 43:217). The payoff at 47:341 ("It went the whole way, this time") is untouched. |
| WB-04 (F04a–c) | Applied | 34:161 "She did not go red. Anwen never went red." → "She did not go red."; 38:297 `At home." She did not go red. Anwen never went red. "I'll be on` → `At home. I'll be on`; 48:245 the two sentences cut (with R41 in the same paragraph). |
| WB-05 (F05) | Applied | 41:113 "who wrote *Talley* with his left hand for the first time in a week," → "who steadied the sheet with his left hand while he wrote *Talley,*" |
| WB-06 | = P1; applied once with P1's wording | F06 ("on Thursday, first thing") **not used**: the decision follows P1, which agrees with 35:50 (Yeo at the board on Wednesday night) and lets her tell the mother before the card goes up. |
| WB-07 (F07) | Applied | 46:191 "I asked you in the second month what ash was for," → "I asked you what ash was for," |
| WB-08 | = W6; applied once | — |
| WB-09 (F09) | Applied | 26:63 "And tomorrow's the Longshore. If they go today, you don't plant tomorrow." → "And Wednesday's the Longshore. If they go on Tuesday, you don't plant on Wednesday." |
| WB-10 (F10) | Applied | 36:383 "a fortnight ago" → "on Wednesday night". |
| WB-11 (F11) | Applied | 1:95 "four of them besides" → "three of them besides". |
| WB-12 (F12) | Applied | 46:101 "went over a race lip" → "had gone over a race lip". |
| WB-13 (F13) | Applied | 46:129 sentence reordered: "Kellan Renn, who had given the Clerk a folded sheet of fault paper at a quarter past eight, stood at the back of the small crowd at the gate with his mother's watch in his pocket and did not say anything." |
| WB-14 (F14) | Applied | 19:391 "when she got there" → "when Orla got there". |
| WB-15 (F15) | Applied | 39:59 "He was on the gallery" → "Hart was on the gallery". |
| WB-16 (F16) | Applied | 20:173 "The Company man let go of the line." → "The Company man on the third line let go of it." |
| WB-17 (F17) | Applied | 1:67 "eleven and four days… ten and four days" → "eleven weeks and four days… ten weeks and four days". |
| WB-18 (F18) | Applied | 31:227 "took the fourth corner" → "took a corner". |
| WB-19 (F19) | Applied, extended | 41:319 "a tun with a plank nailed under it" → "…a board…"; also 41:291 "nailed a plank across its bottom" → "nailed a board…" (the same tun, same scene). |
| WB-20 | Applied as decided (OD-5 a) | 41:249 clause added (§1). |
| WB-21 | Handled by R01, R06, R07, R08 | — |
| WB-22 | Handled by R02–R05 | — |

### 2.4 The habit edits (R01–R50)

R01–R22 were all applied (three in my own smaller wording, marked). Of R23–R50, one was declined.

| ID | Disposition | Chapter: before → after |
|---|---|---|
| R01 | Applied | 32:597 "It was not a quarter to seven. It was not on purpose. She did not write it down." → "She did not write it down." |
| R02 | **Modified** | 40:327 "Aske looked at her over his spectacles in the candlelight." cut; the next line's `"Nothing came," he said.` → `"Nothing came," said Aske.`, because the cut left "he" two paragraphs from Aske's name in a loft with other men in it. |
| R03 | Applied | 40:311 "There was the count, under the floor and the chandlery and the quay, four and four, going on." cut. |
| R04 | Applied | 40:299 `"Going up." He put the back of his hand against her cheek, as her aunt used to. "Two of them.` → `"Going up. Two of them.` |
| R05 | Applied | 40:299 "That's all I'll write. It's all I know." cut. |
| R06 | Applied | 40:377 "In the Board's press, in a black iron box with three locks, there was a paper with a seal on it and the hour, which would be opened at noon on Wednesday." cut. |
| R07 | Applied (OD-1) | 32:589 "Four and four. Fifty-seven to the minute, or faster." cut. |
| R08 | Applied (OD-1) | 40:375 the same refrain cut. |
| R09 | Applied | 31:321 "She did not say anything either." cut. |
| R10 | Applied | 31:345 "Rhea had nothing to say to that, so she did not say anything." → "Rhea had nothing to say to that." |
| R11 | Applied | 32:179 "Polglase did not answer that. He took" → "Polglase took". |
| R12 | Applied | 32:115 paragraph "Nobody said anything to that." cut. |
| R13 | **Modified** | 32:443 "Orla did not answer that. There was no answer to it. She sat" → "There was no answer to that. Orla sat". The reviewer's version left "She sat" directly after Coombe's speech, so the bad knee could be heard as Coombe's. |
| R14 | Applied | 32:465 "Hart did not say anything, but Peverell turned her head." → "Peverell turned her head." |
| R15 | Applied | 32:483 "Peverell said nothing. Then she took a pencil" → "Peverell took a pencil". |
| R16 | Applied | 29:49 Clerk's "She did not look at a paper." cut; quotation merged. |
| R17 | Applied | 46:259 the same, merged. |
| R18 | Applied | 36:115 the same (the Chair), merged. |
| R19 | Applied | 47:187 "Something moved at the corner of her mouth, and was gone." cut; quotation merged. |
| R20 | **Modified** | 40:349 "She looked at it for a long time." → "She read the top line again." Deleting the paragraph left the next one's "It was a name." pointing at the sub-headlines; the new line keeps it on *THE UNROOFED SKY.* |
| R21 | Applied | 48:89 "She stopped. She looked at it for a long time." → "She stopped." |
| R22 | Applied | 47:195 "He looked at it for a long time. Then he shut it" → "Then he shut it". |
| R23 | Applied | 15:41 paragraph "Nobody said anything for a moment." cut. |
| R24 | Applied | 15:487 paragraph "Nobody said anything." cut. |
| R25 | Applied | 14:243 paragraph "Nobody said anything for a moment." cut. |
| R26 | Applied | 13:507 "Nobody said anything for a moment. Mara," → "Mara,". |
| R27 | Applied | 16:69 "She did not say anything. She held it out" → "She held it out". |
| R28 | Applied | 43:249 "did not say anything. He was looking at her hand." → "was looking at her hand." |
| R29 | Applied | 47:223 "Kiva did not say anything." → "Kiva waited." |
| R30 | Applied | 43:157 "who looked at her and did not say anything," → "who looked at her,". |
| R31 | Applied | 36:229 "She did not look at Mara." cut; Peverell's speech merged. |
| R32 | Applied | 36:103 "She did not look at the sister." cut; Mara's speech merged. |
| R33 | Applied | 40:245 "She did not look at Rusk." cut; Mara's speech merged. |
| R34 | Applied | 35:351 Hart's "He nearly smiled." cut. |
| R35 | Applied | 47:267 Kellan's "He nearly smiled." cut. |
| R36 | Applied | 35:37 Kellan's "He nearly smiled." cut. All ten remaining "nearly smiled" are Pike's (one reported, 31:339). |
| R37 | **Declined** | 22:47 "Her face did what it always did." kept. It is Dray's owned tag (OD-6, which the showrunner left as is); it occurs four times across the book (17:149, 22:47, 29:69, 48:31), never twice on a page, so there is no cluster to thin. |
| R38 | Applied | 35:71 "with his hand pressed to his side," cut (35:67, four lines up, keeps it). |
| R39 | Applied | 46:39 "Perrin with his hand pressed to his side," → "Perrin with his ribs strapped," (the strapping is on the page, 33:55, 33:247). |
| R40 | Applied | 47:147 "Perrin at the end with his hand pressed to his side," → "Perrin at the end,". |
| R41 | Applied | 48:245 "At Perrin with his hand pressed to his side, at Jude" → "At Perrin, at Jude". |
| R42 | Applied | 19:15 "came in, slowly, all ten" → "came in, all ten". |
| R43 | Applied | 22:243 "with his heart going slowly and his hands on the cloth" → "with his hands on the cloth". The slowing is stated twice in the two paragraphs above; "Kellan did not move further" keeps the beat. |
| R44 | Applied | 28:255 "shook it slowly and properly" → "shook it properly" (Trewin's slowness stays at 28:243, "as he said everything"). |
| R45 | Applied | 30:227 "bent over, slowly, as a page turns" → "bent over as a page turns". |
| R46 | Applied | 35:35 "looked at her for a long moment." → "looked at her." |
| R47 | Applied | 42:297 "looked at him for a long moment." → "looked at him." |
| R48 | Applied | 43:101 "looked at her for a long time." → "looked at her." |
| R49 | Applied | 47:185 "looked at him for a long moment." → "looked at him." |
| R50 | Applied | 16:85 "I'm sorry. I'd want it said that we're sorry." → "I'm sorry." (Jude's own "I'd want it said" ten lines on is untouched.) |

Nothing protected was touched: the last section of ch. 48 (from the *no answer* line at 48:277 to the end) is byte-identical to the
frozen edition (SHA-256 of that section, before and after: `221198fc5d9066bdb4050cb2bba742b9f477ad1e7eb6db5b5d274cf390653a34`); the call words and card wording occur exactly as
often as before (*Set.* 17, *Nobody.* 14, *Far edge.* 6, "Then we look again, and either of us may say no." 4, "Not for a
bank, a floor, a crossing or a sale." 4, *The disk is cold.* 1); "Breach" 0; no ledger figure other than W2's and P3's changed;
the one-line hook endings of ch. 8, 26, 29 and 43 are untouched.

## 3. W2: the Hunt reconciled against its own board

The board's rule (29:49; 32:289): each four is marked on **a quarter of its clean yield, less a dram for every remark**. So a
four's clean yield is four times (mark + remarks). Places on the page are marked **P**; places 4, 5, 7 and 8 are the Movement
Four reconciliation (`MOVEMENT-004-CONTINUITY` §3), marked **R4**; the rest are this repair's reconciliation, marked **R**,
placed between the marks above and below them, with no remarks assumed. None of the R rows is on the page.

| Place | Four | Mark | Remarks | Clean | Source |
|---:|---|---:|---:|---:|---|
| 1 | Team Twenty-Eight | 11.80 | 0 | 47.2 | P |
| 2 | Old Four | 10.40 | 0 | 41.6 | P |
| 3 | Westerley second | 9.95 | 0 | 39.8 | P |
| 4 | Holloway second | 9.10 | 0 | 36.4 | R4 |
| 5 | Westerley first | 8.65 | 0 | 34.6 | R4 |
| 6 | Halden License | 8.20 | 1 | 36.8 | P |
| 7 | Holloway first | 7.70 | 0 | 30.8 | R4 |
| 8 | the Ropewalk second | 6.05 | 0 | 24.2 | R4 |
| 9 | — | 5.60 | 0 | 22.4 | R |
| 10 | — | 5.20 | 0 | 20.8 | R |
| 11 | — | 4.55 | 0 | 18.2 | R |
| 12 | the Ropewalk first | 4.10 | 2 | 24.4 | P |
| 13 | — | 3.80 | 0 | 15.2 | R |
| 14 | — | 3.40 | 0 | 13.6 | R |
| 15 | Team Seven | 3.15 | 0 | 12.6 | P (= 12.6 clean, 32:109) |
| 16–23 | — | 2.90, 2.45, 2.10, 1.65, 1.20, 0.85, 0.50, 0.20 | 0 | 47.4 | R |
| 24 | the Tarn first | 0 | — | 0 | P |
| | **Whole Hunt** | | | **466.0** | |

The on-page and M4 rows alone come to 328.4; the board's ordering puts a floor of about 403 under the whole Hunt and a ceiling
of about 534. Red at 4,181.2 of 4,647.2 combed is 89.97%, so Kellan's "Nine-tenths" and the *Mercury*'s "Nine Bags in Ten" stand.
Seven's 59.7 combed and 12.6 clean (M4 ledger) fit inside it. Kellan's spoken form: "Four thousand six hundred and forty-seven
drams and two-tenths combed… Four thousand one hundred and eighty-one and two-tenths red. Four hundred and sixty-six clean." His
argument ("every dram… except the tenth that happens to be dry") reads the same.

## 4. Measurements

### 4.1 Chapters changed (35 of 48)

`wc -w`, headings included. Whole book **326,226 → 325,945** (−281).

| Ch. | Words before | Words after | Δ | SHA-256 before | SHA-256 after |
|---:|---:|---:|---:|---|---|
| 01 | 5887 | 5889 | +2 | `5d07271eab66112c33402ab89d9d8fa8ecc9e420ede7fed3d4fb059e8fadb679` | `436fb3329cb8739768f35d6c449a5e4f31eebb60178b5a891e06921e7e2de410` |
| 03 | 5589 | 5599 | +10 | `ed82c428648e3a8372688d44f1e0bb47141fe75d9ac85c76d02b772ab579484a` | `c4120ba3ac84beeb780a5c4e5faecb3f965a1667d8de8d750e3195526e8ff632` |
| 08 | 6977 | 6973 | -4 | `2cf6a1091908ef2c91b399da139ab3a5291856f922e804fcb16e62d09e1b858c` | `d3523cb5f4cb50ce700b0aff8fc80e6220f911362924932a681e341f137dbb96` |
| 09 | 8918 | 8917 | -1 | `3a2316f2ef3e3e8f2f0da99b110d29cc27690b6c23d2610ef6f8740788728c0d` | `4f951492d37d8f80f178789db2d5dd1a42b7ca120701da45b735a6d2a186788d` |
| 13 | 7315 | 7309 | -6 | `0e3486e5103753ba4903f1159501207198ff64cea46b57e47e30f6fe1bc12a69` | `c3834e03c8298e4ac8cc5552c0abc3022eba896d60c50e868c1ccd19f930ca31` |
| 14 | 6134 | 6128 | -6 | `67950efe8ea329d1d1118bcf2e2ad733b6678a6ddc4db5df3d6b0d15a2ca044d` | `a879cca493717a47eabc862564c00290a5c1a7a555c0252f7067afc03268eb30` |
| 15 | 8423 | 8414 | -9 | `bbee01a321528b1c509c062eef91f9bd3d5a59a995128156115044815f667916` | `ae7960eb39d25f80027d54809f85c915bb9f50d2d163a3171f54f6f378010892` |
| 16 | 7032 | 7024 | -8 | `373064ceee6e79d74348b121be39e4d0773fc065a920d2a8e20235b04314be69` | `712bf52cd168daf4629841dfa7a6c63340ca01d1e62e7d858b1e17edc0498685` |
| 17 | 7158 | 7161 | +3 | `1aaa7d0c5dca778d9ee417ec3d150dc699d0f8d42e535df3a3bd4ad40ce9e0e2` | `dbbb78fa53a5878c4c46a9facaf1c2bcfa6707639a85891c3873464c177a427a` |
| 19 | 7611 | 7610 | -1 | `4a633ce44804458cadd5db1f6ef616ef12a3577ae75b504fd9b9f4ef6585b9c8` | `2946d2594d6c4f2aab58d8f358874967b8ac986fe04243426dac100108a2fb6f` |
| 20 | 7091 | 7094 | +3 | `e5e81ac2b8101dc8ff9027b01eac6126525c9f4afc021b2ccb4ebea57ad4b4b4` | `21bd8a0aae6381b5636b197f76857c9ea81c473b6dd4382f9690d61b831d30bd` |
| 21 | 6562 | 6558 | -4 | `a3684d2b25cf7dc4cd3029819d632c3aa582663b35e50a9611e704b4aaca5dcb` | `2c61f1905c47ad7c39bf397642e800bc63b0f3d419fbed440443158eb0bd81f4` |
| 22 | 5784 | 5779 | -5 | `9d66769d01be3e55e481533c179e45957b0d47c0e79182f0bbdd86ff4821b9f6` | `698872859d82a4f6fb30becc84783fb99e3ab9201622449dc7bc9d28c9d2cd0d` |
| 25 | 6356 | 6364 | +8 | `fbd034ec2f9c353dbbb82243bd0b95a3ac0e90bc580b91a864babb998b6e365d` | `59653f7f481162d4e88739b1c573adc748267062050a5a6c21681542159473d1` |
| 26 | 5104 | 5106 | +2 | `131cf5810a7417aa9b821f2da50416a2bcdc3dafd091cacdc712323965a035bb` | `e51f0c51773bb1447c3cd4ab7201dd1e727fd600ed0ff593697e21830f327da7` |
| 28 | 5023 | 5021 | -2 | `7f7f8031d8753b9ec72db291ef7e9e17519db855aa7f123b37566dd91d3e9cf2` | `a3d147679948502b05ee1879e37f7d347de0228acb8fab2b75121edc0b86e5dd` |
| 29 | 6189 | 6186 | -3 | `da733c71224bd30b96fffe8a5bc837335b2c3ee45cc88bdf5ee76ba0013dd55a` | `9fc46737f1933c505a25774e156b43e32d422712aa4543094b8fd635b17318fe` |
| 30 | 6357 | 6356 | -1 | `a4e471b5833a6a2695f171ca54f42f8b99a029383544a9c8776c746d7078357f` | `4684b0bad35aa1062c1255a93ffda1844a5bb9ec6a2be02768ec0b387a106a87` |
| 31 | 6659 | 6646 | -13 | `b76920e9986a1b7a2a0e3ed258d560a799d4c91f7c6e23691fff22d4614cdf7b` | `c2fad74e257925f8d194a1967f35d34a0e9577083d453fecb7958ede136f9a7e` |
| 32 | 9245 | 9199 | -46 | `97794571410b5772ae55f8dd182be9e4bf948d2d1a9515913f262667c9c2f299` | `835eb0caf7137d74ee6c7e164707026b796e9484920b0f203d45ee72c29376fa` |
| 33 | 8542 | 8537 | -5 | `08763fef4ddc5d98592f666905a37ba7f682c8d96d8cfc770801755a140db746` | `55ccaf402eb63a5d0a613f4006efa8c5e02bfee877b5c3a31e0af9fa2c8b5102` |
| 34 | 6369 | 6365 | -4 | `db02be11b209ceb017084cff4e5fe8f70c87360f470e43271e6c297bb2f370b3` | `6b24e7abe844e79643e77c8f20c6e956e51f0bd40b98443ddeebe0f05aaf5f35` |
| 35 | 6023 | 6006 | -17 | `06cb0ba9c9e6c4b945812022e5d642a632e4420e2e78d4810bc7362f36b389db` | `1dee7ed8caabd3adee8a78fc67dd3e259b516d8a0e8888e052bad5cb043362e1` |
| 36 | 8147 | 8131 | -16 | `12a152b5c534548360d8dbe5f8353bc2751fb0726f7bb5c17812f04978734dd8` | `6a61fd68ff8acdc00884382e11b23a6ca03dcf802db5a7ccfe939b3dbc524457` |
| 37 | 6636 | 6629 | -7 | `62c3aa882679c809e0159dd3208b74710a6f87a1bac70613ec658f3915faa375` | `59097370d58d817dc2ee871f50ec004d5189dcbe4cc1e38ec8ff4a0e3fc7f7be` |
| 38 | 6135 | 6126 | -9 | `14146e401424effa5cac1e2526e234bebae925021fe71d7df3b4e109608a4462` | `3f67d10d46a1186bf0b3d912ba19f3298f391753b1172f1aa913c05cba59e24a` |
| 39 | 5585 | 5585 | +0 | `f223af04ed884268dd0b9d6b27df57b39717f61cde0547d105c995512b9a5acd` | `b98bf1b5d59c048dcb45188ce8894d3f8dfa334c7e8acb2c0192ae9d779d36d5` |
| 40 | 8060 | 7972 | -88 | `b23b1a3f0229fcba82e1ab832903115bb1a553a0cbc5e85d7fc2438767edc5e3` | `4c32f991450a9104fe9cc37615346469383cc72753fb715dc7d451530fc11aee` |
| 41 | 7199 | 7231 | +32 | `39187cd04eb9b527936d09ba274380896202a40b9193e6fdd40f648de4a77850` | `a67ed23f4ac8db2330dce78c4f0521211f32435e5bb662484dde23bc32efd104` |
| 42 | 6904 | 6900 | -4 | `7ff5d82ec7129b91ba3f522673511034a7e73ca6bd5b44527a6bc97ac91386e6` | `b569c1f507d74dde5e821820b1d6fef6e9903a6b390fc22f00ee9b9be909d002` |
| 43 | 5729 | 5715 | -14 | `28e0228f08f475bfa4dcd77ca80538733d0a73b69e84e302b4abd74f3bca8270` | `18aeddbbc35392f2fb20c6d66738b361d4a4ce138ec79c07b9b9e81c0fbd38b1` |
| 44 | 8432 | 8432 | +0 | `aec986b8e1595681c2ab57830ce40c17badd95eef5ea37a9177b44da7efeb316` | `c81c856671d9d99886dbdb6f7277b5111fe0beb3f18c201d46abd97a2f441ace` |
| 46 | 7134 | 7121 | -13 | `3de722446b1d292259b33607c851e83d1631251e7fbca8b6e2d3435641d2f582` | `8b6b8de0ac006f9c9229284f38997c5b671d9be30e536dd396725af875ae05af` |
| 47 | 7206 | 7175 | -31 | `a6f4a501b7837fec4150223a3d4e9c1ebf42ef17987e4b4d157992e542b4d0a0` | `6e3de61edfe18bdba53b0e7f25a0e4a1fc71eb667d07c94c945443172f0dc1c5` |
| 48 | 6453 | 6429 | -24 | `b9fba4d1a77d56751434d0d865ffbb260e8f7dcc5d19ebf4a8e30f72d86e4002` | `0e8c628ef774bcf31a7acfb0b8014c9be67c86bdfb5a1ed2614c0aa33c1a0315` |

Unchanged: chapters 2, 4, 5, 6, 7, 10, 11, 12, 18, 23, 24, 27, 45 (each still matches `editions/whole-book-pre-repair/SHA256SUMS.txt`).

### 4.2 Tic families (raw substring counts over all 48 chapters, case-insensitive)

| Family | Before | After |
|---|---:|---:|
| "did not say anything" | 67 | 60 |
| "said nothing" | 37 | 36 |
| "Nobody said anything" | 23 | 18 |
| "did not answer" | 32 | 30 |
| "did not look at" | 92 | 86 |
| "did not look up" | 41 | 41 |
| "nearly smiled" | 13 | 10 (all Pike's) |
| "slowly" | 128 | 124 |
| "pressed to his side" | 25 | 21 |
| "for a long time" | 59 | 55 |
| "for a long moment" | 42 | 39 |
| "looked at it for a long time" | 10 | 7 |
| The Clerk's / Chair's "She did not look at a paper" | 6 | 3 |
| The Clerk's "Something moved at the corner of her mouth, and was gone" | 3 | 2 (48:211 is a different sentence) |
| "Four and four. Fifty-seven to the minute" | 6 | 4 (once at a movement end, 24:383) |
| "Anwen never went red" | 3 | 0 |
| "long brown face" | 4 | 0 |
| "Sedge" / "Shapter" | 16 / 0 | 0 / 16 |

Correction, 2026-10-15 (second repair, from `WHOLE-BOOK-RECHECK.md` §6 item 4): the refrain row's figures were a case-insensitive
substring count; the exact sentence "Four and four. Fifty-seven to the minute, or faster." occurs **4 → 2** (24:383, 41:7). The
claim it supports, once at a movement end (24:383), is unchanged.

### 4.3 Quote parity (all 48 chapters)

Scan: split each chapter into paragraphs on blank lines; flag any paragraph with an odd number of `"` that does not open a
multi-paragraph quotation (the next paragraph opens with `"` and this one does not end with one). Compared paragraph by
paragraph against the frozen edition.

- **New odd paragraphs: 0.**
- Odd paragraphs overall: 6 before, 6 after; of these, 3 open multi-paragraph quotations and 3 are not dialogue at all: the
  inch marks in Hart's slack log, ch. 26 (*The 8th. 6.12. Quiet. 4' 6½".* and the two lines after it). All 6 are unchanged.

### 4.4 Frozen edition

```
$ cd editions/whole-book-pre-repair && shasum -a 256 -c SHA256SUMS.txt
chapter-01.md: OK … chapter-48.md: OK        (48 OK, 0 failed)
```

## 5. Owner items (recorded, not decided)

### 5.1 W4: Pettit and Yarrow against Book One (not changed)

Book One: Pettit is Halden's **Kill**, a blade who lights (an Ember edge: ch. 32:79, 34:201–211, 37:225, 38:133); Yarrow is
a **still door** (ch. 43:111; Book One ledger: three student still-doors, Wace, Hendry Moss, Yarrow). Book Two: Pettit is a
still door (12:29, 12:111, the leaning duel with Perrin at 12:213–215, and the third still plank at M3 through ch. 42–44);
Yarrow is a hand door (12:111) on the catchers' plank of wards (41:313; 43:149; 43:251; 44:123). Birch's "nothing to put on
[the blade line] since the fifth month" (6:457) also conflicts with Pettit as a blade at Book One's Regional.

No option fits the brief's limit of about eight changed lines without adding an event:
- **(a) Give each a second door in Book Two** (Pettit Ember and still; Yarrow still and hand). Lines: 12:111, 6:457, and
  17:453 ("the only person in Meridian who had to be read"). But the Measure's rule reads "any candidate with more than one
  door … from a sanctioned mast" (17:333), so both would need readings at the gate that the page does not show (17:375–389),
  each one either "one line" or "an incident". That is a new on-page event, not a located correction.
- **(b) Keep Book One and recast Book Two.** Pettit's door → edge at 12:29, 12:111 and the duel at 12:213–239; someone else
  becomes the third still plank (Yarrow, by Book One) at 42:165, 43:153, 43:185, 43:241, 43:289, 44:261, 44:281, 44:285,
  44:299, 44:369, 44:421, 44:423, 44:467; a ward replaces Yarrow on the catchers' plank (for example Hesketh) at 41:313,
  43:149, 43:251, 44:123; 6:457 rewritten; ledger M6.5 ("Pettit: boots frosted"). More than twenty lines, through the climax.
- **(c) Accept the discrepancy** for Book Two and carry a note for any Book One errata (outside this repair).

### 5.2 Carried from the brief (unchanged; listed so the record is complete)

The colour "brushed twice" (45:157; 48:317); the certificate precedent; the new interaction properties (reading a count through
a still door; "one hold"; Thrale's ward holding water; no fever after two masters); the revised bible §6; Hollis Vane's absence
(and his planned "off the roll" turn, which the page drops: CHARACTERS still plans it); whether the sentence targets govern
dialogue; the progression density; the Home Line roll turn dropped; the tide clock; the 41-minute hold; the brown-ink line;
"my best machine"; Penhale's ward as frost; the Order's six questions left open (four of them); whether Book Two's last page
should lean outward (the hull).

### 5.3 Seen during this repair

1. **39:189**, the Proprietor: "I'm sure of my reading. I've been sure of it for seventy-seven years." Four lines after "I've
   had it since I was twenty-seven" (39:185), this is P4's arithmetic again (seventy-six). P4 was scoped to 47:183 and 47:233,
   so I left it. The same reading would make 39:251 ("I've spent seventy-seven years not learning the difference") a round
   figure from the window. Owner's call whether 39:189 follows P4.
2. **47:29**, Hart: "near the bank for twenty years and near the Regiment for six months". The Regiment is the town's name for
   the harbour bank, so heard aloud the sentence may make two machines of one. Raised by the promises review "in passing";
   not in this repair's list.
3. **The Hunt rows 9–11, 13–14 and 16–23** (§3) are this repair's reconciliation and are not on the page. If a later scene
   prints another place's mark, check it against §3.
4. **The Barrel and the Well.** The book never prices a Well. 686.4 sits above the Flask's "best part of five hundred"; if the
   series later gives a Well a figure, it must be above that.
5. **Plan differences still open** (the continuity review's §2, not caused by this repair and not edited): CHARACTERS for Pru
   ("catches a national board when Kiva is down with fever"), Vane, and "Rusk and A. Renn travel"; BOOK_MAP §6's 10.53;
   UNIVERSE_BIBLE §7.6's date for Kiva's proof.
6. **Pettit and Yarrow** also appear in CHARACTERS.md only by name; the dated note added there points to §5.1.

## 6. Records reconciled

- `STATE_LEDGER.md`: M3.1 (the yes/no hour, recorded once: evening from Sun 13th to Sun 20th; morning from Mon 21st); M4.4
  (Coombe's new rope); M5.7 (Thrale's reach in the Graving; Kellan's figures); M5.9 (Shapter, with the reason); M6.1 (the
  Slack's crossings are the eighth and ninth in Book Two, Aske's seventh and eighth; the morning hour); M6.3 (686.4); M6.10
  (a pointer to this record).
- `provenance/MOVEMENT-002-CONTINUITY.md` §8: Thrale's jars ("forty-one since she was made Master, forty-four before").
- `provenance/MOVEMENT-003-CONTINUITY.md`: the yes/no hour.
- `provenance/MOVEMENT-004-CONTINUITY.md` §0 and §10: Orla held the card "ten days"; Coombe's new rope.
- `provenance/MOVEMENT-005-CONTINUITY.md` §3 (Kellan's figures), §5 (Thrale's reach), §12 (Shapter; the "no collision" was wrong
  for Sedge).
- `provenance/MOVEMENT-006-CONTINUITY.md` §8: the crossings' numbering; 686.4.
- Each of the six continuity files has a closing "Whole-book repair reconciliation" section naming what changed in its
  chapters.
- `BOOK_MAP.md` §3: a dated note that the prose now gives seventy-six years of belief (P4).
- `CHARACTERS.md`: a dated note under the continuing cast giving Pike's, Adlam's and Lyle's descriptors as the prose holds
  them, Shapter, and the W4 owner item.
- `AUTHORSHIP.md`: a whole-book repair entry.
- The continuity review's §3 record defects: 1 (M2 jars), 2 (Sedge "no collision"), 3 (Kellan's totals), 4 (Orla's "a
  season"), 5 (the yes/no hour) and 6 (the crossings' numbering) are all corrected.

## 7. Status

Repaired, **not rechecked and not accepted**. Nothing committed, pushed or published. A fresh-context recheck of this repair is
the owner's to commission.

## 8. Second repair (2026-10-15)

- **Seat:** Claude Opus 5.5, runtime-reported `claude-opus-5-5` (not verifiable from inside the session); a forked continuation
  of job `32af798e`, session link https://claude.ai/code/session_01FdPqTPms8bcVHbZ9JXn9ec. Brief
  `planning/OPUS-5.5-WHOLE-BOOK-SECOND-REPAIR.prompt.md`, SHA-256 `a341c3fb4d8f683d3a7e27455bf4a5adad1f78755ca4aa2559a587686adfe982`,
  from the fresh-context recheck `provenance/WHOLE-BOOK-RECHECK.md` (job `59421479`), §7–§8. The showrunner authorised D3.
  No subagent, other model or Skill tool.
- **Exactly these edits, each applied by an exact-once replacement:**
  - **D1** (W12 completed) `chapter-33.md:71`: the sentence "Thirty-six hands would be on thirty-six glass cases." cut. The
    paragraph now runs "…the basin would go still for twenty minutes. Somewhere in it, if anybody asked her, she would be
    calling…"; "it" refers to the still basin. The number of hands was Mara's Wednesday-night decision, which Kiva did not yet
    know.
  - **D2** (WB-04, surviving instance) `chapter-42.md:207`: "She did not go red, because she never did." → "She did not go red."
  - **D3** (P4 residue) `chapter-39.md:189`: "I've been sure of it for seventy-seven years." → "…seventy-six years." 39:145 and
    39:251 left (they count from the window). The book now gives one figure for the reading's age, at 39:189, 47:183 and 47:233.
  - **D4** (records) `MOVEMENT-006-CONTINUITY.md` §2–§3: "Sedge" → "Shapter" in the three rosters (Pass 1; who stood; the
    planks). The dated rename note in its closing section is kept as history.
- **Records:** `MOVEMENT-005-CONTINUITY.md` closing section's ch. 33 line now says what replaced the sentence; the ledger does not
  record the sentence, so it is unchanged. `BOOK_MAP.md`'s P4 note extended to name 39:189, 47:183 and 47:233. The §4.2
  refrain figures corrected above (4 → 2), after checking the count against both editions. One sentence added to the
  whole-book repair entry in `AUTHORSHIP.md`.
- **Checks:** quote parity of chapters 33, 39 and 42, working and frozen: 0 odd paragraphs that do not open a multi-paragraph
  quotation in each. `cd editions/whole-book-pre-repair && shasum -a 256 -c SHA256SUMS.txt` → **48 OK, 0 failed**; nothing
  written there.

| Ch. | Words before | Words after | SHA-256 after |
|---:|---:|---:|---|
| 33 | 8537 | 8529 | `f584ff623f871dfe4108aae61816e35f729d0d3af6f5f82344d62a9fd7099da6` |
| 39 | 5585 | 5585 | `6eec65de0644f1a92aa58b2c05aa0592d4a528f022aa5dddd3bb4035f8357356` |
| 42 | 6900 | 6896 | `6d9e7dca70bead9dae377f17c457607434da5e0e690bce5ebb5a286a8e179506` |

Whole book (`wc -w`): 325,945 → **325,933**. "Before" here is the first repair's state (§4.1). Nothing else was touched. Not
rechecked, not accepted, not committed, not published.
