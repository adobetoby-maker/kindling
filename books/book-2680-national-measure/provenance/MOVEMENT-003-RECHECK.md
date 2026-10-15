# Kindling 2680, Book Two — Movement Three — targeted recheck

> Built by TAC

Date: 2026-10-15. Scope: the repaired findings and changed joins in chapters 17–24 only. This is not a second
editorial pass, not a cold read and not a score.

## 0. Who and how

- **Runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This is
  what the runtime states. I cannot verify it independently from inside the session.
- **Session:** Claude Code background job `a495af2f` (job directory `~/.claude/jobs/a495af2f`); remote session
  `session_01PkUroGhh3ubjA8nxUatRWs`. This is a different session from the drafting job, the review jobs
  (`b4e11087` and the cold read) and the repair job (`8e3ee375`).
- **This is a same-family, fresh-context check. It is not human review and not independent testing.** It shares
  the drafting, review and repair sessions' model family and their blind spots. No subagent, other model or
  codex/OpenAI call was used.
- **Brief:** delivered in-session. Its text matches `planning/OPUS-5.5-MOVEMENT-003-RECHECK.prompt.md` (62 lines),
  SHA-256 `d7e8eb4e60e2dabf086ca64e254a6e1fe221389fbfd2d0c9a2d5a09bfc1ec2c3`.
- **Read:** `MOVEMENT-003-REPAIR.md`, `MOVEMENT-003-EDITORIAL-REVIEW.md` and `MOVEMENT-003-COLD-READ.md` in full.
  Every hunk of `git diff --no-index --word-diff` between each frozen chapter and its working chapter. The
  working text around every hunk and every removed break. The cited lines of `STATE_LEDGER.md` (Movement Three
  block), `MOVEMENT-003-CONTINUITY.md`, `BOOK_MAP.md` §12 and the `AUTHORSHIP.md` repair entry. Chapter 13,
  lines 341, 357 and 501 only (C20).
- **Files written:** this report only. No prose, record, authorship entry or commit was touched.

## 1. Frozen edition and integrity

- `cd books/book-2680-national-measure/editions/movement-003-first-draft && shasum -a 256 -c SHA256SUMS.txt`:
  **chapter-17.md to chapter-24.md: OK (8 of 8).**
- Working chapter hashes match repair report §7 exactly (`1aaa7d0c…`, `4a4aba68…`, `0f20ea26…`, `e5e81ac2…`,
  `a3684d2b…`, `9d66769d…`, `8d50b38a…`, `12b01c9f…`).
- `git diff --stat HEAD` on `manuscript/` touches chapters 17–24 only. Chapters 1–16 are unchanged.
- `wc -w`: 7,158 / 8,132 / 7,611 / 7,091 / 6,562 / 5,784 / 6,511 / 5,761 = **54,610**, as reported.

## 2. Priority 1 — factual corrections: **PASS**

Each fix was read in the frozen line, the working line and the scene around it. Working line numbers follow.

