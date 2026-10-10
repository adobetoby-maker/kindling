# Kindling 2680, Book One — Prologue + Movement One — editorial review

> Built by TAC

Date: 2026-10-10
Prompt performed: `planning/OPUS-5.5-MOVEMENT-001-EDITORIAL.prompt.md` (5,803 lines, read in full, in order)
Status: review only. No manuscript, canon, plan, ledger or provenance file was changed. This report is the only file written.

---

## 0. What kind of read this is

**Same-model self-review in a fresh context, informed and not blind.** It is not a real human read and it is not independent testing.

- The manuscript was drafted by an Opus 5.5 seat in this worktree. I am the same model. I do not have the drafting transcript in context, but I was given the formula, the book map, the state ledger, the bible, the prologue plan and the author's own continuity checkpoint. That checkpoint anchors me toward the author's intentions, so treat agreement with it as weak evidence and disagreement with it as the more useful signal.
- The two reader lenses (a fluent thirteen-year-old; an adult genre reader) are simulated perspectives. They are not demographic research and imply no sales forecast.
- Scores are editorial judgments, not calibrated measurements. The two lenses are reported separately and are not averaged into a gate.
- A separate cold-read file appeared in `editor/` while this pass was running. I did not open it, so the two passes stay independent.

### Coverage

Nine files, supplied in declared order, all read completely. The movement is complete as supplied (prologue plus chapters 1–8). The text embedded in the prompt was compared with the files on disk and is byte-identical for all nine.

| File | SHA-256 (first 16) | Words (regex count) |
|---|---|---|
| `manuscript/prologue.md` | e5167b91c6ffeb0a | 16,011 |
| `manuscript/chapter-01.md` | 5c8b57f1c4951d2a | 5,414 |
| `manuscript/chapter-02.md` | 8180dd1277600b83 | 4,511 |
| `manuscript/chapter-03.md` | e522e66323c9ba06 | 5,214 |
| `manuscript/chapter-04.md` | 1cfcc0c1eb371df7 | 5,780 |
| `manuscript/chapter-05.md` | ddb92a2cc42055c7 | 5,244 |
| `manuscript/chapter-06.md` | 05f625c46c96aef9 | 5,478 |
| `manuscript/chapter-07.md` | 44138e874fde0114 | 4,810 |
| `manuscript/chapter-08.md` | 51afcca43544175d | 5,546 |
| **Total** | | **58,008** |

