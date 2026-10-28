# Prose pass pilot: prologue, Chapter 1, Chapter 46

Ticket P1, 2026-10-28. Author seat O'Connor 1.3.2 (Monroe Jackson), Claude Opus 5.5.
Branch `feature/2680-prose-pilot`, based on `origin/main` 9e79575. Canon used:
`universe/SEED-2680.md`, `editor/MOTIF-BUDGET-REVISION.md` §5, §6, §8,
`BOOK_MAP.md` §8, `PROLOGUE_PLAN.md` §4, §5, §7.6, §8, packets 001 and 006, and the seat's
"Motif budget and anti-tic" rule. Tournament name: the Gates (owner-approved).

## 1. Numbers, before → after

Counts use `grep -oiE` on each file. *write-it-down* is
`(write|wrote|written|writing|writes) [a-z ]{0,20}down`. *count\** is
`\bcount(s|ed|ing)?\b`. *Free nine* and *free eleven* use the §8.5 filters, so fixed
quantities are left out. *Measure* is the case-sensitive tournament word.

| File | Words | write-it-down | ledger | notebook | record* | count* | free nine | free eleven | Measure |
|---|---|---|---|---|---|---|---|---|---|
| prologue.md | 16,621 → 17,366 (+4.5%) | 17 → 0 | 11 → 0 | 5 → 0 | 4 → 0 | 5 → 0 | 14 → 0 | 7 → 0 | 0 → 0 |
| chapter-01.md | 5,547 → 5,147 (−7.2%) | 3 → 0 | 7 → 0 | 0 → 0 | 5 → 0 | 5 → 0 | 5 → 0 | 1 → 0 | 3 → 0 |
| chapter-46.md | 7,238 → 7,308 (+1.0%) | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 23 → 0 | 6 → 0 | 5 → 0 | 0 → 0 |

The §8.5 and §6 mechanical checks, run on the three files from `manuscript/`:

| Check | prologue | ch. 1 | ch. 46 |
|---|---|---|---|
| Time given in counts (expected 0) | 0 → 0 | 0 → 0 | 6 → 0 |
| Counting as a habit or tactic (expected 0) | 0 → 0 | 0 → 0 | 2 → 0 |
| Fixed nines: posts / rings-grooves (each expected ≤4 book-wide) | 0/0 → 1/1 | 0/1 → 0/0 | 0/0 → 0/0 |
| Fixed elevens: an hour said once | 1 → 0 | 0 → 0 | 1 → 0 |
| Decimals (report only) | 0 → 0 | 13 → 8 | 0 → 0 |
| Rule Nine / Team Eleven | 0 → 0 | 0 → 0 | 0 → 0 |
| Ends on a count | no → no | no → no | no → no |
| §6 banned phrasings (expected 0) | 20 → 0 | 3 → 0 | 1 → 0 |
| §6 ledger/notebook/column-as-record | 22 → 0 | 7 → 0 | 0 → 0 |
| §6 theme words (remember, passed on, the reasons…) | 7 → 0 | 0 → 0 | 2 → 0 |
| §6 broad motif lines (targets: 0 / 1 / 0) | 58 → 0 | 11 → 0 | 4 → 0 |
| Closing `*Why:` entries | 2 → 0 | 0 | 0 |
| Prologue title contains "write it down" | yes → no | | |

