# Movement Six — consolidated same-author repair report

> Built by TAC

- **Author run:** Claude Opus 5.5 (`claude-opus-5-5`), the same selected manuscript author, writing as Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- **Brief:** `editor/MOVEMENT-006-REPAIR.prompt.md`, including its owner/orchestrator rulings.
- **Method:** one continuous session. No subagents, no Agent tool, no skills.
- **Reading order:**
  1. `manuscript/chapter-41.md` … `chapter-48.md` in full, in order;
  2. `editor/MOVEMENT-006-COLD-READ.md`;
  3. `editor/MOVEMENT-006-EDITORIAL-REVIEW.md`;
  4. `provenance/MOVEMENT-006-CONTINUITY.md`.
  - I also read `manuscript/chapter-39.md` lines 85–105 (Callie's knees going with the Ward still fixed in the steel) to anchor the Priority 2 bridge. I grepped chs 1–48 for "Marsh", "disk" and "Satori" to settle the six-line names and the disk's prior Book Two appearances.
  - `provenance/MOVEMENT-005-CONTINUITY.md` and `packets/MOVEMENT-006.md` were not needed.
- **Scope:** only the three priorities and the owner rulings. After the edits I read the repaired movement once, in order. That read found four small problems introduced by the repair, and I fixed them (§6). I did not open a broader pass.
- **Disclosure:** the session began with automatic memory summaries of the drafting and review runs. This repair was made by the same model that drafted the movement and wrote both reviews. Nothing here is an independent check.

## 1. Files changed

| File | Change |
|---|---|
| `manuscript/chapter-41.md` … `chapter-48.md` | Sentence- and passage-level repairs, listed in §3 |
| `provenance/MOVEMENT-006-CONTINUITY.md` | Updated to the repaired page (§5) |
| `editor/MOVEMENT-006-REPAIR-REPORT.md` | This file (new) |
| `AUTHORSHIP.md` | Movement Six status changed from first draft to repaired, with acceptance pending the recheck (§8) |

**Not touched:**
- the frozen edition `editions/movement-006-first-draft/`;
- the cold read, the editorial review and all prompts;
- the packet, the map and the bible;
- chapters 1–40 and all other books.

**Frozen-edition check.** After the last edit I hashed all eight frozen files with `shasum -a 256` and compared them with the table in `editions/movement-006-first-draft/README.md`. **All eight match.** For example, `chapter-41.md` is still `746bf389…5696d` and `chapter-48.md` is still `2874a543…c750c`. The frozen files' modification times are unchanged (02:43–02:44). A `cmp` of each repaired chapter against its frozen copy reports a difference for all eight, as expected.

## 2. Word counts (`wc -w`)

| Ch | POV | Before (frozen) | After | Δ |
|---|---|---:|---:|---:|
| 41 | Jab | 7,541 | 7,543 | +2 |
| 42 | Toren | 5,061 | 5,078 | +17 |
| 43 | Callie | 7,133 | 6,984 | −149 |
| 44 | Jab | 4,530 | 4,667 | +137 |
| 45 | Toren | 6,994 | 7,065 | +71 |
| 46 | Callie | 5,299 | 5,377 | +78 |
| 47 | Jab | 5,294 | 5,141 | −153 |
| 48 | Toren | 5,470 | 5,453 | −17 |
| **Total** | | **47,322** | **47,308** | **−14** |

- **Book Two total:** 317,695 (was 317,709). Owner ruling: the length is accepted.
- **The net change is smaller than the brief's "roughly 150–500 words" reduction.**
  - The Priority 2 bridges needed about +480 words:
    - Jab's corroborated onset, its cost and the fallible cue (ch 44);
    - Callie's ch 39 link and controlled release (ch 45);
    - the blood check (ch 46);
    - the disk reintroduction (ch 42).
  - The Priority 3 compressions removed about −500 words:
    - the ch 47 recital;
    - ch 43's restated body, jar and ration check-ins;
    - pause-phrase thinning;
    - two restatements in ch 44.
  - I made further local trims only where the text restated state it had just given. I stopped short of cutting any developed scene, patient action, fight adaptation or payoff, as the brief forbids. The movement is therefore about level rather than a net reduction. I report this as a deviation (§7).
- **Viewpoint (Movement Six):** Toren 17,596 (37.2%), Jab 17,351 (36.7%), Callie 12,361 (26.1%). **Cumulative, chs 1–48:** Toren 34.0%, Callie 33.2%, Jab 32.8%. No viewpoint scene was moved or added (owner ruling).

## 3. Exact changes, by priority

### Priority 1 — every count, place and clock now agrees

| Item | Where | Before | After |
|---|---|---|---|
| Meal after D+51 supper | ch 43 | "Eleven cups… Three nights and two cups" | "Eight cups… And a bit. Fourteen yesterday, before the pot. Three last night. Three tonight." / "Two nights and two cups" |
| Meal after D+52 supper | ch 43 | "Eight cups" | "Five cups" |
| Meal after D+53 supper | ch 43 (after the wedge) | no meal shown | "They ate there, at the halt, three cups for six." / "Two," said Callie, at the sack. "Two, and the dust." |
| Meal on D+54 | ch 43 | "Two cups… That's the last" | unchanged; now supported by 14 → 11 → 8 → 5 → 2 |
| Siding camp | ch 43 | camp "east end", Callie "at the west end" | both **east end**. The approach line now reads "came to the west end of it again, going the other way" |
| Jars on D+55 | ch 44 | "Five jars and a dirty one and two empties" | "Four jars with clean ash in them, and the dirty one, and two empties." Callie's nearby tally was checked (¼, 7½, 5, 8) and needed no change |
| Empties on D+58 | ch 48 | "the empties, six of them" | "five of them" (the four frame empties plus the road jar) |
| Ward beds | ch 47 | "Four beds on the right. The fourth had Senna… The fifth had Tonk." | "The fourth bed on the right had Senna in it… The fifth had Tonk." Tonk's bed and rail are unmoved |
| Home-Flask weighing | ch 46 | "I'll weigh them in the morning. Your three." | "I'll weigh your three when they let them out of the shed… At the plate, with the test weights on first." |
| | ch 47 | "Tilda weighed them this morning… She said they were hers." / "So the store's had thirty-five back" | "Tilda weighs them tomorrow… At the plate. Her own knots on the stoppers." The Director's past-tense line is removed with the recital compression |
| | ch 48 | the weighing at the plate | unchanged: **the only weighing**, on D+58 |
| Tonk's chair | ch 47 | "This morning. After the chair." / "all night, and in the morning while Tonk did the chair" | "Yesterday. After the chair." / "two nights, and while Tonk did the chair". There is one transfer only, on D+56 |
| Surge onset | ch 44 | Dessa: "It came up at noon" / "Since noon? Forty" / "since noon" (×2) | "at the fourth hour" throughout. It is observed on the page at the culvert by the wall at the fourth hour (P2) |
| | ch 45 | "sick at the fourth hour"; "since noon" (×2) | "sick inside an hour of it coming up"; "since the fourth hour" (×2) |
| | ch 46 | Tilda "sat down at the fourth hour when the fog came up" | unchanged (now agrees) |
| | ch 41 | "It's been down since the fourth hour" (said at dawn) | "since the middle of the night", so "the fourth hour" means late morning in this movement only |
| | ch 46 | "At the fourth hour the two orderlies came" (after Sowerby's "This afternoon") | "After noon the two orderlies came" |
| Ch 48 hour sequence | ch 48 | weighing "the third hour of the morning"; Senna lifted "at the third hour"; lane at the fourth hour; Toren arrives "at the end of the morning" | weighing "the third hour, a grey morning"; Senna lifted "at the fourth hour, when the lanes began"; Toren arrives "at noon, when the lane broke" |
| Lateness | ch 45, ch 46 | "Four days" (Toren; Tilda) | "Two days". The machine-cycle lateness ("a day past the cycle", "a day late") is untouched and stays separate |
| Callie's reading | ch 46 | "I read about fifteen… At a hand." | "I read about fifteen boxes… At a hand's width." |
| Units | ch 45 | "It came up to thirty feet" | "thirty paces" |
| Six lines | ch 45 | "*E. Marsh. D. Wren. P. J. C. T. Voss.*" and "*K. I. O. …*" | "Rook first, as *E. Marsh*, the name Hallet had for him. Then Dee, *D. Wren*. Then Pell, and Jab, and Callie, each by the one letter she had always written for them. Toren last, *T. Voss*." / "Katori. Ines. Otto. *The weighbridge girl.* … Wyck, *cleared tomorrow*." |
| Dee's term, as Jab states it | ch 47 | "when they're off their fourteen days" (the Director had just written twenty) | "when they're fit to be" |

The **96 lent / 61 spent / 35 returned** ledger and the **10½-Handful** wash cost are unchanged. No figure in them was touched.

### Priority 2 — capability beats bound to established limits

**Jab (chs 44–45, with echoes in 47).**
- **Restaged onset.**
  - At the fold (second hour) he feels the ditch grey "lying", cold, wanting nothing.
  - At the culvert by the wall (fourth hour), Callie's counter goes 12 → 20 → 26 "at nothing", and the whole ditch-bottom visibly slides south. Only then does he feel it.
  - What he feels is not a person but "the ground's grey. All of it. South", a moving field "the way water goes to a drain". The text says outright that this is not the one-man "lean at a mile" of the forty-third.
- **External corroboration** comes before anything depends on it:
  - Callie's counter and the sliding ditch at onset;
  - "Thirty… And back to twenty" at the first push;
  - Callie as the named back-up caller in Toren's orders ("And you call every one he doesn't").
- **Cue replaced.** "Two breaths" is gone in every instance (chs 44, 45). The field now "gathers" — "a small hard load under everything", then pushes, "A breath, mostly".
  - It fails on the page: "Twice he said it and nothing came. Once it came and he had not felt it gather at all, and Callie said *thirty* before he knew."
  - He calls the mid-drop push late in ch 45 ("Now—" said Jab. He had it late.), and Callie calls it as well.
  - Toren's report across the bowl reads: "Jab can feel it gather before a push. Most times. A breath." Dessa answers "*Most times?*"
- **Cost.**
  - The skin round the white place goes hot to the wrist, and his stomach turns.
  - Dee measures him and finds the floor "come up. A finger and a bit. You've drawn nobody… That's what that costs. Feeling it." She orders "Hand off your coat". His later measure repeats the raised floor and a hot palm.
- **Range.**
  - In the last mile he feels only "knots" where grey catches on bodies. He can name only Otto ("I think"), whose weight he knows, and a still place the field "goes round" (Dee: "That'll be Dessa").
  - From the north lip (300 paces) he feels individuals.
  - Ch 45 "I felt you from two miles" became "I felt it go round you, from the road." Ch 47 "felt the Sag from two miles off" became "felt the watch across the Sag."
  - No permanent range and no third door are stated.

**Callie (chs 43, 45, 46).**
- **Ch 43, washout.** "The lee wanted her whole body behind it, the way a door did, the way it always had" became "She had set herself behind the lee the way she always stood to a door, braced, the whole of her leaning in." The failure is now her habit, not the Ward's nature.
- **Ch 45, the bridge to ch 39** replaces "The steel holds it… Not me.":
  > "On the hill it stayed in the steel… When my knees went. It held a breath with nothing of me behind it, and I went down onto it. I thought that was the falling… It wasn't the falling. It was the steel. This time I'm putting it there."
- **Breadth.** "It was over all of them at once, cart and horse and people, not a door with her behind it."
- **Controlled release.**
  - "The lee went out" became "She let the lee down. She did not drop it. She brought it in off the road the way you pay a rope back through your hands, the lean-to coming upright, and shorter, and then out."
  - Her own words: "I put it there, and it held, and I let it down when I said."
- **After the hold.** "I thought I did… My whole life" became "On the hill my knees chose it. At the washout I forgot it. I stood behind it, the way I always stand to a door… I don't have to."
- **Price.** Her ribs and "all the half, and some of mine" are unchanged.
- **Ch 46, to her mother.** "I found out" became "I'd seen it on the hill and not known it… I know it now."
- **Blood (ch 46).**
  - Keel listens to her back, left and right, and makes her breathe and cough. He looks in her nose by lamp: "Nose. Burst at the floor. That's your blood. The lung's clear."
  - He wipes her lip and chin — "that was the end of the blood" — and then re-straps her ribs.

**The disk (ch 42).** On the slope above the wash, Toren's hand goes to his shirt:
> "Under it, on its cord of boot-lace, lay the disk his father had worn and his grandfather before him: near black, two thumbs wide, nine fine grooves on each face, cold. He had carried it under the shirt all the way out and into the hill and across the wash, because his father had said to, and he had not once thought about it. He took his hand away."

This comes before the ch 46 socket and the ch 48 recognition. No origin, Maker, Satori link or meaning is added. `released to bearer` stays a clue only.

### Priority 3 — final read-aloud cadence

- **The ash account.**
  - The ch 46 reconciliation to Tilda (the first necessary one) is kept.
  - The ch 48 public board is kept whole.
  - The ch 47 recital is compressed to what the terms scene needs. Callie gives "Lent, ninety-six… Back, thirty-five. The fence's eleven, and home, twenty-four… Home, not touched", then "Twenty-eight clean, off the floor of the first room. All spent, on us and your watch. None left… And four dirty. Never used." The Director does the arithmetic herself ("Sixty-one Handfuls…"). The narration now says why the recital is short: "It was on the paper, every halt, and the Director had just read the paper."
- **Ch 43 road check-ins.** Removed:
  - a second statement of Callie's carrying limits;
  - the recap of Pell's D+42 washout crossing;
  - the rain-day restatement of everyone's positions on the cart;
  - Rook's re-told last paper;
  - Pell's repeated "Say it at every halt";
  - the D+54 full jar inventory, now only what changed: "The lifter's first, a quarter. My first, seven and a half. Settled: a Handful in Toren. Half in me… Meal, none.";
  - the D+54 name-by-name count, now "Six… And a horse."
  
  Kept: the days, the machine's ninth hour, "half a cup", Toren reading the road, the washout's six breaths, "cheaper than a wheel" and every culvert number.
- **Ch 42 and 44 restatements.**
  - The cart-loading and Pell-on-the-cart paragraphs were tightened.
  - In ch 44, Toren's second long look at the Sag, the second list of what lies beyond the fog, and the separate "fourth, fifth" split in the jar tally were cut. Toren's sum was shortened.
- **Pause phrases in chs 45–48** (the recurring "for a long…" and "did not say anything" pauses).
  - "for a long time / moment" and "for a moment" fell from 30 to 15. "Did not say anything" fell from 12 to 6.
  - Four "the way…" frames in ch 45 were cut or merged.
  - Kept: Tonk's "for a long time in the dark", Dessa over the six lines, Jab's silence at the table, and the Director before "Nobody asked you for that".
- **Attribution.** "He looked at Jab. 'Callie. Every one he doesn't.'" became "He looked past Jab at Callie. 'And you call every one he doesn't.'"

## 4. Owner rulings — compliance

| Ruling | On the page |
|---|---|
| Length accepted; no scene cuts to hit range | No scene was cut; −14 words net |
| Three-protagonist balance accepted | No viewpoint moved or added |
| Plain voice; no restyle | Local cadence edits only |
| Front-loading accepted | Not addressed; no manuscript slot |
| Sag surge causally unproven | No mechanism is stated. The onset is observed (the ditch moves south; "the same shape. That's all anybody can write" is kept) |
| Jab: no general two-mile sense, no prophetic two-breath warning | Restaged as above: an anomalous moving field, corroborated, costly, fallible |
| Callie: intentional control and shared scale, not first discovery | Linked to ch 39; framed as choice, breadth and controlled release |
| Late disk clue accepted; reintroduce the disk first | Ch 42 carried-object beat; the clue is unchanged |
| Home Line accepted | Unchanged |

**Preserved as required:**
- the wash crossing in pieces, the post bridge, 10½, Duchess and Pell with the home Flasks;
- the five-day pressure and the late machine cycle;
- Dessa's command and "Everybody back";
- the full return hold (Callie holding, Jab rotating and stopping, Toren's single-configuration Guard/Edge, Katori and the home cohort);
- no deaths and no miraculous recovery;
- the 110 box calibrating, with the 106 kept as proof;
- Tonk's agency and "supper first", Tilda's state and Senna's course;
- 61 written as the machine's cost;
- the breach censure, the two year terms and Jab's own terms;
- the board, the untouched Flasks, the Home Line, the same watch, the three lanes and the append-only ledger;
- one disk clue and one Cinder trace.

## 5. Continuity checkpoint updates

`provenance/MOVEMENT-006-CONTINUITY.md` now carries a repair-status note, and every changed item is marked *(repaired)*:
- the disk resolution row (ch 42 reintroduction);
- Food (the counts 14/11/8/5/2 with their moments);
- husk lines (the fold "lying"; the fourth-hour culvert onset);
- the Sag onset (the fourth hour);
- Jab's push sense (rewritten to the ruling: field, corroboration, cost, fallible cue, no range gain);
- Callie's correction (ch 39 link, choice, breadth, release);
- the six lines (the spoken form);
- the day map for D+50, D+51, D+52 (east-end camp), D+53, D+55, D+56, D+57 (afternoon scan, short recital, "Yesterday"), D+58 (the only weighing) and D+59 (lane clock);
- the word and viewpoint tables;
- return-hold entry floors, the cue, the late call, controlled release, "thirty paces", the big-push line and the nosebleed;
- the ledger note (single weighing; the recital split);
- Jab's and Callie's body states;
- the frame's jars and the five empties;
- Jab's terms ("when they're fit to be");
- the surge cause listed among withheld truths;
- the phrase counts.

## 6. The final read

After the edits I read chs 43, 44 and 45 in full and in order from disk. Chs 41, 42, 46, 47 and 48 had been read in full at the start of the session, and I re-read every repaired passage in them in context. The read found and fixed four problems the repair had introduced:
1. **Ch 43:** the new D+53 supper was cooked "on the last of the thorn root", but thorn feeds the D+54 fire. The phrase was cut.
2. **Ch 45:** "He was sick inside the hour" was ambiguous. It now reads "sick inside an hour of it coming up".
3. **Ch 45:** the audible six-line list skipped Dee's written form. It now reads "Then Dee, *D. Wren*."
4. **Ch 46:** the new blood check left "She did not sleep much" opening the ward scene, ahead of the sleep it describes. That opening was reworded to "In the ward, Keel looked at her first."

I found no blocking contradiction beyond these.

## 7. Unresolved and owner-only

1. **Net length.** The movement is −14 words, not the brief's 150–500 reduction, because the Priority 2 bridges cost about as much as the Priority 3 cuts saved. Further cuts would have to come from developed scenes, which the brief forbids. It is owner's call whether to accept this or to ask for a separate trim.
2. **The book-wide hour convention.** The ruling makes "the fourth hour" late morning, and ch 44's "the fifth hour, in the afternoon" agrees. However, ch 43 keeps "the ninth hour" as "the hour of the morning lift" (Senna's shed slot, established in earlier movements). On a daylight count the ninth hour would be mid-afternoon. I did not change it, because it is earlier-movement canon and outside this repair. It needs one book-level ruling.
3. **"four feet" (ch 48).** "…on a gravel bar at midnight, four feet from a disk on a cord" appears to echo Book One and was left as written. The brief named one isolated unit; this second one is flagged, not changed.
4. **The surge cause** stays withheld by ruling. The map's "caused by the distant rip's collapse" is not asserted.
5. **Jab's sense after the book.** The page now limits the Sag event to the anomalous moving field. Whether he ever reads a field that way again is left to Book Three planning.
6. **Unchanged, as ruled:** Callie's 26% share this movement, the front-loading, and the Flesch and sentence-length departures from the formula.

## 8. Status

- The manuscript repair is complete for the three priorities.
- The continuity checkpoint matches the repaired page.
- `AUTHORSHIP.md` Movement Six is updated to **repaired**. **Acceptance is pending the targeted recheck.**
- The frozen edition is untouched and hash-verified (§1).
