# Kindling 2680, Book One — Movement Two (chapters 9–16) — editorial review

Reviewed: 2026-10-10. Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), one session, no subagents.

Status: review only. No manuscript, canon, planning, ledger or provenance file was changed. This report is the only file written. Nothing was committed.

---

## 0. What kind of read this is

**An informed, same-model editorial review. It is not a blind cold read, not a real human read, and not independent testing.**

- The chapters were drafted by an Opus 5.5 seat in this worktree. I am the same model. I do not have the drafting transcript in context.
- I was given the movement packet, the bible, the book map, the state ledger and both continuity checkpoints before judging. The Movement Two checkpoint was written by the drafting author straight after the run. Agreement with it is weak evidence. Disagreement is the more useful signal, and in two places (C1 and C5 below) the checkpoint repeats a slip that is on the page.
- I read the compiled prompt `editor/MOVEMENT-002-EDITORIAL.prompt.md` from line 1 to line 4960, all eight chapters in order before scoring anything.

### Coverage

Eight files, complete, in declared order. The chapter text embedded in the prompt is identical to the files on disk (checked by diff).

| File | SHA-256 (first 16) | Words (regex count) | Sections |
|---|---|---:|---:|
| `manuscript/chapter-09.md` | 36f95ac80704ff59 | 6,578 | 10 |
| `manuscript/chapter-10.md` | 1692c3cc9ed46476 | 6,720 | 8 |
| `manuscript/chapter-11.md` | bef52075d57e1c72 | 5,925 | 9 |
| `manuscript/chapter-12.md` | 0735eea9d597f8af | 6,078 | 9 |
| `manuscript/chapter-13.md` | 4f10f761954b1687 | 7,426 | 11 |
| `manuscript/chapter-14.md` | 3e8d7c52c8026827 | 6,700 | 8 |
| `manuscript/chapter-15.md` | 89370fe924378129 | 5,464 | 7 |
| `manuscript/chapter-16.md` | 959ae5a4fa5b366f | 7,008 | 9 |
| Movement Two | | 51,899 | 71 |

A file named `editor/MOVEMENT-002-COLD-READ.md` appeared in the editor folder while this review was running. Another process wrote it. I did not open it, so nothing here is drawn from it or checked against it.

Not covered as prose: the prologue and chapters 1–8. I used them three ways only: through `provenance/MOVEMENT-001-CONTINUITY.md`; through four targeted line lookups (`chapter-08.md:85`, `chapter-01.md:207–211`, `chapter-06.md:475`, `chapter-07.md:137–151`); and as a second input to the metrics script so the two movements are measured the same way.

Locations are `chapter:line` in the manuscript files, with line 1 the chapter title. `13:365` means `manuscript/chapter-13.md`, line 365. Canon evidence is cited only from what the prompt supplied.

---

## 1. Verdict in brief

**Keep reading. This movement does what its packet asked, and the idea at its centre is the freshest thing in the book so far.** The hero's first license is to kneel beside a dead monster, open nothing, and pick up what is left before a clock runs out. Every later scene tests that one skill against a new pressure, and then chapter 15 turns the skill into the weakness a human opponent reads and uses.

It is also a much cleaner draft than Movement One's first draft was. I rebuilt the calendar, both event clocks, the meet score, the dram ledger, the share arithmetic and the hold-post readings from the page. Almost all of it agrees with itself (section 4b).

Three bounded repairs:

1. **A short list of days, counts and rules that do not agree.** About fifteen located lines. One of them is a plain timeline error (Kiva tells Orla on Friday two things that happen on Saturday).
2. **The school never pushes back, and the adults share one voice.** Jude says half the school is angry or frightened. After the first scene, nobody on the page is either. Six different adults answer Kiva with the same dry "Hm."
3. **The "strong year / dirty spring" pairing is laid side by side three times, each with a narrator's nudge that the two are unconnected.** The packet asked for one concrete sign. Chapter 14 carries most of the weight and is the one place the pace slackens.

Whole-text sentence targets are missed by the same margin and for the same reason as in repaired Movement One. Narration alone is near the formula. That is a carried owner decision, not a new repair (sections 5a and 7).

---

## 2. Unscored reader response

**Where interest caught.**

- `09:3–31`. A quench box at her peg, tagged *For emergencies*. An insult made of an object, and an immediate choice about it. I cared before anything was explained.
- `09:141–185`. Druce's demonstration. The thread of ash leaning toward a lamp with no draft in the room is the image that makes every later scene legible.
- `10:231`. "Left ribs." She calls the blow without meaning to and the door stays shut. A discovery, not a lesson.
- `11:209–227`. Orla does not kill the husk. She holds it off and watches Kiva. Then the door that comes for Kiva is the one that "felt like being good." This is the best page in the movement.
- `12:91–129`. The warm tin in a cold room. Kellan did the best thing he knew and it cost the whole yield.
- `12:185`. "What do you do? For the sixty." The best blade in his year asks the provisional Third how to stand still.
- `12:439–441`. "The bell had rung. And Anwen was coming down."
- `13:135–155`. Selka Dray's lovely four seconds end in a stopped pump and an old woman saying "There now."
- `13:375–395`. "Stay dark. Kellan. Count." Then Perrin: "You're being rescued. I said I'd like to be told."
- `14:129–133`. Three and nine-tenths drams "would have fitted in an egg cup," and it is the first ash she has not been afraid of.
- `15:103–111` and `15:259–277`. Her hands let go when a body kneels beside her. Then Brask hands Jude a point so that it will happen again.
- `16:61` and `16:105`. Jude turns the offered point down. "You didn't look."

**Where it slipped.**

- `14:222–270`. Noa alone in a corridor with forty summary sheets. It is the longest cutaway in the movement, nothing moves in it, and it is where I first felt the author arranging evidence for me.
- `16:317–321` and `16:439–443`. The same two facts are set next to each other again, twice, with a remark each time that they are unrelated. By the third I was ahead of every character and waiting.
- The middle of the movement has less interpersonal pressure than chapter 9 promises. "Everything's Saturday" (`09:305`) sets three clocks. Kellan stays one chapter later (`10:447`). Orla signs three days before the bell (`11:325`, `12:439`), so Anwen's hard choice never has to be made. What replaces that tension is procedural, and it is good, but I noticed the change.
- Small stumbles that sent me back a line: `10:419` ("She told her"), `13:365` ("Agnes Roake's cloth"), `16:15` ("sixteen paces").

**Which person matters.** Kiva, without competition. Kellan is the one who changes most. Perrin is the one I would miss most.

**What I expect next.** Mara's hearing on the 9th. A Flask qualifier in three weeks with Kiva still certified only to kneel. Noa's nineteen more readings. Rhea Sorn deciding to speak. The first real two-door hand-off, now that Kiva has felt one across two people.

**Would I continue?** Yes, at once.

---

## 3. Scored dimensions, two lenses

Anchors: 5 = understandable but inconsistent; 7 = engaging with located weaknesses; 9 = compelling with few substantial distractions. These are editorial judgments by one reviewer, not measurements. The two lenses are not averaged and no sales inference is drawn.

### 3a. Fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 8 | `09:3–31` | A mean present on her first day and a captain who asks if she wants it. No explanation needed. | High |
| Keep reading | 8 | `12:441`; `15:381`; `16:517`; dip at `14:222–368` | Chapter ends pull hard ("Rowan. Still." / "Orla. Count."). Chapter 14 is mostly people at tables. | High |
| Interest / freshness | 8 | `09:211–229`; `11:259`; `12:7` | Ash that listens; sandbags called Donny, Gerald and Old Tom. | High |
| Clarity / flow | 7 | `09:193–203`; `14:115–119`; `16:233–283` | Rules are taught before they are used. But drams, tenths, hundredths, holds, counts and shares pile up in chapters 14–16, and this reader will skim them. | Medium |
| Character attachment | 9 | `13:385`; `12:185`; `10:433–437` | Perrin standing in the line; Kellan asking for help; Kiva being glad for Anwen first. | High |
| Humor / warmth | 9 | `09:99`; `10:165`; `13:263–267`; `13:339`; `14:330` | "Down people don't have opinions." "It's so wet it's nearly soup." The jokes belong to the people who make them. | High |
| Action / suspense | 8 | `13:283–417`; `15:189–277`; `16:69–109` | Every set piece can be followed move by move. The husks themselves are not very frightening. | Medium |
| Progression payoff | 9 | `09:239` → `11:309` → `12:83` → `13:449`; `11:117` → `16:483` | Count 94, then 71, then sealed at 49, 44 and 51 in a field. The drill falls from 9.5 to 8.4. Every gain has a number she earned. | High |
| Connection | 8 | `09:183`; `13:51–55`; `14:306` → `16:119` | Old lines come back with meaning: the salted tin from the trial, the mast Mara left alone, "lean under it" passed from Anwen to Kiva to Pru. | High |
| Read-aloud quality | 7 | `13:357–417`; `10:419`; `14:145–150` | Counting aloud is a gift to a narrator. Decimal boards and a few loose pronouns are not. | Medium |

