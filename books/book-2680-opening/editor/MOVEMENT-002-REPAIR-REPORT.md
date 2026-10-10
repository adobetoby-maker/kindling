# Kindling 2680, Book One — Movement Two (chapters 9–16) — consolidated repair report

> Built by TAC

Date: 2026-10-10
Brief performed: `editor/MOVEMENT-002-REPAIR-BRIEF.md`
Author of the repair: Claude Opus 5.5 (`claude-opus-5-5`), Monroe Jackson 1.3.0 / O'Connor 1.3.0. Same selected author and model as the first draft. New session; no subagents; Movement Three not started.

**Status: repaired, not verified.** This report does not claim the movement passed, and the author has not reviewed or approved the repair. A separate recheck is still owed. Section 5 gives the numerical targets that are still missed, and section 6 lists what is unresolved.

Locations are `chapter:line` in the repaired files.

---

## 1. What was read before editing

Read in full, in this order, before the first edit:

- The brief.
- Both reviews: `editor/MOVEMENT-002-EDITORIAL.md`, including the metrics appendix and script, and `editor/MOVEMENT-002-COLD-READ.md`.
- `packets/MOVEMENT-002.md`.
- `provenance/MOVEMENT-001-CONTINUITY.md` and `provenance/MOVEMENT-002-CONTINUITY.md`.
- `UNIVERSE_BIBLE.md`, `BOOK_MAP.md` and `STATE_LEDGER.md`.
- `manuscript/chapter-09.md` through `manuscript/chapter-16.md`, in order.
- `AUTHORSHIP.md` (the Movement Two entry and the Movement One repair entry) and the layout of `editor/MOVEMENT-001-REPAIR-REPORT.md`, for the record format.

Not re-read: the prologue and chapters 1–8. Anything this repair needed from them was taken from the Movement One checkpoint. That covers two fixes: the "twenty-eight seconds" in chapter 11 (checked against the trial clock in the checkpoint, where "it's holding" falls at about 2:20 and the stair husk at about 2:48), and Draw's direction (the checkpoint records it as "lower is better").

The frozen edition at `editions/movement-002-pre-repair/` was checked against its `SHA256SUMS.txt` before the first edit, when it was also byte-identical to the working manuscript, and again after the last edit. All eight files report OK both times. It was not modified.

## 2. Files changed

| File | Change |
|---|---|
| `manuscript/chapter-09.md` … `chapter-16.md` | Repaired in place by targeted edits |
| `provenance/MOVEMENT-002-CONTINUITY.md` | Reconciled to the repaired prose (31 edits) |
| `AUTHORSHIP.md` | Movement Two repair record appended |
| `editor/MOVEMENT-002-REPAIR-REPORT.md` | This file (new) |

Nothing else was written. Canon, plans, packets, both reviews, the brief, the compiled prompts and the frozen edition are unchanged. Nothing was committed or pushed.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `chapter-09.md` | 6,596 | 6,764 | +168 |
| `chapter-10.md` | 6,734 | 6,733 | −1 |
| `chapter-11.md` | 5,939 | 6,121 | +182 |
| `chapter-12.md` | 6,093 | 6,156 | +63 |
| `chapter-13.md` | 7,439 | 7,837 | +398 |
| `chapter-14.md` | 6,705 | 6,371 | −334 |
| `chapter-15.md` | 5,475 | 5,608 | +133 |
| `chapter-16.md` | 7,019 | 7,043 | +24 |
| **Movement Two** | **52,000** | **52,633** | **+633** |

Chapter 14 is the only chapter that was cut, as the brief asked. Chapter 10 is one word shorter from a revoiced line. Chapters 11, 12, 13, 15 and 16 were not shortened anywhere in their action. Chapter 13 grew most, from the Selka Dray exchange, the Team Eleven outcome and the corrected second-husk kill.

### Post-repair SHA-256

