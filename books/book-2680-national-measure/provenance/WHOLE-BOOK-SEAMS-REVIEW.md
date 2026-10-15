# Kindling 2680, Book Two, *The National Measure*: whole-book review C-SEAMS

> Built by TAC

Layer: seams, scene clarity, chapter openings and endings, repeated habits, read-aloud, and terminology across all 48
chapters. Date: 2026-10-15. **Read-only review. No manuscript, ledger, map, packet or canon file was edited.** This report
is the only file this session wrote in the repository. Nothing was committed, pushed, repaired or drafted.

## 0. Who and how

- **This is a same-model-family simulated review, not human reader feedback and not independent testing.** The prose,
  every movement review, every repair and every recheck were also written by Claude Opus 5.5. This read can share their
  blind spots.
- **Model, as the runtime reports it:** Claude Opus 5.5, model identifier `claude-opus-5-5`. It cannot be verified from
  inside the session. No subagent, other model, Skill tool, Codex or OpenAI call was used.
- **Session:** Claude Code background job `ffc1e86f` (job directory `~/.claude/jobs/ffc1e86f`); the harness reports the
  session link as https://claude.ai/code/session_01DCyjsWrajxEZcnvvRQuYEG. It worked read-only in the worktree
  `/Users/drive/kindling-2680-book-02`, branch `codex/kindling-2680-book-02`. Scratch scripts and outputs are in the job's
  `tmp/` directory, outside the repository.
- **Text baseline.** At the start of the run I took a SHA-256 of all 48 files in `manuscript/` (326,215 words by `wc -w`,
  21,068 lines). The SHA-256 of that 48-line hash list is
  `c77a85c091727c4fccc6ed401f6a674433f18f14f4fb9b2d2fdad8fd2367c6b0`. I re-hashed before writing this report and every
  file was **unchanged**. All line numbers below come from `grep -n` / `awk NR` on those files.
- **Movement Six status.** There is no `MOVEMENT-006-RECHECK-CONFIRMATION.md`. `MOVEMENT-006-REPAIR.md` says the
  repair is "not rechecked, not cold-read after repair, not accepted". Chapters 41–48 are uncommitted edits in the
  working tree. A separate Movement Six recheck (`provenance/MOVEMENT-006-RECHECK.md`, job `22f7111d`) appeared during my
  run. I read only its header and searched it for overlap with my Movement Six findings. It does not raise any of them.
  **Chapters 41–48 may still change, so their line numbers may shift. Re-anchor every Movement Six edit by its quoted text
  before applying it.**

### What I read

| Input | How much |
|---|---|
| `provenance/WHOLE-BOOK-REPETITION-DATA.md` | all 153 lines |
| `OWNER_BRIEF.md` | all |
| `provenance/MOVEMENT-00{2,3,4,5}-RECHECK-CONFIRMATION.md` | all (`...006-RECHECK-CONFIRMATION.md` does not exist) |
| `provenance/MOVEMENT-006-REPAIR.md` | first 40 lines (status only) |
| Chapters 1, 20, 31, 46 | in full |
| Every chapter, 1–48 | at least the first 80 and last 60 lines |
| Movement joins | last 150 lines of chs 8, 16, 24, 32, 40; first 150 lines of chs 9, 17, 25, 33, 41 |
| Passages cited below | each one in context; about 40 extra short windows |
| Narration feedback `narration/monroe-1.2.5/calder/*/writing-monroe-feedback.md` | all 25 files (they exist for chs 1–21 only) |
| `UNIVERSE_BIBLE.md` §lay, `packets/MOVEMENT-006.md` door-vocabulary lines, `BOOK_MAP.md` (grep for plank/lay) | targeted |
| Book One (`books/book-2680-opening/manuscript/chapter-26.md`) | one passage: Mr. Adlam's first description |

**I did not read the whole book.** In lines, I read about two-fifths of the manuscript (about 8,900 of 21,068 lines). The
middle stretches of chapters 2–19, 21–30 and 32–48 I read only through searches and short windows. Whole-text
facts in this report (counts, identical sentences, who says a tag line, section anchors) come from scripted searches over
all 48 files, not from reading. A defect inside an unread middle passage that a search would not catch is outside what
this report can vouch for.

## 1. Top line

- **Seams hold.** Each of the six movements opens oriented within its first page: who, where, the day and date, and what
  is at stake, given through action and with no recap lecture. Each movement ends on a turn and a pressure. The date
  chain runs unbroken across all five joins.
- **Seven cross-movement contradictions** that no movement-sized review could see, because each pair sits in different
  movements: Rhea's years as an officer (six or eleven), Mr. Adlam's age, Pike's face, whether Anwen ever blushes,
  Jude's writing hand, and two date slips in chapter 46. One further slip mixes up the day of the week (26:63) and
  would mislead a listener.
- **The worst audible habit is at the seams.** Movements Three, Four and Five end on the same panorama and refrain, and
  the closing three sentences of chapters 24 and 32 are word for word the same. The two fever nights (chapters 23 and
  40) share about a dozen identical or near-identical sentences. These are the top entries in the edit list.
- **Bounded edit list:** 50 line-level edits, ranked by read-aloud cost (§5). There are 27 further located fixes for the
  findings (§2). Every "before" string has been checked by script to occur exactly once on its cited line.

## 2. Findings: defects of the prose

Severity key: **BLOCKING**, a reader or listener would be misled. **CONTRADICTION**, two passages disagree.
**CLARITY**, one pass is unclear. The exact before/after for each fix is under its F-number in §2.1.

