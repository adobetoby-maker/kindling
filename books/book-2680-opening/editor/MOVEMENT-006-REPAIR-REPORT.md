# Kindling 2680, Book One — Movement Six (chapters 41–48) — repair report

> Built by TAC

Date: 2026-10-12
Brief performed: `editor/MOVEMENT-006-REPAIR-BRIEF.md` (SHA-256 `0867b5d5733e1955951b1f0b90958d2896aa7a2a6e3d030023ca5dc59e8cf047`)
Repairing author: Claude Opus 5.5 (`claude-opus-5-5`), the model that wrote the first draft. One Claude Code session (`0deb8efc-acbf-419b-8426-ea8a81183e21`), new, not the drafting session and not either review session. No subagents, no workflow, no skill, no other model.

**Status: repaired, not rechecked.** This is one bounded same-author pass under the brief's three priorities. The author did not review, score or measure the result and did not reread the repaired chapters end to end. The only checks made afterward were mechanical: that each edit matched its target exactly once, that the protected passages are byte-identical, and that hashes and word counts are as reported. A separate targeted recheck is owed. Nothing was committed, pushed, published or narrated. Book Two was not started. Neither review report, no prompt file and no packet was altered.

---

## 1. What was read

In full, before the first edit: the repair brief; `editor/MOVEMENT-006-EDITORIAL.md` (SHA-256 as read `c0100a9e6478a551455eb528acadf4557c2d83fd4c763034fb591e12c10d5398`, all 777 lines); `editor/MOVEMENT-006-COLD-READ.md` (SHA-256 `0974adb5b333bbfdf65b50ddf240ad1e96ca7ab8624daa0e7b308a735e714dc6`); chapters 41–48; `provenance/MOVEMENT-006-CONTINUITY.md`; lines 1–125 and the Movement Six block of `STATE_LEDGER.md`; and the Movement Six section of `AUTHORSHIP.md`.

The eight working chapters were byte-identical to the eight frozen files (`cmp`, all eight) before the first edit, so one reading covered both, and the editorial review's `chapter:line` citations applied directly.

By search and line lookup only, to settle a fact before changing it:

| Question | Where it was checked | Result |
|---|---|---|
| Was Perrin withdrawn for his hands or his ribs? | chapter 14 (39, 164), chapter 15 (173–177), Movement Two checkpoint | Ribs. The 4th of the fifth month is right. |
| When does Noa's page of notches begin? | chapter 26 (121–125), chapter 40 (101) | The sixth month. "Six months" was wrong; "since the sixth month" was right. |
| How long has Halden had its contained string? | chapter 32 (79–83), chapter 34 (199, 207) | A six-knot string was there in the sixth month, and Pettit has cut "a rung a week since the thaw." |
| What may Kiva know about the date of Annick's page? | chapter 25 (223), chapter 31 (311–313), the Movement Four ledger block | The page is undated on the page ("for a date. There was none"). |
| Is Hesketh a ward or a corner-hand? | chapters 37–39 | Halden's ward. Consistent; see section 5. |
| Is "in the Pit, in the spring" a different event from the Pit of the ninth month? | chapter 23 (397, 525) | Yes: the Flask of the 29th of the fifth month, when the string "took the bus." Consistent; see section 5. |
| What does the book call the post's lean? | all chapters, by search | "To the left" appears only at 42:107, 42:469 and 48:477. |
| What are the first book's seven columns? | prologue (283–285) | A different document with its own headings; not touched. |

**Read late, and disclosed as such.** `BOOK_MAP.md`, `UNIVERSE_BIBLE.md` and the Movement Three to Five blocks of `STATE_LEDGER.md` were read in full only after the 100 edits had been applied, while this report was being checked. Before that, only their headings and the lines found by the searches above had been seen, and the reviews' canon findings stood in for them. Read in full, they contradicted none of the edits and prompted one correction to a clause the repair had just written (section 3). Not read: chapters 1–40 beyond the lines above.

