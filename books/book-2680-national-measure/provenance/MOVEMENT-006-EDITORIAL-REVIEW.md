# Kindling 2680, Book Two — Movement Six — editorial and numerical review

> Built by TAC

Date: 2026-10-15. Reviewer: **Claude Opus 5.5 (`claude-opus-5-5`)**, Claude Code background session (job `6e915e3e`).
The owner directed that this review be done by this session directly. No penname-editor skill, Codex, subagent or other
model was used.

## 0. What kind of review this is

- **Same model, fresh context, informed. Not blind.** The drafting author of chapters 41–48 is recorded as Claude Opus 5.5
  (`AUTHORSHIP.md`, "Movement Six, first draft", job `35fbff1b`). This session did not have the drafting transcript. It did
  have the compiled brief (packet, ledger, map, cast, bible, formula) as supplied in the prompt, and the author's own
  continuity file. This is **not** a cold read, a human read or independent testing. The two reader lenses below are
  simulated editorial perspectives, not reader research, and no sales inference is made. A same-family reviewer shares the
  drafter's blind spots.
- **Coverage.** All eight supplied files were read in chapter order, in full: `manuscript/chapter-41.md` to `chapter-48.md`.
  - Size: 56,569 words by `wc -w`; 56,463 body words by the script tokenizer (headings and `---` lines excluded).
  - Integrity: every file is byte-identical to `editions/movement-006-first-draft/` (`cmp`: all same;
    `shasum -a 256 -c SHA256SUMS.txt`: OK ×8). Hashes in §7.
  - Completeness: the movement is complete as planned. It is the last movement of the book; chapter 48 ends the book.