| ID | Severity | Location | Quoted text | Problem and evidence | Smallest fix |
|---|---|---|---|---|---|
| WB-01 | CONTRADICTION | 20:351; 31:365; 31:401 | "On every floor for six years she had had a catcher who watched her heel"; "for six years"; "every night for six years" | Six other passages say eleven years: "I've been an officer of this company for eleven years" (Rhea, 3:217); "Rhea had been an officer for eleven years" (7:311); "for the first time in eleven years" (7:385); "an officer of eleven years" (14:389). Pike: "I've called *now* off that heel for eleven years" (6:57); "as they had gone to it for eleven years" (11:133). Movements Three and Four say six. | F01a–c: *six* → *eleven* in all three. |
| WB-02 | CONTRADICTION | 25:393; 36:209 | "He was a thin grey man with a stoop"; "the old man's hand" (this is Adlam, beside Kellan) | 21:403 describes him as "pleasant and fortyish, with a narrow gold cord at his cuff", matching Book One (`book-2680-opening` ch 26:161: "about forty, and pleasant"). Movements Four and Five make him old. | F02a, F02b. |
| WB-03 | CONTRADICTION | 43:191; 44:495; 47:341; 48:107 | "his long brown face" (Pike) | Movements One and Two describe Pike as "a square grey man" (3:265; 8:557), with a "square grey face" (8:487) and a "square face" (6:77; 10:201). Movement Six changes him to long and brown, four times. Two of these instances carry Pike's payoff beat (47:341, the smile "went the whole way"). | F03a–d: "long brown" → "square grey". |
| WB-04 | CONTRADICTION | 34:161; 38:297; 48:245 | "She did not go red. Anwen never went red." | 10:451: "Kiva watched her go red, slowly, from the collar, exactly as her mother had gone red at a laundry table." The same two-sentence beat also recurs word for word three times. | F04a–c: keep "She did not go red." once (34:161); cut "Anwen never went red." everywhere. |
| WB-05 | CONTRADICTION | 41:113 | "Jude, who wrote *Talley* with his left hand for the first time in a week" | Jude's left forearm was frosted on the moor in the second month (15:199). He has written the team book with his "good hand", the right, ever since (15:517; scratches his jaw "with his right hand", 33:129; "The left was for holding", 33:141). Aske's bar is on *gripping* with the left until Monday (33:139), set four days earlier, not a week. | F05: he steadies the sheet with the left hand while writing. |
| WB-06 | CONTRADICTION | 46:175 | "Mrs. Yeo told me on Saturday. She came down to tell me before she carded you." | Jude's Company card was on the baize by Thursday the 17th: on Friday Kellan touches his card "as Jude had touched his yesterday" (35:13), Perrin's cards were there "yesterday" (35:57), and Kellan read the board "on Thursday at the baize" (36:13). Saturday was after the carding. | F06: "on Saturday" → "on Thursday, first thing". |
| WB-07 | CONTRADICTION | 46:191 | "I asked you in the second month what ash was for," said Jude, "on the Ropewalk steps." | Seven reached Saltmere on the 30th of the second month (17:47). Yeo is at the Ropewalk on Saturday the 5th of the third month (19:253, 19:291), and on Monday the 7th Jude has "been thinking about it since Saturday" (20:299). | F07: drop "in the second month". |
| WB-08 | CONTRADICTION (minor) | 17:139 | "Halden License had come down by the station transit three days before" | 6:461: the Works "sends its four down by station transit on the twenty-eighth of next month; I'm told that it's a day and a half". Ch 17 is Monday the 30th, so leaving on the 28th means arriving on the 29th or 30th, not the 27th. | F08: "three days before" → "the night before". |
| WB-09 | BLOCKING | 26:63 | "And tomorrow's the Longshore. If they go today, you don't plant tomorrow." | Spoken on Monday evening the 14th (26:75 "Monday the 14th"). The next day is the Carry (26:13, Tuesday the 15th), and the Longshore is Wednesday. A listener is told the wrong day for the Hunt. | F09: name the days. |
| WB-10 | CONTRADICTION (minor) | 36:383 | Mara looks at her hand "as she had looked at it on a gallery at the pump house a fortnight ago" | Ch 36 is Friday the 18th. The gallery scenes in which Mara studies the hand are Tuesday the 8th (21:169–291, ten days earlier) and Wednesday the 16th (32:449–471, where she holds it "an inch from the glass" and looks at it). No such scene is a fortnight back. | F10: "a fortnight ago" → "on Wednesday night". |
| WB-11 | CONTRADICTION | 1:95 | "There were four of them besides." | Only three are named: the warden, the fitter and Ned. The carter arrives later. The narration preparer raised this as a non-blocking query (ch 1 feedback file) and it is still open in the text. | F11: "four" → "three". |
| WB-12 | BLOCKING (read-aloud) | 46:101 | "her own sheet: a new one, bought in the second month after the old one, with her name on its pole, went over a race lip at a mill." | Without a finite verb on the relative clause, the listener parses the *new* sheet as the one that went over the race lip. The old sheet was the one lost at Garside's mill (16:37). | F12: "went" → "had gone". |
| WB-13 | CLARITY | 46:129 | "Kellan Renn, standing at the back of the small crowd at the gate with his mother's watch in his pocket and a folded sheet of fault paper that he had given to the Clerk" | The sentence has him still holding a sheet he has already handed over. | F13: reorder the sentence. |
| WB-14 | CLARITY (anchor) | 19:391 | "The pump house was lit when she got there." | First sentence after a section break in a "Kiva:" chapter, but the viewpoint is Orla's. The section's details ("come to the door four times since Tuesday", the transit) fit Orla and not Kiva, yet nothing names her until Hart says "Dane" at 19:405, fourteen lines in. | F14: "she" → "Orla". |
| WB-15 | CLARITY (anchor) | 39:59 | "He was on the gallery at a quarter to seven" | Opens a section in Orla's viewpoint with a bare "He" for Hart. | F15: "He" → "Hart". |
| WB-16 | CLARITY | 20:173 | "The Company man let go of the line." | Two Company men are in play: the one poling the punt (20:113) and the one hauling the third line (20:163). | F16. |
| WB-17 | CLARITY (read-aloud) | 1:67 | "There had been eleven and four days. There were ten and four days now." | Heard aloud, "eleven and four days" does not say weeks. The book's first page is where a listener is least oriented. | F17. |
| WB-18 | CLARITY (minor) | 31:227 | "Kiva took the fourth corner with her left hand" | Four others are already placed on the boards (Ivey at the head, Trewin at the foot, Jude on one side, the boatman on the other), so "the fourth corner" does not add up. | F18: "the fourth corner" → "a corner". |
| WB-19 | CLARITY (term collision) | 41:315 → 41:319 | "two planks holding one thing" … "a tun with a plank nailed under it" | *Plank* as door vocabulary and *plank* as a literal board occur four lines apart, in the scene that teaches the method. | F19: "plank" → "board" at 41:319. |
| WB-20 | CLARITY (terminology; owner) | 13:221 vs 41–43 | 13:221: "A plank was two still doors on one patch of ground." | Movement Six widens *plank* to any group of like doors at one station, "the catchers' plank" (four wards) and "two planks" of wards and Embers (41:315). It never restates the wider sense. The same door type is also named two ways in one sequence: Anwen's four wards are "the first ward line" (43:185) but Pru's four wards are "the catchers' plank". | Owner decision OD-5. |
| WB-21 | CLARITY (seam habit) | 24:381–391; 32:589–597; 40:375–383 | "…the town's count went on. Four and four. Fifty-seven to the minute, or faster." / "*It keeps time.* / It was not a quarter to seven. It was not on purpose. She did not write it down." | Three consecutive movements end on the same machinery: a survey of places ("In a black iron box with three locks…", "In a pump house…"), the town-count refrain, and the disk or finger ritual. The last three sentences of chs 24 and 32 are identical. 40:377 repeats 24:381's black-box sentence nearly word for word. Heard in sequence, these movement endings sound copied. | §5 R01, R06; R07/R08 subject to OD-1. |
| WB-22 | CLARITY (cross-movement echo) | 23:339–409 vs 40:293–335 | e.g. "There was the count, under the floor and the chandlery and the quay, four and four, going on." (identical); "Aske looked at her over his spectacles in the candlelight." (identical); "\"Nothing came.\" She shut her eyes." (identical); "That's all I'll write. It's all I know." (identical) | A sentence-level comparison finds about a dozen identical or near-identical sentences between the two fever nights. 40:321 deliberately signals the echo ("as it had on the barge and on the night after the Counting House"), but at this density the second scene reads as reused text. | §5 R02–R05 (OD-4 if the echo is wanted). |