Locations below are `file:line` in the manuscript files (line 1 is the chapter title). Canon evidence is cited only from what the prompt supplied: `UNIVERSE_BIBLE.md`, `STATE_LEDGER.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `PROLOGUE_PLAN.md` and `provenance/MOVEMENT-001-CONTINUITY.md`.

### Evidence baseline — canon changed on disk during this pass

The prompt was compiled at 08:26. Between 08:34 and 08:39, while this review was running, six planning and canon files in this worktree were modified by some other process: `IDEA.md`, `BOOK_MAP.md`, `SERIES_MAP.md`, `README.md`, `STATE_LEDGER.md` and `UNIVERSE_BIBLE.md`. This review did not write to them. They show as uncommitted changes against commit `1003491`. The nine manuscript files and the continuity checkpoint are unchanged.

Every canon citation in this report is to the evidence **as embedded in the prompt**, not to the newer text. I read the new diff for the bible, the book map and the state ledger but did not re-run the review against it. From that reading:

- Nothing in the new text reverses a finding in sections 4–7.
- The new material adds a combat-progression and earned-ash lock, a yield ladder (Handful, Flask, Barrel, Well) kept separate from grade (purity), and a filter-escalation note.
- It may create new items this pass did not assess. The manuscript says "Handful-grade" and "Barrel-grade" for spawn size (`chapter-05.md:83`, `prologue.md:841`, `:931`), and the new canon reserves "grade" for purity. Kellan ignoring clean ash on the floor (`chapter-05.md:279`) now touches a locked loop.

Treat those as prompts for a recheck against the updated canon, not as findings of this review.

---

## 1. Verdict in brief

The movement works. The Cellhouse failure (chapters 5–6) is an original, well-planted set piece whose consequences are still arriving two chapters later, and the adults around Kiva have reasons of their own. I would keep reading.

Three things stand between this draft and a clean one:

1. **The numbers do not survive a reader with a pencil.** A book whose ethic is "write down what the needle does" has a bout that ends at 2.5 points called as 3, a trial clock whose stated rate contradicts its spoken countdown, four wrong day references, and several other measurements that disagree with each other.
2. **Sentence rhythm is far from the owner's formula.** Mean sentence length is 8.3 words against a 14.6 target; 45% of sentences are five words or fewer against 27.7%; Flesch-Kincaid grade is 2.4 against 6.8. The short punch is the default register, not the exception.
3. **The cast shares one moral idiom, and three backstories arrive in one shape.** Six characters speak in "I'm not saying X, I'm saying Y" and "I want it said." Jessamy Hart's story is told three times, which drains the confession in chapter 8.

Three plan-adherence questions need the owner rather than the author. They are listed in section 7 and are not counted as repairs.

---

## 2. Unscored reader response

**Where interest caught**

- `prologue.md:107–177` (Teo's ledger). The narrow column he ruled himself, and the line "If I don't write the why, they'll make one up," is where the prologue stops being history and becomes a promise.
- `prologue.md:181–257` (The Tear). First physical danger. "The thing hit nothing" is the right size of sentence for the moment.
- `prologue.md:455–581` (The Weir). Tamar eating Gideon's bread, then the bowl. The best snapshot: a person, a joke, a small physical proof and an honest "Answer: unknown."
- `chapter-01.md:5–23`. A girl staring at a sticky needle because it is easier to look at than the board. Character before system.
- `chapter-02.md:41–109`. "It's in a hurry." The idea that a cell keeps the operator's mood is the freshest thing in the movement, and it is taught through a repair job.
- `chapter-04.md:177–215`. Kiva stops, watches the part that moves least, and sees that Kellan sequences. The fight turns on a perception, not a power.
- `chapter-05.md:317–451` and `chapter-06.md:3–123`. The tune that works, the joy, the fear, the cell that keeps all three doors, the rail, the shutter on Perrin's hands.
- `chapter-07.md:239–321`. Waking with her hand on the panel. The dream is a physical interruption with a bill attached.
- `chapter-08.md:153–211`. Three lines in three old books.

**Where it slipped**

- `prologue.md:585–947` (snapshots 7–9). By the seventh snapshot the pattern is known: a decent person, a hard choice, a ledger line ending in *Why*. Each is well made. Together they are predictable, and each one resets the pressure to zero. The protagonist's story does not begin until 28% of the supplied text has passed.
- `chapter-01.md:25–39`. The four axes arrive as a glossary straight after the needle.
- `chapter-03.md:147–225`. Three tutorials in a row (Ember, ward, stance), each with the same teach, fail, try-again shape.
- The cutaway backstories (`chapter-02.md:159–197`, `chapter-03.md:383–429`, `chapter-04.md:321–363`) are all summary narration ending on a quiet gesture. Kellan's is the strongest because it changes how the next scene reads.
- `chapter-08.md` has six endings (office, records room, embankment, Rhea, rosters, yard). Each earns its place, but the chapter exhales five times before the last one.
- Whenever a character explained their own honesty. See priority 3.

**Which person matters.** Kiva, and then Mara. Mara is the most alive adult on the page: "I'd like you to be a little uncomfortable" (`chapter-02.md:255`), "Now tell me what you can't do" (`chapter-04.md:403`), and her admission that her yes is partly self-interested (`chapter-08.md:231`). Perrin matters for warmth. Kellan is the most interesting, because his belief in measurement is given a real origin and then tested.

**What I expect next.** A first sanctioned meet with one declared door and Orla's name at risk. The Works review of Mara's license. Graywater's list on the twentieth, with Anwen on it or not. The clerk's copy of the 2446 entry. Rhea making contact. Whether the two fingers come all the way back.

**Would I continue?** Yes. As the adult reader, without reservation after chapter 5. As the thirteen-year-old, yes from chapter 1 onward, with a real risk of not reaching chapter 1.

---

## 3. Scored dimensions, two lenses

Anchors: 5 = understandable but inconsistent; 7 = engaging with located weaknesses; 9 = compelling with few substantial distractions.

### 3a. Fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Confidence |
|---|---|---|---|---|
| Opening pull | 6 | `prologue.md:3–103`; `chapter-01.md:5–23` | The kitchen going white is concrete and frightening. But this reader meets ten strangers across 13,000 words before Kiva appears. Chapter 1 on its own would be an 8. | Medium |
| Keep reading | 8 | `chapter-01.md:449`; `chapter-05.md:447`; `chapter-06.md:467` | Chapter ends are clean hooks: "No," then "I've stopped. It hasn't," then the woman at the glass. Local payoffs land inside each chapter. | High |
| Interest / freshness | 7 | `chapter-02.md:93–109`; `chapter-05.md:391` | A machine that keeps your mood is new. The placement-day and ranked-rival frame is familiar to this reader. | Medium |
| Clarity / flow | 8 | `chapter-04.md:53`; `chapter-05.md:63–101` | Rules and spaces are laid out before they are used. Short sentences make every beat easy to follow. | High |
| Character attachment | 8 | `chapter-04.md:403–409`; `chapter-07.md:193–205` | Kiva fails in public and owns it. Perrin is lovable and honest about envy. | High |
| Humor / warmth | 8 | `chapter-04.md:7–11`; `chapter-07.md:169`; `chapter-01.md:355` | "*What went wrong:* Perrin." The dumplings "for the hero. And also for Kiva." | High |
| Action / suspense | 8 | `chapter-04.md:81–279`; `chapter-06.md:43–123` | Both set pieces can be tracked move by move and both cost something. This reader will not check the arithmetic. | High |
| Progression payoff | 8 | `chapter-03.md:87–129` → `chapter-04.md:205–213` → `chapter-06.md:75` | Saying "one" is learned, used, lost under fear, then held under impact. Effort changes capability, and it shows. | High |
| Connection | 7 | `chapter-05.md:245`; `chapter-06.md:255–277`; `chapter-07.md:367–371` | Brannock's hurry, "give the ground its weight back" and the red-striped letter all return. A sharp reader will catch "three to a half." | Medium |
| Read-aloud quality | 8 | `chapter-05.md:207–451` | Attribution is never in doubt and the cadence is easy. Ledger abbreviations will trip a young reader aloud. | Medium |

### 3b. Adult genre reader

| Dimension | Score | Location | Reason | Confidence |
|---|---|---|---|---|
| Opening pull | 7 | `prologue.md:107–177` | Teo's column gives a reason to care about the motif before any system is explained. The eleven-snapshot structure asks for patience and repeats its closing gesture. | Medium |
| Keep reading | 8 | `chapter-05.md:317–451`; `chapter-07.md:325–449` | Pressure is real and consequences compound: the trial failure becomes a license review, which becomes the reason sponsorship is required. | High |
| Interest / freshness | 8 | `chapter-04.md:327–337`; `chapter-05.md:391`; `chapter-08.md:153–211` | Measurement as protection for people who are not in charge; a failure mode that turns the protagonist into bait; paper law. The frame is conventional but the mechanisms are not. | Medium |
| Clarity / flow | 6 | `chapter-04.md:119–279`; `chapter-05.md:249–335`; `chapter-04.md:39`; `chapter-06.md:151–163` | Meaning is clear on one pass. The numbers, days and geometry are not consistent on a second. See section 4. | High |
| Character attachment | 8 | `chapter-08.md:215–265`; `chapter-07.md:79–161` | Mara's compromised yes and Anwen's "the score first" are adult-grade honesty. Deduction for voice convergence. | Medium |
| Humor / warmth | 7 | `prologue.md:467–479`; `chapter-02.md:255`; `chapter-07.md:165–205` | Real and character-grounded, but Perrin carries almost all of it after the prologue. | Medium |
| Action / suspense | 8 | `chapter-04.md:177–279`; `chapter-06.md:149–209` | Adaptation on both sides in the ring; a contest of priorities in the Cellhouse. Deductions for the unsupported clock, the doubled chute release and a rail jump with clear stairs above it. | Medium |
| Progression payoff | 8 | `chapter-06.md:75–79`; `chapter-06.md:329–359` | Capability is priced. The risk is plan pacing, not craft: a working two-door hold arrives in Movement One. | Medium |
| Connection | 7 | `chapter-08.md:353`; `chapter-07.md:185`; `chapter-07.md:259` | Plants and payoffs are unusually tidy. State tracking across days and clock times is not. | High |
| Read-aloud quality | 6 | `chapter-07.md:209–237`; `chapter-04.md:227`; `chapter-07.md:139` | Nearly half of all sentences are five words or fewer. Narrated, that reads as constant emphasis. "Said" at 92 per 10,000 words is an audible drumbeat. "Step" means both a stride and a stone step in one sentence. "Three-thirty" can be a clock time or a run time. | Medium |

---

## 4. Canon, state, power, knowledge and reserved disclosures

### 4a. Contradictions with supplied evidence

| # | Location | Observed | Evidence | Confidence |
|---|---|---|---|---|
| A1 | `prologue.md:1109` | Stance stone "worn smooth in the middle by six hundred years of feet," in 2676. | `UNIVERSE_BIBLE.md` Timeline: Fall 2080; Kindling begins about 2090 onward; Meridian's first lanes 2150, "roughly 530 years of institutional growth" by 2680. A Kindling stone cannot be older than about 580 years, and a Meridian one not older than about 526. | High. Canon contradiction. |
| A2 | `chapter-02.md:51`; `chapter-08.md:157` | Paper cell books by law "for six hundred years"; "Six hundred years of it, nearly" for municipal meter transients. | Bible, *Energy revolution*: ash induction and licensed cells post-date Tamar Vey's 2182 question. The oldest register entry cited on the page is 2446. `chapter-02.md:205` ("Six hundred years ago … a medical station's yard") is consistent and can stand. | Medium. The Fall anniversary is being used as the age of institutions. |
| A3 | `chapter-03.md:149` | Orla is "Torch rank, which was as far as one door went." | Bible, *Power invariants*: the ladder runs to Glory with no single-door cap. `STATE_LEDGER.md`: school orders "whose masters pursue near-monastic devotion to one tradition." The manuscript's own `prologue.md:965–993`: the Even Hand train "in a single door for their whole lives," and Hesper Annick "reached Glory in 2431." | High as phrased. `chapter-08.md:285` ("as far as her door went") reads as Rhea's personal ceiling and survives. |
| A4 | `chapter-02.md:57` | Cell-book tunes dated "Fourth of this month … Eleventh … Eighteenth," read aloud on Classification Day. | Continuity checkpoint §1: Classification Day is Wed 3rd. `chapter-01.md:311–327` fixes it on the page: the trial is "on the twelfth," "nine days from now." Those entries are in the future. | High |
| A5 | `chapter-03.md:87` | "She thought about the draw bench yesterday," on Friday. | Checkpoint §1 and `chapter-02.md:201`: the bench was Wednesday; Thursday was the north round. | High |
| A6 | `chapter-04.md:39` | Anwen: "He said so on Monday." | Kellan said it on Classification Day, Wed 3rd (`chapter-01.md:125`). | High |
| A7 | `chapter-08.md:353` | Anwen on roster Monday: "I've got eight days to get higher" before the twentieth. | Checkpoint §1: rosters post Mon 15th. Five days remain. Eight was true on Friday the 12th. | High |
| A8 | `chapter-07.md:325`, `:347`; `chapter-08.md:161` | Core "reset itself at a quarter to three"; the report "will have gone at a quarter to three"; the register logs "Trip, two forty-four." | Checkpoint §1 puts the trip at 02:44. The scene between trip and reset (`chapter-07.md:259–321`) holds the quench, the whole dream told aloud and the window check. That is not one minute. | High |
| A9 | `chapter-07.md:185`, `:193` | Perrin's note: 400 kg "on hands, 9 sec, after winch loss." | The board (`chapter-06.md:373–375`) gives breaker 3:38, quench 3:44, casualty over the line 4:41. Between 3:38 and Perrin's release the page shows the quench, Kellan descending and killing the husk, Anwen freeing and hauling the dummy "a hand's length at a time," Kiva releasing her stance, and a finger-by-finger lowering (`chapter-06.md:213–289`). That is far longer than nine seconds. The checkpoint repeats "~9 s." | Medium-high |
| A10 | `chapter-07.md:259`, `:325` | "The Pryce laundry downstairs." | `chapter-01.md:421`: the shop is "between a laundry and a bakery." `chapter-02.md:123`: "Go next door and get Mrs. Pryce." `chapter-07.md:321`: "Our building, and the laundry, and the bakery." The checkpoint says "ground floor" and so disagrees with three manuscript lines. | High that the page is inconsistent. Which is canon is the owner's call. |

### 4b. Internal inconsistencies (no external evidence needed)

| # | Location | Observed | Confidence |
|---|---|---|---|
| B1 | `chapter-04.md:53`, `:119`, `:161`, `:279`, `:377` | "Three points won." Renn scores a half, one, then one: 2.5. The referee calls "Renn wins, three to a half," and Kiva logs "Lost 3 to ½." The checkpoint repeats 3–½. | High |
| B2 | `chapter-05.md:249–335` against `chapter-06.md:175` | Kiva measures "a tenth every ten seconds," with red at 8.5. From 6.3 that is 220 seconds. She calls "about two minutes," then "Ninety seconds" at 6.7, "Sixty seconds" at 6.9, and the narration gives "forty seconds" at 7.2. Those countdowns need a tenth every three to five seconds. The readings shown between them advance evenly. Acceleration is asserted ("Faster as it went") but never shown. Kellan then stakes his decision on her being "right every time, to the tenth." | High that it does not close. See the note below. |
| B3 | `chapter-05.md:73` against `chapter-06.md:51`, `:113` | Mezzanine "about twice a man's height," then "two and a half meters" twice. A twelve-step stair supports 2.5 m. | High |
| B4 | `prologue.md:297` against `prologue.md:361` | In 2152, "Two years ago a scavenger crew had come back … from the dead power station at Corbel Reach." In 2170, "For eighty years nobody had gone closer than the far bank." | High |
| B5 | `chapter-05.md:441` against `chapter-06.md:27` | The chute clangs and "more husks come out" at needle 8.1–8.2. Chapter 6 opens at 8.2 and the chute clangs again with three husks. Releases are "on a timer." Either one release is narrated twice or a wave is never accounted for. | Medium |
| B6 | `chapter-06.md:151`, `:163` | The stair runs up the south wall to a mezzanine at the east end (`chapter-05.md:73`). Kellan faces down it toward the husk, so the south wall is on his left. The text has "Brick wall on his right. A steel rail on his left," and the mezzanine "above him and to his left." It reads mirrored until he turns at `:195`. | Medium |
| B7 | `chapter-06.md:195–203` | Kellan backs up two steps with the husk below him, then jumps from the rail to catch the platform edge. The seven steps above him are clear. The jump is vivid but unmotivated. One clause would fix it, such as the husk at his heels or the top of the stair fouled with ash. | Medium |
| B8 | `chapter-08.md:303` | Rhea runs the plate "from three thirty-nine" to watch the disk swing out "as the husk hit the girl." The board has Kiva over the rail at 3:31 and the breaker at 3:38, and the husk is already on her when the breaker goes (`chapter-06.md:83–111`). The hit is nearer 3:34. The checkpoint's "~3:39" carries the same error. | Medium |
| B9 | `chapter-01.md:319–321` against `chapter-03.md:399` and `chapter-08.md:137–145` | Orla: "I don't have sponsoring standing." Her cutaway: standing was "restored for eleven" years. Ysra: sponsorship takes "one form and a hearing." In chapter 8 Ysra stamps the form with no hearing. | Medium |
| B10 | `chapter-01.md:271` | "Your draw is down, from two-nine." It went from 2.9 to 3.1. Lower is better, so "down" says the opposite of what Ysra means. | High |
| B11 | `prologue.md:1047`, `:1113` against `chapter-08.md:179` | The courier comes at seven and they hurry for the tram. Kiva goes eleventh of thirty-one. Mara later reads the frame clock at "a quarter to three." Nothing says the ceremony began after noon. | Low-medium |
| B12 | `chapter-06.md:385`; `chapter-07.md:21`; `chapter-08.md:89` | "Three thousand people" behind glass along one wall of a hall forty paces long. | Low-medium |
| B13 | `prologue.md:427` | "You come out at forty-five again." The ledger line just above has her out at 41. | Medium |
| B14 | `chapter-05.md:199` | Perrin "swallowed his like medicine." Everywhere else a dram is settled through the palm, including the same paragraph. No supplied evidence covers ingestion. | Apparent inconsistency only |
| B15 | `chapter-07.md:245`, `:267` | Mara pulls the quench "the way she had done ten thousand times." `chapter-02.md:73–75` makes the quench a last resort. "Ten thousand times" also appears eleven sentences earlier. | Medium |
| B16 | `chapter-04.md:19` | Orla speaks and "Kiva put down her toast." Nothing places Orla at the Rowan breakfast table. | Medium |
| B17 | `chapter-08.md:161` | "I filed it. Ours. Last night. It's in today's book." Mara filed that morning (`chapter-07.md:415`). Heard aloud, "Last night" attaches to "filed." | Medium |

**Note on B2.** This is the most consequential item. On the manuscript's own stated rate, an untuned cell would have tripped at about 4:08. That is after the four-minute extraction standard and about two minutes after Perrin asks for "thirty more." Read with a pencil, Kiva did not need to break her declared role at all. The story needs the opposite to be true.

### 4c. Knowledge boundaries

- **Slip.** `chapter-07.md:371`: Kiva says "This came in the winter" as a statement. Only Mara's cutaway (`chapter-02.md:167`) and the reader know that. The quoted letter carries no date beyond "2677." Medium confidence. One date on the letter fixes it.
- **Slip.** `chapter-06.md:171`: Kellan thinks "She had said it would call them. In the corridor." The line he then quotes says only that "the cell will take the fight." Nobody predicted the calling. Ysra later says no one in the Compact had seen it (`chapter-08.md:85`). Medium-high confidence.
- **Held.** Kiva does not learn the name Unroofed Sky, does not see the Annick notebook, and tells Ysra only that the dream came (`chapter-08.md:23`). Orla has the catalog card but no proof, matching `STATE_LEDGER.md` *Knowledge boundaries*. Rhea recognizes the disk only after she has judged the performance (`chapter-08.md:297–335`), matching `BOOK_MAP.md` §4, Movement One exit state.
- **At the edge.** `chapter-08.md:207`: "She did not know who had been dreaming in 2446." See owner decision D2.

### 4d. Power limits and physical state

- **Held.** The disk is cold throughout and never teaches. The dream supplies no tactic and costs a nosebleed, a quenched cell and a license filing. Ward does not move radiation (`prologue.md:431`). No Glory figure is on stage. Husks go to worked power, which matches the bible's "rift attraction" failure mode. Kiva's three bounds of Stride (`chapter-06.md:47–55`) match "three steps, maybe four" (`chapter-04.md:143`). Dark Edge strikes dispersing a small husk match the shovel in `prologue.md:219`.
- **Physical state tracks.** Left knee (Wed, again Fri), left forearm scrape, heat-lines extended to mid upper arm, the sling, two fingers, Perrin's hands and Kellan's knee and forearm bruise are all carried correctly through chapter 8.
- **Plan-adherence risk, not a canon error.** See owner decision D1 on the two-door hold.

### 4e. Reserved disclosures

- **Held.** The cause and authorship of the Fall are voiced as belief only (`prologue.md:35–69`). The Mars-disk story is rumor from a man who also denies the moon landing (`prologue.md:253`). The filter appears as post-Homura hearsay (`prologue.md:321`). The crooked post's reason stays lost. No snapshot ends on a thesis line. The prologue ends on the post, as `PROLOGUE_PLAN.md` §6 requires.
- **Flagged by the author and confirmed here.** Snapshot 4 is dated 2152, just outside the plan's range of about 2135–2150.
- **Prologue scale** (`PROLOGUE_PLAN.md` §2: "usually 900–1,600 words each," 11,000–17,000 in total). Measured: 1,044; 967; 1,255; 950; 1,594; 1,777; 1,334; 1,552; 1,435; 1,234; 2,869. The total of 16,011 is inside the range. Snapshots 6 and 11 are over the per-scene guide. This is plan adherence only.
- **Question for the owner.** `prologue.md:291` lists ledger initials "T.V. J. D.W. K." and `:311` "S.V." Snapshot 6 then introduces Tamar Vey, written "T. Vey" in Gideon's book (`prologue.md:577`). A reader can take the 2152 "T.V." to be Tamar, who would have been about twenty. The supplied evidence does not let me check the trilogy's initials, so this is a possible collision, not a verified one.
- **Adult-reader plausibility, low priority.** `prologue.md:7–25` puts the white light, the spreading colors and a short conversation before the lights fail. The fast pulse from a high-altitude burst arrives with the flash. The plan's own table has the two together.

---

## 5. Numerical formula alignment

Targets come from the formula embedded in the prompt (O'Connor 1.3.0, sections 2–6 and 8). Every observed value below comes from one stdlib script, reproduced in full in the appendix. These numbers are kept separate from the reader scores above.

### 5a. Sentence rhythm

Tokenizer: rule-based. A sentence ends at `.`, `!` or `?` (plus closing quotes) followed by whitespace and a capital, digit or opening quote. A paragraph end always ends a sentence. A line of dialogue and its lowercase tag count as one sentence. Listed abbreviations and single initials do not split.

| Metric | Target | All 9 files | Chapters 1–8 | Per-file range |
|---|---|---|---|---|
| Sentences | — | 6,986 | 5,167 | — |
| Mean length | 14.6 words | **8.30** | 8.13 | 7.29 (ch 7) to 9.34 (ch 4) |
| Median length | 11 | **6** | 6 | 5 to 7 |
| Population stdev | about 26 | 6.94 | 6.98 | 6.40 to 7.79 |
| Share of five words or fewer | 27.7% | **45.1%** | 47.5% | 38.5% (prologue) to 53.6% (ch 7) |
| Share of forty words or more | 3.3% | **0.30%** | 0.35% | 0.00% (ch 5) to 0.62% (ch 1) |

Length distribution, all files: 0–4 words 34.4%; 5–9 words 37.2%; 10–14 words 13.4%; 15–19 words 6.6%; 20–24 words 4.2%; 25–29 words 2.4%; 30 or more 1.8%. Twenty-one sentences in 58,008 words reach forty words. The longest is 52.

Cross-checks from the same script:

- A naive tokenizer that splits after every terminal mark gives mean 8.22 and 46.1% short. The result does not depend on the tokenizer.
- With all quoted speech removed, narration alone gives mean 9.06, median 7 and 41.9% short. Dialogue is not the cause.

**Reading.** This is material drift, and it runs the opposite way from the failure the formula warns about. The formula fears uniform mid-length prose with no short spikes. This draft is uniformly short with almost no long sentences to spike against.

**Conflict to report, not paper over.** The source formula was measured on ASR transcripts. A standard deviation of about 26 on a mean of 14.6 implies some very long machine-segmented "sentences," and I do not think a typographic tokenizer can reach it. I treat the stdev target as not comparable. The mean, median and both share targets are comparable, and all four are far off.

### 5b. Paragraphs and section breaks

These are typographic counts. The formula's targets are ASR pause proxies, so the comparison is directional only.

| Metric | Target (ASR proxy) | Observed |
|---|---|---|
| Paragraph median | 18 words | 15 |
| Paragraph mean | 26.8 words | 25.7 |
| Paragraphs | — | 2,258; 45.4% are twelve words or fewer; 38 reach 100 words; 1 reaches 150 |
| Words between section breaks | about 950 | 667 (87 sections) |
| Section breaks per 10,000 words | about 8.7 | 15.0; per chapter 13.3 to 18.3 |

Paragraph texture is on target. There are no dense expository blocks. Sections break about 1.7 times as often as the target, most in chapters 4–6 (17.2 to 18.3 per 10,000). That suits the action, and I do not recommend changing it.

### 5c. Readability

Syllable estimator: heuristic vowel-group count with silent-e, `-ed` and `-es` adjustments. Proper names and system terms are not special-cased.

| Metric | Target | All 9 files | Chapters 1–8 | Per-file range |
|---|---|---|---|---|
| Flesch Reading Ease | 72.3 | **92.4** | 92.7 | 88.7 to 96.5 |
| Flesch-Kincaid grade | 6.8 | **2.4** | 2.4 | 1.8 (ch 6) to 3.0 (ch 2) |

Observed inputs: 8.30 words per sentence and 1.254 syllables per word.

A derived point worth the owner's attention: the formula's three readability targets together imply about 1.41 syllables per word (14.6 words per sentence, ease 72.3, grade 6.8). This draft runs at 1.25. At the target sentence length and the present vocabulary, the grade would be about 4.9. So sentence length closes roughly half the gap, and the rest is word choice. The draft's plain vocabulary is a real strength for the thirteen-year-old lens. That is a tradeoff to decide, not a defect to fix on reflex.

### 5d. Progression vocabulary

Project lexicon, defined before counting and listed in the appendix: rank names and axes (case-sensitive), door compounds, techniques, and classification and placement terms. It borrows nothing from the source novel. Density depends on the lexicon, so the comparison with the source's 58 per 10,000 is directional.

| Scope | Hits per 10,000 (full lexicon) | Excluding door compounds |
|---|---|---|
| All 9 files | 115.3 | 84.0 |
| Chapters 1–8 | 142.2 | 103.6 |
| Prologue | 45.0 | — |
| By chapter, 1 to 8 | 255, 42, 203, 201, 141, 102, 42, 123 | — |

The formula's whole-book figure is about 58, with the opening third near 83 (58 × 3 × 900/1,885). Movement One sits above that even on the narrow count. That is consistent with "teach aggressively in the first third." The two quiet chapters, 2 and 7, are the home and consequence chapters, which is the right place for the system to recede.

**The front-loading ratio is UNMEASURED.** The supplied text is about 18–21% of a planned 270,000–315,000 words, so the first third is not complete and thirds cannot be compared. This is provisional cumulative coverage only.

### 5e. Development moments

**Regex proxy** (formula §5 method: a reflection marker within 120 characters of a name):

| Scope | Lead (Kiva, Rowan) | Supporting |
|---|---|---|
| Chapters 1–8 | 30 hits, 7.1 per 10,000 (target 4.5) | Mara 4.0; Orla 3.6; Ysra 1.2; Anwen, Perrin, Kellan and Rhea 0.5 each (target 0.1–0.7 each) |
| By chapter, lead | 5, 6, 5, 3, 4, 3, 2, 2 | — |

The proxy is noisy here. Kiva's sections mostly say "she," which undercounts her. Mara and Orla are named near other people's realizations, which overcounts them. Do not read 7.1 as an overshoot.

**Manually identified lead beats** (actual choices or realizations), 23 across chapters 1–8, about 5.5 per 10,000 words:

| Chapter | Beats |
|---|---|
| 1 | Decides to stop waiting for a board to name her (`:407`) |
| 2 | Hears the hurry in the tune and is surprised by her own voice (`:93`) |
| 3 | Notices the bottom line lights first (`:87–89`); links her own rush to Brannock's (`:247`); "The gap was not the enemy" (`:279`); leaves *Why* blank (`:349`) |
| 4 | Makes herself stop and watch (`:177`); "He was fast because he never did" (`:199`); finds what the bar is for (`:215`); refuses stance and uses the riser (`:261`); states her limits to Mara (`:403–409`) |
| 5 | Declares no doors near the cell (`:183–189`); changes role aloud (`:343`); understands she made the cell a lamp (`:391`, `:447`) |
| 6 | Goes over the rail (`:43–45`); shuts the hand door under impact (`:75`); writes "Should have said it" (`:437`) |
| 7 | Admits there was time (`:67`); tells Mara the whole dream (`:293`); writes "Why: Don't know" (`:449`) |
| 8 | "I don't know how to keep them out when I'm frightened" (`:49`); accepts the lowest place (`:145`); "Again" (`:437`) |

Distribution is even. Nothing is saved for the end.

**Supporting cast, manual.** Seven named people get one or two independent beats each:

- Mara signs (`chapter-04.md:413`) and apologizes (`chapter-07.md:401`).
- Orla completes the form (`chapter-08.md:135`).
- Anwen says "the score first" (`chapter-07.md:103`) and "I want it anyway" (`:159`).
- Perrin is grateful and jealous at once (`chapter-07.md:193–197`).
- Kellan learns from someone the board cannot read (`chapter-04.md:359`) and takes the quench (`chapter-06.md:193`).
- Ysra gets a book she can rule on (`chapter-08.md:93`).
- Rhea writes "Responder" (`chapter-08.md:297`).

No single deuteragonist absorbs the secondary budget. This matches the intended shape.

### 5f. POV word share

Viewpoint segments were identified by reading every section, not by name frequency. The map is in the script and guarded by assertions on each cutaway's first words.

| Viewpoint | Words | Share of chapters 1–8 | Share of all 9 files |
|---|---|---|---|
| Kiva | 36,627 | **87.2%** | 63.1% |
| Kellan (two cutaways: ch 4, ch 6) | 1,728 | 4.1% | 3.0% |
| Rhea (ch 8) | 1,174 | 2.8% | 2.0% |
| Anwen (ch 7) | 999 | 2.4% | 1.7% |
| Orla (ch 3) | 872 | 2.1% | 1.5% |
| Mara (ch 2) | 597 | 1.4% | 1.0% |
| Prologue | 16,011 (snapshot 11, Kiva at thirteen, is 2,869 of these) | — | 27.6% |

Within the eight chapters the target is met almost exactly: 87.2% lead against 87%, and 12.8% secondary across five people against 13% across four or five. Kellan is slightly above the 2.5–3.7% band and Mara is below it. Every cutaway is a brief scene, and none is a chapter.

Counting the prologue, the lead holds 68.1% of the supplied text.

**Conflict for the owner.** This is a projection, not a measurement. If later chapters hold 87.2% and the book lands at 270,000–315,000 words, the prologue's 13,142 non-lead words put the whole-book lead share at about 83–84%. To reach 87% at book level with the prologue counted, chapter cutaways would have to average about 8.6%. The plan should say whether the prologue is inside or outside the POV denominator.

### 5g. Secondary signals

Section 8 of the formula is use-to-taste. These are reported and not treated as quotas. Lexicons are in the appendix. A suffix count is not proof that a word is an adverb.

| Signal | Source figure | All 9 files | Chapters 1–8 | Note |
|---|---|---|---|---|
| `-ly` suffix words per 10,000 | about 161 | 39.0 | 42.9 | Far lower. Top: slowly 35, exactly 19, quietly 13. Optional register signal. |
| Reporting verbs per 10,000 | about 41 | 115.2 | 117.4 | "said" alone is 92.4. 22.8% of all words sit inside quotation marks. |
| Combat terms per 10,000 | about 22 | 40.5 | 51.0 | Lexicon includes "bar" (8.8) and "blade" (8.3), Kiva's and Kellan's Edge shapes. |
| "that" per 10,000 | 92.1, tighten below | 82.9 | — | Below the source. Good. |
| "just", "felt", "almost", "seemed" | 5–25 band each | 10.0, 13.8, 2.4, 0.5 | — | Two in band, two below. |
| "for a moment" per 10,000 | 2–4 background | 4.0 | 4.8 | At the top of background. |

Repetition above background (all files, count and rate per 10,000):

| Phrase | Count | Per 10,000 |
|---|---|---|
| "did not" | 248 | 42.8 |
| "looked at" | 130 | 22.4 |
| "she did not" (3-gram) | 90 | 15.5 |
| "the way" | 89 | 15.3 |
| "very" | 80 | 13.8 |
| Narration fragments opening "Not …" (eight words or fewer) | 78 | 13.4 |
| "like a" | 55 | 9.5 |
| "at once" | 52 | 9.0 |
| "it was not" | 34 | 5.9 |
| "for a long time / moment / while" | 21 | 3.6 |

The uncontracted "did not" is clearly a chosen narrative voice, and I would keep it. The two audible tics are different:

- **The negation-then-correction pair.** "It was not X. It was Y." and "Not X. Y." Examples: `prologue.md:9`, `chapter-01.md:183`, `chapter-04.md:179`, `chapter-08.md:287`.
- **"looked at … for a long moment" as the default pause.**

---

## 6. Repair brief — three priorities

The author keeps every scene. Nothing below shortens the Terrace Ring bout or the Cellhouse run.

### Priority 1 — Make every number, day and measurement on the page true

**Location.** Line-level, across all nine files. The full list is in sections 4a, 4b and 4c. The ones that matter most:

- `chapter-04.md:279` and `:377`: the bout score.
- `chapter-05.md:249–335` with `chapter-06.md:175`: the trial clock.
- `chapter-07.md:185` and `:193`: Perrin's nine seconds.
- `chapter-02.md:57`, `chapter-03.md:87`, `chapter-04.md:39`, `chapter-08.md:353`: day and date references.
- `chapter-07.md:325` and `:347`: core trip against reset.
- `chapter-05.md:73`: mezzanine height.
- `prologue.md:1109`: the six-hundred-year stone.
- `prologue.md:297` against `:361`: Corbel Reach.
- `chapter-03.md:149`: the one-door Torch cap.
- `chapter-01.md:271`: draw "down."
- `chapter-07.md:259` and `:325`: the laundry.
- `chapter-06.md:171` and `chapter-07.md:371`: the two knowledge slips.
- `chapter-05.md:441` against `chapter-06.md:27`: the doubled chute release.
- `chapter-06.md:151–163`: stair handedness.

**Observed issue.** The measurements contradict each other or the checkpoint calendar. The central one is the trial clock. On the stated rate, Kiva's intervention was not needed.

**Effect on the reader.** This book tells the reader, through Mara, Kellan and Ysra, that written numbers are what protect people. A thirteen-year-old who adds a half, one and one will get 2.5. An adult who does Kiva's sum will find the urgency was not there. Each miss spends trust the climax depends on, because Kellan acts only since "her measurements had been right all run."

**Proposed scope.** About 25 to 30 single-sentence edits. No scene is restructured.

- For the bout, either add one more exchange or have the referee call the true score. The author chooses. Do not trim the fight.
- For the clock, keep the board timestamps (3:31, 3:38, 3:44, 4:41). Then make the stated rate, the readings on the page and the spoken countdowns agree with them. Show the acceleration in the readings if it is real.
- Afterward, reconcile `provenance/MOVEMENT-001-CONTINUITY.md` to the corrected page. Four of its entries currently carry the same errors: 3–½, about 9 s, about 3:39 and the ground-floor laundry.

**Strength to preserve.** The role-change calls, the board as a scored artifact, the riser half-point, and every beat of adaptation in both set pieces. Punctuation and numbers only.

### Priority 2 — Restore the long sentence so the short one can land

**Location.** Movement-wide. Start where the prose is connective, not at impact points:

- `chapter-01.md:25–39` (the four axes)
- `chapter-02.md:159–197` (Mara's evening)
- `chapter-03.md:383–429` (Orla's cutaway)
- `chapter-04.md:321–363` (Kellan's cutaway)
- `chapter-05.md:63–101` (the Cellhouse layout)
- `chapter-07.md:325–449` (the license conversation)
- `chapter-08.md:269–335` (Rhea)
- Prologue snapshots 4, 7 and 10

**Observed issue.** Mean 8.3 words against 14.6. Median 6 against 11. Five words or fewer, 45.1% against 27.7%. Forty words or more, 0.30% against 3.3%. Grade 2.4 against 6.8. Fragments carry exposition, transition and backstory as well as impact. Two tics ride on the same habit: the negation-correction pair (78 "Not …" fragments, 34 "it was not") and "looked at" (130).

**Effect on the reader.** For the thirteen-year-old, little harm: it is easy and fast. For the adult, and for anyone hearing it narrated, every beat is stressed, so none is. The deliberate punches ("She went." "The thing hit nothing." "Holding. Holding.") lose their contrast.

**Proposed scope.** One bounded same-author rhythm pass.

- Join runs of fragments into compound and complex sentences in the connective passages listed above.
- Leave fragments at fight beats, chapter ends and ledger lines.
- Thin the two tics by about half. Leave "did not" alone.
- Re-run the appendix script afterward and report target against observed honestly.
- Do not chase the stdev target. Do not iterate to decimals.
- The remaining grade gap is vocabulary (section 5c). Bring that tradeoff to the owner. Do not solve it by inflating diction.

**Strength to preserve.** Short paragraphs (already on target), clean attribution, plain concrete nouns, and the true impact fragments. The section-break rate needs no change.

### Priority 3 — Give each voice its own way of being honest, and tell each secret once

**Location.**

- "I'm not saying X. I'm saying Y": Ysra `chapter-01.md:305`; Mara `chapter-02.md:149` and `chapter-08.md:265`; Kellan `chapter-04.md:309`; Anwen `chapter-08.md:357`.
- "I want it said" and "It's said": Anwen `chapter-01.md:381` and `chapter-06.md:451`; Perrin `chapter-03.md:325` and `chapter-07.md:197`; Mara `chapter-08.md:231`.
- "Not a good reason. The true one": Orla `chapter-02.md:307` and `chapter-08.md:119`.
- Jessamy Hart: hinted at `chapter-02.md:307`, told in full at `chapter-03.md:391–405`, retold aloud at `chapter-08.md:119`.
- Prologue closings on an italic *Why* line: `prologue.md:441`, `:821`, `:935`. The same gesture closes snapshots 2, 4, 6 and 7.

**Observed issue.** Candor is the book's value, but six people express it in one syntax, and the text names the borrowing ("Like Anwen does," "That's what Anwen would do"). The reader also learns Orla's worst secret in full, in summary, five chapters before she says it to Kiva. The spoken confession in chapter 8 therefore carries no new information. In the prologue, seven of ten historical snapshots resolve on the same record-keeping beat.

**Effect on the reader.** Characters who should be recognizably different start to sound like one author. The chapter 8 sponsorship scene is the movement's emotional resolution, and it plays as confirmation instead of revelation. Prologue snapshots 7 to 9 are where attention slipped for both lenses.

**Proposed scope.** Small and surgical.

- Let Anwen own "I want it said" and Mara own "say it out loud." Reword the other instances in each speaker's own manner: Kellan through numbers, Perrin through jokes that fail to hide it, Ysra through procedure.
- In `chapter-03.md:383–429`, keep Orla's fear and the unsigned second page. Withhold the particulars (the hand, the two burned students, four thousand people) so chapter 8 delivers them first.
- In the prologue, vary how two or three of snapshots 5, 8 and 9 end, so the record is present without always being the last line. Do not cut or merge snapshots. The plan locks eleven.

**Strength to preserve.** Anwen's "the score first." Perrin's envy said to Kiva's face. Mara's compromised yes on the embankment. Orla's "That's why it counts." The seven-column book as the object that finally lets Ysra rule.

---

## 7. Owner decisions (plan adherence, not repairs)

These are not errors. Each spends, or comes close to spending, something the plan reserves for later.

**D1 — A working two-door hold in Movement One.**
`chapter-06.md:57–79`. Kiva holds still door and Ember under impact with the hand door deliberately shut, and it works. `chapter-04.md:127` says she had "never in four years been able to hold two without the third." `BOOK_MAP.md` §4 places "First deliberate two-door sequence works briefly" at the end of Movement 3, and §5 says two-door use "appears only after single-door discipline is visible." The text frames the hold as wrong and costly, and Orla says so. That framing protects the plan. But Rhea's card records it as an achievement (`chapter-08.md:331`).
*Decide:* is this an accident Kiva cannot repeat, or has Movement 3's milestone moved?

**D2 — The register entries bring Kiva within one inference of the Movement 4 reveal.**
`chapter-08.md:153–211`. Kiva now holds dated evidence of "every lamp at once" in 2446 and 2604, and she frames the dream hypothesis herself at `:207`. `BOOK_MAP.md` reserves the pre-Kiva dream fragment for Movement 4 and a confirming second account for the ending. The checkpoint (§4) already flags the deliberate 2446 placement. It is the movement's best mystery hook.
*Decide:* keep it as is, or cut the single line at `:207` so the connection stays the reader's and not Kiva's.

**D3 — The two fingers.**
`chapter-06.md:359`; `chapter-08.md:391`, `:435`. `STATE_LEDGER.md` reserves permanent loss for the regional sequence and wants it "planted before it occurs." The plant is here. But the movement closes on "her two dull fingers," which can read as the cost already paid.
*Decide:* how much recovery Movement 2 should show, so that Movement 5 still takes something.

**D4 — Is the prologue inside the POV denominator?** See section 5f.

**D5 — Snapshot 4's date (2152) and the "T.V." / "T. Vey" initials.** See section 4e.

**D6 — Reading level.** The formula's readability targets imply a more polysyllabic vocabulary than this draft uses (section 5c). The plain diction serves the younger lens.
*Decide:* which to favor.

---

## 8. Tradeoffs and uncertainty

- One movement does not establish how this seat performs across a series. No other run was supplied, so no comparison is made.
- This is a same-model read. Its blind spots overlap the author's. The arithmetic and calendar findings are the most reliable, because each can be checked against the page. The scores are the least reliable.
- Geometry findings (B6, B7) rest on the stair rising eastward along the south wall. The text strongly implies that but does not state it.
- Metric comparisons with the formula are imperfect by construction: the source was measured on ASR transcripts and this draft on typography. The gaps in sentence mean, median, short-sentence share and long-sentence share are large enough to survive that caveat. The stdev, paragraph and section comparisons are not.
- UNMEASURED: front-loading by book thirds (the book is incomplete), and protagonist development distribution by book thirds.

---

## Appendix — reproducible metrics method

**Environment.** Python 3.14.6, standard library only. Read-only against the manuscript. No network access.

**Command** (the argument is the book root, so the script works wherever it is saved):

```
python3 metrics.py /Users/drive/kindling-repo-stage/.claude/worktrees/kindling-2680-prologue-m001-opus55/books/book-2680-opening
```

**Script SHA-256 as run:** `462e9ac63f3d831ce8465b78598e32ed0a95b25b25adef9373d1495dc402a308`

**Input hashes:** see the coverage table in section 0. The script prints them first, so a later run can confirm it is measuring the same text.

**Definitions.**

- *Words:* regex `[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*`, after removing heading lines, horizontal rules and emphasis markers. Italic ledger lines and dated captions are counted as prose.
- *Sections:* blocks between `---` rules.
- *Paragraphs:* blocks separated by blank lines.
- *Sentences:* the `sentences()` function below. The naive and narration-only tokenizers in block 8 are cross-checks.
- *Syllables:* the `syllables()` heuristic below.
- *Flesch Reading Ease:* 206.835 − 1.015 × (words per sentence) − 84.6 × (syllables per word).
- *Flesch-Kincaid grade:* 0.39 × (words per sentence) + 11.8 × (syllables per word) − 15.59.
- *Progression lexicon:* `PROG_CI` (case-insensitive) and `PROG_CS` (case-sensitive) below. "Ward" is counted once, through the case-insensitive entry.
- *POV map:* `POV` below, identified by reading. Assertions fail loudly if a section boundary moves.

**Known false positives.**

- "ward" also matches city "wards."
- "Hold", "Draw" and "Call" match when sentence-initial.
- "bar" and "cut" match non-combat uses.
- The `-ly` count is a suffix count with a stoplist, not a part-of-speech tag.

**Not captured by the script.** The manual development-beat list in section 5e and all reader scores are judgments. They are labeled as such where they appear.

### `metrics.py`

```python
#!/usr/bin/env python3
"""Movement 001 numerical alignment — Kindling 2680 Book One.

Stdlib only. Read-only against the manuscript.
Usage: python3 metrics.py /path/to/books/book-2680-opening
"""
import re, sys, statistics, hashlib, collections

ROOT = sys.argv[1].rstrip('/')
FILES = ['prologue'] + ['chapter-%02d' % i for i in range(1, 9)]

# ---- viewpoint map: manually identified by reading every section. ----------
# Sections are the blocks between `---` rules (and, in the prologue, the dated
# `## N.` snapshots). Index is 0-based within each file after splitting on
# rules. Anything not listed is the lead (Kiva).
POV = {
    'chapter-02': {3: 'Mara'},     # "The shop closed at seven. Mara did not go up..."
    'chapter-03': {7: 'Orla'},     # "When they had gone, Orla Dane sat on the crate..."
    'chapter-04': {8: 'Kellan'},   # "Kellan Renn walked out of Stonehand Hall..."
    'chapter-06': {4: 'Kellan'},   # "Kellan Renn heard her the first time."
    'chapter-07': {2: 'Anwen'},    # "Anwen Pryce did not go home after the Cellhouse."
    'chapter-08': {5: 'Rhea'},     # "Rhea Sorn watched the run four times..."
}
POV_CHECK = {  # first words each mapped section must start with (guards drift)
    ('chapter-02', 3): 'The shop closed at seven',
    ('chapter-03', 7): 'When they had gone, Orla Dane',
    ('chapter-04', 8): 'Kellan Renn walked out',
    ('chapter-06', 4): 'Kellan Renn heard her',
    ('chapter-07', 2): 'Anwen Pryce did not go home',
    ('chapter-08', 5): 'Rhea Sorn watched the run',
}

WORD = re.compile(r"[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*")
ABBR = {'mr', 'mrs', 'ms', 'dr', 'st', 'c', 'approx', 'est', 'hr', 'min', 'sec',
        'bldg', 'cart', 'no', 'vs', 'ed', 'recal', 'sub'}


def load(name):
    raw = open('%s/manuscript/%s.md' % (ROOT, name), encoding='utf-8').read()
    return raw


def sections(raw):
    """Split on horizontal rules; drop markdown headings; keep prose blocks."""
    out = []
    for block in re.split(r'(?m)^---\s*$', raw):
        lines = [l for l in block.split('\n') if not l.startswith('#')]
        text = '\n'.join(lines).strip()
        if text:
            out.append(text)
    return out


def clean(text):
    return text.replace('*', '').replace('_', '')


def paragraphs(text):
    return [p.strip() for p in re.split(r'\n\s*\n', clean(text)) if p.strip()]


def words(text):
    return WORD.findall(text)


def sentences(text):
    """Rule-based tokenizer. A sentence ends at . ! ? (plus closing quotes)
    followed by whitespace and an uppercase letter, digit or opening quote.
    Paragraph ends always end a sentence. A lowercase continuation after a
    closing quote ('"What?" said Kellan') does NOT split, so a line of
    dialogue plus its tag is one sentence. Listed abbreviations and single
    capital initials do not split."""
    sents = []
    for para in paragraphs(text):
        para = re.sub(r'\s+', ' ', para)
        start = 0
        for m in re.finditer(r'[.!?]+["”’\')\]]*\s+(?=["“‘(\[]?[A-Z0-9])', para):
            chunk = para[start:m.end()]
            tail = re.findall(r"([A-Za-z]+)[.!?]+[\"”’')\]]*\s+$", chunk)
            if tail and chunk.rstrip().rstrip('"”’\')]').endswith('.'):
                t = tail[0]
                if t.lower() in ABBR or (len(t) == 1 and t.isupper()):
                    continue
            sents.append(chunk.strip())
            start = m.end()
        rest = para[start:].strip()
        if rest:
            sents.append(rest)
    return [s for s in sents if words(s)]


def syllables(w):
    """Heuristic estimator: vowel-group count, minus silent final e, plus
    consonant+le, floor of one. Hyphen/apostrophe parts are summed."""
    total = 0
    for part in re.split(r"[’'\-]", w.lower()):
        part = re.sub(r'[^a-z]', '', part)
        if not part:
            continue
        n = len(re.findall(r'[aeiouy]+', part))
        if part.endswith('e') and not part.endswith(('le', 'ee', 'ye')) and n > 1:
            n -= 1
        if part.endswith('ed') and n > 1 and not part.endswith(('ted', 'ded')):
            n -= 1
        if part.endswith('es') and n > 1 and not part.endswith(
                ('ses', 'zes', 'ces', 'ges', 'xes', 'shes', 'ches')):
            n -= 1
        total += max(n, 1)
    return max(total, 1) if w and not w.isdigit() else max(len(w), 1)


def sent_stats(sl):
    lens = [len(words(s)) for s in sl]
    n = len(lens)
    return dict(n=n, mean=statistics.mean(lens), median=statistics.median(lens),
                pstdev=statistics.pstdev(lens),
                le5=100 * sum(1 for x in lens if x <= 5) / n,
                ge40=100 * sum(1 for x in lens if x >= 40) / n,
                mx=max(lens))


def flesch(text):
    sl = sentences(text)
    wl = words(clean(text))
    syl = sum(syllables(w) for w in wl)
    wps = len(wl) / len(sl)
    spw = syl / len(wl)
    return 206.835 - 1.015 * wps - 84.6 * spw, 0.39 * wps + 11.8 * spw - 15.59


def per10k(count, nwords):
    return 10000.0 * count / nwords


# ---- lexicons (project-specific; published with the report) ---------------
PROG_CI = [  # case-insensitive, whole word
    r'rank', r'ranks', r'ranked', r'kindled', r'kindling', r'twin-kindled',
    r'classification', r'classified', r'unclassified', r'placement', r'placements',
    r'division', r'standings', r'roster', r'rosters', r'provisional',
    r'sequence', r'sequenced', r'sequences', r'stack', r'stacked', r'stacking',
    r'dram', r'drams', r'heat-line', r'heat-lines', r'stance', r'ward', r'warded',
    r'edge-light', r'mastery', r'backwash', r'three-door', r'ashcraft',
    r'(?:ember|hand|still|first|one|two|three|single)[- ]doors?',
]
PROG_CS = [  # case-sensitive: rank names, axes, named techniques
    r'Ember', r'Flame', r'Fire', r'Torch', r'Blaze', r'Glory',
    r'Rank', r'Hold', r'Draw', r'Call', r'Edge', r'Stride', r'Strode',
    r'Strides', r'Sustain', r'Ward', r'Grade',
]
REPORTING = ['said', 'asked', 'called', 'shouted', 'whispered', 'replied',
             'agreed', 'added', 'answered', 'muttered', 'murmured', 'snapped',
             'cried', 'told']
COMBAT = ['strike', 'struck', 'strikes', 'block', 'blocked', 'blocking',
          'dodge', 'dodged', 'blade', 'blades', 'impact', 'cut', 'hit', 'hits',
          'thrust', 'swing', 'swung', 'blow', 'feint', 'feinted', 'spar',
          'sparring', 'bout', 'bouts', 'fight', 'fought', 'fighting', 'fighter',
          'fighters', 'kill', 'kills', 'killed', 'spear', 'bar']
FILLERS = ['that', 'just', 'almost', 'felt', 'seemed']
LY_STOP = {'only', 'family', 'families', 'early', 'reply', 'supply', 'belly',
           'ugly', 'holy', 'fly', 'july', 'apply', 'rely', 'lily', 'jelly',
           'ally', 'bully', 'silly', 'chilly', 'hilly', 'curly', 'elderly',
           'lonely', 'lovely', 'friendly', 'unfriendly', 'likely', 'unlikely',
           'early', 'daily', 'weekly', 'quarterly', 'assembly', 'butterfly',
           'italy', 'gravelly', 'rumbly', 'wobbly', 'lumpy', 'ply'}
PHRASES = ['for a moment', 'for a long moment', 'for a long time', 'for a while',
           'did not', 'had not', 'could not', 'was not', 'it was not',
           'the way', 'as if', 'like a', 'at once', 'very', 'a little',
           'said nothing', 'did not say anything', 'did not answer',
           'looked at', 'out loud', 'write it down', 'wrote it down',
           'writing it down', 'i want it said', "it's said"]
DEV_MARKERS = [r'realized', r'realised', r'decided', r'understood',
               r'for the first time', r'swore', r'no longer', r'made the decision',
               r'found out', r'had never', r'she knew', r'he knew', r'learned']
LEAD = ['Kiva', 'Rowan']
CAST = ['Mara', 'Orla', 'Anwen', 'Perrin', 'Kellan', 'Ysra', 'Rhea']


def count_ci(text, terms):
    low = text.lower()
    c = collections.Counter()
    for t in terms:
        c[t] = len(re.findall(r'(?<![A-Za-z\-])' + t + r'(?![A-Za-z\-])', low))
    return c


def count_prog(text):
    c = collections.Counter()
    low = text.lower()
    for t in PROG_CI:
        c[t] = len(re.findall(r'(?<![A-Za-z\-])(?:' + t + r')(?![A-Za-z])', low))
    for t in PROG_CS:
        c[t + ' (cs)'] = len(re.findall(r'(?<![A-Za-z\-])' + t + r'(?![A-Za-z])', text))
    # avoid double counting: "Ward" (cs) is also matched by "ward" (ci);
    # "Ember door" is matched by both the compound and "Ember" (cs).
    c['Ward (cs)'] = 0
    return c


def dev_proxy(text, names):
    """Formula §5 proxy: a marker with a listed name within 120 characters."""
    hits = 0
    for m in re.finditer('|'.join(DEV_MARKERS), text, flags=re.I):
        window = text[max(0, m.start() - 120): m.end() + 120]
        if any(re.search(r'\b' + n + r'\b', window) for n in names):
            hits += 1
    return hits


def main():
    print('SHA-256 (first 16) / raw whitespace word count')
    data = {}
    for f in FILES:
        raw = load(f)
        data[f] = raw
        print('  %-11s %s %6d' % (f, hashlib.sha256(raw.encode()).hexdigest()[:16],
                                  len(raw.split())))

    print('\n== 1. Sentences (tokenizer: rule-based, see sentences()) ==')
    print('%-11s %6s %6s %6s %7s %7s %6s %6s %4s' % (
        'file', 'words', 'sents', 'mean', 'median', 'pstdev', '<=5%', '>=40%', 'max'))
    allsent, movsent = [], []
    tot = {}
    for f in FILES:
        text = '\n\n'.join(sections(data[f]))
        sl = sentences(text)
        st = sent_stats(sl)
        nw = len(words(clean(text)))
        tot[f] = nw
        allsent += sl
        if f != 'prologue':
            movsent += sl
        print('%-11s %6d %6d %6.2f %7.1f %7.2f %6.1f %6.2f %4d' % (
            f, nw, st['n'], st['mean'], st['median'], st['pstdev'], st['le5'],
            st['ge40'], st['mx']))
    for label, sl in (('ALL 9 files', allsent), ('Chapters 1-8', movsent)):
        st = sent_stats(sl)
        print('%-11s %6s %6d %6.2f %7.1f %7.2f %6.1f %6.2f %4d' % (
            label[:11], '', st['n'], st['mean'], st['median'], st['pstdev'],
            st['le5'], st['ge40'], st['mx']))
    lens = [len(words(s)) for s in allsent]
    hist = collections.Counter(min(x, 45) // 5 * 5 for x in lens)
    print('  length histogram (bucket start: share%): ' + ', '.join(
        '%d:%.1f' % (k, 100 * hist[k] / len(lens)) for k in sorted(hist)))
    longest = sorted(allsent, key=lambda s: -len(words(s)))[:3]
    for s in longest:
        print('  longest (%d w): %s...' % (len(words(s)), s[:110]))

    print('\n== 2. Paragraphs and section breaks (typographic, not ASR pauses) ==')
    allp, allsec = [], []
    for f in FILES:
        secs = sections(data[f])
        pl = [len(words(p)) for s in secs for p in paragraphs(s)]
        sw = [len(words(clean(s))) for s in secs]
        allp += pl
        allsec += sw
        print('%-11s paras %4d mean %5.1f median %4.1f | sections %2d mean %6.0f min %5d max %5d | breaks/10k %4.1f' % (
            f, len(pl), statistics.mean(pl), statistics.median(pl), len(sw),
            statistics.mean(sw), min(sw), max(sw), per10k(len(sw), sum(sw))))
    print('ALL         paras %4d mean %5.1f median %4.1f | sections %2d mean %6.0f | breaks/10k %4.1f' % (
        len(allp), statistics.mean(allp), statistics.median(allp), len(allsec),
        statistics.mean(allsec), per10k(len(allsec), sum(allsec))))
    print('  paragraphs >= 100 words: %d; >= 150 words: %d; one-sentence-or-less (<=12 w): %.1f%%' % (
        sum(1 for x in allp if x >= 100), sum(1 for x in allp if x >= 150),
        100 * sum(1 for x in allp if x <= 12) / len(allp)))

    print('\n== 3. Readability (syllables: heuristic vowel-group estimator) ==')
    for f in FILES:
        fre, fk = flesch('\n\n'.join(sections(data[f])))
        print('%-11s FRE %5.1f  FK grade %4.1f' % (f, fre, fk))
    fre, fk = flesch('\n\n'.join('\n\n'.join(sections(data[f])) for f in FILES))
    print('ALL         FRE %5.1f  FK grade %4.1f' % (fre, fk))
    fre, fk = flesch('\n\n'.join('\n\n'.join(sections(data[f])) for f in FILES[1:]))
    print('Ch 1-8      FRE %5.1f  FK grade %4.1f' % (fre, fk))

    print('\n== 4. Progression vocabulary (project lexicon) per 10k words ==')
    grand = collections.Counter()
    for f in FILES:
        text = clean('\n\n'.join(sections(data[f])))
        c = count_prog(text)
        grand.update(c)
        print('%-11s hits %4d  per10k %6.1f' % (f, sum(c.values()), per10k(sum(c.values()), tot[f])))
    W = sum(tot.values())
    Wm = W - tot['prologue']
    print('ALL         hits %4d  per10k %6.1f   (words %d)' % (sum(grand.values()), per10k(sum(grand.values()), W), W))
    mov = collections.Counter()
    for f in FILES[1:]:
        mov.update(count_prog(clean('\n\n'.join(sections(data[f])))))
    print('Ch 1-8      hits %4d  per10k %6.1f   (words %d)' % (sum(mov.values()), per10k(sum(mov.values()), Wm), Wm))
    print('  top terms (all files): ' + ', '.join('%s=%d' % kv for kv in grand.most_common(24)))

    print('\n== 5. Development-moment regex proxy (formula s5 method) ==')
    for f in FILES:
        text = clean('\n\n'.join(sections(data[f])))
        lead = dev_proxy(text, LEAD)
        cast = {n: dev_proxy(text, [n]) for n in CAST}
        print('%-11s lead %2d (%.1f/10k) | %s' % (f, lead, per10k(lead, tot[f]),
              ' '.join('%s=%d' % kv for kv in cast.items() if kv[1])))
    text = clean('\n\n'.join('\n\n'.join(sections(data[f])) for f in FILES[1:]))
    lead = dev_proxy(text, LEAD)
    print('Ch 1-8      lead %2d (%.1f/10k) | %s' % (lead, per10k(lead, Wm), ' '.join(
        '%s=%d(%.1f/10k)' % (n, dev_proxy(text, [n]), per10k(dev_proxy(text, [n]), Wm)) for n in CAST)))

    print('\n== 6. POV word share (manual viewpoint map) ==')
    pov = collections.Counter()
    for f in FILES:
        secs = sections(data[f])
        for i, s in enumerate(secs):
            who = 'Prologue (historical anchors)' if f == 'prologue' else POV.get(f, {}).get(i, 'Kiva')
            if (f, i) in POV_CHECK:
                assert clean(s).startswith(POV_CHECK[(f, i)]), (f, i, s[:60])
            pov[who] += len(words(clean(s)))
    # the final prologue snapshot (## 11) is Kiva's viewpoint: measure it apart
    p11 = data['prologue'].split('## 11. Three Doors')[1]
    p11w = len(words(clean('\n\n'.join(sections(p11)))))
    for who, n in pov.most_common():
        print('  %-30s %6d  %5.1f%% of all  %s' % (who, n, 100 * n / W,
              ('%5.1f%% of Ch1-8' % (100 * n / Wm)) if who != 'Prologue (historical anchors)' else ''))
    print('  prologue snapshot 11 (Kiva, age 13) words: %d' % p11w)
    lead_all = pov['Kiva'] + p11w
    print('  lead share incl. prologue: %.1f%%; chapters 1-8 only: %.1f%%' % (
        100 * lead_all / W, 100 * pov['Kiva'] / Wm))
    # prologue snapshot sizes
    snaps = re.split(r'(?m)^## \d+\. ', data['prologue'])[1:]
    print('  prologue snapshot words: ' + ', '.join(
        str(len(words(clean('\n\n'.join(sections('\n'.join(s.split('\n')[1:]))))))) for s in snaps))

    print('\n== 7. Secondary signals per 10k words (all 9 files | chapters 1-8) ==')
    A = clean('\n\n'.join('\n\n'.join(sections(data[f])) for f in FILES))
    M = clean('\n\n'.join('\n\n'.join(sections(data[f])) for f in FILES[1:]))
    for label, terms in (('reporting verbs', REPORTING), ('combat terms', COMBAT), ('fillers', FILLERS)):
        ca, cm = count_ci(A, terms), count_ci(M, terms)
        print('  %-16s %6.1f | %6.1f   %s' % (label, per10k(sum(ca.values()), W), per10k(sum(cm.values()), Wm),
              ' '.join('%s=%.1f' % (t, per10k(ca[t], W)) for t in terms if ca[t])))
    for label, T, n in (('all', A, W), ('ch1-8', M, Wm)):
        ly = [w.lower() for w in words(T) if w.lower().endswith('ly') and w.lower() not in LY_STOP and len(w) > 3]
        print('  -ly suffix words (%s): %6.1f per 10k; top: %s' % (label, per10k(len(ly), n),
              ', '.join('%s=%d' % kv for kv in collections.Counter(ly).most_common(10))))
    print('  phrases per 10k (all | ch1-8):')
    for ph in PHRASES:
        a = len(re.findall(r'(?<![A-Za-z])' + re.escape(ph) + r'(?![A-Za-z])', A.lower()))
        m = len(re.findall(r'(?<![A-Za-z])' + re.escape(ph) + r'(?![A-Za-z])', M.lower()))
        print('    %-24s %5d %6.1f | %5d %6.1f' % (ph, a, per10k(a, W), m, per10k(m, Wm)))
    toks = [w.lower() for w in words(A)]
    tri = collections.Counter(zip(toks, toks[1:], toks[2:]))
    print('  top 3-grams (all): ' + ', '.join('%s=%d(%.1f)' % (' '.join(k), v, per10k(v, W)) for k, v in tri.most_common(14)))
    frag = [s for s in allsent if re.match(r'^(Not|No)\b', s.strip('"“')) and len(words(s)) <= 6]
    print('  short "Not/No ..." correction fragments (<=6 w): %d (%.1f per 10k)' % (len(frag), per10k(len(frag), W)))

    print('\n== 8. Cross-checks ==')
    naive = [x for x in re.split(r'(?<=[.!?])["”’]?\s+', re.sub(r'\s+', ' ', A)) if words(x)]
    nl = [len(words(x)) for x in naive]
    print('  naive tokenizer (split after every . ! ?): sents %d mean %.2f median %.1f <=5 %.1f%% >=40 %.2f%%' % (
        len(nl), statistics.mean(nl), statistics.median(nl), 100 * sum(1 for x in nl if x <= 5) / len(nl),
        100 * sum(1 for x in nl if x >= 40) / len(nl)))
    narr = re.sub(r'[“"][^”"]*[”"]', ' ', A)
    ns = [len(words(x)) for x in sentences(narr)]
    print('  narration only (quoted speech removed): sents %d mean %.2f median %.1f <=5 %.1f%% >=40 %.2f%%' % (
        len(ns), statistics.mean(ns), statistics.median(ns), 100 * sum(1 for x in ns if x <= 5) / len(ns),
        100 * sum(1 for x in ns if x >= 40) / len(ns)))
    q = sum(len(words(x)) for x in re.findall(r'[“"][^”"]*[”"]', A))
    print('  words inside double quotes: %d (%.1f%% of all words)' % (q, 100 * q / W))
    syl = sum(syllables(w) for w in words(A))
    print('  syllables per word %.3f; words per sentence %.2f' % (syl / W, W / len(allsent)))
    door = r'(?:ember|hand|still|first|one|two|three|single)[- ]doors?'
    print('  progression hits excluding door compounds: all %.1f per 10k; ch1-8 %.1f per 10k' % (
        per10k(sum(grand.values()) - grand[door], W), per10k(sum(mov.values()) - mov[door], Wm)))
    notfrag = [x for x in allsent if re.match(r'^Not\b', x) and len(words(x)) <= 8]
    print('  narration fragments opening "Not ..." (<=8 w): %d (%.1f per 10k)' % (len(notfrag), per10k(len(notfrag), W)))
    for pat in (r'three thousand', r'ten thousand times', r'six hundred years', r'four hundred kilos',
                r'said it (?:plainly|flatly)', r'did something complicated', r'almost smiled',
                r'for a long (?:time|moment|while)', r'looked at (?:her|him|it|kiva|mara|orla) for a', r'the way you'):
        print('  /%s/: %d' % (pat, len(re.findall(pat, A.lower()))))


if __name__ == '__main__':
    main()
```
