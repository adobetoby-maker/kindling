# Prose pass, Movement Six (*Why It Is Crooked*), Chapters 41–45, 47, 48

Ticket M6, 2026-10-28. Author seat O'Connor 1.3.3 (Monroe Jackson), Claude Opus 5.5.
Branch `feature/2680-prose-m6`, base `origin/main` 4677a03. Canon used: `universe/SEED-2680.md`
§3, §6, §8, §11, §12; `editor/MOTIF-BUDGET-REVISION.md` §5 (beats 8, 11, 13, 14, the Lumb beat),
§6, §8.2, §8.4, §8.5, §8.7; `BOOK_MAP.md` §8; `packets/MOVEMENT-006.md` (read with the ticket's
correction: direction is spoken in the moment, nothing written); `CHARACTERS.md`. Style anchor:
Chapter 46 (pilot, DONE), which was not touched (`git diff --stat` lists only the seven chapters).

## 1. Numbers, before → after

Patterns as in the pilot and M1 reports (`grep -oiE`). *Free nine / free eleven* use the §8.5
30-character filters (so "twenty-nine" counts, and the posts/rings are left out). *X/Y* is
"It was not X. It was Y." plus "It did not X. It Y.", checked by hand after the pass.

| Ch. | Words | write-it-down | ledger | notebook | record* | count* | free nine | free eleven | Measure | aloud / to … face | X/Y after |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 41 | 7,264 → 6,985 (−3.8%) | 1 → 0 | 0 → 0 | 1 → 0 | 1 → 0 | 7 → 0 | 6 → 0 | 4 → 0 | 1 → 0 | 1/0 → 0/0 | 3 |
| 42 | 6,479 → 6,260 (−3.4%) | 3 → 0 | 1 → 0 | 0 → 0 | 0 → 0 | 9 → 0 | 4 → 0 | 5 → 0 | 0 → 0 | 2/1 → 0/0 | 1 |
| 43 | 6,882 → 7,276 (+5.7%) | 1 → 0 | 0 → 0 | 1 → 0 | 2 → 0 | 22 → 1 | 4 → 0 | 1 → 0 | 0 → 0 | 4/0 → 0/0 | 3 |
| 44 | 5,583 → 5,337 (−4.4%) | 2 → 0 | 1 → 0 | 1 → 0 | 0 → 0 | 11 → 0 | 6 → 0 | 3 → 0 | 0 → 0 | 1/1 → 0/0 | 2 |
| 45 | 5,297 → 5,159 (−2.6%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 4 → 0 | 3 → 0 | 3 → 0 | 0 → 0 | 3/0 → 0/0 | 2 |
| 47 | 6,368 → 5,618 (−11.8%) | 2 → 0 | 3 → 0 | 0 → 0 | 0 → 0 | 4 → 0 | 4 → 0 | 5 → 0 | 1 → 0 | 1/1 → 0/0 | 1 |
| 48 | 6,573 → 5,613 (−14.6%) | 2 → 0 | 2 → 0 | 0 → 0 | 0 → 0 | 6 → 0 | 5 → 0 | 6 → 0 | 6 → 0 | 7/0 → 0/0 | 2 |

The one count* left is Ch. 43's "for the first time in his life he had not counted the rivets"
(Kellan), kept per §8.4 as the one place counting is named, as a thing he stops doing. All seven
chapters are inside ±15%. Ch. 47 and 48 lost the most because the canon cuts were whole scenes
(the slip readings, the keeper's book, the slate readout, the watch sitting, the editions,
the proof sheet and its columns).

**§8.5 and §6 mechanical checks**, run on the seven chapters (output reproduced by
`.foreman/scratch/check.sh` and the inline greps; not committed):

| Check | Result |
|---|---|
| Banned phrasings (expected 0) | 0 |
| Ledger / notebook / column-as-record | 0 |
| Theme words (remember, passed on, the reasons…) | 0 |
| §6 broad motif lines (target 0) | 67 → 0 |
| Closing `*Why:` entries | 0 |
| Time in counts (expected 0) | 29 → 0 |
| Counting as habit or tactic (expected 0) | 0 |
| Free nine / free eleven | 32 / 27 → 0 / 0 |
| Fixed nines: posts / rings-grooves | 0 / 1 (Ch. 48, the Reader: "the plate of nine rings that the first teachers carried") |
| Fixed elevens (an hour) | 0 (every "eleven" hour and the wardens' "eleven of them" were varied) |
| Decimals (report only) | 0 in all seven (figures are said in words: "five and sixty-two held") |
| Measure / Measure Hall / Rule Nine / Team Eleven | 0 |
| Chapter ends on a count | none |

## 2. Main changes

**Ch. 41.** Mara's "trunk book", Kiva's field book ("left and right"), Rhea's slate and its
fourth column, Pike's tally of Pru's crossings (34/30/4), "Write me his name… and nine more",
"four in, and four out", Mara counting the rise six times, the sealed half-sheet prediction, and
"Write that down while it's still only arithmetic" are gone. Mara now puts the date to it across
the table ("Twenty-eight. On Monday the third…"). Seven's accounts are a spend scene with figures
said, no signing, no read-back. Perrin's plate hold is "Hold made" from the master; no clerk counts
to thirty, Kiva does not count with him. Noa's columns are a spoken trend. Perrin's line is "I
don't mind" (no "I'd like it known"; Ch. 46's "I've been saying that I don't, since Thursday" still
lands). Ends on Mara's plan to walk the main up from the pump house with corks (sets up Ch. 42).

**Ch. 42.** Required cuts (§5 beat 13) done: no "sheet older than that plan", no Noa-to-the-Library,
no "to write down what she had not found", no "longer than anybody had kept the reason"; *leaning
toward* kept. **The float:** Mara has walked the main up from the pump house dropping a cork at
each manhole and watching for it at the next; on Stopgate Kiva watches at the lower grating. Above
the gate, in the School's gully, where the Works' plan shows the main straight, the cork goes in
with two buckets of Ansty's kettle behind it and never comes down to the grating below the gate;
Mara cannot say where the main goes. Sunday's flat puddle and Kiva's palm along the wall find the
turn under the post. "Recopied from the worn sheet, 2553" is gone; Mara reads the ruler-straight
line herself ("Somebody's tidied my drain"). Aske's card is spoken. "The count of a thing" → "a
thing's time". Pike's drill: no "sixty counts", "One! Corners!", "Fifty-one", "fourteenth",
"eleven times". The carry drill: no litter tallies, no book on the forearm, no "Say it back". The
Vane/Orla exchange loses the manual, the ledger and the Library; Orla asks him to run it the Line's
way, dark, before he cuts it, and Vane sets the drill for Monday night (Ch. 43). The post now has
its short iron bar through the top (seed §5; prologue snapshot 4).

**Ch. 43.** Mara's half sheet (39, 47, 203) → she says the assumption at the bench ("Stop the pumps
and the main lies still"); Rusk owns it as the Works' whole plan ("It was my plan before it was
yours"); after the box: "There. That's what I said at the bench… It doesn't." Kellan: no "Count
against it… threes"; he refuses the floor's time. Yarrow "I've time"; Pike says the open-ash rule
once ("about a minute"). The fill test has no countdown. "*Out* Two. Three. Four. *In*" → Kiva
feels the pull top out and calls late; Brask lets it hang longer. "if anybody's writing / It's
noted" → a joke without a record. Ysra *said* it at the Chair. The Library/manual/S.V. scene
(449–499 and the sealed paper at 523–553) is cut. **New, per §5 beat 13:** after drum twenty-eight
falls (Rusk hands Mara the job; she has the head-of-hill manhole lifted), Vane runs five of Seven
dark through the Old Yard as a Line drill: call the turn before the eighth, say who has the bar.
Kiva is planted in the still door on the cross, palms on the dirt, and feels the main. Perrin
reaches the bar: "Cade has the bar… Why does it lean?" Vane: "Because the road isn't straight."
(the saying's third and last use). Jude: "Talley has the bar." Perrin opens his still door; the bar
turns until it comes up hard against something dense; the shaft answers with a sound the whole yard
hears; the water under Kiva's hands falters, not still. Mara, from the manhole below the gate, felt
the rise and fall falter. "It's a gate." It is found, not shut.

**Ch. 44.** Opens on the dug shaft with the penstock hanging on its screw a hand into the water
(44:19). "*Two to the bar. Nine turns*" → "*Two to the bar.* Run it home." The old iron bar is
swapped for an ash pole (Ch. 46's bar). Silt in the groove jams it (44:319). Halloran's shelf
loses its cards, its "306 years", the read-aloud jar label and the signed write-off. Anwen's "I had
it written" → her own two questions, asked of Jude (sets up Ch. 46). Rhea's slate, its columns and
the ruled "Before" column are gone: she thinks; Pike says "You cut, and she pays after"; her line is
*I cut first, and I ask the price after* (matches Ch. 46); her conditions to Orla are spoken ("It's
an order I can ask in"). Dray: no count, no "eight to a breath", no pencil margins, and her third term
is spoken ("nobody takes it that I've come round"). Kiva's night-time page is now her own thoughts
on the tram. The quench-box entry is spoken, with Anwen's condition added. The 0.59 figure, "seven
turns", "two counts", "eleven handbells", "nine days" are gone.

**Ch. 45.** "you've been writing it down for a week" → "Tell whoever's standing nearest";
"Say it back" → "Call it behind you"; Vane's slate and written wire message → a runner with words;
Mara's wire slip read aloud (with timings) → a porter's spoken message; Kiva's numbered, timed knot
calls and her book cut; knot ordinals (ninth/tenth/eleventh/twelfth) → the top one, the last; "four
counts of haul" → "it hauled, and it eased"; Rhea's "Eight… I've cut two and there are eight" → "I've
cut two and it's no shorter"; Mace's card in a drawer and his board cut; Perrin's "I'd like it known
that I mind" removed (it pre-empted Ch. 46's confession). The chapter now closes on an action (Kiva
opens her mouth) instead of a declaration, so Ch. 46's "Then say it" still follows.

**Ch. 47.** Retitled *As Before* (was *Entered as Such*, a record phrase). The slips at 31 and 41
(three counts, six-and-twenty minutes, A. Renn's written note) are spoken by Ned. Breaking the
sealed reserve is four people saying yes; no entry read as written, no signing; Pru takes the other
side of the tin. **Lumb (171–199):** the keeper's book for 2604, the "T-0, four of them", the calf
page and Kiva's Library page are cut. Lumb comes up from his sump, knows the look, and says it under
the pumps: forty years ago, three nights' fever, the roof off and nothing over it, all four-and-twenty
needles standing up and looking, the levee lamps out and back of themselves, never told the Works
because a fever is not a fault. Kiva: "The roof was off." Lumb: "You know it." Kiva gives one line of
what the Warden told her Annick saw. Mara: older than you, wider. **423–426:** Mara tells Yeo the
reader has one hand until the eleventh month and Saltmere must send somebody to be shown on a box;
nothing is written. Vane's slate readout (timings, "four-and-twenty counts", the remarks column) is
now the Home Line's debrief at the cart, cost said before anyone leaves (§5 beat 8), with the pot
shared the Line's way. Pru's tag is a word said over a bag. The canvas book, the ledger older than
the School, E.K.'s 2471 line and "The watch sat yesterday" are cut; Kiva tells Vane once, on the
infirmary step, *I did not ask it anything. It did not do anything.* (§5 beat 11). Noa's sheets
and Yeo's wired column are spoken. Aske's "eleven weeks and four days. I've counted them" is gone.
Ends on Mara's and Kiva's hands on the table, not on a book.

**Ch. 48.** Per §5 beat 14. The Thursday hall is explicitly not a sitting of the watch: the Ferren,
Vane, Orla and Rhea, the bursar and the Reader. The Ferren to Kiva: *Rowan, K. Catcher. Hand as
before. A Line foreman may call you at a line-hand's day rate, with your sponsor's leave.* No
motion, vote, roll or ledger. The bursar brings the School's "plate" from the press because the
post made him look at what else the School retains; it is plaster. The Reader, who has packed that
cast every spring for thirty years, lays it beside Kiva's plate (wider fifth ring, flaw across the
third) and says which is which: a cast taken by leave of a bearer; the plate of nine rings the first
teachers carried, released by appointment. No label, editions, printer, Noa's drawing, or Ferren's
book. The result is read on the Placement Hall basement board (*The Regional Gates*; *National
Gates*; Ysra's line shortened, no "column/page"). Dray says it to Kiva on the Pit stair (her rule
goes to Saltmere with her name on it; objected twice, not changed her mind; would have seated her
on the lid); the fair-copied clerk's line is gone. Rhea's offer is spoken, not a card; Kiva's
condition is hearing the price before, not the slate's "before" column; Pike shows what a second
is for. The kitchen table closes the accounts in words (no signing, no "did the sum aloud");
Mara's eleven sheets for the coast boat are gone. Orla's Jessamy beat no longer turns on a letter
("the one who writes everything down"): a Saltmere officer brings his words. **Ending:** no proof
sheet, no columns, no pencil. The plaited junior: *Miss Dane says that we're to run it. Dark. From
the sheds.* Orla asks whether they should be told why it leans; Kiva has the speech and does not
give it: *Run it dark. Make them say who has the bar.* Then *Anwen. My cuff.* The book ends on the
junior in the dark: *Bettony has the bar! And me! We've got the bar!*

## 3. Renames applied

- Measure Hall → the Placement Hall: Ch. 41:473 (the *Held* board), Ch. 48:121 (the basement
  board), Ch. 48:211 (the steps, calling back to Ch. 1's steps).
- The Regional Measure / National Measure / "a Measure at Saltmere" → the Regional Gates / the
  National Gates (Ch. 47, 48).
- Rule Nine, Team Eleven: 0 uses in these chapters.

## 4. Dependencies fixed

- Ch. 41 → 42: the float (corks down each manhole, watched for at the next) replaces "a float in
  every grating with a mark beside it, twice a day".
- Ch. 41 → 43: the drum-twenty-eight call is spoken in the hearing room, so Ch. 43's sealed paper
  and Rusk reading it are gone.
- Ch. 42 → 43: Vane sets the dark drill for Monday night; Orla's "I'll hold the lamp for your man"
  pays in Ch. 44.
- Ch. 42 → 46: Aske says he will name the price himself, before (Ch. 46: "since I said that I
  would").
- Ch. 43 → 44 → 45 → 46: the gate is found, not shut, hangs on its screw, jams on silt, fitters work
  it from Tuesday, Perrin and Lowen run it home (Ch. 46, unchanged).
- Ch. 44 → 46: Rhea's spoken conditions to Orla are the order Kiva gives in Ch. 46; Anwen's two
  questions are set up; Dray's terms are spoken; Rhea's *I cut first, and I ask the price after*.
- Ch. 45 → 46: the chapter break still reads into "Then say it."

## 5. Canon conflicts flagged (nothing invented)

1. **The bar.** Seed §2/§5 and prologue snapshot 4 put an iron bar through the ninth post's top;
   the base Ch. 42 and the pilot's snapshot 11 describe the 2680 post without one, and Ch. 46 uses
   an ash pole. Resolved without new plot: the post keeps its short old iron bar (Ch. 42, 43, 48);
   the fitters drive it out for a longer ash pole for leverage (Ch. 44); the pole hangs on the wall
   afterward (Ch. 48).
2. **Why the bar turns in Ch. 43.** Canon has the screw turn in the drill but gives no reason a
   drill turns a bar. I used the Line's own lanes: Vane says their lanes end on a stake with a
   crosspiece that the first two in walk round, and Perrin, with his still door open, is strong
   enough to move a screw nobody has moved since 2390. Flat custom, no lore.
3. **Preserved-thing saves (§4b).** Two canon dependencies remain and are flagged: the sealed 2.0
   medical reserve opened for Mara's hand (packet 006 requires a shown medical need; Ch. 46 says
   there is no plain ward-trace in Meridian), and Halloran's plain reference shelf salting the bank
   (seed §5 names the shelf; Ch. 46 says "Every one's had its pinch"). Both are framed as ash spent
   at a cost, not as something kept that saves; the shelf's years, cards and jar labels are cut.
4. **Packet 006 still says "written field direction", "entered as such", "written limits" for the
   offer, and "a professional company makes a bounded offer… with written limits".** Per the
   ticket, I made all of these spoken. The packet text should be aligned.
5. **"Ch. 47 Ned's message" and "Vane's cart"** use runners and spoken words where the base used the
   municipal wire's printed slips; the wire itself is still there (the lodge clerk).

## 6. Dependencies created for earlier movements (for the M5 worker and later passes)

- **Rhea's line** must read *I cut first, and I ask the price after* wherever it was said to Kiva
  (base: "I cut, and I count after, and I'm thought very honest for it", Movement 5).
- **Orla's letter, Ch. 36:327** ("*There is another. She writes everything down…*"): Ch. 48 now has
  Orla having "sent word south in the seventh month" and an answer brought by a Saltmere officer in
  words. Ch. 36 should drop "She writes everything down"; Ch. 40's "had not written to be answered"
  line is echoed in Ch. 48 as "had not looked to be answered… said so, to a Placement Chair".
- **Dray's mast rule** is now "put to the Chair" (Ch. 44) and "granted this morning" (Ch. 48); any
  earlier "written to the Chair" should match.
- **The watch** does not sit in Movement 6 (Ch. 47's "The watch sat yesterday" is cut).
- **Kiva's "I can't weigh it"** is used twice in Ch. 41 and once in Ch. 42 (plus Ch. 46); earlier
  movements should not add more.
- **AUTHORSHIP.md** still lists Ch. 47 as *Entered as Such* (outside my write set).

## 7. §4b self-check (Ch. 41–45, 47, 48)

| Sibling device | Count after | Notes |
|---|---|---|
| Repeat-back ("say it back", "said back") | 6 → 0 | (Ch. 46 keeps its two; untouched) |
| A correct reading/instrument deciding a beat | 0 | Mrs. Renn's glass (Ch. 43 ×2, Ch. 47 ×1) and Noa's trend (Ch. 41, 47) are flavor; beats turn on what people do and see |
| Kept/sealed thing saving someone | 0 evidence saves | 2 canon reserve uses, flagged §5.3 |
| Number refrains, countdowns, timing closes, tallies | 0 | house "Fifty-eight" ×4 → ×1; drum "twenty-nine" ×8 → 0; ordinal knots → 0 |
| "I'd like that said/known", "understood", "All of it, in order" | 4 → 0 | Perrin's three "I'd like it known" outside Ch. 46 removed |
| Meter/gauge similes | 0 | |
| Crowd-witness payoff | 4 → 0 | "in front of forty people", "to the whole yard", "carried the whole floor" cut |
| Read-backs ("one at a time", "once more") | 0 | Kellan's account read-backs cut (Ch. 41, 48) |
| Counting as structure | 0 | |
| Ritual question lists | 1 | the Home Line's debrief at the cart, Ch. 47 mid-chapter (seed §6.2); Anwen's two questions as Ch. 46's setup (Ch. 44) |
| Documents as evidence | 0 | the Works' plan is looked at, not laid down as proof; the result board is canon |
| Timing objects as arbiter | 0 | |
| "aloud" / "out loud" | 19 → 0 | |
| "to … face" | 3 → 0 | |
| Shared tics "I'd like / I want / I'll not" | 51 → 31 | "I'll not" kept for Aske, Mara, Dray, the Ferren |
| Closing gestures (by kind, Ch. 41–48) | declaration aloud: 2 (Ch. 46 §1 "Yes.", untouched; Ch. 48 end, canon-mandated) | Ch. 45's close changed to an action so two do not run in a row |
| Refrains watched | "slow and even" 5 → 3; "keep/kept … time" 11 → 5; "haul" (Ch. 43) 6 → 4 | |

## 8. Commit

See `feature/2680-prose-m6` (sha in the ticket reply).
