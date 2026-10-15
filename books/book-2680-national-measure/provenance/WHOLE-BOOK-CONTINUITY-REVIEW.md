# The National Measure — whole-book continuity review (layer A-CONTINUITY)

> Built by TAC

## 0. Who and how

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), a fresh-context session run as background job `6f04bed8`,
  2026-10-15. **This is a same-model-family simulated review.** It is not human reader feedback and not
  independent testing. The book's author seat is the same model family.
- **Scope:** the whole-book layer only: defects that cross movements, or that no movement-sized review could see.
  Style, formula scores and rewrites are out of scope. No subagent or other model was used. Nothing in
  `manuscript/`, the ledgers, the map or the canon files was edited. This file is the only file written. Nothing
  was committed or pushed.
- **Line numbers** come from `grep -n` on `books/book-2680-national-measure/manuscript/` during this run. I did not
  change those files, so the numbers stand. The accepted audio-clarity edits to chapters 8, 9, 11, 14, 15, 19 and 24
  (`provenance/AUDIO-*-REPAIR.md`) are not flagged. I checked that none of the findings below falls on a line those
  repairs changed.

**Read in full:** `STATE_LEDGER.md` (sections 1–11 and all six movement blocks); `provenance/MOVEMENT-001-CONTINUITY.md`
to `MOVEMENT-006-CONTINUITY.md`; `BOOK_MAP.md`; `OWNER_BRIEF.md`; `UNIVERSE_BIBLE.md`; `CHARACTERS.md`. I also read every
movement join in full: the last 100 lines of chapters 8, 16, 24, 32 and 40, and the first 100 lines of chapters 9, 17, 25,
33 and 41.

**Checked by targeted grep and local reading:** all 82 weekday-and-date pairs (by script, against the ledger calendar);
all 130 interval phrases ("a week ago", "since Thursday", "a fortnight", "last Wednesday" and the like), each in context;
every on-page "Held" figure; the sealed tin; the Order's jars; the hunt shares and board marks; every crossing; injuries
by person and side; finger counts; the yes/no log; the dream's occasions and who knows what; eye, hair and face
descriptors; ages; pronouns; team colours; doors by person; ranks; Saltmere distances; the Hoop's heights; slack times;
year references; and new names against Book One.

**Book One (`books/book-2680-opening/`)** was used only to test locks, at located points: the ledger (§§ on the body,
three doors, names and pronouns) and manuscript chapters 3, 15, 24, 32, 34, 36, 37, 43, 47 and 48.

**Not read:** the 326,000 words end to end (I estimate that I read under a tenth of the prose directly); the editorial
reviews, cold reads, rechecks and repair reports (except the four `AUDIO-*` files, which I grepped); `packets/`;
`planning/`; `narration/`; `WHOLE-BOOK-REPETITION-DATA.md`; the Book One manuscript beyond the located passages.

## 1. Findings

Severity: **BLOCKING** (a reader or listener would be misled), **CONTRADICTION** (two passages disagree), **CLARITY**
(one passage is unclear or wrong on its own). Each finding is a defect in the prose unless it is marked as an owner decision.
Plan and record differences are listed separately in §2 and §3.