| File | SHA-256 |
|---|---|
| `chapter-09.md` | `111d5b583d5b851a69b3de4b3eb6cf6d9395bd1480df3249275c2f0a22676841` |
| `chapter-10.md` | `826c16323de4faf9d34ecdd0dec0678f5ffb04171d0d297f67b70d26254b513d` |
| `chapter-11.md` | `0cbb663565f4202579aa04b3b90b1c35adc024cb8d239f9ad93325547b7af6cb` |
| `chapter-12.md` | `ed94d8455fb3ffa67f5ae37bc1c9268c1c836aef4ac518b44f2431f91bd2cb98` |
| `chapter-13.md` | `de97fe38d89ed9f710663c1dd46b386a71648d7ed7394e3209ccf2b75e75ea3d` |
| `chapter-14.md` | `320f9246c1da7aa1dadce6d2a2e5fbc2dac4ec65a5a10efedc6ba42a7bfc53b2` |
| `chapter-15.md` | `51e43a03dee95b40fc8eaab70ff2ff53f846a179fb2ad606a563d9393ff77012` |
| `chapter-16.md` | `51ec863cbf15621e3765ce304fc759c1ccf9b3d9cfb5444a0bd809e9004cc112` |

## 3. What the brief said to preserve

| Requirement | Result |
|---|---|
| All chapter headings | Unchanged, all eight |
| All eight chapters; section structure | 71 sections before, 71 after |
| All developed fights | Unchanged in length or longer: sponsor's floor, both contained floors, license day, all three carries |
| Every meaningful choice | All twenty lead beats in the editorial's list are still on the page |
| The kitchen-table ash vote | Complete. One phrase of Perrin's was revoiced (`14:160`); nothing was cut |
| Halloran's shelf and comb | Untouched apart from two revoiced reactions (`14:67`, `14:91`) |
| The ward-trace dram and Aske's warning | Kept; the exchange around them is shorter |
| Exact share arithmetic | 20.8 → 10.4 / 2.6 / 3.9 / 3.9, now on the clerk's slate (`14:113–117`). Spend 0.5 + 1.0 + 1.0 + 1.4 unchanged |
| Noa asking consent before filing | Kept in his cutaway and in chapter 16 |
| Calendar, both clocks | Unchanged except the one corrected day (C1). License-day times and the thirteen forty-minute intervals stand |
| 9–7 meet score, dram line | Unchanged: 4–2, 8–4, 9–7; 0.38, 0.87, 0.98 |
| Hold-post readings | Kiva's unchanged. Jude's spring figure corrected (C15) |
| Injury and power boundaries | Unchanged. No two-door sequence. Disk cold at all three checks. Fingers still dull and recovering |
| Movement's ending state | Unchanged: place retained, Flask moved up, 8.4, "Orla. Count." |
| Brask's courtesy, Jude's opening speech, Anwen's phrase | Kept. One clause of Jude's was revoiced (`09:37`) |
| No new viewpoint | None added |
| Noa and Hollis he/him; no pronoun for Aske | Kept |

## 4. Material decisions

### Owner rulings, as applied

- **Brief dialogue stays brief.** No speech was lengthened to move the sentence figures. They did not move (section 5).
- **The Handful license stays controlled.** No husk injures anyone who did not choose it.
- **Cutaways kept, none added.** Noa's was shortened as Priority 3 asks. Rhea's lost 83 words when her gloss came out.
- **Disk cold, two-door sequence reserved, Unroofed Sky withheld.** Nothing touched.
- **Lowen Brask is the adaptive human rival.** Selka Dray now carries resentment only. She does not fight Kiva, speak to her directly, or adapt.

### Priority 1 — days, counts, measurements, space, rules

Every C1–C15 item and every row of the cold read's table was addressed.