### 3b. Adult genre reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 8 | `09:3–51` | Jude's plain account of his own ceiling, and his question ("what you won't do"), set the movement's ethic in one page. | High |
| Keep reading | 7 | `09:305` → `10:447` → `11:343`; `14:222–368` | The three Saturday clocks resolve early and at no cost to Kiva. Chapter 14 after the license-day climax is the slack point. The meet restores full pull. | Medium |
| Interest / freshness | 9 | `11:209–227`; `13:135–183`; `15:103–111`; `14:43–65` | Recovery as the heroic act. A perfect kill that fouls a pump. A training scar read by a teacher. For progression fantasy this is new ground. | High |
| Clarity / flow | 7 | section 4a | Clear on one pass. On a second, about fifteen lines do not agree with their neighbours. Far fewer than Movement One's first draft. | High |
| Character attachment | 8 | `12:133–201`; `15:147–185`; `14:139–218` | The cutaways earn their place and the kitchen vote is adult-grade. Deduction: everyone is scrupulously honest about their motives in much the same words (Priority 2). | Medium |
| Humor / warmth | 8 | `12:233`; `13:131`; `16:61` | Wider than Movement One. Pru, Druce and Agnes Roake carry some of it now. The warmth edges toward cosiness because no one is unkind for long. | Medium |
| Action / suspense | 8 | `13:357–417`; `15:189–277` | The meet is the best fight in the book: both sides adapt, and the decisive move is a refusal. Deduction: no husk hurts anyone who did not choose it, and an adult is always at the lever. | Medium |
| Progression payoff | 9 | `15:321–335`; `16:233–287`; `16:463–473` | Capability is priced and, in chapter 15, turned against her. "A door she had shut cleanly was a door that was resting" is measured, hedged and left unproved. | High |
| Connection | 8 | `13:29–71`; `16:463`; C1, C10, C11 | Plants pay off across both movements. Deductions for the Friday/Saturday slip, Orla's unpaid second condition and Team Eleven vanishing. | High |
| Read-aloud quality | 7 | `10:53` → `16:431`; section 5g | Narration is near the formula and the long sentences hold. "Said" at 96 per 10,000 words and a chorus of "Hm" are audible. | Medium |

---

## 4. Canon, state, power, knowledge and reserved disclosures

Summary: **no contradiction of locked canon found.** Every item in 4a is internal to the manuscript or between the manuscript and its own checkpoint, except C6, which touches a condition set on the page in Movement One. Plan-adherence observations are kept apart in 4f.

### 4a. Inconsistencies

| ID | Location | On the page | Against | Confidence |
|---|---|---|---|---|
| C1 | `11:67` | Orla sent word "on Friday." "Kiva had gone early **that night** to tell her about the fourth condition, and about Anwen's bell, and about Kellan staying." | Anwen's posting is Saturday at nine (`10:361`). Kellan announces he stays on Saturday at noon (`10:447`). Chapter 10 ends that Saturday with "She would tell Orla tonight" (`10:467`). `11:77` itself puts "the news from the Cellhouse steps" on Saturday. The checkpoint's Fri 19th row repeats the error. | High |
| C2 | `13:411` | The Home Line kills the second husk "against the silver wall," and Bettan is "on her knees beneath it with a cloth already spread." | Druce's first rule: inside the count and inside three paces "nothing is lit. Not an Edge, not a ward, not a stance" (`09:199`). Open ash "will take the first pattern that touches it" (`09:155`). A lit hold wall is a ward. The experts break the rule the movement has spent five chapters teaching, and nothing says the wall dropped. | Medium |
| C3 | `16:421` | Ysra reads Noa's sheet: still-door draw "across four minutes under load, nought point nine three." | The board shows 0.87 → 0.98 for carry three (`15:309`, `16:181`) and Kellan reads it as "eleven hundredths in four minutes" (`16:335`). In the Low Lane, nine hundredths in four minutes was "somewhere near nine-tenths" against a book figure of "about a tenth" (`11:23–27`). By that conversion eleven hundredths is about 1.1, above standard, not below it. No line says the figure is corrected for three people pulling. Kellan, of all readers, would catch this. | Medium |
| C4 | `16:15` | Third carry: "Kiva walked to the foot of her own porch. She had sixteen paces to go." | "You begin on your own porch" (`15:43`). The foot of her own porch is two steps down. Sixteen paces is the distance to the litter in carry one (`15:79`). | Medium |
| C5 | `13:77`, `13:135`, `13:465` | "Fourteen teams had mustered … and a fifteenth with one new face." Nineteen goes "thirteenth of fourteen." Vane: "I've had fourteen." | Positions 27–40 already hold fourteen teams. Nineteen was "put back to thirty-ninth" and Seven is "still fortieth" (`12:161`). That makes fifteen, or it silently drops one. The checkpoint asserts the same count. | High on the arithmetic; low severity |
| C6 | `09:283`, `11:325` | "You can't go on a live floor until Dane signs." Orla certifies "live work." | Ysra's condition as spoken in Movement One: "No **live-cell events** until your sponsor certifies you in writing" (`chapter-08.md:85`). A Kennel floor and a tear over a potato bed are not live-cell events by those words. The whole movement's engine rests on the wider reading and no line makes the bridge. The packet itself slides between "live-cell work" and "live work." | Medium |
| C7 | `13:83–87` | Kiva logs the third group's first three teams as "T27," "T28," "T29." | "The order had nothing to do with the numbers the teams wore" (`09:105`). Team Nineteen also happens to stand nineteenth (`09:277`) and Team Eleven eleventh (`10:389`). Five coincidences read as a slip. | Medium; low severity |
| C8 | `10:5` | "There were eleven of them, one from each team that had not yet been called." | On that Wednesday twenty-eight teams had not been called (`09:105–109`). The Kennel plainly runs sections of eleven or twelve teams ("about fifty first-years," `09:97`; "eleven teams were flooring," `12:207`). The clause overstates. | High; low severity |
| C9 | `13:365` | The second husk's line "ran across the middle of **Agnes Roake's cloth**." | The cloth is Team Seven's (the Stonehand spare, `13:209`). Agnes Roake owns the plot, the shed, the bed and the bean poles (`13:123`). | High |
| C10 | `10:279`, `11:327` | Orla's written condition two: "Six seals of six, sound, with the bad hand, called and checked." The certificate cites only the tin record and the sponsor's floor. | Orla is the character who will not sign for what she hopes. She wrote three conditions and the page shows two met. Kiva seals three on the floor (`11:281–289`). | Medium |
| C11 | `13:67`, `13:103`, `13:165` | Seven is the "last slot," yet "Seven, Eleven" have both not been in, and Eleven sits waiting "with their Wren House reserve." | Eleven's floor is never shown or mentioned again. The tear throws an early husk at 4:33 and the closing crew arrives at 5:30. The reader has tracked that seat since `10:389` as Anwen's other road. | Medium; low severity |
| C12 | `14:107` | Aske, on Monday: "the catcher herself walks in with four drams of it." | The team share (3.9) is not worked out until Tuesday (`14:111–119`). On Monday the team's yield is 20.8. | Medium; low severity |
| C13 | `13:305` | Anwen "held its eyes." | A husk has "no face" (`09:123`) and "doesn't see. It reads" (`09:131`). A figure of speech that argues with the anatomy lesson. | High; low severity |
| C14 | `11:5`, `12:7` | "Every school in the Compact had a dozen of them." Then Perrin: "The Hall has four hundred of them." | Possibly Perrin exaggerating. Nothing marks it. | Low |
| C15 | `09:37`, `16:237` | Jude: "six and a half on a good day." Noa: "You were six and six at the Hall in the spring." | A tenth apart, and the measured figure is above his "good day." | Low |

Two smaller questions, not counted as findings:

- `15:21` against `10:435`. Kiva has lived beside a poster of Rhea Sorn for six years and has now seen the white streak twice. She still thinks only "a Graywater officer." Either she knows the name or the poster line needs a reason she does not connect them.
- `12:135`. Kellan stands over the trough with "twenty-one drams of ash" while holding the first of four six-dram tins. Reads as the whole yield for a moment.

### 4b. Checked and consistent

These were rebuilt from the page and hold. They are listed because they are a strength to protect during repair.