| # | Working location | Checked | Result |
|---|---|---|---|
| F1 | ch. 19:259, 269, 279 | Carry 1: "three to Seven and a down" (Jude on their blade as he "shut and ran for the hazel"; this follows the lane-1 lesson). 4–0. Carry 2: Perrin down (+1) and their litter over (+3): "Four all." Carry 3: a point and a down: "Six to Seven. Four to the Ropewalk." Board, ch. 24: lanes 2–7, 6–4, 4–5 give **12 for, 16 against**. Yeo's "in the third carry" (19:303) still fits. | PASS |
| F2 | ch. 18:91, 221, 239, 259 | Carry 1: Carrow carries "with nothing open at all", which is legal. Carry 3: Kiva is "at the hurdle with her door open on it, holding it planted"; "Seven's catcher kept her hands off the poles while her door was open; if she shut it to lift, the hurdle would stand unplanted… That was the rule, and Seven had chosen it." Carrow: "Not while your door's on the hurdle, and it's the only one you're let open." This is one rule, Seven's own, and it fits both carries. No Board rule is implied. Lane 1 still totals 2–7 ("Seven to two"). | PASS |
| F3 | ch. 18:459, 507, 517 | Thursday 6 p.m. cutaway: "Yesterday" ×2 and "yesterday in the lane" (lane 1 was Wednesday). Lyle now asks about what she saw on the page, the lean ("Somebody taught you to lean from the floor. Did they teach you to walk a wall as well?"). The far-end walk is first shown in this scene, then in lane 2 (ch. 19:277). No "this morning" remains. | PASS |
| F4 | ch. 23:3; ch. 24:177 | Friday: "three nights to go"; Sunday: "One night to go"; Monday: "A sulk of four nights" (ch. 24:353). | PASS |
| F5 | ch. 20:351 | "a catcher who watched her heel, and since the first month a second who watched the far edge". This agrees with Pike's "twenty years before there was ever a second". | PASS |
| F6 | ch. 20:389 | "*Tinned: seven bags… The seventh bag light.*" The page shows three purses shut at midnight ("Three purses shut", 20:201) and four reset at dawn (20:323). Posts 5, 6 and 7 were cut, then the fourth, light (20:341–373). The records say seven everywhere (§5 below). | PASS |
| F7 | ch. 21:177, 223–225 | Quiet at "Twelve past six"; down "At six thirty-three"; "stood for twenty-one minutes" (6.12 + 21 = 6.33). Mara's "twenty-one minutes of slack" (21:297) agrees. Wednesday: 6.13 to 6.33, "twenty minutes" (21:323, 357). No start time moved. | PASS |
| F8 | ch. 20:315, 337 | Rhea "at ten past six", then "Low water slack: a quarter past six". | PASS |
| F9 | ch. 22:51, 71, 91, 165, 193–205, 209 | Order on the page: 7.00 crossing, 7.15 signing (Orla: "Your healer wants that hand at noon"), Adlam "at half past eleven, as he had promised", the wire ("It came at eleven"), noon in the loft, 4 p.m. and 10 p.m. in summary, then Kellan at seven. The day now reads forward. The bedside "cold to a hand below the elbow" (22:335) agrees with the 10 p.m. reading. The hand-check block is word for word the same except its opening clause and "wrote both down without a word". | PASS |
| F10 | ch. 24:179, 369–373 | Sunday: "If my ribs go on the Bench tomorrow". Monday: "You're not at the Bench. It's on your card… watch us do it, and Halden, and Old Four, and Twenty-Eight." Both lines say Seven stands without Kiva. | PASS |
| F11 | ch. 21:207–215, 345 | On Tuesday Mara said "It's the bank's" and "How"; Hart said "as if the count goes out of the harbour". Hart on Wednesday: "Your aunt asked me *how* yesterday… I told her what it looks like. It was the first time in six months I'd said it aloud… You've said it without being told. And you've said more than I did." This now agrees with the page. Kiva's "Taking it in. Holding it." (21:341) is the "more". | PASS |
| F12 | ch. 24:195 | "plant on the gate's boards on Tuesday" (reading at the gate mast, ch. 21:85). | PASS |
| F13 | ch. 24:39 | "eleven days ago" (Tue 1st → Sat 12th). | PASS |
| F14 | ch. 19:97 | "Then I meant to write to you at the house of the Even Hand. Then you had a fever on the ferry, and I heard of it at the kitchen table with my bag not yet packed". There is no day count and nothing contradicts her Wed 2nd arrival. | PASS |
| F15 | ch. 17:167 | "My mother wired it on." | PASS |
| F16 | ch. 21:161 | "Maud told me." | PASS |
| F17 | ch. 19:245 | "Your sponsor's in town?" he said. | PASS |
| F18 | ch. 22:35 | "The old man had his own dividers out, a small brass pair, and he had measured before Noa had." | PASS |
| F19 | ch. 21:297 | "the eleven minutes without pumps that the low town would bear on a making tide". | PASS |
| F20 | ch. 20:395 | "Held in part on walls lying flat on the water." | PASS |

**Invariants.**
- **Ash.** No diff hunk touches an ash figure. On the page: 4.70 (ch. 23:287, "four and seventy hundredths"),
  4.28 and 4.16 (ch. 24:203, 271). The review's chain 6.23 − 0.43 − 0.31 − 0.40 − 0.09 − 0.30 = 4.70; − 0.42 =
  4.28; − 0.12 = 4.16 still holds.