| Item | What was wrong | What the page says now | Where |
|---|---|---|---|
| C1 | Kiva told Orla on Friday two things that happen on Saturday | She goes early on Saturday, before the others, because the fourth condition "was not a thing to say across a lane." | `11:71` |
| C2 | The Home Line killed the second husk against a lit wall with a catcher beneath it | The ward-holder drops her wall and steps back three paces, the neighboring walls close behind the husk, the blade lights for the cut and runs home, and Bettan catches on bare grass | `13:415` |
| C3 | Draw was never defined, and 0.93 did not follow from eleven hundredths | Noa defines it once: what you burned on a piece of work against what the book says that work should cost; one is standard, lower is thriftier. Ysra reads "eleven hundredths and a hair on the tape, set against the book's twelve for that work. Nought point nine three." | `11:31`, `16:419` |
| C4 | Third carry began at the foot of the porch with "sixteen paces to go" | "Kiva went down her own two steps and no further." | `16:13` |
| C5 | Fifteen teams in fourteen positions | Fourteen called: thirteen from the bottom of the call, plus Nineteen "in the place of a team the warden had not passed fit." A fifteenth (Eleven) sits apart | `13:77` |
| C6 | "Live-cell events" did not cover a Kennel floor or a held tear | Kellan, having asked the Chair's clerk: "It runs to any charged cell, and to a held rift, and to the Kennel lattice, which is a rift in a cage." | `09:287` |
| C7 | Team numbers coincided with call positions five times | Nineteen stands 18th and Eleven 9th. Kellan would go up "twenty-two places." Kiva's log reads T33, T14, T26 | `09:281`, `10:389`, `10:453`, `13:83–87` |
| C8 | "One from each team that had not yet been called" | "One from each team in that afternoon's section" | `10:5` |
| C9 | "Agnes Roake's cloth" | "Kiva's cloth" | `13:369` |
| C10 | Orla's second written condition was never shown met | Wednesday night, six tins sealed with the bad hand, each called and each turned over. Orla's speech and the certificate both cite it | `11:131–133`, `11:155`, `11:335` |
| C11 | Team Eleven vanished | Vane will not seat a new hand-door in front of a tear that has "stopped keeping time." Eleven leaves without a floor; Anwen watches and does not take out her list | `13:67`, `13:465`, `13:503` |
| C12 | Aske said "four drams" a day before the share was worked out | "A catcher walks in off a potato bed with a whole Handful of it." | `14:105` |
| C13 | Anwen "held its eyes" | "Did not give it an inch." | `13:309` |
| C14 | "A dozen" sandbags against "four hundred" | "The Hall has forty of them." | `12:7` |
| C15 | Jude's "six and a half on a good day" against a measured 6.6 | Measured 6.4. Down to 4.1 is still "a bit more than a third" | `16:237` |

From the cold read and the editorial's smaller notes:

- **The chained Kennel book.** It "hung by a chain and a hook" (`10:81`) and is "unhooked" to go down to the floor (`11:181`, `12:353`).
- **Twenty against twenty-eight seconds.** Kiva now recalls "the better part of half a minute" (`11:93`). Kellan's exact twenty-eight stands.
- **Kellan's first tin.** He holds "the first six of twenty-one drams" (`12:135`).
- **Floor geometry in the print scene.** The north gutter is gone from the sentence. Kiva sees the south tank "with the iron grate at its low end," and Kellan on the bridge "with his blade low and lit" (`12:67`). She says so in the cold room (`12:125`). The reveal now plays fair on a second reading.
- **The lit blade Druce did not call.** He says it looked like more than two and a half paces to him too, "and that's in the book against my name" (`12:113`).
- **"Stood over it lit."** Vane now says Dray "was still lit when it went" (`13:175`), which is what the scene shows.
- **Loose pronoun.** "Anwen told Kiva on the Cellhouse steps" (`10:419`).
- **Perrin's "both lanes."** "My Hall won your lane. It lost Kellan's" (`16:361`).
- **Taps against Hold.** Pru's post reading no longer gives a tap count beside her Hold (`16:239`), so the two scales are not set against each other.
- **"He hit it with a chalk."** Anwen now cites what chapter 9 shows: the printed dish tipped into the salt (`12:227`).
- **Rhea's name.** Kiva knows the white streak from the poster and thinks "Rhea Sorn" (`15:21–23`). The checkpoint already assumed this.
- Two things I found on the way and fixed: teams go down to the floor "in fours," not threes, to match "three other teams" (`09:219`); "Sundays too" is "Sunday too," since the week holds one (`11:69`).