- **Calendar, Tue 16th to Mon 6th, on a thirty-day month.** Every weekday and date I could test agrees, including the relative ones: "six days ago" (`09:45`), "eleven days ago" (`12:129`), "ten days ago" (`12:83`), "the Wednesday before last" (`12:247`), "twelve days ago" (`15:231`), "Saturday week. The fourth" (`11:61`), "a little more than three weeks ago" for the Thursday mast round (`13:31`), and live lanes "in three weeks" becoming "next week" (`09:277`, `14:156`). The only break is C1.
- **The tin drill.** Seven nights (18th–24th). Five squares running, Saturday to Wednesday (`11:77–109`). That is exactly Orla's written condition one (`10:277`) and the certificate's "seven nights' tin record" (`11:327`).
- **Yields.** Sponsor's floor: 14.6 tinned and "about 9" to sweepings make the book's 24 (`11:309`, `11:399`). Nineteen's 9 means fifteen lost (`10:45`, `12:33`). Second floor 15.3 is "under the mark by nearly five" (`12:355`).
- **License-day clock.** Mast six at ten to three, five and seven at six minutes to (`12:427`, `13:33`). Forty-minute interval "written thirteen times" fits fourteen husks (`13:357`). Nineteen's husk at 3:40, Seven's at 4:22, the early one eleven minutes later.
- **Shares.** 20.8 → 10.4 civic, 2.6 reserve, 3.9 schools, 3.9 team (`14:115–119`). That is the order in `STATE_LEDGER.md`. The spend is 0.5 + 1.0 + 1.0 + 1.4 = 3.9 (`14:198`), and 3.9 at 0.7 is "five releases and a bit" (`14:152`).
- **The meet.** Scoring every call by the referee's stated rules gives 4–2, 8–4 and 9–7, with carry three at 3–1 (`15:143`, `15:307`, `16:177–179`). "Four touches to their two" (`15:319`) and "that's five" (`16:93`) are right. The dram line runs 0.38, 0.87, 0.98, with thirteen, seven and two hundredths left (`16:23`, `16:131`, `16:275`).
- **Hold posts.** Jude 6.6 → 4.1 is "a bit more than a third." Kiva's stance 6.2 → 4.9 is "a fifth, a bit more" (`16:237`, `16:265–269`). Her Classification Day figures match `chapter-01.md:207–211` and the Movement One checkpoint (Edge eleven counts, Ward six taps and 2.6, Stance 6.2).
- **Small sums.** Forty to nineteen is "twenty-one places" (`10:447`). 2649 plus thirty-one is 2680 (`15:171`). Thirty days from the 20th (`10:381`). The drill has come down three times in a fortnight (`16:485`).

### 4c. Knowledge boundaries

All hold.

- Kiva learns nothing about the disk's origin, the filter, Annick, the T-0 entries or the name Unroofed Sky. The dream does not recur.
- Rhea's knowledge of "Corran's disk" stays in her own head (`16:325`). She does not approach.
- Hollis Vane recognises Orla's name, not the disk (`13:231`).
- Noa knows only what the tapes and public sheets show. He asks before filing (`16:219`).
- Ysra tells Kiva and Orla that two reports exist and calls them separate (`16:439–443`). No character connects them. Kiva and Orla now both hold the two facts side by side. That is allowed by the packet, and it is early (Priority 3, section 7).
- The one open question is Kiva and Rhea's name, noted under 4a.

### 4d. Power limits and physical state

All hold except C2.

- **No two-door sequence.** Kiva opens three doors at the meet, one at a time, each declared, none before the flag, and never lights a second heat-line (`15:315`, `16:205`). On the field she opens none (`13:537`). The carry-three hand-off is across two people and Orla says so in terms: "It isn't yours. Don't write it down as yours" (`16:467`).
- **The disk is cold** at each of three checks (`11:369`, `13:535`, `16:489`) and gives no guidance.
- **Fingers.** Dull, recovering, and failing once under load (`14:103`, `16:163`). Neither healed nor permanent. The Movement Five cost is intact and now better planted.
- **Other injuries carried.** Sling until Friday (`09:53`, `10:337`). Heat-lines keep their new length (`10:341–343`). The knee is in every physical scene. Perrin's hands go from bandaged to green to split again (`10:419`, `13:425`, `14:324`). Orla's knee folds on the third step (`11:237`) and is still bound on the 6th.
- **Ash rules.** Resonance is shown as what work the ash takes to, not a transferred power (`14:47–51`, `14:107`). No kill raises anyone's rank. Shares follow the ledger's order.
- **Husk behaviour** is consistent with Druce's lesson throughout: straight lines, brightest lit thing, no memory, seeks a pattern when nothing is lit (`12:273–281`, `13:269`, `13:361`).
- One soft spot beside C2: Vane says Dray "stood over it lit" (`13:175`), but in the scene she cuts "at a run" and the wind takes the ash at once (`13:141–145`). The Kennel version is where she stood lit (`10:39`).

### 4e. Reserved disclosures

All intact: the cause of the Fall, the filter theory, the Makers, the disk's origin, the first deliberate two-door sequence (Movement Three), the pre-Kiva dream fragment (Movement Four) and the permanent finger loss (Movement Five).

One pacing risk, not a breach. `BOOK_MAP.md` holds "measured proof that human potential and spawn strength are rising together" for the end of Movement Six, and gives Movement Four to Noa, Orla and Hollis pursuing "different evidence." By `16:443` the Placement Chair has both reports on one desk and has said so aloud to the protagonist. Nothing is proved. The reader has been shown the join three times (Priority 3).

### 4f. Plan adherence (not canon errors)

- **Packet, "what this movement is for": met.** Spawn anatomy, terrain, the four declared roles, the abort word, loose ash, catch, cold room, grade, comb, shares, the spend/save/return choice, a kill that is a failed response, a developed meet with a useful loss, Noa's measurements. All are in scenes, not summary.
- **Packet, "where we leave pressure": "one concrete sign" of each rising trend.** The draft gives several of each and juxtaposes them three times (Priority 3).
- **Book map, Movement Two entry pressure: Kiva "is treated as both weak and dangerous."** Shown at `09:3`, `09:63` and `11:13`, then not again (Priority 2).
- **Book map: "rivalry … develop[s] under real fear."** The fear is real in the catch scenes. The rivalry is thin: Kellan becomes an ally by `10:447`, Selka Dray never speaks to Kiva, and Lowen Brask is a courteous opponent.
- **Bible: "Riftspawn are dangerous animals or expressions, not training dummies."** A Handful here is the size of a mastiff, knocks one boy into bean poles by his own choice, and ignores anyone who is dark. The danger shown is to pumps and yields. That may be the right pitch for a first license. It is the owner's call (section 7).
- **POV, "near the established 87%": met.** Kiva holds 89.6% (section 5f).

---

## 5. Numerical formula alignment

