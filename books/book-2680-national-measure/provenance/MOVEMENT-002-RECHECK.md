# Kindling 2680, Book Two — Movement Two — targeted recheck of the consolidated repair

Date: 2026-10-14, about 23:20 MDT. Scope: chapters 9–16 of *The National Measure*, the repaired
findings and changed lines only.

## 0. What this is

- **This is a fresh-context, targeted verification of a same-author repair.** It is not a second
  editorial pass, a cold read, a human review or independent testing. No prose was scored.
- **The check is from the same model family.** The drafting, editorial review, cold read and repair
  were all recorded as Claude Opus 5.5, so this check can share their blind spots.
- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** That is what the
  runtime states. I cannot verify it independently from inside the session.
- **Session:** Claude Code background job `7508774e` (session file
  `7508774e-cd8e-49b8-b08c-951d352d2aff`); remote session `session_01RnjyaLjTBmt6n6XVupoNh4`. This is
  a different session from the drafting session and from the repair job (`80479656`).
- **No subagent, other model or delegated worker** was used. No codex or OpenAI call was made.
- **The context was not perfectly clean.** A memory hook at session start injected short progress
  notes from earlier sessions on this branch, including one-line notes that the repair was under
  way. I used none of them as evidence. Every finding below rests on files read in this session.
- **Brief:** delivered in-session; its text matches
  `planning/OPUS-5.5-MOVEMENT-002-RECHECK.prompt.md` (SHA-256 prefix `31b5407644c7`).
- **What I read:**
  - in full: `provenance/MOVEMENT-002-EDITORIAL-REVIEW.md`, `provenance/MOVEMENT-002-COLD-READ.md`
    and `provenance/MOVEMENT-002-REPAIR.md` (prefix `092cc3261358`)
  - every changed paragraph, by word-level diff (`git diff --no-index --word-diff`) of each frozen
    chapter against its working chapter, with surrounding context wherever a join, a cut or a
    referent needed it
  - `STATE_LEDGER.md`: the Movement Two block, and §2 (the three-door record and Body)
  - `provenance/MOVEMENT-002-CONTINUITY.md`: every *(repair)* entry and the lines they touch
  - `AUTHORSHIP.md`: the Movement Two repair entry
- **For F13 and for D1 below I also read Book One evidence:**
  - `books/book-2680-opening/manuscript/chapter-39.md` l.59
  - `books/book-2680-opening/STATE_LEDGER.md` l.305–312
  - the Stopgate table in `planning/OPUS-5.5-MOVEMENT-001.v2.prompt.md` l.2108
- **Changed lines:** 210 paragraph lines in the working files: ch. 9 26, ch. 10 22, ch. 11 34,
  ch. 12 24, ch. 13 18, ch. 14 20 (36 in the draft), ch. 15 30, ch. 16 36 (42 in the draft).
  All were inspected.
- **What I changed:** this file only. Nothing was committed, pushed or published, and no chapter
  was drafted.

Repaired text checked (SHA-256 prefixes):

| ch. 9 | ch. 10 | ch. 11 | ch. 12 | ch. 13 | ch. 14 | ch. 15 | ch. 16 |
|---|---|---|---|---|---|---|---|
| 60912ab028ea | c1a2d19ca47b | f8cfba5b8af7 | bcb42ba03979 | 0e3486e51037 | ebde9d5bd295 | 81f155d3ac51 | 814b0c9e4c7b |

Line numbers below are for these working files unless they are marked "draft".

---

## 1. Frozen edition — checksum

`cd books/book-2680-national-measure/editions/movement-002-first-draft && shasum -a 256 -c SHA256SUMS.txt`

```
chapter-09.md: OK
chapter-10.md: OK
chapter-11.md: OK
chapter-12.md: OK
chapter-13.md: OK
chapter-14.md: OK
chapter-15.md: OK
chapter-16.md: OK
```

Exit status 0. All eight hashes also match the chapter prefixes that the editorial review recorded
(§7: `e43856746d41` … `825f2c5d1fa5`). The frozen first draft is intact.

---

## 2. Priority 1 — factual corrections: **FAIL** (one defect survives, in F8's line)

