# Kindling 2680, Book Two — Movement Four — editorial and numerical review

> Built by TAC

Date: 2026-10-15. Reviewer: **Claude Opus 5.5 (`claude-opus-5-5`)**, Claude Code background session
(job `28d8a21c`).

## 0. What kind of review this is

- **Same model, fresh context, informed. Not blind.** The movement's drafting author is recorded as Claude
  Opus 5.5 (`AUTHORSHIP.md`, Movement Four entry, job `9f1bbf7e`). This session did not have that drafting
  transcript. It did have the plan (`BOOK_MAP.md`), the bible, the cast file, the packet, the state ledger
  (including the author's own Movement Four block), the author's continuity file and the formula. This is
  **not** a cold read, a human read or independent testing. The two reader lenses below are simulated
  perspectives, not reader research. A same-family reviewer shares the drafter's blind spots.
- **Other review artefacts.** A file `provenance/MOVEMENT-004-COLD-READ.md` appeared in the working tree during
  this session, written by a parallel job. It was **not read**, and nothing here depends on it. The other Movement
  Four provenance files are `MOVEMENT-004-CHECKPOINT.md` (superseded) and `MOVEMENT-004-CONTINUITY.md`.
- **Coverage.** All eight supplied files were read in chapter order, in full: `manuscript/chapter-25.md` to
  `chapter-32.md`. That is 52,401 words by `wc -w` and 52,311 body words by the script tokenizer (headings and
  `---` lines excluded). Every file is byte-identical to `editions/movement-004-first-draft/`
  (`shasum -a 256 -c SHA256SUMS.txt`: all OK; `cmp`: all same), and its SHA-256 matches the `AUTHORSHIP.md`
  table. The movement is complete as planned: chapters 25–32 of 48. No later chapter exists.
- **Canon evidence used.** `STATE_LEDGER.md` (sections 1–11 and the Movement One to Four blocks), `BOOK_MAP.md`,
  `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `packets/MOVEMENT-004.md`, `provenance/MOVEMENT-004-CONTINUITY.md`, the
  Movement Three review, repair and recheck, plus targeted greps of chapters 13, 17, 23 and 24 (the Pit lodger,
  the Tarn jar, the Proprietor's Friday, the Sunday rehearsal). The Book One manuscript was not read.
  - **Verified:** a contradiction inside chapters 25–32, or between them and a chapter I grepped.
  - **Apparent:** a conflict with Book One or an earlier movement that this evidence cannot settle.
  - **Plan:** a departure from the plan or packet, not a canon error.
- **Formula source.** `/Users/drive/penname/research/ironprince-craft-formula.md` is present. Its SHA-256 is
  `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`, matching the recorded hash. Sections 2–6
  and 8–9 were used as given, including the ~1.7× and ~950 values.
- **No manuscript prose was changed.** No repair, no later chapter, no commit, no push. The only files this
  session wrote are this report and `provenance/tools/m4_metrics.py`.

---

## 1. Unscored reader response

**Where interest caught.** On the first line: "The Salt Hall had been built to keep salt dry, and it still
smelled of it." Then the load board, "every needle was moving", and Orla's "Don't give them yours." The Bench is
a clever board, because it puts the harbour's problem on a floor ("She's put the harbour on the floor"), and it
pays off when Kiva sees the one trough of water that nobody on the floor can see. The torn page, dropped twenty
feet and caught "as if it had been a rung", is the movement's first great small moment.

The movement then peaks three times:

- **The climb (ch. 27 §0).** *Set*, rung by rung. The rib goes at the eleventh rung. Kiva does not say the word
  until the heel settles. This is the best sustained action in the book so far.
- **The far edge (ch. 30 §2).** Pru calls it once, and the fold lies down where Kiva had been.
- **The pass, and the death (ch. 30 §3 to ch. 31 §0).** It is stunning and earned. "The fold had two ends." Then
  "Let it come to you": Pru's tray as "the nearest thing". The pass holds. Penhale is already dead, with his hand
  round the girl's wrist and the count stopped at three.

The death is carried by the people who loved the man, not by the narrator: Yeo's "I said it was ground", Pike's
"He had nobody at his far edge", Coombe's still hands on the counter, Ivey's "He laughed so hard a curlew got up".

**Where it slipped.**

- **The Bench rules speech** (ch. 25 §1, the Clerk) and the needle-reading passages ask a lot of a first pass.
  The heat-one demonstration rescues it.
- **The Carry waiting** (ch. 26 §4). Kiva's three timings of the water (1:40, 1:20, "a minute's start") do not
  agree, and the reader stops to sort them out.
- **The aftermath chapter** (ch. 32): 9,389 words and twelve sections. After Mallow it becomes a survey: tent,
  cart, comb, mast, Ropewalk, board, Dray, the *Mercury*, printer, pump house, chandlery, bed. Each piece is good.
  Together they slacken the drive the death created, especially in the board / Dray / *Mercury* run (§5–7).
- **Board arithmetic** (§3a below). A counting reader cannot make the Bench's stepped places agree with the heat
  times on the page. This book trains its readers to check.

**Who matters.** Kiva first. She is more of a caller and less of a doer than ever, and this is the book's argument
made physical. **Perrin** comes next. The ladder, then the honest line on envy: "It's not better… It's just the
other side of the same thing." Then **Pru** ("I could carry that"; "*No*", said to an officer). **Penhale**
matters more in death than any minor character in the book. **Bridie** is a fine new person, and her question
about the gap is the movement's best teaching line. **Trewin** gets the movement's warmest laugh. **Yeo** carries
the cost.

**What I expect next.** The Lane, from Thursday. Seven is one mark off the roll. Dray is waiting with her needle.
Carrow is on one door. Kiva's seventh crossing is due, and Aske will say the price twice. The Proprietor's letter
to Crest will come back to Kiva in the Chair's hand. Coombe's page will be in every pocket by six. Halden's claim
on "nine-tenths of the Hunt" is on paper. Mara's thirty-six hands will be taught for the 23rd.

**Would I continue?** Yes, eagerly. This is the strongest movement of Book Two.

---

## 2. Scored dimensions — two lenses

These are lenses, not research. Scores are editorial judgments. They are not averaged and they are not a
release gate. Confidence is how sure I am of the score: H high, M medium, L low.

### 2a. A fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Conf. |
|---|---:|---|---|---|
| Opening pull | 8 | ch. 25 §0 | The smell, the moving needles, Orla's "They always want a name". Then the Clerk's rule paragraph (25:23–29) is a block of abstraction before any person acts. | M |
| Keep reading | 9 | ch. 27 §0 (11th rung); end of ch. 30 ("Bridie was standing on it") | Each chapter ends on an open problem with a local payoff. The movement dips in ch. 32 §5–7. | H |
| Interest / freshness | 8 | ch. 25 §3 (draining the jacket); ch. 26 §0 (planting a rung) | Problems a child can state: "there's water under them"; "a rung's iron, it's in granite". | H |
| Clarity / flow | 6 | 26:273; 27:377; 30:317; the Bench's stepped ranking | The water timing, Carrow's unlaying and why the Tarn's sleeve does not fold each need a second read. The boards rank stepped fours by a rule nobody says. | M |
| Character attachment | 9 | ch. 27 §4 (Perrin, envy); ch. 31 §0 (Penhale, Bridie) | Agency and vulnerability in almost every named person; Pru's "Don't say *well called*". | H |
| Humor / warmth | 8 | ch. 26 §1 (Yarrow's boots); ch. 28 §4 (Trewin's laugh); ch. 29 §3 (Penhale's mother) | Grounded in character and well placed before the dark turn. | M |
| Action / suspense | 9 | ch. 27 §0; ch. 30 §0; ch. 31 §0 | The contest is trackable. Both sides adapt (the Tarn and Halden copy the far-edge weight). The cost is visible. | H |
| Progression payoff | 8 | ch. 29 §5 (wall on water); ch. 30 §2 (far edge); ch. 31 §0 (the pass) | Effort from Movements Two and Three changes what happens. Standings move 12th → 3rd → 9th. | H |
| Connection | 9 | Penhale's fathoms (M3 → ch. 31); the Tarn jar (ch. 17 → ch. 28); Trewin's Sunday (ch. 24 → ch. 31) | Plants pay off cleanly, and the movement plants the Lane. | H |
| Read-aloud quality | 7 | "slowly" ×43; "nobody" ×114 as both word and call; 27:241 | Clean attribution. A few referent and logic slips (§3). | M |

### 2b. An adult genre reader

| Dimension | Score | Location | Reason | Conf. |
|---|---:|---|---|---|
| Opening pull | 8 | ch. 25 §0–1 | A national event, press, crowd, and a board that is the series' central problem in miniature. | M |
| Keep reading | 8 | strong ch. 25–31; ch. 32 §5–7 | The aftermath survey disperses the tension the death built. | M |
| Interest / freshness | 9 | the stow as a sleeve; "The book's for a sheet"; *set* | Coast craft and the book's own method collide in specific, plausible ways. | H |
| Clarity / flow | 7 | §3 items C1, C2, C11–C13 | Mostly clear on one pass. The board ranking, the water direction and the Tarn's fold logic catch a careful reader. | M |
| Character attachment | 9 | Yeo, ch. 31 §2 and §4 | Adults with responsibility and a fair, unlike reading of events. Nobody is a villain. | H |
| Humor / warmth | 7 | Penhale throughout ch. 29 | Warmth is strong. Humor thins after ch. 29, which suits the movement. | M |
| Action / suspense | 9 | ch. 27 §0; ch. 30 §0 | Geometry is stated. Every choice has a price paid on the page. The fight is not padded. | H |
| Progression payoff | 8 | the pass; Pru's call; Ivey's request | Capability travels to people who are not Kiva. That is the plan's argument, shown. | H |
| Connection | 9 | the harbour clock (ch. 26 §2); the 12.44 hair (ch. 32 §3) | Evidence accumulates fairly, and no meaning is forced. | H |
| Read-aloud quality | 8 | the long sentences in ch. 27 §0 | The restored long sentences read well aloud. A few slips. | M |

---

## 3. Canon, physical state, power limits, knowledge and reserved disclosures

### 3a. Arithmetic: every board, tally, standing, weight and clock

**Ash book (Jude).** Every line checks to the hundredth.

| Board | Spend on the page | Sum | Held |
|---|---|---:|---:|
| Carried, Mon 14th | — | — | 4.16 |
| Bench (25 §4) | Pryce 0.16 + Finch 0.09 + Cade 0.06 | 0.31 ✓ | 3.85 ✓ |
| Carry (27 §3) | Cade 0.22 + Pryce 0.09 + Talley 0.04 | 0.35 ✓ | 3.50 ✓ |
| Hunt doors (32 §2) | Pryce 0.17 + Talley 0.10 + Finch 0.12 | 0.39 ✓ | 3.11 |
| Hunt quarter | 12.6 clean: Board 6.30, Company 3.15, four 3.15 | +3.15 ✓ | **6.26** ✓ |

- **Combing.** 9.1 + 38.0 + 12.6 = 59.7 ✓. Red: 9.1 + 38.0 = 47.1 ✓.
- **"The most we've had since the hills".** Plausible: every held figure in Movement Three is lower.
- **Kellan's "nine-tenths".** If one dry bag in four combs clean and no wet bag does, 90% red implies about 40% of
  bags dry. That is an estimate, and it is presented as one ✓.
- **Kellan's "Nineteen… out of twenty-four".** That is 79%, so "near enough four in five" ✓. Five held plus
  nineteen stepped makes 24 ✓.

**Place marks (24 down to 1) against every on-page sheet.** The bracketed places are the author's off-page
reconciliation in `MOVEMENT-004-CONTINUITY.md` §3.

| Four | Bench | Carry | After two | Hunt | After three |
|---|---|---|---:|---|---:|
| Halden License | 1 (24) | 3 (22) | 46 ✓ | 6 (19) | 65 ✓ |
| Ropewalk first | 3 (22) | 2 (23) | 45 ✓ | 12 (13) | 58 ✓ |
| Team Seven | 6 (19) | 1 (24) | 43 ✓ | 15 (10) | 53 ✓ |
| Old Four | 4 (21) | 5 (20) | 41 ✓ | 2 (23) | 64 ✓ |
| Holloway first | 2 (23) | [7] (18) | 41 ✓ | [7] (18) | 59 ✓ |
| Tarn first | [8] (17) | 4 (21) | 38 ✓ | 24 (1) | 39 |
| Team Twenty-Eight | [11] (14) | 6 (19) | 33 | 1 (24) | 57 ✓ |
| Westerley first | 5 (20) | [9] (16) | 36 | [5] (20) | 56 ✓ |
| Westerley second | [7] (18) | [10] (15) | 33 | 3 (22) | 55 ✓ |
| Holloway second | [9] (16) | [8] (17) | 33 | [4] (21) | 54 ✓ |
| Ropewalk second | [10] (15) | [11] (14) | 29 | [8] (17) | 46 ✓ |

- Every printed total adds up.
- Any four not in this table can score at most 13 + 13 + 16 = 42, which is below 46. So the printed top ten is
  complete, given the reconciliation.
- Perrin's "one mark off eighth" (53 against 54) ✓.

**But the Bench reconciliation conflicts with the page (C1 below).**

**The Carry's clocks and order.**

- Reverse seeding: run *n* is seed 25 − *n*. Run 10 is the Ropewalk second four (seed 15) ✓. Run 12 is the Tarn
  second four (seed 13) ✓. Run 13 is Seven (seed 12) ✓. Run 16 is Twenty-Eight (seed 9) ✓. Run 23 is Halden
  (seed 2, "second to last") ✓. Run 24 is the Ropewalk first four (seed 1) ✓.
- "Eleven fours still to run": 24 − 13 ✓. "Twenty-three fours before them" ✓.
- Old Four (seed 6) runs 19th and the Tarn first four (seed 3) runs 22nd. The unnarrated runs in between do not
  contradict that ✓.
- The Ropewalk: 2:59 + 10 for the face = 3:09 ✓. "Twenty… six seconds faster than Seven" (0:20 against 0:26) ✓.
- Seven's 3:08 decomposes plausibly:
  - 0:26 to out
  - the sling and "Up" by about 1:00, when the shutters go full ✓
  - about 30 s for ten rungs at "three a rung"
  - a three-count stop
  - about 54 s for twelve rungs at four to five a rung
  - the lip and the last twenty paces
- The Purser is 85 kg throughout ✓. Perrin's earlier figure, "three hundred and eighty kilos for thirty counts",
  matches the ledger ✓.
- Chamber geometry checks: 60 paces long, start 40 paces from the casualty, stair 50 paces back, ladder 10 paces
  from the casualty ✓.

**The Hunt's clocks.**

- Slack from 12:12 (fingers) to 12:51 (the flood) = 39 minutes, against Yeo's "forty minutes or near enough" ✓.
- Kiva at 12:29: "holding for seventeen minutes… twenty minutes more" = 37 ✓.
- Near post 12:14, far post 12:24, stow dead 12:29, upper tear shut 12:40, the Tarn's near post 12:35 ✓.
- The turn at 12:44 and the water at 12:51 = seven minutes ✓. This matches Noa's hair at 12:44 ✓.
- The lower tear "near one in the morning": 12:21 + 12 h 25 m ≈ 00:46 ✓.

**The harbour clock (a strength).** Hart's gate-table series runs 5.49, 6.38, 7.27 and 8.15 on the 8th–11th
(about 49 minutes a day).

- Carried forward, it gives a morning low of about 10:42 on the 14th.
- The next low is about 23:07, against Hart's "ten past eleven" ✓.
- Wednesday's low is about 12:20, against Yeo's "twenty-one minutes past twelve" ✓.
- Mara's watch at the neap reads 11:34, against the predicted "thirty-four or five" ✓.

This is consistent across two chapters and two narrators. The old C12 problem is now on the page as an unexplained
observation ("held"), not as a slip.

One small physical note (Apparent): on an Earth-like tide, neaps fall about seven days after springs centred near
the 9th–10th, so about the 16th–17th. Wednesday's "It's the neap" fits. Monday's "It was the neap" (26:141) is
about three days early. Accept, or write "near the neap".

### 3b. Findings

Severity: **H** high, **M** medium, **L** low.

| # | Sev. | Kind | Location | Finding |
|---|---|---|---|---|
| C1 | **H** | Verified (page vs records; affects the exit) | 25:151; 25:283; continuity §3 | **The Bench's stepped places do not follow from the heat times.** Seven is 6th, with a 4:10 find ("the slowest in the heat by a minute") and a step at 8:40. The only rule that puts it above every other stepped four is ranking by length of hold. Holloway second, which found faster, stepped at 5:00. But under that rule, the page's own times put three unnamed fours above Westerley second (5:20) and Holloway second (5:00): heat one's "stepped at eight minutes, and another at six" and heat three's "At six, one of the three Kiva did not know". The reconciliation that the printed after-three sheet depends on cannot then hold (Westerley second 7th, the Tarn 8th, Holloway second 9th). Re-ranked by hold, Westerley second and Holloway second each fall to about 52, and **Seven at 53 would stand seventh, on the roll.** That contradicts the movement's planned exit ("ninth, a place off the roll"). The Tarn's step time in heat three is also never given. |
| C2 | M | Verified (plant) | 25:169 vs 25 §1 | **The rail minute.** Kiva says, "There's a minute at the rail, between the quench and the tune. The Clerk read it out this morning." The Clerk's quoted rules (25:23–29) do not include it, and heat one goes from quench straight to tune. The device that carries the Bench's best moment arrives unplanted, which an adult reader will call convenient. |
| C3 | M | Verified (physical) | 27:217 vs 27:89 | **The water's direction.** At the ladder, the water is "pushing at the backs of their legs as it went down the chamber toward the tail". Walking to the tail afterward, it is "running against them now… like walking up a river". Both cannot be true: water entering at the head and walking toward the tail means the flow is with them. |
| C4 | M | Verified (position / referent) | 27:241 | **Aske's position.** "I felt it go from the bottom of the ladder; everybody did." Aske was on the quay, and the rib went at the eleventh rung. Trewin's "I heard it. From the stair" (ch. 28) shows the intended sense: heard, from where they stood. |
| C5 | L | Verified | 25:233 vs 32:513 | Pru reads "with her lips moving, the way Orla read the book". Ivey reads "the way Orla read, with her lips shut". |
| C6 | L | Verified | 30:183 vs 32:129 | Narration: Kiva "would not hear it until three o'clock, at the gate". Kiva to Kellan: "I heard. On the causeway. Lyle." Also, combing begins at four. |
| C7 | L | Verified (clock) | 31:371 | Yeo: Pru "called it at twenty past twelve… Forty minutes later I'd a man under a fold". On her own slate the near post was cut at 12:14, the call came at once, and Penhale went under at about 12:45, so about thirty minutes. |
| C8 | L | Verified (geometry) | 30:61 vs 30:3 | Kellan is "forty paces off". Halden's stow is "forty paces above the kiddle" and Lyle is "twenty paces below it", so the distance is about sixty. |
| C9 | L | Verified (ledger) | 26:39 | Perrin's rehearsal climb ("came up with my door open", twenty-two plants) is not on the book. At the Carry rate (0.22 for 22 rungs), it is about 0.2 dram. Either put it on the book or say it was off his own thimble. The ledger "reconciles to the hundredth" (bible §9). |
| C10 | L | Verified (rule) | 29:49 vs 29:301–331 | The Clerk: "A four does not go onto the mud below a form on running water." Kiva and Pru go down to set purses "a yard downstream" of the tear and under the posts at 11:30, while "the thread… ran seaward". Yeo ordered it and Penhale led, but the rule as read has no officer exception. One phrase fixes it (for example, "…on running water, but on its officer's word"). |
| C11 | M | Clarity | 26:273; 27 ("A minute. They had a minute's start on the face.") | Three face timings that do not reconcile. "If it's full sooner, a minute and twenty" is a dead conditional: the shutters always go full at one minute. Jude then plans on 1:40. |
| C12 | M | Clarity | 27:377 | "She was holding it with nothing open, because she was laid, and to lift anything she had to walk, and to walk she had to unlay." "Because she was laid" contradicts "nothing open" on one pass. The intended sense is that a laid person cannot move, so she had shut both doors. |
| C13 | M | Clarity | 30:317 | Kiva: "Ours was cut short. Theirs isn't. It's still got a post to stand on." Both stows had a whole far post standing after the near post was cut. Seven's far end lifted and the Tarn's did not. The line does not explain the difference it claims to explain, and the reader needs it to follow the turn eight minutes later. If the point is that nobody knows, let Kiva say so. |
| C14 | L | Clarity | 26:205 | "The Harbour Committee wrote to the Clerk three times". Everywhere else, "the Clerk" is the Clerk of the Measure. Name the Works' clerk, or Rusk. Hart's "The fourth" then also reads more cleanly. |
| C15 | L | Freshness | 27:311 | "Then he did a thing that made the whole quay go quiet. He bent and picked up the Purser by himself and put him across his shoulders". Brask did exactly that three runs earlier. The quiet belongs to the planting on every step, which comes two paragraphs later. |
| C16 | L | Apparent | 28:235 | "as Trewin had held out his own on Sunday morning, at the top of the loft stair". Chapter 24 shows Trewin coming down the room and nodding. No flat hand is on the page. Harmless if off-page. |
| C17 | L | Apparent | 32 §8 | Orla knew Coombe "by sight for a fortnight". Coombe was in Meridian 1st–14th of the second month, and the ledger does not say whether Orla saw her there. |
| C18 | L | Power image (new) | 31 §0 | Penhale's ward is left "grey… the shape of a ward, standing on nothing, like frost". A ward persisting as frost after its owner's death is new. It is a fine image, but it hints at a property of wards that the bible does not have. Keep it if it is meant to be inexplicable. Owner note. |
| C19 | L | Apparent (time words) | 28:145; 29:213 | The draw posted Tuesday at six says the lodger was marked "at the evening low", which must be Monday's (about 23:07). Penhale's "evening low" for the Mallow tears could be Tuesday's (about 23:56). Kellan's "not moved since five" at 28:173: at 5 p.m. Tuesday the pill's mouth is near high water. 5 a.m.? |
| C20 | L | Ranking rule | 32 §5 | Seven "need[s] two places in a bracket" (Perrin). Against Holloway second (one mark ahead) that means two places in the Lane, and against Westerley second it means three. The line is fine if it is his estimate. |

**Physical state: PASS.**

- Kiva: left hand warm Mon, Tue and Wed ✓. Right knuckles burned and in linen; she writes and carries
  left-handed ✓.
- Pru: all ten fingertips frosted ✓.
- Perrin: seventh rib cracked ✓. Aske's card is stated once and quoted consistently ✓. He breaks it once,
  lifting at the spur. No consequence is shown, and Aske was on his bed that night (32 §11). That is carried, not
  a slip.
- Jude: frosted left arm leaned on once ✓; the shin limp persists ✓.
- Dray: on two feet with a slight limp ✓.
- Bridie and Trewin: frost injuries as listed on Yeo's slate ✓.
- Lyle: ward gone, stance intact. She shows this on the page (32 §4) ✓.

**Power limits: PASS.**

- **No crossing, no stack, no three-door.** One declared door at each board: none at the Bench, stance at the
  Carry, Ember at the Hunt ✓.
- **The pass matches the bible.** Hand to Ember to still door, called, nobody holding twice. It closes no tear,
  kills nothing and mends nothing ✓. It was done with people who had rehearsed, not strangers ✓.
- **Students close no tear.** Ivey's and Bray's crews close them ✓.
- **No Glory master appears.** The Proprietor is offstage ✓.
- **Kellan's lit cut without an officer's word costs a remark.** So does Lyle's lay on her captain's word. That
  explains the Ropewalk's two remarks against Seven's none (Anwen lit on "*Pryce. Flat.*") ✓.

**Knowledge boundaries: PASS.**

- The dream: nobody new. No fever. White lights stay Kiva's alone.
- The Proprietor's letter reaches Kiva by Adlam, and Orla by the book ✓.
- Kiva knows the Mallow turn time "afterward", from Perrin's watch (30 §3), before she tells Noa ✓.
- Mara's thirty-six hands are known to Peverell and Hart only ✓.
- Halden's claim is known to Kellan and Kiva ✓.
- One note: Aske tells a tentful (including the Company healer) that Mara's hand was starved and eased with
  plain (32 §0). That is not a reserved disclosure, but it is a private medical fact said in public.

**Reserved: PASS.**

- "Unroofed" 0, "Breach" 0. No point of light, no hull. The disk is cold.
- No explanation of the Step, the notch, the hair, the held slack, the Hoop or the stow's early turn. Penhale
  ("Things like that don't hear") and Ivey hold the line.
- The public phrase is the plan's: "the worst Hunt in memory… a gifted generation in a bad season".
- No real month names (script: none).

**Plan adherence (Plan): PASS on every packet requirement.**

- The Bench without Kiva.
- The Carry won outright on Perrin's back, envied and "not better".
- Lyle's door lost for good.
- Penhale killed making the book's recovery, carried by Yeo, Pike, Rhea, Jude and Kiva.
- The pass live with Trewin, holding.
- Ninth after three.
- Carrow learning to declare.
- A Saltmere catcher reading the columns.
- No draft for Jude.
- Kiva and the cutaways inside 84–87%.

Departures are recorded in the continuity file §12. One addition to it: Rhea served as a Hunt officer, which the
packet did not ask for but which is consistent with it.

---

## 4. Numerical formula alignment

Method: `python3 -I provenance/tools/m4_metrics.py manuscript`, run from the book directory. The script is a copy of
`m3_metrics.py` with only the chapter range, the output labels and the viewpoint map changed (diff in §7). The
tokenizer, sentence splitter, syllable estimator and every lexicon are identical, so the figures are comparable with
Movements Two and Three. "M3r" means Movement Three as repaired (`MOVEMENT-003-REPAIR.md` §3b and the recheck).
Anything marked *manual* is the reviewer's judgment.

### 4a. Sentence rhythm — **the long tail is back; the short spike is worse**

| Metric | Target | **M4 all text** | M4 narration* | M4 dialogue | M3r all | M3r narration |
|---|---:|---:|---:|---:|---:|---:|
| Mean words | 14.6 | **9.5** | 10.9 | 5.9 | 9.6 | 10.8 |
| Median | 11 | **6** | 7 | 4 | 7 | 7 |
| Population SD | ~26 | **9.2** | 10.6 | 5.5 | 8.05 | 9.1 |
| ≤5 words | 27.7% | **46.1%** | 42.2% | 63.9% | 40.3% | 37.1% |
| ≥40 words | 3.3% | **1.6%** | 2.6% | 0.1% | 0.5% | 0.8% |
| Longest | — | 62 | — | — | 55 | — |

\*Narration has quoted spans removed; leftover tags ("said Kiva.") count as short sentences. 5,516 sentences;
dialogue is 29.1% of words.

The mid-band (6–39 words) is **52.3%** (M3r about 59%).

Per chapter, the short share runs from 40.0% (ch. 25) to **50.5% (ch. 28)**. Ch. 28's median is 5 and ch. 32's
short share is 49.2%. The long share reaches the target only in ch. 27 (3.1%), and is 2.1–2.2% in ch. 30–31.

**Read.**

- **The long tail is back.** The Movement Three waypoint for narration's long share (1.5–2.5%) is met (2.6%).
  The long sentences sit where they read best aloud: the climb, the cloth, the pass, the reflective close of
  ch. 25.
- **The short spike grew.** The short share rose about 6 points overall and 5 in narration, and the median fell
  to 6.
  - Part of that is deliberate fight rhythm (*Set.* / *Nobody.* / *Fold.*).
  - Most of it is the dialogue-dense planning and aftermath chapters (28, 32), where short exchanges and short
    narrated reactions alternate ("Kiva did not answer." / "It's said.").
  - The prose is bimodal again, with a thin middle. Not as extreme as Movement Two, but in that direction.
- **The owner conflict is unchanged and sharper.** Dialogue alone is 64% short. The whole text cannot approach
  27.7% unless the target governs dialogue too, or dialogue changes register.

### 4b. Paragraphs and scenes — **on target for the first time**

| Metric | Target (ASR proxy) | **M4 (typographic)** | M3r |
|---|---:|---:|---:|
| Paragraph median / mean | 18 / 26.8 | **18 / 31.4** (1,667 paragraphs; 18.8% over 60 words) | 22 / 32.2 |
| Section mean / median | ~950 | **1,006 / 827** (52 sections; 7 under 400; 22 at 900+) | 813 / 644 |
| Breaks per 10k, internal | ~8.7 | **8.41** | 10.83 |
| Breaks per 10k, with chapter openings | — | 9.94 | 12.29 |

Typographic breaks are not ASR pauses, so this is directional. Even so, every scene metric is now inside the
target band. The long unbroken sections (ch. 27 §0, 3,641 words; ch. 31 §0, 3,188) are single continuous actions,
which is correct. **Ch. 32** carries twelve sections, five of them under 650 words. The book-level numbers are fine.
The problem there is shape, not count (P3).

### 4c. Readability — **unchanged drift**

| Metric | Target | M4 | M3r |
|---|---:|---:|---:|
| Flesch Reading Ease | 72.3 | **96.3** | 96.0 |
| Flesch-Kincaid grade | 6.8 | **2.2** | 2.2 |
| Syllables per word (estimator) | — | 1.192 | — |

Tokenizer: regex words. The splitter is guarded for Mr./Mrs./initials. Syllables come from a vowel-group heuristic
with silent-e trimming. Names and terms (Purser, Polglase, Peverell, Mercury, Westerley) raise the estimate
slightly. As before, Flesch under-reads the real difficulty, which sits in procedure: needles, troughs, fathoms,
slack clocks and place marks.

### 4d. Progression vocabulary — **the mid-book recession the formula asks for, overshot**

The lexicon is unchanged from Movements One to Three.

- **Raw:** 152 hits = **29.1 per 10k** (M3r 56.3). Top hits: doors 74, Ember 24, licence 15, Hold 13, crossing(s)
  8, thimble 5.
- **Manual adjustment.** I read all 74 door contexts. About 24 are literal or metaphorical: the hall door, the
  barn door, "a door shut gently", "face like a shut door", the lockkeeper's hut, the van doors, the printer's
  door. Two "Hold" hits are the verb (30:237, 31:37). That leaves about **126 = 24.1 per 10k**. The automated
  literal-phrase grep removes only 8, giving 27.5. **Report about 24–28 per 10k, with the manual figure
  preferred.**
- **By equal-word thirds within the movement:** 43 / 54 / 55. The Bench and the Carry are lightest; the Hunt
  planning and the pass carry the system terms. That suits "surface only at genuine turning points".
- **Ash-economy terms:** 11.9 per 10k (M3 8.1).
- **Cumulative and provisional.**
  - The planned opening third (M1 + M2) is about 51–55 adjusted per 10k (Movement Two review).
  - The middle third so far (M3 + M4, 106.8k words) is about (245 + 126) / 106.8k ≈ **34.7 adjusted**.
  - The provisional front-load ratio is **≈1.47–1.58**, against the source's ~1.7×. It is closing.
  - The whole-book 58 per 10k is now out of reach. A final third at ~30 would land the book near 39.
  - **The standing conflict resolves toward the shape, against the average.** Owner decision, unchanged since
    Movement Two.

### 4e. Development beats

**Kiva (manual): about 35 choices or realizations, about 6.7 per 10k** (target 4.5). By chapter: ch. 25 ×5,
ch. 26 ×3, ch. 27 ×2, ch. 28 ×4, ch. 29 ×4, ch. 30 ×5, ch. 31 ×5, ch. 32 ×7. Representative:

- She tears the first page ever from her book: "It's for whoever has the drum." (25 §2)
- "It was not insurance. It was the thing itself." (25 §4)
- *I told him to*, left uncrossed. (25 §6)
- She says the price to Perrin. (26 §0)
- "I'm only the word." (26 §0)
- She waits for the heel at the eleventh rung. (27 §0)
- "Yes… It's that." Envy named. (27 §4)
- "It's yours to say… Ember." (28 §0)
- "Don't." (to Trewin) (28 §4)
- "Nothing… can't fold onto nobody." (28 §4)
- "Finch, ma'am. The second." (29 §1)
- *Down a hand*, unprompted. (29 §5)
- She writes the lean in the left column only. (29 §5)
- She lets go of the line. (30 §2)
- She does not say *well called*. (30 §2)
- *Far edge* across sixty paces. (30 §3)
- "Don't lift it… Let it come to you." (31 §0)
- She makes herself look. (31 §0)
- She puts the seven minutes somewhere. (31 §1)
- "Then we'd have had to talk about it." (32 §1)
- She tells Noa the time. (32 §3)
- She does not go up the Counting House steps. (32 §7)
- She gives Ivey the columns. (32 §10)
- "It turned before the water." (32 §10)
- *Before. D. Penhale…* (32 §11)

The regex proxy (29 hits, 5.5 per 10k) is reported only for reproducibility.

**Supporting cast (manual): at least twenty named people get a beat, and nobody becomes a deuteragonist.**

| Person | Beats |
|---|---|
| Perrin | the ladder plan and "Say the price"; the rib; envy; declares Ember for a thing "that might not happen"; captaincy as deciding for people; lifts against the card |
| Pru | carries the page ("I could carry that"); the far edge; "*No*" to an officer; "Don't say *well called*" |
| Anwen | reads two cells at once; "I want it said… I'll stand with it"; first wall on water; at Lyle's bench, no "I told you" |
| Jude | drains the jacket; two fingers on the loop; "Carrying it up the bank"; "I'll stay anyway" |
| Kellan | cuts on no word; "I'm saying it about you" (Pettit); the claim clerk's sum |
| Trewin | "If it's her… you'll not stop to ask me"; the laugh; the plant on the word |
| Yeo | answers by the book; decides the pass; "I said it was ground" |
| Coombe | the drill; holding the page back; the name at its head |
| Mara | thirty-six hands, not hers |
| Rhea | "for six years I'd have told you we didn't need one"; "Ask her tonight" |
| Pike | "He had nobody at his far edge" |
| Orla | "You'll find out now whether you meant it"; the card held a season |
| Carrow | shuts her stance: "I'm learning to declare" |
| Lyle | "There's one hand on the rope now" |
| Ivey | "I'll have a second" |
| Bridie | "What happens in the gap?" |
| Dray | "That's three people" |
| Polglase | "He's begun to look" |
| Peverell | writes names |
| Hart | "That's the right number" |
| Brask | the flat hand |
| Penhale | "I'll read that" |
| Aske | "You may hold a glass. A small one." / the plain not wanted |

### 4f. POV word share (viewpoint segments, not name frequency)

Segments (0-based sections after splitting on `---`):

- Mara: ch. 26 §2 and ch. 32 §9
- Kellan: ch. 30 §0–1
- Rhea: ch. 31 §4
- Anwen: ch. 32 §4
- Orla: ch. 32 §8
- Everything else is Kiva.

Ch. 32 §10 opens on Ivey arriving, but from "Quiller sent the boy up" it is narrated from Kiva's side of the
counter, so it is Kiva. Each cutaway opens on its lens by name and a private cue ✓.

| Lens | M4 words | M4 share | Cumulative M1–M4 (M2, M3 as repaired) | Cumulative share | Target |
|---|---:|---:|---:|---:|---|
| Kiva | 43,922 | **84.0%** | 185,406 | **86.6%** | ~87% (85–90) |
| Kellan | 2,541 | 4.9% | 6,829 | 3.2% | 2.5–3.7% |
| Mara | 2,282 | 4.4% | 6,941 | 3.2% | 2.5–3.7% |
| Rhea | 1,432 | 2.7% | 6,244 | 2.9% | 2.5–3.7% |
| Anwen | 1,159 | 2.2% | 3,856 | **1.8%** | 2.5–3.7% |
| Orla | 975 | 1.9% | 4,924 | **2.3%** | 2.5–3.7% |

The cumulative total is 214,200 body words. M1 + M2 are derived from the Movement Three review's cumulative
table; Movement Three uses the repaired recount (`MOVEMENT-003-REPAIR.md` §3c).

**The book holds its target.** Inside the movement, Kellan and Mara run hot and Orla and Anwen run cool.
Cumulatively, Anwen and Orla are the two lenses under the band. They are the natural lenses for Movement Five
cutaways (the hearing, Lyle's floor work).

The movement's count (52,311 here; 52,348 in the author's whitespace count) matches the author's 84.0% and 8,387
cutaway words to within tokenizer differences.

### 4g. Secondary signals (optional per formula §8)

| Signal | Source band | **M4** | M3 | Note |
|---|---:|---:|---:|---|
| "that" | 92.1 (tighten below) | **96.3** | 119.6 | best yet |
| just / almost / felt / seemed | 5–25 | 1.9 / 1.3 / 4.6 / 0.2 | 1.3 / 0.6 / 4.8 / 1.3 | — |
| -ly words | ~161 | 30.8 raw; **22.0** filtered | 26.5 | **"slowly" ×43 (8.2 per 10k)**, nearly double M3; "carefully" 10, "gently" 8 |
| Quote-adjacent tags | ~41 | **60.8** (318) | 56.9 | — |
| Combat terms | ~22 | **16.2** | 12.3 | *cut* 43, *blade* 12 |
| "out of the" / "one of the" / "for a moment" | 2–4 | 5.5 / 0.4 / **4.4** | 7.2 / 0.2 / 5.0 | — |
| House trigrams | — | "she did not" **13.2**, "looked at the" 10.7, "he did not" 8.6, "on the mud" 8.0 | "she did not" 14.5 (M3r) | "looked at" family heavy: 7.3 + 7.3 + 6.5 |
| Causal *since* | packet: use *because* | **0** (45 hits, all temporal; checked by hand) | 5 | fixed |

**Tics and voices (raw counts in 52.3k words).**

- **"I'd like it known" 4, all Perrin** ✓. **"I want it said" 3, all Anwen** ✓.
- **"I'd expect nothing else" 4.** Kellan ×3, plus Pettit's deliberate echo ✓.
- **"I'd want…" 18, now concentrated: 14 are Jude's "I'd want it said".** The rest are ordinary uses by Aske,
  Bray, Yeo and Anwen. The packet's voice fix worked, but Jude now says it **seven times in ch. 32 alone** (32:61
  ×2, 113, 343 ×2, 567 ×2). It is close to a catchphrase that the reader will hear coming, and it is at its
  densest in the movement's most grave stretch.
- **"said nothing" 8** (M3 22) ✓. "I'd sooner" 8. "nobody" 114, intended (the call), but aloud the word and the
  call collide ("Nobody passes anything to nobody").

---

## 5. Movement Three repair state in `STATE_LEDGER` against chapters 25–32

| Ledger item (M3 block, as repaired and rechecked) | In chapters 25–32 | Result |
|---|---|---|
| Hand to Ember six of six, certified; one in seven days | No crossing; "Thursday's the soonest" (26 §3, 29 §0, 32 §0, 32 §11) | PASS |
| Sixth: warm Mon 14th after four nights; Aske wants more than one warm morning; Thu 17th soonest; price said first | Warm Mon (packet), "Two mornings" Tue (26:229), "Three mornings" Wed (29:3); "I'll say it twice" (32:15) | PASS |
| The notch is shorter on the coast | Not exercised (no crossing); new evidence is the 12.44 hair, kept separate | PASS |
| Two fingers: *keeps time* everywhere; *nothing* at slack; the slack's end before the water | The rail, stave, desk leg and pole (all yes); silent at 12:12; silent through the 12.44 turn, which comes before the water (12:51) | PASS |
| Hart's method: same question, same hour, yes/no; first entry Sun 13th | Mon, Tue and Wed entries at a quarter to seven; the bed-rail touch not written (32 §11) | PASS |
| Disk cold | Checked Wednesday night: "cold through every crossing… and a Glory master's table" | PASS |
| Fever Fri 11th, "Nothing came"; Aske and Pru suspect | No fever. Aske's "Thursday. Soonest." in his sleep is untouched | PASS |
| Refused the Proprietor's ask (Friday, at his table; "the country can ask… in the Chair's hand", ch. 23:315) | Adlam: "the sequence you were asked for on Friday… as you told him the country could"; Kiva: "*I told him to*" | PASS (a strong payoff) |
| Seeded twelfth; lanes won 1, lost 2 | "We go thirteenth"; "seeded twelfth… the exact middle" | PASS |
| Book 4.16; sealed 2.0 W, bound *For a hand…* | Carried 4.16 → 6.26; the sealed tin asked for and refused on Aske's reading, binding restated (32 §0–1) | PASS |
| Catcher's rule: hands off the poles while her declared door is open | Not exercised (Kiva stood down, or stance at the Carry); she plants on the cloth, which is consistent | PASS |
| The Clerk's ruling on the lay | The Ropewalk lays freely; no incident question arises | PASS |
| The Hoop: 4′6½″ on the 8th and 9th; 6.12–6.33 / 6.13–6.33; basin lags the table by 23 minutes | Hart's book: 8th 6.12 at 4′6½″, 9th 6.13 at 4′6½″, then 10th 4′5″, 11th 4′2″. The 23-minute lag is now explicitly a neap behaviour, and the springs dawn slack is "held". Mara's first-night lag (on the 2nd, near the neap) still fits. | PASS (C12 used deliberately; the "Staff" column is read as ring height, which agrees with the ledger) |
| The prediction: 6.09, opens noon Wed 23rd | "at nine past six. That's what we wrote." | PASS |
| The Step at 57 | "Fifty-seven to the minute, or faster" (32 §11) | PASS |
| Mara has not touched a cell | Holds through the movement; Wednesday's decision is not to | PASS |
| Rhea: one night left, card ends the 30th; spring's advice spent | "the thirtieth, a fortnight off" (Wed 16th, 14 days ✓); "She had spent the spring's advice already" | PASS |
| Pike's hands close halfway | "half-closed hands", "hands half shut on a sack" | PASS |
| Jude: out of the sling for contests; shin limps | linen off for the Bench, held away; limps | PASS |
| Perrin: ribs as before; wants a second plant | Sprung, then the seventh cracked; the second plant "asked for on Sunday" is paid | PASS |
| Dray: walking without the stick | "on two feet, without a stick… a limp" | PASS |
| Coombe's page with the printer until after the Measure | Brought forward on Wednesday night by the Clerk's leave, on the page | PASS (consequence, not slip) |
| Orla and Hart met badly; Kiva told by Orla | Not contradicted; Orla's "a card held a season" agrees | PASS |
| Knowledge: dream, ferry white lights, 2604 entries | Nobody new; the white lights stay Kiva's alone | PASS |
| Open M3 owner items C13, C14, C21 | Untouched | carried |

**The author's Movement Four ledger block and continuity file against the prose.** They agree with the page on
every dated event, injury, ash figure and knowledge change I checked. Exceptions:

1. **Continuity §3's Bench reconciliation (places 7–11) conflicts with the page under the only ranking rule that
   gives Seven sixth (C1).** The ledger's standings after three are copied from the page and are internally
   consistent, but they rest on that reconciliation.
2. Continuity §1 says "Kiva would hear [Skerry] at three, at the gate". The page has her hearing on the causeway
   (C6).
3. Perrin's Monday rehearsal climb is not in the ledger's book (C9).

The viewpoint figures in `AUTHORSHIP.md` (whitespace tokens) and the script's (regex tokens) differ by fewer than
40 words for every lens.

---

## 6. Repair brief — three priorities, bounded

**P1 — Make the boards add up, and fix the line-level continuity (C1–C10).**

- *Location:*
  - the Bench heats, 25:151 and 25:283
  - Kiva's rail line, 25:169, and the Clerk's rules, 25:23–29
  - 27:217 (the water's direction)
  - 27:241 (Aske)
  - 25:233 (Orla reading)
  - 30:183 (when Kiva hears)
  - 31:371 (Yeo's clock)
  - 30:61 (forty paces)
  - 26:39 and the book (Perrin's rehearsal)
  - 29:49 (the rule)
  - the continuity file §1 and §3 and the ledger's M4 block, reconciled to whatever changes
- *Observed issue:*
  - Under the only ranking that gives Seven sixth on the Bench, three unnamed fours outrank the reconciled
    7th–9th, and Seven would stand seventh after three, on the roll. That is the movement's exit.
  - The rail minute that delivers the Bench's best moment is unplanted.
  - Plus a physical contradiction, a misplaced healer, three clock and geometry slips, and an unbooked door.
- *Effect on the reader:* the book promises that its sums add up ("That adds"), and its counting readers will
  test the boards first. C1 is the one slip that changes a result, and C2 is the one a sceptical adult will call
  convenient.
- *Proposed scope:* line edits; no scene changes.
  - **C1.** Have the Clerk say the rule once, in her opening (for example, "A four that holds is marked by its
    find. A four that steps is marked by how long it held."). Then make the heat times obey the reconciliation:
    - heat one's unknowns step before 5:00 (for example, "A four Kiva did not know stepped at four minutes, and
      another at three")
    - heat three's unknown steps before 5:00 ("At four, one of the three…")
    - give the Tarn's step on the page between 5:00 and 5:20 ("The Tarn's went at five and ten; Trewin did not
      move.")

    Do not change the printed boards.
  - **C2.** Add one clause to the Clerk's opening ("…and a minute at the rail between the quench and the tune,
    as at home"), or show Halden take and waive it in heat one.
  - **C3.** "…which was running with them now, pushing at their backs, pouring in from the head and going out
    nowhere". Or keep the river image for wading out against the press of the crowd at the stair.
  - **C4.** "I heard it go from the lip; everybody did."
  - **C5.** "…with her lips moving, the way Pru always did", or change 32:513.
  - **C6.** Change 30:183 to "until the cart, on the causeway".
  - **C7.** "at a quarter past twelve… Half an hour later".
  - **C8.** "sixty paces off".
  - **C9.** Add "off his own thimble" at 26:39, or a 0.22 line to the book (which would change every later held
    figure; the thimble is simpler).
  - **C10.** Add "but on its officer's word" to the Clerk's rule.
- *Strength to preserve:* the boards as printed; Kellan's sums; Jude's book lines; the clean harbour clock; the
  Clerk's flat "There are no squares on a ladder."

**P2 — One-pass clarity at the three teaching moments (C11–C15).**

- *Location:*
  - 26:273 and ch. 27 ("a minute's start"): the face clock
  - 27:377: Carrow's unlaying
  - 30:317: why the Tarn's sleeve does not fold
  - 27:311: the Tarn's carry
  - 26:205: "the Clerk"
- *Observed issue:* each needs a second read, and each sits at a point where the reader is learning a rule that
  matters in the next scene.
- *Effect on the reader:*
  - The thirteen-year-old loses the Carry's clock just before the climb.
  - Both lenses miss why the Tarn's stow does not fold, so the turn at 12.44 reads as arbitrary rather than
    uncanny.
- *Proposed scope:* one sentence each.
  - Kiva: "Half for a minute, then full. At full it reaches his face at a minute and twenty." Remove the dead
    conditional, and let Jude repeat the right number.
  - Carrow: "…but she was holding it with nothing open. A laid girl cannot walk, and to lift and walk she had
    shut both doors."
  - Kiva at 30:317: either name a difference she saw ("Ours had a post cut short before the slack. It never
    stood true after.") or say plainly that she does not know ("I don't know. Ours folded. It should.").
  - 27:311: move the "made the whole quay go quiet" beat to the first planted step.
  - 26:205: "wrote to the Works three times".
- *Strength to preserve:* "The fold had two ends"; "It's a sleeve… The book's for a sheet"; Bridie's "What
  happens in the gap?"; Penhale's "Things like that don't hear."

**P3 — Rhythm and the aftermath's shape, narration only (§4a, ch. 32).**

- *Location:*
  - ch. 28 (median 5; 50.5% short) and ch. 32 (49.2% short)
  - ch. 32 §5–7: the board, Dray and the *Mercury*, 1,332 words in three sections
  - "slowly" (43)
  - Jude's "I'd want it said" in ch. 32 (×7)
  - the "looked at" family
- *Observed issue:*
  - The short share is up 6 points and the median is down to 6.
  - The aftermath is a twelve-section survey.
  - Jude's tic is densest at the movement's gravest moment.
- *Effect on the reader:*
  - The planning and aftermath chapters trot.
  - Read aloud, the run of short reactive sentences ("Kiva did not answer." / "It's said." / "Nobody said
    anything.") flattens the grief.
  - The adult lens feels the survey as a roll-call.
- *Proposed scope:* a focused same-author pass on narration.
  - Join adjacent short narrated reactions where the thought is continuous, chiefly in ch. 28 §0, §2, §5 and
    ch. 32 §1, §2, §11.
  - Consider folding ch. 32 §6 (Dray, 316 words) and §7 (the *Mercury*, 294) into the board scene (§5) as one
    walk along the boards. **No cut of content.** This removes two breaks and keeps every line.
  - Recast three or four of Jude's ch. 32 "I'd want it said". Keep the window speech (32:567) and the board line
    (32:343).
  - Vary about a third of "slowly".
  - Leave dialogue alone until the owner rules on whether the sentence targets govern dialogue.
- *Strength to preserve:*
  - **Do not shorten the climb (ch. 27 §0) or the pass (ch. 31 §0).** They are the movement's earned length, and
    the long sentences there are the book's best read-aloud prose.
  - Keep the short call beats (*Set.* / *Nobody.* / *Fold.*).
  - Keep the night survey of the last paragraph of ch. 32. It closes the movement well.

**For the owner, not prioritised:**

1. Does the sentence target govern dialogue? Dialogue is 64% short this movement.
2. The progression shape now trends toward ~1.5× front-loading at the cost of the whole-book 58 (§4d). Confirm
   the shape is the priority.
3. Perrin lifted against Aske's card with no consequence on the page. Carry it to Movement Five, or have Aske
   notice.
4. Penhale's ward left as a frost-shape (C18): an inexplicable image, or a new property?
5. Monday's "It was the neap" (26:141): accept, or "near the neap".
6. Orla's "by sight for a fortnight" (C17) and Trewin's hand "at the top of the loft stair" (C16): accept as
   off-page.
7. Old M3 items C13, C14 and C21 remain open.

**Strengths to protect in any repair:**

- "Don't give them yours." / "That's why they'll want it."
- the torn page, caught "as if it had been a rung"; "I want it in your voice, so I've got it twice"
- "Is there anything in the rule about the jacket?" / "If your cells run hot, that's your hold, not mine."
- "I'm not on a ladder at all. I'm on twenty-two little pieces of the earth"
- "Say the price." / "I'm only the word."
- the eleventh rung, and "You waited for my heel"
- "It's not better… It's just the other side of the same thing."
- "There are no squares on a ladder."
- Trewin's "It's horrible" / Pru's "It gets more usual. That's not the same."
- "What happens in the gap?"
- *Far edge*, once, and the fold lying down where Kiva had been
- "It's a sleeve. It's got two ends. The book's for a sheet."
- "Let it come to you… Be the nearest thing."
- "He stopped at three."
- Yeo's "And mine. I said it was ground."
- Pike's "He had nobody at his far edge."
- Coombe's still hands, and the type set "like somebody counting"
- Ivey's curlew
- *Before. D. Penhale…*

---

## 7. Method — reproducible command, script hash and limits

Command, run from `/Users/drive/kindling-2680-book-02/books/book-2680-national-measure`:

```
python3 -I provenance/tools/m4_metrics.py manuscript
```

- `provenance/tools/m4_metrics.py` SHA-256 `d38a4760e55d9ef0cdf5397c3c136e199062f57eb3c34019328f68669c645a55`
- Copied from `provenance/tools/m3_metrics.py`, SHA-256
  `12036c794861f73e868759a4f73c511186146e751513de7c1af8db0747eb07cd` (the hash recorded in the Movement Three
  review and recheck).
- Full diff (only the range, the labels and the viewpoint map changed):

```
2c2
< """Movement Three numerical pass (copy of m2_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m3_metrics.py <manuscript_dir>"""
---
> """Movement Four numerical pass (copy of m3_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m4_metrics.py <manuscript_dir>"""
6c6
< CHS = list(range(17, 25))
---
> CHS = list(range(25, 33))
10,12c10,12
< POV = {(18, 12): "Anwen", (19, 10): "Orla", (19, 11): "Orla", (20, 7): "Rhea", (20, 8): "Rhea",
<        (21, 4): "Mara", (21, 5): "Mara", (21, 6): "Mara", (22, 6): "Kellan", (22, 7): "Kellan", (22, 8): "Kellan"}
< # 22/9 opens "Kiva was sitting on her bed" and stays observable from her bed, so it is Kiva (see report)
---
> POV = {(26, 2): "Mara", (30, 0): "Kellan", (30, 1): "Kellan", (31, 4): "Rhea",
>        (32, 4): "Anwen", (32, 8): "Orla", (32, 9): "Mara"}
> # 32/10 opens on Ivey arriving but is narrated from Kiva's side of Quiller's counter, so it is Kiva (see report)
```

**How the viewpoint map was derived.** Each chapter was split on `---` lines with the script's own regex. I listed
each section's index, its body-word count and its first paragraph, then read every section. I assigned a lens only
where the narration stays inside that person and Kiva is absent or seen from outside.

**Chapter SHA-256 at review time.** These are identical to `editions/movement-004-first-draft/SHA256SUMS.txt` and
to `AUTHORSHIP.md`:

| File | SHA-256 |
|---|---|
| chapter-25.md | 1667b92288d75c9a… |
| chapter-26.md | 759d563af7d82b45… |
| chapter-27.md | d00c10cf06ebbc86… |
| chapter-28.md | ab304c343318c170… |
| chapter-29.md | 4c4015080fe646a6… |
| chapter-30.md | 68adf8be9916736e… |
| chapter-31.md | 36a6b355de3ad948… |
| chapter-32.md | 1f137e9f86c09e19… |

**Manual counts and their limits.**

- **Literal doors.** I classified all 74 contexts by reading. Overlapping matches on the same line were resolved
  by reading the line.
- **Causal *since*.** I read all 45 hits.
- **Kiva's development beats and the supporting-cast table** are judgments, not counts.
- **Cumulative viewpoint** adds three sources with slightly different tokenizers (M1 + M2 via the Movement Three
  review; M3 repaired via its recount; M4 here). Expect ±0.1 point.
- **The arithmetic in §3a** used only figures on the page, except the bracketed places, which come from the
  author's continuity §3 and are labelled as such.
- **The tide-table extrapolation** in §3a assumes the ~49-minute daily step shown in Hart's own figures.

**Scope boundaries.** Nothing in this report changes manuscript prose, the ledger, the continuity file or
`AUTHORSHIP.md`. No repair, commit, push, publish or later chapter.