- **Canon evidence used.**
  - Book Two records: `STATE_LEDGER.md` (§1–§11 and the Movement One to Six blocks), `BOOK_MAP.md`, `CHARACTERS.md`,
    `UNIVERSE_BIBLE.md`, `packets/MOVEMENT-006.md` (as supplied), `provenance/MOVEMENT-006-CONTINUITY.md` (as supplied),
    `MOVEMENT-005-EDITORIAL-REVIEW.md` and `MOVEMENT-005-REPAIR.md` (for comparable figures and the repair state).
  - Targeted greps of Book Two ch. 17 (the gate comb of the sealed tin), ch. 22–23 (the foundation cell; the sealed
    prediction's text), ch. 24 (Pike's hands), ch. 27 (Old Four's protest), ch. 28–30 (Skerry Pill), ch. 35, 38, 40 (Graving
    attendance) and ch. 37 (Saturday's lane result).
  - Labels used below:
    - **Verified:** a contradiction inside chapters 41–48, or between them and a file I read (cited).
    - **Apparent:** a conflict this evidence cannot settle.
    - **Plan:** a departure from the map, cast plan or packet, not a canon error.
- **Other files in the working tree.** `git status` shows chapters 11, 14, 15, 19 and 24 modified by parallel audio repairs,
  and a new `provenance/MOVEMENT-006-COLD-READ.md` written by a parallel job. I read none of the audio edits except where a
  grep above touched ch. 19 or 24. The cold read's first sixty lines (its reader response and the start of its first lens
  table) appeared in a directory listing at the start of this session. I did not read the rest, and **nothing here is taken
  from it**; where my judgment happens to agree with that opening (the coda's repeated shape) I say so.

---

## 1. Unscored reader response

**Where interest caught.**

- **41, Kellan's card (41:27–45).** A concrete, human reason to care before any plan is explained: a hundred-and-three-year-old
  man asking for "one morning of somebody who won't" tell him what he wants to hear. Kellan's "the most honest sum anybody in
  that house has written in my lifetime" is the movement's first real pull.
- **41, the trestle among the pumps.** Planning a stop "in the middle of it, with your feet on it" is a strong image, and the
  scene earns its 3,158 words by carrying three things: Mara's child-sayable plan, Brask's cask ("The water's its head"), and
  Rusk's six-not-eight, which Kiva rightly calls the best thing in the morning.
- **41, the rope drill (41:327–339).** Absurd, physical, and it solves the problem the hour of failure exposed. "That's
  strangers stopping."
- **42, "It's looking at the pipes" (42:51).** The best turn in the movement. The plan is overturned by an observation from
  the person least inclined to help, and the cost is shown at once: the water turns to look at Anwen, and Anwen sits down.
- **42, Tuesday's test (42:241–307).** Kellan's question and the Proprietor's "simpler, not harder" plant the surviving bad
  assumption so cleanly that "She could not have said why she did not like it" is enough.
- **43, the refusal (43:83–101).** "If this morning needs my three, it's not a method. It's me." This is the book's argument
  said once, in the right mouth, to the right listener.
- **44, the passes.** The sill (Bannock: "It's water" on Tuesday, then a post that cannot step), Lyle's "I'm saying it before",
  Aske's ten-count with the price inside it, Perrin's declaration from the wall, the run, the hand going "the way a lamp goes
  when somebody turns the key the whole way down", and the cut on a count read through her still door. Every beat raises the
  cost and every beat was planted.
- **45, "It's one hold. Not two" (45:73) and "Twenty-two" (45:107).** Kellan's arc lands here, and the Proprietor's lift is
  given a real price on the page (the print, the pulse, the first cell missing a step).

**Where interest slipped.**

- **43's position map (43:131–151).** Useful for tracking, but it stops the forward motion just after the Proprietor scene had
  built pressure, and one of its bearings is wrong (C7).
- **44:25 and the scale.** I pictured a man-high cask with water "over their heads", then remembered four feet eleven. The
  picture and the number fight each other (C2).
- **46's box (46:215–273).** Precise, and mostly new information (the minute early, the 23 minutes, "not tested, by design").
  But the three-accounts paragraph re-reads lines the reader saw an hour of story time earlier.
- **The coda (ch. 46–48).** About twenty-one thousand words in twenty-four sections after the climax. Many sections share one
  shape: someone offers, someone declines or accepts, and someone says they would like that said or written. By the Mole
  farewells I felt the pattern repeating (the cold read's opening makes the same observation; I reached it independently).
  The Tanyard (47 §8) is the exception and the coda's best scene.

**Which person matters.** Kiva first. Then Kellan, whose movement is the surprise of the ending. Then Mara (the watch hand kept
still until case nineteen) and Pike ("two words, once", from both sides).

**What I expect next.** The hull and who answered; the first morning the left hand says *yes*; the first bank called by
somebody who is not Kiva.

**Would I continue?** Yes. As the end of a book it satisfies: the competition was read in Movement Five, the nation counts what
it has, and the beat itself comes out of the harbour at a visible price. The final image is earned.

---

## 2. Scored dimensions — two lenses

Scale: 5 = understandable but inconsistent; 7 = engaging with located weaknesses; 9 = compelling with few substantial
distractions. Editorial judgments, not measurements. The two lenses are not averaged and are not a release gate.

### 2a. A fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 7 | 41:1–45 | The card is a clear human hook, but the first page leans on Hart, the Step, Halden License's beds and the fever's "bill" without re-introducing them. | Medium |
| Keep reading | 9 | 42:51; 43 ends "*Take.*"; 44 throughout; 45:73 | Each chapter ends on unresolved danger; ch. 44 has a cliffhanger inside nearly every section. | High |
| Interest / freshness | 8 | 41:157 the cask; 41:327 the rope; 42:57 "the nearest thing that keeps time" | Specific images, a new problem, people solving it with what they already have. | High |
| Clarity / flow | 6 | 44:149–213 the sill; 45:11–57 quench/draw/set; 43:131–151 | The movement assumes the series' vocabulary (planks, wards, Embers, still doors, cans, plain ash). The sill's geometry and the cask's size (C2) are hard to hold on one pass. | Medium |
| Character attachment | 8 | 42:177–193 Lyle; 44:277 "I'm saying it before"; 42:347 Bannock | Fear owned out loud is very readable at this age; Pru's "Far edge" and "I did not" land. | High |
| Humor / warmth | 7 | 41:185 Rusk; 44:467 Pettit's "*Oh*"; 46:201 "Davy never did the corners"; 48 Pru "I did not" | Gentle and character-grounded; almost absent from ch. 44–45, which is right. | Medium |
| Action / suspense | 9 | ch. 44 | A trackable contest (three marks, three planks, a count), adaptation at each failure, a visible cost. Length earned. | High |
| Progression payoff | 8 | 44:439–443 still door reads a count; 47:107–125 Ivey calls | Effort visibly changes what people can do, and the payoff is passed to someone else. | Medium |
| Connection | 9 | 41:79 → 44:311 (ten counts); 42:347 → 44:171 (Bannock); 42:177 → 44:277 (Lyle); 42:299 → 45:73 | Every failure at the Slack was planted in rehearsal; a young reader will feel the click. | High |
| Read-aloud quality | 6 | 44:315 the interleaved count; second-precise times in 44–45 | Attribution is clean. Italic counts mixed with speech and "eleven minutes past six and forty seconds" are hard to voice. | Medium |

### 2b. An adult genre reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 7 | 41:1–83 | The card pulls; Aske's second pricing scene is necessary but recaps ("I said the price twice last week… I'll not say it a third time"). | Medium |
| Keep reading | 8 | 44–45 at 9; 46–48 at about 7 | The climax compels; the coda's repeated offer-and-acknowledge shape slackens it. | Medium |
| Interest / freshness | 8 | 42:241–307 → 45:73 | The surviving bad assumption is the Proprietor's own hand: a design that makes the antagonist's pattern the obstacle without making him a villain. The prediction audit is a fresh kind of payoff. | High |
| Clarity / flow | 6 | C1, C2, C3, C4, C7 | A rules-minded reader will trip on the Master standing over the sill plank, "over their heads" at 4 ft 11, Saturday's lane reversed, and several clocks that do not add. | High |
| Character attachment | 8 | 45:101 Kellan's sum; 47:229 "I'm only certain I let go"; 45:265 Mara's "Mine" | The Proprietor is given dignity and doubt; Mara's restraint pays. | High |
| Humor / warmth | 7 | 45:245 "six bands at a fair"; 46:375 the knock; 41:185 | Wry, sparse, honest. | Medium |
| Action / suspense | 9 | ch. 44 | Geometry stated, both "sides" adapting (the thing leans; the planks keep its count), cost visible, a second crossing chosen with the price said. | High |
| Progression payoff | 8 | 44:183 "She did not decide it…"; 48:159 the conditions; 47:5 the fourteen | Capability and consequence move together. One new property (reading a count through the still door) arrives late, though it is planted in ch. 23 and 42. | Medium |
| Connection | 8 | as 2a; less the clock and records slips (§3b) | Strong plant-and-payoff chain; the counting reader will test the sums first and find about a dozen small slips. | High |
| Read-aloud quality | 7 | 47:153 (85 words); 46:265 (83) | Dialogue reads well aloud; some narrated summaries and the Clerk's two long sentences run past breath. | Medium |

---

## 3. Canon, physical state, power limits, knowledge and reserved disclosures

### 3a. Arithmetic: clocks, counts, ash, the crossing calendar and the last of the month

**Calendar.** The third month began on a Tuesday (ledger §1), so Monday 21st, Tuesday 22nd, Wednesday 23rd, Thursday 24th,
Friday 25th, Saturday 26th, Sunday 27th, Monday 28th, Tuesday 29th, **Wednesday 30th**, and **Thursday the 1st of the fourth
month** are all correct. Months have thirty days, so the 30th and the 1st are consecutive. ✓

| Item | Page | Arithmetic | Result |
|---|---|---|---|
| Six pumps × six minutes × 57 | 41:39 | 6 × 6 × 57 = 2,052 | ✓ |
| Seventy years, "something over twenty-five thousand days" | 41:45; 45:101 | 2681 − 2611 = 70; 70 × 360 = 25,200 | ✓ |
| Hand warm "Eight mornings" Mon; "Ten mornings" Wed | 41:65; 43:3 | M5: Thu 4, Fri 5, Sat 6 → Sun 7, Mon 8, Tue 9, Wed 10 | ✓ |
| Crossing calendar | 41, 44 | Sixth crossing Thu 10th; one in seven → seventh possible from Thu 17th; Wed 23rd is inside the card | ✓ |
| Seventh crossing | 44:217 | 6.11.40, Ember to still, at M2, mast sanctioned, Noa reading, declared by Cade at six | ✓ inside the certificate |
| Eighth crossing | 44:401 | 6.14.50, second in the hour, against the card, price said first (Mon 41:75–83 and 44:315), declared, read | ✓ as planned |
| Aske's ten-count rule | 41:79 → 44:311–319 | Planted Monday, used Wednesday | ✓ |
| Aske's card after | 47:5–17 | One in fourteen days, the year at least; hand seen next morning; three doors not on the card | ✓ BOOK_MAP §3 |
| Hand gone three weeks | 46:25; 47:9 | From the 23rd → about the 14th of the fourth month (30-day months); commission starts the 15th | ✓ |
| "No answer", ninth day | 48:271 | 23, 24, 25, 26, 27, 28, 29, 30, 1 = nine | ✓ |
| Coast boat "three weeks ago" (Tue) / "a month ago" (Thu 1st) | 42:359; 48:305 | 30th of the 2nd month → 22nd = 22 days; → 1st of the 4th = 31 days | ✓ |
| Thrale's hour | 43:119; 45:279–315 | In the town from 5.50; ward 6.15–7.04 = **49** min; 5.50 → 7.04 = **74** min ("an hour and fourteen minutes") | ✓ (but see C5) |
| Lift, points, salt | 45:107; 45:179; 45:199 | Lift 6.22.11; nine seconds; "Salt" at 6.22.20 = 6.22.11 + 9 s | ✓ a neat join |
| Pumps restarted; low town wet | 45:243–245; 46:139 | First pump 6.26, sixth 6.29; wet 6.22–6.29 = 7 min; "four inches" against Peverell's "a foot" for eleven | ✓ |
| Slack length | 46:233–235 | 6.08 → 6.31 = 23 min, over the 18–22 limit | ✓ "wrong" correctly called |
| Proprietor's age and years | 45; 47 | 2681 − 2604 = 77; born 2578, 26 at the window, 27 at the reading (M5r) | ✓ |
| Foundation cell | 45:95–97 | 2681 − 2391 = 290 years | ✓ |
| Mara's 6.24 line vs Kellan's | 45:83; 45:101 | Slack ends 6.30 (Mara). Salt+cards+count 4 min, pumps 3 more. Lift by 6.24 → still water to 6.28, pumps to 6.31. Mara: "by twenty-four… there's time". Kellan: "at twenty-four, there's not." | **Contradiction (C4h)** |
| Carrow's "eleven minutes on that seam" | 48:57 | Down off the wall about 6.10; tear closed 6.14 (44:113) = about **four** | **✗ (C4b)** |
| "she had made it eleven minutes ago" | 44:305 | Made 6.11.40; it is now about 6.13 | **✗ (C4a)** |
| "She ran forty paces… caught them at thirty-four paces" | 44:349, 353 | From the sill; then eleven more to 45 = 34 + 11 | **✗ by six (C4c)** |
| "a hundred and forty paces off" (the bank from M3) | 43:207 | Bearings: ring 10 from the outfalls + 50 to the sill + 45 = about 105; 43:167, 181, 225, 233, 285 all say "a hundred" | **✗ (C4d)** |
| Lyle hurt "eight days ago" | 42:169 | Skerry Pill was Wed 16th (ch. 28–30); said Tue 22nd = **six** days | **✗ (C4e)** |
| "Three weeks in the shop" | 48:205 | Works' transit Fri 2nd; commission at Meridian the 15th = about **thirteen** days | **✗ (C4f)** |
| Orla "Hers for a year and a half" | 46:297 | Same section: "since the spring of last year" (46:281) → about **one** year | **✗ (C4g)** |
| "six times on sanctioned masts" | 44:203 | Ledger: Book One six Ember→still on masts; M1 one more; M2 four and M3 two hand→Ember = **thirteen** gaps on sanctioned masts | **✗ (C4i)** |
| Cohort "twenty-four" on the wall | 42:3 | Names on the warrant: Ropewalk 4 + Halden 4 + Old Four 4 + Holloway second 4 + Seven 5 + Twenty-Eight 4 = 25; Kellan at the pump house → 24 | ✓ |
| "Eighteen strangers" | 41:341; 44:23 | Ward A 4, catchers 4, Embers 4 (Jude, Gower, two Pascoes), still 6 (Brask, Tolver, Bannock, Wace, Pettit, Lyle) = 18, plus Kiva as caller | ✓ |
| The Slack's positions | 43:131–151 | 18 on the mud + Kiva + 4 cutters on the wall + Perrin on the wall = 24 | ✓ |
| "Ninety-six people" at the reading | 41:89 | 24 fours × 4 (reserves omitted) | ✓ (approximate) |
| The thirty-six jars | 42; 43:41–49; 45:197 | Combed Tue, slept at the Mole, carried by 36 fitters, 36 into 36 cells; Order's cellar 40 − 36 = **4** | ✓ |
| Seven's sealed tin | 46:37–103 | 2.0 (0.8 + 1.2 from the Order) − 1.2 for L. Hosken = **0.8**; resealed, bound as before; "the same as your aunt's hand took" (Book One ledger: 1.2) | ✓ |
| Seven's book | 48:23 | Held **5.15**, unchanged (rehearsal and Slack doors on the Board's ash, by the warrant) | ✓ |
| The Slack's yield and shares | 46:125–133 | 286.4 drams, every dram red; *no claim* (relinquished 6.35); "the warrant pays no share on red"; held as evidence | ✓ consistent with "the red bags stay evidence" |
| Old cans | 45:29 | 36 drawn stepped, boxed, red-tagged, to the press | ✓ |
| Grid order's price | 47:157–175 | A tenth of the light (Ferren a ninth since the autumn); a third again in wages; 112 municipal licences | ✓ internally; new figures, no conflict found |
| Rhea's six nights | 47:367 | 2 in the 1st month (M1), 2 in the 2nd (M2), Gannet Creek and the Tanyard in the 3rd | ✓ |
| Last-of-the-month dates | 48 | Rhea's card ends Wed 30th, looked at at noon; Mara signs at four; Anwen leaves Thu 1st at seven; Jude's crew "from Thursday" = the 1st | ✓ |
| Tuesday's ring and the prediction | 42:35; 43:265 | Tue 4 ft 10½; Wed 4 ft 11 (prediction "4 ft 11, not less than 4 ft 10") | ✓ |
| The prediction's text | 46:219–257 vs ch. 23:27–31 | Read **verbatim** (all six clauses) | ✓ |

### 3b. Findings

Numbered C1–C15. Severity: **High** (breaks a stated rule or picture the climax depends on), **Medium**, **Low**.

**C1 — The Master's forty paces and the sill plank. Verified internal. High.**
- The rule is stated twice: "she'll lay down every door within forty paces of her, without meaning to, as she always has.
  You'll want to know that before you put anybody's door near her" (41:223); and the sister paces forty *from the sill* to
  place M3 (42:321).
- From 5.50 the Master stands "on the stone above the dock mouth… high above the sill" (43:113–115, 147; 44:407).
- At 6.11 three still doors open *into that sill* directly below her: Bannock and Wace (44:149–171) and Kiva's (44:207–209).
  On the page none of them lies down, and Kiva feels the Master only "when she came down the steps" (44:409).
- **Effect:** the Master's visible limit is a packet requirement and the plan's own logic. A rules reader will ask why the M2
  plank works at perhaps ten paces when M3 had to be put at forty-five.
- **Fix (one or two lines):** keep her back along the outer quay until the plant is called. For example at 43:113, "stopped
  well back along the outer quay, by the gate's moorings, sixty paces from the sill, where she had said she would wait"; at
  41:223 Yeo adds "She'll wait back on the outer quay till the sill's planted"; at 44:407 "came along the outer quay and down
  the steps". Kiva's "seventy paces off on the basin wall" (43:117) can stay.

**C2 — The cask's height. Verified internal. Medium.**
- 4 ft 11 by Hart's level, Polglase's call, the prediction and the box (43:265; 46:237).
- Against: "the held water standing over her head" (43:269, Kiva standing), "four feet eleven inches of it over their heads"
  (43:301), "with its water over his head" (44:75, Jude, "a tall young man"), "the height of a man" (44:25), "as tall as a man"
  (44:139).
- 43:257 has it right: it rose "past the height of Anwen's shoulder". Kneeling lines (44:191, 209) are fine.
- **Fix:** "level with her eyes", "to their chins", "taller than a child and as wide as a cart". No scene change.

**C3 — Saturday's lane, reversed. Verified against canon. Medium.**
- 41:273: "Twenty-Eight had beaten Seven in a lane on Saturday." Ch. 37:331–343: Seven won 6–5; Dray: "That's the fairest lane
  I've ever lost." BOOK_MAP §3: "Seven wins the lane on the other three."
- Same sentence: "Halden License had beaten everybody" (Halden was second in the Measure, and "tenth, two points to the good"
  in the Lane after the M5 repair).
- **Fix:** "Twenty-Eight's blade had beaten Seven's catcher in a lane on Saturday"; "Halden License had beaten nearly
  everybody".

**C4 — Clocks, counts and small facts. Verified (each cited). Medium as a group, Low singly.**
- **a.** 44:305 "made it eleven minutes ago" → "at eleven minutes past" (it is about 6.13).
- **b.** 48:57 Carrow "eleven minutes on that seam" → "four minutes".
- **c.** 44:349 "She ran forty paces" vs 44:353 "thirty-four paces" → "She ran up the dock floor".
- **d.** 43:207 "a hundred and forty paces" → "a hundred paces". (The continuity file §0 records this as corrected. It is not.)
- **e.** 42:169 Lyle "eight days ago" → "six days ago".
- **f.** 48:205 "Three weeks in the shop" → "A fortnight in the shop".
- **g.** 46:297 "Hers for a year and a half" → "Hers for a year".
- **h.** 45:101 Kellan "If you lift at twenty-four, there's not" contradicts Mara's "by twenty-four… there's time" three
  paragraphs earlier. Mara's sum works (the still water is needed for the salt and the count to 6.28; the pumps may start
  after). → Kellan: "If you lift after twenty-four, there's not."