## 2. Frozen edition

`editions/movement-006-pre-repair/` was verified against its `SHA256SUMS.txt` before the first edit, after the 100 edits, after the three later adjustments, after the records were reconciled, and after the authorship entry and this report were written. All eight files were OK each time. It was not modified.

## 3. Files changed

| File | What changed |
|---|---|
| `manuscript/chapter-41.md` … `chapter-48.md` | 100 targeted in-place edits (13, 10, 8, 7, 12, 11, 25, 14). Each was an exact-string replacement that aborts unless it matches once. No chapter was rewritten whole. No scene, section break or viewpoint was added, cut or moved; the movement still has 44 sections. Three of the 100 were adjusted once more before the pass closed, at the same places: the ward-trace clause (46:567), reworded after `STATE_LEDGER.md` and chapter 14 were checked for what "plain" means; and the two compactions (47:259, 48:237), which had come out longer than what they replaced and were cut down. These are part of the one repair, not a second. |
| `provenance/MOVEMENT-006-CONTINUITY.md` | 22 edits, and one later correction to the word count in item 19. A new section 0 lists them; the status line and sections 1, 2, 4, 5, 6, 7, 9 and 11 were corrected only where the repaired prose made a line false. |
| `STATE_LEDGER.md` | 5 edits, all inside the Movement Six block (line 394 onward). |
| `AUTHORSHIP.md` | One appended section, "Movement Six consolidated repair." Nothing above it was changed. |
| `editor/MOVEMENT-006-REPAIR-REPORT.md` | This file. |

Not touched: the frozen edition, chapters 1–40, the prologue, the packet, the compiled prompts, the brief, both reviews, `BOOK_MAP.md`, `UNIVERSE_BIBLE.md`, and the records of Movements One to Five.

## 4. Resolved findings and their new locations

Locations are `chapter:line` in the repaired files, with the chapter heading as line 1. "C" numbers are the editorial review's table 3b; "cold" numbers are the cold read's table of apparent inconsistencies.

### Priority 1 — the mechanism on one pass

