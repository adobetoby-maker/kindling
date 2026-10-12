# Kindling 2680, Book One — Movement Six (chapters 41–48) — targeted recheck

> Built by TAC

Rechecked 2026-10-12 by Claude Opus 5.5 (`claude-opus-5-5`) from `editor/MOVEMENT-006-TARGETED-RECHECK.prompt.md` (SHA-256 `5dfc701d17667d0a78a0d6b353afe0daef355339f06d8f6e1e9db0f48764d7f3`). Review only. This file is the only thing written in the repository.

## Verdict

| Priority | Verdict | Owed |
|---|---|---|
| 1. Mechanism, map, counts, time, causal handholds | **PASS** | R1, a contradiction in the spindle's geometry. It is in the frozen draft and was not caused by the repair. |
| 2. Closing record, chronology, knowledge, cost | **PASS** | R2, a date phrase the repair made wrong. R3, one stale record line. |
| 3. Voice, listening clarity, protected material | **PASS** | Nothing. |

The repair did what the brief asked. With one exception (R2), every finding the report claims as resolved is resolved on the page at the line it cites, and the protected passages are byte-identical. Three corrections are owed: two in prose (three phrases in all) and one record line. None needs a second repair pass. Until they are applied the movement is rechecked with corrections owed, not closed.

Citations are `chapter:line` in the current `manuscript/` files, with the heading as line 1.

## 0. What this is, and its limits

- **Kind of read.** A same-model targeted recheck in a new session (Claude Code session `12e22edd-c1ec-4ca7-9da2-f9a57349a8a4`, begun 02:12 MDT). Opus 5.5 also wrote and repaired these chapters, so this is not independent, not blind, and not a human read. It is not a second editorial pass: I tested the three priorities, the joins their edits made, and the three spatial lines the prompt names.
- **Read in full.** The brief, both reviews, the repair report, current chapters 41–48, the continuity checkpoint, the Movement Six block of `STATE_LEDGER.md` (lines 394–509), and the Movement Six draft and repair entries of `AUTHORSHIP.md` (lines 1425–1742).
- **The frozen edition.** I verified its eight hashes, then read a complete `diff` of each frozen chapter against its current file (105 changed regions). Every frozen line that differs was read beside its replacement. Lines outside the diff are identical to the current text, which I read whole.
- **Also consulted, by line lookup only.** `UNIVERSE_BIBLE.md` lines 92–120 and `BOOK_MAP.md` lines 10–27 and 59, for what Book Two reserves. Not opened: chapters 1–40. Perrin's ribs, Noa's sixth month and Annick's undated page therefore rest on the report's lookups, not mine.
- **Disclosed.** Session start-up and a file-read hook injected project memory: a stale Movement One handoff, one-line notes that this movement was drafted and repaired, and titles of earlier observations. None was used as evidence, and no memory tool was called. I looked at the first twelve lines of the Movement Five recheck for its header layout only. No subagent, skill or other model was used. Scratch diffs were written to `/tmp/m006-recheck.MnOksZ`, outside the repository, and left there.

## 1. Mechanical verification

| Check | Result |
|---|---|
| Frozen edition against its `SHA256SUMS.txt` | All eight OK. The hashes equal the report's "before" column. `HEAD` (`7877842`) holds the same eight texts, so the whole repair is uncommitted. |
| Current chapter hashes | All eight equal the report's "after" column and the authorship entry's post-repair table. |
| Word counts (`wc -w`) | 50,866 before and 51,670 after, +804. By chapter: +14, +71, +29, +2, +150, +63, +461, +14, as reported. |
| Changed-file list | `git status` shows the eight chapters, the continuity checkpoint, `STATE_LEDGER.md` and `AUTHORSHIP.md` modified, and the brief, report and recheck prompt untracked. Nothing else. |
| Reviews and brief unaltered | The editorial review, cold read and brief hash to the values the report says it read. |
| `STATE_LEDGER.md` | Five changed regions, all between lines 396 and 477, inside the Movement Six block. |
| `AUTHORSHIP.md` | One appended block of 138 lines. No earlier line removed or changed. |
| Continuity checkpoint | 20 changed regions. Its hash equals the one the report and authorship entry record. |
| Report hash in the authorship entry | Matches the report as it stands. |
| Sections | 44 before and 44 after. No scene, break or viewpoint added or moved. |
| Passage sizes the report claims | Four days: 230 words. Pot: 96 to 87. Team book: 139 to 137. All confirmed. |
| Edit count | The diff shows 105 changed regions and 111 changed or added lines. That fits "100 edits," since several span or share a line. A diff cannot re-derive the figure itself. |

