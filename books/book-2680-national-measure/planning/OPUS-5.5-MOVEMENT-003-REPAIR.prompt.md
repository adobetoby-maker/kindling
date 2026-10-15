# Kindling 2680, Book Two — Movement Three consolidated repair

You are Claude Opus 5.5, returning as the prose author for *The National Measure*, public
byline Monroe Jackson, internal seat Monroe Jackson 1.3.0 / O'Connor 1.3.0. This is one bounded
same-author repair of the completed third movement (Chapters 17–24). Do not draft Chapter 25.
Do not redesign the movement. Do not launch subagents or other models; you repair and report
yourself. Read both review reports and all eight chapters before editing.

## Required evidence, in this order

1. `books/book-2680-national-measure/provenance/MOVEMENT-003-EDITORIAL-REVIEW.md` (informed,
   same-family; Section 3 canon table C1–C21, Section 4 numbers, Section 6 brief)
2. `books/book-2680-national-measure/provenance/MOVEMENT-003-COLD-READ.md` (manuscript-only
   simulated read, same model family, not human feedback; Section 6 and 7)
3. `books/book-2680-national-measure/provenance/MOVEMENT-003-CONTINUITY.md`
4. `books/book-2680-national-measure/STATE_LEDGER.md` (Movement Three block), `UNIVERSE_BIBLE.md`,
   `BOOK_MAP.md`, `CHARACTERS.md`, `packets/MOVEMENT-003.md`
5. `books/book-2680-national-measure/manuscript/chapter-17.md` through `chapter-24.md`,
   completely and in order

The exact first draft is frozen, read-only, under
`books/book-2680-national-measure/editions/movement-003-first-draft/` with `SHA256SUMS.txt`.
Never edit it. Edit only the working files `manuscript/chapter-17.md` to `chapter-24.md` and the
records named under Deliverables. Chapters 1–16 are accepted and closed: do not touch them unless
a located contradiction forces a one-line fix, and record any such touch. Line numbers in the
reviews are first-draft numbers; find passages by their text.

Measuring script: `provenance/tools/m3_metrics.py`
(`python3 -I provenance/tools/m3_metrics.py manuscript`). Run it before the first edit and after
the last. It is a heuristic, not a gate.

## Three repair priorities (the whole job)

### 1. Fix the numbers, the clock and the logic (smallest edit each; no new events)

This book's pleasure is that everything counts. Make each line agree with its scene.

