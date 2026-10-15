# Kindling 2680, Book Two — Movement Four — targeted recheck of the consolidated repair

> Built by TAC

Date: 2026-10-15. Scope: the repaired findings and changed joins in chapters 25–32 only. This is not a second
editorial pass, not a cold read and not a score. No prose, record or tool was edited; this report is the only
file written.

## 0. Who checked, and how independent it is

- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** That is what the runtime
  states. I cannot verify it independently from inside the session.
- **Session:** Claude Code background job `e6a7d3ad` (job directory `~/.claude/jobs/e6a7d3ad`); remote session
  `session_01UzXXKECaMj6vGCVEZ2Xxap`. No subagent, other model, codex or OpenAI call was used.
- **Independence.** I am a different session from the drafting job (`9f1bbf7e`), the repair job (`647704f1`)
  and both review jobs. I had none of their transcripts. **This is a same-family, fresh-context check, not human
  review**, and it shares the author's and reviewers' blind spots.
- **Context leak, disclosed.** Before I read anything, a session-start memory hook injected a short work log. It
  said the repair had "reconciled" the Bench to Seven 6th, 3rd after two (43), 9th after three (53). I therefore
  knew the intended result before re-deriving it. The derivation below uses only the page.
- **Inputs read:** `MOVEMENT-004-EDITORIAL-REVIEW.md`, `MOVEMENT-004-COLD-READ.md` and `MOVEMENT-004-REPAIR.md`
  in full. A word-level `git diff --no-index --word-diff` of every frozen chapter against its working chapter;
  every changed passage was read in context. Chapter 25 was read in full, and so were chapter 28 and chapter 32
  §0–§3, §5 (with the folded Dray and *Mercury* text), §8 (Ivey) and §9 (the window). The ch. 30 climax
  (ll. 286–411) and the ch. 31 passages around every change were also read. Also read: the `git diff HEAD` of
  `STATE_LEDGER.md` (Movement Four block), `provenance/MOVEMENT-004-CONTINUITY.md` and `AUTHORSHIP.md`, and the
  continuity header and §12.
- **Working-file hashes** match the table in repair §9 for all eight chapters.

## 1. Frozen edition — checksum

```
cd books/book-2680-national-measure/editions/movement-004-first-draft && shasum -a 256 -c SHA256SUMS.txt
chapter-25.md: OK
chapter-26.md: OK
chapter-27.md: OK
chapter-28.md: OK
chapter-29.md: OK
chapter-30.md: OK
chapter-31.md: OK
chapter-32.md: OK
```

Exit 0. The frozen first draft is intact, and its hashes match the review's table (repair §9 / review §7).

---

## 2. Priority 1 — factual corrections F1–F18: **PASS**

### 2a. The Bench, re-derived from the page alone

**The rule as the Clerk now states it** (`chapter-25.md:53`, just before heat one): "A four that holds is
marked by its find. A four that steps is marked by how long it held, and by nothing else." The cross-category
order (every held four above every stepped four) is implied, not stated. Holding means holding all ten minutes,
which beats any shorter hold, and the printed board puts the five held fours first. A reader can follow it in
one pass. The old opening sentence ("marked by the time to find and by the hold") is gone from l. 39, so the
rule is said once.

**Every time on the page:**

| Heat | Four | Find | Hold / result | Line |
|---|---|---|---|---|
| 1 | Halden License | 1:40 | held | 25:69, 151 |
| 1 | Holloway (first, per the board) | 2:00 | held | 25:93, 151 |
| 1 | Westerley second | 4:30 | **stepped 5:20** | 25:93, 107–109 |
| 1 | unnamed A | — | **stepped 4:00** ("had stepped") | 25:151 |
| 1 | unnamed B | — | **stepped 3:00** | 25:151 |
| 1 | unnamed C | 6:00 | not stated | 25:93 |
| 2 | Ropewalk first | 2:10 | held | 25:159 |
| 3 | Team Seven | 4:10 ("slowest in the heat by a minute") | **stepped 8:40** | 25:213–215, 295–299 |
| 3 | unnamed | — | **stepped at 4** | 25:281 |
| 3 | Holloway second | — | **stepped 5:00** | 25:283 |
| 3 | the Tarn first | — | **stepped 5:10** ("Trewin did not move") | 25:283 |
| 2/4 | Old Four, Westerley first | 3:05, 3:30 | held (board only) | 25:355–357 |

