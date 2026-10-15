# Kindling 2680, Book Two — Movement Five — editorial and numerical review

> Built by TAC

Date: 2026-10-15. Reviewer: **Claude Opus 5.5 (`claude-opus-5-5`)**, Claude Code background session
(job `887082aa`). The owner directed that this review be done by this session directly. No penname-editor
skill, Codex, subagent or other model was used.

## 0. What kind of review this is

- **Same model, fresh context, informed. Not blind.** The drafting author of chapters 33–40 is recorded as
  Claude Opus 5.5 (`AUTHORSHIP.md`, Movement Five entry, job `dd002b97`). This session did not have the drafting
  transcript. It did have:
  - the compiled brief (packet, ledger, map, cast, bible, formula) as supplied in the prompt
  - the author's own continuity file and Movement Five ledger block
  - the Movement Four review and repair

  This is **not** a cold read, a human read or independent testing. The two reader lenses below are simulated
  perspectives, not reader research. A same-family reviewer shares the drafter's blind spots.
- **Coverage.** All eight supplied files were read in chapter order, in full: `manuscript/chapter-33.md` to
  `chapter-40.md`.
  - Size: 55,218 words by `wc -w`; 55,137 body words by the script tokenizer (headings and `---` lines excluded).
  - Integrity: every file is byte-identical to `editions/movement-005-first-draft/` (`cmp`: all same), and its
    SHA-256 matches the `AUTHORSHIP.md` table (§7).
  - Completeness: the movement is complete as planned, chapters 33–40 of 48. Chapter 41 does not exist.