| Finding | New location | What the page now says |
|---|---|---|
| One growth rule for the string (C7, cold 13) | 45:137; 45:269 | Brask: it would come up without her, at the drain's own pace, until it ran out of road; every cut only lets the next one out at once; she is "hurrying it up your hill." Then: nobody cut it again, and it came all the same, only slower. Rhea's stop now has a cause: cutting gains nothing and drives the head toward the School faster. |
| Cross dug under two days ago, not four (C1) | 46:201 | "The best part of two days." |
| Kellan's seventh month against Birch's eighth (C4, cold 7) | 43:5 | Birch has had the string "since the thaw." Kellan's "since the seventh month" stands. |
| Rusk's four hours against half an hour (C5, cold 5) | 41:301; 43:45 | Four hours is one crew, a cell at a time, by the book. Half an hour is every hand at once, one to a cell. |
| Mara's arrival, hands, trial and comparison (C6) | 45:11; 45:19; 45:401 | All of her forty "but the night shift" are in bed; a dozen of the night shift are on the pump-house floor already and she must find the other dozen; the slip compares the water with "twenty past eleven, when I came in and chalked it." |
| "Halfway down" (C8) | 44:353 | "Near the top of it, not forty paces below her." |
| The drill: how a litter meets the post (C10) | 42:249–251; 42:271 | Pettit means to run along the lane side of the south row. The leaning post is the last of that row counted from the sheds and the first met from the gap, eight paces in. Brask: "Wace, a pace right." |
| North-row numbering (C16, cold 2) | 45:359; 46:37 | "The eighth post, the last of the north row," both times. Dray is put down beside Kiva at that post. |
| Which way the post leans (cold 3) | 42:107; 42:469 | It leans into the lane: "to the left, if one stood at the sheds and looked along the row." At the second mention, "out over the lane." The last paragraph's "to the left," seen from the first shed, is unchanged. |
| Where the gate lies from the post, before the step test | 46:141 | "To the east of the post, where the black gate lay beyond the gap." |
| Whose count is running (C11, cold 4) | 46:233–235 | One labelling sentence after the declaration: the go's count is hers; the fours are the arm's, and Dray's. |
| Planned, performed and reported hand-off (C11, cold 4) | 46:21; 46:299; 46:301 | Planned: "After six, it goes to somebody." Performed: she counts on from her own six, *Seven. Eight. Nine,* and says "Wace" between nine and ten. Reported: Dray's "at nine," Vane's "after six" and the proof's "after six" are unchanged and now agree. |
| A knot is "the seventh knot," never "Seven" | 45:81–83; 45:91; 45:109; 45:269; 45:279; 46:119 | The first, the eighth, the seventh, the tenth, the eleventh, the twelfth. Pike: "Finch has hers under the eleventh knot." |
| Six hundred households against sixty-two houses (C9, cold 1) | 41:471; 42:25; 42:211; 43:535; 47:237 | The six hundred are "the streets that the two drums fed," most of them behind and to either side of the hill, "with roads of their own." The hill itself has sixty-two houses. |
| Why the shelf's plain ash cannot feed a hand (cold 12) | 46:567 | The shelf's pinches "were plain of everything, ward and all, and a hand can't feed on that." |
| How the remaining houses leave once the gate is taken (cold 14) | 45:279–285; 45:341; 47:245 | Vane orders what is left of the top down by the curb, behind the porch, boxes dark. Perrin's empty litter was for "a next house that was by now going down the hill instead." The slate records it. |
| Four figures in the year, not five (C14, cold 6) | 41:457 | "That's four." |
| "Three hands" against two reporting (cold 9) | 47:165 | "We've two hands between us that report… I make it two and a bit." "I've got the bit" stands (the arm above the white). |
| Elapsed hours (C13, cold 10) | 47:81 | "Not eight hours before." |
| The plank under the first or the tenth knot (C12, cold 8) | 48:251 | Jude: "two knots down the hill from mine." His was the tenth; that is the first, as the slate has it. |
| Wire slip called "my mother's hand" (cold 15) | 47:41 | "That's my mother." |
| Six at the table, five named (cold 18) | 41:319 | Five at the table, and a sixth who would not sit. |
| Perrin's injury at the exhibition (editorial 3c) | 41:401 | "I'd my ribs in linen." Checked against chapters 14 and 15. |

### Priority 2 — the closing record and the cost

