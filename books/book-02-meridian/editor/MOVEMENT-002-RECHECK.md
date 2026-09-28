# Movement Two ("The North Yard", chapters 9–16): targeted post-repair recheck

## Reviewer and disclosure

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), in a fresh context and in the editorial-checker role only.
- **Disclosure:** the same model wrote the manuscript and the repair. This is a same-model check with a fresh context. It is **not** an independent human read, and it has no independent judgement of voice or taste.
- **Scope:** only the eight questions in `MOVEMENT-002-RECHECK.prompt.md`. This is not a new developmental review. No source file was edited.

### Method

- I compared the frozen `editions/movement-002-first-draft/chapter-09.md`–`16.md` against `manuscript/chapter-09.md`–`16.md`, using a line diff and a word diff. Every changed hunk was read.
- I read the Sag sequence in full in its repaired form: ch. 14 lines 345–644, ch. 15 lines 60–360, and ch. 16 lines 85–470.
- I checked named facts against:
  - `../book-01-kindled/UNIVERSE_BIBLE.md`, for Kindling at 13, Homura, Vell, Dee Wren and the handover lapse;
  - both name registries;
  - Book One `chapters/chapter-50.md`, for where the arm broke;
  - Movement One `manuscript/chapter-01.md` and `chapter-03.md`.
- All line numbers below refer to the manuscript files as they stand on disk at this check.

---

## Results

| # | Question | Result |
|---|---|---|
| 1 | Minute-20 handover is causally clear and worded consistently through the ledger | **PASS** |
| 2 | Toren's sighting, silence, admission and ledger entry agree, with no impossible knowledge | **PASS** |
| 3 | Dee's arrival order and two-minute delay agree across ch. 14–16 | **PASS** |
| 4 | Day and count corrections and Dee's Homura age are consistent with the map and canon | **PASS** |
| 5 | Dee-reference cleanup: no ambiguous pronoun, no viewpoint-name error, the girl stays unnamed | **PASS** |
| 6 | No broken grammar, power-limit change, moved object, reset injury, exposed reserve or spatial damage | **PASS** |
| 7 | Preserved motifs and decisive fight beats are present | **PASS** |
| 8 | The repair report accurately describes the on-disk changes and word counts | **PASS** (with minor notes) |

### 1. Minute-20 handover: PASS

**The new beat.** It sits in ch. 14 at lines 445–449.
- Pell calls "Minute twenty. Holder, do we change?"
- The holder refuses, because letting go to hand over opens a gap on the moving slab at six. This agrees with the bible's lapse rule (bible l. 389; the Director's "lapse of about four seconds" in ch. 10 l. 407).
- She orders "Keep your hands down, Marsh."
- The fold follows at l. 451 ("And then the ground spoke").

**Why it works as a decision.** The choice is visible and belongs to named people. The ledger can therefore name it as a failed decision.

**The wording stays consistent in every place it appears:**
- Pell's plan, ch. 14 l. 227: *M. takes the line at the twentieth minute.*
- The ch. 14 narration: "nobody had said when they would try the change again".
- The ledger timeline, ch. 16 l. 331: "Minute nought to minute eighteen: lift as planned", then "Minute twenty: change of holders called — P. Holder kept the line with six moving; R. kept his hands down. No new minute set. Minute twenty-one: slab dropped."
- The *what to change* rule, ch. 16 l. 351: "If the change can't be made on the minute, somebody says out loud who's holding and when we try again."
- Continuity sequence items 2–3.

**Not defects:**
- The ledger's "R." and Pell's plan's "M." both mean Rook. They are written by different people, and the ledger itself uses "R." consistently.
- The prose moves from the minute-18 "listen" blast to Pell's minute-20 call with a plain "Then" (l. 443–445). No interval is stated, but nothing contradicts one.

### 2. Toren's sighting and ownership: PASS

**Chapter 14 (l. 631–633).**
- At the fold he is looking up the track at the south lip. He sees the holder leave the hollow, takes Callie's sleeve, runs, and does not call it.
- Every physical detail matches the fight as staged:
  - he is at post five, just below the lip-to-bottom track;
  - the fog is knee-high at the lips (l. 349);
  - the holder shouts "*Weight!*" (l. 457–459);
  - he has Callie by the sleeve (l. 483).