The saying (*because the road isn't straight*) appears twice in the prologue: snapshot 4,
said flat by the trainer, and snapshot 10, quoted by a student as a joke. That matches
budget.

## 2. Main changes

**Prologue** (retitled *The Leaning Post*. Snapshot titles: 2 *The Annex*, 4 *The South
Lane*, 10 *The Stair*.)
- 1: Ruth's notebook is gone. The Turn is now the suggested one: Joel puts his boots on to
  go to his substation, then stays with the children until light. The watch runs, and the
  time is read once ("Quarter to twelve"). Joel's EMP explanation is cut by about 40%.
- 2: Teo's ledger and its "why" column are gone. The Board's fuel man comes down, and the
  price is said to Teo's face: two hours of a line-crew man's Thursday. Teo answers with
  his own name. Old Farrow's grid explanation is trimmed.
- 3: Aud Fenn's written record is gone. The same news, theories, and Pell's line are now
  spoken at the mill.
- 4: Rebuilt. Oriel learns the lane dark, calls the turn, and says who has the bar. She
  asks why it leans and gets the flat answer once. She stays the four slow days her
  director wanted cut. She treats the crew at a cost she says aloud ("Three drams… That's
  what it costs"). The "lid" theory is said once, at a fire, and nobody confirms it.
- 5: The ledger is gone. The abort is called aloud, and two other people call it back.
  Ines's notebook line is now her own thought. The recall lecture is trimmed. "Slow count
  of thirty" became "half a minute."
- 6: "The reasons," the ledger-eating goat, Gideon's counting under his breath, and every
  "nine hours / nine weeks" are cut. The reactor lecture is about 45% shorter. The Turn:
  Gideon puts the question to his crew at the bench and they start that day.
- 7: The news-sheet transcriber is gone. The signing book and the *Why* column are gone.
  *Check the pairs* is said down the speaking tube and answered. "Eleven degrees" became
  "twelve."
- 8: The license book and its *Why* column are gone. Femi's refusal is "pass," not "sign."
  The cell boxes keep their meter and red handle, but their "little ledger" is cut. "He
  counted up" became "he looked up."
- 9: The ledger became "the rule." The company book entry became Hob saying, aloud, what he
  will tell the standings board. The nine-minute harness became eight. "Corran" (a place
  name that clashed with Ilse Corran) became "Lisk."
- 10: Rebuilt as the lane-drill committee and the stair, per §5 beats 1 and 2. Marisol owns
  the boy's injury. The vote is not close. Lyle quotes the saying and laughs. Rudd says the
  Line keeps its lanes dark, and Orme answers, "That is the Line's business." On the stair
  the Warden recruits Marisol and gives Annick's images as the Order's belief. No catalog,
  no manual, no Annick papers, no pencil line.
- 11: The ledgers are gone. "Nobody opened at more than one" is deleted, so the third door
  now surprises. "Kiva went eleventh" is cut. "Substation fire" became "Tallow fire" to
  match the seed and Ch. 2. The early mention of the post is cut, so the post is a single
  beat at the end. The assessor now tells Mara to her face that she has "no name for what
  that was" (§5 beat 3).

**Chapter 1** (retitled *No Name for It*)
- The column legend is cut. One sentence keeps Call's dark column, and the readings teach
  the rest.
- Ysra's policy speech is down about 50%: no record, file, or incident report. Sponsorship
  is now "you answer for her." The form is stamped and its lines are said aloud ("Sponsor,
  none").
- The bios of Ysra, Orla, and Perrin are each cut by about a third to a half.
- On the steps, Kiva now chooses out loud and with an action: she hands back the bun and
  says she is done waiting for a board, and that she will put the form in front of Mara now.
- Line edits: "steady/steadily" 9 lines → 0 (one "unsteady" remains). "It was not X. It was
  Y." 4 → 0. "Which meant" 3 → 0. "Not unkindly" and "checking a weight against a scale"
  are cut. The heat-lines get one full description and two short ones, where there were
  three full ones. "Could see the scar from the door" became "Even from the step."
- Record items cut: "Write it, please," the clerk's ledger, the banner *WE WROTE IT DOWN*
  (now *SIX HUNDRED YEARS OF LIGHT*), *ROWAN INSTRUMENTS & RECORDS*, Mara's paper ledgers
  (now Works tags), and Anwen writing on her list (she now adds to it in her head, aloud).
  Mara's bank and meter work stays.
- Counting tics cut: the clerk's *Nine… Ten… eleven*, "count to thirty," "ask them to
  count," "a board could count."

**Chapter 46**
- Kiva's control is now the call said aloud. She takes the *in* on the slack by feel, a
  hair before Dray calls it. The sequence calls are now *Hand* / *Ember* / *Still* /
  *Planted*, not *One… Six*. The handoff to the still-doors is *Now* on each slack, not
  "go in fives." Dray calls *out* and *in*; that is the call, not a count.
- Every count is cut: the fives against fours, the fours of the arm, "the count's
  S. Dray's," the spawn's "count" (now its haul and ease, its rhythm), and Perrin hearing
  "two counts." The apron man no longer counts turns on his fingers. "Stuck at seven" became
  "stuck short of home," and "Nine! She's seated!" became "That's home!" The bar now comes
  up hard against its stop, and the yard hears the shaft.
- Record items cut: Rhea's six-column slate, Vane's written direction (now spoken aloud),
  Anwen's green book "reading the why" (she now asks aloud what it's for and what it costs),
  "I'd like that written," Ysra's "page," Orla's "paper," Aske's "card," Noa's "column" and
  "page," and "longer than anybody had kept the reason."
- In the pump house: no "counting sixty aloud," no numbered cards, no "count against both,"
  and no "*The count of a thing.*" Lumb's minute-calls go from 8 to 3 ("five-and-twenty,"
  "halfway," "that's my sill"). Mara's reading hand feels the water lie still. Her tune
  readings stay as flavor ("Three… Five… Seven… Four").
- Noa's notch is now "about a dozen seconds… the same every time," per §8.4. Dray's closing
  line keeps its content without numbers. The two numbered kill calls (*One!*) are cut.

## 3. Canon conflicts and gaps (flagged; nothing invented)

1. **Team Eleven / Rule Nine.** There are 0 uses in these three files, so nothing was
   renamed here. Canon gives no new name for Team Eleven. For Rule Nine it gives new wording
   ("A change called aloud is declared when it is called") but no new number or name. The
   owner needs to decide both before the Ch. 3, 19, and 20 pass.
2. **"Measure Hall."** This is a building (Ch. 1, 4, 8, 14, 24, 26, 33, 35, 48), not the
   tournament, and `NAME-OPTIONS.md` does not give it a new name. Ch. 1 now says "the
   placement hall" in lower case. Other chapters still say "Measure Hall" until the owner
   names it. "Junior Measure" became "the junior singles," following the Gates option's
   event names. None of the three files names the tournament itself, so neither "Regional
   Gates" nor "National Gates" was needed here.
3. **The gate's state between Ch. 43 and Ch. 46.** In §5 beat 13, Ch. 43's drill already
   has "the bar comes up hard against its stop" and the water lying still. Ch. 46 has the
   gate "stuck short of home since Tuesday" until Perrin and Lowen run it home (seed §8,
   M6). I kept Ch. 46's version and put the stop in Ch. 46. Ch. 43 should show the bar
   meeting silt or stopping partway, or this needs an owner ruling.
4. **Lines in Ch. 46 that now depend on other chapters:**
   - Anwen's condition is now asked aloud, not read from her green book. The green book is
     in Ch. 35, 36, 42, 44, and 48.
   - Rhea's "I cut, and look after" assumes Ch. 44:161 drops "I count after."
   - Mara's cut callback to "*the count of a thing*" still has its source in Ch. 42:183.
   - Dray's *out*/*in* call assumes Ch. 39 becomes Brask's *in*/*out* rhythm (§8.4).
5. **Packet 006** still says the Pit action was under "written field direction." Ch. 46
   makes field direction spoken. The packet text needs the same change.
6. **Prologue length.** The prologue is up 4.5%, within ±15%. The rebuilt snapshots 4 and
   10 are scenes and run longer than the record beats they replace. The exposition trims
   in snapshots 1, 2, 5, 6, and 7 make up part of the gain.

## 4. Before/after excerpts

**Prologue, snapshot 11 (§5 beat 3).**
Before: "We'll write it down," she said at last. "All three. Classification deferred." She
turned to Mara. "I'm sorry. I don't know what else to put. There isn't a column for this."
After: Then she turned to Mara, and said it to her face. "All three," she said.
"Classification deferred. I'm sorry. I've been reading children on that bench for thirty
years, and I have no name for what that was."

**Chapter 46, the handoff (§8.4).**
Before: She did not look. She was counting. She counted on from her own six, to make a
five of it and not a four. *Seven. Eight. Nine.* The thing had fours. It bit on the first
of each…
After: She did not look. She was feeling for the slack. The thing hauled and eased under
her heel, and it bit hardest at the top of each haul… on each ease, in the slack, she took
the weight a little further down into the ground.

**Chapter 1, the steps (cold-read fix).**
Before: And she decided something she had been circling around for most of a year. She
was not going to wait any longer for a board to tell her what she was. She was going to go
into the Cellhouse and do something that a board could count.
After: She stood up and put the last of the bun back into Perrin's hand. "I'm done waiting
for a board to tell me what I am," she said. … "I'm going home now, not tonight, and I'm
putting that form in front of Mara."