- **Canon evidence used.**
  - Book Two records: `STATE_LEDGER.md` (sections 1–11 and the Movement One to Five blocks), `BOOK_MAP.md`,
    `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `packets/MOVEMENT-005.md` (all as supplied),
    `provenance/MOVEMENT-005-CONTINUITY.md`, `MOVEMENT-004-EDITORIAL-REVIEW.md` and `MOVEMENT-004-REPAIR.md`.
  - Targeted greps of Book Two ch. 17–32 (lane rules, declarations, the 12th's Tarn lane in ch. 24).
  - Targeted reads of **Book One** (`books/book-2680-opening/manuscript/`): ch. 23–24 (the Pit and the night
    the page was written), ch. 1 (Classification Day) and the prologue (Annick's catalogue card).
  - Labels used below:
    - **Verified:** a contradiction inside chapters 33–40, or between them and a file I read.
    - **Apparent:** a conflict that this evidence cannot settle.
    - **Plan:** a departure from the plan or packet, not a canon error.
- **Other files in the working tree.** At the end of this session `git status` showed edits to chapters 11, 14,
  15, 19 and 24, and new files `provenance/MOVEMENT-005-COLD-READ.md` and `AUDIO-HAND-COUNTS-REPAIR.md`, all
  written by parallel jobs. **None was read for this review, and nothing here depends on them.** The one exception
  is ch. 24, which was grepped for two lines (the Graving "was full"; the marshal's walk-round at the glass) in
  whatever state it was in at the time.
- **Formula source.** As recorded in the brief: SHA-256
  `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`. Sections 2–6 and 8–9 were used as given,
  including the ~1.7× and ~950 values.
- **No manuscript prose was changed.** No repair, no later chapter, no commit, no push. The only files this
  session wrote are this report and `provenance/tools/m5_metrics.py`.

---

## 1. Unscored reader response

**Where interest caught.** The first line has a boy with ink on both thumbs knocking at every lit door with a dead
man's name at the head of a page. *After D. Penhale, catcher… who went in by the book.* That is a superb
re-entry: it carries Movement Four's grief forward as print, not as mourning. Then comes "It's not for this week.
It's the week's crossing." I knew immediately what the movement was about. Kiva is keeping her one coin for
somebody else.

The movement peaks five times:

- **Thursday's lane (ch. 33 §5).** The hen ("It's trying very hard," said Kiva, "at sitting"), then "Elbows". Two
  catchers with no working fingers carry a dummy over a hurdle on their forearms "as one puts down a sleeping
  child". It is funny, physical, and earned by the injuries the reader watched happen.
- **Friday's adaptation (ch. 35 §1).** "She was not reading the lane. She was being read for." Carrow strikes on
  Treen's *set*, Kiva's own ladder word. Pru's answer is to carry with no hands, so there is nothing to read. Then
  "two places" lose the third carry. It is the best-built lane contest in the book: both sides adapt on the page.
- **The Salt Hall (ch. 36 §1).**
  - A laugh from the gallery at the lamp-man.
  - Adlam's five calf books: 48, 48, 50, 55, 57.
  - Kellan's "every dram but the dry tenth", and counsel's "Well done, Renn".
  - Perrin's "I'd sooner the low town were wet than that word was".
  - Kiva standing on the word *will*.
  - Then a cream letter in a large old hand.
- **Saturday's exchange (ch. 37 §3).** Perrin's mouth open on the count, and a shake of the head. Dray's face
  "was not a door. It was a person who has been told a thing she knew already, and finds that she minds it after
  all." "That's the fairest lane I've ever lost."
- **The Counting House (ch. 39 §2).** The far chair. "Were any of them white?" Kiva gives him the one thing that
  serves his reading, because withholding it would be "choosing a side by leaving a thing out of a column". Then
  the right hand over the eyes.

**Where it slipped.**

- **The Graving sitting (ch. 40 §0)** becomes a procession. In ch. 39–40 the reader hears the dream described
  by the Proprietor, Mara's page, Annick, the Ferren keeper, the Saltmere keeper, the Holloway return, a
  re-reading of the Proprietor's evidence, and Thrale. The Holloway reply and Thrale's price rescue it. But
  "no roof, nothing over, something attending" is said so often that it stops landing, and the packet warned
  against exactly that ("say each fact once where it matters").
- **Sums that a counting reader will catch** (§3a).
  - Thursday's lane adds to 7–2 on the page's own rules, not 6–2.
  - Kiva's tiers sum at 1 p.m. on Saturday forgets Old Four's live chance.
- **Two knowledge slips**, both at the movement's evidential core.
  - The Proprietor quotes "the Mercury" for ferry details only Seven heard.
  - Kiva's public list of occasions leaves out the Pit, which is the very occasion the sealed page records.
- **Paragraph mass in the hearings.** Several speeches run to 170–200 words in one block.

**Who matters.** Kiva, who chooses throughout; this is the movement in which she stops being a solo instrument.
**Pru** ("I'm not grateful. I'm only good."), **Perrin** (the shut mouth), **Dray**, the **Proprietor** and
**Thrale**. Both masters are given fair, unlike readings and a visible limit. **Kellan** gets a costly act of
his own, and **Mara** a costly one of hers. **Mara's** "That was the hardest thing I've done this year. Harder
than the low town." is the movement's best single line about guardianship.

**What I expect next.** The Slack on Wednesday at 6.09. Kiva's week's crossing spent when a link fails. The
thirty-six on thirty-six counts. The Proprietor's hand on the pumps. Thrale at the dock mouth. Kellan's white
card. Jude's answer to Yeo. Rhea's last night and the 30th.

**Would I continue?** Yes. This is a satisfying close to the competition, and the hearing turns the series'
private secret into a public fact without explaining it.

---

## 2. Scored dimensions — two lenses

These are lenses, not research. Scores are editorial judgments. They are not averaged and they are not a release
gate. Confidence (H high, M medium, L low) is how sure I am of the score.

### 2a. A fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Conf. |
|---|---:|---|---|---|
| Opening pull | 8 | ch. 33 §0 (33:3–29) | A boy, a damp page, a dead man's name, a girl with a bound hand. Concrete before any explanation. | H |
| Keep reading | 9 | ends of ch. 33 ("I've had the first returns"), 36 (the letter), 38 (the transit), 39 ("You've a dock at two") | Each chapter closes on a new person arriving or an open question. | H |
| Interest / freshness | 9 | the hen (33 §5); "being read for" (35 §1); "one voice" (37 §2) | Each lane has one idea a child can state: sit on it; carry with no hands; only one person talks. | H |
| Clarity / flow | 7 | 33:415 tally; 35:19 (88-word sentence); 39:197; the hearing exhibits in 36 §1 | The lanes are clear on one pass. The hearing is dense, and two slips (§3) make an attentive child stop. | M |
| Character attachment | 9 | 37:339–347 (Pru); 33:75–89 (Perrin); 38:283–321 (Anwen) | Agency and difference everywhere. Pru's scarlet, Anwen's not-red, and Jude's jaw all do work. | H |
| Humor / warmth | 9 | 33:355 ("at sitting"); 38:261 ("whether it was a cat"); 35:61 (Gower) | Character-grounded and well timed against the gravity of the hearings. | H |
| Action / suspense | 8 | 33 §5; 35 §1; 37 §3 | The contests are trackable and both sides adapt. A child may wait a long time for action between Friday 11 a.m. and Saturday 10 a.m. (ch. 35 §2 to ch. 36). | M |
| Progression payoff | 9 | 38:187–189 | "Not one mark of it was three doors." Seven reaches the roll by things other people can learn. | H |
| Connection | 9 | Penhale's page (33 §0); Holloway (34 §0 → 40 §0); the *Witnessed* page (40:267–273) | The Holloway lamp-man is planted, laughed at, and answered. That is the movement's cleanest arc. | H |
| Read-aloud quality | 7 | 40:295 (66-word *and* chain); "said the Clerk" ×29; "on the table" ×18 | Attribution is clean and dialogue has rhythm. Several long chains and very long speech paragraphs are hard to voice. | M |

### 2b. An adult genre reader

| Dimension | Score | Location | Reason | Conf. |
|---|---:|---|---|---|
| Opening pull | 8 | ch. 33 §0–2 | Grief made procedural (the printed page), then the calendar decision with the price said aloud. | H |
| Keep reading | 8 | strong through ch. 39; 40 §0 sags | The restatement of the dream across two chapters disperses the hearing's tension. | M |
| Interest / freshness | 9 | Adlam's books (36:161–167); Kellan's index (36:183–189); Thrale's price (40:193) | The hearing turns on old account books, a patent's wording and a cellar rule. These are specific, plausible institutional stakes. | H |
| Clarity / flow | 7 | §3b C1–C6 | Mostly clear. The arithmetic and knowledge slips will be caught by exactly the readers the book has trained. | M |
| Character attachment | 9 | the Proprietor, 39 §2; Thrale, 40 §0 | Two Glory masters with opposite, defensible readings, each with a visible limit, and neither a villain. | H |
| Humor / warmth | 8 | the Reader (38 §6); Carrow, 35:283–301 | Warm without breaking tone. | M |
| Action / suspense | 8 | 37 §3 (the exchange) | A loss chosen under declared rules, shown move by move. Masterly. Friday's door change between carries needs a rules line (C6). | M |
| Progression payoff | 9 | Carrow's "and no change" (38:45); Treen's "far edge" (38:51) | Seven's methods travel to rivals within a day. The plan's argument is shown, not stated. | H |
| Connection | 8 | Book One ch. 23–24 vs 34:107, 36:307, 39:217 | Rich payoffs, but the evidence chain omits the Pit occasion the page records (C4). | M |
| Read-aloud quality | 8 | 39 §2; 37 §3 | The best long sentences sit where they read best. Some hearing speeches are single 180-word blocks. | M |

---

## 3. Canon, physical state, power limits, knowledge and reserved disclosures

### 3a. Arithmetic: every lane, bracket, standing, place mark, clock, ash total and the crossing calendar

**Lane scoring rule** (ch. 18:39, unchanged): three for the litter over your own hurdle, one for a down, two
halves a down, and at the glass a point to the half the litter lies in. A call of "*Down.* The Tarn" means a Tarn
fighter is down, so the point goes to Seven. That is how the marshal's own tallies at 33:379 and 35:237 count it.

**Thursday, Seven v the Tarn second four (ch. 33).**

| Carry | Events on the page | Seven | Tarn | Marshal |
|---|---|---:|---:|---|
| 1 | Anwen downed (+1 Tarn); glass in the Tarn's half (+1 Tarn) | 0 | 2 | "Two to the Tarn. Nothing to Seven." ✓ |
| 2 | Tarn blade down (+1); catcher "Two halves. Down" (+1); glass in Seven's half (+1) | 3 | 2 | "Three to Seven. Two to the Tarn." ✓ |
| 3 | Tarn still door "*Down.* The Tarn." (33:403) (+1); "*Over… Three to Seven*" (+3) | **7** | 2 | **"Six to Seven. Two to the Tarn."** ✗ |

The page's own events give **7–2**. The printed result is 6–2: at 33:415, on the board (33:437), in "Six," said
Perrin (33:439), in the Lane line "sixteen for, twelve against" (38:145) and in "Six to two with no fingers"
(38:187). This is finding C1.

**Friday, Seven v the Ropewalk first four (ch. 35).**

| Carry | Events | Seven | RW |
|---|---|---:|---:|
| 1 | Kiva downed (+1 RW); over (+3 RW) | 0 | 4 ✓ |
| 2 | Lyle downed (+1 Seven); over (+3 Seven) | 4 | 4 ✓ |
| 3 | No downs; glass in the Ropewalk's half (+1) | 4 | 5 ✓ |

**Saturday, Seven v Team Twenty-Eight (ch. 37).**

| Carry | Events | Seven | TT28 |
|---|---|---:|---:|
| 1 | Jude downed (+1 TT28); over (+3) | 0 | 4 ✓ |
| 2 | Bannock downed (+1 Seven); over (+3) | 4 | 4 ✓ |
| 3 | Kiva downed (+1 TT28); Marten downed (+1 Seven); glass to Seven by a foot (+1) | 6 | 5 ✓ |

**Points for and against.** Using the printed scores: for 6 + 4 + 6 = 16 ✓, against 2 + 5 + 5 = 12 ✓. If C1 is
fixed as 7–2, the totals become 17 for and 12 against.

**Bracket.**

- **Thursday.** Drawn by standing after three, 1 v 24 … 9 v 16 … 12 v 13. Halden (1st) v 24th ✓. Old Four (2nd)
  at ten ✓. The Ropewalk first four (4th) v 21st ✓. Seven (9th) v the Tarn second four (16th) ✓.
- **Twelve winners.** Friday's six winners-against-winners lanes leave six fours at 2–0. Saturday's three lanes
  leave three at 3–0: the Ropewalk first, Westerley first and Holloway second ✓ ("won three", 38:145).
  - The three Saturday losers at 2–1 are Halden, Old Four and Holloway first ✓.
  - The twelve fours at 1–1 play six lanes, which gives six more at 2–1. That makes nine at 2–1 ✓ ("the nine who
    had won two").
  - Seven (W, L) and Twenty-Eight (W, L) are correctly drawn into the 1–1 group ✓.
  - Seven did meet the Ropewalk first four in the seeding rounds as well (ch. 17–18). The rule "no four to meet a
    four twice" reads as Lane-only. I accept that reading.

**Lane places among the nine at 2–1, by points for less points against.** Places marked * are the author's
off-page reconciliation (continuity §2).

| Lane place | Four | Record | Diff. | Marks |
|---:|---|---|---:|---:|
| 4* | Tarn second | L W W | +10 | 21 |
| 5* | Ropewalk second | — | +9 | 20 |
| 6* | unnamed | — | +8 | 19 |
| 7* | Holloway first | 7–1, 6–3, 3–5 | +7 ✓ | 18 |
| 8* | unnamed | — | +5 | 17 |
| **9** | **Seven** | 6–2, 4–5, 6–5 | **+4** ✓ | **16** ✓ |
| 10 | Halden | 6–2, 5–4, 2–5 | +2 ✓ ("by two points") | 15 |
| 11 | Old Four | 6–3, 5–4, 2–5 | +1 ✓ ("by one") | 14 |
| 12* | Westerley second | 5–4, 3–6, 5–4 | −1 | 13 |

If C1 is fixed as 7–2, Seven is **+5**. That **ties** the unnamed eighth four. The fix keeps Seven ninth (and the
Measure at 69) only if the reconciliation moves that four to +6 or better.

**The Measure (38 §4).** Every printed total adds up:

| Four | After three | Lane place (marks) | Total | Printed place |
|---|---:|---|---:|---|
| Ropewalk first | 58 | 1st (24) | 82 ✓ | 1st |
| Halden | 65 | 10th (15) | 80 ✓ | 2nd |
| Westerley first | 56 | 2nd (23) | 79 ✓ | 3rd |
| Old Four | 64 | 11th (14) | 78 ✓ | 4th |
| Holloway first | 59 | 7th (18) | 77 ✓ | 5th |
| Holloway second | 54 | 3rd (22) | 76 ✓ | 6th |
| **Seven** | **53** | **9th (16)** | **69** ✓ | **7th** |
| Twenty-Eight | 57 | 14th (11) | 68 ✓ | 8th (tie, won on the Hunt, first) |
| Westerley second | 55 | 12th (13) | 68 ✓ | 9th (best single place: Hunt, third ✓) |
| Ropewalk second | 46 | 5th (20) | 66 ✓ | 10th |
| Tarn second | 38* | 4th (21) | 59 ✓ | 11th |

- Seven's breakdown: Bench 19 + Carry 24 + Hunt 10 + Lane 16 = 69 ✓ (38:187 and Jude's line, 38:235).
- "On the roll by one mark": 69 against 68 ✓.
- Holloway second "ninth on the Bench and fourth on the Hunt" (38:7) matches the Movement Four (repaired)
  reconciliation ✓.

**Kiva's sum on the tiers at about 1:15 on Saturday (38:17–21) is premature (C3).**

- Her claim: "It's the Ropewalk's… if they beat Holloway's first four at three", and if not, "it's still not
  Halden's".
- Halden's 80/81 ✓ and the Ropewalk's 82 ✓ are right.
- But Old Four (64, 2–0) had not yet played Westerley first (2 p.m., 38:33). An Old Four win would make it 3–0,
  worth 64 + 22 to 24 = **86–88**, which wins the Measure outright.
- Kellan's two raised fingers at the same moment (38:27) rest on the same assumption.

**Ash book (Jude).**

| Day | Spend | Held |
|---|---|---:|
| Carried, Thu 17th | — | 6.26 |
| Thu | 0.31 (split off the page) | 5.95 |
| Fri | 0.42 (split off the page) | 5.53 |
| Sat | Pryce 0.15 + Talley 0.11 + Finch 0.12 = 0.38 ✓ | **5.15** ✓ |

- "Thirty-one, forty-two, thirty-eight. A dram and eleven." 0.31 + 0.42 + 0.38 = 1.11 ✓. "Held, five and
  fifteen" ✓.
- Rowan's doors are on her own thimble ✓. The sealed 2.0 W plain is unopened and bound. It was asked for in the
  Salt Hall and refused (36:255–263) ✓.

**Kellan's figures (36:179–189), checked.**

- 1,106 − 1,102 = 4 silent ✓. The four are named, and they agree with earlier movements: Seven's sealed medical
  (W full, I silent, M3); the Tarn's soot-cut jar (M3/M4); a pre-thaw tin; the Board's reference jar.
- 371.3 + 41.1 = 412.4 ✓. 371.3 / 412.4 = 90.0% ("nine-tenths") ✓. 371.3 matches the claims clerk's Hunt figure
  in Movement Four ✓.
- **1,175.1 drams in 2680 for the Meridian district is exactly the ledger's red rows:** 111 + 503.7 + 560.4 =
  1,175.1 ✓ (ledger §3). This is an excellent hidden check.
- Adlam's bench books: 48, 48, 50, 55, 57 ✓ (ledger M3.5).

**The crossing calendar.**

| Item | Page | Check |
|---|---|---|
| Sixth crossing Thu 10th; seventh possible Thu 17th | 33:59 ("Thursday's come… Soonest.") | ✓ |
| Warm mornings | Thu "Four… Monday, Tuesday, Wednesday, and today" (33:59); Fri "Five" (34:295); Sat "Six" (37:31) | ✓ |
| Aske's price said twice | Thu 7 a.m. (33:63) and Sat 7.15 a.m. (37:33) | ✓ |
| The rule as Aske states it | "If you go today, the next is Thursday week… the Saturday after" (33:63); "If you cross in a lane today, the next is Saturday next. Not Wednesday." (37:37) | one in seven ✓ |
| No crossing in the Lane week | Kiva fights stance, then stance/Ember, then Ember "and no change". The exchange is lost on one door (37:257–285). "She had not crossed once since Thursday the 10th" (38:189) | ✓ |
| Kept for Wed 23rd | 33:75; 33:473; 35:295; 37:41 | 13 days after the 10th ✓ |
| Three doors stay three clean | "She had not opened three doors since the fifth of the tenth month" (38:189) | ✓ |

**Dates and weekdays.** The third month began on a Tuesday, so the 12th is a Saturday, the 17th a Thursday, the
20th a Sunday and the 23rd a Wednesday ✓. The sixth month of 2680 began on a Friday, so the 25th is a Monday ✓
(the Reader's wax, 40:37). Mara sealed on a Sunday night in the sixth month, the 24th ✓. Her page is dated the
29th of the fifth month, 2680 ✓ (Book One ch. 23–24).

**Clocks.**

- **The tide.** Hart's quiet runs from 2:19 to 2:39 on Friday (35:313, 35:345), 20 minutes ✓, at "twenty-three
  minutes behind" the sea gate's table. So the table slack was about 1:56. Movement Four had Wednesday's low at
  12:20–12:21 and Hart's step of about 49 minutes a day; carried two days, that gives about 13:58 ✓. The harbour
  clock stays consistent across three movements.
- **"It's the neap" on Friday the 18th** fits the neap Movement Four put near the 16th–17th ✓.
- **The gate tape's hair at 00:52 Thursday** against the lower Mallow tear "at the bottom of the ebb": Wednesday's
  12:21 low plus 12 h 25 m is about 00:46 ✓.
- **The Salt Hall.**
  - Timeline: Board at 7; "It's eight" (chairman); Mara at 8:15; "twenty to nine"; Kiva stands at about
    8:41–8:42; the Proprietor's letter received at 8:56 (36:337).
  - The Proprietor says Adlam told him at 8:45 and he wrote at 8:50 (39:161).
  - Adlam must leave during Kiva's statement and reach the Counting House within about three minutes. That is
    tight but feasible on the Long Quay. Accept.
- **The Reader's custody.** She has "not let go of this since eight o'clock yesterday morning" (Fri 8 a.m., 38:261).
  A day-and-a-half transit puts her in at Sat 9:35 p.m. ✓. "Nine months" in the press, from the 25th of the sixth
  month to the 19th of the third, is about 8 months 24 days ✓. "Every hour for two days" by Sun 2 p.m. ✓.
- **Thrale.** Mara's wire of the 12th; she left Wednesday the 16th by ferry; a day and a half at the bow of the
  coast boat; landed Sat 4:50 p.m. (38:71). That is about 3½ days, against Seven's Sat 28th → Tue 1st on the same
  road ✓.
- **Thrale's hour in the Graving.** 2:00 → "twenty-five to three" (40:157) → "ten to three" (40:213) → leaves
  about 2:55 ✓. Aske's "Two Glory masters inside six hours" (40:287): 9:00 to about 2:50 ✓.
- **Ages and years.**
  - The Proprietor: 26 in 2604 (39:145), so 103 in 2681 ✓. "Seventy-seven years" ✓. "Four years in the house"
    makes him arrive about 2600, which matches the Halden heir's theft "the year I came" and the Reader's "eighty
    years ago" ✓.
  - Orla: 2664, "seventeen years ago" ✓.
  - Thrale: Master in 2670, eleven years past her gate ✓.
- **The jars.** 44 → 41 (made Master) → 40 (after Seven's 1.2) → 36 given + 4 left = 40 ✓.
- **The Clerk's dating of Annick, "between 2446 and 2450" (40:251),** matches Book One's catalogue card
  (*c. 2446–2450*, prologue 1041) ✓.

### 3b. Findings

Severity: **H** high, **M** medium, **L** low.

| # | Sev. | Kind | Location | Finding |
|---|---|---|---|---|
| C1 | **H** | Verified (score) | 33:403–415, 437, 439; 38:145, 187; continuity §2; ledger M5.2 | **Thursday's lane is 7–2 on the page's own rules, printed as 6–2.** In the third carry the Tarn still door is downed ("*Down.* The Tarn." She knelt.) and then the litter goes over for three. The marshal's tally skips the down. Fixing it to 7–2 makes Seven +5 in the Lane, which ties the reconciled eighth four (+5). Either the reconciliation moves, or Seven's Lane place (and the 69) changes. |
| C2 | **H** | Verified (knowledge) | 39:197 vs 37:19 and 36:301–311; 34:113 | **The Proprietor cites "the Mercury" for ferry details only Seven heard.** "The Mercury says you were lower than before, and that the lights were nearer, and that some were going out." Kiva said this only to her four, in a shut shop (34:113). In the Salt Hall she said "No roof, and nothing over, and the nothing paying attention." Ch. 37 states the Mercury "had not said what she had seen". At the hinge scene of the movement, a reader asks how he knew, and the only answers are a leak from the four or an error. |
| C3 | M | Verified (arithmetic) | 38:17–27 | **Kiva's tiers sum at about 1:15 on Saturday forgets Old Four.** Old Four (64, 2–0) still had a 2 p.m. lane. A win would make it 3–0, worth 86–88, outright first. "It's the Ropewalk's if…" and Kellan's two fingers are premature for a character the book presents as a good counter ("You'd make a grader"). |
| C4 | M | Verified against Book One | 34:107; 36:307; 39:217; ledger §2 | **Kiva's public list of occasions omits the Pit.** She lists "at thirteen… on Classification Day… and on the ferry" three times, including to the Board. The sealed page she asks the Board to open records the Pit on the 29th of the fifth month, 2680 (Book One ch. 23:235–256: the height, the roads, "This time there was sound", "She got as far as four and lost the number"; ch. 24:105–125: the page that night). The page's own "There were notes. That's new." (40:69) marks a distinct occasion. The Clerk's "at thirteen and since" (40:251) covers it; Kiva's lists do not. Source of the slip: ledger §2's "No recurrence since Classification Day, 2680", which Book One ch. 23 contradicts. |
| C5 | M | Verified (internal) | 39:207 vs 39:257 | **"It was the one piece of the dream she had kept, even from the page."** Fifty lines later Kiva keeps a second piece (the thing with no word), which "was not on Mara's page, because she had never told Mara". At the movement's most careful scene, the narration states something false about the very withholding it dramatises. |
| C6 | M | Apparent (power rule) | 35:203–205; ledger §2 (the Chair's conditions of the seventh month) | **Friday's change from stance to Ember between carries.** It is declared at the box and read at the mast, and the spring condition allows "any change declared". But the seventh-month condition says "no second door on any Circuit floor except a crossing declared to a count". Dray authored a mast rule, and Movement Four's ch. 28:57 has Perrin say "She can light it and nothing else, on that board, all day". Readers trained on these rules will ask whether a second door was opened in a crossing-free week. The page never says why this is a *change* and not a *second door*. |
| C7 | M | Plan (reserved cost) | 37:321 | **Dray's "You'll be on one in fourteen by then, if your healer's right."** Nobody on the page has said fourteen; Aske has priced the seventh crossing in sulking nights only. "One in fourteen" is the Slack's planned cost (map §3, §7). Here it arrives early, in a rival's mouth, from no source. |
| C8 | L | Verified (records vs page) | 34:187, 34:289; continuity §10; ledger M5.7 ("Has not touched a cell") | Mara lays her reading hand on training cells twice. The records' "has not touched a cell" should read "a bank cell". The distinction matters on Wednesday. |
| C9 | L | Verified (clock) | 38:287 vs 37:413 | Anwen: "Rhea Sorn pinned it at the baize at noon, after our lane". Rhea left the tiers to pin it straight after the 10 a.m. lane ("Come on"). Say "this morning". |
| C10 | L | Apparent (bracket reconciliation) | 33:435; continuity §2 | "Every one of the twelve lanes had gone to the four that stood higher", and the Tarn first four won. With 39 after three, it must have been 11th or 12th, which allows at most one unnamed four between 39 and 46. Also, the two unnamed Lane fours (6th, 8th) must be capped at 40 and 42 after three, or one of them outranks the Tarn second four's printed 59 for eleventh. Settle both in the reconciliation; the page does not need to change. |
| C11 | L | Clarity | 35:89, 35:265 | "On Saturday, against the Tarn" means the seeding lane of the 12th (ch. 24:33, 105: full, with a walk-round), which is correct. But two days earlier Seven played *another* Tarn four. Add "a week ago". |
| C12 | L | POV | 40:363 ("…and nobody saw him") | The closing survey asserts facts Kiva cannot know. It is house style (ch. 32 ended the same way), but "nobody saw him" claims the unwitnessable. Accept, or anchor it in her thought. |
| C13 | L | Apparent (knowledge record) | 34:323 | Orla read the Ferren keeper's leaf "over your aunt's shoulder in the autumn", and the Saltmere entry in Kiva's book. The ledger's §7 and M3.7 do not list Orla for either. The account is coherent (the book goes to her weekly), so update the records. |
| C14 | L | Draw wording | 37:3 | A draw by lot "had said what everybody in the loft had known it would say since the bag was opened". Read literally, a lot was foreknown. If the meaning is "since the clerk drew it", say so. |
| C15 | L | Style | 34:337; 38:143; 39:233; 40:241 | Four causal *since* remain, all in dialogue (Orla, the Clerk, the Proprietor, Mara). The packet asked for *because*. |

**Physical state: PASS.**

- **Kiva.** Left hand warm on four, five and six mornings ✓. Two fingers as before (Hart, 35:329; the Proprietor, 39:161) ✓. Right
  knuckles: the blisters rose Thursday, as Aske said (33:5), opened on the poles (33:311), re-wound at five, and
  stay in linen through Sunday ✓. She writes left-handed throughout ✓.
- **Perrin.** Seventh rib cracked. Aske finds the Wednesday lift ("A fortnight from Wednesday, not from Tuesday",
  33:115). This resolves Movement Four's carried owner item 3. He breaks the card again on Sunday night and Aske
  stops him (40:283) ✓.
- **Jude.** The arm is shown and examined at last. Aske's card: "edge on the right fist only; nothing gripped
  with the left till Monday" (33:139). He carries one-handed in every lane ✓.
- **Pru.** Ten caps. Two torn and bleeding Thursday (33:313). "Two of them fresh" on Friday (34:93, 35:99) ✓.
- **Others.** Dray: weight on the right (37:81) ✓. Lyle: no ward, stance leaning from the floor ✓. Trewin:
  frosted feet, boots two sizes too large ✓. Bridie: "stand on Friday" by report only ✓.

**Power limits: PASS, apart from C6 and C7.**

- **No crossing, stack or three-door.** One declared door per carry. The exchange is lost on one door, by choice,
  with the price spoken to Dray first.
- **The Saturday hurdle.** Kiva vaults on her Ember's bound and takes the litter on her forearms (37:233). That
  keeps to the letter of Movement Three's catcher rule ("hands off the poles while her declared door is open on
  the hurdle"). It is also exactly the point of "elbows" ✓.
- **Glory limits, both visible.**
  - The Proprietor: cannot lift his hand, so the Board comes to him.
  - Thrale: an hour in the town ("a day's work"), the sea at her back, grey by ten to three.
  - Neither does a student's or a fitter's work ✓.
- **The two masters' fields never touch.** The commission at nine and the Graving at two are separated. Thrale
  stands three hundred paces off at the gate. This protects the Slack's planned point of light, and it is a
  strength of construction.

**Knowledge boundaries: PASS, apart from C2, C4 and C13.**

- **The dream moves only by Kiva's decisions on the page.**
  - Decided between the mast and the wall (34:69–75).
  - Told in this order: her four first (34 §1), then Mara, Aske, Orla, Kellan, and the room.
  - She tells the four outright that she is holding one ferry detail back.
- **The white lights are given by choice**, against her own preference, for a stated reason (39:203–213).
- **The colour stays hers**: "not put on the table" (39:259–267). Mara learns only that it exists.
- **The Holloway lamp-man's name is withheld** at his request ✓.

**Reserved disclosures, against the packet's boundaries.**

| Item | Boundary | Page | Result |
|---|---|---|---|
| The dream | Public by Kiva's own choice; the sealed page opened before the Board | 36 §1 (asks); 40 §0 (opened with Mara, seal broken by both hands) | ✓ |
| "The Unroofed Sky" | First appearance in this movement, coined by a Board clerk from Annick's phrase | First use as a name is the Clerk's finding (40:255); then the *Mercury*'s late sheet (40:333). The chapter title was changed so as not to precede it ✓ | ✓ |
| The white lights | Hers at entry; may move by decision | Given to the Proprietor's commission (39:217) and read in the Graving | ✓ |
| The colour | "Stays Kiva's alone" (packet; map §13) | Its *content* stays hers. Its *existence* is now public: Annick's line read aloud (40:109), plus "A thing she has no word for. Not put on the table." (40:153). See owner item 1 | ✓ (owner) |
| The disk | Cold, even beside two masters | "It was cold… at the far end of the Proprietor's table… on the bench in the dock… through the fever" (40:347) | ✓ |
| The Slack | Not played; the Proprietor's letting-go not spent | Not played. Counsel withdraws only the *request to note* the Hunt claim, "for the present" (36:197). The patent claim stands for the court | ✓ (watch: do not let the withdrawal blunt Wednesday's) |
| The prediction seal | Not opened until noon on the 23rd; separate from Mara's page | "The sealed prediction in the Board's press will be opened at noon on Wednesday" (40:259); "a paper with a seal on it" in the press (40:365). Never confused with Mara's page | ✓ |
| Point of light, hull, "Breach", cause, what attends | Withheld | None. "Breach" 0. No explanation offered; the Board "can't say what was dreamed" | ✓ |
| New power property | None planned | Thrale's presence holds Kiva's fever down, which rises "all at once like water when a hand is taken off a pipe" (40:225). See owner item 2 | owner |

### 3c. The hearing: is it drama?

The packet asked for "a contest between people who want things, with a clock, a surprise, and a cost". Three
rooms:

1. **The Salt Hall (ch. 36 §1): yes.**
   - **The clock** is the Committee's midnight deadline and the Board rising at ten.
   - **The wants:**
     - Counsel wants the claim noted.
     - Adlam wants the patent defended truthfully.
     - Kellan wants the sum said whole.
     - The chairman wants the pumps kept.
     - Peverell wants to be "the keeper who let it be tried".
     - Mara wants the risk on her own name.
     - Perrin wants the word kept.
     - Kiva wants the page opened.
   - **The surprises:** the laugh, the bench books, counsel's "Well done, Renn", the tin demanded, the sister's
     announcement, the letter.
   - **The costs:** Kellan's card, Mara's name, the low town's eleven minutes.
   - **Weakness.** The first fifteen hundred words (the Chair, Noa, the returns, counsel) are a run of exhibits
     before anybody opposes anybody. The chairman is a type with a gold watch.
2. **The Counting House (ch. 39 §2): the best scene of the movement.** It is one question with a real dilemma: the
   white serves the opposing reading. Kiva's reasoning is shown, the cost is stated ("knowing what I'd do with
   it"), and the master's limit is visible in his hand. It also contains C2 and C5.
3. **The Graving (ch. 40 §0): drama in the second half, procession in the first.**
   - Breaking the seal with two hands is a strong image.
   - The page read in Mara's fault-report voice is very strong.
   - Then Annick, Ferren, Saltmere, three returns and a re-read of the Proprietor's evidence run as a sequence,
     with the reader already holding all of it. The re-reading of what the reader saw five hours earlier
     (40:147–153) is pure restatement.
   - **The new Holloway return (40:131–137)** is the surprise that rewards the sequence and should be its peak.
   - **Thrale's price** is the real contest: the chairman must sign, and Peverell writes it in her
     great-grandfather's book. That works.

---

## 4. Numerical formula alignment

**Method.** `python3 -I provenance/tools/m5_metrics.py manuscript`, run from the book directory.

- The script is a copy of `m4_metrics.py` (unmodified; its hash matches the one recorded in the Movement Four
  review) with only the chapter range, the output labels and the viewpoint map changed (diff in §7).
- The tokenizer, sentence splitter, syllable estimator and every lexicon are identical, so the figures are
  comparable with Movements Two to Four.
- "M4r" means Movement Four as repaired (`MOVEMENT-004-REPAIR.md` §5). Anything marked *manual* is the
  reviewer's judgment.

### 4a. Sentence rhythm — **the best distribution of the book so far; the long tail now meets target in narration**

| Metric | Target | **M5 all text** | M5 narration* | M5 dialogue | M4r all | M4r narration |
|---|---:|---:|---:|---:|---:|---:|
| Mean words | 14.6 | **10.5** | 12.3 | 6.8 | 9.55 | 11.0 |
| Median | 11 | **7** | 8 | 5 | 6 | 7 |
| Population SD | ~26 | **10.1** | 11.6 | 6.6 | 9.23 | — |
| ≤5 words | 27.7% | **40.6%** | 36.9% | 58.8% | 45.8% | 41.7% |
| ≥40 words | 3.3% | **2.3%** | **3.8%** | 0.2% | 1.7% | 2.7% |
| Longest | — | 88 (35:19) | — | — | 62 | — |

\*Narration has quoted spans removed. 5,237 sentences; dialogue is **32.5%** of words (M4r 28.9%).

- **The mid-band (6–39 words) is 57.1%** (M4 52.3%).
- **Per chapter.** The short share runs from 35.4% (ch. 36) to 45.5% (ch. 37). The long share is 1.5% (ch. 35)
  to 3.0% (ch. 37, 38).

**Read.**

- **Narration is near the formula's shape for the first time.** It has a median of 8, a short share of 36.9% and
  a long share of 3.8%, slightly over the 3.3% target.
- **The middle came back**, as the packet's craft notes asked.
- **The all-text gap is now mostly dialogue.** Dialogue is 59% short and makes up a third of the words. The
  owner question about whether the targets govern dialogue (open since Movement Two) is the only thing between
  this movement and the whole-text targets.
- **Two long sentences break the packet's "no *and…and* chains over about 45 words":**
  - 40:295, 66 words with eight *and*s
  - 40:143, 63 words, *and of … and of …*

  The 88-word 35:19 is a semicolon list of what Kiva told Kellan. It reads as summary, but it is the longest
  sentence in the book. The 73-word 37:257, the imagined crossing, earns its length.

### 4b. Paragraphs and scenes — **scenes too long, paragraphs heavier**

| Metric | Target (ASR proxy) | **M5 (typographic)** | M4r |
|---|---:|---:|---:|
| Paragraph median / mean | 18 / 26.8 | **25 / 38.0** (1,451 paragraphs; **23.6%** over 60 words) | 18 / 31.3; 18.5% |
| Section mean / median | ~950 | **1,414** (39 sections; 4 over 3,000) | 1,042 |
| Breaks per 10k, internal | ~8.7 | **5.62** | 8.06 |
| Breaks per 10k, with chapter openings | — | 7.07 | 9.59 |

Typographic breaks are not ASR pauses, so this is directional.

**Scenes.** The author joined 38 in-scene breaks on purpose. Every long section is one continuous scene:

- the Salt Hall, 6,117 words
- the Graving sitting, 6,422
- three lanes of 3,219–3,721
- the Counting House, 3,430

I read every join and found none across a change of place or viewpoint. **The low count is honest structure, not
a defect**, and the packet asks that hearings and fights stay unbroken. The cost is that the formula's ~950-word
rhythm is not met. Only the opening and closing chapters (33, 38) carry the formula's texture.

**Paragraphs drifted the wrong way.** The median of 25 and the 23.6% share over 60 words come largely from
hearing speeches set as single blocks:

| Paragraph | Words |
|---|---:|
| Kellan, 36:183 | 199 |
| Thrale's price, 40:193 | 192 |
| Mara's fitter's rule, 40:241 | 184 |
| Kellan, 36:189 | 179 |
| the Clerk's finding, 40:251 | 177 |
| Adlam, 36:161 | 170 |
| the Proprietor, 39:161 | 165 |

There are 75 paragraphs over 110 words. Read aloud, a 190-word speech without a beat reads as testimony, not as a
person. Inserting one gesture or interruption into each would also bring the median back toward the target
without cutting a word.

### 4c. Readability

| Metric | Target | M5 | M4r |
|---|---:|---:|---:|
| Flesch Reading Ease | 72.3 | **93.8** | 96.3 |
| Flesch-Kincaid grade | 6.8 | **2.8** | 2.2 |
| Syllables per word (estimator) | — | 1.21 | 1.19 |

- **Method.** Tokenizer: regex words. The splitter is guarded for Mr./Mrs./initials. Syllables come from a
  vowel-group heuristic with silent-e trimming. Names and terms (Peverell, Polglase, Arkwright, Proprietor,
  Westerley, Holloway) raise the estimate slightly.
- **Read.** The movement climbs toward the target for the first time in Book Two, driven by longer narration
  sentences and institutional vocabulary (patent, foundation, prediction, magistrate). Flesch still under-reads
  the procedural difficulty of bracket rules and bench books.

### 4d. Progression vocabulary — **rises at the turning points, as the packet asked**

The lexicon is unchanged from Movements One to Four.

- **Raw:** 268 hits = **48.6 per 10k** (M4r 29.4). Top hits: doors 139, Ember 23, Hold 20, crossing(s) 20,
  licence 18, crossed 12.
- **Manual adjustment**, by the same method as Movement Four.
  - **Doors.** I classified all 139 contexts with a reproducible script plus a hand pass. **59 are literal or
    figurative**: side, great, shop and office doors; "face like a shut door" ×4; "like a door in somebody else's
    house"; "the other side of a door". **80 are the door system.**
  - **Hold.** All 20 "Hold" hits are the role, not the verb, so none are removed.
  - **Adjusted:** 268 − 59 = **209 = 37.9 per 10k**.
  - **Crossed.** 11 of the 12 "crossed" are literal ("crossed at the wrists", "one thumb crossed the other").
    Removing those gives 198 = 35.9. Movement Four did not adjust "crossed", so **37.9 is the comparable
    figure.**
  - The automated literal-door grep removes only 18.
- **By equal-word thirds within the movement:** 80 / 112 / 76 (raw). The middle third (Friday's lane, the Salt
  Hall, Saturday's lane) carries the most, which is where doors, declarations and licences decide things.
- **Ash-economy terms:** 9.6 per 10k (M4 11.9).
- **Cumulative and provisional.**
  - Opening third (M1 + M2): about 51–55 adjusted per 10k (Movement Two review).
  - Middle third (M3 + M4): about 34.7 adjusted.
  - M5 opens the final third at about 37.9.
  - Everything after the opening third so far: (371 + 209) / 161.9k ≈ **35.8**.
  - **The provisional front-load ratio is ≈1.42–1.54**, against the source's ~1.7×. It has eased slightly
    because the Lane rightly turns on doors.
  - The whole-book 58 per 10k remains out of reach; the book will finish near 40.
  - This is the standing owner decision since Movement Two: the shape is being kept at the cost of the average.

### 4e. Development beats

**Kiva (manual): about 43 choices or realizations, about 7.8 per 10k** (target 4.5; M4 6.7). By chapter: ch. 33
×7, ch. 34 ×8, ch. 35 ×7, ch. 36 ×1, ch. 37 ×5, ch. 38 ×4, ch. 39 ×5, ch. 40 ×6. Representative:

- "It's not for this week… It's the week's crossing." (33:75)
- "Then we don't carry it." / the hen (33:323–337)
- "It wasn't on anybody's. That's why it worked." (33:429)
- A coin put by (33:475)
- "A second who never said it at all was not a second." (34:63)
- "A seal is not for keeping a thing safe." (34:67)
- She decides to put it on the table (34:73–75)
- "Her four, before anybody." (34:83)
- She holds back the ferry and says she is holding it (34:115–117)
- "He'd nobody with a pencil… I had you." (34:277)
- She tells Aske, Orla and Kellan first (34–35)
- "She was being read for." (35:165)
- "It gets easier. That's not the same as better." (35:283)
- "It's spoken for." (35:295)
- She asks a ruined hand to stand up (35:325)
- She stands in the Salt Hall (36:295–297)
- She tells Dray to her face (37:55)
- "Finch's." (37:101)
- She keeps the promise (37:241–243)
- She shakes her head at Perrin (37:263–267)
- "Not one mark of it was three doors." (38:189)
- The far chair (39:133)
- She gives the white (39:213–219)
- She withholds what she cannot name (39:259)
- "It was for the column." (39:293)
- The page heard without shame (40:91)
- "Nothing came… I'd tell anybody now." (40:319)
- The name she does not mind (40:339)

**The cadence is above target and even across the movement.** The one risk is restatement. The realization
"put a thing down where anybody could see it" recurs about seven times (33:475, 34:75, 37:285, 37:387 in Rhea's
mouth, 39:41 in Orla's, 40:339, and others). "On the table" occurs 18 times.

The regex proxy (86 windows, 15.6 per 10k) is reported only for reproducibility. It is inflated by the many
pronouns near "found that", "decided" and "understood".

**Supporting cast (manual).** At least 26 named people get a beat, and nobody becomes a deuteragonist:

| Person | Beats |
|---|---|
| Perrin | "Not wanted in the Lane"; owns the lift ("I'd do it again"); "I think we'll just go and look at the draw"; the Halden card refused, the grey kept; refuses the tin in public; *shuts his mouth on the count* |
| Pru | "Elbows"; "the first thing… that wasn't on somebody's word"; "If you say one word I'll stop and listen to you"; calls the pen; "I'm not grateful. I'm only good." |
| Anwen | teaches Lyle to lean ("I'd not say no to that because of a lot"); walks her wall away; "I'll be at your back"; Graywater, *yes*, told to Kiva first |
| Jude | shows the arm; the Company card ("after Wednesday"); "I never asked what you were for"; doesn't turn; writes *We'll stand where she stands* |
| Kellan | "That's not a sum"; *No… under my own name*; reads it whole; two fingers |
| Mara | asks only "Who first?"; two wires; "Mine."; the low town on her name; "the hardest thing I've done this year"; the fitter's rule |
| Orla | "Don't let anybody make you into doctrine"; asks the Chair to strike her line; one true sentence to Hart |
| Rhea | names *Mine* to herself; gives away Pryce's card; "the first time I've said a thing like that to you" |
| Others | Aske (the price twice; one day, not a week); Noa (the fourth column; wires Holloway himself); Hart (stands up; the sentence to Orla); Dray ("Read."; "the fairest lane"; "I'll be there"); Carrow ("and no change"; "on the wall"); Treen; Lyle; Peverell; Adlam; Pettit; counsel; the Chair (the third *Witnessed* line); the Reader; the Proprietor; Thrale; Gower; the Tarn captain; the Holloway lamp-man |

### 4f. POV word share (viewpoint segments, not name frequency)

**Segments** (0-based sections after splitting on `---`, from a fresh listing of every section's opening; the
Movement Four map is stale after the joins):

| Segment | Lens | Note |
|---|---|---|
| ch. 33 §3 | Anwen | |
| ch. 34 §2 | Mara | |
| ch. 36 §0 | Kellan | |
| ch. 37 §4 | Rhea | |
| ch. 39 §0–1 | Orla | §1 opens "He was on the gallery…" but is Orla climbing to Hart |
| everything else | Kiva | including ch. 40 §2's closing survey, which is narrated out from Kiva's bed |

Each cutaway opens on its lens by name and a private cue ✓.

| Lens | M5 words | M5 share | Cumulative M1–M5 (M2–M4 as repaired) | Cumulative share | Target |
|---|---:|---:|---:|---:|---|
| Kiva | 47,956 | **87.0%** | 233,178 | **86.6%** | ~87% (85–90) |
| Mara | 1,977 | 3.6% | 8,919 | 3.3% | 2.5–3.7% |
| Kellan | 1,377 | 2.5% | 8,206 | 3.0% | 2.5–3.7% |
| Orla | 1,565 | 2.8% | 6,488 | 2.4% | 2.5–3.7% |
| Rhea | 1,108 | 2.0% | 7,340 | 2.7% | 2.5–3.7% |
| Anwen | 1,154 | 2.1% | 5,011 | **1.9%** | 2.5–3.7% |

- **The cumulative total is 269,142 body words.** It is built from the Movement Four review's cumulative table,
  adjusted by the M4 repair's remapped deltas, plus M5. Expect ±0.1 point.
- **The book holds its target.** Orla is now just under the band, and **Anwen is the one lens clearly under it**
  (1.9%). Movement Six's plan has her leading a mixed ward line at the Slack, which is the natural place for an
  Anwen cutaway.
- **The author's count agrees.** `AUTHORSHIP.md` has Kiva 87.0% and 7,188 cutaway words. The script has 7,181,
  within tokenizer differences.

### 4g. Secondary signals (optional per formula §8)

| Signal | Source band | **M5** | M4r | Note |
|---|---:|---:|---:|---|
| "that" | 92.1 (tighten below) | **113.2** | ~96 | rose again, mostly in reported reasoning ("She found that…", "she knew that…") |
| just / almost / felt / seemed | 5–25 | 1.5 / 0.4 / 5.1 / 1.3 | — | — |
| -ly words | ~161 | 31.2 raw; **22.5** filtered | 19.2 | "slowly" **15** (the author's §0 reports 14 → 9; the script counts 15 whole-word hits in ch. 33–40); "exactly" 13, "carefully" 10, "lightly" 9 |
| Quote-adjacent tags | ~41 | **51.1** | 60.8 | "said the Clerk" 29 (5.3 per 10k) |
| Combat terms | ~22 | **8.9** | 16.2 | lowest yet, despite three fights; the lexicon misses this book's fight words (*touched*, *down*, *edge*, *half*). A lexicon limit, not an absence of action |
| "out of the" / "one of the" / "for a moment" | 2–4 | 2.9 / 1.6 / 2.5 | — | in band |
| House trigrams | — | "she did not" **15.4**, "did not look" 9.1, "he did not" 9.1, "looked at the" 8.5, "she looked at" 8.3, "it was not" 8.2 | "she did not" 13.2 | negation and the "looked at" family are rising again |
| Causal *since* | packet: *because* | **4**, all dialogue (C15) | 0 | — |

**Tics and voices (raw counts in 55.1k words).**

- **"I'd like it known" 1 (Perrin)** ✓, **"I want it said" 2 (Anwen)** ✓ and **"I'd want" 3 (Jude's heaviest
  lines)** ✓. The packet's voice rationing worked.
- **"I'd sooner" is the new shared idiom: 13 uses across nine speakers.** Aske, Perrin ×3, Kiva ×2, Mara ×2,
  Dray ×2, Orla, Thrale and Peverell. Dray's "I'd sooner you heard it from me" (40:357) echoes Kiva's to Aske
  (34:301).
- **"scarlet" 12** (Pru's tag, plus Perrin ×2) and **"face like a shut door" 4** (Dray's tag). These are
  intended voice markers, at the edge of audible repetition.
- **"the warm sound" 10.** The crowd-sound taxonomy (warm / long / the other) is a nice device. Ten uses is
  enough.
- **"as people look at a thing that has been sent for" ×3** (34:149, 36:347, 37:127). Planted, paid, and then
  paid again.
- "four thousand" 4; "the smallest thing in the hall/Graving" 2 (both as the author's §0 records); "nobody" 100.

---

## 5. Movement Four repair state in `STATE_LEDGER` against chapters 33–40

| Ledger item (M4 block, as repaired and rechecked) | In chapters 33–40 | Result |
|---|---|---|
| Unclassified; one door declared by her captain's voice | Every declaration is by Perrin's voice | PASS (C6 for Friday's change) |
| Left hand warm Mon–Wed; seventh possible Thu 17th; Aske says the price twice | Four, five, six mornings; Thu and Sat | PASS |
| Right hand burned; blister, "peel by Sunday" | Blisters Thu, opened on the poles; linen through Sunday. No peel shown, which is consistent with the reopening | PASS |
| Yes/no at a quarter to seven | Thu mooring ring; Fri gallery rail; Sat Graving lip; Sun bed rail (written by Pru, 40:307) | PASS |
| Disk cold | Cold at both masters and through the fever | PASS |
| Dream known to nobody new; white lights hers | Moved by decision on the page (§3b) | PASS (C2, C4) |
| The Proprietor's letter to Crest (Sat 12th) | The Chair's written answer, 5 a.m. Sun (39:17–19) | PASS (strong payoff) |
| Standings after three: Halden 65 … Seven 53 (9th) | 33:241 "(9)" v "(16)"; Thursday draw 1v24, 2v23, 4v21 | PASS |
| Book 6.26; sealed 2.0 bound | → 5.15; sealed refused to the Committee | PASS |
| Perrin cracked rib; lifted at the spur (owner item carried) | Aske finds it; card moved one day; "I nearly did" | PASS (resolved) |
| Pru: ten fingertips frosted | Caps; two torn Thursday | PASS |
| Jude: frosted arm, "not worse" (packet: let it matter or retire it) | Examined; carded; mending; a scar | PASS (retired well) |
| Penhale dead; Coombe's page out at five | 33 §0, his name at its head | PASS |
| Lyle ward gone; Carrow learning to declare | Lyle leans from the floor; Carrow "*edge. Declared. Single.*" and then "*and no change*" | PASS |
| Yeo wants columns; Ivey copying | Copied twice; Kiva at the Company yard "not a Lane night" (agreed, not held) | PASS (carry) |
| Rhea: one night left; card ends the 30th | Card for Pryce; will not write Kiva's before the 30th | PASS |
| Pike's hands close halfway | "closed halfway, as they had lain for a fortnight" | PASS |
| Mara has not touched a cell; thirty-six hands | Teaches at the training cells (C8); "I'll not touch a case" (36:241) | PASS (records wording) |
| Hart: springs dawn slack held; neaps walk with the table | Neap Friday 2:19–2:39; "near a quarter past six" at the springs | PASS |
| The 12.44 hair; Noa draws no line | A second hair at 00:52; "Two is not a column"; a fourth column, no line | PASS |
| Halden's claim on the red bags | Read under Kellan's own name; counsel withdraws "for the present" | PASS |
| Dray on two feet; "not changed my mind" | Kept to the last line | PASS |
| Owner items M4.9 ("It was the neap"; Penhale's frost ward; Orla "by sight") | Friday's neap is consistent; the other two are untouched | carried |

**The author's Movement Five ledger block and continuity file against the prose.** They agree with the page on
every dated event, injury, ash figure, offer and knowledge change I checked. Exceptions:

1. The Thursday score and "16 for" (C1).
2. "Has not touched a cell" (C8).
3. Continuity §0 says "slowly 14 → 9"; the script counts 15.
4. The ledger's Book One line "No recurrence since Classification Day" (§2) is contradicted by Book One ch. 23
   and has propagated into Kiva's lists (C4).
5. Orla's knowledge of the 2604 entries is not recorded (C13).

---

## 6. Repair brief — three priorities, bounded

**P1 — Make the sums and the evidence chain true (C1–C5, C7).**

- *Location:*
  - 33:403–439 and 38:145, 187 (Thursday's score)
  - 38:17–27 (the 1 p.m. sum)
  - 39:197 (the Proprietor's source)
  - 34:107, 36:307, 39:217 (the list of occasions)
  - 39:207 (the "one piece")
  - 37:321 (Dray's fourteen)
  - the continuity file §2 and the ledger M5 block, reconciled to whatever changes
- *Observed issue:*
  - A lane score that does not follow its own events.
  - A champion-by-arithmetic claim made while a rival could still win.
  - A master who knows what was said only in a shut shop.
  - A public list of occasions that leaves out the occasion the sealed page proves.
  - A narration line that the next scene falsifies.
  - A rival quoting the Slack's future cost.
- *Effect on the reader:* the movement's case rests on two things, numbers that add and a page that cannot have
  been borrowed. The trained reader will test both first. C2 and C4 sit exactly where the book asks to be
  believed.
- *Proposed scope:* line edits, no scene changes.
  - **C1** (choose one):
    - **(a) Preferred:** keep the down and make it 7–2 everywhere ("Seven to Seven", "Seven… With no fingers",
      "seventeen for, twelve against", "Seven to two with no fingers"). Move the reconciled eighth four to +6 so
      that Seven stays ninth and 69 stands.
    - (b) Make the Tarn still door a half that does not kneel, and rework her letting go. More invasive.
  - **C3:** put the conversation after Old Four's lane, or have Kiva add the condition ("…if Westerley beat Old
    Four at two"). Make Kellan's fingers come after three.
  - **C2:** "The ferry," he said. "Below the Order's house. Last month. Were any of the lights white?" Kiva then
    volunteers *lower* and *nearer* in her answer, which she already does at 39:217.
  - **C4:** add the Pit to each list in one clause. For example, "at thirteen… on Classification Day… in the
    Pit last spring, the night my aunt wrote it down… and on the ferry". At 39:217: "Not on Classification Day,
    not in the Pit, and not when I was thirteen." Correct ledger §2 in the records.
  - **C5:** "It was the one piece of the dream she had words for and had kept, even from the page."
  - **C7:** cut the figure ("You'll not spend it on a lane, this year or next"), or attribute it to Aske's sulk
    arithmetic said on the page earlier.
- *Strength to preserve:* the Lane's carry-by-carry calls; the Measure's reading from the bottom and the tie read
  in the Clerk's flat voice; Kellan's 1,175.1, which equals the ledger's red rows; the far chair; "That's not the
  same as keeping it."

**P2 — Turn the Graving's procession into a sequence that builds, and give the rules one line (40 §0; C6).**

- *Location:*
  - 40:95–117 (Annick read in full again)
  - 40:121–127 (the Ferren and Saltmere keepers quoted again)
  - 40:147–155 (the Proprietor's evidence re-read)
  - 35:203–205 (Friday's door change)
- *Observed issue:* in ch. 39–40 the dream's content is spoken by about eight voices. Two of the readings repeat
  text the reader saw hours earlier on the page (the Proprietor) or in earlier movements (the keepers). Friday's
  change of door is unexplained against a condition the book has taught.
- *Effect on the reader:* the climactic sitting loses tension just before its best moments (the Holloway reply,
  Thrale, the price). The rules-minded adult stops at Friday's change.
- *Proposed scope:* compress, do not cut evidence.
  - Summarise the two keepers' entries in one sentence each ("Peverell read her house's page herself, the long
    *s* and the white lamps, and sat down without a word").
  - Reduce the Proprietor's re-read to its one new line, Kiva's answer, and the Graving's reaction.
  - Keep Annick and Mara's page in full: they are the two documents the hearing exists to open.
  - Let the Holloway return land as the peak of the evidence run.
  - For C6, add one line at 35:205 or at the marshal's call, for example: "*A change between carries, declared to
    the box, with nothing open in the pause. It's on her card.*" That makes it a change and not a second door.
- *Strength to preserve:*
  - the two hands on the bone knife
  - Mara's fault-report voice
  - Noa's *N.B.*
  - "Read it… so that it belongs to nobody. And don't make it anything."
  - Thrale's price, and Peverell's pencil in her great-grandfather's book
  - "I'd sooner a house where nothing answers"
  - the Clerk's "for want of a better"
  - the third *Witnessed* line

**P3 — Paragraph mass and the remaining voice drift, narration and speeches only (§4a, §4b, §4g).**

- *Location:*
  - the hearing speeches over about 150 words (36:161, 183, 189; 39:161; 40:193, 241, 251)
  - 40:295 and 40:143 (the long *and* chains)
  - 35:19 (88 words)
  - "I'd sooner" ×13
  - "on the table" ×18
  - "sent for" (third use, 37:127)
  - "that" (113 per 10k)
- *Observed issue:*
  - The paragraph median rose to 25, with 23.6% of paragraphs over 60 words.
  - Two chains break the packet's 45-word rule.
  - A new shared idiom has spread across nine voices.
  - The movement's argument ("put it on the table") is restated about seven times.
- *Effect on the reader:* read aloud, a 190-word speech without a beat becomes testimony rather than a person. The
  repeated motif tells the reader what the movement means after the action has already shown it.
- *Proposed scope:* a focused same-author pass.
  - Break each long speech once with a gesture, an interruption or a reaction from the room. No words cut.
  - Split the two chains at their natural pause.
  - Recast about half of "I'd sooner", keeping Perrin's "I'd sooner be hated" and "I'd sooner the low town were
    wet", and Thrale's line.
  - Cut two or three of the "table" restatements in narration (keep the Clerk's, Orla's and Rhea's).
  - Drop the third "sent for".
  - Leave dialogue length alone until the owner rules.
- *Strength to preserve:*
  - **Do not shorten any lane, the Counting House, or the exchange with Dray.** They are the movement's earned
    length.
  - Keep the long sentences of the imagined crossing (37:257) and the planted lean (35:263).
  - Keep the short calls (*Set.* / *Elbows.* / *Walk.*).
  - Keep the closing survey's music (40:363–369), with or without C12.

**For the owner, not prioritised:**

1. **The colour's existence is now public.** Annick's line was read aloud, and the Board records "A thing she has
   no word for." The packet and map reserve the colour itself; this keeps it. Confirm that the *existence* may
   be public.
2. **A new interaction property.** Thrale's presence held Kiva's fever down, and it rose when she left (40:225).
   It is interpretive ("she understood now"), but it is new. Keep, or soften to "as if".
3. **Does the sentence target govern dialogue?** Dialogue is 59% short and a third of the words. Open since
   Movement Two.
4. **The progression shape (~1.4–1.5× front-loading) over the whole-book 58.** Confirm, as before.
5. **Section rhythm.** At 5.6 breaks per 10k, against the formula's 8.7, the joins honour the packet. Accept the
   departure for hearings and lanes.
6. **Old items still open:** Movement Four C16/C17/C18; Movement Three C13/C14/C21.

**Strengths to protect in any repair:**

- *After D. Penhale, catcher… who went in by the book.*
- "It's the week's crossing… If I spend it on a lane, I can't have it back."
- "I'd have given you a week more if you'd lied to me about it." / "That's why it's one day."
- "It's trying very hard… at sitting."
- "Elbows… I've carried coal like that."
- "She was not reading the lane. She was being read for."
- "It gets easier. That's not the same as better."
- "A seal is not for keeping a thing safe. It is for being opened in front of people."
- Mara's "Mine." at the training cell
- Hart: "It's let be asked one thing. *Quiet,* or *not.*"
- Kellan's "every dram but the dry tenth", and "Well done, Renn"
- Perrin: "It's two drams against a word."
- "*Rowan, Ember, declared, single, by her captain's voice, and no change.*"
- Dray's face that "was not a door", and "the fairest lane I've ever lost"
- "Not one mark of it was three doors."
- The Reader: "The guard asked whether it was a cat."
- "I'd been keeping it from you. That's not the same as keeping it."
- The Holloway reply: "IF THE GIRL CAN SAY IT TO A BOARD UNDER HER NAME HE CAN SAY IT TO HIS WARDEN UNDER HIS."
- "for want of a better"
- *Put it on the table herself, under her own name, before anybody asked.*
- *Fever, the third. Nothing came. Said so.*

---

## 7. Method — reproducible command, script hash and limits

Command, run from `/Users/drive/kindling-2680-book-02/books/book-2680-national-measure`:

```
python3 -I provenance/tools/m5_metrics.py manuscript
```

- `provenance/tools/m5_metrics.py` SHA-256 `9bb5f801c6bfb0e585cdd25897c669eb020786d5ca07d418ef7806a785f0eb49`
- It was copied from `provenance/tools/m4_metrics.py`, SHA-256
  `d38a4760e55d9ef0cdf5397c3c136e199062f57eb3c34019328f68669c645a55`. That matches the hash recorded in the
  Movement Four review, so the source was unmodified.
- Full diff (only the range, the labels and the viewpoint map changed):

```
2c2
< """Movement Four numerical pass (copy of m3_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m4_metrics.py <manuscript_dir>"""
---
> """Movement Five numerical pass (copy of m4_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m5_metrics.py <manuscript_dir>"""
6c6
< CHS = list(range(25, 33))
---
> CHS = list(range(33, 41))
10,12c10,12
< POV = {(26, 2): "Mara", (30, 0): "Kellan", (30, 1): "Kellan", (31, 4): "Rhea",
<        (32, 4): "Anwen", (32, 8): "Orla", (32, 9): "Mara"}
< # 32/10 opens on Ivey arriving but is narrated from Kiva's side of Quiller's counter, so it is Kiva (see report)
---
> POV = {(33, 3): "Anwen", (34, 2): "Mara", (36, 0): "Kellan", (37, 4): "Rhea",
>        (39, 0): "Orla", (39, 1): "Orla"}
> # 39/1 opens "He was on the gallery" but is Orla climbing to Hart; 40/2's closing town survey stays Kiva's section (see report)
```

**How the viewpoint map was derived.** Each chapter was split on `---` lines with the script's own regex. I
listed each section's index, its body-word count and its first paragraph (39 sections), then read every section.
I assigned a lens only where the narration stays inside that person and Kiva is absent or seen from outside. The
Movement Four map was not reused.

**Chapter SHA-256 at review time.** These are identical to `editions/movement-005-first-draft/SHA256SUMS.txt`
and to `AUTHORSHIP.md`:

| File | SHA-256 |
|---|---|
| chapter-33.md | 8912b98dd1ad0dce… |
| chapter-34.md | 7887460915affc59… |
| chapter-35.md | ab0c4f161e316dcf… |
| chapter-36.md | 772455ade509f93a… |
| chapter-37.md | 202ecefdb693d559… |
| chapter-38.md | 5926eed539ef7b52… |
| chapter-39.md | a2d8afcf2b8ec080… |
| chapter-40.md | e6d7be38ea313595… |

**Known limit of the inherited script.** Its `reserved_terms` check is case-sensitive and reports "Unroofed" 0.
Movement Five actually contains "the unroofed sky" at 40:255 and 40:369, "THE UNROOFED SKY" at 40:333, and
Annick's "the sky unroofed" at 34:67, 36:303 and 40:115. All are planned and inside the packet's boundary (§3b).
I left the definition unchanged so that runs stay comparable. A future script should match case-insensitively.

**Manual counts and their limits.**

- **Doors.** The literal/system classification used an in-session regex pass followed by reading the 86 residual
  contexts. The commands are in this session's transcript; the classifier is not saved to the repository.
- **"Hold", "crossed" and causal *since*.** I read every context.
- **Line references** (`ch:line`) are to `manuscript/chapter-NN.md`, where each paragraph is one line.
- **Kiva's development beats and the supporting-cast table** are judgments, not counts.
- **Cumulative viewpoint** adds sources with slightly different tokenizers: M1–M4 via the Movement Four review's
  table and the M4 repair's remapped deltas, and M5 here. Expect ±0.1 point.
- **The arithmetic in §3a** used only figures on the page, except places marked *, which come from the author's
  continuity §2 and are labelled as such.
- **Book One** was read only at ch. 1, ch. 23–24 and the prologue's catalogue card, by targeted grep.

**Scope boundaries.** Nothing in this report changes manuscript prose, the ledger, the continuity file or
`AUTHORSHIP.md`. No repair, commit, push, publish or later chapter.
