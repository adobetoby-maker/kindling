# Prose pass, Movement Two (*The Crooked Lane*, Chapters 9–16)

Ticket M2, 2026-10-28. Seat: O'Connor 1.3.2 (Monroe Jackson), Claude Opus 5.5.
Branch `feature/2680-prose-m2`, base `origin/main` 8491277. Canon used:
`universe/SEED-2680.md`; `editor/MOTIF-BUDGET-REVISION.md` §5, §6, §8.4, §8.5 and §8.7;
`BOOK_MAP.md` §8; `packets/MOVEMENT-002.md`; `CHARACTERS.md`; the pilot report. The
foreman's Movement One facts (sent mid-task) were applied too. They are listed in §4.

## 1. Numbers, before → after

Each count uses `grep -oiE` on the file. The *free nine* and *free eleven* columns use the
§8.5 filters. *Contrast* counts "It was not X. It was Y." and "It did not X. It Y.",
checked by hand after the pass.

| Ch | Words | write-it-down | ledger | notebook | record* | count* | free nine | free eleven | measur* | aloud / out loud | "to … face" (device) | Contrast |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | 6,764 → 6,879 (+1.7%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 11 → 0 | 2 → 0 | 1 → 0 | 2 → 0 | 2 → 2 | 0 → 0 | 0 |
| 10 | 6,733 → 6,637 (−1.4%) | 4 → 0 | 4 → 0 | 0 → 0 | 0 → 0 | 6 → 0 | 12 → 0 | 13 → 0 | 0 → 0 | 0 → 1 | 1 → 0 | 0 |
| 11 | 6,121 → 5,924 (−3.2%) | 3 → 0 | 0 → 0 | 0 → 0 | 2 → 0 | 10 → 0 | 13 → 0 | 1 → 0 | 4 → 0 | 0 → 0 | 0 → 0 | 3 |
| 12 | 6,156 → 6,187 (+0.5%) | 2 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 13 → 0 | 3 → 0 | 5 → 0 | 1 → 0 | 1 → 0 | 0 → 0 | 1 |
| 13 | 7,838 → 7,742 (−1.2%) | 4 → 0 | 0 → 0 | 0 → 0 | 1 → 0 | 13 → 0 | 7 → 0 | 5 → 0 | 0 → 0 | 0 → 0 | 2 → 0 | 2 |
| 14 | 6,372 → 6,186 (−2.9%) | 6 → 0 | 3 → 0 | 1 → 0 | 0 → 0 | 10 → 0 | 8 → 0 | 2 → 0 | 5 → 0 | 2 → 2 | 0 → 0 | 2 |
| 15 | 5,608 → 5,621 (+0.2%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 9 → 0 | 2 → 0 | 0 → 0 | 1 → 0 | 0 → 1 | 0 → 0 | 0 |
| 16 | 7,045 → 7,126 (+1.1%) | 6 → 0 | 0 → 0 | 2 → 0 | 1 → 0 | 10 → 0 | 10 → 0 | 7 → 0 | 4 → 0 | 3 → 0 | 2 → 0 | 2 |

The remaining *aloud* hits are plain verbs, not closing devices. Ch 9 has two: the rule
"declare the roles aloud" and Kiva's "say so out loud first". Ch 10's is Anwen's "the
truth, straight away, out loud". Ch 14's are Noa wanting to hear his list "out loud" and
Kiva's "I say so first. Out loud." Ch 15's is the old master who "laughed out loud". Ch 13 has one grep
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
  for about a minute" and "settles when it settles". *Cut* starts a drill, *Settled* ends
  it, and a sand glass on the stair table times the practice catches.
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
- The grader's card stays as a readout prop. Halloran's counting aloud is gone: she grades
  against a banded sand glass (the sand runs past the blue band, then the red).
- "Nine reeds" → "a row of reeds". The shelf's cards and labels are cut, and the shelf
  jars are now heard on the comb ("come down here and listen… on my comb").
- Kellan's mother's story is no longer told here. He argues for the shelf because the
  board will have to come down and listen with their own ears: "the only half dram on
  this table that makes somebody else do something." There is no preserved-evidence save.
- The clerk's slate and ledger are now the shares said aloud. The team gets "four drams,
  less a tenth", which avoids "three and nine-tenths". The ledger signing is now the clerk
  splitting the ash across the counter.
- Noa's drawers, notebook, and five-column page are now a conversation with the old
  first-bench reader in the Placement Hall basement (median Hold 6.1). He then says his
  "probably nothing" list to Jude.
- Vane's half-sheet to the Works is now Vane at Rusk's counter, reported by Mara.
- Orla reading the week's pages is now Orla making Kiva tell the week. The chapter no
  longer ends on "Eight and six"; Orla gets the last line after the readout.
- Measure Hall → the Placement Hall (1). The post glance is cut here.

**Ch 15.**
- Kneeling downs use the line judge's glass, not a count of ten.
- Noa does not touch the mast during the meet. He works from the public draw board.
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
   - Druce's practice sand glass (Ch 9).
   - The grader's banded glass (Ch 14).
   - The line judge's glass for downs (Ch 15, 16; Jude's plan in Ch 14).
   - An unnamed old first-bench reader in the Placement Hall basement (Ch 14).

   Later chapters that show grading or downs should match these or replace them.
4. **Vane's four questions at the cart** (Ch 13) leave out the cost, which matches seed §7
   ("never asked the cost at the cart"). Ch 27's rule change pays it off.
5. **The team share** is now said as "four drams, less a tenth" (the same 3.9) to avoid
   the nine refrain. The spend arithmetic is unchanged.

## 6. Dependencies this movement creates for later chapters

- **Ch 17–24 (Movement Three):**
  - Use "while it's open" / *Settled* for the open-ash window, not "the count".
  - Kiva's control is calling: door names and what is in front of her.
  - Downs in meets use the line judge's glass.
  - Grading uses the banded glass and "a row of reeds" (Ch 24's "nine brass reeds" and
    "Nine and six-tenths… Graded First" need to match or vary).
  - Noa reads with a referee beside him and Kiva's leave, asked monthly. He keeps no
    notebook.
  - Ysra gets findings first, with no "copy… in writing".
  - The Flask qualifiers are moved to the last week of this month. Team Seven stands
    seventeenth of thirty-one.
- **Ch 27** (the cost at the cart): built on Ch 13's four questions.
- **Movement Three, any echo of Kellan's "pencil" or "folded paper":** these are cut in
  Movement Two. He keeps things in his head.

## 7. Section-closing devices (brief rule 4)

- **Declarations aloud closing a section:** two in the movement, not in a row.
  - Ch 13 §3 ends on Anwen's one word, *Seven*, guessed at a distance.
  - Ch 15 ends on "Rowan," she said. "Still."
- Two call-closings (Ch 11 "*Yours!*", Ch 15 "*Down!*") were merged into the following
  action.
- **Numbers closing a section:** none. Ch 15 had two board-figure closings and Ch 16 one;
  each now has a consequence line after it.
- Every other section ends on plain action, consequence, or dialogue.

## 8. Self-check against the Movement One review warnings

1. **Call repeated back as a record.** Druce's "Heard" is now a nod (Ch 11, 12). Kiva no
   longer echoes Perrin's "Boy in the way" (Ch 13). Anwen's laundry recap is now "Then
   it's off." *Seal check / Sound* stays: it is a thumb on a lid, not a record.
2. **A reading deciding a beat.** "To a tenth" and "to the tenth" are cut (Ch 10, 12).
   Ysra's "same as a mast in a cart shed said" is cut. Her ruling rests on her referee
   having watched the tape. That is the packet's required witnessed act and is cited as a
   person's witness, not a figure being right. Bettan's 20.8 against the canon mark of
   twenty stays as a readout.
3. **A kept thing saving someone.** Kellan's jar story is removed (Ch 14). "Jars gone brown
   with age" is cut.
4. **Renumbered refrains.** No time is restated as a new number. There are no countdown
   paragraphs.
5. **Spoken-record phrases and the meter simile.** "All of it" is cut from Kellan (now
   "The last"), Anwen (Ch 16), and Mara (Ch 10). Every "in order" is cut. The meter or
   needle similes are cut in Ch 10, 11, 12, 13 and 16. One remains in Ch 10 ("the way a
   reading came out of her at the bench"), because it is where calling begins.
6. **The closing-gesture cap.** See §7.

Mara takes Orla's form to Rusk in person (Ch 11). She files nothing anywhere. Ch 9's
"That's what a call is for" does not echo a card.