| Finding | New location | What the page now says |
|---|---|---|
| Seven headings settled (C2) | 43:463; 43:497–499 | The manual's first column is "only the lane's name, and where it lay"; then *What, How, Went wrong, Cost, Second try,* and the *Why.* The Line's sheet now reads a sixth line, *Second try: called it, and said which two. Shut in nine turns.* |
| The collarbone under the right heading; the exchange follows the sheet (C2) | 48:369; 48:373; 48:389 | Kiva writes in the fourth, under *Went wrong.* "She passed over the fifth, where the collarbone was." Then the sixth. Orla's "You've not put what it cost" now follows from what was skipped, and her message to the bursar is "a hand in two of his columns." |
| Noa's scene out of order, arm unseen (C3, cold 11) | 47:387; 47:391; 47:425 | The scene opens "before the sling came off. It was Saturday the 8th, two days after the slate was read." Kiva reaches to hold the sheet's corner and the arm "only stirred in its sling." On the 8th Mara has only begun her sheets; the eleven are for the 15th. |
| Crate and first shed (C15) | 48:365; 48:393 | Orla makes room and the proof is laid on the crate beside her. Kiva goes down the lane to the juniors at the fourth post, so that "walked back along the lane to the first shed" (unchanged) is now true. |
| One-unit date slips (C13) | 41:401; 46:615; 47:435; 48:251 | Perrin "five months"; Noa "four months" and "a four-month mistake"; Jude "the week before last." |
| The shared dream in front of bystanders (K1) | 47:177–179; 47:213–217; 47:225 | Mara waits until Lumb has gone back to his sump and Aske and Kellan's mother have taken the tin to the door lamp; Adlam is at the far end of the needles, "out of hearing of the desk"; she keeps her voice under the pumps. Lumb comes back for his book and is told only that the keeper's page is to be kept, which gives him his line. |
| Exact date for Annick's page | 47:197; 47:203 | "Long before this. The page had no date." Mara: "They're lifetimes apart." |
| Four days without the arm (plan adherence, 3e) | 47:293–301 | Four short paragraphs before "The elbow came back on Friday": bread, a boot, the coat over the sling, the arm's weight against doorposts, waking on it, and the brass weight in place of Pru's finger. The return, the two fingers, Mara's hand and the reserve are unchanged. |
| The pot's arithmetic (cold repair 2) | 47:259–261 | Reported in narration: the Line's way, in the Pit's own parts, half of it into the hill's boxes and the Hythe's that night. Kept in speech: nine drams to a team, and the Halden four drawing the same as Twenty-Eight. Five amounts were spoken before; one is now. |
| The old team-book entries read again (cold repair 2) | 48:235–241 | Reported in one sentence of narration: seven-tenths of the call drams spent, Anwen's forty-one hundredths the most and Kiva's none; the three-door line; the loan come home. Kept in speech: the new credit, Jude's 7.8, and "Held: 26.53… That adds." Jude's dram and the 25.53 follow unchanged. |

### Priority 3 — voices and listening

Thirty-nine single-line touches in all.

| Finding | New location | Change |
|---|---|---|
| Perrin's phrase thinned before the climax | 41:331; 42:325; 44:313 | Three uses reworded. Kept: 41:465, 44:151, 45:233, the exchange at 46:205–211 and the payoff at 46:389. |
| Perrin's phrase after the payoff | 47:63; 48:253 | Two reworded. Kept: "I'd like it noted that I minded properly, and at length" (48:279). |
| The phrase in other mouths | 41:333 (Anwen); 41:371 (Kiva); 42:17 (Aske); 43:241 (the fitter); 44:65 (Vane); 47:389 (Noa) | Reworded or cut. Perrin's "It's noted" in reply to the fitter stands. Kiva's "I'd like that written" at 46:105 stands. |
| "I find that" left to Mara | 43:535 and 46:429 (Rusk); 47:231 (Adlam) | Reworded. |
| Optional "that" in young or plain speech | 41:461; 42:61; 42:353; 43:49; 44:137; 47:63; 47:67; 47:77; 47:275; 48:131; 48:197; 48:205; 48:241; 48:263 | Dropped. |
| A house number colliding with a seal count (cold lens A) | 45:169 | The warden's call begins at fifty-four, so "fifty-two" is only Pike's count. |
| Choppy narration joined, chapters 41, 44, 47, 48 only | 41:125; 41:151; 41:237; 44:157; 44:237; 44:331; 47:17; 47:135; 47:267; 48:185; 48:269 | Eleven joins. No speech was lengthened. No narration in chapters 45 or 46 was joined. |

### Protected passages

Checked mechanically after the edits:

- Chapter 48 from the junior's "Miss Dane says that we're to run it" (frozen line 393) to the end is byte-identical to the frozen edition. That covers the juniors' run and the last two paragraphs.
- Orla's cutaway and Hart's card (chapter 48, "Orla Dane had moved her crate" to "She put the card away") is byte-identical.
- Pru's finger, the keeper's book entry, the cast and its label, the plate, Dray's third line, Jude's dram and every protected line named in the editorial review's three "Preserve" lists were not edited, with the two exceptions in section 6, items 5 and 6.

## 5. Findings left unchanged, and why