| ID | Severity | Location | Quoted text | Problem | Evidence | Smallest fix |
|---|---|---|---|---|---|---|
| **W1** | **BLOCKING** | 21:263 (also 3:149, 16:353) | 21:263 "telling her what she had seen when she was thirteen and again on Classification Day. Mara had written it down… and sealed it" | Mara's memory says the sealed page records the thirteen and Classification Day dreams. The page records the **Pit** dream of the 29th of the fifth month. A listener is told one thing about the book's central exhibit and later hears another read aloud. Chapters 3 and 16 also count only two earlier occasions, which leaves the Pit out. | Book One ch. 24:111–113: that night Kiva told "the height, and the roads… the notes… lost her number at four… It ticked. Once." Book Two 34:107 and 36:325 ("In the Pit last spring, and my aunt wrote that one down the same night"); 40:43 and 40:65 (the page dated "The 29th of the fifth month, 2680. Ten at night"); `STATE_LEDGER` §2 (corrected at the Movement Five repair). The Movement Five repair fixed ch. 34, 36, 37 and 39 and missed these three earlier lines. | 21:263: "…telling her what she had seen that afternoon in the Pit." 3:149: "…it had come again in the spring, on Classification Day, and once more in the Pit, in the fifth month." 16:353: "…when she was thirteen, and on Classification Day, and in the Pit…" |
| **W2** | CONTRADICTION | 36:29, 36:193 against 32:289–295 | 36:193 "Four hundred and twelve drams and four-tenths combed… Three hundred and seventy-one and three-tenths red. Forty-one and a tenth clean." | The Hunt board is marked on "each four's quarter of its clean yield" (32:289). Twenty-Eight's 11.80 alone means 47.2 clean drams, which is more than Kellan's total for the whole Hunt. The six fours named on the board (places 1, 2, 3, 6, 12 and 15, remarks added back) come to **202.4** clean. Places 1–15 under the board's own rule come to at least about 375. Seven's own clean bag (12.6, 32:109) is nearly a third of Kellan's total. | 32:291–293 (11.80; 10.4; 9.95; 8.2 with one remark; 4.1 with two; 3.15); 32:289 (the rule); M4 ledger (Seven 3.15 = a quarter of 12.6). Kellan's figures are repeated in `STATE_LEDGER` M5.7 and `MOVEMENT-005-CONTINUITY` §3. | **Owner decision.** Restate the three Hunt figures in 36:29 and 36:193 (and the claims line "The Measure to date: 371.3" in 36:29) so that the clean total is at least what the board implies, with red still about nine-tenths. For example: combed 4,513.0; red 4,061.7; clean 451.3. The author should reconcile the exact figure against the board. Then correct the two records. The board, "Nine Bags in Ten" and Seven's 3.15 can all stay. |
| **W3** | CONTRADICTION (Book One lock) | 9:27 | "What you did in the eighth month is in your book, and in your book it stays. I'll not count a thing that I didn't see on a tape." | Orla says she did not see the eighth-month hand-to-Ember crossing on a tape. She did. | Book One ch. 36:13–15 (Kiva declares it "for the mast, since Noa copied every tape to the Chair… It isn't on my paper. It doesn't count toward anything") and 36:131–135 (Noa reads it off the tape; Orla counts the hand). Book One ledger: five tries "on a sanctioned mast in the eighth month". | "…I'll not count a thing you told the mast didn't count." |
| **W4** | CONTRADICTION (Book One lock) | 12:111; 44:285; 6:457 | 12:111 "Captain, Pettit, carry. Still. Catcher, Yarrow. Hand." 44:285 "He was a still door, square and sleepy" | Book Two has Pettit as a still door and Yarrow as a hand door. Book One has Pettit as Halden's Kill, an Ember edge, and Yarrow as a still door. Birch's "nothing to put on [the blade line] since the fifth month" (6:457) also conflicts with Book One's Pettit as Kill and as the second blade at the Regional. | Book One ch. 32:79 ("Their Kill's a second-year called Pettit… four-tenths at the top"); 34:201 ("lacing his cuff… I'm to carry"); 37:225 ("They had two blades… Pettit"); 43:111 ("Yarrow… He was a still-door"); Book One `STATE_LEDGER` (three student still-doors: Wace, Hendry Moss, Yarrow). At the Slack Pettit plants at M3 with his still door, and Yarrow stands on the catchers' plank. | **Owner decision.** Either (a) give Pettit a second door and Yarrow a ward in one Book Two line each, which brings Pettit under Dray's mast rule at the gate; or (b) keep Book One and recast: Pettit's door at 12:111 and 44:285 becomes an edge, another still door takes M3, and Yarrow leaves the catchers' plank. Option (a) is the smaller edit. |
| **W5** | CONTRADICTION | 40:89, 40:167, 40:229 against 38:79–85, 41:227–231, 43–44 | 40:167 "Kiva felt her doors, which had been lying down since two, lie flatter still" (with Thrale "three hundred paces off", 40:89) | In the Graving on Sunday, Kiva's doors lie down at about 300 paces for the whole hour, and her fever is held down until Thrale leaves (40:229). On Monday the plan for the Slack rests on "every door within forty paces of her", with Kiva at the table (41:227–231). At the Slack Kiva crosses at the sill at 6.11, sixty paces from Thrale. | 24:37 (gate "three hundred paces off" from the pen); 40:25 (Thrale walks past the bench to the gate); 38:79 (forty paces on the quay); 41:231 (the sister paced forty "on the quay, on Saturday"); M6 ledger M6.3 (Thrale sixty paces from the sill until 6.15). | **Owner decision.** Either (a) add one exchange at 41:231 in which Kiva says what happened on Sunday in the Graving and somebody gives the reason forty still serves on the morning (a new rule, which needs pricing); or (b) edit 40:167 and 40:229 so that the doors lie down as Thrale passes the bench and get up as she walks on to the gate, and give the fever's hold another cause. |
| **W6** | CONTRADICTION | 17:139 | "Halden License had come down by the station transit three days before" | The 27th is impossible. Halden leaves on the 28th, and the transit takes a day and a half. | 6:461 (Birch: "by station transit on the twenty-eighth of next month… a day and a half, with a bed"); 17:157 (Kellan: "The transit was a day and a half"). | "…had come down by the station transit the night before…" |
| **W7** | CONTRADICTION | 37:137 | "she had walked onto the timber pond on two sticks a fortnight ago and onto the Long Quay on one" | Dray was on one stick from the day she arrived (and had been on two only in Meridian). The order is reversed, and the gate was eighteen days earlier, not a fortnight. | 17:143 ("She had one stick, not two", the loft, Mon 30th); 17:441 and 17:467 (on her one stick at the gate, Tue 1st); 21:9; 22:11 and 22:47 (no stick by Thu 10th). | "…that she had walked onto the timber pond on one stick at the gate, and that she was walking now on none." |
| **W8** | CONTRADICTION | 17:261 against 17:295; 36:29, 36:189 | 17:261 "I've combed four hundred tins since seven o'clock… That's the first that's been silent on the seventh." 17:295 "That's the third I've combed this morning." | The soot-cut jars are old plain ash: "The seventh's right" (17:291). If the clerk had combed two of them earlier that morning, they were silent on the seventh too, and Seven's tin was not the first. Kellan's fortnight count of four silent tins (36:189) also leaves no room for them. | 17:283–291 (the Tarn jar: third thin, seventh silent); 16:91 (the Ottery jar: silent on the seventh); 36:189 (four silent: Seven's, the Tarn's, a Westerley healer's tin, the reference jar). | 17:295: "That's the third I've seen this winter." |
| **W9** | CONTRADICTION (Book One lock) | 32:435 | "I held a card a season," she said. | Orla held Hart's card for about ten days, not a season. | Book One ch. 48 ("It had come on Friday, by the coast boat", two days before Book One ends); Book Two 2:353 ("she had sat on it for nine days"); she handed it over on Mon 24th of the tenth month. | "I held a card ten days," she said. |
| **W10** | CONTRADICTION (Book One lock) | 46:79 | "It was eight-tenths in the autumn and Rowan said it'd stay eight-tenths till somebody killed something quiet." | The line is attributed to the wrong person. Anwen said it. | Book One ch. 48:245 ("'It can't be made up,' said Anwen… it stays eight-tenths until somebody kills something quiet"). | "…and Pryce said it'd stay eight-tenths…" |
| **W11** | CONTRADICTION | 42:359; 41:3; 46:3; 48:273 against 24:305–323, 33:463, 36:83, 38:129, 40:313 | 42:359 "She had laid her fingers on it every morning at a quarter to seven" | Hart's method is "same hour every day" (24:333). The log starts at a quarter to seven in the **evening** (24:319) and is kept in the evening every day to Sunday the 20th. From Monday the 21st it is kept in the **morning**, and 48:273 treats the morning as the standing hour ("She had let the morning's go by"). No line marks the change. | 24:319 ("A quarter to seven in the evening"); 33:463 (after the 6 p.m. board); 36:83 (the Salt Hall, before the 7 p.m. sitting); 38:129 (before the 8 p.m. reading); 40:313 (Sunday evening fever); 41:3 ("on Monday morning"); 46:3 (Wednesday dawn, at the Slack). | 42:359: "every morning" → "every day". **Owner decision** on 41:3: add one clause saying that from this day she takes the morning quarter to seven (Sunday's had been Pru's), or accept "a quarter to seven" as either hour. |
| **W12** | CONTRADICTION (knowledge) | 33:71 | "Thirty-six hands that were not her aunt's would be on thirty-six glass cases." | At 7 a.m. on Thursday Kiva knows Mara's plan. Mara made it at 10.30 on Wednesday night with only Peverell and Hart present, and nobody tells Kiva before the page shows her this thought. | 32:449–475 (the decision, Mara's lens); 32:499–597 (Kiva is with Ivey at Quiller's from a quarter to eleven, then in bed); `STATE_LEDGER` M4.5 ("Mara's thirty-six: Peverell, Hart"). | "Somebody's hands would be on thirty-six glass cases." |
| **W13** | CONTRADICTION | 46:9 | "She had written it in her book with her right hand, for the first time since Sunday" | She last wrote right-handed before the burn of Wednesday the 16th. On Sunday Pru wrote for her. | 33:469 and 34:183 (left-handed, Thu 17th); 40:319 ("Written by Finch"); 41:9 and 42:195 (left-handed, Mon and Tue). | "…for the first time since the Hunt…" |
| **W14** | CLARITY | 19:167 | "She had spent a year trying to make the two fingers tell her something." | The fingers went in the ninth month of 2680, about five months before this scene (Fri 4th of the third month). | Book One ledger (Aske, the 24th of the ninth month); Book Two 16:135 ("in the Pit in the autumn"). | "She had spent a winter trying…" |
| **W15** | CONTRADICTION | 42:179 | "She had a long pale face and very dark eyes" | Maud Lyle's face is "square" everywhere else. | 17:341 ("fair hair cut to her ears and a square, careful face"); 33:177 ("Lyle's square face did not change"). | "She had a square pale face and very dark eyes" |
| **W16** | CONTRADICTION (name collision) | 37:143; 41:125, 301, 307, 311; 42; 43; 44 (13 uses) | "Sedge, ward." | Book One already has a Sedge: the Kiln's warden, she, at the Regional. Book Two gives the name to Twenty-Eight's Hold. A returning reader will look for a link that isn't there. | Book One ch. 21 and 38:185, 303; Book One `STATE_LEDGER` line 173 ("the Kiln's warden is Sedge"). The `MOVEMENT-005-CONTINUITY` §12 note "no collision" is wrong. | **Owner decision:** rename Twenty-Eight's Hold at all 13 places, after a registry check. |
| **W17** | CLARITY | 16:221 | "She had been near a Blaze for a month." | Coombe was in Meridian for twelve days (the 2nd to the 14th) and left twelve days before this scene. | 9 (arrives Mon 2nd); 13:495 (leaves Sat 14th); M2 continuity ("Twelve days in Meridian"). | "She had been near a Blaze for a fortnight." |
| **W18** | CLARITY | 29:53 (also 32:403, 423, 445) | "She stood where she was by the comb table with her rope, and she began to tie a knot in it" | Coombe left her knotted rope on Seven's shed step, and Perrin has carried "Coombe's rope" ever since (21:57; 24:363). No line gives her a new one, so a listener may think that Perrin's rope is back with her. | 13:495; 21:57; 22:313; 23:135; 24:363. | 29:53: "…with a new rope, half knotted already…" |

Idioms I checked and did **not** flag: "a week ago" used for eight or nine days (39:99, 39:133, 39:249, 40:293, 40:325);
"a fortnight off" for twelve days (26:193, Hart's speech); "twenty years" for the 2660 Bench (2:353, 19:377, 32:435), against
Orla's "one-and-twenty years" on the crate (9:17). Each reads as speech or rounding, and none changes a sum.

## 2. Plan differences (BOOK_MAP, CHARACTERS, UNIVERSE_BIBLE): not prose defects

1. `BOOK_MAP` §6 (Movement One exit) and §8: the book is 10.53 after the warrant. The prose has **9.64**, already recorded
   at Movement One, item 1.
2. `CHARACTERS` (Pru): "Catches a national board when Kiva is down with fever." On the page Pru catches the Bench
   because of the Chair's condition, and catches seeding lane 3 because of Kiva's fever. Recorded as open at Movement Three,
   item 5, and not closed in any later record.
3. `CHARACTERS` (Vane): "Calls Kiva off the roll for the first time, at a day rate. Directs the Line's part at the Slack."
   Neither happens on the page. The Slack absence is a carried owner item (M6.10). The call that never comes is not recorded
   anywhere as a departure.
4. `CHARACTERS` (Rusk and A. Renn): "Rusk and A. Renn travel." A. Renn stays in Meridian (she wires a parcel note on,
   ch. 17).
5. `UNIVERSE_BIBLE` §7.6: "Kiva in 2676, proved independent by a sealed and timed page." The page proves the 2680 Pit
   dream. §7.6 also dates Annick "Glory, 2431", while the Clerk's finding (40:259) says her notebook was written "between 2446
   and 2450". Those two are not in conflict, but the bible gives no year for the entry.
6. `UNIVERSE_BIBLE` §6 and `BOOK_MAP` §2: the caller "has been inside both gaps". The line is revised in-world (Ivey,
   ch. 47–48). Already a carried owner item.
7. `BOOK_MAP` §12: Rhea goes short in Movement Four. She goes short in Three; the dated note is already in the map.

## 3. Record defects (ledgers and continuity files): for the next reconciliation, not edited here

1. `MOVEMENT-002-CONTINUITY.md` §8 (Thrale): "(forty-four when she was made Master)". The prose has **forty-one since she
   was made Master, forty-four before** (16:247; 40:185). The ledger chain 44 → 41 → 40 → 36 given → 4 is right.
2. `MOVEMENT-005-CONTINUITY.md` §12 and `STATE_LEDGER.md` M5.9: Sedge is listed with "no collision". See W16.
3. `STATE_LEDGER.md` M5.7 and `MOVEMENT-005-CONTINUITY.md` §3 repeat Kellan's Hunt totals. Correct them with W2.
4. `MOVEMENT-004-CONTINUITY.md` §0 records "Orla held Hart's card 'a season'" as intended. See W9.
5. `STATE_LEDGER.md` M3.1, M4.1, M5.1 and M6.1 give the yes/no hour as "a quarter to seven" without saying morning or
   evening. Record the hour once W11 is settled.
6. The records number the Slack's crossings "the seventh" and "the eighth" (M6.1). They are the eighth and ninth crossings
   in Book Two; "seventh" is Aske's count from the hand-to-Ember series. The prose never numbers them, so nothing is wrong on
   the page, but a reader of the records should know where the count starts.

## 4. Checked and consistent

### 4.1 Calendar
- The month chain holds as the ledger gives it (first-month 1st a Friday; third-month 1st a Tuesday; the 30th of the third
  month a Wednesday; fourth-month 1st a Thursday). All **82** weekday-and-date pairs in the prose match it. The apparent
  misses are other months named in context: the Board's notice in ch. 2 (third month), the ferry Friday the 27th of the
  second month (17:243, 19:359), and the Reader's wax on Monday the 25th of the sixth month (38:263, 40:37).
- Eighty-one days dark (the 10th of the tenth month to the 1st of the first). Five weeks and six days to the relighting
  (4:9, the 20th of the eleventh). "Three months since" the 5th of the tenth (5:223). Eight weeks since the pump house and a
  month since a bank (4:127).
- The shed-door countdown: *44* on Sat 30th (first month); 44 minus the date through the second month (*43*; *31* → *30*
  on the 14th; "Nineteen", "Tomorrow's eighteen", "Sixteen"); then 14 minus the date at Saltmere ("Fourteen" Mon 30th,
  "Thirteen" Tue 1st, "Nought" Mon 14th). Forty-four days from the 30th of the first month to the Bench. Thirty days "at
  the outside" to the road (the road is on the 25th).
- Every interval phrase in the 130-line sweep checks against the calendar, except W6, W7, W17 and the idioms in §1.
  Examples: "Saturday week" (6:457 → the 30th); "since Thursday" (8:271); "a fortnight ago… the tram sheds" (15:73); "six
  days ago… by a kiln" (16:209); "three days off, a gate… on Tuesday" (16:407); "eleven days ago" (24:39); "The Monday of
  last week" (31:337); "eleven days off" (37:373); "six days ago" for Lyle (42:169); "three weeks ago" for the boat (42:359);
  "twelve days before" (46:259); "last Wednesday" (48:171); "the ninth day of no answer" (48:277).
- Travel: the coast boat sails from Meridian every Monday (8:88; the sheets and the copy go on Mondays). The road takes in
  Wed 25th, the Order Thu 26th, the ferry Fri 27th, the barge Fri–Sat, the coast boat from Sunday's first light, and
  Saltmere at four on Mon 30th. Graywater's van takes three days by the coast road. The station transit takes a day and a
  half (6:461; 17:157; 34:259; the Reader's "since eight o'clock yesterday morning", 38:263). Thrale leaves Wednesday and
  lands Saturday at 4.50. The Order's sister comes on Wednesday's boat, after Mara's wire of the 12th.

### 4.2 The team's ash book
- Every on-page "Held" figure matches its ledger: 9.33 (9:149); 9.05 (9:481); 8.81 (10:293); 8.59 (11:467); 7.83 (12:491);
  7.68 (13:83); 3.24 (13:501); 3.06 (13:505); 2.60 and 1.70 uncommitted (14:143, 14:373); 8.93 (15:519); 9.64 → 6.23,
  "ten and eighty-one… seven and forty", 5.63 uncommitted (16:33–41); 4.70 (23:287); 4.16 (24:271); 3.85 (25:323);
  3.50 (27:421); 6.26 (32:109); 5.15 (38:225); 5.15 at the handover (48:23).
- Movement One's sum is said aloud (8:155–167): 24.64 − 15.0 = 9.64; − 4.0 = 5.64; − 1.8 = 3.84. "Three drams and
  eighty-four hundredths" is repeated at 8:445 and 8:575. Floors: 0.32 (2:295) and 0.57 (6:407).
- I re-ran each movement's arithmetic: Two 9.64 − 10.81 + 7.40 = 6.23; Three 6.23 − 2.07 = 4.16; Four 4.16 − 1.05 + 3.15 =
  6.26; Five 6.26 − 1.11 = 5.15; Six, unchanged (the Board's ash).
- The sealed tin: 0.8 → 2.0 (the Order's 1.2, 16:255) → bound → combed at the gate, W full and I silent (17:249–259) →
  refused to Adlam (12 drams) and to the Committee (36:275) → opened for Loveday Hosken, 1.2 used, 0.8 left (46:73–75) →
  "Sealed 0.8, bound as before" (48:23).
- The Order's jars: 44 before Thrale was Master, 41 since, 40 after Seven's 1.2, 36 given, 4 left (16:247; 40:185–193).
  The prose is consistent; see §3.1 for the record.
- Shares: the moor hunt (15:513–519): 59.2 clean = 29.6 + 7.4 × 4. The Longshore: 12.6 clean = 6.30 + 3.15 + 3.15; 59.7
  combed (9.1 + 38.0 + 12.6); 47.1 red. The Slack: 286.4, all red, no share, no claim.
- Kellan's gate count (36:189): 1,106 = 1,102 + 4. His Hunt totals add up among themselves (412.4 = 371.3 + 41.1), but they
  conflict with the board: see W2.

### 4.3 Crossings

| # | Date | Kind; mast | Cost | Cold reached | Sulk; Aske |
|---|---|---|---|---|---|
| 1 | Thu 7th, first month | Ember → still; the Measure Hall's sanctioned mast, Noa | 0.30 (0.26 the gap), her thimble | to the wrist, "as in the summer" | "as before" (Fri 8th) |
| 2 | Sun 1st, second | hand → Ember; the Circuit's travelling mast, Noa, Orla | 0.31 | knuckle | warm by noon |
| 3 | Sun 8th | the same | 0.30 | wrist | warm at four |
| 4 | Sun 15th | the same | 0.31 | an inch above the wrist | warm Tue at seven; "a night" |
| 5 | Sun 22nd | the same | 0.30 | middle of the forearm | warm Wed 25th; "two nights" |
| 6 | Thu 3rd, third | hand → Ember; the Saltmere gate mast | 0.31 | a hand below the elbow | three nights; notch 7 s |
| 7 | Thu 10th | the same; **certified** | 0.30 | the elbow, with an ache | four nights; notch 6 s |
| 8 | Wed 23rd, 6.11.40 | Ember → still at the sill; the Board's lane mast, Noa, declared by Cade | the Board's ash | forecast cold folded into #9 | notch 5 s; inside the certificate |
| 9 | Wed 23rd, 6.14.50 | Ember → still at M3; against the card, the price said twice | the Board's ash | the hand gone to the wrist, not cold | three weeks; card **one in fourteen** (Thu 24th) |

- Spacing: 25, 7, 7, 7, 9, 7 and 13 days; the second in the hour is priced aloud (41:75–85 on Monday; 44:319 inside the
  ten-count). None of the other weeks' goes was spent (the 14th, 21st and 28th of the first month; the 17th–22nd of the
  third, kept on purpose at 33:71–79).
- The notch shortens on the coast, 7 → 6 → 5 seconds, against Meridian's 11, which only ever follows a second cliff.
- Certification: Orla's six, four in Meridian and two at the gate (14: the Chair's entry; 22, the signature). The
  commission repeats "Two crossings certified" (48:87).
- Three doors: three clean (a yard, the Pit, the Old Yard). There is no attempt in Book Two. The Proprietor asks twice
  (23; 43:89), and the letter to Crest is answered on the page (39:17). "Three times with three doors" (44:205). No fourth.

### 4.4 Injuries and bodies
- **Kiva.** Left hand: two fingers numb, three that report, eight that report across both hands (9:85, 14:17, 16:329, 19:345,
  24:361). Gone to the wrist from the 23rd; "Three weeks, I think"; the yes/no gives "no answer" for nine days. Right
  knuckles: burned Wed 16th, blisters Thursday, peeled Sunday, "pink and new" (43:277). The knee is strapped through
  Movement Two and silent afterwards. That is not a contradiction, but nothing marks the strapping coming off.
- **Perrin.** Two ribs sprung (Book One); strapping off the 20th of the eleventh month; the seventh rib on the left cracked
  Tue 15th; the card runs "A fortnight from Wednesday" to the 30th; he lifts against it twice and is stopped once.
- **Jude.** Left shin burned on the 2nd, limping into the Hunt. Left arm frosted on the 20th of the second month; sling;
  "out of the sling for lanes only"; Aske's card ("nothing gripped with the left till Monday"); out of the sling Mon 21st
  (42:229). Right knuckles white at the Slack. The limp is last seen on Wed 16th (30:191) and never closed. Not a
  contradiction.
- **Pru.** All ten fingertips (Wed 16th); two caps torn Thursday; fresh caps at 4.30 on Wednesday; two torn on the plank.
- **Pike.** Both hands taken above the wrists (23rd, first month); a band at each wrist (17th, second); dressings off and
  closing halfway (Fri 4th); two-thirds by summer.
- **Mara.** Reading hand starved (Book One), whole from the eleventh month, kept off every bank cell until case nineteen at
  about 6.30 on the 23rd.
- **Hart.** The right hand is the ruined one on every page; he writes left-handed; the watch is on the inside of the left
  wrist.
- **Dray.** Left leg, slight left limp; sticks two → one → none, except W7.
- **Anwen** is unhurt. **Kellan** is unhurt. **Lyle:** ward gone and stance kept, consistent through ch. 42–44. **Penhale**
  is dead, and nothing later contradicts it. **Bannock, Pettit, Bridie, Trewin, Loveday:** as their ledgers say.

### 4.5 Knowledge boundaries
- That Kiva dreams: Mara only (plus Ysra Crest's contentless note) until Thursday the 17th. There is no leak before that in
  any chapter (grep of "dream" through ch. 33: only 19:371, Orla "had not been told", and 23:19, Kiva's own memory). Then her
  four (Thu night), Aske, Orla and Kellan (Fri morning), and the Board (Fri night).
- The white lights: Kiva's alone until the Counting House on Sunday (39:221). The colour with no word: Kiva's alone to the
  end (39:261; 48:177). Annick's line has a colour too, and that is consistent with the bible's reserve.
- Hart's card: Orla alone until Mon 24th (tenth month), then Kiva and Mara. Orla's knowledge of the 2604 leaves is
  recorded at the Movement Five repair.
- The plate, the sealed pages and the Order's binding: shown or told on the page before anybody uses them.
- The exception is W12.

### 4.6 Facts that should not drift
- **Ages:** Kiva 17; Pike 54; Hart 40 ("He was forty", 19:403); the Proprietor 103 and "fifty-five by his face" (22:217,
  23:197, 39:127, 42:245, 45:331, 47:217); Carrow about 18; Bridie 15; Tamsin 16; Penhale about 30; his mother about 60.
- **Years:** the Proprietor 26 in 2604, his hand on the glass since 2611 (70 years); Annick's box taken about 80 years ago;
  the Reader since 2649; Thrale made Master 2670 and not past her gate in eleven years; the Step's counts 48 (2402),
  48 (2431), 49 (about 2550), 50 (2604), 52 (2650), 55 (ninth month 2680), 57.
- **Descriptors:** Dray's sunk grey eyes; Coombe's pale eyes; Thrale's grey eyes; Carrow's black hair and wind-brown face;
  Polglase's white cropped hair and steel spectacles; Penhale red-bearded; Yeo tall and grey-haired; the Reader's two pairs of
  spectacles. The exception is W15.
- **Pronouns:** the Clerk of the Measure, she, on every page (21, 23, 25, 26, 29, 36, 39, 40, 43); Ivey, she; Yarrow, he;
  Peverell, she; Polglase, he.
- **Ranks:** Orla and Rhea Torch; Coombe Blaze; Thrale and the Proprietor Glory; Kellan Fire; Kiva Flame on one door, with a
  Torch's wage and a Fire's wage named as wages only.
- **Colours:** Saltmere green; Graywater slate blue; Halden black and gold; the Tarn brown and buff; Holloway dark red;
  Westerley sea blue; the unpronounceable circuit grey with a white collar.
- **Saltmere geography:** the Mole a mile long; the sea gate ten feet up; 36 cells, 18 a side, six pumps; the staff 0–24 ft;
  the basin lag 23 minutes (19:203, 21:171, 26:181, 35:315, 36:245); the Graving 300 paces with the pen at the landward end
  (24:37, 40:25); the ring 50 paces from the dock mouth; M1, M2 and M3 at 25, 25 and 45 paces; the Inner Lock 24 feet and 22
  rungs.
- **The Hoop:** a hand high (26th of the ninth month); 4 ft 1 a fortnight back; 4 ft 6½ (8th and 9th); 4 ft 10½ (Tue 22nd,
  42:35); 4 ft 11 (Wed 23rd). Slack times: 6.12 and 6.13 (8th and 9th); 6.09 predicted; 6.08 found.
- **Doors** (except W4): Anwen hand; Perrin still; Jude and Gower Ember edge; Pru hand; Wace still; Hesketh and Edda ward;
  Marten "ward, catcher" (37:143).
- **Names** (except W16): the new Book Two names (Quiller, Polglase, Tolver, Treen, Wenna, Penhale, Bray, Trewin, Peverell,
  Hebden, Ivey, Tregear, Bannock, Hosken, Tamsin, Bolitho, Pascoe, Garside, Ottery, Coombe, Varley, Purvis, Hobday, Dilys,
  Dunnet, Carrow, Lyle, Thrale) do not occur in Book One's manuscript. Bettony is Book One's junior, consistent.

### 4.7 Book One locks (`OWNER_BRIEF.md`)
Held on the page: Kiva is 17, seated, unclassified and on the Home Line roll (and never called). The left arm and two fingers
are unhealed, and nothing silently restores them. Three clean, and no fourth. The disk is cold throughout ("Cold. Both. As
before."; "The disk is cold."). Kellan keeps the Halden yard and stays on Seven's book. Rhea's card is kept to six nights,
ends on the 30th, and both say no. The Ferren bank stays out; the seven drums go one a day and the last is out on the 24th.
Costs carry forward. Hart's card stays private until Orla chooses. The dream moves only by decisions on the page. Also
consistent: Orla's last sight of Hart (2:435 against 19:403: the infirmary, then the Wren House "not let in"); Hart's card text
(2:399 = Book One 48:319); Hart sponsored 2659, the Bench 2660.

Broken: W3, W4, W9, W10, W16, and W1 (against Book One ch. 24).

## 5. Items that need owner decisions

1. **W2:** the Hunt's totals. Restate Kellan's three figures, or the board, so that the clean yield adds up.
2. **W4:** Pettit's and Yarrow's doors, Book One against Book Two.
3. **W5:** Thrale's reach. Forty paces on the quay and at the Slack, the whole dock in the Graving.
4. **W11:** whether the yes/no hour is the morning's or the evening's, and whether the change at ch. 41 is marked.
5. **W16:** a new name for Twenty-Eight's Hold.
6. Not mine to settle, and already carried: Vane's absence and the call that never comes (§2.3); the revised caller line (§2.6).

## 6. Honest limits

- I read less than a tenth of the prose directly. The rest was checked by pattern search, so a contradiction worded in a way
  my searches did not anticipate can survive. For example: a fact restated in paraphrase, or a duration with no number in it.
- I relied on the movement ledgers for scene content I did not read. Where a ledger and the prose might disagree, I checked
  the prose only for the items listed above.
- Book One was consulted only at located points. Other Book One locks (rosters beyond Halden and Old Four, earlier sponsor
  history, the Pit's exact sequence) were not re-derived.
- W2's minimum clean figure uses the board's stated rule and the on-page marks. Places 4–5 and 7–11 rest on the Movement Four
  reconciliation, which is not on the page.
- I made no judgment of style, rhythm or formula targets, and proposed no rewrites beyond the smallest located edits.
- This is a same-model-family simulated review. It should not be described as human reader feedback or as independent testing.