- The old unattributed "a woman's voice" is now correctly "her voice". This agrees with l. 457.
- "Nobody else had been looking at her. Nobody ever was." stands as his belief, not as authorial fact.
- He learns what happened at the north lip only "afterward" (l. 449). This avoids a sight-line error, because he cannot see the north lip from post five.

**Chapter 15.**
- Toren's impossible report is gone. He now says only "I don't know… Three blasts went. She'll have come to the lip." (l. 285). He could infer that from the map, which put Dee at the gate.
- Jab's thought is narrowed to "nobody had seen her hit" (l. 93). That is true, and it is Jab's knowledge.
- The italic *nobody saw.* earlier in the same line is Jab's own belief from his viewpoint. It is not the ledger, and it does not break the requirement.

**Chapter 16 admission (l. 195–205).**
- It restates the ch. 14 facts exactly: *weight*, looking up the track, leaving the hollow, Callie's sleeve, did not call it.
- The emotional cost is kept physical and brief: the stitched right hand on the chair handle bleeds through at the seam, which is consistent with l. 87.
- Dee's answer and Jab's look follow.

**The ledger (l. 335–337, l. 351).**
- *NOBODY COUNTED HER.*
- *T. saw her leave the hollow at the fold. Did not call it.*
- *The runner calls anybody who leaves their place.*

The ledger no longer claims that nobody saw. The thesis is intact, and *COUNT THE HOLDER* is unchanged (l. 353).

### 3. Dee's arrival order and delay: PASS

**The rationale (ch. 14 l. 197).** "Two hundred paces is nothing to somebody running light", but she will have "the bag and the jars and two men with a stretcher", and she will stop for "the first hurt person I come to… Call it two minutes. In fog, three."
- This agrees with the map, l. 279: *Gate. 200 paces. D. W., kit, stretcher crew, stores* and *three jars clean Flask*.

**The arrival (ch. 15 l. 283–291).**
- The order is: Katori's kill, then "Where's the medic", then Toren's limited answer.
- Dee then comes "from the south", down the road from the lip, with the bag and two stretcher-bearers behind her.

**Her account (ch. 16 l. 187).**
- The order is: gate, then up the road with bag, jars and stretcher, then the weighbridge girl's wrist at the lip, then Wyck's "where's the holder" while she was splinting, then down.
- Its counterfactual, "two minutes longer", is about splinting time and does not contradict the ch. 14 travel estimate.

**The ledger (l. 343).** "Came at three blasts, with kit and stretcher. Did the girl's wrist first… Came down at Wyck's word."

Everything agrees with continuity sequence items 10–11. The overall interval before she reached the holder is longer than two minutes. The text explains that by the stop and by nobody having the holder on the count, which was the draft's own logic.

### 4. Day and count corrections and Dee's age: PASS

All of these were checked against the D+11–D+28 map:

| Location | On disk | Check |
|---|---|---|
| Ch. 13 l. 495 (D+20) | "Thirty-eight alone, three mornings ago" | The 38 s was measured on the yard's "third morning" (ch. 12 l. 3, l. 35–39), which is D+17. Correct, and not awkward arithmetic |
| Ch. 13 l. 535 | "the tally for six days" | She started D+14; this is D+20. Correct |
| Ch. 14 (D+22 argument) | "a week of the yard" | The yard opened D+15. Correct |
| Ch. 12 l. 495 (D+18) | "eighteen days" | Counted from D-0 night. Correct |
| Ch. 16 l. 447 (D+28) | "the day before yesterday" | The demonstration was D+26 (ch. 16 l. 103–149, "yesterday" = D+25 at l. 155/181). Correct |
| Ch. 10 (Director, D+13) | Breach kill on the south approach; "Two days later, with that arm already strapped", the north-road charge with struts and spike | Book One ch. 50 l. 169 breaks the left forearm on the crash rail at the Breach. M1 ch. 3 l. 11 has the north-road charge "two days after the Breach", with struts and spike. The two feats are now in order and plain. Correct under canon |
| Ch. 10 (Jab, D+13) | "the day after tomorrow's tomorrow", unchanged | That is D+16, Tonk's picture. Correct |
| Ch. 16 l. 125 | "since I was fourteen" | The bible fixes Kindling at 13, and Dee was 14 at Homura's fall (ch. 9 l. 443; ch. 15 l. 499). Vell was Homura's lead (bible l. 470). 14 + 11 years = about 25 (ch. 16 l. 193; ch. 9 l. 473). Canon-safe |