**Ranking.** Held fours by find: Halden 1:40, Holloway first 2:00, the Ropewalk first 2:10, Old Four 3:05,
Westerley first 3:30, which gives places 1–5. Stepped fours by hold: Seven 8:40, Westerley second 5:20, the Tarn
5:10, Holloway second 5:00, which gives places 6–9. Every other step on the page is 4:00 or less. That matches
the printed board at `25:349–361` (six lines and "Five fours held. Nineteen stepped."), and Kellan's "Nineteen
fours out of twenty-four" (25:375). The heat-three steps are told in clock order (4, 5:00, 5:10).

Places 10–11 (the Ropewalk second and Twenty-Eight) are the author's reconciliation, off the page: both stepped
between 4:00 and 5:00. Nothing on the page contradicts that. Neither four is in heat one or heat three as told:
Kiva knows both, and the unknown fours there are fours she "did not know".

**Marks and sheets** (place *n* = 25 − *n*; the rule is printed at 28:109 and 32:307):

| Four | Bench | Carry | After two | Hunt | After three |
|---|---|---|---:|---|---:|
| Halden License | 1 (24) | 3 (22) | **46** | 6 (19) | **65** |
| Old Four | 4 (21) | 5 (20) | **41** | 2 (23) | **64** |
| Holloway first | 2 (23) | [7] (18) | **41** | [7] (18) | **59** |
| Ropewalk first | 3 (22) | 2 (23) | **45** | 12 (13) | **58** |
| Team Twenty-Eight | [11] (14) | 6 (19) | 33 | 1 (24) | **57** |
| Westerley first | 5 (20) | [9] (16) | 36 | [5] (20) | **56** |
| Westerley second | 7 (18) | [10] (15) | 33 | 3 (22) | **55** |
| Holloway second | 9 (16) | [8] (17) | 33 | [4] (21) | **54** |
| **Team Seven** | **6 (19)** | **1 (24)** | **43** | **15 (10)** | **53** |
| the Tarn first | 8 (17) | 4 (21) | **38** | 24 (1) | 39 |
| Ropewalk second | [10] (15) | [11] (14) | 29 | [8] (17) | **46** |