| Finding | Why it stands |
|---|---|
| Forty gratings at twenty paces against sixty-two houses (the tail of C9) | The brief asks only that the two household figures be reconciled. Making an 800-pace hill fit sixty-two houses would mean new facts about the street. |
| Hesketh hauls a corner, then stands a ward (cold 16) | Not a conflict. She is Halden's ward (chapters 37–39) and hauls a corner for her own catcher in Halden's yard. |
| "In the Pit, in the spring" (cold 17) | Not a conflict. It is the Flask of the 29th of the fifth month, the same event as Rhea's "on the bus, in the fifth month." |
| "It isn't hers to have offered" has two possible owners (cold lens B) | The line is quoted back word for word at 44:189 and in two records. Left for the owner. |
| "The Ferren" as a person beside the Ferren main (cold lens B) | A seat name since chapter 33. The sentence at 47:383 marks her as a person ("she wants to say it herself, and at seventy she's entitled"). |
| Rhea's "I find that I've a column for the other" (46:67) | Inside the consent sequence. |
| Dray's "I find that I mind that a good deal more" (44:271) | Dray's lines are protected entire. |
| The junior's four optional "that"s (48:395) | The editorial review offers this line as an example, and it also begins the final scene that the review protects. The scene was kept byte-identical. |
| "I'd sooner" and "I'd as soon," fourteen uses | Counted by the review; not named in the brief. |
| The hearing room's length, the cork readings given twice, the chapter 41 kitchen read-out | Not in the brief. Priority 2 is limited to chapters 47 and 48. |
| The dream joined to a T-0 night (K2) | The review flags it as matching the book map's ending promise. No change was asked. |
| The witness's rank; the string's name and yield class; a street cutaway for the release; the Reader, not Orla and Noa, recognizing the plate | Owner decisions, listed as such by the editorial review. |
| The formula's sentence, reading-level and reporting-verb targets | The brief says not to chase them. Nothing was measured. |

Three things noticed while repairing that neither review located. None was changed.

- The master says "I've cut that line four times since the thaw" (41:451) as he kneels to cut the fourth. It reads if today's is counted.
- The spindle's rake. The post leans over the lid on its lane side, and the fitter says the lean is "on the rake of the screw" to a gate "a pace to one side" (44:33). A straight rod running down toward a gate on the lane side would lean the other way above ground. A recheck may want to look.
- "Five paces from the shaft" for Dray's post (46:37) is unchanged. The north row may be farther than that from the lid.

## 6. Choices in this repair that the owner should review

1. **A line was added to a canon document.** The Line's lane sheet now has a *Second try* line (43:497), so that its seven ruled columns are seven on the page. The checkpoint's quotation of the sheet was updated to match.
2. **Vane gives a new spoken order** (45:281), and his slate has a new clause (47:245). The route is down the hill by the curb behind Mace's walking wall. The page does not say how many houses went that way.
3. **A night shift of a dozen** is on the pump-house floor when Mara arrives (45:19). The nineteen hands of her slip are then a dozen and seven fetched; the slip itself says only nineteen.
4. **Kiva and Selka Dray are at the same post** during the consent sequence: the eighth, the last of the north row.
5. **"Three hands" became "two."** The editorial review lists "We've three hands between us that report" under Preserve; the brief directs the count to be corrected. The brief was followed.
6. **Two edits fall inside the consent sequence** that the editorial review asks to keep word for word: "On six" became "After six" (46:21), and the phrase naming Dray's post (46:37). Both are named in the brief. Nothing else from 45:419 to 46:109 was touched.
7. **K1 was settled by earshot,** not by having somebody be seen to hear. The four bystanders still do not know that Kiva has dreamed. Lumb's and Adlam's lines are kept by having each come back to the desk afterward.
8. **Figures taken off the page.** Cade's 0.14, Talley's 0.09 and Renn's 0.06 of the call drams, and the pot's 24, 36 and 36, are no longer spoken. The totals and the decisive figures remain, and the checkpoint marks which figures now rest on the frozen first draft.
9. **The four days are new prose,** about 230 words, inside the existing section. The repair added 804 words to the movement in all; 461 of them are in chapter 47.
10. **Birch's "since the thaw"** was chosen over "since the seventh month" because chapters 32 and 34 already put a contained string in that yard before Kellan came.