### Priority 2 — friction and voices

**The school pushes back in three existing scenes.** No scene was added and nobody is a cartoon.

1. *Kennel, chapter 9.* Nobody sits on the two benches in front of Team Seven (`09:97`). When Druce mentions cells, a dozen heads turn and a girl takes her kit bag onto her knees (`09:181`). On the floor, the neighboring team carries its kit to the far wall, and "Druce saw them go. He let them" (`09:221`).
2. *Sag Line, chapter 13.* Selka Dray says in front of the line that Kiva fouled a cell and "got a roster place for it, and the best blade in the year to stand dark at her back." Nobody answers. Kiva has nothing to say "because the part about the cell was true" (`13:181–183`). Dray leaves when the weight is called, and Kiva "did not think that twenty and eight-tenths had changed her mind about anything" (`13:505`).
3. *Stonehand, chapter 15.* A man moves his small daughter away from the western porch and a dozen people follow (`15:17`). In the second carry the Hall's rows sing "changing" back at her, and by the third change half the gallery says it with her (`15:239`, `15:303`).

**One authority stays unpersuaded.** The meet referee signs the card clean and tells Kiva what she has written on the back: a fighter who has to be flagged from one door to the next "isn't safe. She's supervised" (`16:207`). Ysra reads it and makes no remark (`16:393`). The line "that's a different fighter's card" is kept inside the same speech. Two smaller cases: the ash-office clerk is now bored and brusque (`14:123`), and Halloran "did not say whether she believed a word of it" (`14:67`).

**`Hm` and `Huh`.** Nine before, four after.

| Speaker | Before | After |
|---|---|---|
| Druce (`10:53`) | "Hm" | Kept. His mannerism |
| Perrin imitating him (`10:55`) | "*Hm*" | Kept. Part of the same beat |
| Agnes Roake (`13:131`) | "Hm … exactly like Warden Druce" | Kept as the one deliberate echo |
| Vane (`13:483`, `13:487`) | "Hm"; "did not say *hm*" | "It would be."; "did not chalk that" |
| Halloran (`14:19`, `14:67`) | "Hm" twice | "Are you, now."; the unpersuaded line above |
| Brask (`16:109`) | "Hm" | "'No,' said Brask, as if she had handed him something." |
| Ysra (`16:429`) | "Hm" | "So they are." |
| Kellan (`11:107`) | "Huh" | Kept. See section 6 |

**The "I want it said" family.** Twelve before, four after, plus the deliberate exchanges. Anwen keeps all of hers (`10:405`, `11:125`, `16:349`), and the "It's said" replies stay (`10:441`, `13:433`, `16:351`). Perrin keeps the one that answers Anwen (`13:431`). His other five now sound like him: "I'd have turned it down, mind"; "Somebody put that in the book"; "I mention it so that somebody will have thought about me"; "Somebody write that down"; and at the kitchen table, "I'll tell you the rest, since we're telling." Jude says "I'm telling you now" (`09:37`), Orla "Don't go home thinking I am" (`11:155`), and Ysra "Don't carry it out of this room as anything more" (`16:401`).

**Understated approval.** "Not unkindly" three to one. "Did not soften it" two to one. "Nearly/almost smiled" three to two: Ysra's became a mark in the margin of her notes, "from which Kiva gathered that somebody was about to" write the missing rule (`16:397`).

### Priority 3 — the escalation, and chapter 14

**The pairing is remarked on once.** Three sites before, one after.

- *Noa* keeps a single sentence: "He drew no line between anything on it" (`14:242`). He is the first witness and it is in character.
- *Rhea's* card now carries the tear count on its back "for the board's eye" and nothing else (`16:317–319`). The paragraph that set it beside the load plate and called the class strong is gone.
- *Ysra* gives both reports as what the Flask change rests on: more first-years fit to try, and a Home Line that wants more licensed hands (`16:437`). The aside about two offices and one desk is gone. Orla still lifts her head.

