# Prose pass, Movement Three (*First Season*, Chapters 17–24)

Ticket M3, 2026-10-28. Seat O'Connor 1.3.2 (Monroe Jackson), Claude Opus 5.5. Branch
`feature/2680-prose-m3`, base `origin/main` 8491277. Canon used: `universe/SEED-2680.md`,
`editor/MOTIF-BUDGET-REVISION.md` §5, §6, §8.2, §8.4, §8.5, §8.7, `BOOK_MAP.md` §8,
`packets/MOVEMENT-003.md`, the entry state of `packets/MOVEMENT-004.md`, `CHARACTERS.md`,
the pilot report, and the seat's VOICE.md. Write set: `manuscript/chapter-17.md` to
`chapter-24.md` and this file.

## 1. Numbers, before → after

Same patterns as the pilot report. *count\** is `\bcount(s|ed|ing)?\b`. *Free nine* and
*free eleven* use the §8.5 filters, which also catch hyphenated forms such as
"fifty-nine". *Contrast* is the count of true "It was not X. It was Y." / "It did not X. It Y."
pairs after a hand check. The "before" figure is a regex proxy and overcounts.

| Ch | Words | write-it-down | ledger | notebook | record* | count* | free nine | free eleven | Measure | aloud | "to … face" | contrast |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 17 | 5,833 → 5,860 (+0.5%) | 2 → 0 | 0 → 0 | 2 → 0 | 2 → 0 | 9 → 0 | 3 → 0 | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | ~3 → 0 |
| 18 | 5,106 → 5,105 (0.0%) | 4 → 0 | 0 → 0 | 1 → 0 | 0 → 0 | 13 → 0 | 3 → 0 | 1 → 0 | 0 → 0 | 1 → 0 | 1 → 1* | ~9 → 3 |
| 19 | 5,868 → 5,855 (−0.2%) | 3 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 11 → 0 | 12 → 0 | 4 → 0 | 0 → 0 | 1 → 3† | 0 → 0 | ~7 → 3 |
| 20 | 6,413 → 6,456 (+0.7%) | 3 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 14 → 0 | 5 → 0 | 3 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | ~6 → 2 |
| 21 | 5,857 → 5,783 (−1.3%) | 7 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 9 → 0 | 4 → 0 | 1 → 0 | 0 → 0 | 1 → 1 | 0 → 0 | ~5 → 2 |
| 22 | 3,961 → 3,930 (−0.8%) | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 11 → 0 | 0 → 0 | 1 → 0 | 0 → 0 | 3 → 0 | 0 → 0 | ~5 → 3 |
| 23 | 7,084 → 7,010 (−1.0%) | 4 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 16 → 0 | 2 → 0 | 4 → 0 | 0 → 0 | 1 → 0 | 0 → 0 | ~14 → 3 |
| 24 | 8,653 → 8,108 (−6.3%) | 9 → 0 | 1 → 0 | 1 → 0 | 2 → 0 | 10 → 0 | 7 → 1‡ | 8 → 0 | 1 → 0 | 3 → 0 | 0 → 0 | ~8 → 3 |
| **M3** | 48,775 → 48,107 (−1.4%) | 32 → 0 | 1 → 0 | 4 → 0 | 6 → 0 | 93 → 0 | 36 → 1 | 23 → 0 | 1 → 0 | 10 → 4 | 1 → 1 | — |

\* Ch 18's hit is a gaze ("then it came up to her face"), not the device.
† Ch 19's three are the rule's own wording ("called aloud", twice) and "'Ember,' she said aloud".
‡ Noa reading the tape in Ch 24: "Nine seconds and a little." This is the one Noa reading that
§8.4 allows. It is Movement Three's only free nine.

§6 and §8.5 checks run on the eight files. Full output: `.foreman/scratch/m3-checks.txt`.
- **Expected-zero checks, all 0:** banned phrasings; ledger/notebook/column; theme words
  (remember, passed on, the reasons…); closing `*Why:`; time in counts; counting habit;
  any `count*` word; free eleven; renames (Measure Hall, Rule Nine, Team Eleven); chapters
  ending on a count.
- **Broad §6 motif lines:** 0. "The book" survives only as the Circuit's home book of
  rules, the way canon uses it (17, 19, 20).
- **Fixed nines:** 1 ("the nine black posts", Ch 20); rings/grooves 0.
- **Decimals:** 19 → 4 (Ch 19's 0.10 and 0.44 board readouts; Ch 24's 3.0 price and 72.0
  standing). Ch 24's ash accounts are now said in words at the share table.
