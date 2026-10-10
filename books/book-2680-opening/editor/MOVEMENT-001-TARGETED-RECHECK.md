# Kindling 2680, Book One — Prologue + Movement One — targeted recheck

> Built by TAC

Date: 2026-10-10
Prompt performed: `editor/MOVEMENT-001-TARGETED-RECHECK.prompt.md`, read in full
Status: review only. This report is the only file written. No manuscript, canon, plan, continuity, authorship, prior report or prompt file was changed. No subagents were used.

---

## 0. What kind of read this is

**A same-model, informed recheck in a fresh session.** It is not a human read and it is not independent testing. The reviewer is the same model that drafted and repaired the text, and it read the repair report and the continuity checkpoint before judging the page. Agreement with those two files is weak evidence. Disagreement is the more useful signal, and section 2f lists every disagreement found.

### Read before judging

- Repaired manuscript, all nine files, complete and in order.
- Both reviews, the repair brief, the repair report, the continuity checkpoint and `AUTHORSHIP.md`, complete.
- Canon and planning: `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `STATE_LEDGER.md`, `CHARACTERS.md`, `PROLOGUE_PLAN.md`, `IDEA.md`, `SERIES_MAP.md`, `README.md`, `packets/MOVEMENT-001.md`, `packets/MOVEMENT-002.md`, complete.
- Frozen edition: used for every before/after number and for line-by-line comparison of each passage cited below. It was not re-read end to end as prose.

### Integrity checks

- Frozen edition: all nine files pass `SHA256SUMS.txt` and match the manuscript at commit `1003491`.
- Repaired manuscript: all nine SHA-256 values match the table in the repair report.
- Metrics script: extracted unchanged from the editorial appendix. SHA-256 `462e9ac63f3d831ce8465b78598e32ed0a95b25b25adef9373d1495dc402a308`, the hash both earlier reports record.

Locations are `file:line` in the repaired manuscript unless marked "frozen."

---

## 1. Verdict

| Priority | Result | In one line |
|---|---|---|
| 1 — factual and spatial continuity | **PASS**, one line correction owed | Every original finding is closed on the page. The repair introduced one new miscount (a single word) and four soft wording seams. |
| 2 — cadence and read-aloud | **PASS** | Narration is at the formula. Impact fragments land. The whole-text targets are still not met, and the remaining gap is not an audible defect. |
| 3 — voice, revelation, aftermath | **PASS** | Six distinguishable voices. Jessamy Hart's particulars arrive once, in chapter 8. Each aftermath scene keeps its own judgment. |

**Overall: PASS. A second repair pass is not justified.**

The one thing that should be fixed before this text is treated as settled:

- `chapter-06.md:203` says "Seven more steps" after Kellan has already climbed two of the seven. It should be five. Details in 2f, item N1.

Four optional line-level touch-ups are listed in 2f (N2 to N5). One planning file outside the manuscript still uses the retired ash wording (2d).

This report does not change the status lines in `AUTHORSHIP.md` or the continuity checkpoint. Both still read "repaired, not verified." Updating them is the owner's or author's step.

---

## 2. Recheck 1 — factual and spatial continuity

### 2a. Terrace Ring score, rebuilt from the page

Rules at `chapter-04.md:55`: body or head is one point, arm or leg is a half, three points wins.

| Touch | Where | Call on the page | Running score | Line |
|---|---|---|---|---|
| Renn 1 | Collarbone (body) | "One. Renn." | 1 – 0 | `:119–121` |
| Renn 2 | Ribs (body) | "One. Renn leads, two." | 2 – 0 | `:161–163` |
| Rowan | Right forearm (limb) | "Half. Rowan." | 2 – ½ | `:269–271` |
| Renn 3 | Back, between the shoulders (body) | "One. Renn wins, three to a half." | 3 – ½ | `:279–281` |

It adds. The supporting lines agree: "cost her a point" (`:141`), Kiva's book "One point to him … One more point … Lost, 3 to a half" (`:375`), dram 0.31 against 0.88, "nearly three times as much" (`:301–305`, ratio 2.84), and Kellan's pocket note (`:359`). No exchange was removed.

### 2b. Cellhouse clock, rebuilt from the page

Only five clock values are printed: the first release "at a minute and ten" (`chapter-05.md:269`) and the four board times (`chapter-06.md:383–389`). Everything else below is my interpolation from the needle readings and the stated intervals. Breaker at 8.5 (`chapter-05.md:253`). Standard extraction 4:00.

| Clock | Needle | Event on the page | Line |
|---|---|---|---|
| 0:00 | — | Bell | `05:221` |
| ~0:40 | 6.0 | Left palm on the drum, no door | `05:233–237` |
| | 6.1 → 6.2 → 6.3 | A tenth in ten seconds, the next in nine | `05:249` |
| ~1:08 | 6.3 | "It'll trip in under two minutes." | `05:259` |
| **1:10** | — | Release 1, one husk | `05:265–269` |
| ~1:16 | 6.4 | | `05:279` |
| ~1:39 | 6.7 | "Seventy seconds." Tenths every seven seconds. Perrin needs thirty. | `05:285–293` |
| ~1:46 | 6.8 | | `05:299` |
| ~1:55 | — | Release 2, two husks | `05:301` |
| ~2:00 | 7.0 | "Fifty seconds." Next tenth takes five seconds. | `05:313–319` |
| ~2:10 | 7.2 | Forty seconds left. Perrin needs thirty more. | `05:339–343` |
| ~2:12 | — | Declared change: tuning, hand door only | `05:351` |
| ~2:20–2:40 | 7.3 | Needle holds. "Ten seconds. Fifteen. Twenty." | `05:373–385` |
| ~2:40 | 7.3 | Release 3, three husks | `05:387–389` |
| ~2:48 | 7.3 → 7.6 | Fear. All three doors go into the cell. | `05:409–421` |
| ~2:52 | 7.7 | Kiva breaks the stair husk with the dark bar | `05:425–433` |
| to ~3:21 | 7.7 → 8.2 | "A tenth with every few breaths," no hand on it | `05:437–459` |
| ~3:25 | 8.3 | Release 4, three husks | `06:29–33` |
| **3:31** | — | Over the rail, undeclared | `06:49`, `:389` |
| ~3:34 | — | Husk hits. Disk swings out. | `06:85`, `:111`; `08:291` |
| **3:38** | 8.5 | Breaker. Winch dies. Shutter onto Perrin's palms. | `06:115–123` |
| **3:44** | — | Renn declares, vaults, pulls the quench | `06:201–219` |
| ~4:20 | — | Perrin lets the shutter down and rolls clear | `06:293–297` |
| **4:41** | — | Casualty over the green line | `06:311` |

Checks I ran against that table:

- **The three later countdowns agree with each other.** Seventy seconds from ~1:39, fifty from ~2:00 and forty from ~2:10 all predict a trip at 2:49–2:50. "Under two minutes" from ~1:08 covers the same moment.
- **The countdowns agree with the stated intervals.** Take the gap the page gives at each call point (nine seconds, seven, five, then a little under five) and let it shrink by about five percent per tenth. That gives roughly 115, 80, 51 and 42 seconds to the red line. Kiva calls "under two minutes," 70, 50 and 40.
- **The intervention is now necessary on the page.** Untuned, the cell trips near 2:50, more than a minute inside the four-minute standard. At 7.2 Perrin needs thirty of the forty seconds left just to clear the housing (`05:343`). The later page shows the haul itself as slow, "a hand's length at a time" (`06:259–271`), so a ten-second margin would not have been enough. The editorial review's central objection (B2) is answered.
- **After the contamination, the rate fits the board.** 7.7 to 8.5 is eight tenths in about 46 seconds, and 8.3 to 8.5 is two tenths in about 13 seconds. Both sit near six seconds a tenth.
- **Releases.** A 45-second timer (1:10, 1:55, 2:40, 3:25) fits all four. "Four releases to a run" appears at `05:83` and `05:109`, and `06:31` says "for the fourth time." The duplicated release is gone.
- **Husks.** Nine released (1, 2, 3, 3) and nine accounted for. Renn kills five from the first three releases (one, two, two). Kiva breaks one with the dark bar (`05:425`). Of the last three, one is "in pieces on the bottom tread" (`06:147`), Renn breaks one on Kiva with a dark blade (`06:243–245`), and he goes back for the one he left alive on the stair (`06:253`).
- **Perrin's hold.** 3:38 to about 4:20 is about forty seconds. His note says "approx. 40 sec" (`07:185`) and he says "forty seconds" (`07:193`).
- **Twenty seconds.** The tune's hold is twenty on the page (`05:385`), in Kellan's mouth (`06:411`) and in Orla's (`07:21`).

**Tolerance.** The table closes to within about ten seconds, not to the second. The tight spot is the first call: Kiva reads 6.3, does the sum twice, leans over, calls and gets two replies, and the first release follows at 1:10. With the page's own intervals that is about two seconds for some twelve seconds of action. No printed number is contradicted, and a reader cannot see the squeeze, because the early readings carry no clock.

### 2c. Cellhouse geometry, rebuilt from the page

- Hall about 40 by 14 paces. Gate and green line west. Gallery along the north wall (`05:67–69`, `:211`).
- Mezzanine at the east end, **2.5 m** up, the same figure in all three places (`05:73`, `06:55`, `06:141`).
- Twelve-step stair on the south wall, rail on the open side (`05:73`). Facing down it: wall on the left, rail on the right, mezzanine above and behind (`06:159`, `:171`). That is consistent for a stair rising east.
- Pump room under the mezzanine with one wide west-facing doorway and a knee-high gap (`05:75`).
- **Hands.** Left palm reads the cell (`05:237`, `:441`). The bar forms on the right fist (`05:411`). "Both hands" is gone. She goes over the rail on her left hand (`06:49`).
- **Sightline.** From the rail she sees "the length of him and nothing past him" and cannot see Anwen at all (`05:257`). Everything inside reaches her by voice (`05:337`, `06:17`).
- **Perrin.** On his back along the threshold, hands on the shutter above his chest, shoulder under the housing (`05:257`, `:293`; `06:13`). "Drops on me" (`06:277`). He rolls toward Kiva to get clear (`06:297`). One position, held throughout.
- **Dummy.** Out head-first by the collar, past Perrin's boots, heels last (`06:259–261`).
- **Cuff.** The limb scrapes from the elbow down "until it struck the leather cuff and skidded over the slab" (`06:107`), and the cuff leather is scored (`06:325`).
- **Kellan.** Vaults from the rail to the mezzanine edge with a stated reason (`06:203–213`), drops back off the edge beside Kiva (`06:241–243`), and scrapes his right knee on the way up (`06:215`, `:405`).

The climax reads on one pass. I did not have to redraw the room.

### 2d. Original findings, one by one

**Editorial review, section 4.** All thirty items are closed.

| # | Finding | Status | Evidence in the repaired text |
|---|---|---|---|
| A1 | Six-hundred-year stance stone | RESOLVED | "five hundred years of feet" (`prologue.md:1113`) |
| A2 | Paper law and register "six hundred years" | RESOLVED | "since the first licensed cells, more than four hundred years ago" (`02:51`); "more than four hundred years of it" (`08:145`) |
| A3 | Torch as a one-door cap | RESOLVED | "as far as her own door had ever taken her" (`03:149`); Rhea likewise (`08:269`) |
| A4 | Cell-book tunes dated in the future | RESOLVED | 13th, 20th, 27th "of last month" (`02:57`) |
| A5 | Draw bench "yesterday" | RESOLVED | "the draw bench on Wednesday" (`03:87`) |
| A6 | "He said so on Monday" | RESOLVED | "on Classification Day" (`04:41`) |
| A7 | "Eight days" on roster Monday | RESOLVED | "five days" (`08:337`) |
| A8 | Core trips and resets in the same minute | RESOLVED | Trip 02:44 (`08:149`); report "at a quarter to three, the minute it tripped" (`07:347`); reset "a little after half past three" (`07:325`) |
| A9 | Perrin's nine seconds | RESOLVED | "approx. 40 sec" (`07:185`); see 2b |
| A10 | Laundry downstairs or next door | RESOLVED | Next door in every chapter (`01:421`, `02:123`, `07:131`, `:259`, `:321`, `:325`) |
| B1 | Bout totals 2.5, called as 3 | RESOLVED | See 2a |
| B2 | Trial clock does not close | RESOLVED | See 2b |
| B3 | Mezzanine height | RESOLVED | 2.5 m throughout |
| B4 | Corbel Reach access | RESOLVED | 2152 crew worked "the empty towns on the far bank" (`prologue.md:297`); before 2170 only scavengers went closer (`:361`) |
| B5 | Doubled chute release | RESOLVED | See 2b |
| B6 | Stair handedness | RESOLVED | See 2c |
| B7 | Unmotivated rail vault | RESOLVED | Reason given (`06:203`). The new sentence carries a miscount: N1. |
| B8 | Rhea's plate time | RESOLVED | From the three-and-a-half-minute mark (`08:263`), then 3:31 (`:287`), disk at 3:34 (`:291`) |
| B9 | Sponsorship standing and hearing | RESOLVED | "one form and my stamp … You haven't filed" (`01:321`); form signed and stamped (`08:125–127`) |
| B10 | Draw "down" | RESOLVED | "your draw is worse, up from two-nine" (`01:271`) |
| B11 | Kindling clock | RESOLVED | "well past two in the afternoon" (`prologue.md:1103`); Mara's clock (`08:167`) |
| B12 | Three thousand in the gallery | RESOLVED (owner ruling) | Four hundred in all five places (`05:211`, `06:397`, `07:21`, `:189`, `08:33`). "Three thousand" no longer appears. |
| B13 | "Forty-five again" | RESOLVED | "forty-one again" (`prologue.md:427`), matching the ledger line (`:411`) |
| B14 | Perrin swallows his dram | RESOLVED | He closes his fist on it (`05:201`). The wording is awkward: N5. |
| B15 | Quench "ten thousand times" | RESOLVED | "had almost never had to do it herself" (`07:267`) |
| B16 | Orla at the breakfast table | RESOLVED | She climbs to the kitchen doorway (`04:17`) |
| B17 | "Last night" attaching to the filing | RESOLVED | "I filed it. Ours, from last night." (`08:149`) |
| 4c | Kiva knows the letter came in winter | RESOLVED | "When did this come?" / "In the winter." (`07:371–373`) |
| 4c | Kellan recalls a prediction nobody made | RESOLVED | "She had not said it would call them." (`06:179`) |
| 4c | Kiva at the edge of the 2446 inference | RESOLVED (owner ruling) | See section 5, ruling 6 |

**Cold read, section 4.** Items 1 to 15 and 17 to 21 are the same findings as above, or are closed as follows.

| # | Finding | Status | Evidence |
|---|---|---|---|
| 1–4, 6, 13, 14, 15, 17, 18, 19 | Same as B1, A7, A6, A8, B10, A9, A3, B4, B17, A10, 4c | RESOLVED | See the table above |
| 5 | Kellan's Draw "better than eight-tenths" | RESOLVED | "a Draw near eight-tenths" (`01:107`) |
| 7 | Rhea's card knows the placement | RESOLVED | "Placement not yet posted." (`08:313`) |
| 8 | Orla wondered "for eleven years" | RESOLVED | "for four years, ever since the seal was broken" (`03:407`) |
| 9 | Perrin's orientation and the dummy's exit | RESOLVED | See 2c |
| 10 | Kiva sees inside a room beneath her | RESOLVED | See 2c |
| 11 | Which hand is on the drum | RESOLVED | See 2c |
| 12 | Scrape with no cuff or slab | RESOLVED | See 2c |
| 16 | Mixed units | PARTIAL, by choice | Meters throughout the chapters and in snapshot 9 (`prologue.md:841`, `:909`). "Sixty miles" stays in 2085 (`:117`). The repair report lists this as left. It reads as period speech. |
| 20 | Drill "in ten" after 9.5 | RESOLVED | "in nine" (`08:345`) |
| 21 | Sling "hung at her side"; unsaid cold-cloth line | RESOLVED | "lay across her chest in a sling" (`07:9`); the medic now says it (`06:369`) |
| Thread | Draw absent from the trial | RESOLVED (owner ruling) | Board dram line (`06:391`) |
| Thread | Rail vault with a clear stair | RESOLVED | `06:203`; see N1 |

**Read-aloud hazards the reviews named.**

| Hazard | Status | Evidence |
|---|---|---|
| Star on the bout board | RESOLVED | "K. Renn (requested) against K. Rowan" (`04:37`) |
| "3 to ½" | RESOLVED | "Lost, 3 to a half" (`04:375`) |
| "T-0. 14:52" | RESOLVED | Mara says "T-zero" and "eight minutes to three in the afternoon" (`08:167`) |
| Spelled-out board stutter | RESOLVED | Described instead (`01:241`) |
| "Scram, P.M." | RESOLVED | "Scram pulled, P. Morrow." (`prologue.md:683`) |
| "est. 200 bbl" | RESOLVED | Gone |
| "Three-thirty" as clock or run time | RESOLVED | "the three-and-a-half-minute mark" (`07:139`, `08:263`) |
| "Step" as stride and as stone step | RESOLVED | Strides are "bounds" in that passage (`04:229–231`) |
| Kiva and Kellan share "K. R." | OPEN, by lock | Still side by side on two boards (`04:37`, `05:8–11`). The names are locked. A narration note is the only remedy. |

**Ash terminology (owner ruling 7).** The manuscript is clean. Yield words carry quantity: "bigger than a Handful" (`03:267`), "the kind the yield books called a Handful" (`05:83`), "a Handful of clean ash" (`05:281`), "a Barrel yield," "a whole Barrel," "Barrel-yield spawn," "one full Barrel" (`prologue.md:843`, `:877`, `:933`). Grade carries purity only: "Grade First," "grade at Third," "Grade Second" (`prologue.md:753–771`, `05:117`). "Finer grades" in snapshot 6 became "Purer ash" (`prologue.md:499`). Resonance is not on the page.

One upstream file still carries the retired wording: `packets/MOVEMENT-002.md:46` asks for "a developed supervised Handful-grade kill." That is not manuscript and I did not touch it. Left as is, it will seed the same error into Movement Two.

**Names.** "Bram" appears nowhere in the manuscript. "Femi" appears on nineteen lines, all in snapshot 8, and matches nothing else in this repository. I did not check the research corpus outside the repository, so that half of the repair report's claim is unverified here. The T.V. and T. Vey echo is untouched (`prologue.md:291`, `:579`), as ruled.

**Rank.** The ladder in `01:27` matches the bible. No Glory figure is on stage. Kiva's frame still flickers Ember, Flame and dashes in both the prologue and chapter 1.

### 2e. Continuity checkpoint against the page

The checkpoint matches the repaired manuscript. I checked every row of its calendar, the trial clock, each character block, the world facts and the prologue notes against the lines cited above. The four entries the editorial review found wrong (3 to ½, about 9 s, about 3:39, ground-floor laundry) are all corrected.

Two rows are the checkpoint's own interpolation and sit a few seconds tight against the page. Neither is a contradiction.

- It gives 6.1, 6.2 and 6.3 at 0:50, 1:00 and 1:09. The page prints no clock for those readings. See the tolerance note in 2b.
- It gives the needle as 6.9 at release 2. The last reading on the page before the clang is 6.8 (`05:299–301`).

### 2f. New items introduced by the repair

None of these reverses a ruling. Only N1 is countable.

| # | Location | What the page says | Why it matters | Smallest fix |
|---|---|---|---|---|
| **N1** | `06:203`, against `06:171` | On the fifth step, "the stair went up seven more steps." Then he "went up two steps backward. Seven more steps of wet grating with a husk at his heels was three seconds." | Five steps remain, not seven. It sits in the paragraph where Kellan chooses on the strength of measurement, which is the trust both reviews wanted protected. "Wet" is also unsupported: the treads are slick with dry ash (`06:159`). | "Five more steps of slick grating" |
| N2 | `06:159` | "He had been holding this stair for a minute and a half." | Loose, not wrong. He has guarded its foot since about 2:00 (`05:311`), but he met release 3 away from the stair (`05:391–403`) and is first shown on the treads at release 4 (`06:33`). The frozen text said twenty seconds. | "guarding the foot of this stair" or leave |
| N3 | `06:415` | "And every number you called was right. Including the last one, from the floor." | The call from the floor (`06:149`) contains no number. | "every call" |
| N4 | `04:197` | "…in the junior lanes and thought that, seeing blade and struts and blade so quickly that it looked like one thing, and she had thought that was what being good meant." | The join made a garden path. Heard aloud, "thought that, seeing" opens a clause that never gets its verb. The frozen text was four short sentences. | Restore one full stop after "thought that." |
| N5 | `05:201` | "Perrin closed his fist on his with a face, as if it were medicine." | "On his with a face" stumbles aloud, and the medicine simile belonged to swallowing. | Reword the clause |

### 2g. Seen while checking, not from either review and not from the repair

Low priority. All five are in the frozen edition too. They are listed so nobody has to find them twice.

- **Three bounds, two paces.** Kiva drops from the rail "above the pump room door" (`06:11`), takes three Stride bounds (`06:57–59`) and lands "two paces in front of the pump room door." A reader may picture her overshooting. Rhea repeats the landing spot (`08:265`).
- **Heat-line extent.** The medic sees them "halfway to her elbow" (`06:343`). Chapters 7 and 8 say "from her breastbone to her elbow" (`07:9`, `:211`, `08:401`).
- **Orla's standing.** She sponsored Jessamy twenty-one years ago and entered him "in his second year," yet ten years suspended plus eleven restored already makes twenty-one (`03:387–393`). The sum leaves no room for the year before the trial.
- **Name echoes for narration.** A place called Corran (`prologue.md:871`) and Ilse Corran, whose name closes chapter 8's Rhea scene as "Corran's disk" (`08:319`). Tallis Street substation and Tallow substation about a hundred lines apart (`02:43`, `:145`).
- **"Sequence" as Kiva's label for the drill.** Orla says "That's a drill" (`03:273`). Kiva's book still heads the row "Sequence" (`03:329`), and she tells Mara "a full sequence takes nine and a half seconds" (`04:405`). It is in character. Given the ruling that the first true sequence belongs to Movement Three, the loose label is worth a conscious decision.

One canon note outside my scope: the bible says the disk warms after the first correct "three-door sequence" (`UNIVERSE_BIBLE.md:258`), and the book map has it warm after the first two-door sequence in Movement Three (`BOOK_MAP.md:56`). The manuscript depends on neither yet.

---

## 3. Recheck 2 — cadence and read-aloud

### 3a. Editorial metrics, reproduced

Same script, same tokenizer, run on both editions. Every figure in the editorial review and in the repair report's section 5 reproduces exactly.

| Metric (all nine files) | Target | First draft | Repaired |
|---|---|---:|---:|
| Sentences | — | 6,986 | 5,809 |
| Mean length | 14.6 | 8.30 | **10.33** |
| Median | 11 | 6 | **7** |
| Five words or fewer | 27.7% | 45.1% | **41.5%** |
| Forty words or more | 3.3% | 0.30% | **1.67%** |
| Flesch Reading Ease | 72.3 | 92.4 | **90.4** |
| Flesch-Kincaid grade | 6.8 | 2.4 | **3.2** |
| Syllables per word | about 1.41 implied | 1.254 | 1.253 |
| Paragraph median / mean | 18 / 26.8 | 15 / 25.7 | 15 / 26.6 |
| Section breaks per 10,000 words | about 8.7 | 15.0 | 14.5 |
| Kiva's share of chapters 1–8 | about 87% | 87.2% | 87.3% |

Chapters 1–8 alone: mean 8.13 → 10.03, median 6 → 6, short share 47.5% → 43.4%, long share 0.35% → 1.59%, grade 2.4 → 3.1.

**The whole-text targets are not met.** That part of the repair report is accurate.

### 3b. The narration, speech and ledger split, reproduced

The repair report asked that its split be reproduced before anyone relied on it. I rebuilt it from scratch with the same tokenizer. The rule is in the appendix.

| Slice | Share of sentences, before → after | Mean | Median | Five or fewer | Forty or more |
|---|---|---|---|---|---|
| Narration | 60.6% → 54.2% | 9.90 → **13.81** | 7 → **10** | 35.5% → **26.8%** | 0.42% → **2.95%** |
| Quoted speech, with its tag | 35.5% → 41.0% | 5.84 → 6.26 | 5 → 5 | 59.8% → 58.6% | 0.04% → 0.08% |
| Ledger and board lines | 3.9% → 4.8% | 5.82 → 5.81 | 4 → 4 | 61.9% → 61.9% | 0.74% → 0.72% |

**Reproduced.** Narration and speech match the repair report to within 0.03 words and 0.1 points. The ledger slice differs a little (the report has 5.86 → 6.15). That comes from where each rule draws the line around italic rows. It is under five percent of sentences and changes nothing.

Narration by scope after repair: prologue mean 15.19, short share 22.2%, long share 3.23%. Chapters mean 13.33, short share 28.3%, long share 2.86%. Among the chapters, the narration mean runs from 12.05 (chapter 7) to 14.32 (chapter 4).

So the narration now sits at the formula: 13.8 against 14.6, median 10 against 11, short share 26.8% against 27.7%, long share 2.95% against 3.3%.

### 3c. Why the whole-text number cannot move much further

The gap is arithmetic, not neglect.

- 59,989 words at a 14.6 mean is 4,109 sentences. Narration and ledger lines already use 3,426 of them.
- That leaves 683 sentences for all the speech, which now takes 2,383. Speech would have to average **21.8 words a sentence**. It averages 6.26.
- The short-sentence budget at target is 1,138. Narration and ledger lines already hold 1,015. That leaves room for 123 short spoken sentences. There are 1,397.

No dialogue pass that keeps these people sounding like themselves closes that. Joining two hundred spoken pairs would move the whole-text mean from 10.33 to about 10.7.

Grade behaves the same way. Narration alone reads at grade 4.4 on 1.236 syllables per word. Speech reads at 2.1. The rest of the distance to 6.8 is vocabulary, which the owner has already said not to inflate.

### 3d. How the sentences were joined, and whether hierarchy survives

- Sentences of twenty-five words or more went from 294 (4.2%) to 607 (10.4%).
- Most joins are coordinate. ", and" doubled, from 9.4 to 18.8 per thousand words. "And" is now 4.0% of all words, up from 2.9%.
- Subordination rose less: "because" 1.8 → 2.6 per thousand, "which" 0.8 → 1.3, "though" 0.2 → 0.4.
- Long sentences that are flat chains (four or more "and," no subordinating word) are 43 of 607, or 7.1%. The share was 6.8% before. The sampled chains are lists and impact sequences that suit the form: `06:43` (the cup tipping off the table), `06:91` (the hit going down through her).

Read aloud in my head, the sixteen longest sentences and a sample of fourteen chains all keep one clear main clause. The longest, at 68 words (`prologue.md:909`), hangs its list on a colon. The best joins do real work: "although probably nobody's rank would change because of it, probably was not the same as nobody" (`01:23`).

I found one join that lost its hierarchy in the full read: N4, `04:197`. I cannot claim line-edit coverage of all 607 long sentences. This was one complete read plus the samples.

One honest reservation: ", and" is now the default joint, about once every fifty-three words. It is clear and it breathes well aloud. It is also a sameness. Movement Two should reach for the subordinate clause more often than this pass did.

### 3e. Impact fragments

All present, and they land harder than before because the sentences around them are longer.

- Prologue: "Then the lights went out." "Eleven forty-seven." "The thing hit nothing." "It came apart." "The fence held." "She went."
- Chapters: "He was not fast because he stacked. He was fast because he never did." (`04:201`). "It had stopped." (`05:377`). "And she was afraid." (`05:407`). "She did not decide." (`06:47`). "The husk hit her." / "She did not move." (`06:85–93`). "The shutter dropped." (`06:121`). "Holding. Holding." (`06:131`). "He pulled." (`06:219`).
- Every chapter ending is intact: "No," said Mara. / "And I'll sign." / "She walked home with it." / "say it out loud." / "Eight and two." / "She was looking at Kiva." / "Writing it down so somebody can." / "Again."

Runs of eight or more consecutive sentences of five words or fewer fell from 22 to 13. None of the 13 is exposition. They are Kellan's role call (`05:191`), Orla's two drill lists, the results board, the register line, Kiva's quench shout, and seven fast spoken exchanges.

### 3f. The two possible overcorrections

**"looked at": 130 → 3.** Confirmed. Every form of "looked" fell from 207 to 47.

- *Do the substitutes form a new tic?* No single one does. About a hundred replacements are spread over some two dozen verbs and phrases. The largest gains are "watched" +13, "turned to" +12, "studied" +9, "eyes went/stayed" +7, "stared" +7, "glanced" +6. The rest were joined away.
- *Do they sound evasive?* Mostly not. "Marguerite studied the floor" (`prologue.md:137`) is the normal idiom for avoiding someone's eye. "Regarded it as if it might bite" (`prologue.md:1059`) and Ysra "regarded her over the ledger" (`01:269`) suit the people doing it. A handful run a register high for a thirteen-year-old's ear: "considered" five times, "weighed" four, "regarded" three.
- *What did not change.* The reviews named the default pause, not the verb, as the tic. The pause is still there with new verbs in front of it: "studied her a moment longer" (`01:123`), "considered her for a moment longer" (`04:299`), "held her eyes for a moment longer" (`04:407`), "considered that for a moment longer" (`07:135`), "weighed that for a moment longer" (`08:377`). "Moment longer" is 5 before and 5 after. "For a long moment" is 7 → 6. "For a long time" is 14 → 14.

Judgment: overshoot, as the repair report says. It is not a defect. The plain verb could come back in a dozen places at no cost. Movement Two should not be drafted under a ban on it.

**"it was not": 34 → 41.** Confirmed, and it is mostly an artifact of joining.

- Narration fragments opening "Not …" fell from 78 to 39. Those two forms together fell from 112 to 80, about 29%.
- The form changed. Most new instances are single concessive sentences: "It was not a flash, exactly, because a flash would have hurt" (`prologue.md:9`); "The knee was better, though it was not good" (`05:33`). That is the joined shape the brief asked for.
- The two-sentence pair ("It was not X. It was Y.") survives about thirteen times. Examples: `01:269`, `03:403`, `04:199`, `06:407`.
- One audible cluster. Kellan's cutaway has five in about five hundred words (`04:329`, `:337`, `:339`, `:343`, `:353`). Chapter 4 carries eleven of the forty-one.

Judgment: not a new movement-wide tic, and not evasive. The Kellan cluster is the one place a listener would hear it. Two of the five could go.

### 3g. Dialogue as prose

Numbers first, then the ear.

- 874 spoken turns. Median six quoted words. 29% of turns are three words or fewer. 19% are twenty-five words or more.
- Sentences inside quotation marks average 6.4 words. 58% are five words or fewer. 35% are three or fewer. All of that is essentially unchanged from the first draft.
- Speech tags do not drum. 49% of turns carry "said." No stretch has four consecutive paragraphs each carrying it. The longest is three. 83 turns (9.5%) are three words or fewer hung on a bare "said X."
- Turn length separates the cast. This table uses tag-attributed turns only, about a fifth of chapter turns, so it is directional.

| Speaker | Turns | Words per turn | Words per spoken sentence | Spoken sentences of three words or fewer |
|---|---:|---:|---:|---:|
| Ysra | 16 | 41.8 | 9.8 | 16% |
| Mara | 31 | 30.4 | 8.3 | 26% |
| Orla | 41 | 19.1 | 6.4 | 37% |
| Perrin | 17 | 17.3 | 7.3 | 30% |
| Kellan | 9 | 10.3 | 7.2 | 31% |
| Anwen | 22 | 9.5 | 5.6 | 43% |
| Kiva | 37 | 7.8 | 5.3 | 33% |

By ear, the short speech is doing dramatic work. The license scene (`07:343–401`) is two people who love each other choosing very few words. The office scene sets Ysra's long procedural periods against Orla's "Twenty-one" (`08:97`). The corridor argument (`05:129–199`) is quick because it is an argument on a clock. Shortness is not uniform across speakers. It is the default for Kiva and Anwen and the exception for Ysra and Mara. That is characterization.

Three habits do cross every voice. None is new, and none was moved by the repair.

- **The echo reply.** One speaker confirms by repeating the other: "He's rushing." / "He's rushing." (`02:63–65`); "Thinks." / "Thinks." (`07:45–47`); "Every lamp." / "Every lamp." (`07:297–299`); "Like a fever." (`07:305–307`); "This is the household." (`07:383–385`). Fifteen by a strict count, before and after. The ear finds more, because the strict count misses tagged repeats such as "It's creeping up." (`02:223–225`). Four fall inside ninety lines of chapter 7 (`07:297–385`).
- **"I know."** as a whole reply: sixteen times, spread across the cast and the prologue.
- **The full-stop list at an emotional peak.** Mara: "Not Orla. Not your team. Not that boy with the steady eyes. Not the gallery." (`04:415`). Perrin, Anwen, Orla and Kiva do it too.

### 3h. Is the remaining gap a concrete audible defect that justifies a second, dialogue-focused repair?

**No.**

- The audible problem both reviews described was constant emphasis: fragments carrying exposition, backstory and transition. That is fixed where it lived, in the narration.
- What remains is that these people speak briefly, and that speech is 41% of the sentences but only about a quarter of the words. Read as prose, it is intentional, it varies by speaker, and it never runs long enough unbroken to become a drone.
- A dialogue pass could not close the formula gap (3c). It could move the mean by about 0.4 words, at real risk to the voices Priority 3 just separated.
- Formula distance alone is not grounds, by the owner's rule.

Because the answer is no, I give no repair scope. The three shared habits in 3g, the ", and" joint, the timed pause and the plain "looked at" are better handled as drafting guidance for Movement Two than as another pass over Movement One.

---

## 4. Recheck 3 — voice, revelation and aftermath

### 4a. The six principal voices

I cannot do a blind test on text I have just read with the names attached. What I can report is whether each person has a way of being honest that nobody else uses, and whether the shared idioms the editorial review listed are gone.

**The shared idioms.**

| Idiom | First draft | Repaired |
|---|---|---|
| "I want it said" / "I want that said" | Anwen ×2, Perrin, Mara | **Anwen only**, ×3 (`01:381`, `06:459`, `08:341`). Kiva's "It's said" answers her each time. |
| "I'm not saying X. I'm saying Y." | 15 uses across Ysra, Mara, Kellan, Anwen | Gone as a frame. Four "I'm saying" remain: Kiva's shout (`05:359`) and Mara's "I'm saying it out loud" lines (`07:401`, `08:219`). |
| "Not a good reason. The true one." | Orla ×2 | Gone |
| "Like Anwen does" / "what Anwen would do" | Perrin ×2 | Gone |

**Each voice now.**

| Person | Their way of being honest | Lines that could be nobody else |
|---|---|---|
| **Anwen** | States the uncomfortable fact, then files it. Lists, counts. | "I'm going to ask them to count. It's different." (`01:59`). "The score first. Then the legs. I'd like to say it the other way round. I can't, honestly." (`07:103`). "I'm not angry with you. I want that said, so you don't spend the week guessing." (`08:341`). |
| **Mara** | Makes you say it aloud, and holds herself to the same rule. Bench similes. | "I sign forms because they're true or I don't sign them." (`02:19`). "I'd like you to be a little uncomfortable." (`02:255`). "So I'm saying it out loud, here, before I sign anything, and you can decide what my signature's worth." (`08:219`). |
| **Ysra** | Procedure as candor: file, items, record, standing. Long periods. | "The file is what I am permitted to rule on. Item one …" (`01:305`). "That is outside my office … I have no standing there." (`08:29`). "I want that on the record of this meeting." (`08:69`). |
| **Kellan** | Rates and columns. No softening and no malice. | "That's a rate, not an insult." (`04:311`). "I've got one column that says you broke the run and one that says I'd have been wrong without you. They don't add." (`06:415`). "It's a number. It's on the board. I know where you are." (`08:361`). |
| **Perrin** | Jokes first. The joke fails and he says the true thing anyway. | "I'm observing with my whole heart and a small amount of bitterness." (`01:355`). "It's just that the joke keeps coming out jealous." (`03:321`). "It's just the jealous left." (`07:197`). |
| **Orla** | Field stories, reluctantly, with herself as the fool. | "Every time I teach something, it's a ceremony. Ask anyone." (`03:7`). "I had a ward-holder on the Ferren levee once … Both entries. I'm not going to pick one." (`07:29`). "I'm the fool in most of them. This is the one I never told." (`08:107`). |

**Distinguishable: yes.** The six no longer share a syntax for candor. The table in 3g shows they do not share a length either.

Two things to watch. Neither is a defect.

- **Perrin's new device is close to a formula.** Three times he reports a joke the reader does not hear: "I had a joke ready instead" (`05:23`), "the joke keeps coming out jealous" (`03:321`), "I had a whole joke … and it's gone" (`07:197`). Three is the limit. In Movement Two, let one joke be heard failing.
- **One conclusion in four mouths.** In chapters 6 and 7, Anwen ("You did both," `06:455`), Kellan (two columns), Orla ("Both entries") and Perrin ("Both, at once," `07:197`) all land on "two things are true." Each uses a private vocabulary, so it reads as theme and not as one author. It is where the voices sit closest.

### 4b. Jessamy Hart

- **Chapter 2** carries only the shape. "Somebody I thought I understood. And it went wrong, and what happened to my name afterward was nothing compared to what happened to the student." (`02:307`). No name, no sex, no injury.
- **Chapter 3** gives the name, twin-kindled Ember and hand, the Brickfields, a Circuit trial in his second year, and then stops on purpose: "She did not let herself go through the rest." (`03:387–391`). It keeps the sealed file, his leaving at nineteen, the letter never written, the ten and eleven years, and the unsigned second page (`03:421`).
- **Chapter 8** delivers, for the first time anywhere: the ashcraft trial at the Regional, four thousand people, the cell running away, the lost hand, two students burned pulling him clear, one hand and no category, pumps on the south coast (`08:107`).

**Confirmed.** The concrete history is revealed once, at the sponsorship scene, to the person it is for. Three small facts are heard twice (sealed file, left at nineteen, never wrote). That is fair: they are what Orla could bear to think in chapter 3. The confession now carries new information, and "That's why it counts" (`08:123`) lands on it.

### 4c. Aftermath scenes

No scene was removed. Each keeps the judgment that belongs to its speaker. The shared beat list is gone from the four places it was heaviest. I compared each against the frozen text.

| Scene | Unique judgment kept | Retelling |
|---|---|---|
| Kellan after the board (`06:405–421`) | "That's what a card is for. It tells me where to stand." Two columns that do not add. | The frozen "And then you went over the rail … And held a husk … And called the quench" chain is gone. |
| Anwen with the card (`06:449–463`) | "I chose the casualty … I want that said." | None |
| Ysra at the glass (`06:467–473`) | Hand on the master stop, not pulled | None |
| Orla on the tram (`07:11–29`) | Best single-door work she has seen; the landing was a jam and is not to be tried again; "Both entries." | The frozen seven-clause "And … And … And" walk-through is gone. Two beats remain as the ground for her verdict. |
| Mara on the step (`07:51–67`) | "Did you say it out loud?" / "Was there time to say two words?" | None |
| Anwen and Mace (`07:79–135`) | "The score first." "She's always trying to fix the thing in front of her." | One line of setup |
| Perrin and the dumplings (`07:165–205`) | "Exceptional." "Nobody's ever seen me do anything." "Say so first." | None |
| Ysra's office (`08:33–89`) | "I don't need it told to me again. I need two things the board can't give me." Why she did not pull the stop. The lowest defensible place. | The frozen question-by-question replay is gone. |
| Rhea's plate (`08:257–319`) | The left hand that came up and threw no ward. "Responder." Both cards. | Still walks rail, stance, hand, call in order. Reviewing the plate is the scene's premise, and each beat carries a reading only she could give. |
| Kellan at the rosters (`08:347–377`) | "I'll be comparing." The fingers as "a number that was still moving." | None |

**Confirmed.** Everything the brief said to preserve is present: Ysra's hand on the stop, "responder," Rhea noticing the left hand, both cards, and every consequence.

### 4d. Prologue endings

| # | Snapshot | Closes on | Record present in the scene |
|---|---|---|---|
| 1 | Night of the Fall | "But I wrote down what we saw." | Closing line |
| 2 | Machine Book | "If I don't write the why, they'll make one up." | Closing line |
| 3 | The Tear | Aud Fenn's written record | Closing passage |
| 4 | The Copy | "Now you're in two places." | Closing line |
| **5** | Rotation | **Image:** the camp at dusk and the panel she did not open (`:451–453`) | Abel's entry, earlier (`:441`) |
| 6 | The Weir | "Begin tomorrow." | Closing line |
| 7 | Commissioning | "…began with the same three words." | Closing line |
| **8** | First Light | **Image:** one small yellow light on this side of the water (`:825`) | License-book entry, earlier (`:817–821`) |
| **9** | The Haul | **Image:** the girl and the dog watching their roof get smaller (`:951`) | Company-book entry, earlier (`:933–937`) |
| 10 | Superseded Stacks | The card in the drawer | Closing line |
| 11 | Three Doors | The crooked post | — |

**Confirmed.** Three endings were varied, and they are exactly the three that used to close on an italic *Why* line. The ledger is still written in all three scenes. It no longer has the last word every time. No snapshot ends on a thesis line. All eleven snapshots remain, and the prologue still ends on the post.

Snapshot lengths are 1,069; 986; 1,266; 968; 1,759; 1,800; 1,372; 1,677; 1,510; 1,248; 2,887. Four exceed the plan's 900–1,600 guide. The total of 16,542 is inside the 11,000–17,000 range.

---

## 5. The nine accepted owner decisions, checked on the page

| # | Decision | On the page | Note |
|---|---|---|---|
| 1 | Ysra may set aside her Classification Day condition in writing, with authority and evidence clear | **Authority:** "That condition is mine to enforce and mine to set aside, and if I set it aside, the rules require me to write down why." (`08:73`). The condition was hers and on a form she signed (`01:327–329`). **Evidence:** the field book, "a record I can rule on" (`08:77–81`). The run is still ruled a failure (`08:69`). | Verified. The page states the duty to write the reason and gives the reason aloud. It does not show her writing it or say "I set it aside" in so many words. If "in writing" is meant literally, one clause closes it. |
| 2 | Keep the dram-spent board line | `06:391`: Renn 0.41, Pryce 0.55, Cade 0.93, Rowan 0.96, no overspend | Consistent with one standard dram each and with the ring figures (0.31 and 0.88). |
| 3 | Four-hundred-person gallery | Five places, all four hundred | No stray larger figure remains. |
| 4 | One-Barrel lost yield | `prologue.md:877`, `:933` | Consistent with the yield ladder. |
| 5 | Chapter 6 overlap is a failed, unrepeatable jam | "It was not a hand-off … two doors jammed against each other" (`06:75`). "She did not think she could do even that again on purpose" (`06:333`). Orla: "You couldn't do it again if I paid you, and you're not to try" (`07:25`). Rhea: "Not a hand-off, and not to be expected twice" (`08:313`). | Verified in four places. The feat (standing a husk off Perrin with the hand door shut) is intact. The disk stays cold. |
| 6 | Transient entries stay; Kiva must not know an earlier dream existed | All three entries and the margin note stay (`08:163`, `:177–183`). Kiva: "There was nothing in either of the old books about a sky, or about people … She did not know whether the lamps had anything to do with a dream at all, hers or anybody's." (`08:195`). *Why: unknown.* | Verified: she does not know and does not conclude. The two words "or anybody's" are the one place the idea of another dreamer crosses her mind, and there it is stated as not known. If the link is meant to be the reader's alone, cutting those two words does it. |
| 7 | Finger dullness is temporary and recovering | Medic: "most of the rest over a week or two … Next time it might not" (`06:369`). Prickling at 02:44 (`07:285`). "A bit. It's coming back." (`07:335`). "Thin gloves" (`08:5`). "More each day." (`08:373–375`). "Two half-woken fingers" (`08:419`). | Verified. The warning is planted. The loss is not spent. |
| 8 | Formula POV applies to chapters 1–48 | Kiva holds 87.3% of chapters 1–8. Cutaways: Kellan 4.2%, Rhea 2.8%, Anwen 2.3%, Orla 2.0%, Mara 1.4%. | All six cutaway guards in the script pass. |
| 9 | Snapshot 4 stays 2152; T.V. and T. Vey unresolved | `prologue.md:263`, `:291`, `:579` | Untouched. |

---

## 6. Limits and uncertainty

- Same model, informed. See section 0. The arithmetic, calendar and count findings are the reliable part, because each can be checked against a cited line. The read-aloud judgments are the least reliable. No audio was rendered, and "by ear" here means read silently with attention to stress.
- The clock in 2b assigns times the page does not print. Another careful reader could shift the middle rows by several seconds either way. The five printed values and every stated interval are honored.
- Geometry rests on the stair rising east along the south wall. The page states the wall and the rail side and implies the direction.
- The split in 3b is my own implementation of the repair report's idea. It reproduces the report's narration and speech figures. It is not the report's code.
- The per-speaker table in 3g uses only tag-attributed turns. Kellan's row is nine turns.
- I did not re-score the two reader lenses. The prompt asked for the three priorities and the changed joins only.
- Section 2g lists what I happened to see. It is not a fresh full continuity audit.

---

## Appendix — method

**Environment.** Python 3.14.6, standard library only, read-only against both editions. Scripts were written to a scratch folder outside the repository.

**Editorial script.** Extracted from the appendix of `editor/MOVEMENT-001-EDITORIAL.md`, hash verified, and run twice:

```
python3 metrics.py books/book-2680-opening/editions/movement-001-pre-repair
python3 metrics.py books/book-2680-opening
```

**Split rule (3b).** For each paragraph, before emphasis markers are stripped:

1. If every line of the paragraph is wholly italic, or is an italic-labelled field-book row (`*Why:* text`), all of its sentences are **ledger**.
2. Otherwise tokenize the paragraph with the editorial script's own `sentences()`. Walk the sentences in order, tracking whether a double quote is open. A sentence that contains a double quote, or that starts while one is open, is **speech**. Its tag counts with it, as in the editorial tokenizer.
3. Everything else is **narration**.

```python
whole_it = all(re.fullmatch(r'\*[^*].*\*', l) for l in lines)
label_it = all(re.match(r'\*[^*]+:\*\s', l) or re.fullmatch(r'\*[^*].*\*', l) for l in lines)
if whole_it or label_it:
    out['ledger'] += sents
else:
    inq = False
    for s in sents:
        n = len(re.findall(r'["“”]', s))
        out['speech' if (inq or n) else 'narration'].append(s)
        if n % 2:
            inq = not inq
```

**Other counts.**

- *Staccato runs (3e):* consecutive sentences of five words or fewer within one section, same tokenizer.
- *Spoken turns (3g):* paragraphs containing a double-quoted span; length is the word count inside the quotes.
- *Echo reply:* a turn of eight words or fewer whose text equals, begins or ends the previous turn's text.
- *Tagged turn:* a turn whose words outside the quotes include "said."
- *Per-speaker rows:* turns whose words outside the quotes name exactly one of the principals with a speech verb.
- *Joins (3d):* counts of ", and" and of listed subordinating words per thousand words. A flat chain is a sentence of twenty-five words or more with four or more "and" and none of because, while, when, which, although, though, until, so that, as if, since, where.
- *Gaze verbs (3f):* case-insensitive regex counts over both editions.

**Not captured by any script.** The clock and geometry reconstructions, every RESOLVED, PARTIAL or OPEN status, the voice table, the aftermath table and all read-aloud judgments are readings of the page. Each is cited by line.