- **i.** 44:203 "six times on sanctioned masts" → "a dozen times on sanctioned masts" (thirteen by the ledger).
- **j.** 46:63 "He [Aske] had combed it at the gate on the first day of the Measure." Ch. 17:249–261: a Board clerk combed it at
  the gate on arrival. → "It had been combed at the gate the day they came".
- **k.** 47:293 Pike's hands "half closed… since the second month". M3 and ch. 24:219: halfway from Friday the 4th of the third
  month. → "since the gate".

**C5 — The Master's stated limits, broken without a price. Verified internal. Medium.**
- "She can't hold it and move" (41:223), repeated at 45:279 ("she did not move, because she could not"), then 45:291: "She
  stepped back… one pace, with her hands still folded and her ward still up."
- 43:119, the sister: "if she couldn't keep to it she'd say so first." She overruns by fourteen minutes and nobody says so.
- **Effect:** the packet requires a Glory master's limit "the reader can see". Both lines are good drama but weaken the limit.
- **Fix:** let the step cost something visible ("the grey across the mouth shivered from wall to wall, and the flood came a
  hand nearer before it held"), or have the sister lower the ward-line request ("She says she can step if it's one pace and
  slow"). At about 6.50 let the sister say, flatly, "She says she'll be late. She's saying it first."

**C6 — The prediction's last line: "wrong, twice". Apparent. Low.**
- The paper specifies its instrument: "Nothing else in the basin will keep any count, *by the hand on the grating*" (ch. 23:31).
- At 6.15.40 Hart reports "Quiet… Still quiet" (45:7–9) while the planks have kept Dray's count since 6.09. By the paper's own
  measure, the line failed once (6.16–6.22, the pumps), not twice.
- Hart's honesty reads well and the Clerk records his words, so this is a choice. If kept, give Hart one clause: "By my hand,
  once. By what we did, twice. I'd want both written."

**C7 — Where Carrow and Dray stand. Verified internal. Medium (spatial).**
- 43:143: "Further along the wall toward the Graving, above the place where the tear would be open…: Carrow and Dray." The
  survey has just placed Polglase's mast above M1 (25 paces toward the Graving from the ring).
- The tear is where the ring stood, "ten paces from the outfalls" (44:85), so it lies *back toward the pump house* from the mast.
- **Fix:** "Back along the wall toward the pump house, above the place where the tear would be open…".

**C8 — Chapter 43's clock runs backward. Verified internal. Low (clarity).**
- §4 opens "At ten to six" (43:111); §5 opens "At a quarter to six Yeo blew one long note" (43:129) and walks Kiva to her place.
- Perrin had said "Positions at six" (43:17).
- **Fix:** "At a quarter to six Yeo had blown…", or swap the two sections.

**C9 — Records against prose. Verified. Low (records).**
- The continuity file §0 says "a hundred and forty" was corrected (C4d) and that "the two who held it before me" was removed
  from ch. 45. Both remain (43:207; 45:95).
- The second is partly supported by canon: ch. 23:205, "I've kept it since 2611, when the man who kept it before me died with
  his hand on this glass." **Recommend** "Not the man who held it before me" in the prose, and correct the continuity file §0
  and the ledger records either way.

**C10 — The colour, brushed twice. Reserved; not spent. Owner confirmation.**
- At 6.22: "It was not white. Kiva did not know what colour it was" (45:157). The hull: "It was not white. It was not yellow.
  It was not the colour of anything she could have pointed to" (48:311).
- Kiva connects neither to the dream's colour, and the colour is not named. This is inside the packet ("a light… like no lamp
  in Saltmere"). A reader will make the connection. Confirm this is the intended hint.

**C11 — Kiva's doors "lying down for forty-nine minutes". Verified internal. Low.**
- 45:145 and 45:299 say her doors had lain down since the ward came up (6.15). At 44:419–443 she held her still door open
  against the pull until the cut at 6.16 and read the cask's count through it.
- **Fix:** "which had lain down since the cut" / "for forty-eight minutes".

**C12 — The second crossing against the certificate. Apparent (rules). Low; owner note.**
- Orla's line on the certificate says "one in seven days". The Chair enters the second as "against her healer's card… and
  against the rate on her certificate… Not an incident: not a sanctioned event, and the rate is the healer's to enforce"
  (46:295).
- It is handled on the page, and it is the right ending. It also sets a precedent: certificate conditions breached outside
  sanctioned events carry no Board consequence. Confirm for Book Three.

**C13 — Plan items not paid. Plan.**
- **Hollis Vane** is absent. CHARACTERS.md: "Directs the Line's part at the Slack." The packet does not ask for him; the map's
  cast plan does.
- **Carrow and Kiva** ("each uses a piece of the other's method at the Slack", BOOK_MAP §9). Carrow uses Kiva's declared,
  single, read door (44:43); Dray and Carrow make a lay between two (44:105–109). What Kiva takes from Carrow is not shown.
  One line at 48:57–61 would pay it (Kiva: "Your lay's how the planks kept her count").
- **Peverell's** "I'll say it was wrong in front of the Board on Wednesday, in seven columns" (41:185) is not shown on
  Wednesday. It is partly paid at 48:205 (Rusk's sheet).

**C14 — "Old Four had protested Seven's Carry" (41:273). Checked: ✓** (ch. 27:399–403, dismissed). Listed because a reader
may doubt it; it holds.

**C15 — Voice: "I'd want" is the new shared idiom. Verified count.** See §4g.

**Knowledge boundaries (checked, all PASS).** Kiva's knowledge of the three written accounts arrives at the box (46:271–277:
"She had not known about the sister's book, or Kellan's sheet") ✓. Hart knows *no answer* from Mara (47:49), consistent with
Mara reading the book ✓. The Proprietor's knowledge of Rhea's Monday night (47:233, "I'm told") is plausible through Kellan.
The colour stays Kiva's ✓. The commission is barred from asking about the dream ✓.

**Power limits (checked).** No third door; asked and refused with reasons (43:83–101) ✓. No fourth ✓. Disk cold at 6.22 and
at the hull (45:183; 48:323) ✓. Students close nothing; the tear closed by Ivey's crew ✓; cuts on a slate (Yeo's for the
wall; Rhea's for the cask) ✓. No Glory master does a student's or fitter's work ✓. Physical states carried: Bannock frosted
hip to boot; Pettit's boots; Jude's knuckles; Perrin lifts nothing; L. Hosken's hand ✓.

### 3c. The ending: against BOOK_MAP §3, the packet, and what a reader needs

| Promise (BOOK_MAP §3 / packet) | On the page | Result |
|---|---|---|
| Three handed crossings in a row; every mark tested first | 43:211–243 marks tested in the minute; passes 1–3 in ch. 44 | ✓ |
| Students stand the wall, carry, cut on a slate, bag | 44 §1–2; 44:449–457; 46 §3 | ✓ |
| First link fails → a certified crossing, mast, office's reader | Bannock (44:171); crossing 6.11.40 | ✓ |
| Second link fails → a second crossing, against the card, price said first | Lyle (44:277); Aske's ten (44:315); Perrin (44:335); 6.14.50 | ✓ |
| No third failing link; three doors stay three | ✓ | ✓ |
| Professionals close the tear; fitters and keepers fill 36 cells on 36 counts under Mara, Hart, Peverell | 44:115; ch. 45 | ✓ |
| Mara does not read the bank; touches a cell only when she decides | 45:213–215; 45:251–265 | ✓ (strongest secondary payoff) |
| The Proprietor holds the pumps; the operation cannot finish while he holds; he lets go of the bank and, in writing, the claim | 45 §1, §5 | ✓; the cost (print, pulse, first cell) is real and shown |
| The Master holds a ward across the mouth; cannot move | 44 §5; 45 §4 | ✓ but see C1, C5 |
| Two Glory fields touch; every lamp to a point; three who dreamed count together; unexplained | 45 §2; 46:261–273 | ✓ |
| The bank comes out; the pumps stand; the low town takes water; nobody dies | 45; 46 §4 | ✓ |
| The prediction opened and read honestly, including where wrong | 46 §5 | ✓ (C6 is a nicety) |
| The grid order; slower, dearer, uneven; costs light, money and a house's oldest property | 47 §4 | ✓ |
| Not settled whether the Proprietor was right; no fool, no villain | 47:179–185; 47:229 | ✓ |
| Kiva's cost: the hand to the wrist for three weeks; one in fourteen | 46 §1; 47 §0 | ✓ |
| The sequence asked twice in the book, refused twice | M3 and 43:83–101 | ✓ |
| The 30th: each says no to something; no seat; a name on the commission under another officer's hand with *either of us*; two conditions of Kiva's own | 48 §2–3 | ✓; the conditions are hers, not a pattern |
| The four go four ways by their own choices, each in a scene | Jude 46 §4; Kellan 47 §6; Perrin 47 §7; Anwen 48 §5; Pru keeps Seven 48 §0 | ✓ |
| Relationships landed (Pike, Rhea, Orla, Mara, Anwen, Perrin, Kellan, Pru, Dray, Carrow, Hart; Orla–Hart) | 47 §8; 48 §2–3; 46 §6; 47 §2; 48 §5; 47 §7; 47 §6; 48 §0; 48 §1; 47 §1 | ✓ except Carrow–Kiva half-paid (C13) |
| Wires vouch the engineer; a hull from the south with a light like no lamp; the disk cold; she writes it | 48 §6 | ✓ |
| Reserved: filter's loss, cause, what attends, the disk's purpose, Annick's death, the first trilogy, a single doctrine, nations, Kiva's class, "Breach" | none spent; "Breach" 0 | ✓ (C10 is a hint, not a disclosure) |

**Is the ending earned?** Yes, with two qualifications.

- **What earns it.** Every capability used at the climax was shown and priced earlier: the handed crossing, the week's
  crossing, the far edge, the ten-count, the quiet, the thirty-six counts, the jars, the Graving, the lay, the hands, the
  still door that wanted to beat. Every failure was planted in rehearsal (Bannock's "It's water", Lyle's foot, the Proprietor's
  "simpler"). The cost lands on the person who chose it, after the price was said twice. The Proprietor's act is motivated by
  something he *felt*, not by persuasion, and he keeps his belief. The last image opens outward without explaining.
- **Qualification 1 — the climax's logic** has three visible holes a careful reader will find (C1, C2, C5). They are line
  fixes, but they sit exactly where the book asks to be believed.
- **Qualification 2 — the coda's shape.** Ch. 46–48 resolve about fifteen threads in twenty-four sections. Several scenes end
  by stating their meaning after the action has shown it, which the packet warns against:
  - Pike, 47:339: "That's the whole of it. Two people watching the other one's far edge…"
  - Anwen, 48:243–247: "In two places. Not one of us for the other."
  - Perrin, 47:285: "I'd like it known that I was nearly wrong, and wasn't… That's how I know it's mine."
  - Jude, 46:205–207: "I think that's what it's for."
  - Kiva's book, 41:347 and 47:133, writes the lesson after the narration has already said it.

  The scenes themselves are right for a book's ending. The repetition is in their last lines.

---

## 4. Numerical formula alignment

Measured by `provenance/tools/m6_metrics.py` (a copy of `m5_metrics.py`; only the chapter range, labels and viewpoint map
changed; §7), so the figures are comparable with Movements Two to Five. "M5r" is Movement Five as repaired
(`MOVEMENT-005-REPAIR.md` §5). Anything marked *manual* is the reviewer's judgment.

### 4a. Sentence rhythm — **the long tail now overshoots; the median is unmoved**

| Metric | Target | **M6 all text** | M6 narration* | M6 dialogue | M5r all | M5r narration |
|---|---:|---:|---:|---:|---:|---:|
| Mean words | 14.6 | **11.8** | 13.6 | 6.9 | 10.56 | 12.3 |
| Median | 11 | **7** | 8 | 4 | 7 | 8 |
| Population SD | ~26 | **12.0** | 13.6 | 7.3 | — | — |
| ≤5 words | 27.7% | **38.9%** | 35.9% | 59.3% | 40.3% | 36.6% |
| ≥40 words | 3.3% | **4.6%** | **6.8%** | 0.7% | 2.3% | 3.8% |
| Longest | — | 85 (47:153) | — | — | 73 | — |

\*Narration has quoted spans removed. 4,781 sentences; dialogue is **27.0%** of words (M5r 32.3%).

- **Per chapter.** Short share from 33.1% (ch. 41) to 43.1% (ch. 44); long share from 3.8% (ch. 47) to **6.8% (ch. 44)**.
- **Read.**
  - The mean is the highest in Book Two (11.8), and the whole-text long share now **exceeds** target for the first time (4.6%
    against 3.3%; narration 6.8%). The packet asked for "a few well-built 35–55 word sentences"; ch. 44–45 used many.
  - **The packet's "no *and … and* chains over about 45 words" is broken 27 times** (sentences over 45 words with five or more
    *and*). The worst: 47:153 (85 words, nine *and*s, the grid order); 44:87 (77); 48:77 (76); 46:105 (74); 45:131 (73);
    42:359 (72); 47:291 (70); 44:329 (69, seven *and*s).
  - Several of those are the climax's best long sentences (45:131, the count going out of the Proprietor; 44:349, the run) and
    should stay. The summary ones (47:153, 47:291, 46:139) should be split.
  - The median (7) and short share (38.9%) have not moved toward 11 and 27.7%. The gap is still mostly dialogue (59% short).
    The owner question about whether the targets govern dialogue remains the only lever left.