**Passages claimed byte-identical.** Both confirmed by hashing the two ranges:

- Chapter 48 from the junior's "Miss Dane says that we're to run it" to the end (frozen line 393, current line 395). This covers the juniors' run and the last two paragraphs.
- Orla's cutaway and Hart's card, "Orla Dane had moved her crate" to "She put the card away" (frozen 301–335, current 303–337).

I also checked the consent sequence. Chapter 45 from "I'd like to say what it costs" to its end is byte-identical. Chapter 46 lines 1–109 differ in exactly two places, 46:21 and 46:37, both named in the brief and disclosed in the report.

## 2. Priority 1 — mechanism, map, counts, time: PASS

### 2a. The layout, from the surviving prose only

- **Stopgate.** A straight hill from the Brickfields road up to the School's bottom wall, a tram line up the crown, a grating between the rails every twenty paces (41:151, 44:329, 45:273). Sixty-two houses stand on the hill itself: the bottom forty and the top twenty-two (42:211–213).
- **Drums and knots.** Eight knots rise eight paces apart, the first at the rail of twenty-nine and the eighth at twenty-eight (45:83). The eighth and seventh are cut. The ninth and tenth rise on those cuts, at 8 and 16 paces above twenty-nine. The eleventh rises uncut at the last grating and the twelfth in the gateway (45:115–127, 45:269–279). That puts the top of the first seam 32 paces below the gate, which agrees with "not forty paces below her" (44:353). Ten stand, over "seventy paces" (45:371).
- **The bottom yard.** Thirty paces square. The black gate is in the middle of its south wall, the core house on the east, a low wall with a gap on the west (42:55–67).
- **The Old Yard.** Beyond the gap, a strip under the bottom wall running west to the sheds, forty paces (42:91). The south row stands a yard out from the brick. Posts are counted through the lane from the sheds: the sheet says "run it dark, from the sheds" and "call the turn before the eighth" (43:491). The ninth is the last of the south row, eight paces in from the gap, a pace out of its row. The eighth is the last of the north row.
- **The sluice.** The lid lies at the foot of the leaning post on its lane side (44:9, 45:361, 46:135). The shaft is eight feet deep, with the gate hanging in it (44:17).
- **The main.** It comes in under the black gate, runs west under the wall to the post, and goes on west under the south row. A small mouth joins from the core house to the north-east (42:441–449, 44:69, 46:167).
- **Roads.** The casualty road runs gate, yard, gap, lane, side gate at the sheds (42:213). Once the twelfth knot takes the gate, what is left of the top goes down by the east curb behind Mace's walking wall (45:281).
- **Halden yard and pump house.** No repair edit touches either layout, and both hold as drafted (43:7–19, 43:57, 43:111; 46:431–443).

### 2b. What the prompt asked me to verify

