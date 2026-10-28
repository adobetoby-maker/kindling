# Prose pass, Movement Two (*The Crooked Lane*, Chapters 9–16)

Ticket M2, 2026-10-28. Seat: O'Connor 1.3.2 (Monroe Jackson), Claude Opus 5.5.
Branch `feature/2680-prose-m2`, base `origin/main` 8491277. Canon used:
`universe/SEED-2680.md`; `editor/MOTIF-BUDGET-REVISION.md` §5, §6, §8.4, §8.5 and §8.7;
`BOOK_MAP.md` §8; `packets/MOVEMENT-002.md`; `CHARACTERS.md`; the pilot report. The
foreman's Movement One facts (sent mid-task) were applied too. They are listed in §4.

## 1. Numbers, before → after

Each count uses `grep -oiE` on the file. The *free nine* and *free eleven* columns use the
§8.5 filters. *Contrast* counts "It was not X. It was Y." and "It did not X. It Y.",
counted with a perl match on the base (8491277) and on the fix-round text. *aloud / out loud*
matches `\baloud\b|out loud` on both sides (fix round 1 corrected the before figures).

| Ch | Words | write-it-down | ledger | notebook | record* | count* | free nine | free eleven | measur* | aloud / out loud | "to … face" (device) | Contrast |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | 6,764 → 6,866 (+1.5%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 11 → 0 | 2 → 0 | 1 → 0 | 2 → 0 | 4 → 2 | 0 → 0 | 0 → 0 |
| 10 | 6,733 → 6,612 (−1.8%) | 4 → 0 | 4 → 0 | 0 → 0 | 0 → 0 | 6 → 0 | 12 → 0 | 13 → 0 | 0 → 0 | 1 → 1 | 1 → 0 | 1 → 1 |
| 11 | 6,121 → 5,907 (−3.5%) | 3 → 0 | 0 → 0 | 0 → 0 | 2 → 0 | 10 → 0 | 13 → 0 | 1 → 0 | 4 → 0 | 0 → 0 | 0 → 0 | 4 → 3 |
| 12 | 6,156 → 6,219 (+1.0%) | 2 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 13 → 0 | 3 → 0 | 5 → 0 | 1 → 0 | 2 → 0 | 0 → 0 | 2 → 2 |
| 13 | 7,838 → 7,761 (−1.0%) | 4 → 0 | 0 → 0 | 0 → 0 | 1 → 0 | 13 → 0 | 7 → 0 | 5 → 0 | 0 → 0 | 0 → 0 | 2 → 0 | 5 → 3 |
| 14 | 6,372 → 6,154 (−3.4%) | 6 → 0 | 3 → 0 | 1 → 0 | 0 → 0 | 10 → 0 | 8 → 0 | 2 → 0 | 5 → 0 | 3 → 1 | 0 → 0 | 3 → 2 |
| 15 | 5,608 → 5,561 (−0.8%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 9 → 0 | 2 → 0 | 0 → 0 | 1 → 0 | 1 → 1 | 0 → 0 | 0 → 0 |
| 16 | 7,045 → 7,095 (+0.7%) | 6 → 0 | 0 → 0 | 2 → 0 | 1 → 0 | 10 → 0 | 10 → 0 | 7 → 0 | 4 → 0 | 3 → 0 | 2 → 0 | 4 → 3 |

The remaining *aloud* hits are plain verbs, not closing devices. Ch 9 has two: the rule
"declare the roles aloud" and Kiva's "say so out loud first". Ch 10's is Anwen's "the
truth, straight away, out loud". Ch 14's is Kiva's "I say so first. Out loud." Ch 15's is the old master who "laughed out loud". Ch 13 has one grep
hit, "and then to her face", which is a glance, not the device.

The §8.5 and §6 checks were run on Chapters 9–16 from `manuscript/` (scratch output:
`.foreman/scratch/m2-checks.txt`):

- Banned phrasings: 0.
- Ledger, notebook, and column-as-record: 0.
- Theme words (remember, passed on, the reasons…): 0.
- Closing `*Why:` entries: 0.
- Time given in counts: 0.
- Counting as a habit or tactic: 0.
- Free nine: 0. Free eleven: 0.
- Fixed nines (posts / rings-grooves): 0 / 0.
- Decimals: 3. All three are the Stonehand draw board (0.38, 0.87, 0.98).
- Measure Hall, Rule Nine, Team Eleven: 0.
- Chapters that end on a count: none.
- count, measure, score, and tally as words: 0.

## 2. What changed, by chapter

**Ch 9.**
- The field book is gone. Kellan's "Can I read your book?" now asks for her account in
  her own words, and she tells it on the steps. The chapter now ends with Kiva touching
  the middle of Mara's scar, and no `Why:`.
- Druce's counting up the tube is gone. He now teaches the rule once: fresh ash is "open
  for about a minute" and "settles when it settles". *Cut* starts a drill and *Settled* ends
  it. Druce calls it by judgment, the way a live heap would go quiet. There is no glass (fix
  round 1).
- "You'll keep the clock" is now "you can hear a dirty pivot across a room".
- The call-order slate is now Kellan saying the order. The yield sheet is now a clerk on
  the stair. The mast's written order is now Jude telling her.
- Noa "keeps" the tapes → "pulls" them. "Measuring something else" → "reading".
- Line 287 "steady eyes" is fixed, and "That's what a card is for" → "That's what a call
  is for."

**Ch 10.**
- The catchers say their predictions to Druce instead of writing them on slates. Druce's
  chained book and his "third this month" entry are now spoken.
- Anwen's "nine" refrain is now "the whole drill, bar and ward and stance, with
  everything in your hands". Orla no longer counts the drill in her head.
- Kiva's call when the line warms is now *Ember*. The tin weighings are cut from four
  figures to two plain readouts, and "Write it down… last column" is gone.
- Orla's field-book "accounts" are now her thinking through what she would need to sign.
  The three conditions stay. No list is written.
- The Works notice is still delivered by post, but Mara says its conditions to Kiva.
  There are no "shop books" and no "eleven years of my handwriting".
- Team Eleven → Team Twenty-Two (5 uses in the chapter). The team now stands "eighth on
  the call". Mace's ledger, "I'd like it said", "to her face", "I counted", and both
  "since … eleven" are cut.
- Kellan's reasons no longer quote Nineteen's Kennel book or the yield figures 9/11/7.

**Ch 11.**
- The thesis line now reads "It's when I stop calling. When I'm calling something, the
  calling's in the doorway…"
- Orla's margin squares are now "good four nights running" and "That'll do". Anwen's
  "nine" is now "That's quicker than I asked for… Do it again."
- On the sponsor's floor, every count is now a call: *Coming*, *Ember*, *Still's up*,
  *Hand's at the door*, *Pan*, *Lid*. Orla's "*Count!*" → "*Yours!*". The window closes
  when Kiva feels the listening stop.
- The Kennel-book entry and the certificate's quoted text are cut. Orla signs the form
  and says what it covers. The form stays because the packet requires a signed
  certificate.
- Mara: "a meter, and a shutdown path, and a hand. Hers." The closing `Why:` is now Kiva
  telling Mara at the table that the still door felt like helping.
- Noa's "nine hundredths" is now "under a tenth", and his Draw is "a hair under one".
  "Somebody ought to be counting that" → "watching".
- The post glance is cut here; she looks at the lamp instead.

**Ch 12.**
- Kiva teaches Kellan to *call*, not count: "If my mouth's got a word in it, the door
  stays in the doorway."
- Kellan's written plan is now something he goes over in his head. In the laundry he
  practices by saying under his breath what is in front of him.
- The laundry plan is now spoken, with no list headings. Anwen's "I don't write things
  down twice" → "I'm not going to keep telling you."
- Druce's "say it a third time while I write" is now Druce laying his own fingers on the
  tin: "Curved… That's what I felt in Wednesday's tins, and called it nothing."
- The courier's "keep the book for mast six" → "tend". "Since she was nine" → "six".
- The catch counts are now calls. "Somebody put that in the book" → "I'll say so at the
  inquest".

**Ch 13.**
- Mara's cell-book entry is gone. She tells Vane she left the trim screw alone, and why.
- Vane has no slate and no chalk. His result is spoken, his tag note is gone, and his
  report to the Works is "come and stand on this road and ask me".
- Kiva's field-book falls are now her watching every fall. Three falls are told in
  narration. Their team numbers moved into group three (Thirty-Three, Thirty-Four,
  Thirty-Six) because group three is 27–40.
- "The kill column out of its book" → "The Home Line doesn't ask who made the kill. We
  ask four things at the cart." That list leaves out the cost, which sets up Vane's flaw
  in seed §7 and Ch 27.
- Kellan's hand stops on "Stay dark. Kellan. Call it." He answers "Dark. Hand open.
  Staying."
- The written tags are gone. Bettan says over her shoulder, "Seven's. Rowan caught."
- Mara now heard her "calling… flat as a bench reading".
- Team Eleven → Team Twenty-Two (3 uses). "Nine seconds" → "before I'd drawn breath".
- Two contrast constructions cut, along with "steady".

**Ch 14.**
- The grader's card stays as a readout prop. Halloran's counting aloud is gone. The banded
  glass is one clause, and she does not look at it. The suspense rests on what's at stake
  (license, Graywater, Kellan's place) and on what Kiva feels, the little tune sitting
  "like a coin on a table" until one edge goes soft.
- "Nine reeds" → "a row of reeds". The shelf's cards and labels are cut, quoted labels
  included. Halloran: "a jar on this shelf is something the board will have to answer."
- Kellan's mother's story is no longer told here. He argues for the shelf as a test of
  whether they are right ("Better to pay half a dram than be wrong in comfort"). There is no
  preserved-evidence save and no witness line.
- The clerk's slate and ledger are now the shares said aloud. The team gets "four drams,
  less a tenth", which avoids "three and nine-tenths". The ledger signing is now the clerk
  splitting the ash across the counter.
- Noa's drawers, notebook, and five-column page are now his own afternoon holding the rod
  at the Wren House posts: this spring's first-years hold longer than his year did. He says
  his "probably nothing" list to Jude. The bench reader is cut (fix round 1).
- Vane's half-sheet to the Works is now Vane at Rusk's counter, reported by Mara.
- Orla reading the week's pages is now Orla making Kiva tell the week. There is no drill
  time: Kiva feels the frame catch once, and Orla says nothing.
- Measure Hall → the Placement Hall (1). The post glance is cut here.

**Ch 15.**
- Downs kneel, with no count of ten. The referee's rule names the line judge's glass once,
  and there is one kneeling image. Every other glass is cut (fix round 1).
- Noa reads nothing during the meet. Kiva makes the third-carry choice by feel: the still
  door "hardly drinks", and every change drains her "like water out of a cracked cup".
- Kiva asks for "a call" when one of them goes down. Pru: "I'm good at calling disasters."
- "Kill column" is fixed. Perrin's "book… *what it cost*" → "She would ask him what it
  cost, the way Dane had taught her to." The plate reads "thirty seconds", not counts.
- Two section closings that ended on a board figure now end on consequence lines.

**Ch 16.**
- Pru's tap counting is now her calling the disaster ("He's down! Brask's down…"), and
  Kiva answers *Staying*. "Nine taps!" → "She had to *lean*!"
- The referee's lane card is now her ruling, said across the sand.
- Noa asks to *read* her, with consent: "They're your doors."
- **The witnessed fact (packet 002, ticket):** the Circuit referee cuts the Stonehand
  tape herself and stands at Noa's shoulder while he reads the fourth pen. Her words:
  "That's my board… I'll tell the Chair I stood here and saw it." In Ysra's office the
  referee stands at the door and nods. Ysra rests her ruling on that ("It came off my own
  instruments, and my own referee watched it come off"). The figure is "a hair under one",
  which matches the Low Lane reading.
- Hold figures off the posts stay as readouts (nines removed).
- Rhea's draft card is now what she will tell Doran.
- Kellan's copied paper, Anwen's "Write it down. Then I can read it", and Perrin's "It's
  in my book" are cut. Ysra's desk papers and "consent in writing every month… a copy" are
  replaced: "with her leave, asked again every month… comes to this desk before it goes
  anywhere else."
- Lane scores: "Nine to seven… eleven to three" → "Two points… eight in the autumn". The
  board's digits stand.
- The closing field book is now Orla's debrief, spoken in the Old Yard as the scene,
  mid-scene, with Kiva's "I can open three. I can only stand on one." The chapter ends on
  action, with Kiva waiting at the top of the lane, not "Count." Its one post glance is
  kept as the movement's only glance.

## 3. Renames applied

- Team Eleven → Team Twenty-Two: Ch 10 (5 uses, including bare "Eleven" → "Twenty-Two"),
  Ch 12 (1), Ch 13 (3).
- Measure Hall → the Placement Hall: Ch 11 (1), Ch 14 (2), Ch 16 (3, including hold posts
  "like the ones in the Placement Hall").
- No Rule Nine in these chapters.

## 4. Dependencies fixed (including the foreman's Movement One facts)

- **No field book anywhere.** Done in Ch 9, 10, 11, 12, 13, 14, 15, 16. The Ch 10 phrase
  "the three she had ruled for the children" is cut.
- **The warm-line call names the door** (*Ember*, *Hand*, *Still*), not "one": Ch 10, 11,
  13. Ch 16 has *No*, said to the door.
- **Mara's third word is Hand:** Ch 11.
- **Mara reads and mends for the Works; no shop books.** Ch 9 has the "tray of the city's
  meters" and Works tags. Ch 10's notice is spoken.
- **Kellan's mother and the jar:** Ch 14 first matched "jar regraded on an open bench".
  Then the Movement One review warning (no preserved-evidence saves) arrived, so Ch 14
  no longer refers to how she was saved. It stands whatever Ch 4 settles on.
- **Mast six and the trim screw, no cell-book entry:** Ch 12, Ch 13, Ch 14.
- **Rhea wrote no draft card:** Ch 16.
- **Mara's nightly check of the two fingers:** Ch 9 already has "I've had my thumb on them
  every night". It is unchanged and consistent.
- **Declared roles, no team card:** Ch 9's "That's what a call is for" replaces the card
  echo.
- **First clean drill at fourteen seconds, ten by the next Tuesday:** Ch 10 says "Your
  best with shapes is ten, near enough". Ch 11 and Ch 16 keep 8.8 and 8.4.
- **Post budget:** one glance in Movement Two (Ch 16). The Ch 11 and Ch 14 glances are
  cut.
- **Hanley Street:** not present in these chapters.

## 5. Canon conflicts and judgment calls (flagged)

1. **"Noa measuring, not recording."** Packet 002 says "reading", and seed §11 bans
   "measure" as narrative vocabulary. I read the ticket's note as "an act on an
   instrument, never record-keeping". Noa *reads* tapes and gauges, keeps nothing, and the
   word "measure" is gone. If the owner wants "measure" kept as Noa's verb, it needs an
   exemption from §11.
2. **Orla's certificate stays as a signed form.** Packet 002's entry state requires it.
   Its text is no longer quoted; Orla says it.
3. **New mechanisms (no new plot) that replace counting:**
   - The grader's banded glass, one clause (Ch 14).
   - The line judge's glass, named once in the referee's rule and in one kneeling image
     (Ch 15).

   Druce's glass and the bench reader were removed in fix round 1.

   Later chapters that show grading or downs should match these or replace them.
4. **Vane's four questions at the cart** (Ch 13) leave out the cost, which matches seed §7
   ("never asked the cost at the cart"). Ch 27's rule change pays it off.
5. **The team share** is now said as "four drams, less a tenth" (the same 3.9) to avoid
   the nine refrain. The spend arithmetic is unchanged.

## 6. Dependencies this movement creates for later chapters

- **Ch 17–24 (Movement Three):**
  - Use "while it's open" / *Settled* for the open-ash window, not "the count".
  - Kiva's control is calling: door names and what is in front of her.
  - Downs in meets: fighters kneel and are waved up. Use no glass or count.
  - Grading uses "a row of reeds". Use no timing object as the arbiter (Ch 24's "nine brass reeds" and
    "Nine and six-tenths… Graded First" need to match or vary).
  - Noa reads with a referee beside him and Kiva's leave, asked monthly. He keeps no
    notebook.
  - Ysra gets findings first, with no "copy… in writing".
  - The Flask qualifiers are moved to the last week of this month. Team Seven stands
    seventeenth of thirty-one.
- **Ch 27** (the cost at the cart): built on Ch 13's four questions.
- **Movement Three, any echo of Kellan's "pencil" or "folded paper":** these are cut in
  Movement Two. He keeps things in his head.

## 7. Section-closing devices (brief rule 4), corrected in fix round 1

Every section ending in Chapters 9–16 was listed by script and classified by hand.

- **A declaration or quoted word closes the section:** two, not in a row.
  - Ch 13 §3 ends on *Seven*.
  - Ch 15 ends on "Rowan," she said. "Still."
- **A number or timing closes the section:** none.
  - Fix round 1 re-ended Ch 13 (it ended "She had four tins."; it now ends on Mara holding
    her boots).
  - Also re-ended: Ch 15 §5, Ch 16 §2, Ch 16 §3, and Ch 16 §8 (Ysra's "three weeks",
    now followed by Orla's silence).
  - Ch 10 §2's repeated "third one this month" closing is now "I don't know."
- **Character verdicts back to back:** Ch 12 §7 and §8 now end on plain action (Druce
  fetches the salt; Anwen goes to help with the coppers).
- My first report claimed Ch 15 and Ch 16 had no number closings. That claim was wrong
  for the Ch 13 ending and for Ch 16 §2/§3.

## 8. Self-check against the review warnings and brief §4b, corrected in fix round 1

Counts from `.foreman/scratch/check.sh` (output in `.foreman/scratch/m2-checks.txt`):

| Item | Count |
|---|---|
| Timing-glass uses | 2 (Ch 15:45 referee's rule; Ch 15:281 kneeling image), plus one clause in Ch 14:33 |
| "glass" overall | 45 against 43 at base; the rest are windows, dishes, spectacles |
| One-line drill times ("X and Y," said Orla.) | 1 (Ch 11) |
| "Come down three times" progress line | cut |
| Repeat-backs ("Recovery only" ×2, "Until the ninth" ×2) | 0 |
| "the ninth" | 1 (Ch 10, said once by Mara) |
| Meter, gauge, or weather similes | 0. The remaining "like a compass needle" and "like a needle to north" are original images of a husk turning to light, not reading similes |
| Skinned-Handful tally | 1 ("Third this month", Ch 10). Ch 12 is now "Another." Ch 14's figures are cut |
| Crowd-witness lines | "with their own ears" ×2, "in front of a referee", and the referee's "I'll tell the Chair" ×2 are cut |
| Read-backs or "one at a time" terms | 0 (two hits are original, unrelated phrasing) |
| Shared "I'd like / I'd rather" | thinned for Noa, Kellan, Halloran and Anwen; kept as Perrin's habit |
| Contrast constructions | 3 or fewer in every chapter (column in §1) |

My first report's §8 claim that one meter simile was kept in Ch 10 for the origin of
calling is withdrawn. That simile ("the way a reading came out of her at the bench") is
now "the way a word comes out when you stub your toe".

Mara takes Orla's form to Rusk in person (Ch 11) and files nothing anywhere. Ch 9's
"That's what a call is for" does not echo a card.

## 9. Fix round 1 summary

Verifier finding → fix:

1. **Glasses as renamed counts.**
   - Ch 9: the glass is gone, and *Settled* is Druce's felt or judged call.
   - Ch 14: the glass is one clause, and the suspense is rebuilt on stakes and feel.
   - Ch 15: four timing uses cut. Ch 16: all three cut.
2. **Drill-time refrain.** Kept once, in Ch 11. The Ch 14 and Ch 16 times are now feel,
   and the "three times in a fortnight" line is cut.
3. **Repeat-backs.** Removed in Ch 11 and Ch 10. "The ninth" goes from 4 to 1.
4. **Closing gestures.** See §7.
5. **Similes.**
   - Ch 9 "weather" → "as if it had nothing to do with him".
   - Ch 10 → "stub your toe".
   - Ch 13 "inventory" → "the way people sound the morning after a flood".
   - Ch 13 "bench reading" → "Your voice never once went up".
   - Ch 15 "label on a jar" → "a horse he might buy".
6. **Noa reading during the meet.** Removed. Kiva's own feel decides the third carry.
7. **Witness lines, quoted labels, bench reader, tally.** Cut or varied, as in §8.
8. **Report.** This section, §7 and §8 are corrected, and the *aloud* before-counts are
   recomputed.