### 4b. Paragraphs and scenes — **scene rhythm near target; paragraph mass the heaviest yet**

| Metric | Target (ASR proxy) | **M6 (typographic)** | M5r |
|---|---:|---:|---:|
| Paragraph median / mean | 18 / 26.8 | **24 / 39.5** (1,430 paragraphs; **26.5%** over 60 words) | 25 / 37.6; 23.6% |
| Paragraphs over 110 words | — | **96** | 75 (M5 first draft) |
| Section mean | ~950 | **1,027** (55 sections) | 1,421 |
| Breaks per 10k, internal | ~8.7 | **8.32** | 5.59 |
| Breaks per 10k, with chapter openings | — | 9.74 | 7.04 |

- **Scenes are the closest to the formula in Book Two.** The operation's long passes (44 §2 2,157; 44 §5 1,644; 45 §1 1,942) are
  continuous and stay unbroken, as the packet asks. The trestle (41 §3, 3,158) is the one long block; it is one continuous
  scene.
- **Paragraph mass is the worst in the book.** Heaviest: 41:243 Kiva's plan (198); 47:153 the grid order (188); 41:139 the
  meeting roster (184); 41:75 Aske's price (183); 47:179 (176); 48:165 Kiva's first condition (173); 46:263 the Clerk's thing on
  no line (169); 47:53 (167); 44:113 the tear's close (167); 43:95 the refusal (163). Speeches set as single blocks again. One
  beat or interruption in each would pull the median down without cutting a word.