## 7. Word counts and hashes

Word counts are `wc -w`. "Before" is the frozen edition, which was identical to the working files when the session began.

| File | Words before | Words after | Change |
|---|---:|---:|---:|
| `manuscript/chapter-41.md` | 7,250 | 7,264 | +14 |
| `manuscript/chapter-42.md` | 6,408 | 6,479 | +71 |
| `manuscript/chapter-43.md` | 6,853 | 6,882 | +29 |
| `manuscript/chapter-44.md` | 5,572 | 5,574 | +2 |
| `manuscript/chapter-45.md` | 5,147 | 5,297 | +150 |
| `manuscript/chapter-46.md` | 7,175 | 7,238 | +63 |
| `manuscript/chapter-47.md` | 5,907 | 6,368 | +461 |
| `manuscript/chapter-48.md` | 6,554 | 6,568 | +14 |
| **Movement Six total** | **50,866** | **51,670** | **+804** |

Nothing was cut for length. The two compactions are lighter by figures, not by much length: the pot passage went from 96 words to 87, and the team-book passage from 139 to 137.

| File | SHA-256 before | SHA-256 after |
|---|---|---|
| `chapter-41.md` | `5f8cb0aacec4f9f62e6d92b21cd641eddda2bbb3741547df045dd8da17001b1e` | `b10b2d3e31db1be3cd2ddbc1c0fc6564ba6cd425eaec6c73f5f4c1d023998711` |
| `chapter-42.md` | `60cd5291f62137f77d94e668bb297ba847a8b852a35807367d6121a1c82d3a80` | `2f6dbe93302800436b50dc0439a152a443507598fc921ff931dbc4ce0dd4ff62` |
| `chapter-43.md` | `3ab68ff5e796349b64b641506734e6c28873b6f61586a171e29fad7ab6200cb7` | `4426364475e9390931faf1052a4994b13788ba2a5a89e0fd73d0d951ce21822c` |
| `chapter-44.md` | `e0ef75033f437348d3b3e11c1873aa15c6a3cf170f7f1010a48fad43fa9c64c4` | `24c2ce49d249d540c961250515ebf5cc644feb48cd72c93211a779a42693bab7` |
| `chapter-45.md` | `45209fc0e4abd57d83552fafaebfa685f96a148c40a7aa49614084276cfc0cf4` | `adf79c56ac28e1fa734c92f4ed54bf26e5f56404dd69e61abb8d4c847b9339ff` |
| `chapter-46.md` | `7f154f83eeaf430b98fca1c2e49e4838b9d2fca0211fb967b9aeff96c72a34ed` | `74101cd043c4f9cd04a4a8cdca505bfdcf7176be37ecd5f22d005c0dc179e5a4` |
| `chapter-47.md` | `335e89f86a309ad3966ec5b5b0d9c52f1b5fcab272e2fe74e0c12b7ea1c062b9` | `b649b15974082cbb31992cefe248597a8a7b90d70db74e76be290dbb400fb860` |
| `chapter-48.md` | `7902237b16c8dc5f882acac6cfe990abda96faff38f24958abfd3f7520753b39` | `86f180322194764f30808d8d9827fe39f80da547fcd202c7165f689c24333b4f` |

Records after reconciliation: `provenance/MOVEMENT-006-CONTINUITY.md`, SHA-256 `60ddf404562ef0cbb7d05f9c6d618209f61275b0284dd1c02dc06c0cd02cd208`. `STATE_LEDGER.md` and `AUTHORSHIP.md` are not hashed here, since the authorship entry was written after this table.

## 8. Confirmation

The frozen edition `editions/movement-006-pre-repair/` was not changed. Its eight chapter files match `SHA256SUMS.txt` and the "before" column above.

## 9. What is owed

