# Movement Two ("The North Yard", chapters 9–16): same-author repair report

## Identity and method

- **Model:** Claude Opus 5.5 (`claude-opus-5-5`), the selected manuscript author. Public byline Monroe Jackson; seat Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- **No subagents.** No prose was delegated or drafted by any subagent or other model. All edits were made in one session.
- **Reading done before any edit:**
  - chapters 9–16 in order
  - both editorial reports
  - the continuity checkpoint, the packet and `BOOK_MAP.md`
  - `UNIVERSE_BIBLE.md` and both name registries
  - `VOICE.md` and `FORMULA.md`
- **Canon checked for the arm question:** Book One ch. 50, and Movement One chapters 1 and 3.
- **Scope:** a focused repair of the existing text, not a rewrite. No scene was cut or added. The Sag fight (ch. 14–15) keeps its full length, all of its tactical changes and all of its costs.

## Files changed

- `manuscript/chapter-10.md` through `chapter-16.md`, edited in place.
- `manuscript/chapter-09.md` was read and left unchanged. None of its lines needed any of the three repairs.
- `provenance/MOVEMENT-002-CONTINUITY.md`, factual corrections only:
  - two new resolution rows
  - the D+26 day row
  - the Dee position note
  - the renumbered failure sequence
  - the ledger object state
  - Toren's exit state
  - the length table
- `editor/MOVEMENT-002-REPAIR-REPORT.md` (this file).

Not touched: the frozen edition (verified byte-identical to the pre-repair chapters), the reviews, the packet, the map, the name registries and Book One.

---

## Priority 1: the Sag failure's causal chain

### The line handover (ch. 14; ledger in ch. 16)

**What happens now:**
- At minute 18, Toren shouts "Six!" and Pell blows one *listen* blast. A new beat follows that blast:
  - Pell calls "Minute twenty. Holder, do we change?"
  - The day holder refuses from her hollow: "Not with six moving… I let go to hand it over, there's a gap, and the gap's on six. I've got it down. I'll keep it."
  - She then shouts across the dip: "*Keep your hands down, Marsh.*"
- From post five, Toren cannot see the north lip. He learns afterward that Rook kept his hands down and that nobody said when they would try the change again.
- The fold comes at minute 21, one line later.

**Why the refusal is physically plausible:** the bible says a lapse of seconds lets something through. Here the lapse would open exactly on the moving slab.

**How the ledger names it:** the ledger now reads "Minute nought to minute eighteen: lift as planned", followed by:

> *Minute twenty: change of holders called — P. Holder kept the line with six moving; R. kept his hands down. No new minute set.*

*What to change* gains:

> *If the change can't be made on the minute, somebody says out loud who's holding and when we try again.*

### Toren's sighting (ch. 14; ch. 16)

**Chapter 14:** the sighting is kept and made a failure he owns.
- When the ground spoke, he was looking straight up the track at the south lip. He saw her leave the hollow and go down alone toward the corner.
- Then he took Callie's sleeve and ran, "and he had not called it to Pell or to Katori or to anybody. He was the runner."
- It closes: "He had been, and he had said nothing, and now Jab was going to her in the dark on his own."
- "Nobody else had been looking at her. Nobody ever was." is kept as his belief.

**Chapter 16, the shed on D+26:** after Rook and Dee's exchange, Toren says it plainly, standing behind the wheeled chair. He saw her go, he didn't call it, and he was meant to know where everybody was.
- **The cost is shown physically:** his stitched hand closes on the handle and a red spot comes through the new wrapping.
- **Dee answers flatly:** "Then you saw her, and I was two hundred paces off with a stretcher, and we both got to her after Jab did."
- **Jab** looks up at him and does not look away.
- **Dessa's "Write it down"**, spoken in Senna's voice, now answers Toren's admission.

**The ledger:**
- The capital line is now: *THE HOLDER WAS HIT AT THE FOLD, IN THE FOG. NOBODY COUNTED HER.*
- A plain entry follows it: *T. saw her leave the hollow at the fold. Did not call it.*
- *What to change* adds: *The runner calls anybody who leaves their place.*
- Rook's closing *COUNT THE HOLDER* and Senna's dictated *why* are unchanged.