- **Refrain watch:** "haul"/"the slack"/"beat"/"steady" are at most 3 per chapter. The
  "step" hits are the licence tier, the Step, and wall calls.

## 2. Renames applied (§8.7)

- **Rule Nine → Rule Six,** worded "*A change called aloud is declared when it is called.*"
  - Ch 17: Brask's "I'd read Rule Six", and "What's Rule Six?".
  - Ch 18: Kiva means to ask Jude what Rule Six says.
  - Ch 19: the title is now *Rule Six*; Jude reads the rule; the referee's reading.
  - Ch 20: Lowen at line 15; the referee's ruling at 343, now spoken: "One change, called
    under home Rule Six, and made on the call."
- **Old echoes reworded:**
  - 19:455 is now the board's "*one change, declared*".
  - 20:15 now reads "the moment it was doing it".
  - 20:17 now reads "planned for the call… *When you hear her call, lift.*"
- **The new mechanic, carried through Ch 19, 20 and 23.** A call is declared the moment it
  is said, and the change may be made from then on, never before.
  - The slow way: stop, call, plant.
  - Kiva's fast way: call it as she leaves the ground, shut the Ember at the top, and set
    the stance as her foot lands.
  - Lowen hears the call and knows she is in the air with nothing open, so he lifts.
  - The old *one / two / three* is gone from all three set pieces. So are Kiva's "On three,
    it's theirs" (now "*Rowan! Still to dark!*"), Pru's "Gate on three" (now "*Finch! Gate
    off!*") and Brask's capstan "On three" (now "When I call *give*").
- **Measure Hall → the Placement Hall:** Ch 24 (the ash office).
- **Team Eleven:** 0 uses in Movement Three.

## 3. What changed, by chapter

- **17.**
  - The field book and the Why column are gone. The chapter ends on Orla's debrief, asked
    aloud at the lane, then the lamp goes out. It closes on Kiva's unanswered question, not
    on the debrief.
  - The post glance is kept (Ch 17 is the movement's one glance).
  - Druce's lecture names the open-ash window once ("open for about a minute"). "Sixty
    counts", "a slow hundred" and "inside the count" are gone. The foreman's "four columns"
    are now four spoken questions.
  - Rusk's hearing is rebuilt with no books:
    - Mara brings the quenched flat panel, not eleven years of books.
    - Rusk spots her left hand by the crimp of her seals.
    - Mast six is "you told the depot why".
    - The new job is reading masts and drums by hand at the reading rate. The Works' plan of
      the trunk, with its *S. link* label, replaces the "trunk's own book". The plan carries
      that plant to Ch 21.
  - Kiva's "counted one, four hundred times" is gone. Brask's notebook is now the home book.
    Kellan "wrote it down" is gone. Spends are agreed aloud, not signed.
- **18.**
  - The Kennel bagging drill runs on calls (*Dark*, *Corners*, *Haul*, "half the minute
    gone", *Sealed*). It no longer runs on a chant.
  - Druce's Kennel-book entry is now spoken ("Curved. Again.").
  - Kiva at the weir watches rather than writes, and the counting-iron frame is gone.
  - (Superseded by fix round 1, §7: the watch is now cut.) Kellan's watch was used once, at the end. The
    folded paper is gone; he pockets the watch instead.
  - The clerk's slate is now an officer's hand scale. Mara's copy-and-read evening is now
    Mara with the trunk plan and a tired hand in warm water.
  - The field-book ending is now Kiva going over the morning in bed.
  - "Since she was nine" is now "since they were both small".
- **19.**
  - Rule Six, as above. Noa's tape no longer goes into anyone's book. Kiva's tries are no
    longer numbered.
  - Kellan's "inside *two*" is now "inside your name". The Why entry is now thought.
  - Dray's objection is now "a dozen seconding" (was eleven signatures). She lays the
    Works' plan on the desk (she no longer copies it). Ysra no longer says "noted" or
    "written down".
  - The line judge's ten-count is now a raised hand. The New Lane's ninth post is no
    longer remarked on (post budget, below).
- **20.**
  - Lowen's POV is aligned to Rule Six. Pru's tap-counting is cut. "On your own count" is
    now "When you choose".
  - The score keeps its board digits. Lowen now says "One point" (was "Nine to eight").
  - The referee's card is now spoken. Orla's "I counted" closing is gone, and so is her
    "write it as a miss".
  - "You weren't counting" is now "You'd stopped calling… the door's just standing there"
    (the Ch 11 thesis line as canon rewrites it).
  - Tries 11–14 are no longer numbered. The second Kennel floor is argued aloud, with no
    Why read out. Druce no longer writes in the Kennel book. The chapter no longer ends on
    copying.
- **21.**
  - The field book and Vane's slate are gone. Vane's "I'm a slate" is now "I'm a foreman".
    His "I'll write down why" is now "Tell me what you call, and why, and I'll hold you to
    both". The slate entry is now "Company's call".
  - Kiva says the weir plate aloud (she no longer reads it out). Anwen's list is gone, and
    so are Dray's pencil and card.
  - "The count" (open ash) appears 0 times; the window is "while the ash is open". The Pit's
    capacity is no longer a number ("full").
  - Keeper's figures stay as spoken lines.
- **22.**
  - The bagging calls carry no numbers. The weir plate is "thought… and not trusted".
  - The grating countdown (*one, two, three, four… sixty counts*) is now a watched creep:
    the grey moves at a walking pace, it will be at the sump inside the minute, and the
    keeper wants four.
  - Vane's "for the slate… stand where I can count you" is now the field voice and "where
    I can see you".
- **23.**
  - The countdown frame is gone (*Forty-eight… One*). Vane's field direction is spoken.
    Orla says "it's mine. I'll not have it laid on her", not "write it as mine".
  - The crossing runs on the Rule Six call: "*Rowan! Ember, to still!*" as she leaves the
    lip.
  - On the shelf, Kiva holds the doors shut by calling the thread cold aloud ("*Ember,
    cold. Hand, cold*", like crusts to dogs), per packet 003. Dray says it for her when she
    fades. "Thank you for counting" is now "Thank you for calling it".
  - The dream no longer counts the lights. Brask's capstan runs on a called *give*.
    Perrin's "I'd like it said / It's said" is gone.
  - Rhea's draft card is gone. She tells Mace on the floor, and Ysra hears of it in person
    in Ch 24.
  - The keeper's book is gone ("I don't know what I'll tell the Works"). Vane's slate
    summary is now a short spoken account; he answers for Perrin's ribs.
  - The reserve is released by four spoken agreements and Kiva's raised right hand.
- **24.**
  - The cart: the reserve is "released", with no page and no signatures. Orla asks to hear
    it on Sunday; she no longer wants a page. The dream is told at Mara's table with no
    pencil. "Began → First felt" is now Kiva's own thought that night and a spoken
    self-correction on Sunday.
  - Mara's line ends "a meter, and a shutdown path, and a hand".
  - The grading: the test tune is no longer given in counts. The comb of reeds is
    unnumbered. The grader says the card's readings aloud.
  - Ysra's findings are spoken, framed by the foreman's four questions. "Recorded" and
    "written" are gone, and the rule change is in "the rules".
  - The share is said by the clerk (no slate).
  - The Twenty-Eight boy's eleven-teams count is now "a dozen" and the chalk at the foot of
    the board.
  - **The Hanley Street copy, the 2446 margin, the keeper's book and Mara's three older
    T-0 copies are cut entirely** (§5 beats 5 and 6).
  - **Dunmore chalks *T-0* on the rim**, at the foot of every lamp post, as trade habit.
    Noa asks what it means and is told only "It's what a keeper chalks". He does not know
    what it means, which matches packet 004's entry state.
  - The share division is spoken. Readouts are kept as speech. There is no writing,
    signing, list or book, and no "I want that said".
    - Anwen's two pencilled entries are now her saying them to Kiva's face over a cup.
    - The conditions are said back and checked aloud.
  - Noa's notebook, his copy, the slate, the draft card and his closing written line are
    all gone. The section ends on an action.
  - The Sunday yard:
    - The healer's bill is now spoken by Orla.
    - The debrief is said aloud.
    - Orla's "bearer's book / ledger older than this school / somebody wrote before him" is
      now what canon allows. The plate is held of the Home Line; a bearer names the next
      before their watch; Corran named Kiva; Vane stands watches and says the watch will
      want her before the summer.
    - The ending is "somebody had kept the page" in the old text. It is now Kiva carrying
      Orla's crate to the shed, which lines up with Ch 25's opening bargain.

## 4. Dependencies fixed, and coordinator facts applied

- **No field book exists:** applied. There is no field book, Why column, or written page
  anywhere in Ch 17–24, including at 19:83 and 19:177.
- **The warm-line call names the door:** applied.
  - 17:65 "*Still. Off.*"
  - 17:337 "*Still! Off!*"
  - 20:477 "*Ember! Off!*"
  - Ch 19's "one… two… three" is gone with Rule Six.
- **Mara's three words end in *Hand*:** applied (Ch 24).
- **Mara reads banks by hand, with no shop books:** applied.
  - Ch 17: Rusk's reading-rate job.
  - Ch 18: her tired hand in warm water.
  - Ch 21: "with my hand on the cells".
  - Ch 22's "a shop full of it" (the pens) is kept as setting.
- **Hanley Street, records office and Transient Register:** 0 uses in Ch 17–24.
- **Rhea wrote no draft card:** applied.
  - Ch 23: she tells Doran Mace.
  - Ch 24:221: she "came up my stairs on Thursday to ask it".
  - Ch 23's *Not to be expected twice* is now "*Not for draft this season,* she had told
    Doran then", to match M1's Ch 8.
- **Declared roles:** the roles are said to Druce (Ch 18) and to Vane (Ch 21). There is no
  team card in these chapters. No clerk repeats them, because no clerk is present at those
  declarations, and I added none.
- **The disk:** Ch 24's Orla says "Ilse Corran named you. I've known that much since you
  were thirteen and I saw it on you." This is consistent with both "named in 2669" and
  "came to Coper Street at her Kindling".
- **Post budget:** one glance, at the end of Ch 17. Cut elsewhere:
  - Ch 19: the plumb ninth in the New Lane.
  - Ch 24: the lane's last post, and the cross "at the crooked post's foot".
  - Kept, because they are action or terrain rather than the lean: the post Kiva hits in
    Ch 17, and "the post tilting up" mid-bound in Ch 19.

## 5. Canon conflicts and judgement calls (flagged; nothing else invented)

1. **The Order announced in Ch 24 (added plant).** Packet 004's entry state says "The Order
   of the Even Hand has asked to see her", but nothing in Ch 17–24 did that. Mara now says
   that somebody from the Order came to the pump-house door on Thursday, asked whether
   Kiva was at home of an evening, and said they would "come to Coper Street and ask you
   nicely". This is the Order's first mention in the book. It gives no doctrine, no images,
   and no pronoun for the Warden.
2. **Packet 004 says "three *written* conditions".** The prose now has the three
   conditions spoken and said back. The packet needs that one word changed.
3. **Two debriefs in the movement** (end of Ch 17 and the Ch 24 Sunday yard). Both are
   scenes where a debrief is the point, and neither closes its chapter. Ch 24's is
   partial: it asks only what went wrong and why.
4. **Closing gestures.**
   - Ch 21 ends on a call ("Not yet"), Ch 22 on Kiva's self-declaration ("Rowan. Seven.
     Catcher.") and Ch 23.1 on "Go". These are action cliffhangers from the original, and
     the call is canon's control device. I kept them. Flagged for the verifier.
   - Ch 20.6, the referee's spoken ruling, was followed directly by Orla's spoken lesson.
     The referee section now ends on action instead.
5. **Pit capacity.** My chapters no longer give the Pit a number. Ch 27, 38, 39, 40 and 41
   say "eleven hundred" six times, which would break the free-eleven cap. A later movement
   should drop the number or vary it.
6. **Mara's "I signed a paper on an embankment six weeks ago"** (Ch 24) points to Movement
   One, Ch 8:231 (she signs the form on the embankment). The beat is consistent with M1's
   committed text.
7. **Ch 17 Rusk** now says Mara "were at the Works door when it opened, to report
   yourself". It used to say she filed at the records office. If Movement One or Two keeps
   a "filing", it should say the same.
8. **"Nine seconds and a little"** (Ch 24, Noa) uses the single Noa reading that §8.4
   allows. Later movements should not spend another on the crossing's length.

## 6. Dependencies created for later movements

- **Ch 25** (still the old text) must change in several places:
  - 25:23 "Write that one in the right-hand column".
  - 25:157 "the field book under her arm".
  - 25:43–59 Noa's notebook, the Transient Register, and "I'll ask at Hanley Street".
  - 25:173 and 25:303 the Hanley Street clerk and the "register line".
  - Ch 24 no longer gives the Library any errand. The Warden's visit to Coper Street now
    pays off Mara's Ch 24 announcement ("ask you nicely", which fits the old title *Asked
    Nicely*).
  - Ch 25's crate bargain (out at eight, in at ten, until the thirteenth) matches Ch 24's
    ending.
- **Ch 26:** 26:57, 97, 109 and 277 still use the Hanley Street clerk, the register, and
  "Rowan Instruments" borrowing transient volumes.
- **T-0:** Noa knows only that "it's what a keeper chalks". Chalk is at the foot of every
  lamp post on the Pit's rim.
- **The watch:** Orla has asked Vane, and Vane wants Kiva before the watch "before the
  summer's out". This feeds Ch 32. Orla has not mentioned the Order or 2664, so the Ch 25
  and 26 reveal stands.
- **Rhea:** she asked Ysra in person for Seven to be attached, and "I'll take the shift
  myself" is spoken. Any later callback to a written draft card should change.
- **Kellan's watch** (his mother's) has been cut from Movement Three in fix round 1. It appears nowhere in Ch 17–24, so later chapters must not refer back to it.
- **Rule Six** is still to be applied at 36, 37 (including 37:233 "One change, called to a
  count") and 39, per §8.7. The mechanic is set in Ch 19:11 and 255.
- **Dray's "Thank you for calling it" / "Somebody had to"** (Ch 23) sits ahead of Dray
  calling Kiva's time in Ch 39 and 46.

## 7. Fix round 1 (verifier FAIL on sibling devices and caps)

Brief §4b was read before this round. Before → after counts are over Ch 17–24, from
`.foreman/scratch/m3-fix1-before.txt` and `m3-fix1-refrains-after.txt`.

| §4b item / refrain | before | after | What changed |
|---|---|---|---|
| Witnessed-by-a-crowd payoff | 10 | 0 | "the whole Pit heard/had heard" (23:7, 23:9) cut. "In front of every assessor" (24:101), "Out loud. With the Chair in the front row" (24:137) and "in the hearing of the whole ground" (24:231) cut. Orla's "in front of the whole ground" (24:463) is now "your healer took me at my word". Vane's "I have the catcher's file" (21:341) is now "Mark's where the Chair wants it. I've no cause". "I'll be saying so in a room on Friday" (23:603) cut. "Asked that his own name stand first" (24:209) cut. Rhea's "I'll say so to anyone who asks" (23:499) cut. Also cut: Lowen's "in front of four hundred witnesses" (20:41), Anwen's "in front of sixteen people" (24), Kiva's "say so out loud first" (19:217) |
| Read-backs | 2 | 0 | The conditions said back "one at a time" are cut. Kiva now says yes and visibly does not give her ready answer. Kellan's "went over it once more… Nobody had a figure wrong" is cut |
| "That's the rule" (dream told that night) | 2 | 0 | Now "I'll tell you all of it tonight" / "You will", and she goes down "because she could not lie still with it" |
| Kept-thing save | 1 | 0 | 24:51 is now "four people had agreed, in the time it took to say so, to spend what they had" |
| Ritual question list | Druce's four questions, plus Ysra's findings and the Ch 24 title | 0 | Druce's four questions cut (17:167). Ysra's findings are plain sentences. Ch 24 is retitled *Attached*. Ch 17 no longer ends on the debrief's *Why*: Orla stops at "Who was hurt?"; Kiva's question is her own thought after the lamp goes out, with the movement's single post glance |
| Distance countdowns | 6 | 0 | Cut: 20:89–91 "sixteen to the line / Four goes", 20:149 "twelve paces", 20:211 "Eight paces to the line", 20:279 "Ten paces". 21:371–375 "Twenty paces. Fifteen… Ten." is now the tread coming nearer |
| Try tallies | 2 | 0 | 17:381 "Six goes. Two drops, three jams" is now "That's the lot". 19:41 "tried six times / fallen over six times / twice into a post" is now "she's fallen over every time" |
| Watch reading settling a beat | Kellan's watch ×6 | 0 | The watch is cut from Ch 18. Rhea's economy is now Kellan's "I hardly saw it. I'm lit longer than that warming up". The weir tally ("446 of 480") is cut |
| Documents as evidence | 4 | 0 | The *S. link* label (17:287) is no longer quoted; Ch 21's Kiva asks "Is it locked?" instead of reciting it. The feeder label is not read; Mara tells her what the plates are. Dray lays no plan on the desk; she "went over the road on Sunday and looked". "I've read your file" is now "The Chair sent for me… told me what the objection was" |
| Number / board-line / declaration closes | 18.1, 18.6, 19.6, 20.4, 20.5, 22.3→22.4, 24.1 | 0 | 18.1 is now Druce looking back at the door. 18.6 is now Perrin's baker line. 19.6 is now the mustache thought, with no dram figure. 20.4 is now Kiva's heel taking the post. 20.5 is now the result in prose (no board line). 22.3 is now students walking back. 22.4 is now Kellan's action ("Carry" with no declared-to-nobody gloss). 22.5 is now the clerk's stare. 24.1 is now Orla walking off (no "Show me six"). One-word call closes are down to two (21.6 "Not yet", 23.1 "Go"): 18.5 got an action beat and 19.5 merged into 19.6. Ch 19's "*Rowan, K.: one change, declared. Dram, 0.44.*" board line is cut |
| Simile tics (cell/board/reading) | 5 | 0 | Cut: 18:105, 18:253, 20:235, 23:185 "as she would have read down a board", and 24:61 "as it rested on a case she was reading" |
| "inside the minute" | 9 | 1 | Varied: "quick", "in good time", "before the keeper's at his door". One kept: the Monday companies in Ch 21 |
| "inside the hour" | 4 | 2 | Aske and the clerk keep it; Anwen's two are cut |
| "four minutes" | 12 | 4 | Kept: the keeper's "Four minutes!" (Ch 22), the referee's carry length (Ch 19), Rhea's "three times in four minutes" at the weir (Ch 18), and "twenty-four minutes past ten" (Ch 24, a clock time the pattern also matches) |
| "twenty-two" | 9 | 3 | The mark is now "two paces past your heel" and "further from the lattice than I'm told to be". Kept: Mara's "twenty-two minutes past ten" and Ysra's restatement of the time |
| "four hundred" | 11 | 6 | The rest are "four hundredweight" (a fixed spec, twice), "four hundred and nineteen drams", Perrin's "four hundred kilos", and Kiva's "I've done that four hundred times" (once) |
| "It likes a gate" | 3 | 2 | Bettan's original (Ch 18) and Rhea's echo (Ch 23); Anwen's in Ch 20 is now "leave it something to lean on" |
| "went over it" | 4 | 1 | Now "turned it over", "thought about the morning", "told it plainly" |
| "make a bill out of that" | 2 | 1 | Ch 24 is now "Let her send me a bill for that" |
| "Get that straight" | 1 | 0 | Now "Don't make anything of it" |
| "I'd like" | 15 | 3 | Two Perrin jokes and one other |
| "I want" | 14 | 5 | Anwen's private *I want it*, Rhea's command, Jude, and two others |
| "I'll not" | 11 | 7 | Now Orla's (4), Vane's (1) and Mara's (2) register; Jude, Anwen and the keeper switched to *won't* / other phrasing |
| Ch 23 contrast pairs | 6 | 3 | 23:79, 23:189 and 23:297 rewritten in this round, along with the race-end, Rhea's fist and the after-floor pairs. Kept: "She did not wait for it…", "She did not pull…", and Rhea's "It had not broken… It had slid" |

Item 8: the Ch 24 Order plant is kept. On Sunday Kiva now thinks of the pump-house door,
opens her mouth to tell Orla, sees Orla's tired face, and does not. This is a choice, not a
device.

Re-run after this round. §6 and §8.5 expected-zero checks are all 0. Free nine: 1 (Noa,
Ch 24). Fixed nines: 1. Free eleven: 0. Decimals: 2. Renames: 0. Contrasts are ≤3 per
chapter. Output: `.foreman/scratch/m3-fix1-checks.txt`. Words: 48,107 → 47,702, and every
chapter is within ±15% of base (Ch 18 5,106 → about 5,000; Ch 24 8,653 → about 8,020).

Added dependencies:
- **25:285.** Orla "had given her a bearer's book at the Home Line hall… a man who had found
  another hand in a ledger". This contradicts Ch 24, where Orla offers only the watch and
  Vane. Movement Four must rewrite it.
- **25:35.** Noa's "The Chair's order says your consent in writing, every month" is a
  written-consent record. Movement Four should make the consent spoken.
- **Ch 25 and later:** nothing should call back to Druce's four questions, the *S. link*
  label, Dray's plan, or Kellan's watch. All four are gone from Movement Three.

## 8. Commit

See the reply for the sha. Scratch outputs are in `.foreman/scratch/` and are not
committed: `m3-before.txt`, `m3-after.txt` and `m3-checks.txt`.