The extra corrections the report lists are also accurate:
- ch. 10 "two weeks" (D+13);
- ch. 13 "the jar Callie called thin at the weighbridge" (D+12);
- ch. 14 "six days ago" (D+19 to D+25);
- ch. 16 "less than four weeks left" (agrees with l. 415, "four weeks was a week ago");
- ch. 13 "Now the Ward" (keeps stage numbering 3/4 consistent with ch. 16 l. 111–115).

`Orrin Vell` is unchanged. Wyck's side and finger count are unchanged.

### 5. Dee references and the unnamed girl: PASS

**Each viewpoint has learned the name before using it:**
- **Toren:** ch. 9 l. 443–447.
- **Callie:** ch. 10 l. 539–541, "Miss Wren," said the Director / "Miss Wren, then." She was also at the fire where the name was told.
- **Jab:** ch. 10 is his office presence and the reunion. In ch. 11 the bridge is at l. 69.

**Forms follow the viewpoint.**
- **Toren and Jab** say *Dee*.
- **Callie** says *Miss Wren*.
- The remaining bare "the woman" tags in the ch. 11 and ch. 16 shed scenes follow a named scene entry, and they are the only unmarked adult female referent in speech.

**Ambiguities checked and found clear:**
- ch. 11 l. 229: "She looked at Dee", where Keel is the speaker;
- ch. 15 l. 289–311: Dee is now named at scene entry, and "the woman under their hands" is the holder;
- ch. 16 l. 187: Dee's own "the weighbridge girl".

**The weighbridge girl** has no name anywhere. No new name was introduced in any changed hunk. "Marsh" (ch. 14 l. 447) is canon, already used on the page by the Director (ch. 10 l. 535) and on the intake sheet.

### 6. Integrity of changed sentences: PASS

- **Grammar and meaning.** Every changed hunk in ch. 10–16 was read. None is grammatically broken, and none changes meaning beyond its stated purpose.
- **Pronoun across a break.** At ch. 14 l. 449, "kept them down" refers back to "hands" across a paragraph break. It is readable.
- **Power limits unchanged.** This covers:
  - the handover lapse;
  - Sustain's lean;
  - the hounds treating light as a fence (ch. 15 l. 271, "shied from it and slid");
  - Callie's 58 s to her floor;
  - Dee's settled Handful and unchanged floor;
  - Toren's one-breath Guard.
- **Objects unmoved.** This covers the cord, jars and bag, map, ledger, stone ("not taken it out to look at it"), plate, hook and sand-glass.
- **Injuries not reset.** Toren's right palm reopens and is stitched and wrapped (ch. 16 l. 87, 201, 421). His left arm stays in its sling. The girl's wrist is still broken. Wyck is unchanged.
- **Nothing reserved exposed.** There is no door count, third door, disk or Cinder material. Callie's "before Meridian" (ch. 13 l. 399) reveals nothing reserved.
- **Spatial logic intact:**
  - post five below the south lip;
  - the north lip 300 paces across (ch. 14 l. 393, 447);
  - the west door, pipe mouths and rim route;
  - Dee's gate, then road, then lip, then the slab.

**Structural check.** Every diff hunk is a change or an insertion. There are **no deleted lines** in any chapter.

### 7. Motifs and fight beats: PASS

**Motifs present:**
- fell like a sack (ch. 12–14);
- something left;
- write why;
- light where you don't want them (ch. 14–15);
- *COUNT THE HOLDER*;
- the cord and the bread;
- the hook, the bucket and floor;
- test weights / *thistle* (ch. 13 l. 535–595);
- the jam with three answers and two keys;
- the handoff count;
- the D+21 scan (ch. 13 from l. 591);
- the good-boots motif, kept as a callback (ch. 16 l. 419).