A separate targeted recheck of the three priorities against the frozen edition, by a session that did not make these edits. Until then the movement is repaired and unverified. Chapters 43–48 as committed and published by the other process were already behind the working tree before this repair; all eight chapters are now ahead of anything committed.

---

## 10. Post-recheck correction note — 2026-10-12

Added after `editor/MOVEMENT-006-TARGETED-RECHECK.md` (SHA-256 `e1bf8aa4213e74568d77987966dc06c132a790f3259430f00da1fa22c66c47b7`) passed all three priorities with three required corrections. Sections 1 to 9 above are left as written; where they disagree with this note, this note governs. Applied by the repairing author in the same session, resumed. Only R1, R2 and R3 were applied. None of the optional notes (O1 to O8) or the optional record notes was acted on. This is not a second repair pass, and the result was not reviewed, scored or rechecked again.

| | File and line | Before | After |
|---|---|---|---|
| R1 | `manuscript/chapter-44.md`:17 | "And across the shaft, a foot above the water," | "And across the wall side of the shaft, back under the post, a foot above the water," |
| R1 | `manuscript/chapter-44.md`:33 | "and a pace to one side." | "and a pace back toward the wall." |
| R2 | `manuscript/chapter-48.md`:251 | "I asked the week before last what ash was for," | "I asked last week what ash was for," |
| R3 | `provenance/MOVEMENT-006-CONTINUITY.md`, section 2 (Noa Bexley) | "the six-month mistake" | "the four-month mistake" |

R2 restores the frozen first draft's wording. The repair had changed it on the editorial review's item C13, and the recheck showed the original was right. So in section 4 of this report, the "One-unit date slips" row no longer includes Jude's line; the Perrin and Noa corrections in that row stand. The row for the plank at 48:251 ("two knots down the hill from mine") is unaffected. Section 5's third note under "three things noticed" (the spindle's rake) is now resolved by R1.

Record lines made stale by these changes and brought into line, all in `provenance/MOVEMENT-006-CONTINUITY.md`: the sluice entry in section 7 (R1); the word count in section 9, item 19; and section 0, which now carries a short post-recheck paragraph. `STATE_LEDGER.md` was not changed: its line on the post ("a penstock in a brick shaft eight feet down, on a raked screw inside the post") is still true. The "not rechecked" status lines in the checkpoint, the ledger and the authorship entry were left for the acceptance entry, as the recheck says.

Changed files in this correction: `manuscript/chapter-44.md`, `manuscript/chapter-48.md`, `provenance/MOVEMENT-006-CONTINUITY.md`, `AUTHORSHIP.md` (one appended note) and this report (this section). Nothing else.

| File | Words after repair | Words now | SHA-256 now |
|---|---:|---:|---|
| `manuscript/chapter-44.md` | 5,574 | 5,583 | `0503075fb6cc278f86a93665542f8b358a82f5aafc8979456d48855427389010` |
| `manuscript/chapter-48.md` | 6,568 | 6,566 | `b1b5835358b0fc77a1eb5d3567feadae5dcc5d1e24e19aea48f538ebd228d27b` |
| **Movement Six total** | **51,670** | **51,677** | (50,866 in the first draft; +811) |
| `provenance/MOVEMENT-006-CONTINUITY.md` | | | `760c9bd1947ffbe691a099822e443380e7f838e68bd6fd948b0e0f1511deff6d` |

Chapters 41, 42, 43, 45, 46 and 47 are unchanged from the hashes in section 7. `STATE_LEDGER.md` is unchanged (`26db4775805b0c381136bdcabae7986d566ce9b81f7b20eebce1c5a77a89b97a`).

Checked mechanically after the three corrections: the frozen edition matches its `SHA256SUMS.txt` (all eight OK); chapter 48 from "Miss Dane says that we're to run it" to the end is byte-identical to the frozen file, as is Orla's cutaway with Hart's card; each replacement matched exactly once. Nothing was committed, pushed, published or narrated.