### 4c. Readability

| Metric | Target | M6 | M5r |
|---|---:|---:|---:|
| Flesch Reading Ease | 72.3 | **93.3** | 93.8 |
| Flesch-Kincaid grade | 6.8 | **3.2** | 2.8 |
| Syllables per word (estimator) | — | 1.20 | 1.21 |

Method: regex word tokenizer; sentence splitter guarded for Mr./Mrs./initials; vowel-group syllable heuristic with silent-e
trimming. Names (Peverell, Polglase, Hosken, Pascoe) raise the estimate slightly. Longer sentences raised the grade; the
vocabulary stays plain. Flesch under-reads the procedural difficulty of quench/draw/set and the certificate's conditions.

### 4d. Progression vocabulary — **rises again at the climax, as the packet asked**

The lexicon is unchanged from Movements One to Five.

- **Raw:** 265 hits = **46.9 per 10k** (M5r 48.7). Top: doors 132, Ember 31, crossing(s) 28, Barrel 15, certif* 13, licen* 9,
  crossed 8.
- **Manual adjustment (same method as M5).**
  - **Doors.** All 132 contexts read. **29 are literal or figurative** (Quiller's door, the green door ×5 with the back door, the
    pump house and warehouse doors, Ropery Row's doors, "a shut door" face, "waiting by the door" ×2, "as a hand presses on a
    door", "through a door" of the gate, "a door is opened somewhere in the house", the loft door and Mara's knock ×2, "a door
    to open" in the Tanyard). **103 are the door system**, including "the other side of her door" for Thrale's ward.
  - **Hold.** 3 of 4 are the verb ("Hold that", "Hold it", "Hold the jars"); 1 is the role (42:169). Remove 3.
  - **Adjusted (M5 method):** 265 − 29 − 3 = **233 = 41.3 per 10k** (M5 37.9). "Draw" ×2 is Mara's can-drawing command;
    removing it gives 231 = 40.9. All 8 "crossed" are the system sense.
- **Within the movement by equal-word thirds:** 62 / **119** / 84 raw. The middle third (the Slack, ch. 44–45) carries nearly
  double: the system surfaces "at genuine turning points", exactly the formula's shape after the opening third.
- **Ash-economy terms:** 8.9 per 10k (M5 9.6).
- **Cumulative by movement (manual-adjusted, provisional method).**
  - Opening third (M1 + M2): about 51–55 per 10k (Movement Two review).
  - Everything after: (580 + 233) / 218.4k ≈ **37.2**.
  - **Front-load ratio ≈ 1.37–1.48** against the source's ~1.7×.
- **First whole-book measure by equal word-count thirds (raw, now that the book exists).** Using m6's lexicon and tokenizer
  verbatim on chapters 1–48 as they stand in the working tree, minus the automated literal-door phrases only (§7):

  | Book third | Words | Hits | Per 10k |
  |---|---:|---:|---:|
  | First | 108,722 | 553 | **50.9** |
  | Second | 108,722 | 441 | **40.6** |
  | Third | 108,722 | 481 | **44.2** |
  | Whole book | 326,166 | 1,475 | **45.2** |

  - **Ratio, first third to the rest: 1.20×** (the source: ~1.7×; the source's own thirds were 900 / 471 / 514, which is
    1.83× by the same calculation). This raw ratio is lower than the movement estimate because the raw count keeps literal
    doors that earlier reviews removed by hand, and the final third rises (the Lane and the Slack turn on doors).
  - **The whole-book density (45.2 raw, about 39 adjusted) is under the 58 target.** That has been the standing owner decision
    since Movement Two: keep the front-loaded shape at the cost of the average. The shape is now front-loaded but shallower than
    the source, with a late rise the source does not have. **This is a formula departure for the owner, not a defect to chase
    with vocabulary.**
  - Caveat: chapters 11, 14, 15, 19 and 24 include uncommitted audio-repair edits; those are small and do not move these
    figures materially.

### 4e. Development beats

**Kiva (manual): about 36 choices or realizations, about 6.4 per 10k** (target 4.5; M5 7.8). By chapter: ch. 41 ×8, ch. 42 ×5,
ch. 43 ×3, ch. 44 ×7, ch. 45 ×1, ch. 46 ×3, ch. 47 ×4, ch. 48 ×5. Representative:

- She puts her name down as caller, "One crossing kept, as certified" (41:115)
- "Nobody carries it far… three passes, and none of them longer than fifty" (41:243)
- "And if two fail?" / "Then I've a healer who said the price… I'll hear it again" (41:253)
- She understands the laid habit is why the hour failed (41:321)
- The word has to belong "to nobody's ear in particular" (41:341)
- "She had been calling the pass for four months as though it were hers" (41:343)
- *The call's not mine… Teach it so they can* (41:347)
- "It's going to the nearest thing that keeps time" (42:57)
- "I can't call it… I need somebody else's count, named before" (42:93)
- The marks can only be tested in the minute (42:337)
- "She found she was going to miss it" (42:363)
- The refusal, with reasons (43:83–101)
- "Never once… entirely inside her certificate, on her own word, that mattered" (43:209)
- "She did not decide it. She had decided it on Monday" (44:183)
- "Count me ten" (44:311)
- She waits for the brake and is not given it (44:331)
- "It's only wanting" (44:429)
- She asks her still door what it knows (44:441)
- "It was the first entry in the column that was not *yes*" (46:11)
- "It's gone back to a hand. That's whose it was" (46:89)
- "She found she could sleep in it" (46:379)
- She keeps the log on Hart's reasoning (47 §1)
- "Ivey. You call it" (47:107)
- *My sheet's wrong on the first line of the limits* (47:133)
- She sits halfway down the table (47 §5)
- "No… Because I'd stay" (48:125)
- "Come on the commission… I'd want you there" (48:133)
- The two conditions (48:159–169)
- *The disk is cold.* (48:333)

**The cadence is above target and evenly spread except ch. 45**, which is the two cutaways' chapter by design. The one risk is
restatement: "the call isn't mine / somebody else will call it" is realized at 41:343–347, applied at 47:107, written at
47:133, made a condition at 48:159 and given to Anwen at 48:227–233. That is a planted arc paid in steps, not padding, but the
narration twice explains it after the scene has shown it (41:345; 47:129).

The regex proxy (58 windows, 10.3 per 10k) is reported only for reproducibility; it is inflated by pronouns near "found that",
"decided" and "understood".

**Supporting cast (manual).** At least 24 named people get a beat, spread wide; nobody becomes a deuteragonist, though Kellan
comes close inside this movement (his two cutaways and two Kiva-side scenes):

| Person | Beats |
|---|---|
| Kellan | "the first job… that's exactly what I'm for"; "What happens when you let go of a pump that's only got you?"; the sum and "Twenty-two"; witnesses under his own name; reads the price; the second card, yes, "from the inside, where it's harder" |
| Mara | "a bucket with no bottom"; "I'll not ask anybody to run"; "Say you can't tell. That's a word as well"; the 6.24 line on her name; case nineteen, "Mine"; signs as guardian and asks nothing |
| Perrin | "I'd want to know what the bucket weighs"; "It can't be done by strangers"; captains from the wall; declares the second crossing, "it's mine as well"; on being envied; "nearly wrong, and wasn't" |
| Anwen | the ward line learning one voice; frightened and does not tell; "That makes me hers"; leads two passes; Graywater; "Not one of us for the other" |
| Jude | asks what the Barrel's ash is for; "I'd want it said I was frightened"; sweeps the corners; yes to Yeo with a condition on every bag; gives Pru the book |
| Pru | calls the catchers' far edge; bags first on her own sheet; no to Ivey; "Finch is not grateful. Finch is good."; "I did not" |
| Rhea | takes the count; *Not mine to keep*; writes Kiva in under Coombe; "Graywater's mine. You're not." |
| Orla | the line struck; "It doesn't make the Bench right." "No." "Good."; "I let go of you before. It was proved after." |
| Pike | names himself Kiva's far edge; "It's a hard job. I'd not known"; smiles the whole way |
| Dray | "It's looking at the pipes"; calls every pass on her feet; "That's fairer"; "That's not friendship" |
| Others | Aske (the price twice; the fourteen; "I said it right"); Hart ("Write it down, somebody"; owns the misses; what a ruined hand can be asked); the Proprietor (one hold; the claim; "I'm only certain I let go"); Thrale ("Write that you counted"); Coombe (the rope; the commission); Rusk ("You might have opened your eyes" / "I believe it. It's happened."); Peverell (six, not eight); Lyle ("I'm saying it before"); Bannock ("It's water"); Carrow; Ivey and Tamsin; L. Hosken; Brask (the cask); Mrs. Penhale; Noa ("I drew one wrong once"); Yeo |

### 4f. POV word share (viewpoint segments, not name frequency)

**Segments** (0-based sections after splitting on `---`, from a fresh listing of all 55 sections' openings; §7):

| Segment | Lens | Note |
|---|---|---|
| ch. 42 §1 | Anwen | the ward line on the Graving floor |
| ch. 45 §0, §3 | Mara | the landing, before and after the lift |
| ch. 45 §1, §5 | Kellan | by the chair; the fault paper |
| ch. 46 §6 | Orla | the Chair's ledger; the gallery with Hart |
| ch. 48 §2 | Rhea | the tailboard and Coombe's sheet |
| everything else | Kiva | including 47 §2 ("Orla found her…"), 48 §4 ("Mara signed it…") and 47 §8 (the Tanyard), all narrated from Kiva's side |

Each cutaway opens on its lens by name and a cue only that person has ✓. No new lens ✓.

| Lens | M6 words | M6 share | Cumulative M1–M6 (M2–M5 as repaired) | Cumulative share | Target |
|---|---:|---:|---:|---:|---|
| Kiva | 48,218 | **85.4%** | 281,660 | **86.4%** | ~87% (85–90) |
| Mara | 2,237 | 4.0% | 11,173 | 3.4% | 2.5–3.7% |
| Kellan | 2,740 | 4.9% | 10,946 | 3.4% | 2.5–3.7% |
| Rhea | 844 | 1.5% | 8,184 | 2.5% | 2.5–3.7% |
| Orla | 1,004 | 1.8% | 7,490 | **2.3%** | 2.5–3.7% |
| Anwen | 1,420 | 2.5% | 6,431 | **2.0%** | 2.5–3.7% |

- **The book's total is 325,884 body words** (M1–M5 cumulative from the M5 review, adjusted by the M5 repair's deltas: Kiva
  +264, Mara +17, Orla −2; plus M6). Expect ±0.1 point across tokenizers.
- **The book holds its lead share** at 86.4% and its secondary share at 13.6% across five lenses, as the formula's §6 asks.
- **Two lenses finish under band**: Anwen (2.0%) and Orla (2.3%). Rhea is at the floor. Mara and Kellan finish inside it.
  Kellan's 4.9% in this movement is right for the story (his decision happens where Kiva cannot see), and the book total is
  inside band.
- **The author's count agrees exactly:** Kiva 48,213 of 56,457 by the author's tokenizer; the script gives 8,244 cutaway words,
  identical to `MOVEMENT-006-CONTINUITY.md` §6.

### 4g. Secondary signals (optional per formula §8)

| Signal | Source band | **M6** | M5 | Note |
|---|---:|---:|---:|---|
| "that" | 92.1 (tighten below) | **98.5** | 113.2 | down a long way; still slightly over |
| just / almost / felt / seemed | 5–25 | 0.9 / 0.2 / 6.9 / 0.2 | 1.5 / 0.4 / 5.1 / 1.3 | — |
| -ly words | ~161 | 32.4 raw; **22.1** filtered | 22.5 | "slowly" **14** (matches the author's count), "carefully" 13, "exactly" 10, "nearly" 10 |
| Quote-adjacent tags | ~41 | **57.0** | 51.1 | "said" is 111 per 10k by bare count |
| Combat terms | ~22 | **9.0** | 8.9 | the inherited lexicon misses this book's action words (*carry*, *plant*, *take*, *nobody*); a lexicon limit |
| "out of the" / "one of the" / "for a moment" | 2–4 | **4.8** / 0.2 / 3.4 | 2.9 / 1.6 / 2.5 | "out of the" just over band |
| House trigrams | — | "she did not" **13.6**, "looked at the" 9.6, **"the dock floor" 9.0 (51)**, "she looked at" 8.0, "did not look" 7.3 | "she did not" 15.4 | the "looked at" family persists; "the dock floor" is a place, but 51 uses is audible |
| Causal *since* | packet: *because* | **0** (all 73 temporal; non-temporal candidates read) | 4 | ✓ fixed |

**Tics and voices (raw counts in 56.5k words).**

- **"I'd like it known" 3, all Perrin** (44:339, 47:285, 48:257) ✓. **"I want it said" 4, all Anwen** ✓. **Jude's "I'd want it
  said" 4** (43:25, 44:75, 46:155, 46:205), at his heaviest lines, as the packet asked ✓.
- **"I'd sooner" fell from 13 to 0** ✓ — and **"I'd want" rose from 3 to 23–24 across eleven speakers**: Aske, Perrin ×2, Dray
  ×3, the Proprietor ×4, Jude ×5, Mara ×2 (counting 46:243), Hart, Kellan, Carrow ×2, Rhea ×3, Anwen. The idiom moved; it was not
  rationed. Nearly every use pairs with "said / written / known / clear / on my card", which is also the movement's theme
  ("say it before; write it down"). The theme is being spoken in the house voice.
- **"scarlet" 7** (Pru's tag), "went red/pink" 3, "something moved at the corner" 3, "said nothing" 3, "nobody" 107 (the
  call word, so expected), **"four and four" 35** (the beat; motif, but at 6.2 per 10k it is close to a tic in the coda where
  nothing keeps time).

---

## 5. Movement Five repair state in `STATE_LEDGER` against chapters 41–48

| Ledger item (M5 block, as repaired and rechecked) | In chapters 41–48 | Result |
|---|---|---|
| Seventeen; seated; unclassified; on the roll | Unclassified to the last page; commission line, no column | PASS |
| No crossing in M5; hand warm Thu–Sat (4–6 mornings) | "Eight mornings" Mon, "Ten mornings" Wed | PASS |
| Aske said the price twice (Thu, Sat) | "I said the price twice last week, for the seventh" (41:71) | PASS |
| The week's crossing kept for Wed 23rd; nobody has asked | Kept; spent at 6.11.40 | PASS |
| Right hand: blisters, linen, left-handed writing | Left-handed Mon; "only just finished peeling" Wed (46:9) | PASS |
| Fever the third; no dream; "Nothing came" | No fever after two masters touching (46:343) | PASS |
| Disk cold | Cold at 6.22 and at the hull | PASS |
| Yes/no log at a quarter to seven | Mon latch *yes*; from Wed *no answer*; ninth day Thu 1st | PASS |
| Dream public; colour Kiva's alone | Commission barred from asking; colour unnamed (C10) | PASS |
| Lane 7–2 / 4–5 / 6–5; 17 for, 12 against; Seven 69, seventh | **41:273 reverses Saturday's lane** | **FAIL (C3)** |
| Roll of eight; warrant: none obliged | Westerley first and Holloway first decline, "Loses nothing by it" | PASS |
| Book 5.15; sealed 2.0 bound; refused to the Committee | 5.15; sealed opened for a hand, 0.8 left | PASS |
| Perrin: card "a fortnight from Wednesday" | "No plant, no lift. Till the 30th" (41:107) | PASS |
| Jude: nothing gripped with the left till Monday | Signs left-handed "because Aske had said Monday" (41:111) | PASS (a lovely payoff) |
| Pru: caps; two torn | Two torn at the catchers' plank | PASS |
| Anwen taught Lyle to lean (Thu) | 42:169 "on the Thursday after" ✓; but "eight days ago" | PASS with C4e |
| Offers: Anwen yes; Jude after Wed; Perrin Works open; Kellan's white card | All resolved in scenes | PASS |
| Kiva: none; Rhea will ask on the 30th | 48 §3 | PASS |
| Thirty-six jars; cellar 4; price (never stepped while the pump house stands) | Grid order extends it nationally | PASS |
| The Proprietor's hand never lifted; "sure of my reading" | Lifted at 6.22.11; "not certain I was wrong" | PASS |
| Thrale: an hour at a time; doors lie down at forty | Overruns by 14 min; the forty broken at the sill | **FAIL (C1, C5)** |
| Mara: has not touched a bank cell; teaching the 36 | Until 6.30, case nineteen | PASS |
| Orla: one true sentence; asked to be struck | Struck "on evidence"; with Hart "No." "Good." | PASS |
| Hart's springs/neaps behaviour | "held its hour for a fortnight while the sea gate's table walked" (41:167) | APPARENT: M4 records that the basin walks with the table at the neaps; "a fortnight" reads as across the neaps. Recommend "at the springs". |
| Noa: fourth column; two hairs; no line | Third hair at 6.22; struck *not entered as fact* "neatly" | PASS |
| Dray: "I'll be there. On my feet." | Calls every pass on her feet | PASS |
| Carrow: "I want to be on the wall" | "That's the wall, Miss Carrow. You asked for it." | PASS |
| Rhea: one night left; card ends the 30th | The Tanyard Mon 28th; the 30th | PASS |
| Owner items carried (dialogue targets; progression shape; section rhythm; the colour's existence public; Thrale's presence and fever) | Section rhythm near target (§4b); the fever line consistent (no fever with two masters); others carried | carried |

**The author's Movement Six ledger block and continuity file against the prose.** They agree with the page on every dated
event, injury, ash figure, ruling, offer and knowledge change I checked, with these exceptions:

1. Continuity §0 says "a hundred and forty" was corrected to "a hundred" (C4d) and that "the two who held it before me" was
   removed (C9). Both remain in the prose.
2. Continuity §0 says the basin tear's close was fixed at 6.14, but Carrow's "eleven minutes" (48:57) was not reconciled (C4b).
3. The ledger M6 block and continuity §7 list Thrale's "74 minutes in the town" correctly but do not record that she moved
   while holding (C5).
4. The ledger M6 block should note the Saturday-lane line (C3) once repaired, since it touches the M5 record.

---

## 6. Repair brief — three priorities, bounded

**P1 — Make the climax obey its own rules (C1, C2, C5, C7, C11).**

- *Location:*
  - 41:223 and 43:113–117, 147; 44:407 (where the Master stands until the plant is called)
  - 43:269, 43:301; 44:25, 44:75, 44:139 (the cask's height)
  - 45:279–293 and 43:119 (the step back; "she'd say so first")
  - 43:143 (Carrow and Dray's bearing)
  - 45:145, 45:299 ("lying down" since the ward)
- *Observed issue:* the Master stands within her own forty paces of the sill plank, which works anyway; a 4 ft 11 cask holds
  water over a tall man's head; a master who "cannot hold it and move" moves, and a promise to "say so first" is dropped; the
  cutters stand at the wrong end of the wall.
- *Effect on the reader:* these sit exactly where the book asks to be believed. The adult genre reader tests the rules first;
  the young reader loses the picture of the cask.
- *Proposed scope:* line edits only; no event, outcome, time or cost changes.
  - The Master waits back along the outer quay (about sixty paces) until the plant is called; Yeo or the sister says so once at
    the trestle; at 6.15 she "came along the outer quay and down the steps".
  - Replace "over their heads" / "the height of a man" with eye- or chin-level phrasing.
  - Price the step (the ward shivers; the flood comes a hand nearer) or have the sister say she can take one slow pace; at about
    6.50 let the sister say "She says she'll be late. She's saying it first."
  - "Back along the wall toward the pump house" at 43:143; "since the cut" at 45:145 and 45:299.
- *Strength to preserve:* **do not shorten any pass in ch. 44 or the lift in ch. 45.** Keep Bannock's "It's water" / "Tomorrow it
  won't be", Lyle's "I'm saying it before", Aske's count with the price inside it, Perrin's "it's mine as well", "the way a lamp
  goes when somebody turns the key the whole way down", Pike's "Far edge", "It's one hold. Not two", "Twenty-two", and the
  Master's "Write that you counted, and that you don't know what."

**P2 — Make the sums, clocks and records true (C3, C4a–k, C6, C9).**

- *Location:* 41:273; 44:305, 349, 203; 48:57, 205; 43:207; 42:169; 46:297, 63; 45:101, 95; 47:293; optionally 46:251–253;
  `provenance/MOVEMENT-006-CONTINUITY.md` §0 and the ledger M6 block, reconciled to whatever changes.
- *Observed issue:* Saturday's lane is reversed against ch. 37; about a dozen clocks, counts and small facts do not add (§3a); two
  corrections the continuity file records were never made.
- *Effect on the reader:* the counting reader trusts the operation because its clocks join to the second (6.22.11 + 9 s = 6.22.20).
  A wrong "eleven minutes" or "a hundred and forty paces" breaks that trust in the same chapters.
- *Proposed scope:* the line edits listed under C3, C4 and C9; one optional clause for Hart (C6). Then reconcile the continuity
  file and ledger, and record what changed in a repair report.
- *Strength to preserve:* the prediction read verbatim and judged line by line; "not tested, by design"; "I've never been early,
  and I was early"; the Clerk's "That's a better record than most sealed papers"; the tin's 1.2 / 0.8; Pru's *Held 5.15*.

**P3 — Lighten the coda's repeated shape and the house voice (§3c qualification 2; §4a; §4b; §4g).**

- *Location:*
  - closing restatements: 47:339 (Pike), 48:243–247 (Anwen), 47:285 (Perrin), 46:205–207 (Jude), 41:345 and 47:129
    (narration after the scene)
  - "I'd want" ×23–24 across eleven speakers
  - the summary chains 47:153, 47:291, 46:139, 48:77
  - the heaviest paragraphs (41:243, 41:139, 41:75, 47:179, 48:165, 46:263, 43:95)
  - the three-accounts paragraph at the box (46:263–267), which re-reads lines the reader saw
- *Observed issue:* about a dozen after-scenes end by stating their lesson; the theme ("say it before, write it down") is spoken
  in a shared idiom; the packet's 45-word chain rule is broken 27 times; paragraph mass is the heaviest in Book Two.
- *Effect on the reader:* the coda tells the reader what the climax meant after it has already shown it, and by the Mole the
  pattern is audible. Read aloud, the 180-word speeches become testimony.
- *Proposed scope:* a focused same-author pass. Cut or shorten the last line of four or five restating scenes (keep the action and
  the image that ends them). Recast about two-thirds of "I'd want", keeping Jude's four, Dray's "I'd want that clear", Rhea's "I'd
  want it on every card" and the Proprietor's "where it happened". Split the four summary chains. Break each speech over about 150
  words once with a gesture or interruption. Compress the three accounts at the box to one sentence that names the three sources.
  Leave dialogue length alone until the owner rules.
- *Strength to preserve:* **the Tanyard (47 §8) entire**; "Davy never did the corners"; "It doesn't make the Bench right." "No."
  "Good."; "Graywater's mine. You're not."; Coombe's "That's a better first line than mine was"; the Proprietor's "I'm only certain
  I let go"; Kellan's watch "four seconds behind… he knew which four"; Mara's knock "as a joke"; Pru "I did not"; and the last
  section (48 §6) word for word, from the ninth *no answer* to *The disk is cold.*

**For the owner, not prioritised:**

1. **The colour, brushed twice** (C10). Confirm the hint at 45:157 and 48:311 is intended.
2. **The certificate precedent** (C12): conditions breached outside a sanctioned event carry no Board consequence; the rate is the
   healer's. Confirm for Book Three.
3. **New interaction properties** (continuity §14.5): reading a count through the still door; the Proprietor's "one hold" and the
   first cell going to its own count; Thrale's ward holding water and the flood as well as the count; Hart's hand quiet near six
   counts; packs keeping no count after the bank came out; no fever after two masters touching.
4. **The bible's §6 revised in-world**: the caller need not have crossed (Ivey; Kiva's second edition). Confirm before Book Three
   leans on the old line.
5. **Plan items** (C13): Vane absent from the Slack; Carrow–Kiva half-paid; Peverell's promised seven columns.
6. **Formula conflicts, standing:** whether the sentence targets govern dialogue (open since Movement Two); the progression shape
   (whole-book raw 1.20×, movement estimate 1.37–1.48×, against ~1.7×, with a late rise); the whole-book progression density
   (about 39–45 per 10k against 58). These are owner decisions, not things a repair should chase.

**Strengths to protect in any repair:**

- "One morning of somebody who won't" — and "It's the first job I've ever been offered that's exactly what I'm for."
- Mara's bucket with no bottom; Brask's "The water's its head. And the head's keeping time."
- Rusk: "You might have opened your eyes." / "I'd not have heard it better."
- The rope drill and "That's strangers stopping."
- "It's not going to the nearest thing. It's going to the nearest thing that keeps time."
- "Unless they keep its count."
- "If this morning needs my three, it's not a method. It's me."
- "That was a girl saying no to a rich man. This is a catcher saying no to a method."
- The quiet going out of the stone "the way warmth goes out of a cup".
- "Two words, once." / "That's the easy part."
- "Say you can't tell. That's a word as well."
- "It sounds like six bands at a fair." / "It sounds like a pump house."
- "We found it… We've been claiming the road ever since."
- *Used, 1.2. Left, sealed, 0.8. Bound as before.*
- "I'll carry it up a bank for six months. Every bag."
- The prediction, read verbatim and judged honestly.
- "I've believed one thing for seventy-seven years… I'm only no longer the man who owns it."
- *Then we look again, and either of us may say no.*
- The hull, and *The disk is cold.*

---

## 7. Method — reproducible commands, script hashes and limits

Main command, run from `/Users/drive/kindling-2680-book-02/books/book-2680-national-measure`:

```
python3 -I provenance/tools/m6_metrics.py manuscript
```

- `provenance/tools/m6_metrics.py` SHA-256 `958bc9aa8e066bf64570479cb2756fd176de28e45aa064512b9d4ab155136c12`.
- Copied from `provenance/tools/m5_metrics.py`, SHA-256
  `9bb5f801c6bfb0e585cdd25897c669eb020786d5ca07d418ef7806a785f0eb49`. That matches the hash recorded in the Movement Five
  review and repair, so the source was unmodified.
- Full diff (only the docstring label, the chapter range and the viewpoint map changed):

```
2c2
< """Movement Five numerical pass (copy of m4_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m5_metrics.py <manuscript_dir>"""
---
> """Movement Six numerical pass (copy of m5_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m6_metrics.py <manuscript_dir>"""
6c6
< CHS = list(range(33, 41))
---
> CHS = list(range(41, 49))
10,12c10,12
< POV = {(33, 3): "Anwen", (34, 2): "Mara", (36, 0): "Kellan", (37, 4): "Rhea",
<        (39, 0): "Orla", (39, 1): "Orla"}
< # 39/1 opens "He was on the gallery" but is Orla climbing to Hart; 40/2's closing town survey stays Kiva's section (see report)
---
> POV = {(42, 1): "Anwen", (45, 0): "Mara", (45, 1): "Kellan", (45, 3): "Mara", (45, 5): "Kellan",
>        (46, 6): "Orla", (48, 2): "Rhea"}
> # 47/2 ("Orla found her") and 48/4 ("Mara signed it") are narrated from Kiva's side; 47/8 (the Tanyard) is Kiva's (see report)
```

**How the viewpoint map was derived.** Each chapter was split on `---` lines with the script's own regex. I listed each of the
55 sections' index, body-word count and first paragraph, then checked each against my full reading. A lens was assigned only
where the narration stays inside that person and Kiva is absent or seen from outside. The resulting cutaway total (8,244) equals
the author's continuity §6 exactly; the map was derived independently and then compared.

**Whole-book thirds (ad hoc; not saved in the repository, reproduced here verbatim).** Run from the same directory as
`python3 -I <path>/book_thirds.py manuscript` (the copy used in this session has SHA-256
`75435b220a0023ef9b779f806662d86ecc480434ac9a4e7db99820bf9a16f764`). It reads m6's lexicon, tokenizer and literal-door regex
from `m6_metrics.py` itself, so the definitions cannot drift:

```python
# Whole-book progression by equal word-count thirds, using m6_metrics.py's lexicon and tokenizer verbatim (raw; no manual door adjustment).
import re, sys, os, importlib.util
MD = sys.argv[1]
src = open(os.path.join(os.path.dirname(MD.rstrip("/")), "provenance/tools/m6_metrics.py"), encoding="utf-8").read()
ns = {}
for name in ["PROG_CS", "PROG_CI", "WORD", "DOORLIT"]:
    m = re.search(r"^" + name + r" = .*?(?=^\S)", src, re.S | re.M)
    exec(m.group(0), {"re": re}, ns)
def clean(t): return re.sub(r"[*_]", "", t.replace("—", " — "))
text = " ".join(clean(open(os.path.join(MD, f"chapter-{i:02d}.md"), encoding="utf-8").read()) for i in range(1, 49))
toks = ns["WORD"].findall(text); N = len(toks); third = N // 3
def prog(t):
    n = sum(len(re.findall(p, t)) for p in ns["PROG_CS"])
    n += sum(len(re.findall(p, t if p == r"\brank\b" else t.lower())) for p in ns["PROG_CI"])
    return n - len(re.findall(ns["DOORLIT"], t.lower()))  # minus automated literal-door phrases
out = []
for i in range(3):
    seg = " ".join(toks[i * third:(i + 1) * third if i < 2 else N])
    w = len(seg.split()); h = prog(seg); out.append((w, h, round(h / w * 10000, 1)))
print("tokens", N, "thirds (words, hits, per10k):", out, "ratio first/mean(rest):", round(out[0][2] / ((out[1][1] + out[2][1]) / (out[1][0] + out[2][0]) * 10000), 2))
```

Output: `tokens 326166 thirds (words, hits, per10k): [(108722, 553, 50.9), (108722, 441, 40.6), (108722, 481, 44.2)] ratio
first/mean(rest): 1.2`. Chapters 11, 14, 15, 19 and 24 were read as they stand in the working tree (uncommitted audio edits).

**Chapter SHA-256 at review time.** Identical to `editions/movement-006-first-draft/SHA256SUMS.txt` (`shasum -a 256 -c`: OK ×8)
and byte-identical by `cmp`:

| File | SHA-256 |
|---|---|
| chapter-41.md | 7fe37b1bab648061… |
| chapter-42.md | 80ce66d148cbf962… |
| chapter-43.md | 285b5e53998a9f16… |
| chapter-44.md | c8afd331f9da46b8… |
| chapter-45.md | c0537f7582034164… |
| chapter-46.md | c3de9336841046d4… |
| chapter-47.md | f6e80fd0836bc1a1… |
| chapter-48.md | 1001dce252f525fe… |

**Known limits of the inherited script** (unchanged so runs stay comparable):
- `reserved_terms` is case-sensitive and reports "Unroofed" 0; ch. 46 has the Clerk's "the unroofed sky" (planned, inside the
  boundary). "Breach" is genuinely 0.
- The combat lexicon misses this book's action vocabulary (§4g).
- The literal-door regex removes only 18 of the 29 literal/figurative doors found by reading.

**Manual counts and their limits.**
- **Doors, Hold, Draw, crossed, causal *since*.** Every context was printed and read in-session (132 doors, 4 Hold, 2 Draw, 8
  crossed; 73 *since*, of which the eight non-temporal-pattern candidates were read individually and all are temporal). The
  printing commands are in this session's transcript; the classification is the reviewer's.
- **"I'd want" speakers** were attributed by reading each of the 24 hits in context; one is "I'd wanted" (Carrow, 48:57).
- **And-chains**: sentences over 45 words with five or more *and*, using the script's own sentence splitter (27).
- **Line references** (`ch:line`) are to `manuscript/chapter-NN.md`, where each paragraph is one line.
- **Kiva's development beats and the supporting-cast table** are judgments, not counts.
- **Cumulative viewpoint** adds sources with slightly different tokenizers: M1–M5 via the Movement Five review's table and the
  M5 repair's deltas, and M6 here. Expect ±0.1 point.
- **The arithmetic in §3a** used only figures on the page, the ledger, and the earlier chapters cited.

**Scope boundaries.** Nothing in this report changes manuscript prose, the ledger, the continuity file or `AUTHORSHIP.md`. The only
files written are this report and `provenance/tools/m6_metrics.py`. No repair, commit, push, publish or later chapter.