Every fact is kept. "Strong year" or "strong class" fell from five uses to two (Noa's thought; the Stonehand master at the plate). "Dirty spring" fell from two to one, now attributed to the Home Line. Nothing is proved and Kiva learns no filter explanation.

**Chapter 14.**

- *A want, early.* Before Halloran appears, Anwen is carrying "passed, subject to the tins": if a tin printed overnight or a pinch will not hold to sixty, there is no license, no Graywater, and Kellan is back at the bottom of a call (`14:11`). Her hand shuts on the bench during the grade count and opens at sixty (`14:33`). The grading lesson now has a stake under it.
- *Aske.* 251 words to 201. The two sentences that load the ward-trace dram are intact, and so is the finger test.
- *The ash office.* The sum is on the clerk's slate as five lines instead of a speech (249 words to 215 for the scene up to the strongroom). The arithmetic and the order of shares are exact.
- *Noa's cutaway.* 1,196 words to 844 by the editorial script, a cut of 29%. The forty-year Draw medians are two sentences. The section moves faster to its decision, which is unchanged: ask her first, name second, file nothing if she says no.
- *Net effect, stated plainly.* The chapter is 334 words shorter (5%), and nearly all of that is Noa's cutaway. The first third, from the grading room to the kitchen table, is 2,628 words against 2,613 before. The stake I added for Anwen cost about what the compressions saved. That stretch is under pressure now. It is not shorter.

## 5. Numerical result — target against observed

Measured with the editorial's own script, extracted unchanged from its appendix (`metrics_m002.py`, SHA-256 `08a6f5b2…9617`, importing `metrics_m001.py`, SHA-256 `462e9ac6…a308`). Run before the first edit, it reproduced the editorial's figures exactly. These are measurements, not a gate, and the repair was not iterated to move them.

### All sentences, chapters 9–16

| Metric | Target | Before | After |
|---|---:|---:|---:|
| Mean sentence length | 14.6 | 9.84 | **9.93** |
| Median | 11 | 7 | **7** |
| Five words or fewer | 27.7% | 41.5% | **41.0%** |
| Forty words or more | 3.3% | 1.52% | **1.63%** |
| Flesch Reading Ease | 72.3 | 92.2 | **92.2** |
| Flesch–Kincaid grade | 6.8 | 2.8 | **2.9** |
| Syllables per word | ~1.41 | 1.237 | **1.236** |

**The whole-text targets are still missed, by the same margin.** That is the expected result of the owner ruling. Speech is still 48.0% of sentences (48.1% before).

### Narration, speech and ledger lines

| Slice | Mean | Five or fewer | Forty or more |
|---|---:|---:|---:|
| Narration, before | 12.95 | 29.0% | 2.94% |
| Narration, after | **13.09** | **28.2%** | **3.06%** |
| Speech, after | 7.21 | 51.7% | 0.32% |
| Ledger and italic rows, after | 5.47 | 62.5% | 0.43% |

Narration stays near the formula and moved slightly toward it. Its mean is still about a word and a half under 14.6.

### Other measures

| Measure | Target | Before | After |
|---|---:|---:|---:|
| Lead POV share | ~87% | 89.6% | **90.6%** |
| Development proxy, lead, per 10,000 | 4.5 | 4.4 | 4.2 |
| Progression vocabulary, combined, per 10,000 | — | 133.9 | 132.3 |
| Chapter 14 progression vocabulary, per 10,000 | — | 204.5 | 202.5 |
| Number words per 10,000 | — | 280.7 | 276.4 |
| Sections; mean words | ~950 | 71; 731 | 71; 740 |
| Staccato runs of five or more / eight or more | — | 61 / 7 | 58 / 7 |
| Paragraphs of 150 words or more | — | 4 | 8 |
| `, and` joint; listed subordinators per 1,000 | — | one per 54; 10.5 | one per 53; 10.7 |
| "said" per 10,000 | ~41 all reporting verbs | 96.5 | 95.9 |

Chapters 1–16 together, after the repair: mean 9.98, five or fewer 42.1%, forty or more 1.61%, grade 3.0, lead share 89.1%. The 1.7× front-loading ratio still cannot be confirmed until later thirds exist.

## 6. Unresolved, or needing the owner

1. **Draw's direction against the brief's wording.** The brief describes Draw as "usable output relative to the relevant book/bench expectation." Movement One fixes it as ash per standard work against 1.0, lower better. I kept the ratio-against-expectation sense and the established direction, and Noa says "lower is thriftier." If the owner meant to reverse the direction, that is a canon change reaching back into Movement One and was not mine to make here.
2. **"The book's twelve" is a new figure.** A four-minute contested hold is given a book cost of twelve hundredths so that 0.93 follows from the tape. Nothing earlier contradicts it. It should be recorded as canon or replaced.
3. **Team Eleven's outcome was a choice.** I had Vane shut the tear. The alternative, that Eleven goes in on a later husk and passes, also fits the clock. Mine makes Anwen's choice of Seven turn out lucky, and the page does not say so. If that reads as rewarding loyalty too neatly, the paragraph at `13:503` is the only one to change.
4. **Lead POV share moved away from the target**, 89.6% to 90.6%. It follows from shortening two cutaways while adding to Kiva's scenes, both of which the brief asked for.
5. **Chapter 14's system-vocabulary density did not fall** (202.5 against 204.5), and its first third is no shorter (section 4). The cuts came out of Noa's narration, which carries little system vocabulary. The chapter is 5% shorter and has a stake under its first scene, but its first third is still five scenes in which an adult explains something. Whether that is enough is for the recheck.
6. **Kellan's "Huh" is kept** (`11:107`). It is his from Movement One, he says it once here, and chapter 15 recalls it. The brief says to revoice the "other repeated hm/huh replies"; I read one use by its owner as not repeated. Easy to change.
7. **Eight paragraphs now run past 150 words**, up from four. The new ones are speeches: Dray, Vane, Ysra. They have not been checked aloud.
8. **The referee's note is a new open thread.** It sits on the back of a card in Ysra's folder. Movement Three may use or ignore it.
9. **Friction was kept to three scenes.** Three scenes were given reactions, as the brief's ceiling allows. I did not add Kellan's first-team master, which the brief listed as a possible carrier, to stay inside that ceiling.
10. **The ash-office slate is in digits**, which adds five decimal rows to a movement the editorial already flagged for a narrator's digit rule. Digit tokens rose from 96 to 105. No rule for reading decimals aloud has been set.
11. **Not addressed, because the brief did not ask:** the 4,900-word run-out after the last bell in chapter 16; chapter headings that all read "Kiva:"; chapter 9's lecture cut into three short sections; the simile rate; "said" at 96 per 10,000. "Did not" rose from 132 uses to 139.
12. **Carried unchanged:** the second purchased Kennel floor has no date; the month is unnamed and has thirty days; Team Nineteen's later history is open.

## 7. Verification still owed

- A separate targeted recheck of the three priorities, by a session that is not this one. I have not reviewed my own repair.
- In particular: that the license-day count now reads cleanly on one pass (`13:67–77`, `13:135`, `13:165`, `13:469`, `13:503`); that the Draw definition lands before `16:419` needs it; that the three friction beats read as pressure and not as decoration; and that chapter 14 moves.
- A read-aloud pass over the new long paragraphs and the clerk's slate.
- Owner confirmation of items 1 to 3 above before Movement Three leans on them.

## 8. Post-repair verification

Completed after this report by a separate Claude Opus 5.5 review-only session. See
`editor/MOVEMENT-002-TARGETED-RECHECK.md`.

- All three priorities passed; no second prose repair was justified.
- The owner accepted Draw as lower-is-better efficiency, the twelve-hundredths
  contested-hold benchmark, and Vane denying Team Eleven its floor.
- Four verifier-identified phrase corrections were applied afterward: Halloran's
  ambiguous pronoun, the month boundary in Ysra's report, the Home Line catch image,
  and the candidate headcount. These raised the final `wc -w` total from 52,633 to
  **52,637** without changing any event.
- Final hashes and word counts are recorded in `AUTHORSHIP.md`. The frozen first draft
  remains unchanged and checksum-verifiable.