### 2.1 Exact fixes for the findings (27 edits)

Each "before" string occurs exactly once on the cited line (script-checked against the baseline). Where a cut joins two
pieces of one speaker's dialogue, the merge of the quotation marks is shown.

- **F01a** `chapter-20.md:351` (WB-01)
  - before: `On every floor for six years she had had a catcher who watched her heel`
  - after: `On every floor for eleven years she had had a catcher who watched her heel`
- **F01b** `chapter-31.md:365` (WB-01)
  - before: `and nobody at the far edge at all, for six years.`
  - after: `and nobody at the far edge at all, for eleven years.`
- **F01c** `chapter-31.md:401` (WB-01)
  - before: `every line of it, every night for six years,`
  - after: `every line of it, every night for eleven years,`
- **F02a** `chapter-25.md:393` (WB-02)
  - before: `He was a thin grey man with a stoop and a habit of looking astonished,`
  - after: `He was a pleasant man of forty or so with a narrow gold cord at his cuff and a habit of looking astonished,`
- **F02b** `chapter-36.md:209` (WB-02)
  - before: `But Kiva saw the old man's hand move on the bench,`
  - after: `But Kiva saw Adlam's hand move on the bench,`
- **F03a** `chapter-43.md:191` (WB-03)
  - before: `his long brown face doing the thing it did`
  - after: `his square grey face doing the thing it did`
- **F03b** `chapter-44.md:495` (WB-03)
  - before: `His long brown face did the thing it did, very nearly.`
  - after: `His square grey face did the thing it did, very nearly.`
- **F03c** `chapter-47.md:341` (WB-03)
  - before: `His long brown face did the thing it did.`
  - after: `His square grey face did the thing it did.`
- **F03d** `chapter-48.md:107` (WB-03)
  - before: `His long brown face did the thing it did, nearly.`
  - after: `His square grey face did the thing it did, nearly.`
- **F04a** `chapter-34.md:161` (WB-04)
  - before: `She did not go red. Anwen never went red.`
  - after: `She did not go red.`
- **F04b** `chapter-38.md:297` (WB-04)
  - before: `At home." She did not go red. Anwen never went red. "I'll be on`
  - after: `At home. I'll be on`
- **F04c** `chapter-48.md:245` (WB-04)
  - before: `She did not go red. Anwen never went red.`
  - after: (delete; close the gap to one space)
- **F05** `chapter-41.md:113` (WB-05)
  - before: `and so did Jude, who wrote *Talley* with his left hand for the first time in a week, because Aske had said Monday, and it was Monday.`
  - after: `and so did Jude, who steadied the sheet with his left hand while he wrote *Talley,* because Aske had said Monday, and it was Monday.`
- **F06** `chapter-46.md:175` (WB-06)
  - before: `Mrs. Yeo told me on Saturday.`
  - after: `Mrs. Yeo told me on Thursday, first thing.`
- **F07** `chapter-46.md:191` (WB-07)
  - before: `"I asked you in the second month what ash was for," said Jude,`
  - after: `"I asked you what ash was for," said Jude,`
- **F08** `chapter-17.md:139` (WB-08)
  - before: `Halden License had come down by the station transit three days before`
  - after: `Halden License had come down by the station transit the night before`
- **F09** `chapter-26.md:63` (WB-09)
  - before: `And tomorrow's the Longshore. If they go today, you don't plant tomorrow.`
  - after: `And Wednesday's the Longshore. If they go on Tuesday, you don't plant on Wednesday.`
- **F10** `chapter-36.md:383` (WB-10)
  - before: `as she had looked at it on a gallery at the pump house a fortnight ago.`
  - after: `as she had looked at it on a gallery at the pump house on Wednesday night.`
- **F11** `chapter-01.md:95` (WB-11)
  - before: `There were four of them besides.`
  - after: `There were three of them besides.`
- **F12** `chapter-46.md:101` (WB-12)
  - before: `with her name on its pole, went over a race lip at a mill.`
  - after: `with her name on its pole, had gone over a race lip at a mill.`
- **F13** `chapter-46.md:129` (WB-13)
  - before: `Kellan Renn, standing at the back of the small crowd at the gate with his mother's watch in his pocket and a folded sheet of fault paper that he had given to the Clerk at a quarter past eight, did not say anything.`
  - after: `Kellan Renn, who had given the Clerk a folded sheet of fault paper at a quarter past eight, stood at the back of the small crowd at the gate with his mother's watch in his pocket and did not say anything.`
