# Prose pass, Movement One (*Three Doors*), Chapters 2–8

Ticket M1, 2026-10-28. Author seat O'Connor 1.3.2 (Monroe Jackson), Claude Opus 5.5.
Branch `feature/2680-prose-m1`, base `origin/main` 8491277. Canon used: `universe/SEED-2680.md`
§3, §6, §8, §11, §12; `editor/MOTIF-BUDGET-REVISION.md` §5 (beats 3, 4, 5), §6, §8.4, §8.5, §8.7;
`BOOK_MAP.md` §8; `packets/MOVEMENT-001.md`; `CHARACTERS.md`. Style reference: the pilot's
prologue and Chapter 1. Chapter 1 was not touched.

## 1. Numbers, before → after

Patterns as in the pilot report (`grep -oiE`). *book/col/card* is
`\bbooks?\b|\bcolumns?\b|\bcards?\b` (the field book, cell books, the team ledger card, draft
cards). *Free nine / free eleven* count each word (`grep -oiw`), less the fixed quantities; the
first draft of this table used the §8.5 30-character window, which merges "nine and a half, nine
and a half" into one hit and undercounted Ch. 4 nine (4, really 5) and Ch. 8 eleven (2, really 3).
*X/Y* is the hand-counted rhetorical contrast "It was not X. It was Y." (and "It did not
X. It Y."), after the pass; plain action negations ("She did not ask. She came down…") are not
counted.

| Ch. | Words | write-it-down | ledger | notebook | record* | count* | free nine | free eleven | Measure | aloud / out loud | to … face | book/col/card | X/Y after |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 4,650 → 4,351 (−6.4%) | 2 → 0 | 3 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 2 → 0 | 1 → 0 | 0 → 0 | 2 → 0 | 0 → 0 | 17 → 0 | 1 |
| 3 | 5,285 → 5,120 (−3.1%) | 2 → 0 | 0 → 0 | 2 → 0 | 0 → 0 | 2 → 0 | 0 → 0 | 6 → 0 | 0 → 0 | 3 → 1 | 0 → 0 | 19 → 0 | 3 |
| 4 | 5,897 → 5,978 (+1.4%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 3 → 0 | 5 → 0 | 0 → 0 | 1 → 0 | 4 → 0 | 0 → 0 | 14 → 0 | 3 |
| 5 | 5,568 → 5,462 (−1.9%) | 1 → 0 | 2 → 0 | 0 → 0 | 0 → 0 | 1 → 0 | 4 → 0 | 0 → 0 | 0 → 0 | 5 → 2 | 0 → 0 | 10 → 0 | 3 |
| 6 | 5,825 → 5,646 (−3.1%) | 2 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 2 → 0 | 0 → 0 | 0 → 0 | 3 → 0 | 2 → 0 | 16 → 0 | 3 |
| 7 | 4,957 → 4,874 (−1.7%) | 2 → 0 | 4 → 0 | 0 → 0 | 3 → 0 | 0 → 0 | 3 → 0 | 1 → 0 | 0 → 0 | 3 → 0 | 1 → 1 | 9 → 0 | 2 |
| 8 | 5,828 → 5,456 (−6.4%) | 5 → 0 | 0 → 0 | 0 → 0 | 6 → 0 | 2 → 0 | 2 → 0 | 3 → 0 | 3 → 0 | 2 → 0 | 1 → 0 | 43 → 0 | 2 |

Notes on the residue: Ch. 3's one "out loud" is Perrin's original "Not out loud. In your knees."
Ch. 5's two are Ysra's Call rule ("said aloud, before you start") and Kiva's "she said aloud" at
the cell. Ch. 7's one "to her face" is a candle held up to a face. Ch. 6's "scored" is the cuff
leather, scored pale. Every chapter is inside ±15%.

**§8.5 and §6 mechanical checks**, run on chapters 2–8 together (output saved to
`.foreman/scratch/prose-m1-checks.txt`, not committed):

| Check | Result |
|---|---|
| Banned phrasings (expected 0) | 0 |
| Ledger / notebook / column-as-record | 0 |
| Theme words (remember, passed on, the reasons…) | 0 |
| Closing `*Why:` entries | 0 |
| Time in counts (expected 0) | 0 |
| Counting as habit or tactic (expected 0) | 0 |
| Free nine / free eleven | 0 / 0 |
| Fixed nines: posts / rings-grooves | 0 / 1 (Ch. 8, Rhea's glass on the disk) |
| Fixed elevens (an hour) | 0 |
| Decimals (report only) | 7, unchanged from base (Ch. 2 Draw 3.1; Ch. 4 drams 0.31 / 0.88; Ch. 6 dram line) |
| Measure Hall / Rule Nine / Team Eleven | 0 |
| Chapter ends on a count | none (Ch. 5 used to end "Eight and two."; it now ends on the line before) |

## 2. Main changes

**Ch. 2.** Cell books, the note column and the "paper worked after the Fall" passage are gone;
Mara asks who tunes Tallis Street and tells Kiva to feel, not guess. Mara's evening is now her
real job (reading banks by hand for the Works, left palm), not reconciling ledgers. The
red-stripe letter becomes Examiner Rusk on her stool in the winter, said plainly. The mast
scene keeps the creeping baseline as the instrument's own trace, read off the live drum against
"when I first came out here"; no archive of rolls, no cell-book entry. Mara lays her thumb on the
trim screw and does not turn it ("Fix what's broken. Leave what isn't."). Mara's third word is
**HAND**: "Somebody whose hand is on it. Somebody who answers for it." "Remember" ×6 rewritten.

**Ch. 3.** Orla glosses Meter and Shutdown path, and says Hand is between her and Mara. The
warm-line call is now **naming the door that is coming** ("Hand", "Still"), not saying *one*
(seed §3/§11: control is the call said aloud). "They did it eleven times" and "counted *one,
two*" are gone; the first clean drill is fourteen seconds. The seven-column field books are
replaced by **Orla's debrief asked aloud at the lane** (What went wrong / Who was hurt / What
it cost / Second go / Why); Kiva has no answer to Why and Orla takes "I don't know." Perrin's
jealousy now comes out when Orla asks him the questions. The walk to the post is cut (the
movement's one post beat is now Ch. 8). Orla's private section: the Annick catalog card and
notebook become her 2664 visit to the Order's house, where the Warden gave her tea by a cold
window and told her what the Order believes (one compressed image set, no full dream). Ilse
named Kiva before the watch (seed §2, 2669), Orla not present. The second-page sponsorship
application becomes Orla stopping at the foot of the Placement Hall steps and not going up.

**Ch. 4.** Opening tally of drill times and the book page become a short spoken debrief
(Perrin / My dignity / Perrin). The bout's "file", "logged", "counted a point" go. Kiva calls
*Hand* and *Still* at the threshold. Kellan's backstory: no grading book; his mother called the
batch Third at her bench, and the other graders stopped work until the Works heard both sides on
the open floor (fix round 1). His creed is now things done in front of everybody versus behind a
shut door. Kellan's notes on
paper become him going back to the empty ring and testing the riser himself. Mara no longer
reads the book: she asks, Kiva tells it from the beginning, shows meter and shutdown path, and offers her
own hand as the third ("It's still my hand"). "Steady eyes" → "dark eyes". The chapter ends on
Mara warming the supper (fix round 1).

**Ch. 5.** Tram: "Call it." Ysra's brief: no "write it down", no ledger card; roles are
declared aloud and the team acts on them (fix round 1: no clerk repeating them). "Card" → the
call throughout. "Counted" and "did the sum" are gone; the needle countdown is thinned. Last line "Eight and two." cut.

**Ch. 6.** *Hand* as the warm-line call. Kellan decides on what he watched her do (fix round 1); "Graywater would write it
down" and "on the card" gone; "to his face" gone. The card-filling scene and the `Why:` entries
are replaced by the three of them sitting in the ash while the clerks sweep; Anwen's confession
stays, and "I want that said / It's said" is replaced by "I'd have done it if you'd come out."
/ "I know you would. That's the part." Ysra: "Bring your lecturer." Contrasts cut from 8 to 3.

**Ch. 7.** Orla answers for the ward-holder at the cart "one and then the other" (no
entries). "Did you call it?" Doran Mace keeps no ledger. Rhea asks who sponsors the girl on the
cell and tells Doran to find out where Dane teaches her (no run record). Anwen's written list
lines become thought. The Ch. 1 "incident report" quote is now Ch. 1's actual line ("Three years
ago a cell ran hot under your hands…"). The core rings the Works; Mara tells Kiva what Rusk said
in the winter (no letter). Mara goes to Rusk herself ("I've never yet let a wire do my
talking"). The field-book entry and "Writing it down so somebody can" are gone; the chapter
ends with Kiva at the window watching Mara walk up Coper Street before seven.

**Ch. 8.** Ysra does not read a book; she rules on what she watched in the run. Conditions:
"your sponsor sees you work every week, in a lane, with her own eyes." Orla's sponsorship is
one word and the stamp (Ch. 1's rule): "Sponsor. Dane." Ysra writes it and stamps it. The
Hanley Street register, the 2604 and 2446 entries, the clerk's copy and Kiva copying three lines
are cut (§5 beat 5, D). Instead Mara, on the Works bench on Hanley Street after seeing Rusk,
tells Kiva what she saw in 2676: every light on the Eastbank out and back "like a blink"; the
Works put it down to the rig. Mara's third condition is now that every night Kiva gives her the
left hand and she presses the two fingers ("The truth, not the brave one"). Mara reads *O. Dane* on the
sponsor line, says "Heaven help her," and signs; the walk home ends on the two of them walking.
Rhea's plate room and draft cards become her going
over the run in her head (she had a pocket glass on the girl from the gallery) and telling Doran
"Not for draft this season"; *Corran's. … Mine.* is a thought. Rosters post on the Placement Hall
basement board. Old Yard: no book; "Why is it crooked?" / "I don't know."

## 3. Renames applied

- Measure Hall → **the Placement Hall**: Ch. 4 (1), Ch. 8 (3: Ysra's office, the roster board,
  now in the basement per seed §12). Also added in Ch. 3 (Orla at its steps).
- Rule Nine, Team Eleven: 0 uses in Ch. 2–8. The Ch. 3 elevens (§8.4: "the team, the hour")
  were drill repetitions and the drill time, not the team; all cut.
- The Gates: Orla's Jessamy trial is "at the Regional Gates" (Ch. 8).

## 4. Dependencies fixed (from the ticket)

- Ch. 3:411–413 Annick card / notebook → the Warden's chair in 2664 (§5 beat 4). The Warden
  "sixteen years ago" in Ch. 25 now has its source.
- Ch. 3 field book → Orla's debrief aloud; every later M1 reference (Ch. 4, 5, 6, 7, 8) removed.
- Ch. 4:415 "steady eyes" → "dark eyes".
- Ch. 7:353 now quotes Ch. 1's surviving line.
- Ch. 8:81 field book → Ysra rules on the run she watched.
- Ch. 8 2446 / 2604 lamp entries → Mara's eyewitness of 2676 only.
- Mara's word **Hand**: Ch. 2 (written and explained), Ch. 3 (Orla), Ch. 4 (Kiva offers her own),
  Ch. 8 (Orla's hand; Mara's closing line).

## 5. Canon conflicts flagged (nothing invented)

1. **Packet 001 "One historical fragment should make the dream harder to dismiss."** Canon
   drops the only one M1 had (the register lines). What carries it now: Orla's 2664 memory of the
   Warden (Ch. 3) and Mara's 2676 eyewitness (Ch. 8). The packet's exit line should be updated.
2. **The disk's delivery.** The prologue (pilot, done) keeps a "sealed appointment" delivered on
   Kiva's Kindling day; seed §2 says Corran named her before the watch in 2669. Ch. 3 now holds
   both (named before the watch; came to Coper Street on the Kindling day). Ch. 32 must not
   contradict either.
3. **Rusk's warning is spoken, but Ch. 10:303 still has a red-stripe review notice by post.**
   Compatible (Ch. 7–8 say the notice comes by the end of the week). Ch. 10:319–327 still give
   Mara "shop books" and "reconciling"; her job is now reading banks by hand.
4. **Hanley Street** is now the Municipal Works office (it was the district records office).
   Ch. 24–26 still use the Hanley Street records office and the Transient Register (§5 beats 5–6
   already cut them).

## 6. Dependencies created for later movements

- **No field book exists.** Ch. 9:297–347, 10:179/265 ("the three she had ruled for the
  children"), 11, 12, 13:81/127/181/361, 14:160/336/346, 15:181, 18, 19:83/177 all lean on it.
- **The warm-line call is naming the door** (*Hand*, *Still*), not *one*. Ch. 19:391's *one…
  two… three* is the old Rule Nine counting and goes with Rule Six anyway.
- **Mara's three words end in Hand.** Ch. 11:389 ("a meter, and a shutdown path, and a book")
  must follow.
- **Kellan's mother** was saved by the grading bench refusing to work until the Works heard her
  on the open floor; no book, no jar: Ch. 14:186.
- **Mast six**: Mara left the trim screw unturned and said why to Kiva; there is no cell-book
  entry. Ch. 12:423–427, 13:35–41, 14:330 cite "her reason written in its book."
- **Rhea wrote no draft card in Ch. 8**; she told Doran. Ch. 16:313 ("The first one was in the
  board's tray") and Ch. 24:221 depend on it.
- **Ysra's weekly condition** is that Orla sees Kiva work, not a book sent weekly (Ch. 9:297).
- **Mara's nightly condition** is pressing the two left fingers; it plants the permanent loss
  (Movement 5) and replaces "the book stays on the kitchen table."
- **Post budget**: Movement One's single post beat is Ch. 8. Ch. 3 no longer stops at the post.
- **First clean drill is fourteen seconds** (said once, Ch. 3), ten by the following Tuesday (no nines).
- **Ch. 9:287** Kellan: "That's what a card is for" calls back a Ch. 6 line that is now "That's
  what a call is for"; "dark steady eyes" (Ch. 1 and 4 now say dark); "The Chair wrote *no
  live-cell events*" (Ysra now says the condition aloud in Ch. 8).
- **Ch. 17:231** Rusk on "the household filing of the thirteenth… at the records office when it
  opened to file against yourself": Mara now goes to Rusk at the Works in person before eight, and
  the core tripped at a quarter to three (Ch. 7), not sixteen minutes to.
- **No clerk repeats declared roles back** (fix round 1); the call stands on what the team does
  with it.

## 7. Fix round 1 (verifier notes)

1. **Repeat-back clerk cut.** Ch. 5: roles are declared aloud and the team acts on them
   (Kellan: "I'll be at the chute with my back to you"; Anwen adds the clock call; Perrin: "Then
   I'll know when to get my hands out"). "So we know" is gone. Ch. 5:331 and Ch. 6:407 no longer
   cite the clerk.
2. **Readings no longer decide beats.** Kellan's choice on the stair rests on what he watched her
   do (the rail, the husk, the one thing shouted at the one person who could do it). Ch. 6's "one
   reading… another" is "Both of those happened, and I was there for both." Ysra rules on acts
   she watched (the rail, the husk stood off Cade, the boy on the stair going); Renn listened
   because what she said in the corridor came true. Rhea's "clock calls right" line is cut.
   Kellan's creed in Ch. 4 is now about things done in front of everybody versus behind a shut
   door.
3. **Kellan's mother** is saved by the grading bench: every grader put down her cups until the
   Works heard both sides on the open floor. No jar, nothing kept.
4. **Closing gestures.** The three words are printed once (Ch. 2 end); Mara writes them mid-scene
   in Ch. 2's evening section, which now closes on her going upstairs. Ch. 4 closes on Mara
   warming the supper. Ch. 8's river walk closes on the two of them walking on; the three-word
   echo is cut, so it no longer sits back to back with Rhea's *Mine.*
5. **Refrains.** "Fourteen seconds" said once. Needle readouts in Ch. 5–6 cut from 21 to 9
   (one-line "Seven and one / Seven and two / Seven and eight / Eight and one / Eight and three"
   gone; "Ten seconds. Fifteen. Twenty." gone); Ch. 5's section no longer closes on a timing.
   "That was one." cut.
6. "Understood between us", "straight between us" cut; "in order" ×3 → 1 (Mara, Ch. 7:75);
   meter similes varied (the time; the weather; flatly; without any expression).
7. Anwen's list is in her head throughout Ch. 4, 7, 8. Ch. 8 matches the prologue: Mara was on her
   feet in the third row when the lamps went out and got down to Kiva after.

Pattern counts, base 8491277 → first pass 1f96862 → fix round 1 (Ch. 2–8 together):

| Pattern | base | pass 1 | fix 1 | residue |
|---|---|---|---|---|
| said it back | 0 | 2 | 0 | |
| repeated | 0 | 2 | 0 | |
| reading(s) | 12 | 16 | 6 | reading glasses, reading the board, "reading it" (the cell by hand), "dreading" |
| in order | 3 | 4 | 2 | Mara Ch. 7:75; Orla's "gone through it in order" Ch. 3:365 |
| between us | 1 | 2 | 0 | |
| reading off / read off | 0 | 1 | 0 | |

## 8. Commit

See the commits on `feature/2680-prose-m1` (shas in the ticket reply).