**Fight beats present and unshortened:**
- warm iron and two shadows;
- "Six!";
- the fold;
- three blasts;
- the dropped bag;
- the girl's correct fall;
- Jab lighting to call the husks;
- the hounds in the pipe;
- Callie's hook to 58 s;
- Toren's light fence;
- "She's worse";
- Toren's fall with the spike still lit;
- the holder one-handed, then her collapse;
- Rook's 31 minutes;
- Jab's nine minutes below his floor;
- the hounds' return and Toren's Stride fence;
- Katori's kill;
- Dee lifting Jab's hand off.

### 8. Repair report accuracy: PASS

**Files changed.**
- Ch. 9 is byte-identical to the frozen draft.
- Ch. 10–16 differ.
- The frozen edition was not touched.

**Word counts (`wc -w`).** Reproduced exactly:
- before 62,793: 7,554 / 8,376 / 7,365 / 7,122 / 8,920 / 8,958 / 7,350 / 7,148;
- after 63,115: 7,554 / 8,376 / 7,334 / 7,097 / 8,853 / 9,161 / 7,322 / 7,418.
- Ch. 10's net zero is real: its 16 changed lines sum to 0 words.
- The continuity length table and the new viewpoint shares (37.7 / 39.1 / 23.2%) match these figures.

**Changed lines, 0 / 16 / 17 / 8 / 23 / 36 / 13 / 31.** Reproduced. The ch. 14 and ch. 16 figures include blank separator lines.

**Quoted before and after text.** Every quotation in the Priority 1 and Priority 2 sections matches the disk.

**Tic counts.** Reproduced:
- "face did/was doing nothing", 6 → 3;
- "water off a plate", 4 → 2;
- Dee's four-second look, 4 → 2;
- "lamp in a draught", 3 → 2.

**Minor notes (not failures):**
- **"Good boots", 41 → 6.** This excludes the ch. 9 introduction, which the report treats separately. With it included, the lowercase count is 42 → 7.
- **Narration diagnostic.** It is not exactly reproducible from the description. The split rule is underspecified, and my approximation got 2,678/2,653 sentences with a ≤5-word share of 30.7% → 28.8%. It does agree in direction and size: the mean rises by about 0.2 and the short share falls by about 2 points. The report already calls it directional.
- **Continuity file and frozen edition are untracked in git.** I could therefore not independently confirm which rows of the continuity file changed, or the frozen edition's byte-identity beyond its README hash statement. The continuity file's current content agrees with the repaired manuscript on every point checked.

---

## Final verdict

**repair accepted**

No repair defects were found. None of the eight questions needs a targeted correction.

## Owner-only unresolved issues (not repair defects)

These were carried over from the repair report and verified as still open. Per its brief, the repair correctly left them alone.

1. **Wyck's injured side and finger count.**
   - Movement One and Movement Two: right collarbone and arm, the last two fingers numb.
   - Book One: left wrist, three fingers.
   - Unchanged in this pass.
2. **When Toren's arm broke.**
   - The repair prompt's premise, "broken on D-0", conflicts with Book One ch. 50 l. 169, which breaks it at the Breach.
   - The Director's new line is true under Book One and under the D-0 re-injury reading.
   - Ch. 9's "over eleven days the break… had settled" (l. 9) reads as the D-0 re-injury.
   - The owner should confirm which account governs.
3. **Tonk "flat… for ten weeks"** (ch. 15) against the map's six-week pattern. Planning-level, and untouched.
4. **Low-confidence distances.**
   - "Forty yards", from the west door to the holder.
   - Jab's "quarter of a mile" stretcher carry (ch. 16 l. 447).
5. **Length.** 63,115 words, about 15% over the packet's 48,000–55,000 band. Nothing was cut or padded, per instruction.
6. **Short-sentence share.** Still about 2 points above the 27.7% formula target. The report attributes the remainder to the fight, the counts and the ledger notation, and leaves it as an owner call.