Targets are from the formula embedded in the prompt (O'Connor 1.3.0, sections 2–6 and 8). Every observed value comes from one stdlib script that imports the Movement One script unchanged, so both movements use the same word regex, sentence tokenizer, syllable estimator, lexicons and proxies. The script and its hash are in the appendix. These numbers are kept apart from the reader scores.

### 5a. Sentence rhythm

Tokenizer: rule-based, the Movement One `sentences()` function. A line of dialogue and its lowercase tag count as one sentence.

| Metric | Target | Movement Two | Chapters 1–8 as now on disk | Chapters 1–16 |
|---|---:|---:|---:|---:|
| Mean length | 14.6 | **9.84** | 10.03 | 9.93 |
| Median | 11 | **7** | 6 | 6 |
| Population stdev | ~26 | 9.19 | 9.38 | 9.28 |
| Five words or fewer | 27.7% | **41.5%** | 43.4% | 42.4% |
| Forty words or more | 3.3% | **1.52%** | 1.59% | 1.55% |

By chapter (mean / five or fewer): 9: 11.11 / 39.2%. 10: 10.24 / 35.8%. 11: 9.81 / 43.4%. 12: 9.60 / 41.9%. 13: 9.46 / 46.4%. 14: 9.90 / 39.7%. 15: 9.95 / 40.1%. 16: 9.02 / 44.0%.

Cross-checks. A naive tokenizer gives mean 9.73 and 42.5% short, so the result does not depend on the tokenizer. The counting device is not the cause: 88 sentences are nothing but a number (1.7% of all), and removing them moves the short share only to 40.5%.

**The split that explains it.** I applied the narration / speech / ledger rule published in `editor/MOVEMENT-001-TARGETED-RECHECK.md`. As a check, it reproduces that report's chapters 1–8 narration figures exactly (13.33, 28.3%, 2.86%).

| Slice (Movement Two) | Share of sentences | Mean | Median | Five or fewer | Forty or more |
|---|---:|---:|---:|---:|---:|
| Narration | 47.8% | **12.95** | 9 | **29.0%** | **2.94%** |
| Speech (with tags) | 48.1% | 7.14 | 5 | 52.1% | 0.20% |
| Ledger and italic rows | 4.2% | 5.39 | 4 | 62.6% | 0.46% |

So narration sits close to the formula on short share and long share and about a word and a half under on the mean, a shade below repaired Movement One. Speech has grown from 42.1% of sentences to 48.1%, and words inside quotation marks from 24.3% to 32.0%. At a 14.6 mean, 51,899 words allow 3,555 sentences. Narration and ledger lines already use 2,739 of them and 869 of the 985 short ones. Speech supplies 1,320 more short sentences. No pass that keeps these people sounding like themselves closes that gap.

**Conflict reported, not papered over.** This is the same irreconcilable pairing the Movement One recheck brought to the owner: a whole-text sentence target measured on audiobook transcripts against a dialogue-forward draft. The stdev target (about 26 on a mean of 14.6) is not comparable to a typographic tokenizer at all. I do not make this a repair priority. I do report that the targets are missed (section 7, decision 1).

One piece of recheck guidance was not taken up. It asked Movement Two to "reach for the subordinate clause more often" than ", and." The joint is unchanged at one per 54 words, and listed subordinators fell slightly (10.5 per thousand words, from 11.5).

Staccato runs of five or more consecutive short sentences: 61 (Movement One, 73). Runs of eight or more: 7 (13). The longest is 15 and is a count.

### 5b. Paragraphs and section breaks

Typographic counts. The formula's figures are inferred from audio pauses and are directional only.

| Metric | Target (ASR proxy) | Movement Two |
|---|---:|---:|
| Paragraph median / mean | 18 / 26.8 words | 21 / 31.1 |
| Paragraphs of 100 words or more | — | 57 of 1,668 (four of 150 or more) |
| Section mean | ~950 words | 731 (median 729) |
| Section breaks per 10,000 words | ~8.7 | 13.7 |
| Sections under 500 words | — | 12 of 71 |

Sections run shorter and more often than the proxy. Chapter 9 has ten and chapter 13 eleven, as the checkpoint flagged. In chapter 13 the short sections are doing work, since each is a beat of the response. In chapter 9 three of the ten are one continuous lecture cut into parts (`09:117–211`).

### 5c. Readability

Syllables: heuristic vowel-group estimator from the Movement One script. Proper names and system terms are not special-cased.

| Metric | Target | Movement Two | Chapters 1–8 as now on disk |
|---|---:|---:|---:|
| Flesch Reading Ease | 72.3 | **92.2** | 90.9 |
| Flesch-Kincaid grade | 6.8 | **2.8** | 3.1 |
| Syllables per word | (about 1.41 implied) | 1.237 | 1.251 |

Material drift from the target, unchanged in kind from Movement One. About half is sentence length and half is vocabulary. The plain diction is a real strength for the younger lens and for narration. Owner decision (section 7).

### 5d. Progression vocabulary

Lexicon defined before counting. The Movement One lexicon is used unchanged. Movement Two's new system terms are counted separately so the two can be compared. Both lists are in the appendix. Density depends on the lexicon, so the comparison with the source's 58 per 10,000 is directional.

| Scope | Movement One lexicon | Movement Two additions | Combined |
|---|---:|---:|---:|
| Chapters 9–16 | 69.4 | 64.5 | 133.9 |
| Chapters 1–8 as now on disk | 137.6 | 14.3 | 151.9 |
| Chapters 1–16 | 100.5 | 41.6 | 142.1 |

Per 10,000 words. The old vocabulary (doors, ranks, Hold, Draw) has halved. A new one (Handful, catch, yield, tinned, printed, Second, Flask) has replaced it at about the same density. Chapter 14 peaks at 204.5 combined and chapter 15 is the low at 98.8.

Chapters 1–16 are the book's first third by chapter count. Teaching is dense there, as the formula's front-loading asks. **The 1.7× ratio cannot be confirmed until the middle and final thirds exist.** Provisional coverage only.

A related count: number words run at 280.7 per 10,000 in this movement against 198.4 in chapters 1–8. Nearly three words in a hundred are a number. That is the movement's method, and it is also the load named under Clarity in 3a.

### 5e. Development moments

**Regex proxy** (formula section 5 method: a reflection marker within 120 characters of a name). Lead: 23 hits, **4.4 per 10,000** against a target of 4.5. By chapter: 1, 4, 3, 1, 5, 1, 5, 3. Supporting cast, per 10,000: Orla 1.35, Perrin 1.16, Brask 0.96, Kellan 0.77, Jude 0.77, Mara 0.58, Anwen 0.58, Noa 0.58, Druce 0.58, Ysra 0.39, Rhea 0.19, Pru 0.19, Vane 0.19. Thirteen names, most inside the 0.1–0.7 band and three a little over it.

**Manually identified beats** (a reading, not a count from the script). Lead choices and realisations:

| # | Location | Beat |
|---:|---|---|
| 1 | `09:25–31` | Gives the quench box to the lane and keeps the tag. |
| 2 | `09:329–359` | Sees that Mara has read with her left hand for three years. |
| 3 | `10:23–51` | Reads the floor and the killer's feet, and predicts the fall. |
| 4 | `10:231–249` | Calls the blow, and the door stays in the doorway. |
| 5 | `10:431–437` | Is glad for Anwen before she is sorry for herself. |
| 6 | `10:465–469` | Decides not to ask Orla to hurry. |
| 7 | `11:81–101` | Works out that it is the not-counting, not the fear. |
| 8 | `11:219–227` | Shuts the door that "felt like being good." |
| 9 | `11:335–341` | Accepts the smallest certificate. |
| 10 | `12:71`; `12:121–129` | Explains away the draft, and learns to say *dark*. |
| 11 | `12:255–293` | Reads how the skin turns: "It can't face two ways." |
| 12 | `13:187–199` | Sets the mark from ground and wind. |
| 13 | `13:327–331` | Hears herself think "I can do this" and counts louder. |
| 14 | `13:375`; `13:393` | Orders Kellan dark, and keeps tinning while Perrin stands in. |
| 15 | `13:481` | Reports "curved" although she fears talking herself out of it. |
| 16 | `14:178`; `14:206` | Votes for the shelf, and refuses a meet reserve. |
| 17 | `15:321–335` | "It isn't a fight." Names both of her habits. |
| 18 | `15:353`; `16:95`; `16:149` | Declares one door, stays, and says why she cannot change. |
| 19 | `16:223` | Sets her terms for Noa. |
| 20 | `16:285–287`; `16:491`; `16:509` | A shut door rests. She has stopped asking the disk. "I can only stand on one." |

Twenty beats in 51,899 words is about 3.9 per 10,000, spread evenly, with no chapter empty and none saved for the end. That matches the formula's shape.

Supporting cast, manual: Kellan (stays `10:447`; owns the print `12:153`; asks `12:185`; sits down `13:255`; stops his hand `13:377`); Anwen (holds the seat until the bell `10:401`; calls *off* `12:269`; stands under her ward `13:207`); Perrin (the bad kit `12:229`; the line `13:385`; the plate `15:171–181`, `16:377–381`); Orla (finds her number `10:265–299`; signs small `11:339`; will not warn `14:360`); Mara (the left hand `09:333`; "you were counting" `13:519`); Noa (asks first `14:260–268`); Jude (turns Moss down `16:61`); Pru (learns to lean `14:316`). Many small beats across eight people, not one deuteragonist. Kellan has the most, and it does not crowd the lead.

### 5f. POV word share

Viewpoint segments were identified by reading every section, and are guarded in the script by the first words of each cutaway.

| Viewpoint | Section | Words | Share of Movement Two |
|---|---|---:|---:|
| Kiva | all others | 46,508 | **89.6%** |
| Noa | `14:222–270` | 1,196 | 2.3% |
| Kellan | `12:133–201` | 1,040 | 2.0% |
| Anwen | `10:361–415` | 918 | 1.8% |
| Perrin | `15:147–185` | 785 | 1.5% |
| Orla | `10:263–299` | 726 | 1.4% |
| Rhea | `16:291–327` | 726 | 1.4% |

Target for the book: about 87% lead, 13% across four or five characters at 2.5–3.7% each. Movement Two is a little lead-heavy, with six cutaways that are each smaller than the band. This reproduces the checkpoint's own figures. Across chapters 1–16: Kiva 88.6%, Kellan 3.0%, Rhea 2.0%, Anwen 2.0%, Orla 1.7%, Noa 1.25%, Perrin 0.8%, Mara 0.7%. That is seven secondary viewpoints where the formula describes four or five. Not a defect yet. It is a drift to watch (section 7).

All six cutaways open on the viewpoint character's full name, which is exactly right for audio. One seam: the section after Anwen's cutaway opens "She told her on the Cellhouse steps" (`10:419`), with two unnamed women and the viewpoint sliding back to Kiva three lines later.

### 5g. Secondary signals (use to taste; reported, not quotas)

Per 10,000 words. A suffix count is not proof that a word is an adverb.

| Signal | Source figure | Movement Two | Chapters 1–8 | Note |
|---|---:|---:|---:|---|
| Reporting verbs | ~41 | 123.9 | 115.1 | "said" alone is 96.5. 51% of spoken turns carry it. |
| Combat terms | ~22 | 44.5 | 49.0 | blade 12.3, kill 6.6, cut 6.6, bar 3.9 |
| "that" | 92.1, "tighten below" | **124.3** | 86.3 | Up by nearly half. Worth a look in any line pass. |
| just / almost / felt / seemed | 5–25 each | 2.9 / 0.6 / 9.6 / 1.2 | 10.6 / 2.8 / 15.4 / 0.7 | Lean. |
| -ly suffix words | ~161 | 42.8 | 41.0 | Top: exactly 33, nearly 18, slowly 15. |
| "like a" | — | 16.8 (87) | 9.9 | The similes are specific and domestic, and they now arrive about once every 600 words. |
| "did not" | — | 25.4 | 41.7 | Down. |
| "the way" | — | 7.3 | 16.8 | Down. |
| "Not …" narration fragments | — | 2.3 | 7.1 | Down. The Movement One habit did not come back. |
| "I know." as a whole reply | — | 4 uses | 13 uses | Down. |
| "Hm" / "Huh" as a spoken line | — | 9 uses | 1 use | Up. Priority 2. |
| "I want it said / noted / known / understood" | — | 12 uses | 3 uses | Up. Priority 2. |

For narration: written boards and lists use decimals in digits (`14:119`, `14:145–150`, `14:238`, `15:143`, `15:309`, `16:181`) while speech says "eight-tenths," "thirteen hundredths" and "nought point nine three." The page never says "zero." A narrator needs one rule for the digits.

---

## 6. Repair brief — three priorities

Same-author repair. Line-level unless stated. The developed action stays at its present length. Nothing here asks for a fight, a floor or the meet to be shortened.

### Priority 1 — Make the days, counts and rules agree with themselves

**Location.** The fifteen items in 4a. The ones a reader will feel: C1 `11:67`; C2 `13:411`; C3 `16:421`; C4 `16:15`; C9 `13:365`; C6 `09:209` or `09:283`.

**Observed issue.** One timeline error, one place where the Home Line breaks the dark-hands rule unremarked, one headline figure that does not follow from the board it is read off, and a dozen small miscounts and slips.

**Effect on the reader.** This book's promise is that numbers written down can be checked, and that checking them protects people. Kellan says so in as many words (`14:188`). A reader who takes the book at its word and checks will find C1 and C3 quickly. C2 matters most to the story. The movement's hardest-won rule is broken by its most expert characters in the same scene where Kiva is praised for keeping it.

**Proposed scope.** One sentence or less at each site. Suggested, not prescribed:

- C1: "Kiva had gone early on Saturday."
- C2: let the east wall drop for the count while its neighbours close, or put the kill three paces inside the wall. One clause.
- C3: one clause from Noa, or on his sheet, that the figure is corrected for the load on the poles. Or bring the figure into line with eleven hundredths.
- C4: she comes down two steps.
- C5: one clause for the team that is not there (not passed fit by the warden, say), or move the three counts to fifteen and the interval count with them.
- C6: one line in chapter 9 that reads the Chair's "live-cell" to cover a lattice and a held tear.
- C10: one clause in the certificate's evidence line, or one sentence on Wednesday night.
- C11: one sentence on what became of Eleven.
- C7, C8, C9, C12, C13, C14, C15: a word or a phrase each.

Afterward reconcile `provenance/MOVEMENT-002-CONTINUITY.md`, which currently repeats C1 and C5.

**Strength to preserve.** Everything in 4b. Both event clocks, the meet score, the dram line and the share sums are right. Do not disturb a figure that is not on this list.

### Priority 2 — Let the school push back, and give the adults more than one register

**Location.**

- The promise: `09:37` ("half this school is one or the other and you'll get tired of guessing which").
- The whole of what answers it: the quench box `09:3`, the mast tag `09:63`, the lane warden's manner `11:13`. After that, only memories of the box (`14:264`, `16:221`).
- "Hm" as a complete reply: Druce `10:53`; Agnes Roake `13:131`, where the narration notes "it sounded exactly like Warden Druce"; Vane `13:479`, and `13:483` "did not say *hm*"; Halloran `14:17` and `14:65`; Brask `16:109`; Ysra `16:431`. Kellan's "Huh" at `11:103` is the cousin.
- The same understated approval elsewhere: "not unkindly" at `10:407`, `13:179`, `14:125`, with `12:161`; "did not soften it" at `14:89`, `16:473`; "nearly" or "almost smiled" at `09:203`, `16:399`, `16:477`.
- The declared-motive formula: Jude `09:37`; Anwen `10:405`, `11:121`, `16:351`; Perrin `10:459`, `12:11`, `12:313`, `13:423`, `13:427`, `14:162`; Orla `11:147`; Ysra `16:403`. Close relatives in other mouths: Kellan `09:283` and `14:156`; Anwen `14:172`; Brask `15:39`; Noa `16:219`.

**Observed issue.** Two things with one root. First, every person in authority whom Kiva meets is fair, dry, sparing with praise and privately impressed. That covers the warden, the Home Line officer, the grader, the healer, the ash clerk, the Graywater officer, the referee, the opposing captain and the Chair. Six of them make the same sound. Second, nearly everyone, adult or student, states their own motives aloud and unprompted in the same scrupulous grammar. The Movement One checkpoint records "I want it said" as Anwen's. Here Perrin uses the family six times to her three, and three older characters say "I want that understood."

The second half of this is plan adherence, not a canon error. The book map's entry pressure for this movement is a school that treats Kiva as "both weak and dangerous."

**Effect on the reader.** For the adult reader the adults blur, and the world starts to feel arranged in Kiva's favour. If honesty is always met with fairness, then "one incident ends your season" stops feeling like a threat. For the younger reader there is nobody to resent after page one. With a single narrator reading every part, nine identical "Hm"s will be heard as one person.

**Proposed scope.**

- Re-voice four or five of the nine "Hm"s so the sound belongs to Druce and at most one other. The `13:131` and `13:483` jokes can stay if the pool is that small.
- Keep Anwen's three. Keep the `13:427` exchange with "It's said," which is a deliberate call and response and lands. Give Perrin his own comic formula at three or four of his other five. Vary at least one of the three "I want that understood."
- Put the angry or frightened half of the school on the page at two or three points that already exist, in a line or two each. No new scene is needed. Candidates: the fifty first-years on the Kennel benches who watched Team Seven fail (`09:97–107`); the other ten catchers (`10:5`); Selka Dray, who has every reason to resent Seven and never speaks to them (`10:15–17`, `13:163`); Kellan's own First Division, of whom we hear only through him (`09:277`); the Stonehand gallery (`15:15`); whoever wrote the tag.
- Let one adult in authority be wrong, or merely unpleasant, and stay that way.

**Strength to preserve.** Druce, Vane and Brask as individuals. Brask's courtesy drives chapters 15 and 16 and should not be touched. Anwen's phrase. Kellan thinking of his teammates by surname in his own section (`12:133–201`). Jude's opening speech. The ethic itself, that these people say what they are doing and why, is the book's subject. The repair is to stop it arriving in one cadence.

### Priority 3 — Seed the rising year once per witness, and tighten chapter 14

**Location.**

- Narrator's denial, three times: `14:254` ("They were not the same sort of thing at all … He drew no line between them"); `16:321` ("They had nothing to do with each other"); `16:443` ("Neither has asked to see the other, and I don't know of any reason why they should. I mention it only because I happened to have them on the same desk").
- "Strong year" or "strong class" five times: `14:236`, `14:246`, `15:173`, `16:321`, `16:439`. "Dirty spring" twice: `16:321`, `16:439`.
- The evidence beats themselves, about nine in eight chapters: `10:85–93`, `11:55–59`, `12:357`, `13:487–491`, `14:77–89`, `14:238–250`, `15:171–173`, `16:319`, `16:439–447`.
- Chapter 14 as a whole: the highest system-vocabulary density in the movement (204.5 per 10,000 against a movement mean of 133.9), one physical beat in 6,700 words (`14:300–318`), and the longest and stillest cutaway (`14:222–270`, 1,196 words).

**Observed issue.** The packet asked that this movement "seed the coupled escalation without explaining it" and leave the reader with "one concrete sign" of each trend. Each trend now has four or five signs. The two are set side by side by three different viewpoint characters, and each time the narration remarks that nobody connects them. The remark is the tell. Chapter 14 does most of this work in the chapter that already has to carry grading, the comb, the shelf, the shares and the vote.

**Effect on the reader.** An attentive reader makes the connection in Noa's corridor and then watches Rhea and Ysra be led to the same shelf and look away. The mystery the series means to prove "gradually" loses room in Movements Three and Four. Chapter 14 is where a reader coming off the license-day high is most likely to put the book down.

**Proposed scope.**

- Keep every fact. Remove the explicit "unconnected" remark at two of the three sites. Noa's is the first and the most in character.
- Let Rhea's card carry the tear count without her gloss (`16:321`).
- Let Ysra state her two reports as her reason for the Flask change and go straight to it (`16:439–447`), without the aside about the desk.
- Bring "strong year" down to two uses, and spend Perrin's plate (`15:173`) as one of them, since it costs someone something.
- Shorten Noa's cutaway by about a third, toward its real subject, which is the decision to ask her first (`14:258–270`). The forty-year medians can be two sentences.
- No scene is removed. Chapter 14's first five sections (`14:3–218`) should not be touched.

**Strength to preserve.** Halloran's shelf with its hand-lettered card (`14:71–89`). The kitchen vote entire (`14:139–218`). Noa's consent ethic and its payoff in Ysra's office (`16:419–435`). Perrin's plate and his "I've decided I'm allowed both" (`16:381`). Ysra's acceleration of the Flask, which is the movement's exit pressure.

### After repair

Re-run the appendix script and report target against observed honestly. Do not iterate to hit decimals.

---

## 7. Owner decisions (plan adherence and formula conflicts, not repairs)

1. **Whole-text sentence and readability targets.** Missed by the same margin as repaired Movement One: mean 9.84 against 14.6, short share 41.5% against 27.7%, grade 2.8 against 6.8. Narration alone is near the formula (12.95, 29.0%, 2.94%). The remaining distance is spoken sentences and plain vocabulary. The Movement One recheck judged this not to be an audible defect and left the choice with the owner. That choice is still open, and this movement is more dialogue-heavy than the last (speech is 48% of sentences, up from 42%).
2. **How dangerous is a Handful?** The bible says Riftspawn are "not training dummies." On the page a husk is a blind animal that ignores anyone who is dark, and the harm shown is to infrastructure and yield. That serves this movement's argument. If the owner wants bodily menace at the first license, it would need one beat where a husk hurts someone who did not choose it.
3. **The rival seat.** Kellan is a committed teammate by `10:447` and counts aloud with Kiva by chapter 13. The book map's Movement Three promises "a developed learning fight against an adaptive rival." Lowen Brask ("I'll have to think of something else," `16:193`) and Selka Dray are both available. Who holds that seat is the owner's to name.
4. **How much the Chair should hold by chapter 16.** Even with Priority 3 applied, Ysra ends the movement with both reports and tells the protagonist. That is permitted by the packet and is ahead of the book map's schedule for evidence.
5. **Scope of "live-cell events"** (C6). Priority 1 can bridge it in a line. Which reading is canon should be the owner's.
6. **Secondary viewpoints.** Seven characters have had a cutaway by chapter 16 against a formula shape of four or five. Movement Two added Noa and Perrin. Worth deciding before Movement Three adds Hollis Vane or Jude.
7. **Carried from the checkpoint, unchanged by this review.** Noa Bexley and Hollis Vane are written he/him by the author's choice. Healer Aske appears with no pronoun. The unnamed month has thirty days. The second purchased Kennel floor has no date.

---

## 8. Tradeoffs and uncertainty

- **Same model, informed read.** I share the drafting seat's habits and may be blind to them. The voice convergence in Priority 2 is the kind of pattern a same-model reviewer is most likely to under-report. Treat that count as a floor.
- **The two reader lenses are constructions**, not research. No sales forecast is implied.
- **Scores are not comparable to Movement One's as a contest.** The rubric and anchors are the same. The coverage is not: the first review included a 16,000-word prologue, and reviewed a first draft that has since been repaired.
- **Priority 2 trades against a real virtue.** A world of fair-minded professionals is part of why this movement is a pleasure to read. Too much added friction would make it a different, more ordinary book. The scope asked for is small on purpose.
- **Priority 3 trades against clarity for a younger reader**, who may need the pairing shown more than once to notice it at all. One removal fewer is defensible.
- **C2, C3 and C6 are medium confidence.** Each could be answered by a rule I have not been shown. In each case the page does not supply the bridge, and that is the finding.
- **Metric comparisons with the formula are imperfect by construction.** The source was measured on audio transcripts and this draft on typography. The mean, median and share gaps are large enough to survive that caveat. The stdev, paragraph and section comparisons are not.
- **The development-beat list in 5e is a reading.** The regex proxy and the manual list agree in rate and shape, which is mild support for both.
- **One movement does not prove anything about the seat across a series.**

---

## Appendix — reproducible metrics method

**Environment.** Python 3.14.6, standard library only. Read-only against the manuscript. No network access. Both scripts were written to a scratch folder outside the repository.

**Step 1.** Extract the Movement One script, unchanged, from the appendix of `editor/MOVEMENT-001-EDITORIAL.md` (the first fenced `python` block) and save it as `metrics_m001.py`. Its SHA-256 must be `462e9ac63f3d831ce8465b78598e32ed0a95b25b25adef9373d1495dc402a308`, the hash that report publishes.

```
awk '/^```python$/{f=1;next} /^```$/{if(f){exit}} f' editor/MOVEMENT-001-EDITORIAL.md > metrics_m001.py
```

**Step 2.** Save the script below as `metrics_m002.py` and run it with the book root and the path to the first script.

```
python3 metrics_m002.py /Users/drive/kindling-repo-stage/.claude/worktrees/kindling-2680-prologue-m001-opus55/books/book-2680-opening metrics_m001.py
```

**Script SHA-256 as run:** `08a6f5b297b81ce510e4709b1446fcf60b81a37b2959838ddcdaaaaeaba89617`

**Input hashes.** See the coverage table in section 0. The script prints them first. Chapters 1–8 as measured: 33f9cfad1b747288, 01e3154d41a7a5b7, 9b74bb223f8be407, 5839b4442b0fd669, ff8258b86ec8ffb0, bc300f9c651e6ce8, a83948c2bfdde53c, a7afe0d10e5fd278.

**Definitions.** Words, sections, paragraphs, sentences, syllables, both Flesch formulas, the Movement One progression lexicon, reporting, combat and filler lexicons, the `-ly` stoplist and the development proxy are imported from `metrics_m001.py` and are exactly as defined in that report's appendix. Added here:

- *Movement Two progression additions:* `PROG2_CI` and `PROG2_CS` below, reported separately from the Movement One lexicon.
- *POV map:* `POV_CHECK` below, identified by reading. The script asserts that all six cutaways were found.
- *Narration / speech / ledger split:* the rule in the appendix of `editor/MOVEMENT-001-TARGETED-RECHECK.md`, implemented in block 8. It reproduces that report's chapters 1–8 narration figures.
- *Number-only sentences:* every word is a number word, "and" or "a."
- *Staccato runs:* consecutive sentences of five words or fewer within one section.
- *Tics:* the `TICS` patterns below, matched case-insensitively with letter boundaries.

**Known false positives.** Those listed in the Movement One appendix, and: "First," "Second" and "Third" also match ordinals that are not grades or divisions; "catch," "print" and "share" match their ordinary senses; "count" matches the noun and the verb; the "Hm" pattern counts Perrin's imitation at `10:55`.

**Not captured by the script.** Every reader score, every finding in section 4, the manual beat list in 5e and all read-aloud judgments are readings of the page. Each is cited by line.

### `metrics_m002.py`

```python
#!/usr/bin/env python3
"""Movement 002 numerical alignment - Kindling 2680 Book One, chapters 9-16.

Stdlib only. Read-only against the manuscript. Imports every shared definition
(word regex, sentence tokenizer, syllable estimator, lexicons, proxies) from the
Movement One script so the two movements are measured the same way.
Usage: python3 metrics_m002.py /path/to/books/book-2680-opening /path/to/metrics_m001.py
"""
import re, sys, statistics, hashlib, collections, importlib.util

ROOT = sys.argv[1].rstrip('/')
_argv = sys.argv
sys.argv = [_argv[2], ROOT]
spec = importlib.util.spec_from_file_location('m1', _argv[2])
m1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m1)
sys.argv = _argv
words, clean, sections, paragraphs, sentences = m1.words, m1.clean, m1.sections, m1.paragraphs, m1.sentences
syllables, sent_stats, flesch, per10k = m1.syllables, m1.sent_stats, m1.flesch, m1.per10k

M1 = ['chapter-%02d' % i for i in range(1, 9)]
M2 = ['chapter-%02d' % i for i in range(9, 17)]

# viewpoint map, identified by reading every section; guarded by first words
POV_CHECK = {
    'When they had gone, Orla Dane sat on her crate': 'Orla',
    'Anwen Pryce was at the Graywater hall': 'Anwen',
    'Kellan Renn poured the first tin': 'Kellan',
    'Noa Bexley had been in the roster corridor': 'Noa',
    'Perrin Cade had both wrapped hands': 'Perrin',
    'Rhea Sorn did not go down to the sand': 'Rhea',
}
# Movement Two additions to the progression lexicon (defined before counting)
PROG2_CI = [r'yield', r'yields', r'handful', r'handfuls', r'flask', r'flasks', r'barrel',
            r'resonance', r'licen[sc]e', r'licen[sc]ed', r'certif(?:y|ied|ication|icate)',
            r'tinned', r'printed', r'print', r'sweepings', r'w-trace', r'ward-trace',
            r'hundredths', r'tenths', r'catch', r'catcher', r'catchers', r'share', r'shares',
            r'abort', r'dark hands']
PROG2_CS = [r'Kill', r'Carry', r'Catch', r'Second', r'First', r'Third']
NUMWORDS = ('one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen '
            'sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety '
            'hundred thousand half tenth tenths hundredths nought').split()
TICS = [
    ('"Hm" / "Huh" as a spoken line', r'[“"]\*?(?:hm|huh)[.,]?\*?[”"]'),
    ('"hm" anywhere', r'(?<![a-z])hm(?![a-z])'),
    ('want/like it said|noted|known|understood', r"(?:want|like) (?:it|that) (?:said|noted|known|understood)|want it to be (?:said|noted)"),
    ("it's said / it is said", r"it(?:'|’)s said|it is said"),
    ('not unkindly', r'not unkindly'),
    ('did not soften', r'did not soften'),
    ('nearly/almost smiled', r'(?:nearly|almost) smiled'),
    ('like/as a man|woman|person|boy|girl', r'(?:like|as) (?:a|an) (?:man|woman|person|boy|girl|people)\b|as people|as a person'),
    ('"as if"', r'as if'), ('"like a"', r'like a'), ('"the way"', r'the way'),
    ('"did not"', r'did not'), ('"had not"', r'had not'), ('"it was not"', r'it was not'),
    ('for a (long )?moment/time/while', r'for a (?:long )?(?:moment|time|while)'),
    ('said nothing / nobody said anything / nobody spoke', r'said nothing|nobody said anything|nobody spoke|no one spoke|did not answer'),
    ('"very"', r'very'), ('"a little"', r'a little'), ('"at once"', r'at once'),
    ('"quite"', r'quite'), ('"rather"', r'rather'),
    ('"nothing to do with each other" / "no line between"', r'nothing to do with each other|no line between|not the same sort of thing|any reason why they should'),
    ('"a strong year|class"', r'strong (?:year|class)'), ('"dirty spring"', r'dirty spring'),
    ('"probably nothing"', r'probably nothing'),
    ('"different column"', r'different column'),
    ('"nineteen years"', r'nineteen years'),
    ('"street lamp for a fortnight"', r'street lamp for a fortnight'),
    ('"thank you" to the ground (italic)', r'thank you'),
    ('"count" as command/noun', r'(?<![a-z])count(?:ed|ing|s)?(?![a-z])'),
]

def body(f):
    return '\n\n'.join(sections(m1.load(f)))

def block(files, label):
    texts = {f: body(f) for f in files}
    tot = {f: len(words(clean(texts[f]))) for f in files}
    W = sum(tot.values())
    print('\n######## %s (words %d) ########' % (label, W))
    print('== 1. Sentences ==')
    print('%-11s %6s %6s %6s %7s %7s %6s %6s %4s' % ('file','words','sents','mean','median','pstdev','<=5%','>=40%','max'))
    allsent = []
    for f in files:
        sl = sentences(texts[f]); st = sent_stats(sl); allsent += sl
        print('%-11s %6d %6d %6.2f %7.1f %7.2f %6.1f %6.2f %4d' % (f, tot[f], st['n'], st['mean'], st['median'], st['pstdev'], st['le5'], st['ge40'], st['mx']))
    st = sent_stats(allsent)
    print('%-11s %6d %6d %6.2f %7.1f %7.2f %6.1f %6.2f %4d' % ('TOTAL', W, st['n'], st['mean'], st['median'], st['pstdev'], st['le5'], st['ge40'], st['mx']))
    lens = [len(words(s)) for s in allsent]
    hist = collections.Counter(min(x, 45) // 5 * 5 for x in lens)
    print('  histogram (bucket start: share%): ' + ', '.join('%d:%.1f' % (k, 100 * hist[k] / len(lens)) for k in sorted(hist)))
    print('  sentences >=30 w: %.2f%%; >=25 w: %.2f%%; 1-3 w: %.1f%%' % (100*sum(1 for x in lens if x>=30)/len(lens), 100*sum(1 for x in lens if x>=25)/len(lens), 100*sum(1 for x in lens if x<=3)/len(lens)))
    A = clean('\n\n'.join(texts[f] for f in files))
    naive = [x for x in re.split(r'(?<=[.!?])["”’]?\s+', re.sub(r'\s+', ' ', A)) if words(x)]
    nl = [len(words(x)) for x in naive]
    print('  naive tokenizer: sents %d mean %.2f median %.1f <=5 %.1f%% >=40 %.2f%%' % (len(nl), statistics.mean(nl), statistics.median(nl), 100*sum(1 for x in nl if x<=5)/len(nl), 100*sum(1 for x in nl if x>=40)/len(nl)))
    narr = re.sub(r'[“"][^”"]*[”"]', ' ', A)
    ns = [len(words(x)) for x in sentences(narr)]
    print('  narration only: sents %d mean %.2f median %.1f pstdev %.2f <=5 %.1f%% >=40 %.2f%%' % (len(ns), statistics.mean(ns), statistics.median(ns), statistics.pstdev(ns), 100*sum(1 for x in ns if x<=5)/len(ns), 100*sum(1 for x in ns if x>=40)/len(ns)))
    quoted = re.findall(r'[“"][^”"]*[”"]', A)
    q = sum(len(words(x)) for x in quoted)
    ds = [len(words(x)) for qq in quoted for x in re.split(r'(?<=[.!?])\s+', qq) if words(x)]
    print('  words inside double quotes: %d (%.1f%%); dialogue sentence mean %.2f median %.1f <=5 %.1f%%' % (q, 100*q/W, statistics.mean(ds), statistics.median(ds), 100*sum(1 for x in ds if x<=5)/len(ds)))
    syl = sum(syllables(w) for w in words(A))
    print('  syllables/word %.3f; words/sentence %.2f' % (syl / W, W / len(allsent)))
    for s in sorted(allsent, key=lambda s: -len(words(s)))[:3]:
        print('  longest (%d w): %s...' % (len(words(s)), s[:90]))

    print('== 2. Paragraphs and sections (typographic) ==')
    allp, allsec = [], []
    for f in files:
        secs = sections(m1.load(f))
        pl = [len(words(p)) for s in secs for p in paragraphs(s)]
        sw = [len(words(clean(s))) for s in secs]
        allp += pl; allsec += sw
        print('%-11s paras %4d mean %5.1f median %4.1f | sections %2d mean %6.0f min %5d max %5d | breaks/10k %4.1f' % (f, len(pl), statistics.mean(pl), statistics.median(pl), len(sw), statistics.mean(sw), min(sw), max(sw), per10k(len(sw), sum(sw))))
    print('TOTAL       paras %4d mean %5.1f median %4.1f | sections %2d mean %6.0f median %6.0f | breaks/10k %4.1f' % (len(allp), statistics.mean(allp), statistics.median(allp), len(allsec), statistics.mean(allsec), statistics.median(allsec), per10k(len(allsec), sum(allsec))))
    print('  paragraphs >=100 w: %d; >=150 w: %d; <=12 w: %.1f%%; sections <500 w: %d; >1500 w: %d' % (sum(1 for x in allp if x>=100), sum(1 for x in allp if x>=150), 100*sum(1 for x in allp if x<=12)/len(allp), sum(1 for x in allsec if x<500), sum(1 for x in allsec if x>1500)))

    print('== 3. Readability ==')
    for f in files:
        fre, fk = flesch(texts[f]); print('%-11s FRE %5.1f  FK %4.1f' % (f, fre, fk))
    fre, fk = flesch('\n\n'.join(texts[f] for f in files)); print('TOTAL       FRE %5.1f  FK %4.1f' % (fre, fk))

    print('== 4. Progression vocabulary per 10k ==')
    door = r'(?:ember|hand|still|first|one|two|three|single)[- ]doors?'
    grand = collections.Counter(); ext = collections.Counter()
    for f in files:
        t = clean(texts[f]); c = m1.count_prog(t); grand.update(c)
        e = collections.Counter(); low = t.lower()
        for x in PROG2_CI: e[x] = len(re.findall(r'(?<![A-Za-z\-])(?:' + x + r')(?![A-Za-z])', low))
        for x in PROG2_CS: e[x + ' (cs)'] = len(re.findall(r'(?<![A-Za-z\-])' + x + r'(?![A-Za-z])', t))
        ext.update(e)
        print('%-11s M1-lexicon %4d (%.1f/10k) | +M2 additions %4d (%.1f/10k) | combined %.1f/10k' % (f, sum(c.values()), per10k(sum(c.values()), tot[f]), sum(e.values()), per10k(sum(e.values()), tot[f]), per10k(sum(c.values())+sum(e.values()), tot[f])))
    print('TOTAL       M1-lexicon %d (%.1f/10k); excl. door compounds %.1f/10k; M2 additions %d (%.1f/10k); combined %.1f/10k' % (sum(grand.values()), per10k(sum(grand.values()), W), per10k(sum(grand.values())-grand[door], W), sum(ext.values()), per10k(sum(ext.values()), W), per10k(sum(grand.values())+sum(ext.values()), W)))
    print('  top M1-lexicon terms: ' + ', '.join('%s=%d' % kv for kv in grand.most_common(16)))
    print('  top M2 additions: ' + ', '.join('%s=%d' % kv for kv in ext.most_common(16)))
    toks = [w.lower() for w in words(A)]
    nw = sum(1 for w in toks if w in NUMWORDS); dg = sum(1 for w in toks if re.match(r'^\d', w))
    print('  number words %d (%.1f/10k); digit tokens %d (%.1f/10k)' % (nw, per10k(nw, W), dg, per10k(dg, W)))

    print('== 5. Development regex proxy ==')
    cast = m1.CAST + ['Noa', 'Jude', 'Pru', 'Druce', 'Vane', 'Brask']
    lead = m1.dev_proxy(A, m1.LEAD)
    print('  lead %d (%.1f/10k) | %s' % (lead, per10k(lead, W), ' '.join('%s=%d(%.2f)' % (n, m1.dev_proxy(A, [n]), per10k(m1.dev_proxy(A, [n]), W)) for n in cast)))
    for f in files:
        t = clean(texts[f]); print('  %-11s lead %d' % (f, m1.dev_proxy(t, m1.LEAD)))

    print('== 6. POV word share ==')
    pov = collections.Counter(); seen = set()
    for f in files:
        for i, s in enumerate(sections(m1.load(f))):
            who = 'Kiva'
            if f in M1:
                who = m1.POV.get(f, {}).get(i, 'Kiva')
            else:
                for k, v in POV_CHECK.items():
                    if clean(s).startswith(k): who = v; seen.add(k); print('  cutaway %-7s %s sec %d: %d w' % (v, f, i, len(words(clean(s)))))
            pov[who] += len(words(clean(s)))
    if set(files) >= set(M2): assert seen == set(POV_CHECK), set(POV_CHECK) - seen
    for who, n in pov.most_common(): print('  %-8s %6d  %5.2f%%' % (who, n, 100 * n / W))

    print('== 7. Secondary signals per 10k ==')
    for lab, terms in (('reporting verbs', m1.REPORTING), ('combat terms', m1.COMBAT), ('fillers', m1.FILLERS)):
        c = m1.count_ci(A, terms)
        print('  %-16s %6.1f  %s' % (lab, per10k(sum(c.values()), W), ' '.join('%s=%.1f' % (t, per10k(c[t], W)) for t in terms if c[t])))
    ly = [w.lower() for w in words(A) if w.lower().endswith('ly') and w.lower() not in m1.LY_STOP and len(w) > 3]
    print('  -ly suffix words: %.1f per 10k; top: %s' % (per10k(len(ly), W), ', '.join('%s=%d' % kv for kv in collections.Counter(ly).most_common(12))))
    tri = collections.Counter(zip(toks, toks[1:], toks[2:]))
    print('  top 3-grams: ' + ', '.join('%s=%d(%.1f)' % (' '.join(k), v, per10k(v, W)) for k, v in tri.most_common(16)))
    print('  tics / phrases (count, per 10k):')
    for lab, pat in TICS:
        n = len(re.findall(r'(?<![a-z])(?:' + pat + r')(?![a-z])', A.lower())); print('    %-52s %4d %6.1f' % (lab, n, per10k(n, W)))
    notfrag = [x for x in allsent if re.match(r'^Not\b', x) and len(words(x)) <= 8]
    print('  narration fragments opening "Not ..." (<=8 w): %d (%.1f/10k)' % (len(notfrag), per10k(len(notfrag), W)))
    cnt = [x for x in allsent if all(w.lower() in NUMWORDS or w.lower() in ('and', 'a') for w in words(x))]
    short = sum(1 for x in lens if x <= 5)
    rest = [len(words(x)) for x in allsent if x not in set(cnt)]
    print('  number-only sentences (counts, weights): %d (%.1f%% of sentences; %.1f%% of the <=5 group)' % (len(cnt), 100*len(cnt)/len(allsent), 100*len(cnt)/short))
    print('  with number-only sentences removed: mean %.2f median %.1f <=5 %.1f%% >=40 %.2f%%' % (statistics.mean(rest), statistics.median(rest), 100*sum(1 for x in rest if x<=5)/len(rest), 100*sum(1 for x in rest if x>=40)/len(rest)))
    itwas = len(re.findall(r'It was not [^.]{1,60}\. It was ', A))
    print('  "It was not X. It was Y." constructions: %d (%.1f/10k)' % (itwas, per10k(itwas, W)))
    print('== 8. Narration / speech / ledger split (rule from MOVEMENT-001-TARGETED-RECHECK.md, appendix) ==')
    out = {'narration': [], 'speech': [], 'ledger': []}
    runs = []; run = 0
    for f in files:
        for sec in sections(m1.load(f)):
            for para in [p for p in re.split(r'\n\s*\n', sec) if p.strip()]:
                lines = [l.strip() for l in para.strip().split('\n') if l.strip()]
                sents = sentences(para)
                whole_it = all(re.fullmatch(r'\*[^*].*\*', l) for l in lines)
                label_it = all(re.match(r'\*[^*]+:\*\s', l) or re.fullmatch(r'\*[^*].*\*', l) for l in lines)
                if whole_it or label_it:
                    out['ledger'] += sents
                else:
                    inq = False
                    for x in sents:
                        n = len(re.findall(r'["“”]', x))
                        out['speech' if (inq or n) else 'narration'].append(x)
                        if n % 2: inq = not inq
                for x in sents:
                    if len(words(x)) <= 5: run += 1
                    else:
                        if run: runs.append(run)
                        run = 0
            if run: runs.append(run); run = 0
    N = sum(len(v) for v in out.values())
    for k in ('narration', 'speech', 'ledger'):
        ls = [len(words(clean(x))) for x in out[k]]
        print('  %-9s %5d sents (%4.1f%%) mean %5.2f median %4.1f <=5 %4.1f%% >=40 %4.2f%% words %d' % (k, len(ls), 100*len(ls)/N, statistics.mean(ls), statistics.median(ls), 100*sum(1 for x in ls if x<=5)/len(ls), 100*sum(1 for x in ls if x>=40)/len(ls), sum(ls)))
    nar = [len(words(clean(x))) for x in out['narration']]
    target_s = W / 14.6
    print('  sentences at a 14.6 mean: %.0f; narration+ledger already use %d; short budget at 27.7%%: %.0f; narration+ledger short: %d; spoken short: %d' % (target_s, len(out['narration'])+len(out['ledger']), 0.277*target_s, sum(1 for k in ('narration','ledger') for x in out[k] if len(words(clean(x)))<=5), sum(1 for x in out['speech'] if len(words(clean(x)))<=5)))
    print('  staccato runs (consecutive <=5-word sentences within a section): runs>=3: %d; >=5: %d; >=8: %d; longest %d' % (sum(1 for r in runs if r>=3), sum(1 for r in runs if r>=5), sum(1 for r in runs if r>=8), max(runs)))
    low = A.lower()
    ca = len(re.findall(r', and\b', low)); sub = len(re.findall(r'\b(?:because|while|when|which|although|though|until|so that|as if|since|where)\b', low))
    print('  ", and" per 1000 w: %.1f (one per %.0f words); listed subordinators per 1000 w: %.1f' % (1000*ca/W, W/ca, 1000*sub/W))
    turns = [p for f in files for sec in sections(m1.load(f)) for p in paragraphs(sec) if re.search(r'[“"]', p)]
    tl = [sum(len(words(q)) for q in re.findall(r'[“"][^”"]*[”"]', p)) for p in turns]
    tl = [x for x in tl if x]
    print('  spoken turns %d; median quoted words %.1f; <=3 words %.1f%%; >=25 words %.1f%%; turns with "said" outside quotes %.1f%%' % (len(tl), statistics.median(tl), 100*sum(1 for x in tl if x<=3)/len(tl), 100*sum(1 for x in tl if x>=25)/len(tl), 100*sum(1 for p in turns if re.search(r'\bsaid\b', re.sub(r'[“"][^”"]*[”"]', ' ', p)))/len(turns)))
    ik = len(re.findall(r'[“"]I know\.[”"]', A)); print('  "I know." as a whole reply: %d' % ik)
    return W

print('SHA-256 (first 16) / whitespace words')
for f in M1 + M2:
    raw = m1.load(f); print('  %-11s %s %6d' % (f, hashlib.sha256(raw.encode()).hexdigest()[:16], len(raw.split())))
block(M2, 'MOVEMENT TWO, chapters 9-16')
block(M1, 'MOVEMENT ONE as now on disk (repaired), chapters 1-8')
block(M1 + M2, 'CUMULATIVE chapters 1-16 (prologue excluded)')
```