- **F14** `chapter-19.md:391` (WB-14)
  - before: `The pump house was lit when she got there.`
  - after: `The pump house was lit when Orla got there.`
- **F15** `chapter-39.md:59` (WB-15)
  - before: `He was on the gallery at a quarter to seven,`
  - after: `Hart was on the gallery at a quarter to seven,`
- **F16** `chapter-20.md:173` (WB-16)
  - before: `The Company man let go of the line.`
  - after: `The Company man on the third line let go of it.`
- **F17** `chapter-01.md:67` (WB-17)
  - before: `There had been eleven and four days. There were ten and four days now.`
  - after: `There had been eleven weeks and four days. There were ten weeks and four days now.`
- **F18** `chapter-31.md:227` (WB-18)
  - before: `and Kiva took the fourth corner with her left hand,`
  - after: `and Kiva took a corner with her left hand,`
- **F19** `chapter-41.md:319` (WB-19)
  - before: `It held because it's a tun with a plank nailed under it.`
  - after: `It held because it's a tun with a board nailed under it.`

## 3. Seams (the five joins and the two ends)

| Join | Last page before | First page after | Orientation within the first page | Result |
|---|---|---|---|---|
| M1 → M2 (8 → 9) | Saturday the 30th, last day of the first month. Perrin chalks *44*; "Jude let go the rung." | "*43*"; "It's Sunday. It's the first of the second month." Old Yard, Orla, the mast; the crossing calendar (9:35). | who, where, when, stake: yes, through action | **Pass.** Turn: the purse-string drill. Pressure: 44 days. |
| M2 → M3 (16 → 17) | The barge, Saturday the 28th; fever broken; "Sixteen"; the gate opens Tuesday | Coast boat, Monday the 30th; Aske: "Warm. As it was on Wednesday"; Perrin "Fourteen"; Saltmere by 4 p.m. | yes; the river-to-coast-boat change is covered in one clause (17:5) | **Pass.** The countdown arithmetic carries over (16 → 15 → 14 → 13). |
| M3 → M4 (24 → 25) | Monday the 14th, 7 a.m., "Nought"; Kiva not at the Bench | Salt Hall, "twenty to nine on Monday morning", Kiva on the gallery with Aske | yes | **Pass.** The turn is the Proprietor's refusal and the ring under seal. **But see WB-21: same ending machinery as M4 and M5.** |
| M4 → M5 (32 → 33) | Wednesday night the 16th; Penhale entered under *Before*; "In the morning there would be the Lane." | Thursday, 5 a.m.: the Marshal's page "After D. Penhale"; Ivey returns the sheets; Aske at seven | yes | **Pass.** The strongest join in the book. |
| M5 → M6 (40 → 41) | Sunday the 20th: "The Measure was read. Seven was seventh."; three days to Wednesday; Rhea's card | Monday the 21st, quarter to seven: the latch ritual; Kellan's card; the warrant | yes | **Pass.** No recap lecture. |
| Book ends | M1 opens on action (the parcel, the mate's question). Ch 48 ends on a hull with an unknown light and a book entry. | n/a | n/a | Book Two's arc closes in chs 45–48 before the closing image (OD-9). |

No handoff is missing or contradictory at any join. The repeated handoff is the one in WB-21: three movement endings
built from the same parts.

## 4. Chapter openings and endings across the book

### 4.1 Openings (first sentence of each chapter)

- **Weekday in the first sentence: 25 of 48. Clock time in the first sentence: 25 of 48** (scripted count). This is the
  book's main way of orienting a listener and it works. It is also heard as a formula. Recommendation: keep it (OD-8).
- **Aske takes the hand: 9 chapter openings** (5, 22, 23, 24, 28, 29, 32, 43, 47), including a run of three in a row
  (22, 23, 24) and two (28, 29). The same ritual also opens at least 11 sections inside chapters (9:163, 12:75, 14:13,
  18:407, 24:345, 26:227, 33:53, 34:295, 37:29, 41:61, 46:15). Its phrasing repeats too: "held the hand … for two
  minutes by his watch", "wrote it on the card, standing, against the window frame" (8 chapters). This is the most
  audible opening habit. It is also a clock the plot depends on (OD-2).
- **The quarter-to-seven fingers ritual** ("*It keeps time.*") opens chs 41 and 46 and starts or ends sections in many
  others (among them 24, 26, 32, 33, 40 and 42). It is a deliberate motif with a payoff at 46:9 ("No answer"). Not edited, except where it
  closes two movements word for word (R01).
- **Crossing-ritual openings:** chs 14 and 16 open "The third/fourth crossing went…". These suit the countdown and are not
  a problem.
- **Card or notice openings:** chs 2, 7, 26, 34, 37 (plus 11:37, 33:3). Varied enough.

### 4.2 Endings (last paragraph of each chapter)

- **Bed or sleep endings: 10** (5, 16, 19, 22, 23, 28, 32, 40, 42, 46), seven of them in Movements Three to Six.
- **"The disk is cold" at or next to the ending: 6** (23, 24, 32, 39, 40, 48). Chapter 48's last line, "*The disk is
  cold.*", is the book's final beat. By then it has been heard as a closing five times (OD-3).
- **Book entry or ledger reading as the close: 10 or more** (1, 9, 12, 13, 14, 16, 17, 25, 32, 48). Strongest in Movement
  Two, where chs 12, 13 and 14 all end on Jude's sum or the license. **Consecutive chapter endings 13 and 14 both end on
  Perrin's "Under my name."** with the license and the coil of tarred rope on the table (13:513; 14:397). Hearable, but
  short and in character. Left to the author.
- **Stated-lesson endings:** 7 ("She only knew what it had cost to find out that it was missing"), 10 and 12 ("*Why: …*").
  Not frequent enough to count as a habit.
- **One-line hook endings:** 8, 26, 29, 43 ("Jude let go the rung." / "The bell went." / "Your stow." / "*Take.*").
  Well spaced. These are protected scene-ending short beats; none is edited.

## 5. Whole-book habits: the ranked bounded edit list (50 edits)

### 5.1 What crosses the audible threshold (from the repetition data, checked against the text)

| Family | Count | Where it clusters | Verdict |
|---|---|---|---|
| Silence beats ("did not say anything", "said nothing", "Nobody said anything", "did not answer") | 170 sentences | ch 32: 14; ch 31: 9 (6 in lines 313–367); chs 13–15: 19, including 8 stand-alone "Nobody said anything." paragraphs | **Audible.** Cut where two fall within a page. |
| "did not look at/up/round/away" | 172 | ch 36: 11; ch 37: 10; ch 40: 8 | **Audible** in the hearing chapters. |
| "[X] looked at [her/him/it] for a long time/moment." as a paragraph of its own | 24 or more | spread across Movements Three to Six; identical sentences "She looked at it for a long time." (31, 40, 48) and "He looked at it for a long time." (23, 38, 47) | **Audible.** |
| "She did not look at a paper." (the Clerk and the Chair) | 6 (25:37, 27:395, 29:49, 36:115, 40:257, 46:259) | one per hearing | Tag at saturation. Cut three. |
| "Something moved at the corner of her mouth, and was gone." (the Clerk) | 3 identical (36:309, 40:267, 47:187) | | Cut the third. |
| "He nearly smiled." | 13 (Pike 9, plus one reported at 31:339; Hart 35:351; Kellan 35:37, 47:267) | | The payoff at 47:341 ("It went the whole way, this time") depends on this being *Pike's*. Cut the three that are not his. |
| "his hand pressed to his side" (Perrin, after the Carry) | 25 | 35:67 and 35:71 four lines apart; one in each of 46, 47, 48 | Cut four. |
| "slowly" | 128 | pairs within four lines in chs 19, 22, 28, 30 | Cut four. |
| Perrin's "I'd like it known", Jude's "I'd want it said", Anwen's "I want it said" | 96 together | each owned by its speaker (scripted check); one leak: Anwen uses Jude's form at 16:85, ten lines before Jude uses it (16:95) | Voice, not tic. Fix the leak only (R50). |
| "the far edge" (136), "nobody" (617), *Set. / Nobody. / Far edge.* calls | | | **Protected** (book vocabulary and call words). Not touched. |
| Ledger figures, card wording ("Then we look again, and either of us may say no."; "Not for a bank, a floor, a crossing or a sale.") | | | **Protected.** Not touched. |
| Similes (per-movement density 17.2 → 10.4) | | | Falling through the book. No action. |

### 5.2 The list

Ranked by read-aloud cost. First come identical text at movement endings and in the fever echo (R01–R08). Then
same-page silence clusters (R09–R15). Then identical tag sentences (R16–R22). Then within-chapter beat clusters
(R23–R33). Then tag ownership and pairs (R34–R50). Apply them in order, stopping wherever the owner wants; each edit
stands alone. R07 and R08 depend on OD-1.

- **R01** `chapter-32.md:597` (identical to 24:391)
  - before: `It was not a quarter to seven. It was not on purpose. She did not write it down.`
  - after: `She did not write it down.`
- **R02** `chapter-40.md:327` (identical to 23:389)
  - before: `Aske looked at her over his spectacles in the candlelight.`
  - after: (delete the whole paragraph and one of the blank lines round it)
- **R03** `chapter-40.md:311` (identical to 23:381)
  - before: `There was the count, under the floor and the chandlery and the quay, four and four, going on.`
  - after: (delete; close the gap to one space)
- **R04** `chapter-40.md:299` (third use: 16:341, 23:357)
  - before: `"Going up." He put the back of his hand against her cheek, as her aunt used to. "Two of them.`
  - after: `"Going up. Two of them.`
- **R05** `chapter-40.md:299` (identical to 23:367)
  - before: `*The third this year. Two Glory masters inside six hours.* That's all I'll write. It's all I know."`
  - after: `*The third this year. Two Glory masters inside six hours.*"`
- **R06** `chapter-40.md:377` (near-identical to 24:381)
  - before: `In the Board's press, in a black iron box with three locks, there was a paper with a seal on it and the hour, which would be opened at noon on Wednesday.`
  - after: (delete; close the gap to one space)
- **R07** `chapter-32.md:589` (refrain also 24:383, 40:375 (OD-1))
  - before: `the town went on keeping its count. Four and four. Fifty-seven to the minute, or faster. On the Longshore`
  - after: `the town went on keeping its count. On the Longshore`
- **R08** `chapter-40.md:375` (refrain also 24:383, 32:589 (OD-1))
  - before: `Saltmere went on keeping its count. Four and four. Fifty-seven to the minute, or faster. At the end of the Mole`
  - after: `Saltmere went on keeping its count. At the end of the Mole`
- **R09** `chapter-31.md:321` (ch 31 silence cluster 313-367)
  - before: `She did not say anything either.`
  - after: (delete; close the gap to one space)
- **R10** `chapter-31.md:345` (ch 31 silence cluster)
  - before: `Rhea had nothing to say to that, so she did not say anything.`
  - after: `Rhea had nothing to say to that.`
- **R11** `chapter-32.md:179` (ch 32: 14 silence beats)
  - before: `Polglase did not answer that. He took his spectacles off`
  - after: `Polglase took his spectacles off`
- **R12** `chapter-32.md:115` (ch 32: 14 silence beats)
  - before: `Nobody said anything to that.`
  - after: (delete the whole paragraph and one of the blank lines round it)
- **R13** `chapter-32.md:443` (ch 32 silence beats)
  - before: `Orla did not answer that. There was no answer to it.`
  - after: `There was no answer to that.`
- **R14** `chapter-32.md:465` (ch 32 silence beats)
  - before: `Hart did not say anything, but Peverell turned her head.`
  - after: `Peverell turned her head.`
- **R15** `chapter-32.md:483` (ch 32 silence beats)
  - before: `Peverell said nothing. Then she took a pencil`
  - after: `Peverell took a pencil`
- **R16** `chapter-29.md:49` (Clerk/Chair tag x6)
  - before: `Students close no tear." She did not look at a paper. "Every bag`
  - after: `Students close no tear. Every bag`
- **R17** `chapter-46.md:259` (Clerk/Chair tag x6)
  - before: `by design." She did not look at a paper. "That's a better record`
  - after: `by design. That's a better record`
- **R18** `chapter-36.md:115` (Clerk/Chair tag x6)
  - before: `at Meridian." She did not look at a paper. "I sent them`
  - after: `at Meridian. I sent them`
- **R19** `chapter-47.md:187` (identical sentence 36:309, 40:267)
  - before: `Something moved at the corner of her mouth, and was gone.`
  - after: (delete; close the gap to one space)
- **R20** `chapter-40.md:349` (identical sentence 31:267, 48:89)
  - before: `She looked at it for a long time.`
  - after: (delete the whole paragraph and one of the blank lines round it)
- **R21** `chapter-48.md:89` (identical sentence 31:267, 40:349)
  - before: `She stopped. She looked at it for a long time.`
  - after: `She stopped.`
- **R22** `chapter-47.md:195` (identical sentence 23, 38:233)
  - before: `He looked at it for a long time. Then he shut it`
  - after: `Then he shut it`
- **R23** `chapter-15.md:41` (M2 standalone 'Nobody said anything' x9 in 13-15)
  - before: `Nobody said anything for a moment.`
  - after: (delete the whole paragraph and one of the blank lines round it)
- **R24** `chapter-15.md:487` (M2 standalone beat)
  - before: `Nobody said anything.`
  - after: (delete the whole paragraph and one of the blank lines round it)
- **R25** `chapter-14.md:243` (M2 standalone beat)
  - before: `Nobody said anything for a moment.`
  - after: (delete the whole paragraph and one of the blank lines round it)
- **R26** `chapter-13.md:507` (M2 standalone beat)
  - before: `Nobody said anything for a moment. Mara, at the far end`
  - after: `Mara, at the far end`
- **R27** `chapter-16.md:69` (M2 silence beat; doubled with without a word)
  - before: `She did not say anything. She held it out to Kiva, without a word,`
  - after: `She held it out to Kiva, without a word,`
- **R28** `chapter-43.md:249` (ch 43 silence beats 157-249)
  - before: `Aske, on his bag at the north end of the sill, did not say anything. He was looking at her hand.`
  - after: `Aske, on his bag at the north end of the sill, was looking at her hand.`
- **R29** `chapter-47.md:223` (ch 47 silence beats x5)
  - before: `Kiva did not say anything.`
  - after: `Kiva waited.`
- **R30** `chapter-43.md:157` (ch 43 silence beats 157-249)
  - before: `past Jude, who looked at her and did not say anything,`
  - after: `past Jude, who looked at her,`
- **R31** `chapter-36.md:229` (ch 36 'did not look at' x11)
  - before: `My own isn't on it." She did not look at Mara. "If the bank`
  - after: `My own isn't on it. If the bank`
- **R32** `chapter-36.md:103` (ch 36 'did not look at' x11)
  - before: `I've been at the pump house." She did not look at the sister. "She's not said what for."`
  - after: `I've been at the pump house. She's not said what for."`
- **R33** `chapter-40.md:245` (ch 40 'did not look at' x8)
  - before: `Mr. Rusk will tell you so." She did not look at Rusk. "I'll tell you mine`
  - after: `Mr. Rusk will tell you so. I'll tell you mine`
- **R34** `chapter-35.md:351` (keep 'nearly smiled' Pike's for 47:341)
  - before: `standing up." He nearly smiled. "Lay them on`
  - after: `standing up. Lay them on`
- **R35** `chapter-47.md:267` (keep 'nearly smiled' Pike's)
  - before: `where he's wanted." He nearly smiled. "I was told`
  - after: `where he's wanted. I was told`
- **R36** `chapter-35.md:37` (keep 'nearly smiled' Pike's)
  - before: `wanting you to win." He nearly smiled. "I'd expect`
  - after: `wanting you to win. I'd expect`
- **R37** `chapter-22.md:47` (Dray tag x5)
  - before: `Her face did what it always did. But she had come forward`
  - after: `She had come forward`
- **R38** `chapter-35.md:71` ('hand pressed to his side' x25; 35:67 four lines above)
  - before: `against the baize, with his hand pressed to his side, in his round careful hand.`
  - after: `against the baize, in his round careful hand.`
- **R39** `chapter-46.md:39` ('pressed to his side' x25)
  - before: `Perrin with his hand pressed to his side,`
  - after: `Perrin with his ribs strapped,`
- **R40** `chapter-47.md:147` ('pressed to his side' x25)
  - before: `Perrin at the end with his hand pressed to his side,`
  - after: `Perrin at the end,`
- **R41** `chapter-48.md:245` ('pressed to his side' x25)
  - before: `At Perrin with his hand pressed to his side, at Jude`
  - after: `At Perrin, at Jude`
- **R42** `chapter-19.md:15` ('slowly' 19:11 four lines above)
  - before: `The fingers came in, slowly, all ten.`
  - after: `The fingers came in, all ten.`
- **R43** `chapter-22.md:243` ('slowly' x3 in 239-243)
  - before: `He sat with his heart going slowly and his hands on the cloth and waited.`
  - after: `He sat with his hands on the cloth and waited.`
- **R44** `chapter-28.md:255` ('slowly' 28:243)
  - before: `He shook it slowly and properly, once,`
  - after: `He shook it properly, once,`
- **R45** `chapter-30.md:227` ('slowly' 30:223)
  - before: `And it bent over, slowly, as a page turns.`
  - after: `And it bent over as a page turns.`
- **R46** `chapter-35.md:35` ('for a long moment' x42)
  - before: `He looked at her for a long moment. Then he nodded, once,`
  - after: `He looked at her. Then he nodded, once,`
- **R47** `chapter-42.md:297` ('for a long moment' x42)
  - before: `The Proprietor turned his head and looked at him for a long moment.`
  - after: `The Proprietor turned his head and looked at him.`
- **R48** `chapter-43.md:101` ('for a long time' x59)
  - before: `The Proprietor looked at her for a long time.`
  - after: `The Proprietor looked at her.`
- **R49** `chapter-47.md:185` ('for a long moment' x42)
  - before: `The Clerk looked at him for a long moment.`
  - after: `The Clerk looked at him.`
- **R50** `chapter-16.md:85` (Anwen using Jude's tag; 16:95 Jude's own 'I'd want it said' ten lines on)
  - before: `"I'm sorry. I'd want it said that we're sorry."`
  - after: `"I'm sorry."`

Each edit was checked for its join. No cut leaves a speech tag pointing at the wrong person, or two paragraphs by the
same speaker back to back without a tag. Where two quotations would touch, they are merged (R04, R17, R18, R31–R36, F04b).

## 6. Scene clarity in the four full chapters, and the "Kiva:" titles

- **Ch 1 (in full).** The opening is clear and oriented: the parcel, the mate, Kiva's three shut doors and why. The drum
  scene's positions are clear (warden at the door, Ned at the grating, Kiva on the pavement, Mara on the sill). Two
  located items: WB-11 (1:95, "four … besides") and WB-17 (1:67, "eleven and four days"). Speaker attribution is clear
  throughout.
- **Ch 20 (in full).** The creek's geometry is set before the action (kiddle 40 paces off, seven posts, three purses,
  Mace's six walls on two banks, Rhea in the punt). The slack times are internally consistent (11:54 to 12:14; low water
  6:15; closed 6:45). Rhea's section is anchored in its first sentence (20:315). Located items: WB-16 (20:173, which
  Company man) and WB-01 (20:351, "six years").
- **Ch 31 (in full).** The rescue reads clearly in one pass: who is on which bank, the order catch → carry → plant, and
  where the far end of the sleeve lies. Time is kept (12:44/45 turn, 12:51 flood, "Seven minutes"). Located items:
  WB-01 (31:365, 31:401), WB-18 (31:227), and the silence cluster at 31:313–367 (R09, R10). Rhea's section is anchored
  (31:325).
- **Ch 46 (in full).** Time is clear (7:20 sill, 7:25 keeper's room, 9:30 Ropery Row, 11:00 bagging, noon box, 4:00 Orla,
  9:00 Mara). The prediction read-back is clear line by line. Located items: WB-12 (46:101, BLOCKING), WB-13 (46:129),
  WB-06 (46:175), WB-07 (46:191). Orla's section is anchored (46:281).
- **"Kiva:" titles over sections in other viewpoints.** All 48 chapter titles read "Kiva:". A scripted list of all 324
  section openings was checked. Sections and chapters that open in another viewpoint name that person in the first
  sentence: Kellan 6:417, 12:3, 22:209, 30:3, 36:3, 45:51, 45:325; Orla 2:305, 14:29, 19:353, 32:393, 39:3, 46:281;
  Rhea 7:249, 7:545, 20:315, 31:325, 37:357, 48:69; Mara 4:125, 16:127, 21:169, 26:139, 32:449, 34:187, 45:3, 45:197;
  Anwen 10:345, 18:441, 32:207, 33:159, 42:139.
  **Exceptions:** 19:391 (WB-14) and 39:59 (WB-15). Also 30:145 ("He went back across the mud", Kellan), which is
  acceptable because the chapter opened in his viewpoint; and 4:303 and 21:233, which are resolved within two sentences.
  Every chapter that opens in another viewpoint returns to Kiva before it ends.

## 7. Terminology

| Term | Use across the book | Verdict |
|---|---|---|
| **plank** | Defined at 13:221 ("two still doors on one patch of ground"). The packet widens it to "two like doors on one ground" (`packets/MOVEMENT-006.md:216`). In M6 it is used for four wards ("catchers' plank"), for wards plus Embers ("two planks", 41:315), and as a literal board (41:319). It also means the gangplank in M1 (1:7, 3:441) and appears in a simile (42:97). | **Used several ways.** WB-19 and WB-20; OD-5. |
| **stack / lay / laid** | *Stack* (Meridian) and *lay* (Saltmere) both mean unlike doors open and agreeing, as the bible says (`UNIVERSE_BIBLE.md:87`). Consistent from 17 to 48. Separately, Pike's catcher's verb "I'll lay west / south", "Varley lays east" (5:373, 7:65, 14:245) means placing the cloth. That sense ends in M2, before the Saltmere sense begins (17:445), and the contexts never meet. 19:255 ("called *run* and *lay*") is the Saltmere sense. | Low risk. No edit. |
| **ward / hand door / still door / stance** | Consistent. "Hand, to Ember" is the crossing name. "Stance" is the declared form of the still door. People are called "wards" once, at 41:345 ("wards and Embers and still doors alike"), against the packet's rule (PD-2). | Consistent apart from PD-2. |
| **Hold / hold / Held** | Three senses: the role (a Hold, Hesketh "was Halden's Hold"); the reading line ("Hold: Edge, three point one", 5:219); the Bench verb ("A four that holds…", 25:53). "Held, …" is the ledger balance. Context separates them each time. | Low risk. Noted for the narrator. |
| **step** | M1 uses it as a Circuit grade ("A first step answers a Handful", 2:43; 8:183). Everywhere else it means falling into time (in step, stepped, "a step ends your hold", 25:39), with *the Step* as the patent. The grade sense is not used after ch 8. | Low risk. |
| **crossing** | Kiva's door-to-door gap crossing; the *handed crossing* (13:471) becomes "the pass" / "the pass in three" in M4–M6. The tin's "not for … a crossing" means Kiva's. | Consistent. |
| **the far edge** | The fold technique ("folded it from the far edge", 5:53), the hazard, the second's place, and the call. One physical idea throughout. | Consistent; protected. |
| **a lodger** | 11, 13, 17, 18, 21, 28, 29, 30, 32, 42: the same creature and the same rule (it enters laid or agreeing doors). | Consistent. |
| **the Hold / hold** (as asked) | See Hold. | — |

## 8. Plan differences (BOOK_MAP and packets; not prose defects)

- **PD-1.** `packets/MOVEMENT-006.md:216` says "a **plank** is two like doors on one ground". The M6 prose uses "the
  catchers' plank" for four wards catching a load in the air (41:313; 43:149; 43:185) and "two planks" for wards and
  Embers together (41:315). The prose widens the packet's definition. See WB-20 and OD-5.
- **PD-2.** `packets/MOVEMENT-006.md:217` says "people are not 'wards'". 41:345 has "all of them, wards and Embers and
  still doors alike". The book names people by their door elsewhere ("both Embers", 41:313), so the prose may stand.
  Recorded only.
- **PD-3.** No `MOVEMENT-006-RECHECK-CONFIRMATION.md` exists, and Movement Six is not accepted (see §0). Every M6 item
  in this report (WB-03, WB-04 at 48:245, WB-05, WB-06, WB-07, WB-12, WB-13, WB-19, WB-20, and edits R17, R19, R21, R22, R28–R30,
  R35, R39–R41, R47–R49) should go to whoever closes the M6 recheck, not be applied around it.

## 9. Owner decisions

- **OD-1 (movement-end refrain).** Is "the town's count went on. Four and four. Fifty-seven to the minute, or faster."
  a deliberate refrain at the end of Movements Three, Four and Five (24:383, 32:589, 40:375)? If yes, apply R01 and R06
  only. If no, also apply R07 and R08, which keep the refrain whole once, at 24.
- **OD-2 (Aske opens nine chapters).** Keep it as the book's clock, or vary two of the run 22–23–24 / 28–29. Varying
  means opening on the scene's first action and moving Aske's reading down a paragraph, which is a structural change
  rather than a line edit, so this report does not draft it.
- **OD-3 (closing images).** Ten chapters end in bed or asleep, and six end with "the disk is cold". Decide whether to
  protect the book's last line by varying one or two earlier disk-cold endings (39 and 40 are the nearest, at 39:315 and
  40:383).
- **OD-4 (the fever echo).** Is the parallel between chs 23 and 40 meant? Even if so, R02–R05 remove only the identical
  sentences and keep the deliberate callback at 40:321.
- **OD-5 (plank).** Either (a) add one clause at the first M6 use widening *plank* to "like doors on one load", or (b)
  rename "the catchers' plank" to "the catchers' line", to match "the first ward line". (b) touches about six lines in
  41–43 and is not drafted here.
- **OD-6 (character tags).** Perrin's "I'd like it known" (about 30), Jude's "I'd want it said", Anwen's "I want it
  said", Dray's "face did what it always did", Orla's "crooked face" (14), Mara's "dry exact" (10). Each belongs to its
  speaker; only the leak and the clusters are edited. Further thinning would change voice and is the owner's call.
- **OD-7 ("Kiva:" titles).** Chapters 12, 30, 36, 39 and 45 open in another person's viewpoint under a "Kiva:" title.
  Each is anchored and each returns to Kiva. Acceptable as a convention, if the owner wants it.
- **OD-8 (weekday-and-clock first sentences, 25 of 48).** Recommended: keep. It is the listener's main way of finding
  where they are in time.
- **OD-9 (the ending).** Book Two resolves its arc (the bank out, the claim relinquished, the name given, the cards) in
  chs 45–48. It ends on an image that opens Book Three (the hull). The owner brief forbids "a bridge novel whose only
  purpose is Book Three"; this book is not one. Whether the last page should lean outward at all is the owner's call.
- **Carried, not mine to settle:** the open items in the recheck confirmations (the 41-minute hold, the brown-ink line,
  "my best machine", Penhale's ward as frost, the basin tide clock). None of them contradicted anything I read at the
  seams.

## 10. Checked and found consistent

- **Countdown arithmetic** across four movements: 44 (Sat 30th, 1st month) → 43 (Sun 1st) → 30 (Sat 14th, 2nd month) →
  16 (Sat 28th) → 14 (Mon 30th) → 13 (Tue 1st, 3rd month) → "Nought" (Mon 14th).
- **Day and date chain at every join**, and the weekday arithmetic for the third month (Tuesday the 1st; Sunday the 6th
  first Sunday; Wednesday the 23rd the spring tide).
- **Aske's warm-morning counts:** "Three mornings" Wed 16th; "Four" Thu 17th; "Five" Fri 18th; "Six" Sat 19th; "Eight"
  Mon 21st; "Ten" Wed 23rd. The sulk sequence (fourth crossing 2 nights; fifth 3; sixth 4).
- **Crossings:** six of six, four at Meridian and two at the gate; the certificate line (22:55); the struck sponsor line
  (46:289–297); "one in fourteen" (47:9).
- **Rhea's card:** six nights, two a month, ending the 30th; "eleven days off" from Saturday the 19th (37:373).
- **Ages and spans:** Pike 54, 26 years at the cloth; Hart's Bench 2660, "twenty-one years ago"; the Proprietor 103,
  hand on the glass since 2611, "seventy years … twenty-five thousand days"; 2,052 strokes (6 × 6 × 57).
- **Mallow Creek times** agree across chs 29, 31, 32 and 34: slack 12:12; stow turns 12:44/45; flood 12:51; "seven
  minutes"; the tape hair at 12:44.
- **The book never had a page torn out** (1:491; 16:393) until 25:163–165 says so explicitly, which sets up 32:569.
  Consistent.
- **Hand-count wording** in the chapters I read (eight that report and two that do not; three and two on the left):
  consistent with the accepted audio repairs. The repaired lines in chs 8, 9, 11, 14, 15, 19 and 24 were treated as
  accepted text.
- **The narration feedback for chs 1–21:** every listed query is resolved in the text except 1:95 (WB-11).
- **Viewpoint anchors** for the 324 section openings (§6).

## 11. Honest limits

- **Same model family.** The author, every movement reviewer, every repairer and every rechecker are the same model.
  This read is fresh-context but not independent.
- **Partial reading.** About two-fifths of the lines were read. Contradictions inside unread middles were found only
  where a search for a number, name, descriptor or exact sentence would surface them. A fact stated once and
  contradicted once in two unread passages would be missed.
- **Book One** was consulted for a single passage (Adlam). Other cross-book facts (for example Pike's or Rhea's
  appearance in Book One) were not checked. In WB-01 and WB-03 the majority of Book Two's own passages, which are also
  the earlier ones, set the canon. If Book One says otherwise, the direction of the fix reverses.
- **Read-aloud judgement** is simulated from text and repetition counts. No audio was rendered or heard, and no human
  listener was consulted.
- **Movement Six** is unaccepted and may still change (§0, PD-3).
- **The edit list is bounded** (50) by instruction. It reduces the worst clusters; it does not bring any family down to a
  target count, and no formula score was chased.