- **Crossings.** The fifth is Thu 3rd and the sixth Thu 10th. Their readings and nights are unchanged except F4
  and F9's order.
- **Countdown.** "Fourteen" on the 30th, "Thirteen" (ch. 17:499) and "Nought" (ch. 24:365) are unchanged.
- **Nothing else moved.** No date, event, injury, power limit, knowledge boundary or outcome moved. The only
  power-related text added is F2's statement of Seven's chosen rule, which adds no new capability or limit.
- **C20.** Ch. 13:341 ("There's a lodger," said Coombe. "Kill it."), 13:357 (Jude's kill "through the grey cord
  lying on" the coping) and 13:501 (logged "a lodger" in the license book). Seven knows a lodger can be killed
  and how, so ch. 18:523 agrees.

**Note, not a defect.** F2 introduces holding the hurdle planted, which the marshal's stated rules (ch. 18:39)
do not mention. It contradicts nothing and is offered as Seven's own choice. A first-time reader may simply not
know why an unplanted hurdle matters.

## 3. Priority 2 — scene structure and sentence work: **FAIL (one join)**

**Breaks.** Internal `---` lines: 79 → 59 (ch. 17–24: 9, 7, 10, 6, 7, 5, 6, 9). No stray dash fragments and no
double blank lines are left at any join. The three breaks kept on purpose are present: ch. 18 after "Carrow had
to run." (18:121–123), ch. 23 after the disk goes back "cold" (23:243–245), and ch. 24 before "She had never
watched Seven from above". Every cutaway is still fenced by a break and opens on its lens by name:
- "Anwen Pryce went back…" (18:441)
- "Orla Dane read the book…" (19:353)
- "Rhea Sorn stood…" (20:315)
- "Mara Rowan stood on the outfall gallery…" (21:169)
- "Kellan Renn had never…" (22:209)
- Kiva's bedside section after it (22:313)

No removed break sat before or after a cutaway. Joins 13 and 14 fall inside Kellan's cutaway.

**The twenty joins.** No prose was cut at any join. The one added transition ("It was the third carry, and",
18:201) reads cleanly. The lane-1 joins (18:59–61, 97–99, 163–165, 199–201, 245–247) read as one continuous
contest. So do the slack joins (20:137–139, 189–191), the gate reading (21:51–55, 83–85), Adlam (22:131–133),
the dinner (22:243–245), the lane-3 join (24:91–93) and the van yard (24:237–239; the yard opens "at ten", so
"at ten past ten" stays inside the scene). Three folded bridges change time or place inside a section, but each
announces it in its first words:
- "On Sunday at seven, in the loft" (19:341)
- "Aske had the hand at noon, when they came back up the loft stair" (22:193)
- "Kellan walked back along the Long Quay at half past nine" (22:293)

None is hidden. The noon check now lands as a quiet close before the Kellan break (repair §8, question 3).

**The defect — ch. 23, joins 16 (§4 | §5).** See §6, D1. With the break gone, a pronoun meant for the Proprietor
now points at Perrin.

**Long sentences.** All eight have one main clause, clear subordination and no *and…and* chain, and all parse:
- ch. 17:61 (Mole, 49 words)
- ch. 17:189 (Graving, 55)
- ch. 18:7 (Ropewalk, 43)
- ch. 19:71 (pump-house hall, 46)
- ch. 20:9 (kiddle, 45)
- ch. 21:201 (Hoop, 53)
- ch. 23:139 (stair lamps, 43)
- ch. 24:35 (Graving full, 46)

Each read aloud with a natural breath at its commas. None sits inside a fight. The longest sentence in the
movement is 55 words.

**Joined declaratives.** These are grammatical and keep their meaning:
- ch. 22:75–79 (the certified crossing)
- ch. 23:265–267 (the window)
- ch. 24:321–325 (the yes/no book)
- ch. 21:383

"She found that she was glad of it in a way that she had never been glad of the three" (22:81) and "She kept
her mouth shut." (23:269) are intact.

**Footholds.**
- **Ch. 17 rule history.** The three beats sit at 17:333 (before the clerk), 17:345 (after Orla names the two)
  and 17:359 (after "Hush.", before Carrow walks). Nothing from the original paragraph is lost: "for her" became
  "for Kiva"; "the condition" became "Kiva's condition". Dray's "That's fairer" and the irony are untouched.
- **"Hand door."** The gloss at 18:343 sits between Perrin's call and "Kiva went to the first cross". The gloss
  at 24:85 sits between Aske's line and "She sat with it". Both are clear, and the second keeps Pru's door apart
  from Kiva's cold hand.
- **"Hold."** At 22:263, "On the Hold rig she reads Edge three-one…" marks a measurement, not Anwen's role.

## 4. Priority 3 — voices and tics: **PASS**

My recounts over chapters 17–24 match repair §4a exactly:

| Phrase | Count | Note |
|---|---:|---|
| "I'd want" | 14 | Jude 12 (including "I'd wanted"), Anwen 18:493, Aske 18:331 |
| "want it said" | 11 | |
| "I'd like it known" | 7 | |
| "said nothing" | 10 | |
| "did not say anything" | 5 | |
| "scarlet" | 7 | |
| blush "red" | 3 | |
| "in two stages" | 2 | |
| "so that it's said" | 2 | |
| "nearly smiled" | 3 | |
| "soonest" | 6 | |

All four remaining ", since" uses are temporal (17:171, 17:481, 19:185, 19:223).

**Recast lines.** Each was read in place, and each keeps its meaning and its speaker's register:
- Perrin: "I'd pay money to know…" (17:193); "I'm saying it out loud." (18:293)
- Kiva: "Please write that beside whatever the comb says." (17:243)
- Pike: "The first wants them all the way to the palm, and the second wants the thumb hard." (19:25)
- Yeo: "I mean to know before the sea does." (19:331)
- Peverell: "Enter that in your book…" (21:283)
- Hart: "That goes in my book." (21:345); "I've said so now. To somebody." (24:341)
- Kellan, as a sum: "That's one side. The other side is…" (22:329); "Add that in." (22:347)
- Mara: "that goes in too." (23:39)
- Orla: "Mark that, in this house." (23:329); "You'll hear it from me…" (24:289); "I've never signed anything I
  was gladder to." (24:301)
- Pru: "You should know that." (24:135)

**Blushes and tells.**
- Perrin: jaw at the hinge (18:153, 21:57; 21:57 refers back to the Ropewalk correctly); neck (19:287, 24:191);
  hands (23:115); throat (23:193); rope (24:373)
- the Tarn girl: "Her chin had begun to shake" (17:293)
- the Ropewalk child: "his face screwed up tight" (18:469)
- Yarrow: "put his fork down" (22:285)

Pru's scarlet is untouched.

**"In two stages."** "got up off it" (19:387), "got up off the crate" (22:71), "got up, stick first, and stood
leaning on it" (23:125).

**Cut "said nothing" lines.** No dangling gesture or unattributed line was left at 17:173, 17:287, 17:297,
18:99, 18:337, 18:339, 18:489, 19:283, 19:345, 20:289, 21:5, 21:49, 21:221, 22:213, 22:293, 22:313, 23:91,
23:353 or 23:375.

**Negation recasts** (21:383, 23:265, 23:405). They keep their meaning. "She had not told anybody. She had not
told Mara. / She did not tell Mara now." (21:377–379) is kept, as the repair says.

**Protected lines.** Perrin's "I'd like it known" (7), Aske's "soonest", Pike's "nearly smiled" (3), Hart's
turned watch and the Proprietor's courtesy survive.

**Dialogue length.** The dialogue-only figures move from 4 / 60.1% / 0.0% to 4 / 60.3% / 0.0%. No dialogue was
lengthened or split for rhythm. The changed spoken lines are the recasts above plus F3, F11, F14, F16 and F17.

## 5. Metrics spot check and records

`python3 -I provenance/tools/m3_metrics.py manuscript`. The script is unchanged (SHA-256 `12036c794861…`). Its
output matches repair §3b on every row I compared:

| Measure | Value |
|---|---|
| Body words | 54,499 |
| Sentences | 5,678 |
| Mean / median / SD | 9.6 / 7 / 8.05 |
| ≤5 / ≥40 | 40.3% / 0.5% |
| Longest | 55 |
| Narration median / ≤5 / ≥40 | 7 / 37.1% / 0.8% |
| Sections / mean | 67 / 813 |
| Internal breaks per 10k | 10.83 |
| Flesch / FK | 96.0 / 2.2 |
| "she did not" per 10k | 14.5 |
| Reserved terms ("Unroofed", "Breach") and month names | 0 / 0 / none |

Its viewpoint line (Kiva 94.7%) is the known section-map artefact that repair §3c describes. I did not recount
viewpoint.

**Records.** Each was checked against the surviving prose:
- `MOVEMENT-003-CONTINUITY.md` (the *(repair)* entries and §14–§16)
- the `STATE_LEDGER.md` Movement Three block (status line, M3.1–M3.8 *(repair)* lines, the new M3.9)
- the dated `BOOK_MAP.md` §12 note (C17)
- the `AUTHORSHIP.md` repair entry

They all agree with the page:
- lane 2 by carry, 4–0 / 4–4 / 6–4
- Seven's catcher rule
- seven bags, the seventh light
- 6.12–6.33 and 6.13–6.33
- "three nights to go"
- Thursday's order
- Seven stands at the Bench
- the gate's boards and eleven days
- "Nothing came", with Aske writing a card line Kiva did not see (ch. 23:395)

Each says **"Not rechecked; not accepted"** or equivalent. None claims a recheck, acceptance, publication or
commit.

No record is stale. One note could be read wrongly:
- **`MOVEMENT-003-CONTINUITY.md` ~line 193:** "Stood 6.12–6.33 (8th, 21 minutes) *(repair; was 6.14–6.35)*".
  "Was 6.14" quotes the old continuity record, which had the start wrong. The prose always said "Twelve past six".
  Read alone, the note suggests the repair moved the start, which contradicts the same file's "The repair moved
  only Tuesday's *end*". This is a clarity point for whoever next touches the file, not a defect.
- **Repair report §2a** says "Each join keeps the place, the time (within minutes) and the lens." That is not
  quite true of joins 6, 11 and 14 (§3 above), which change time or place but announce it in their first words.
  The report is a historical record and this recheck does not ask for it to be edited.

## 6. Defects

**D1 — unclear referent introduced by a removed break (join 16, ch. 23 §4 | §5).**

- **Location:** `manuscript/chapter-23.md` lines 193 and 195.
  > 193: "Perrin cleared his throat and took the rope off his shoulder."
  > 195: "He was not what she had expected."
- **Problem:** In the first draft a `---` sat between these two lines, and the new section began with "He",
  meaning the Proprietor. The repair removed the break and changed line 193's subject action from "went very
  red" to "cleared his throat". "He" now directly follows a sentence about Perrin, so on one pass, and above all
  aloud, it reads as Perrin. The referent only resolves four sentences later ("He was a man of about fifty-five
  by his face… His left lay on the glass case"). This is the unclear-referent case the brief names.
- **Bounded fix:** one word at line 195. Change "He was not what she had expected." to
  **"The Proprietor was not what she had expected."** Nothing else in the passage needs to change. The next
  "He was a man of about fifty-five" then reads correctly.

No other surviving or newly introduced defect was found in the repaired findings or the changed joins.

## 7. Decision

**One concrete defect requiring a second repair:**

- **D1:** `manuscript/chapter-23.md:195`, "He was not what she had expected." → "The Proprietor was not what
  she had expected."

Priority 1: **PASS**. Priority 2: **FAIL** on D1 only. Priority 3: **PASS**. Frozen edition: **8 of 8 OK**.

Once D1 is applied and confirmed by a diff limited to that line, nothing else from this recheck stands between
Movement Three and acceptance as context for Movement Four. This report does not apply the fix, accept the
movement, update authorship, commit, push, publish, narrate, or draft Movement Four.