| # | Verdict | Evidence checked |
|---|---|---|
| F1 comb | **PASS** | **Ash office (Tue 24th).** l.61 "The third reed sang, thin and faint." l.63 "The seventh did not." The hush (l.65) no longer claims a first: "Then Kiva heard what Pru had already heard. The third reed was sounding yet, and it was thin." **Pru (l.77)** blames the third: "The seventh's right; it's old enough never to have heard a beat. It's the third that's wrong. It sang thin…" **Jude (l.91):** "silent on the seventh, thin on the third; cut with soot to about half." **The Order (l.303)** has the only "first", qualified: "a comb held over ash that was whole and plain: the third full, and nothing on the seventh but nothing." A grep of ch. 16 for "first time" finds no other comb claim (the l.261 and l.279 hits are Thrale's eyes and hands). This agrees with the bible and ledger: 2669 stock predates the Step. |
| F2 sheets | **PASS** | **ch. 15 l.101:** Kiva carries "a cloth on each shoulder, Seven's and Pru's own"; Pru has "Mrs. Pryce's grey double rolled on her back". **The casts:** Kiva's first cloth goes over the first heap (l.177). Her second goes over the race lip (l.285–291). "There was no third cloth" (l.311) reads as Kiva's own empty shoulder. **Pru (l.317)** throws "Mrs. Pryce's grey double off her back". **l.331:** the frosted cloth is "Pru's sheet, the second that Kiva had carried down." **l.335:** "Pru tied it on the grey double at fifty-one." **l.369:** "two sheets and a frosted one rolled on Pru's back". **ch. 16 l.37:** "to replace Finch's, frosted at Garside's mill: 2.40". The chain is closed. |
| F3 tallies | **PASS** | **Jude's cuts:** l.175/177 (first, falls), l.191 (second), l.279, l.309 (mill), l.453 (kiln) — five. **Pru's ties:** l.325 (47), l.327 (63), l.335 (51), l.467 (52) — four. **l.519:** "Talley, five cuts, 0.18" and "Finch, nothing lit; four cords tied". |
| F4 countdown | **PASS** | Rule: 44 minus the date. **ch. 9 l.3–5:** *44* rubbed out, *43* chalked (the 1st); l.155 *43*. **ch. 13 l.495:** *31* wiped, *30* chalked (Sat 14th). **ch. 16 l.161:** "Nineteen… It's the twenty-fifth" (Wed 25th). **l.163:** "Tomorrow's eighteen" (26th). **l.411:** "Sixteen" (Sat 28th). A sweep of ch. 9–16 found no other chalked or spoken countdown figure. Perrin's kept comeback (l.165, "I know what tomorrow is. I was saying what today is.") now answers a correct forward count. |
| F5 | **PASS** | ch. 16 l.209 "six days ago": the kiln was Fri 20th; the Order is Thu 26th. |
| F6 | **PASS** | ch. 15 l.73 "a fortnight ago": the tram sheds were Fri 6th (ch. 11 l.37); the hut night is Thu 19th (ch. 15 l.69). That is thirteen days. |
| F7 | **PASS** | ch. 14 l.189 "Two days, five by the time we're there": the tear was Sat 14th, the letter Mon 16th, and the team reaches the hut Thu 19th. |
| F8 | **FAIL** | The amputation reading is fixed ("lost the feeling in two fingers"). But the same clause still places the loss "on a hill", and the repair added "in the dark". See **D1** (§6). |
| F9 | **PASS** | ch. 12 l.157 "The two on the far side, who were only Hesketh, coming off her wall, and Kellan…". Hesketh stays "her" throughout. |
| F10 | **PASS** | ch. 9 l.599 "with his colleague, who had seen to Jude's boot." The source is ch. 9 l.443 ("Aske's colleague from the Wren House kneeling at his boot"). |
| F11 | **PASS** | ch. 14 l.143 now opens the quote. An odd-quote-count scan of ch. 9–16 flags no line. The ledger inside the line still holds: 3.06 − 0.31 = 2.75; 2.75 − 0.15 = 2.60, "two and sixty". |
| F12 | **PASS** | ch. 13 l.193 "stood by the shed step last Thursday morning and heard Perrin say it to the Marshal". The source is ch. 11 l.3 and l.21 (Thursday the 5th, morning, the shed step, the words quoted). Seen from Thursday the 12th, "last Thursday" is correct. |
| F13 | **PASS** | ch. 11 l.345 "It was the Pit in the ninth month, over again: a corner pinning Selka Dray to the ground, and the thing that had had to be done was to take the cord off her and carry it four paces east and plant it." **Confirmed against Book One ch. 39 l.59** (the Pit, the Regional): "It's lying across her leg… I'd bend mine to turn that one east… go with the throw, four paces out, that way.' She pointed east". At Stopgate, by contrast, four paces east "is not clean… Kiva turns the mark north" (M1 v2 prompt l.2108). This agrees with the ledger: three clean three-doors, the Pit on the 17th of the ninth; Dray's leg on the same date. |
| F14 | **PASS** | ch. 15 l.413 "since the autumn". |
| F15 | **PASS** | ch. 15 l.101 "had outlasted Coombe's Thursday by a fortnight and was better". "Limp till Thursday" is ch. 9 l.307, Thursday the 5th; this is Friday the 20th, fifteen days later. |
| F16 | **PASS** | ch. 15 l.425 and l.499 now say "a share". In ch. 14–15, no "eighth" share figure comes before Vane's weighing (ch. 15 l.515). Jude's own rule at ch. 14 l.177 ("If it comes up plain, it's for a hand… it's a share") already uses "share", so the terms agree. |
| F17 | **PASS** | ch. 14 l.219 "By the time Kiva looked out past the tailboard…". Kiva is on the van's side bench (l.199). The slate goes up "to the van's lamp" (l.227), and "There was a pause in the van" (l.235). The slate scene sits inside the van. |

**Ash ledger: reconciles to the hundredth (PASS).**

- **Running totals on the page:** 9.64 → 9.33 → 9.05 → 8.81 → 8.59 → (8.29) → 7.83 → 7.68 → 3.24 →
  3.06 → 2.75 → 2.60 → 8.93 → 6.23. Every spoken total string the repair report lists is still
  present: "nine and sixty-four" … "six and twenty-three", "five and sixty-three", "ten and
  eighty-one", "seven and forty", "fifty-nine drams and two-tenths", "twenty-nine and six",
  "Up six and a third", "Two drams".
- **Hunt (ch. 15 l.519):** 2.60 − 0.40 − 0.31 − 0.18 − 0.12 − 0.06 + 7.40 = 8.93.
- **Month (ch. 16 l.37):** I re-summed the cut readout.
  - Crossings: 1.22.
  - Pit 0.28; Old Yard 0.24; the 7th 0.22; lane 0.46; the 11th 0.15; floor 4.44; the 13th 0.18;
    the tap 0.15.
  - Cowl Edge: 1.07. Sheet: 2.40.
  - Total spent: 10.81. Then 9.64 − 10.81 + 7.40 = 6.23, and 6.23 − 0.60 = 5.63.
- **Shares:** 59.2 = 29.6 + 4 × 7.4. Bags 13.8 + 12.6 + 14.7 + 18.1 = 59.2.
- **Sealed:** 0.8 + 1.2 = 2.0.
- **Crossings:** 0.31 (the 1st, ch. 9 l.149) and 0.31 (the 15th, ch. 14 l.143) are stated. The two
  0.30 figures (the 8th and the 22nd) were stated only in the cut ch. 16 readout. They are now
  derivable but not written: 8.59 → 8.29, and 8.93 − 2.40 − 6.23. See the records note in §5.

**Nothing else moved.** Every weekday, event, outcome, power limit and knowledge boundary in the
changed lines is as before. The one injury-location problem is D1, which predates the repair but
sits in a repaired line.

---

## 3. Priority 2 — clarity edits: **PASS**

| Item | Verdict | Evidence |
|---|---|---|
| "Pit hands" | PASS | ch. 11 l.285 "two Pit hands in brown"; l.287 "The first put a hand door under it"; l.299 "The one with the stance took his boot off the sack"; ch. 11 l.405 and ch. 13 l.351 "two Pit hands on a sack". No person is called a "ward" in the changed lines. |
| Plank and unlike doors, ch. 13 | PASS | l.215 "Kiva did not understand her." l.217 "I can't put up a ward." l.219 "Not a ward. Your ground." l.221 "It was not a plank. A plank was two still doors on one patch of ground." l.223 "This was a ward on a still door's ground, Anwen's hand door on Kiva's still: two unlike doors on one thing, at once." This agrees with ch. 11's two-door vocabulary. |
| Anwen's "her still door" | PASS | ch. 13 l.375 "Because I'd not have Rowan put her still door under my heels…" |
| ch. 10 slope chain | PASS | l.185 "On a wharf, it ran downhill, onto the cloth, because the skin was downhill." l.193 "And it's downhill when the thing faces uphill. The skin trails behind it." |
| Rung rule planted and paid off | PASS | ch. 10 l.187 (Wednesday the 4th, l.99): "Off a heavy edge, it falls away from the edge that cut it. Then down, and to the low side, while it's open." ch. 14 l.237 (Rhea): "falls away from the edge that cut it, if the edge is heavy enough. I've a Torch's edge." ch. 14 l.289: "away from the edge that had cut it, as Rhea had said it would." The "heavy edge" condition matches in both places. |
| Coombe's added lodger line | PASS; **no contradiction** | ch. 13 l.107: "On Saturday I kept one off Rowan to teach a rail. This isn't teaching. It's a license…" The earlier statement is ch. 11 l.241 (the Pit, Saturday, l.229): "I've no notion what this would do near her… I'll not find out on a Saturday morning in a Pit to teach sixteen people a thing they can learn without her." The new line restates that reason (a teaching demonstration) and distinguishes the license floor. It does not contradict it. |
| Causal "since" recast | PASS | All fifteen read correctly as "because": ch. 9 l.137, 159, 211, 375, 535, 561; ch. 10 l.185, 193; ch. 12 l.313; ch. 13 l.295; ch. 15 l.381; ch. 16 l.109, 203, 243. The total is 95 (112 before). |
| ch. 11 §6, Noa's reading | PASS | l.385 gives the whole reading in one speech (first pass; "the same again at the second pass. Ember and stance. One line, for a count.") Then come "Whose?" (l.389), Noa's answer (l.391) and the Chair's sheet (l.395). Each item arrives once, and nothing from the old order is lost. |
| POV anchors | PASS | ch. 10 l.345 Anwen ("the afternoon's wall still aching in both forearms", after ch. 10 l.257). ch. 12 l.3 Kellan, unchanged. ch. 14 l.29 Orla ("her bad left knee"). ch. 16 l.127 Mara ("her reading hand flat on the oilcloth", which agrees with l.135). |

**Non-blocking notes** (no fix required):

- **ch. 10 l.187.** "Your catcher said so. He's written it" now follows a three-part rule, and Pike's
  record supports only the down-and-low-side part (ch. 7 l.65). A reader could take the attribution
  to cover the new "falls away" clause as well. The ambiguity is mild.
- **ch. 16 l.65.** "Then Kiva heard what Pru had already heard. The third reed was sounding yet, and
  it was thin" repeats l.61 ("The third reed sang, thin and faint"). It reads as Kiva taking in the
  meaning after the hush, which is acceptable.

---

## 4. Every changed line — joins, splits, reductions and thinning: **PASS**

- **Joins and splits.** Every split (mostly at an existing semicolon or "; and") and every join
  leaves a grammatical sentence with the same referents and meaning. I found no breathing comma
  between subject and verb, no orphaned "and", and no clause that changed its subject. Some I
  checked closely:
  - ch. 9 l.85; ch. 10 l.23, l.177 (the colon after "listing"), l.257 ("with the sheet lying behind
    them")
  - ch. 11 l.321, l.461; ch. 13 l.449
  - ch. 15 l.101, l.377 ("from the north" moved forward)
  - ch. 16 l.83, l.157, l.167
- **ch. 14 van opener.** Inside the van (§2, F17). Rhea's "my gate" (l.227) still maps to Mace's
  wall, now that "Gate," said Rhea is cut. The slate goes straight from *Before* to "Pike."
- **ch. 14 §7 reduction (l.377–383).** It reads as one exchange: Jude's "It doesn't say what", Mara's
  "If it's quiet, it's a hand," and Jude's "That's what it's for." "She looked up, at last" still
  works after "as she was every night now". The meaning is carried by Jude's own rule at l.177.
- **ch. 16 §1 reduction (l.31–41).** The pieces left are: the opening totals; one narration sentence
  for the read lines; the sheet; "*Held, six and twenty-three.* Spent this month, ten and
  eighty-one; credited, seven and forty."; "It adds"; and the spoken-for line. Nothing reads as
  missing.
- **Later references to cut material.** No later line refers to anything that was cut. I grepped
  ch. 14–16 for "eighth", "Rusk", "new this year", "medical" and "shares". The "handed crossing"
  count fell from 4 to 2 with the readout, and Jude's coinage survives (ch. 13 l.469, l.471).
- **Knots: 21 → 7.**
  - Coombe's rope still pays off in ch. 13: knots at l.103 and l.421, and the coiled rope "with a
    great many knots in it" on the step (l.495).
  - Non-blocking: Friday's "fresh length of rope" (l.433) now gets no knot on the page; its one
    knot became "She looked down at the rope in her hands" (l.463). The reader must infer the
    afternoon's knotting, as the draft already partly required.
  - No dangling gestures.
- **"I'd like it known": 11 → 10, all Perrin.** Checked at ch. 9 l.7, 157, 267, 539; ch. 10 l.29,
  89; ch. 11 l.33; ch. 12 l.169; ch. 13 l.79, 425. Kellan's line at ch. 14 l.87 is plain.
- **"slowly": 39 → 26.** No dangling commas: ch. 11 l.259, 295, 309; ch. 12 l.121, 377; ch. 14 l.263;
  ch. 15 l.467, 517; ch. 16 l.325.
- **"scratched his jaw": 10 → 4.** The cuts leave the speaker clear:
  - ch. 9 l.485: the dresser is set at l.479
  - ch. 12 l.195 and l.271: Jude is identified at l.191 and l.267
  - ch. 13 l.467: "He" follows "said Jude" at l.465
  - ch. 14 l.171; ch. 15 l.149
- **"pale eyes": 8 → 3**, all Coombe. Rhea now has "her eyes" (ch. 14 l.221).
- **Corner-of-mouth tell.**
  - Coombe: "the Marshal's hands go still on her rope" (ch. 10 l.313, the only "for the first
    time"); "Her hands went still on the rope" (ch. 13 l.401). They do not collide.
  - Thrale: "her folded hands moved" (ch. 16 l.279); the folded hands are set at l.247.
  - Mara, ch. 9 l.585: the pencil is set at l.487.
  - Mara, ch. 16 l.123 (non-blocking): "Her pencil tapped once on the oilcloth" uses a pencil that
    the scene never sets (l.113 has only the tide table pushed aside). Her habit from ch. 9 covers it.
- **Vane: "thirty years" 4 → 0.** The slate markers at ch. 15 l.55, l.433 and l.539 are coherent.
  Coombe keeps two (ch. 10 l.323, ch. 13 l.475), and the two Ottery uses are a different person.
- **Dialogue changes.** All were checked as above. None changes a speaker, a fact or a turn of the
  argument.

**Metrics spot check** (`python3 -I provenance/tools/m2_metrics.py`, SHA-256 `67e20cae24cf…ef0f`, the
recorded script). It was run on the frozen edition and on the working manuscript, and reproduces
repair report §5b–§5f exactly:

| Measure | Frozen | Repaired | Report §5 |
|---|---:|---:|---|
| Body words / sentences | 59,556 / 5,494 | 59,150 / 5,518 | same |
| Mean / median / SD | 10.84 / 6 / 12.55 | 10.72 / 6 / 11.18 | same |
| ≤5 / ≥40 words | 46.0% / 4.6% | 44.6% / 3.6% | same |
| Longest sentence | 96 | 78 | same |
| Narration median / ≤5 / ≥40 | 7 / 43.5% / 8.0% | 7 / 41.4% / 6.2% | same |
| Dialogue word share | 30.3% | 30.3% | same |
| FRE / FK | 96.9 / 2.4 | 97.0 / 2.4 | same |
| Progression per 10k / "since" per 10k | 58.9 / 18.8 | 58.5 / 16.1 | same |
| POV (Kiva/Anwen/Kellan/Orla/Mara) | 55,504/1,297/1,134/949/672 | 55,077/1,304/1,134/953/682 | same |

`wc -w` gives 59,234 (59,623 before), which matches §5a. "Unroofed" and "Breach" both count 0, and no
real month names appear. As the brief directs, no formula compliance is required of this pass.

---

## 5. Records: **PASS** for the claims; **two stale lines**

- **No record claims a recheck, acceptance or publication.**
  - `MOVEMENT-002-CONTINUITY.md` l.9–11: "Nothing here is rechecked or accepted."
  - `STATE_LEDGER.md` Movement Two block, status line: "Not rechecked, not accepted."
  - `AUTHORSHIP.md` Movement Two repair entry: "Not rechecked, not cold-read after repair, not
    accepted, not committed, not published."
- **The *(repair)* entries match the surviving prose:** the comb (24th and 27th), the countdown, the
  Pit rig, the Pit hands, the sheets, the tallies, the rung rule, Coombe's line, the plank, the
  shares, and the ledger reading.

**Stale lines** (records only):

1. **`provenance/MOVEMENT-002-CONTINUITY.md` l.216.** "the Board an eighth (on a hunt card; "new this
   year"), 7.4". It quotes "new this year" as on the page, but that phrase was cut with Mara's
   speech. The same file's l.326–328 says so ("The attribution to Rusk and "new this year" were cut").
2. **`provenance/MOVEMENT-002-CONTINUITY.md` l.310.** The unnamed-cast list still reads "two Pit
   wards". The page and the calendar entry (l.42) now say "Pit hands".

**Record-accuracy notes** (in the repair report; no fix required):

- **§4.** "Every figure removed appears earlier on the page" is not exact. The two 0.30 crossing
  costs (the 8th and the 22nd) appeared only in the cut readout. Both can be derived (§2), and the
  month still adds.
- **§3a.** The "since" line numbers for ch. 16 (l.115, l.209, l.249) are first-draft numbers. They
  are now l.109, l.203 and l.243.
- **§3c.** "The longest outside a protected fight is under 60" holds for narration. One dialogue
  sentence of 64 words remains (Vane, ch. 15 l.507), and dialogue was out of scope.
- **"Mrs. Pryce's grey double is the drill sheet"** (continuity l.125; ledger "still the drill sheet")
  is not stated in ch. 9–16. It was carried from the drafting record (present at `HEAD`) and is not a
  repair artifact.
- **`AUTHORSHIP.md`'s earlier drafting entry** ("No frozen edition exists for Movement Two") was true
  when written. The repair entry correctly reports the frozen edition as unmodified.

---

## 6. Decision — **one concrete defect requiring a second repair**

**D1 (prose; priority 1, physical state). `manuscript/chapter-16.md` l.135**, Mara's cutaway:

> She had sat across this table from a girl who had lost the feeling in two fingers **on a hill in
> the dark** for a method that nobody else could do…

- **The defect.** This places the permanent loss of the two fingers at Stopgate. That was the tenth
  month, at night, and this book's own phrase for it is "a hill in the dark" (ch. 6 l.477; see also
  ch. 5 l.165, "under the arm of a thing in a pit, and under a cord on a hill").
- **What the record says.** The fingers went in the **ninth month**, after the lane on the 16th and
  the two gaps "the next day" in **the Pit** (Book One `STATE_LEDGER.md` l.305–312; Aske, the 24th of
  the ninth). Stopgate cost the arm, and the arm came back (this book's ledger, §2 Body).
- **It contradicts this movement twice.** ch. 13 l.21 ("Rowan can't tie. She's said so on a list
  since the ninth month") and ch. 13 l.207 ("she had known since the ninth month that she could
  not").
- **The repair made it worse.** The draft said "on a hill". The repair's F8 kept that and added "in
  the dark", which identifies the night at Stopgate more firmly. That runs against the repair's own
  F13 premise: the Pit was the ninth month and the hill the tenth.
- **Bounded fix.** Replace "on a hill in the dark" with "in the Pit in the autumn". The book already
  uses "autumn" for that Pit (ch. 9 l.187: "in the autumn there had been a square of skinned husks
  over the race"). One phrase changes; nothing else does.

**With the second repair, records only:** correct continuity l.216 by dropping "new this year" from
the parenthetical, and l.310 to "two Pit hands".

After those three edits, a confirmation needs only a diff of ch. 16 l.135, the two record lines, and
the frozen-edition checksum. Every other repaired finding and changed line passed this recheck and
need not be reopened.