| Item | Where | Finding |
|---|---|---|
| One growth rule; Rhea's stop | 45:129–145, 45:269 | Holds. The string pays out at the drain's pace whether or not it is cut, and a cut lets the next knot out at once. Stopping is sound on both counts: after two cuts there are still eight, and each cut hurries the head toward the School. |
| Seventh and eighth month | 43:5, 43:103 | Holds. Birch "since the thaw," Kellan "since the seventh month." |
| Cross age | 44:3, 46:201 | Holds. Tuesday at nine to Wednesday near midnight is about 39 hours: "the best part of two days." |
| Rusk's four hours and half hour | 41:301, 43:45 | Holds. One crew a cell at a time by the book, against every hand at once, one to a cell. Done on the night in 26 minutes by 24 hands. |
| Mara's travel, night shift and trial | 45:11–19, 45:401, 46:425 | Holds. She leaves about 11:05 and is in at 11:20. A dozen night shift plus seven fetched is the slip's nineteen at 11:42, and five students at 11:54 make 24. The trial compares the water with her own 11:20 chalk mark. |
| Elapsed-time corrections | 41:401, 46:615, 47:435, 47:81, 48:251 | Four of five hold: "five months," "four months" twice, and "not eight hours" (7 h 40). **48:251 does not. See R2.** |
| Which way the post leans | 42:107, 42:469, 48:479 | Holds. From the sheds, looking along the row, the wall is on the right and the lane on the left. The unchanged last paragraph is seen from the same end. |
| Row numbering | 45:359, 46:37, 48:393, 48:407 | Holds, read as one count of nine through both rows. No "first post of the north row" survives. |
| Drill collision | 42:249–251, 42:271, 42:311 | Holds. Going in from the gap the post is on the left and a pace out, so Brask's "a pace right" now agrees with "Post, left. Keep right." |
| Gate-to-post relation | 46:141 | Holds. East of the post, beyond the gap, agreeing with 42:55–67. |
| "Halfway down" | 44:353 | Holds, as in 2a. |
| Step-test anchors | 46:143–175 | Hold. East is the main under the wall. North of the lid is clean. The step test itself is unchanged. |
| Catch counts and hand-off | 46:21, 46:83, 46:231–233, 46:291–301, 46:625, 48:375 | Hold. Planned "after six" (Kiva, Vane's direction, the proof). Performed on from her own six to "between nine and ten." Reported "at nine" (Dray). One sentence at 46:233 says whose count is whose. The two edits inside the consent sequence change no other count. |
| 600 households and 62 houses | 41:257, 41:285, 41:471, 42:25, 42:211, 42:347, 43:535, 44:95, 47:237, 47:245 | Holds at every occurrence. The six hundred are the streets the two dry drums feed. The hill has sixty-two houses. |
| Wren ash against ward-trace | 44:99–119, 44:131, 46:567, 47:55, 48:245 | Holds. The shelf's ash is plain of everything, which is why it salts a cell and cannot feed a hand. Seven's sealed two drams are ward-trace without the hair. |
| The last houses' route | 45:281–283, 45:341, 47:245 | Holds. Ordered aloud, answered by a bell, borne out by Perrin's empty litter, entered on the slate. |
| Other count slips | 41:319, 41:457, 47:41, 47:165, 47:249 with 48:251 | Hold. Five at the table and a sixth standing. "That's four." "That's my mother." "Two hands … two and a bit." Jude's tenth knot is two knots up the hill from the first, where the slate puts the split plank. |
| Knot names | 45:81–109, 45:269–279, 46:115–119 | Hold. Every knot is an ordinal. No "Seven" or "Eight" is left standing for a knot. |

### 2c. The three lines the repair author noticed

**1. The master's "four times since the thaw" (41:451): consistent.** He says it kneeling to cut the fourth. The stone has 340 for thirty-one years, then 350, 355, 362 and now 380 (41:399). Noa puts the figure "under four others" and says "That's four … In one year" (41:455–457), and his sheet reads "350, 355, 362, 380, since the thaw" (47:393). After the repair these four statements agree.

**2. The spindle's rake against the post's lean (44:17, 44:33): a required contradiction. See R1.** The lid, and so the shaft and the gate hanging in it, lie on the lane side of the post's foot. The post leans toward the lane, over that lid (42:93, 42:107, 42:469). A straight rod that leans toward the lane above ground runs toward the wall below ground. So the spindle goes down away from the gate it is said to be aimed at. This is in the frozen draft. The repair did not cause it; it only made the direction of the lean plain. Neither review located it.

**3. "Five paces from the shaft" for Dray's post (46:37): optional clarification.** The line agrees with its two nearest neighbours: Dray's voice crosses "five paces of dark" to Kiva on the lid (46:221), and Kiva at that post is "six paces" from the arm in the gap (45:359). The squeeze is elsewhere. The new cross is "four paces north from the lid, out into the middle of the lane, between the two rows" (46:169), and Dray is then "five paces off" from that cross too (46:331). If the north row is beyond the cross and Dray is five paces from the lid, she is at most about three from the cross. No listener can catch this and nothing turns on it. If it is touched, 46:331 is the cheap place, not 46:37. See O2.

## 3. Priority 2 — closing record, chronology, knowledge, cost: PASS

| Item | Where | Finding |
|---|---|---|
| Seven headings | 43:451, 43:463, 43:483–499, 48:345 | Hold. Name and place, *What, How, Went wrong, Cost, Second try, Why.* The manual's page and the Line's sheet now name the same seven, and the sheet reads seven lines. |
| Collarbone; Kiva and Orla | 48:369–389 | Holds. She writes in the fourth, passes over the fifth "where the collarbone was," and writes in the sixth. Orla's "You've not put what it cost" now follows from what was skipped, and "two of his columns" is right. |
| Noa's Saturday and the arm | 47:387–391, 47:301–305 | Holds. Dated Saturday the 8th, before the sling came off. The elbow came back Friday evening and the wrist on Saturday night, so "The elbow knew that there was a table. Below the elbow there was only something that she could see" is exactly the state that afternoon. Mara has "begun" her sheets on the 8th and brings eleven on the 15th (47:425, 48:293). |
| Crate and first shed | 48:365, 48:393, 48:425 | Holds. Kiva leaves the crate for the fourth post, so the unchanged "walked back along the lane to the first shed" is true. |
| Knot references | 47:249, 48:251 | Hold. |
| Elapsed dates | 48:235, 48:269, 48:251 | "Saturday the 15th" and "since six on Friday" hold. **"The week before last" does not. See R2.** |
| Annick knowledge | 47:197, 47:203 | Holds. "Long before this. The page had no date." "They're lifetimes apart." No figure, and no character makes the 2446 link. |
| Perrin's injury | 41:401, 41:451, 46:367 | Consistent inside the movement: ribs in linen, "two ribs that were in pieces," strapped for a spring and a summer. |
| Earshot | 47:177–179, 47:213–227 | Holds. Lumb is back at his sump. Aske and Kellan's mother are at the door lamp. Adlam is at the far end of the needles, "out of hearing of the desk." Mara keeps her voice under the pumps. What Lumb is then told aloud is only a keeper's fever and needles, which is all his line needs. Adlam's line now follows from that same sentence. See O5 for the one unnamed person. |
| Book Two's revelation | 47:193–211 | Not spent. The bible reserves "the shared record" for Book Two. The book map promises that a second account "confirms that part of Kiva's fever dream predates her, without explaining it." The page gives that and no more, to two people who already knew she had dreamed. |
| Four days, chronology | 47:293–305, 47:343, 47:375 | Fits. Thursday bread and Thursday night precede Friday's elbow. Thursday to Sunday is the four days Aske and Vane both enter. |
| Four days, body state | 47:91, 47:239, 47:295–299, 47:391 | Fits. The brass weight in place of Pru's finger is set up here and used in Noa's scene. See O3 and O4 for two soft spots in the new prose. |
| Pot, condensed | 47:259–261 | Keeps the decisive figures and the human line: the Line's way, half to the boxes that night, nine drams to a team, Halden drawing the same as Twenty-Eight "whose blade called a count from a chair." |
| Team book, condensed | 48:237–243 | Keeps 0.70 spent, Anwen's 0.41, Kiva's none, 9.0, 1.8, 7.2, Jude's 7.8, held 26.53 and sealed 0.8. "That adds" still adds from figures on the page: 13.53 (44:315) plus 1.80 back, 4.0 home and 7.2 is 26.53, and Jude's dram leaves 25.53. |
| Ending causally complete | 48:303–481 | Yes. The final scene is byte-identical, and each line it depends on is now true. |

## 4. Priority 3 — voice, listening, protected material: PASS

**The "I'd like it known / noted / written / understood" family.** Counted with the editorial review's own pattern: 19 in the frozen text, 8 now.

| Line | Speaker | Note |
|---|---|---|
| 41:465 | Perrin | "I'd like it known … that I don't mind." |
| 43:243 | Perrin | "It's noted," answering the fitter. |
| 44:151 | Perrin | Carrying the jars. |
| 45:233 | Perrin | "that I mind every one of these." |
| 46:105 | Kiva | "I'd like that written." Kept by instruction. |
| 46:205 | Perrin | Cut off by Kiva's "It's known." |
| 46:389 | Perrin | The payoff at the bar. |
| 48:279 | Perrin | "I'd like it noted that I minded properly, and at length." |

Seven are Perrin's and one is Kiva's protected line. Of the full phrase he has three before the climax, down from six, and one after it. The phrase is his again.

**"I find that."** Nine in the frozen text, six now: Mara at 42:407, 45:23, 47:133 and 47:211; Dray at 44:271; Rhea at 46:67. The last two are protected lines.

**Register.** Not flattened. The rewordings keep each speaker's turn of phrase. The fitter's "And me right-handed, if anybody's writing" (43:241) is better than what it replaced, and Perrin's "It's noted" still answers it. Vane's "Somebody may write that down" (44:65), Rusk's "It seems I remember where it is" (46:429) and Adlam's "I prefer it, on the whole, to being first to a certainty" (47:231) all hold their man. The fourteen dropped "that"s are in plain or young mouths.

**Changed joins, read for one-pass sense.** All 105 read cleanly. Three in chapters 45–48 took a second hearing and still pass:

- 46:299, "She counted on from her own six, to make a five of it and not a four." The next sentence ("The thing had fours") settles it.
- 47:259, "in the Pit's own parts, ground first." Compact, and it leans on Movement Five.
- 47:293, the section opening. See O3.

The eleven narration joins are all in chapters 41, 44, 47 and 48. No narration in 45 or 46 was joined.

**Protected material.** The developed action, the consent sequence, Orla and Hart's card, the juniors' run and the final two paragraphs all survive, as section 1 records. The named lines in the editorial review's Preserve lists stand, apart from the two exceptions the report discloses and one it does not list among them (section 7, third note).

## 5. Required corrections

**R1. The spindle runs away from its gate.** `manuscript/chapter-44.md`, lines 17 and 33.

- *Evidence.* 44:9 puts the lid "at the foot of the leaning post on the side toward the lane." 44:17 hangs the gate "across the shaft." 42:107 and 42:469 have the post lean into and out over the lane. 44:33 says the lean is "on the rake of the screw" and that a straight spindle reaches "a gate that's eight feet under and a pace to one side." A straight rod leaning toward the lane at the post descends toward the wall, so eight feet down it is about a pace on the wall side of the post's foot, not under the lid.
- *Why it matters.* That lower end falls under the line of the south row, where 42:449 and 46:167 already put the main. The mechanism wants the gate there. Only the two phrases that place the gate disagree.
- *Smallest safe change.* Two phrases, nothing else:
  - 44:17, "And across the shaft, a foot above the water," becomes "And across the wall side of the shaft, back under the post, a foot above the water,".
  - 44:33, "and a pace to one side" becomes "and a pace back toward the wall".
- *What it leaves alone.* The lid, the cross, the lean, the east and west grooves (45:59, 45:323), the arm going down on the lane side, and "It was never crooked. It's aimed," which becomes literally true.
- *Owner's call.* This adds one fact, that the shaft runs back under the post. If that is unwelcome, the fallback is to cut the second sentence of 44:33. That removes the figures a reader could check and leaves the direction wrong for anyone who draws it. I recommend the two-phrase change.

**R2. "The week before last" is a week out.** `manuscript/chapter-48.md`, line 251.

- *Evidence.* Jude speaks on Saturday the 15th (48:235). He asked what ash was for on Tuesday the 4th (44:95, 44:149; 47:67, "I said on Tuesday"). The 4th falls in the week directly before the week of the 15th, whether weeks start on Sunday or Monday. In the same chapter the bursar, on Thursday the 13th, calls that same week "last week" (48:47).
- *How it happened.* The frozen "last week" was right. The editorial review listed it as off by one unit, and the repair followed the review.
- *Smallest safe change.* Restore "I asked last week what ash was for".

**R3. A record line the repair made false.** `provenance/MOVEMENT-006-CONTINUITY.md`, line 186.

- *Evidence.* It reads "with the six-month mistake left in and ruled through." The page now says "a four-month mistake" (47:435), and the same file's section 0 says so.
- *Smallest safe change.* "six-month" becomes "four-month".

## 6. Optional taste notes

None is needed for a pass.

- **O1. 45:141, "You're feeding it!"** Brask has just said that it comes up whether she cuts or not. "You're hurrying it!" would match the one rule exactly. As Vane's shouted shorthand it reads.
- **O2. 46:331, "Five paces off."** See 2c item 3. "A few paces off" would let the yard draw true. Leave 46:37 as it is.
- **O3. 47:293, "There were four days of it first."** A new section opens on "it" and "first" with nothing before them. The next sentence rescues it. "There were four days without the arm" would spare the ear the wait.
- **O4. 47:297, the arm "swung into doorposts."** Aske has slung the arm by Thursday at five "to keep it from being knocked" (47:239), and the coat goes on "over the sling" two sentences earlier. "Before the sling" or "Out of the sling" would turn a small friction into the sling's cause.
- **O5. 47:177, the Works clerk.** He was last seen sitting at the keeper's desk over the sounder (46:443). The new sentence covers him only as "anybody else in that room." A clause sending him off would close it.
- **O6. 46:597, "six hundred more had done the same."** These are windows, not households, and the count is plausible for sixty-two tall houses. It echoes the household figure the repair has just untangled.
- **O7. The north row, 45:359 and 46:37.** "The eighth post, the last of the north row" is right once one knows the nine are counted through both rows. The page never says so outright.
- **O8. Outside this recheck's scope, noted in passing.** Perrin sets Ned down "against the shed wall four paces off" (45:349), where 42:91 puts the sheds forty paces from the gap. It is frozen text that neither review located.

## 7. Record notes

Apart from R3, the three records follow the current prose wherever I tested them: the night table, the growth rule, the lane sheet's seven lines, the proof's fourth and sixth columns, the earshot wording, Annick's undated page, the slate's route clause, the team book and the word count.

- **Status lines.** The continuity checkpoint (lines 8–10), the ledger (398–400) and the authorship entry (1608) say "not rechecked." They are for the acceptance entry to update, not for me.
- **The ledger's pot figures.** `STATE_LEDGER.md` line 492 still lists "reserve 24, schools 36, teams 36." Those figures are no longer spoken on the page. They follow from "the Pit's own parts," and the checkpoint marks them as resting on the frozen draft; the ledger does not. Optional.
- **Report, section 4, third bullet.** It says the Preserve-list lines were not edited "with the two exceptions in section 6." Pru's line at 48:205 also lost two optional "that"s. The editorial review lists "Pru entire" under Preserve and offers 48:205 as an example to trim, and the report's own Priority 3 table shows the edit. The edit is authorized; the bullet is slightly too broad. Optional.
- **Report, section 9.** At `HEAD` all eight chapters equal the frozen first draft, so the working tree is ahead of the commit by the repair and nothing else. I did not inspect any published copy.
- **After R1 and R2 are applied,** the checkpoint's sluice entry (line 580) and the report's row for 48:251 should follow the page.

## 8. Not done

I did not edit the manuscript, any record, review, report or prompt. I did not repair, score, re-measure the formula, draft Book Two, commit, push, publish or narrate.