- Carry places 1–6 are on the page (the Clerk's announcement, 27:395). Hunt places 1, 2, 3, 6, 12, 15 and 24 are
  on the page (32:291–297). Bracketed places are the author's reconciliation.
- Every printed figure is reproduced: after two (28:111–121) Halden 46, the Ropewalk 45, Seven 43, Old Four 41,
  Holloway first 41, the Tarn 38; after three (32:309–327) 65, 64, 59, 58, 57, 56, 55, 54, 53, 46.
- **Seven is ninth, one mark behind Holloway second (54), the eighth and last place on the roll** ("The national
  license roll takes the first eight", 32:329; Perrin, 32:337). A four outside the table scores at most
  13 + 13 + 16 = 42.
- Under the frozen times (8:00, 6:00, 6:00), the unnamed steps outranked places 7–9. That conflict is gone.

**The rail minute.** It is planted in the Clerk's opening at 25:39: "It may take a minute at the rail between
the quench and the tune, as at home." It is used at 25:169 ("The Clerk read it out this morning", which fits a
nine o'clock reading and a two o'clock heat) and called at 25:223. Because the rule says "may", Halden's heat
one, which goes straight from quench to tune, stays legal.

### 2b. The other corrections

| # | Check | Result |
|---|---|---|
| F5 | Water at the ladder runs "toward the tail", "pushing at the backs of their legs" (27:77). Walking to the tail: "running with them now, pushing at their backs, pouring in from the head" (27:217). Head inflow agrees with 26:263–265. | PASS |
| F6 | Aske: "I heard it go from the lip; everybody did." (27:241). Agrees with Trewin's "I heard it… From the stair" (28:217). | PASS |
| F7 | "the way she read everything" (25:233); Orla "with her lips shut" (32:509); "the way Pru read" (27:441). | PASS |
| F8 / F9 | "She would not hear it until the cart, on the causeway." (30:183) agrees with "I heard. On the causeway. Lyle." (32:129) and the cart on the causeway (32:53). The bags are combed "back at the gate on the timber pond, as the Clerk had said it would, from four" (32:71). This matches the Clerk's "Every bag is combed at the gate" (29:49), Lyle "at the gate, after they combed us" (32:223) and the gate desk leg (32:203). The morning tins are combed empty at the causeway comb table (29:31, 137), a different event. | PASS |
| F10 | Ch. 29:349: "When it's printed, I'll read it. I've told half the causeway so. I'm not one for reading. But I'll read that." Coombe's line is unchanged (32:441, "on the causeway this morning, in the queue"). Both sources stand. | PASS |
| F11 | Yeo: "a quarter past twelve… Half an hour later" (31:371). Near post 12.14 (32:89), Penhale under at about 12.45 (30:365). | PASS |
| F12 | "a blade, sixty paces off" (30:61). Halden's stow is forty above the kiddle and Lyle twenty below it (30:3). | PASS |
| F13 | "…with my door open, off my own thimble." (26:39). The book is unchanged. | PASS |
| — | **Ash book.** 4.16 → Bench 0.31 → **3.85** (25:323) → Carry 0.35 → **3.50** (27:421; spoken "Three and a half", 28:355) → Hunt doors 0.17 + 0.10 + 0.12 = 0.39 → 3.11, plus 3.15 → **6.26** (32:109; "Six and twenty-six", 32:111). Combing 9.1 + 38 + 12.6 = 59.7; red 47.1; quarter of 12.6 = 3.15 (32:105). | PASS |
| F14 | "…on running water, but on its officer's word." (29:49). The 11.30 purse-setting is on Yeo's order, "Purses… Penhale. Show them." (29:305), with Penhale leading. | PASS |
| F15 | "wrote to the Works three times" (26:205). Hart's "The fourth" (26:209) now reads cleanly. | PASS |
| F16 | Board 6.00. Kellan "at ten past six" (28:165). Anwen "at a quarter past six", Kiva going down (28:189). The yard "at half past six" (28:213), after Perrin's slow walk. Ten passes, then the laugh (28:283–297). **The three-quarters strikes at 28:299**, with the stave and the log line *"Tuesday the 15th. A quarter to seven… Yes."* unchanged (28:303). Then "They did it ten times more" (28:305), Bridie's gap question, and the lamp. The yes/no hour stays a quarter to seven, and the clock now fits. | PASS |
| F17 | "He held out his hand." (28:235). Trewin "did not take the hand" (237) and "took the hand at last" (255), so no gesture is left dangling. | PASS |
| F18 | "This morning, when the upper one leaned before a gust." (32:531). The gust was "At ten minutes to eleven" (29:219). | PASS |

**Nothing moved.** No date, event, injury, power limit, knowledge boundary, outcome or printed board changed.
I compared every board line in the diff, and none of the sheet lines appears in it. Kiva's knowledge of the
12.44 turn still comes from Perrin's watch: "Perrin had the watch" (32:183; 30:365). Reserved terms are still
absent: "Unroofed" 0, "Breach" 0.

---

## 3. Priority 2 — clarity edits: **PASS**

- **The Carry's clock.** One number. Kiva: "Half for a minute… Then full. At full it reaches his face at a minute
  and twenty" (26:273). Jude and Perrin both repeat 1:20 (26:275, 279), and the sluice goes full "At a minute"
  (26:265). Ch. 27:63 reads "A minute, by the customs house clock. They had beaten the water to his face by most
  of a minute". That is consistent: out at 0:26 (27:43) against 1:20. The dead conditional is gone.
- **Carrow** (27:377): "But she was holding it with nothing open. A laid girl cannot walk, and to lift and walk
  she had shut both doors." Clear on one pass. It also no longer clashes with the Ropewalk second's carry
  lifting a spar while laid (26:287).
- **Why the Tarn's stow does not fold** (30:317): "It's still on a post." Then "I don't know why. Ours folded. It
  should." The false explanation is gone, and "It's still on a post" survives as the warning motif (30:355).
- **Climax geometry** (30:317, 373, 401; 31:107). The far post has one bearing: "on the west side of the bend,
  in the deep water". That agrees with "the deep side… a yard of water" (30:325) and the punt. The sleeve lies
  downstream on the west side (30:313). It swings "out of the downstream and inland over the west mud, its mouth
  to the sea". The closed end is named before it lands, as "its closed end last" (30:373), and again as "The
  closed end was still coming round" (30:401) before it comes over Penhale's back (30:403). "Across the channel"
  survives only where the sleeve truly spans it: from the post to Trewin's boots, and Trewin is on the east mud
  (31:89, 159, 313). The opening of ch. 31 ("the grey fold lying on the west mud across the channel", 31:3) is
  Kiva's view from the east bank, so it is correct. **The staging can be followed in one reading.** The
  protected beats are unchanged: the slack still holding, Penhale "as a man goes to a gate he has opened every
  day of his life", and Kiva's unanswered "*Far edge*" (30:381).
- **The Tarn's carry** (27:311–313). The quiet now falls on "He planted on every step he took, and the whole
  quay went quiet." It is no longer on the shoulder lift that Brask had already done. No seam.
- **The Chair's hand** (25:405): "He asked her to ask for it in the Chair's hand, as you told him the country
  could." "Her" is clearly Ysra Crest, and the wording echoes Kiva's own "*In the Chair's hand*" (25:409).
- **The Clerk's rule block** (25:39). It gains one clause (the rail) and loses the marking sentence, which is
  now at 25:53. The block reads cleanly, and the rule is said once, at the moment it matters.

*Observation, not a defect:* "out of the downstream" (30:373) uses "downstream" as a noun. It is a little
unidiomatic, but the arc is clear from "inland over the west mud" right after it. If the owner wants it
smoother, "out of its downstream lie" would do. It does not block.

---

## 4. Priority 3 — catchphrases, images and the aftermath: **PASS**

**Jude's "I'd want it said": 5 on the page, all in his gravest moments.** I re-counted with `grep -o -i`:

- 27:425 "…that I was at the top"
- 28:363 "I'd want it said I thought about it", answered at once by Kiva's "It's said" (28:365)
- 31:319 "…that I've seen it come in now. Over somebody." (protected)
- 32:343 the board line, "I'd want it said that I know it's honest" (protected)
- 32:563 the window speech, "I'd want it said I don't know. I'll stay anyway." (protected)

Every recast still sounds like Jude:

- "I leaned on it once, for a loop, and I'd do it again." (27:291)
- "This is honest as well." It still draws "It is." / "I know it is. I'm saying it." (28:129–133)
- "I know it's luck. We didn't do anything to get it." (28:157)
- "I don't know… And I'm going out on it tomorrow anyway." (28:363)
- "I don't know what I'd have said." (32:61)
- "I'd give it all back." (32:113)
- "I don't care about the mark. Tonight." (32:343)
- "I know she will." (32:563)

Anwen's three "I want it said" are untouched.

**Other voices.** Aske's "Understand that." (32:7) is terse and in character. Polglase's "Put that in your N.B.
as well." (32:197) is dry and fits Noa's ledger, which ends "N.B." (32:187). Kellan's "That's Pettit." (28:181)
fits him. Perrin's six "I'd like it/that known" are kept.

**Images, one home each.** Counts match repair §6:

| Image | Count | Home |
|---|---:|---|
| "frost on a window" | 1 | 31:171 |
| "the warm low sound" | 1 | 25:151 |
| "like a sack going up into a loft" | 1 | 26:287 |
| "as though nodding…" | 1 | 27:299 |
| "the way a referee holds up a hand" | 1 | 27:407 |
| "before the water" | 4 | — |
| "expect nothing else" | 3 | — |
| "slowly" | 28 | — |

The replacements read cleanly in place: "like dust on a sill" (30:271), "thin as a cobweb" (31:159), "lay on his
back on the quay" (27:195), "like a chest between two porters" (27:343), "Then he nodded, once." (32:41), "It
meant *that was right,* and Pru knew it." (25:307), "The quay clapped them, not loudly." (26:291) and "the quay
was pleased with them" (27:265).

**Ch. 29 telegraphing.** "Never gone onto the mud yet" now appears once, with "my mother likes it" (29:169).
Penhale's second instance is cut to "I'd like to see it." (29:341), and Kiva's "I'd sooner you didn't see it"
still follows. Yeo's single echo, "…and his mother liked it", is kept (31:343).

**Ch. 31–32 de-duplication. Nothing new was cut.**

- "The water had not turned. Only the stow." It restated ch. 30's last line.
- Yeo's first "Before the water." "Before the water turned, Dinah… Seven minutes before" survives (31:261).
- On Yeo's slate, "seven minutes before the water" became "in the slack" (31:303). The interval stays in her
  words to Coombe.
- Yeo's "From the spur. She asked… I said what the book says." It is shown in ch. 30 (ll. 335–343), and
  "I told the girl it was ground" opens the line (31:347).
- Kiva's account to Noa is reduced to data (32:183). **Noa's ledger is the single formal record** (32:187),
  with the full interval, the watch and the grass.
- At the board, Kiva's memory drops the quoted "I'll read it" (32:303). Coombe owns that line at 32:441.
- At Ivey's, the timing, fingers and grass are cut. "It turned before the water" (32:523) and "Seven minutes
  before, with the slack still holding, as if it had heard the turn coming" (32:527) keep the beat.
- Also at Ivey's, "He said when the Marshal's page was printed…" is cut. Kiva's "I know. He told me. Penhale.
  This morning, in the mud." (32:515) now answers Ivey's "We give it the corner-hand", which Penhale did say in
  the mud (29:349). The referent is clean.

**The folded ch. 32 sections. No line was lost.** The word-diff shows only two removed `---` lines and one
added sentence: "Kiva went back along the boards to the Long Quay." (32:373). In the same line, "on the Long
Quay" became "there".

- Dray's "Your three people held." (32:357) follows Perrin leaving, and "Kiva turned round" (32:359) places
  her at once, so the time and place run on continuously.
- The *Mercury* paragraph follows the new walking sentence.
- Section count: 50 (42 internal `---`; ch. 32 has 9 breaks, so ten sections).

**Joins of short narrated reactions.** I checked every join in ch. 25–32 (ch. 28 §0–§2, §5; ch. 32 §1–§5,
§9, §11). None makes a run-on. None changes a subject, and no "and"/"but" join reverses meaning. The calls
(*Set.* / *Nobody.* / *Fold.*), the climb (ch. 27 §0), the Skerry Pill fight and the pass are unchanged in the
diff. The only dialogue that changed is the formula recasts, the three borrowed-tic variants, the scoped cuts
listed above, Penhale's added clause, and Kiva's "I don't know why…". **No dialogue was reshaped for length.**

**Protected beats, present and unchanged:**

- *Far edge*: Pru's call once on Seven's stow (30:219) and Kiva's unanswered call (30:381). The frozen ch. 30
  also has two.
- "He stopped at three." (32:49)
- "And mine. I said it was ground." (31:311)
- "…a stow's a sleeve. It's got two ends. The book's for a sheet." (32:531; wording identical to the frozen text)
- "Let it come to you… Be the nearest thing."
- Ivey's curlew (32:543)
- *Before. D. Penhale…* (32:571–575)
- **The night survey that closes ch. 32** (32:589–597), untouched

---

## 5. Metrics spot check (not a gate)

`python3 -I provenance/tools/m4_metrics.py manuscript`. The script's SHA-256 is
`d38a4760e55d9ef0cdf5397c3c136e199062f57eb3c34019328f68669c645a55`, unchanged.

| Measure | Repair §5 "after" | Recheck |
|---|---|---|
| Body words / sentences | 52,116 / 5,456 | 52,116 / 5,456 |
| Mean / median / SD | 9.55 / 6 / 9.23 | 9.55 / 6.0 / 9.23 |
| ≤5 / ≥40 / longest | 45.8% / 1.7% / 62 | 45.8% / 1.7% / 62 |
| Paragraphs; median / mean; >60 | 1,667; 18 / 31.3; 18.5% | same |
| Sections; mean; breaks per 10k internal / with openings | 50; 1,042; 8.06 / 9.59 | same |
| Flesch / FK | 96.3 / 2.2 | same |
| Narration ≤5 / ≥40 / mean / median | 41.7% / 2.7% / 11.0 / 7 | same |
| Dialogue ≤5; dialogue word share | 64.2%; 28.9% | same |
| -ly filtered; "slowly"; progression per 10k | 19.2; 28; 29.4 | same |
| Per-chapter ≤5 / median / sections | as tabled | all eight rows match |
| `wc -w` movement / per chapter | 52,203; 6,356 … 9,245 | same |

**Viewpoint.** The unmodified script misreads ch. 32 after the fold: Kiva 43,747, Mara 2,249, Orla 999, exactly
as the repair predicted. I made a copy in the job's temp directory (not the repository) with only the two map
keys shifted, `(32, 8)` → `(32, 6)` Orla and `(32, 9)` → `(32, 7)` Mara (`diff` shows that single line). It
gives Kiva 43,738 (83.9%), Mara 2,283, Kellan 2,541, Rhea 1,420, Anwen 1,160, Orla 974, with cutaways 8,378.
That matches repair §5.

---

## 6. Records — do they match the surviving prose and claim no acceptance?

- **`MOVEMENT-004-REPAIR.md`:** matches the prose on every item checked. Its status line says "Not rechecked…
  not accepted, not committed, not pushed, not published". **OK.**
- **`STATE_LEDGER.md`, Movement Four block:** status "not rechecked, not accepted". The *(repair)* lines in
  M4.2, the Yeo and Coombe rows, M4.8 (clocks and rules) and M4.9 match the page. The standings line is
  unchanged and correct. **No stale line found.**
- **`AUTHORSHIP.md`, repair entry:** "Not rechecked… not accepted… not published". Word counts, measures,
  remapped viewpoint and the frozen-edition statement all match what I re-ran. **OK.**
- **`MOVEMENT-004-CONTINUITY.md`:** status "not rechecked, not accepted". The *(repair)* entries in §0–§4, §6
  and the §14 table match the prose. **Stale lines (records only; the prose is not affected):**
  1. **§12 item 1** (l. 339): "**Length:** 52,401 words (`wc -w`)". That is the first-draft figure, unmarked.
     Repaired: 52,203.
  2. **§12 item 2** (l. 340–342): "Kiva **84.0%** (43,961 of 52,348…); cutaways **8,387**: Mara 2,274…, Orla
     975". These are first-draft figures, unmarked, although item 3 right below them was updated *(repair)*.
     Repaired, with the remapped script: 83.9%, cutaways 8,378. Both are still inside the packet's bands.
  3. **§14 table section numbers for ch. 32** use first-draft numbering without saying so: "ch. 32 §8" for
     Coombe and the printer, "§10" for Ivey. After the fold these are §6 and §8. The same is true of repair §1
     and §3, where the report does state "first-draft numbers" for lines but not for sections.
  4. **§3 Carry, pre-existing and not changed by the repair:** "On the page also: Westerley second 3:26,
     Holloway first 3:21". The page leaves runs 14 and 15 unnamed by rank. The page also has a Westerley four at
     4:02 (run 1, 26:269) and a Holloway four at 3:38 (26:285), both slower than the Ropewalk second's 3:27. The
     reconciliation's Carry places 7–10 for Holloway first, Holloway second, Westerley first and Westerley second
     therefore hold only if Holloway and Westerley each send **more than two fours**. The page neither says nor
     contradicts that: 24 fours, three outside circuits, and the heats are full of fours Kiva "did not know". So
     this is **not an on-page contradiction**. The record should say it, so that a later movement does not name
     a "Westerley third" or "Holloway third" in conflict, or assume two fours each.

None of these lines claims a recheck, acceptance or publication.

---

## 7. Decision

| Priority | Result |
|---|---|
| 1. Factual corrections (F1–F18; Bench re-derived; sheets; ninth, one mark off) | **PASS** |
| 2. Clarity edits (Carry clock, Carrow, the Tarn's fold, climax geometry, Tarn carry beat, Chair's hand, rule block) | **PASS** |
| 3. Catchphrases, images, telegraphing, restatement, ch. 32 fold, joins | **PASS** |
| Frozen edition checksum | **OK ×8** |

**Overall: accepted for Movement Five context.**

No surviving or newly introduced prose defect was found in the repaired findings or the changed joins. The
record items in §6 (1–4) are housekeeping and do not block acceptance. They are bounded, and could be done at
the next touch of `MOVEMENT-004-CONTINUITY.md`:

- mark §12 items 1–2 as first-draft figures and add the repaired ones (52,203; Kiva 83.9%; cutaways 8,378);
- label the §14 ch. 32 section numbers as first-draft numbering;
- add a note to §3 that the Carry reconciliation assumes Holloway and Westerley each field more than two fours,
  and that the run-1 Westerley four (4:02) and the 3:38 Holloway four are neither the first nor the second four.

The `m4_metrics.py` viewpoint map is stale after the fold, as the repair documents. Any future run needs the
two-key shift.

This report accepts nothing beyond the scope above. It does not score the book, edit any file, update
`AUTHORSHIP.md`, commit, push, publish or draft forward.