**Chapter 15 (Jab's viewpoint):** Jab's thought "nobody had seen any of it" now reads "nobody had seen her hit". That is still true, because Toren saw her leave the lip but not the blow.

### Toren's impossible report (ch. 15)

- **Before:** "Coming… Dessa sent her. Wyck asked where the holder was. Nobody had her on the count."
- **After:** "I don't know… Three blasts went. She'll have come to the lip."
- **Who supplies the rest:** Dee, correctly positioned, in her ch. 16 account: the three blasts, stopping at the lip for the girl's wrist, nobody having the holder on the count, and Wyck's "where's the holder".

### The two-hundred-pace delay (ch. 14; ch. 16)

**Chapter 14:** Dee's argument now says why it takes two minutes:

> "Two hundred paces is nothing to somebody running light. I won't be running light. I'll have the bag and the jars and two men with a stretcher, and I'll stop for the first hurt person I come to, because that's the job. Call it two minutes. In fog, three."

**Chapter 16:** her account now follows the same order.
- She came up the road "with the bag and the jars and two men carrying a stretcher, which isn't the same thing as running".
- She stopped at the lip for the weighbridge girl's wrist.
- "If Wyck hadn't said *where's the holder* while I was splinting, I'd have been on that lip two minutes longer."
- Her ledger entry adds "with kit and stretcher".

---

## Priority 2: the clock and canon slips

| Location | Before | After | Basis |
|---|---|---|---|
| Ch. 13, widening scene (D+20) | "Thirty-eight, alone… Yesterday." | "Thirty-eight alone, three mornings ago" | The 38 s was measured on D+17 |
| Ch. 13, weighbridge | "the tally for three days" | "the tally for six days" | She started D+14 ("short a tally from tomorrow" on D+13) |
| Ch. 14, argument (D+22) | "ten days of the yard" | "a week of the yard" | Yard opened D+15 |
| Ch. 12, steps (D+18) | "in seventeen days" | "in eighteen days" | They met on D-0 night |
| Ch. 16, steps (D+28) | "yesterday she did a quarter of a Handful" | "the day before yesterday…" | The demonstration was D+26 |
| Ch. 16, Dee | "since I was eleven" | "since I was fourteen" | Kindling is fixed at 13 and she was 14 at Homura's fall, so this is her Homura months under Vell. It keeps Rook's ch. 15 line true: at fourteen she did not know how to hold up *another* body |
| Ch. 10, the Director | "killed a Breach… with your arm broken… two days later you did the same thing with your legs" | "You killed a Breach on my south approach, which nobody on my register has ever done. Two days later, with that arm already strapped, you ran at a pack of hounds on the north road with your struts and your spike both going at once, in front of half my gate crew." | Two feats, in order, in plain words. See the owner note below |
| Ch. 10, Jab | "the day after tomorrow's tomorrow" | **unchanged** | Spoken on D+13: tomorrow is D+14, the day after is D+15, and the day after that is D+16. That is correct, and it is Jab's voice |

These fixes go slightly beyond the listed items. All of them are the same class of error, and all are line-level:

| Location | Before | After | Basis |
|---|---|---|---|
| Ch. 10 | "I've known them twelve days" | "two weeks" | D+13: Callie since D-1, Jab since D-0 |
| Ch. 13, stage 3 (D+20) | the thin Flask was "the day before yesterday" | "the jar Callie called thin at the weighbridge" | That call was D+12 |
| Ch. 14 | the fence rail "five days ago" | "six days ago" | The jam was D+19 and the lift D+25 |
| Ch. 16 | "four weeks in it, and less since yesterday" | "less than four weeks left in it" | The technician's warning was not dated to yesterday |
| Ch. 13 | `"Four," said the woman… "Callie. Stand in it."` | `"Now the Ward," said Miss Wren` | Stage four is *settle*. The review flagged the reused numbering as a clarity slip |
| Ch. 14 | Toren "had not taken [the stone] out since the glass" | "…had not taken it out to look at it since the glass" | Removes the cold read's contradiction with the spike scenes in ch. 12–13 |

`Orrin Vell` is unchanged. Wyck's injured side is unchanged.

---

## Priority 3: cadence and references

**References to Dee**

"The woman with the good boots" went from 41 uses to 6.

Kept:
- all the uses in Callie's ch. 10 office scene before she hears the name;
- the new bridge in ch. 10, "The woman with the good boots uncrossed her ankles. Miss Wren, then.";
- the ch. 11 bridge, "Dee Wren, the woman with the good boots, was sitting…";
- one comic callback in ch. 16 (Jab's blankets).

Ch. 9's introduction and Callie's "Good boots" track-reading are untouched.

Replacements follow each viewpoint:
- **Toren and Jab** say *Dee*.
- **Callie** says *Miss Wren*, the Director's form, which is the one she heard first.

A few bare "said the woman" tags became *Dee* or *Miss Wren* where another woman was in the scene. In ch. 15 this matters most: "the woman" had meant both the holder and Dee in the rescue. The scene entry "She came out of the fog" is now "Dee came out of the fog". In Dee's ch. 16 account, "a girl" is now "the weighbridge girl".

**The weighbridge girl** stays unnamed throughout.

**Tics thinned**

| Tic | Before | After | Kept |
|---|---:|---:|---|
| "face did/was doing nothing (at all)" | 6 | 3 | Dee in ch. 9; Toren "which was how Callie knew" in ch. 10; the closing callback in ch. 16 |
| "like water off a (tipped) plate" | 4 | 2 | Ch. 12 and the Ward-walk in ch. 13 |
| Dee's four-second observation look | 4 | 2 | The first, in ch. 9, and at the holder in ch. 15 |
| "like a lamp in a draught" | 3 | 2 | Ch. 13's use cut |

The structural "four seconds" lines are kept: the Director's lapse, Rook's "A shout's four seconds", and Tilda's word gap.

**Combining fragments.** About forty adjacent fragments that carried one thought were joined with commas, semicolons, colons or dashes. Examples:
- "Across was the bottom of the dip, in the fog, where the line was."
- "He was looking east, across the fog, at the bottom of the Sag where the line was…"
- "Husks came at anything worked, anything lit."
- "Not far, at first: a lean, the old lean…"
- "It was the sound his father had made—exactly the sound…"

**Kept as deliberate impacts:**
- the fight beats: "Hounds. In the pipe. Where the husks had not gone."; "It threw two."; "The spike was still lit."
- the counts: the handoff gaps, the breath minutes, "Three. Three cycles, maybe. Then a guess."
- the ledger notation
- the long action sentences

No breathing commas were added between a subject and its verb.

**Motifs verified present:** fell like a sack, something left, write why, light where you don't want them, COUNT THE HOLDER, the cord, the bread, the hook, the bucket and floor, the test weights, the jam and its two keys, the handoff count, *thistle* / *test weights*, and the D+21 scan.

---

## Measurements

### Word counts (`wc -w`)

| Ch | Before | After | Change |
|---|---:|---:|---:|
| 9 | 7,554 | 7,554 | 0 |
| 10 | 8,376 | 8,376 | 0 |
| 11 | 7,365 | 7,334 | −31 |
| 12 | 7,122 | 7,097 | −25 |
| 13 | 8,920 | 8,853 | −67 |
| 14 | 8,958 | 9,161 | +203 |
| 15 | 7,350 | 7,322 | −28 |
| 16 | 7,148 | 7,418 | +270 |
| **Total** | **62,793** | **63,115** | **+322** |

The net gain comes from three causal beats that Priority 1 required: the handover exchange, the owned sighting, and the shed admission plus its ledger lines. The epithet and fragment work reduced every other chapter.

Changed lines per chapter against the frozen text: 0 / 16 / 17 / 8 / 23 / 36 / 13 / 31.

### Narration-only sentence diagnostic

This is my own script, reproducible from this report.
- **What it measures:** paragraphs that open with a quotation mark are excluded. Sentences are split at `.!?` followed by a capital letter.
- **What it does not exclude:** dialogue embedded inside narration paragraphs stays in. Treat the results as directional.

| | Sentences | Mean | Median | Share ≤5 words | Share ≥40 words |
|---|---:|---:|---:|---:|---:|
| Before | 2,714 | 14.76 | 9 | 31.5% | 7.7% |
| After | 2,691 | 14.96 | 9 | 29.7% | 7.7% |

**By chapter,** the ≤5-word share moved as follows:

| Ch | Before | After |
|---|---:|---:|
| 10 | 31.5% | 28.0% |
| 11 | 27.2% | 24.8% |
| 13 | 31.8% | 29.8% |
| 14 | 38.9% | 35.2% |
| 15 | 36.0% | 35.2% |
| 16 | 35.5% | 33.9% |

**Against the formula's targets:** the target is 14.6 words mean and 27.7% at five words or under. The mean now sits just above target. The short share is still about 2 points high.

The remaining excess is concentrated in:
- the fight in ch. 14–15
- the counts
- Dessa's ledger notation

I judged these purposeful and did not flatten them. Whether to push further there is an owner call.

---

## Left for the owner

1. **Wyck's injured side and finger count.** Unchanged. Movement One gives right collarbone and arm, two numb fingers. Book One gives left wrist, three fingers.
2. **When Toren's arm broke.** The repair prompt said D-0. Book One ch. 50 breaks the left forearm on the crash rail at the Breach, and M2 ch. 1 has it strapped before D-0; he then lands on it on the D-0 slabs. The Director's line is worded to be true under both accounts ("with that arm already strapped"). Ch. 9's "eleven days" and ch. 12's "the noise… on the slabs" still read naturally as the D-0 re-injury. If the owner wants a single account, rule on this.
3. **Tonk "flat… for ten weeks"** (ch. 15) against the map's "six-week pattern". Plan-only. Not touched.
4. **Low-confidence distances not touched:** "forty yards" from the west door to the holder, and Jab's "quarter of a mile" of stretcher carry.
5. **Length.** Still about 15% over the packet band. As instructed, nothing was cut for length.