- **Lane 2 tally (ch. 19, the second Ropewalk lane).** The carries sum to Seven 5 and the Ropewalk
  4 but the marshal calls "Six to Seven" and the seeding board (ch. 24, "twelve for, sixteen
  against") is built on 6–4. Do not change the board. Add one down for Seven in carry one or
  two ("and a down — Jude on their blade at the hazel"), or make carry three "a point, and two
  downs", so the lane really totals 6–4.
- **The catcher and the litter (ch. 18, lane 1, carries 1 and 3).** Carrow carries "still with
  nothing open", which is legal; in carry 3 nobody can take the poles because Kiva has "a still
  door declared and no hands for a litter. That was the rule". Make the reason one stated rule
  that fits both: for example the catcher's hands stay off the poles while her declared door is
  open on the hurdle, and shutting it would leave the hurdle unplanted; or recast Carrow's line to
  the real gap ("Your catcher stays planted. Ours doesn't have to."). State it once, in Seven's
  or the marshal's terms.
- **Lyle's "this morning" ×2 and the far-end walk (ch. 18, Anwen cutaway, Thursday evening).**
  The lane was Wednesday; Anwen does not walk a wall in lane 1 on the page (she leans, then goes
  with the litter). Change to "yesterday" and point Lyle at what she did see on the page, or
  move the far-end walk to what Lyle could have seen; do not add a scene.
- **"two nights to go" (ch. 23, Friday morning)**: three remain (Thu sixth crossing; sulk Thu, Fri,
  Sat, Sun; warm Monday). Sunday's "One night to go" is right.
- **Rhea's "six years … a second who watched the far edge" (ch. 20)** contradicts Pike, who did
  both for twenty years, and the standing slate line dating from the 23rd of the first month.
  Rephrase: a catcher who watched her heel, and since the first month a second who watched the
  far edge.
- **Bag count (ch. 20 slate and anywhere it recurs):** three purses shut at the high-water slack
  and four at dawn is seven, the seventh (the fourth post's) light. Change "six bags … the sixth
  bag light" to seven; reconcile records.
- **Quiet 6:12 to ring down 6:35 vs "twenty-one minutes" (ch. 21):** make the figures agree.
- **Ch. 20 section opening "at twenty past six" vs "Low water slack: a quarter past six":** make
  the opening time 6:10 (or equivalent) so the slack is still a few minutes off.
- **Ch. 22 order:** the noon hand check and its 4 p.m. and 10 p.m. follow-ups are told before
  Adlam's half-past-eleven visit. Reorder so the day reads forward, moving the hand checks after
  the Adlam scene (a transition clause only; no new prose scene).
- **Ch. 24 Bench:** Perrin's "If my ribs go on the Bench tomorrow" vs the closing scene listing
  only other fours. Settle whether Seven stands at Monday's Bench, according to the book's own
  structure (the Bench is Monday the 14th; Seven is entered). Fix whichever line is wrong.
- **Ch. 21 Hart: "Mara said the same thing yesterday … On the gallery."** On the page Mara said
  only "It's the bank's" and "How". Change Hart's line to what she actually said or nearly asked.
- **Smaller:** ch. 24 Trewin "on the Ropewalk's boards" → "on the gate's boards"; ch. 24 Trewin "a
  fortnight ago" → "eleven days ago" or "at the gate"; ch. 19 Mara "a transit two days behind
  you" (she was still in Meridian at the fever) → "and I was still at the kitchen table, two days
  from leaving" (or equivalent); ch. 17 Talley's parcel "forwarded" reaching Kellan by Monday →
  "wired it on"; ch. 21 Carrow "Maud told me last night" → drop "last night"; ch. 19:245 punctuation
  ("Your sponsor's in town?"); ch. 22 the dividers sentence ("brass ones that he must have brought
  in the black book's spine") untangled; ch. 21 "eleven minutes that the low town would bear" gloss
  in four words or cut; ch. 20 "walls laid flat on the water" → "walls lying flat on the water"
  (avoid the doctrine word *laid*).
- **ch. 23 "Nothing came."** Kiva says it aloud to Aske and Pru. It is a decision made on the page
  and legitimate. Make no prose change; record in the ledger that Aske and Pru now suspect (not
  the content).
- **C20 check (do not edit unless wrong):** "She had not told Lyle that a lodger could be killed,
  or how." Verify against chapter 13 (the lodger killed by a cut along its length on the license
  floor); if it agrees, leave it.
- **Do not touch:** the tide clock (the harbour slack moves one minute between consecutive days;
  C12/T4) — an owner/Movement Four item; record it. The 41-minute hold vs 20-minute quiet (C13);
  the brown-ink "temperature" line (C14); "my best machine" (C21).

### 2. Scene structure, sentence contrast and first-read footholds (narration only)

The movement fixed the 60–90-word chains but over-corrected: only 0.4% of sentences reach forty
words, the SD fell from 11.2 to 7.9, and sections average 625 words with 14.5 internal breaks per
10k (formula about 8.7). Single fights and dinners are cut into several scenes by `---`.

- **Remove 15–20 intra-scene `---` breaks** where place, time and lens do not change, joining the
  sections with at most a one-clause transition and no cut prose. Targets: lane 1 (ch. 18 §1–7),
  the high-water slack (ch. 20 §2–4), the gate reading (ch. 21 §0–2), the Proprietor's dinner
  (ch. 22 §6–7), the Counting House evening (ch. 23 §3–8), lane 3 (ch. 24 §1–3 and §7–8). Keep a
  break wherever place, time, or viewpoint genuinely changes, and keep every break before and
  after a non-Kiva cutaway. Fold the very short bridge sections (ch. 22 §2 at 125 words; ch. 19 §9
  at 146; ch. 22 §8 at 224) into a neighbour.
- **Write one or two hierarchical long sentences (40–55 words) per chapter**, only in descriptive
  set pieces (the Saltmere arrival ch. 17 §1; the Graving ch. 17 §4; the pump-house hall ch. 19 §2;
  the kiddle ch. 20 §0; the Hoop rising ch. 21 §4; the Counting House stair ch. 23 §3). One main
  clause, clear subordination, readable aloud by a thirteen-year-old; no *and … and* chains.
- **Join runs of three or more short narration declaratives** in reflective passages where they
  carry one thought (Kiva's thinking in ch. 22 §1, ch. 23 §7, ch. 24 §10).
- Waypoint (not a gate, not a new target): narration median 8–9, narration short share nearer 33%,
  ≥40 share about 1.5–2.5%. The formula (mean 14.6, median 11, ~27.7% at five or fewer, ~3.3% at
  forty or more) is unchanged. Do not chase the number. **Leave dialogue alone.**
- **First-read footholds (cold-read priority 3).** Break the paragraph of rule history in ch. 17
  (opening "Kiva knew about the rule", at the gate) into two or three beats around Carrow's walk to
  the cross so the scene does not stop; add one clarifying clause the first time "hand door"
  appears in the movement (ch. 18, "Hand. To Ember." and the first "She's a hand door", ch. 24)
  distinguishing the ward-tray door from Kiva's literal cold hand; where "Hold" is both a role and a
  reading (ch. 22, Kellan's recital), mark which. Do not change the "Kiva:" chapter titles; every
  non-Kiva section already opens on its lens by name.

### 3. Distinct voices and read-aloud clarity (line edits only)

Both reviews found one shared idiom ("say it before, not after") in almost every mouth.
- **"I'd want it said / I'd want …" (28 uses; "want it said" 11):** keep for **Jude** (his
  diffident form) and Anwen's own "I want it said"; recast the other ~16 in each speaker's
  register: Orla rough and brief; Hart plain and gauge-like; Mara dry and exact; Kellan as a sum;
  Peverell in her columns; Aske's price speeches; Perrin's alone is "I'd like it known" (7). Keep
  the formula where it is *about price or consent*: Aske's card speeches, Perrin's "beaten fairly"
  book line, Kiva's "I'm saying it so that it's said" before the Counting House. Count and vary.
- **"said nothing / did not say anything" (22 + 14):** vary or cut about half.
- **Scarlet / "went red" (13):** keep Pru's; give Perrin and the others different physical tells.
- **"in two stages" (5), "so that it's said" (3):** thin to the places that matter.
- **Causal "since" (5: ch. 17 ×2, ch. 18, ch. 20, ch. 21):** recast as *because*.
- **Negation runs ("she did not … she did not …")** in Kiva's reflective passages, densest in
  ch. 21–23: recast the worst runs into positive statements.
- Keep Perrin's "I'd like it known"; Aske's "soonest"; Pike's "nearly smiled" (3); Hart's turned
  watch; the Proprietor's dry courtesy.

## Strengths to protect

"It's every count at once"; the Tarn jar and "It isn't anybody. That's the trouble. It's just
people."; one line for two doors and "*Laid* … as a man says *amen*"; "There's no gap … Carrow had
to run"; lane 1's three carries; Hart's barometer; "It's yours" to Mara and "I find that I don't
care for it at all"; the kiddle standing upright at slack; *Far edge*, two words, once; Rhea's
remark against herself; Orla's "She's—" and Hart's "There."; the Hoop and "It's gone out of the
harbour, into that"; Perrin asking to be read: "The tape does not know the difference. The lodger
did."; the Proprietor's hand on the glass, "I'm not brave enough", and his laugh; Pru's "I'm not
grateful"; *yes or no*, never *what*; the short scene-ending beats ("It sang." / "Nothing." /
"There."). Retain Kiva's voice, the crew's warmth, character agency and every developed contest at
full length. Do not shorten lane 1, the slack cuts, the Counting House, or the Proprietor scenes.

## Boundaries

- No change to any event, outcome, date, ash total, power limit, injury, knowledge boundary or
  reserved disclosure. The fifth crossing is Thursday the 3rd and the sixth Thursday the 10th; the
  book stays at 4.28 / 4.16 as written; the sealed 2.0 stays bound and refused for sale; the
  disk stays cold; "Unroofed Sky" and "Breach" stay unused; the dream stays private.
- No new chapter, scene, revelation, named person, power or subplot. No wholesale rewrite.
- Do not modify plans or canon to excuse prose errors. If a repair would touch owner-protected
  wording, leave it and record why.
- **Owner items — not for you to decide; record any you touched or left:** whether sentence targets
  govern dialogue and how long a "long" sentence may be read aloud; the front-load progression
  arithmetic; the harbour tide clock (C12); the Graving used as a seeding floor (C15) and the
  re-run slate template (C16): record these as accepted departures in the continuity file;
  `BOOK_MAP.md` §12 (Rhea goes short is now in Movement Three, authorised by the packet): add a
  one-line dated note to the map; the 41-minute hold (C13); the brown-ink line (C14).

## Deliverables

1. Repair the working files `manuscript/chapter-17.md` through `chapter-24.md`, in reading order.
2. Write `provenance/MOVEMENT-003-REPAIR.md`: runtime-reported model and session/job identifier
   (say plainly if unverifiable); each factual correction with its evidence; what was restructured,
   joined, split or recast, by chapter and section; the list of `---` breaks removed (chapter and
   section); before/after `wc -w` per chapter and for the movement; before/after metrics from the
   script (all text, narration, sections, breaks per 10k); counts before and after for "I'd want",
   "want it said", "said nothing", scarlet/red, "in two stages" and causal "since"; every requested
   item left unchanged, with the reason; confirmation that the frozen edition was not modified
   (`shasum -a 256 -c SHA256SUMS.txt`).
3. Reconcile `provenance/MOVEMENT-003-CONTINUITY.md` and the Movement Three block of
   `STATE_LEDGER.md` to the surviving prose where a repair changed what they state (bag count,
   nights, lane 2, hand-check order, accepted departures, the "Nothing came" knowledge note). Add a
   repair entry to `AUTHORSHIP.md`. Do not claim recheck, acceptance, publication, or any Movement
   Four work.

When finished, stop. Do not commit, push, publish, or draft forward.
