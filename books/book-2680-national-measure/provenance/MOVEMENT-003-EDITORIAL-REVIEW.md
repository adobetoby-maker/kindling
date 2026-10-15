# Kindling 2680, Book Two — Movement Three — editorial and numerical review

> Built by TAC

Date: 2026-10-15. Reviewer: **Claude Opus 5.5 (`claude-opus-5-5`)**, Claude Code background session
(job `b4e11087`).

## 0. What kind of review this is

- **This is a same-model, fresh-context, informed editorial pass.** It is not a cold read, not a
  human read and not independent testing. The movement's drafting author is recorded as Claude
  Opus 5.5 (`provenance/MOVEMENT-003-CHECKPOINT.md`, `AUTHORSHIP.md`). This session did not have
  the drafting transcript, but the prompt supplied the plan (`BOOK_MAP.md`), the bible, the
  cast file, the state ledger (including the author's own Movement Three block), the packet, the
  author's continuity checkpoint and the formula. So the review is **not blind**. The two reader
  lenses are simulated perspectives, not reader research. A same-family reviewer shares the
  drafter's blind spots.
- **Other review artefacts.** A file `provenance/MOVEMENT-003-COLD-READ.md` appeared in the
  working tree during this session, written by a parallel job. It was **not read** and nothing
  here depends on it.
- **Coverage.** All eight supplied files were read in chapter order, in full:
  `manuscript/chapter-17.md` to `chapter-24.md`. That is 54,482 words by `wc -w` and 54,351 body
  words by the script tokenizer (headings and `---` lines excluded). Every file is byte-identical
  to the frozen edition `editions/movement-003-first-draft/` (`shasum -c SHA256SUMS.txt`: all
  OK). During the session another process committed the chapters as `f529390` ("Complete
  National Measure movement three draft"); the working tree matches HEAD. The movement is
  complete as planned: chapters 17–24 of 48. No later chapter exists.
- **Canon evidence used.** Only `STATE_LEDGER.md` (sections 1–11 and the Movement One, Two and
  Three blocks), `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `packets/MOVEMENT-003.md`
  and `provenance/MOVEMENT-003-CONTINUITY.md`, plus three targeted greps of Movement Two chapters
  (ch. 13 for the Pit's race and the string, ch. 15–16 for Mara and the cart). The Book One
  manuscript was not read. Contradictions inside chapters 17–24 are **Verified**. Conflicts with
  Book One or earlier movements that cannot be checked from this evidence are **Apparent**.
  Departures from the plan or packet are **Plan**, not canon errors.
- **Formula source.** `/Users/drive/penname/research/ironprince-craft-formula.md` is present; its
  SHA-256 is `9f97e2f2…c0b8`, matching the recorded hash. Sections 2–6 and 8–9 were used as
  given, including the ~1.7× and ~950 values.
- **No manuscript prose was changed.** No repair, no later chapter, no commit, no push. The only
  files this session wrote are this report and `provenance/tools/m3_metrics.py`.

---

## 1. Unscored reader response

**Where interest caught.** On the first page, with Jude at the rail counting waves: "It's every
count at once." That one line sets the movement's whole subject, water that will not keep one
time, through the person who most wanted to see the sea. Interest stays high through the
arrival. The sea gate hangs ten feet above the water "as though there were nothing there at
all". The low town lies below the tide. The two fingers on a bollard say *It keeps time*. Then
the gate gives the movement its best small human moment: the Tarn reserve's grandfather's jar
singing thin. It ties to Mrs. Ottery without a speech ("It isn't anybody. That's the trouble.
It's just people."). The lay is a superb rival doctrine. It shows on the tape as one line, the
pen draws it, and Carrow is "smiling a little" because it is the easiest thing anyone has ever
seen. The movement's peaks:

- lane 1's three carries and the insight that a laid person must unlay to move (ch. 18 §2–6)
- Hart's barometer speech, "the book knows what weather is. The needle never does" (ch. 19 §4)
- the kiddle standing upright at slack, and *Far edge*, two words, once (ch. 20 §2–3)
- Rhea's dawn: the voice behind her a count late, and the remark "She wrote the card" (ch. 20 §7–8)
- the Hoop rising, with Hart's hand quiet on the grating (ch. 21 §4, §7)
- the Proprietor's hand on the glass, and his laugh at the refusal (ch. 22 §6, ch. 23 §8)

**Where it slipped.** Not in the fights. The slips come in three places:

- the rule-history paragraph in ch. 17 §6
- the long middle of ch. 22 (bench-book figures, then the offer, then the wire), where three
  procedural scenes run back to back
- the movement's two recorded arithmetic or logic misses: lane 2's tally does not add up
  (ch. 19), and Kiva "had no hands for a litter" just after Carrow carried one with nothing open
  (ch. 18)

Both misses land in a book that trains its reader to check. Lanes 2 and 3 are summarised
quickly. That is right for the plan, but the movement has fewer pages of fighting than
Movement Two.

**Who matters.** Kiva first, and more inward than before: she withholds three things on the page
(the question for Hart, "white" from Mara, "white" from the Proprietor). Then **Hart**, the
strongest new adult in the book: the watch turned an inch before he answers, the hand that
aches near anything keeping time, "badly on both sides". Then **Orla**, whose failure on the
landing is the movement's best cutaway. **Rhea** carries the cost scene. **Anwen** gets the most
generous minor scene (teaching Lyle, admitting Lyle's wall is better). Perrin is quieter than in
Movement Two, and that improves the supporting-cast balance.

**What I expect next.** Kiva not at the Bench, and Perrin's Carry. The Hunt on the Longshore,
where Lyle's lay and Wenna's "bad night" are now loaded. The seventh crossing (Thursday the 17th
at the soonest) competing with the Lane. The 23rd, when the sealed paper opens. The Proprietor
asking again in another form. Kiva's withheld "white" coming out somewhere.

**Would I continue?** Yes, under both lenses. The movement widens the world without losing Kiva.
Its new adults (Hart, the Proprietor, Peverell, Polglase, Carrow) are each a fair position, not a
villain, which is what the plan asked for.

---

## 2. Reader-lens scores

Anchors: 5 = understandable but inconsistent; 7 = engaging with located weaknesses; 9 =
compelling with few substantial distractions. These are editorial judgments, not calibrated
measurements. The lenses are separate and **not averaged** into a gate. No sales inference.

### 2a. Fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 7 | ch. 17 §0 (Jude: "every count at once"; Aske's "soonest") | Warm and specific before any explanation, but the pull is character, not danger. The first real stakes arrive at the gate (§4), 2,400 words in. | Medium |
| Keep reading | 8 | ch. 17 §6 → ch. 18 §6 (lay, loss, "make it walk"); ch. 23 §8 (the ask) | Every chapter closes on an open pressure (a protest, a notch, a summons, a wire, a fever). It dips in ch. 22 §3–5 (bench books, offer, wire) and ch. 23 §1 (the prediction text). | Medium-high |
| Interest / freshness | 9 | ch. 17 §6 (one line for two doors); ch. 20 §0 (the kiddle); ch. 21 §4 (the Hoop) | New rules, each shown before it is named. A child can state every one: they lay; it can't walk; you cut at slack; the water in the ring keeps the count. | High |
| Clarity / flow | 6 | ch. 18:247 vs 18:93 (who may carry); ch. 19:279 (6 vs 5); ch. 21 §2 (stack / whose); ch. 21:301 ("eleven minutes", unexplained) | Rules mostly arrive once and cleanly. A careful child will catch the carry contradiction and the score. "Laid" for the doctrine and walls "laid flat" on the water (ch. 20:399) collide aloud. | Medium |
| Character attachment | 8 | ch. 18 §12 (Anwen: "You're better than me"); ch. 24 §4 (Pru: "I'm not grateful… I'm going to go and be sick") | Several friends make choices that cost them. Pru and Anwen are distinct. Jude's sea line is a quiet thread a younger reader will hold. | High |
| Humor / warmth | 8 | ch. 17 §2 ("My dad's crane drops a stroke if you look at it"); ch. 17 §9 ("This is only true"); ch. 17 §0 ("she's had a knee for twenty years") | Grounded in character and well timed. Penhale's talk adds a new comic register. | Medium-high |
| Action / suspense | 8 | ch. 18 §2–6 (lane 1); ch. 20 §2–4 (the slack cut) | Trackable contest, adaptation on both sides, cost (downs, a dropped foot). Lane 1 earns its length. Lanes 2–3 are summaries, which a younger reader may want developed. | High |
| Progression payoff | 8 | ch. 22 §1 ("It was certified… glad of it in a way that she had never been glad of the three") | The certification lands with a visible price (the elbow, four nights). Losing to the lay teaches a tactic that pays in lane 2. | High |
| Connection | 9 | ch. 19 §4 (Hart's barometer) → ch. 20 §4 (the pole goes quiet) → ch. 21 §7 (the grating) → ch. 24 §10 (*yes or no*) | A plant, a test, a proof and a habit in four chapters. Thrale's room (M2) is contrasted in ch. 23 §4. | High |
| Read-aloud quality | 7 | max sentence 52 words (no 60–90-word chains); ch. 22:35 ("brass ones that he must have brought in the black book's spine"); 28 × "I'd want…" across thirteen speakers | Much better breath control than Movement Two. Voices blur where everyone says "I'd want it said / I'd want you to know". "Said nothing" (22) and "she/he did not" (27 per 10k) give a negative, flattening cadence. | Medium |

### 2b. Adult genre reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 7 | ch. 17 §0–1 | The arrival is atmospheric and exact (the Mole, the hung gate, the low town). An adult forgives the slow first page for the place. | Medium |
| Keep reading | 8 | strongest ch. 19–20 and ch. 23 | Propulsive. The procedural middle of ch. 22 is the one sag. | Medium-high |
| Interest / freshness | 9 | ch. 22 §3 (the Step quickening, 48 → 57); ch. 21 §5 (the 2604 Saltmere entry) | Strong evidence-ladder work. Each discovery is said by someone who can be wrong ("I'd like it noted that he's never looked"). | High |
| Clarity / flow | 7 | as 2a; plus ch. 21 §4 / §7 (spring slack at 6.12 and 6.13 on consecutive days) | Clear to a systems reader. A reader who knows tides will notice the slack moving one minute in a day (see §3, C12). | Medium |
| Character attachment | 9 | ch. 19 §11 (Orla on the landing); ch. 20 §8 (Rhea's remark); ch. 23 §7 (the Proprietor at his window) | The adults carry real, specific cost, and none is a villain. The Orla scene is the best cutaway in the book so far. | High |
| Humor / warmth | 8 | ch. 23 §2 ("I'll sit there like a post. I've had practice."); ch. 22 §3 ("It's a great trial.") | Dry and earned. | Medium-high |
| Action / suspense | 8 | ch. 18 §2–6; ch. 20 §7 (the count late) | The best suspense beat is not a fight: a voice a count late. Combat vocabulary is the lowest of the book so far (12.3 per 10k), which an adult genre reader may feel across the movement. | Medium-high |
| Progression payoff | 8 | ch. 18 §9 → ch. 22 §0 → ch. 24 §11 (cold to a hand below the elbow, then the elbow, three nights, then four) | The rising price of an ordinary capability is still the book's best progression device. | High |
| Connection | 9 | the 2604 night: Ferren keeper (Book One) → Saltmere keeper (ch. 21 §5) → the Proprietor (ch. 23 §7) | Book-scale plants are carried and deepened without being spent. | High |
| Read-aloud quality | 7 | as 2a | The register suits adults. The shared "I'd want…" idiom flattens voices the cast file distinguishes. | Medium |

---

## 3. Canon, physical state, power limits, knowledge and reserved disclosures

| # | Label | Location | Issue | Evidence |
|---|---|---|---|---|
| C1 | **Verified (arithmetic)** | ch. 19:259–279 (lane 2) | The carries do not add to the marshal's total. Carry 1: Seven over, 3, no down. Carry 2: Perrin downed and Ropewalk over, Ropewalk 4 ("Four to three"). Carry 3: "A point to Seven, and a down", +2, so **Seven 5**. The marshal says "Six to Seven". The seeding board ("twelve for, sixteen against", ch. 24 §5) uses 6–4, so the board is consistent with the wrong total. | ch. 19:259, 269, 277–279; ch. 24 §5; ledger M3.2. |
| C2 | **Verified (logic)** | ch. 18:247 and 18:269 vs 18:93 | The catcher and the litter contradict each other. In carry 1 Carrow carries the litter over the hazel "still with nothing open", which is legal. In carry 3 nobody can take the poles because "Kiva had her still door declared and no hands for a litter. That was the rule, and Seven had chosen it." Carrow then says "You can't, can you? You've a door declared and that's all you're let open." Carrying needs no door, so the reader cannot tell whether this is a Board rule, a Chair condition, or Seven's own doctrine. | Marshal's rules as stated (ch. 18 §1) do not bar a declared catcher from the poles. |
| C3 | **Verified (calendar and event)** | ch. 18:467 and 18:515 | Lyle tells Anwen "You leaned well. **This morning**" and "I saw you do it **this morning**, at the end. You walked it from the far end." The cutaway is at six on **Thursday** evening (18:449); the lane was **Wednesday** at nine. And Anwen never walks a wall in lane 1 on the page: she leans (§2), then goes with the litter (§6). The walk is shown first in lane 2, on Saturday (ch. 19:277). | ch. 18 §1–6; ch. 19 §7; continuity §1. |
| C4 | **Verified (count)** | ch. 23:3 | On Friday morning Aske says "That's two nights to go." The sixth was Thursday morning, and warmth came on Monday at seven: a sulk of four nights (Thu, Fri, Sat, Sun). On Friday morning **three** remain. Sunday's "One night to go" (ch. 24 §6) is correct. | ch. 22 §0; ch. 24 §6, §11. |
| C5 | **Verified (internal)** | ch. 20:355 vs 20:335 and ch. 20 §8 | Rhea: "On every floor for six years she had had a catcher who watched her heel **and a second who watched the far edge**." In the same section Pike says "I did both for twenty years before there was ever a second in this van", and Rhea thinks "You don't know you've stopped till she's gone." Kiva has been the second since the first month of this year; the standing slate line dates from the 23rd of the first month. | ledger M1.3; ch. 20 §7–8. |
| C6 | **Verified (count)** | ch. 20:393 (*Tinned: six bags… The sixth bag light.*) | Seven purses were drawn shut: posts 1–3 at the high-water slack (ch. 20 §2–3: "Three purses shut") and four at dawn (5, 6, 7, then the fourth, "light"). That makes **seven bags, the seventh (the fourth post's) light**. The continuity file §4 and the ledger M3 block repeat "six". | ch. 20 §2–4, §7. |
| C7 | **Verified (place)** | ch. 24:197 | Trewin: "I watched your captain plant **on the Ropewalk's boards** on Tuesday… to be read." The reading was on the gate's boards in the timber pond, "with the whole of the Ropewalk watching" (ch. 21 §2). | ch. 21 §2. |
| C8 | **Verified (interval)** | ch. 24:39 | Trewin at the gate "a fortnight ago": the gate was Tuesday the 1st, lane 3 is Saturday the 12th, which is eleven days. A small slip, but it is the kind of count the book trains its reader to check. | ch. 17 §5. |
| C9 | **Verified (logistics, low)** | ch. 19:97 | Mara: "Then you had a fever on the ferry and I was on a transit two days behind you." At the fever (Friday the 27th) Mara was still in Meridian; she arrived on Wednesday the 2nd, two days after Seven. Ch. 16:133 has her meaning to tell Kiva "on the cart… on Wednesday morning", which fits "on the cart". "At the house of the Even Hand" can only mean by letter, since she was not there. | ch. 16:133; ledger M2.4. |
| C10 | **Verified (logistics, low)** | ch. 17:167 | Talley's note on a parcel to Kellan's mother ("broke Saturday"), forwarded by her, reaches Kellan in Saltmere by Monday evening. That means barge to Meridian to Saltmere in about two days, faster than the transit. "My mother **wired** it on" would fix it. (Orla's daily letters, 17:317, are plausible if posted ahead.) | ch. 17 §3. |
| C11 | Verified (minor) | ch. 21:165 | Carrow on Tuesday the 8th: "Maud told me last night." Lyle heard it on Thursday the 3rd. It is possible she waited four days; "Maud told me" without "last night" removes the question. | ch. 18 §12. |
| C12 | **Apparent (physical world; owner)** | ch. 21:181–185 (Tue 8th, quiet 6.12) and 21:327 (Wed 9th, quiet 6.13) | On an Earth-like semi-diurnal tide, slack comes about 50 minutes later each day. Here the spring low-water slack moves one minute in a day. The fortnight-later prediction (6.09 on the 23rd) is plausible, because springs recur near the same clock time. The day-to-day figure is the problem. The world may have its own tide, but nothing on the page says so, and the coast night (11.54 high, about 6.15 low) behaves like Earth's. | ch. 20 §2, §7; prediction ch. 23 §0. |
| C13 | Apparent (owner) | ch. 19:217–219 | The cells "held while it was quiet". The longest held 41 minutes from a slack beginning at 3.38, but Hart gives the quiet as about twenty minutes at the springs, "longer at the neaps". If the 21st of the eleventh month was a neap, this is consistent. The page does not say so. | ledger M1.5. |
| C14 | Apparent | ch. 19 §6 ("a line in brown ink… *Somebody at Saltmere had a temperature as well*") | `BOOK_MAP` §12 gives this as Lumb's remark (Book One). The prose makes it a line in brown ink in a keeper's book. It may be Lumb's own written gloss; check Book One. | `BOOK_MAP` §12. |
| C15 | **Plan** | ch. 24 §1–3 | The packet says "the Graving [is] not played this movement". Lane 3 is a seeding lane on the Graving's floor. It is not a national board, but it spends the first view of the national floor. The continuity file §14 does not list it as a departure. | packet "What must remain true". |
| C16 | **Plan** | ch. 20 §8 | The packet says "Do not repeat the van-slate template a third time". Rhea's slate is written out again (*Closed… Lives… Works… Tinned… Remarks*). It is used for character (the officer's remark against herself) and works, but it is the template. It is not listed in continuity §14. | packet, craft lessons. |
| C17 | **Plan (owner)** | ch. 20 | Rhea goes short in Movement Three. `BOOK_MAP` §12 maps that payoff to Movement Four. The Movement Three packet authorised it, so this is a map/packet difference, not a prose error. The map should be updated. | `BOOK_MAP` §12; packet. |
| C18 | Plan (viewpoint) | whole movement | Kiva 82.4% by segment against the packet's 82–85%. Cutaway words 9,545 against a ceiling of 9,500 (+45; the author's `wc -w` count was +52). Mara's 4.5% for the movement is above the per-lens band, but the cumulative shares are inside it (§4f). | packet. |
| C19 | Knowledge (owner) | ch. 23 §10 | "Nothing," said Kiva… "Nothing came." Said aloud to Aske and Pru. It discloses no content, but it tells two people that she expected something to come with a fever. The ledger M3.7 says "Known to nobody new", which is true of the content. The page should record that Aske's card line ("Both near a Glory master") and Pru's "I want to, though" now mean both suspect. This is a decision made on the page, so it is legitimate. | ledger §7; M3.7. |
| C20 | Knowledge (owner) | ch. 18:531 | "She had not told Lyle that a lodger could be killed, or how." This asserts that Seven knows how to kill a lodger. The supplied record shows the lodger demonstrated (M2) and avoided, not killed. If Movement Two never established a kill method, this line creates one by implication. | ledger M2.5 ("The lodger and the laid door"). |
| C21 | Owner (wording) | ch. 23 §7 ("now your aunt is going to stop my best machine in this town") | The harbour bank is the pump house's, not Halden's. The Proprietor may mean it by the foundation's claim on "all ash exhibiting the Step", which suits him. Keep it if that is intended; a clause would make it unmistakable. | bible §1 (the patent claim). |

**Checks that passed.**

- **Arithmetic (book).** 6.23 − 0.43 − 0.31 − 0.40 − 0.09 − 0.30 = 4.70 (on the page, ch. 23
  §8); − 0.42 = 4.28 (ch. 24 §6); − 0.12 = 4.16 (Jude's entry). The per-line split of lanes and
  the gate reading is the author's reconciliation (only the totals are on the page), as the
  continuity file says. The sealed 2.0 is declared, combed (W full, I silent) and refused for
  sale.
- **Lanes 1 and 3** add up: 2–7 and 4–5. Only lane 2 fails (C1).
- **Weekdays and countdown.** Every weekday from Sunday the 29th of the second month to Monday
  the 14th agrees with `STATE_LEDGER` §1. Perrin's count (14 minus the date) is right on the
  30th (Fourteen), the 1st (Thirteen) and the 14th (Nought). Seventy-seven years (2604 → 2681),
  twenty-one years (2660 → 2681), Hart at forty, and the Proprietor at 26 in 2604 and 103 now
  all check.
- **The hand.** Fifth: Thursday 3rd, 0.31, a hand below the elbow, warm Sunday 6th at seven,
  three nights. Sixth: Thursday 10th, 0.30, the elbow with an ache in the joint, warm Monday 14th
  at seven, four nights. Seven days apart, with the price said first each time. Seventh soonest
  Thursday the 17th. Only C4 misstates the count on the way.
- **Power limits.** One declared door at every board (stance), by the captain's voice. No stack,
  no three-door, no Ember-to-still crossing. Kiva lights nothing on the coast night and speaks
  once before the purses are declared shut (*Far edge*, the slate's standing exception). The
  handed crossing is a yard rehearsal only, with one declared Ember. Students close no tear
  (Bray's crew does). The Glory limit is visible: the Proprietor cannot lift his hand from the
  glass (bible §9). No Glory master does a student's work. No fingers heal.
- **Knowledge.** The dream's content stays with Kiva and Mara. The ferry detail "some had gone
  white" stays with Kiva alone: she withholds it from Mara over the 2604 page (ch. 21 §8) and
  from the Proprietor over his lamps (ch. 23 §7). Kiva learns that Orla is coming from Aske on
  the page (ch. 17 §0) and finds Mara herself (ch. 19 §2). The Proprietor's 2604 account has a
  fever and lamps but **no dream**, so his Movement Five testimony is unspent. Hart's own
  dreaming is unasked.
- **Reserved.** "Unroofed" 0, "Breach" 0. The disk is cold at every look, including on the
  Proprietor's table. No point of light, no hull, no Saltmere Company death. Penhale is
  introduced as an ordinary colleague, without telegraphing.
- **No real month names.** 0 by script.
- **The ch. 13 thread is retired on the page.** It was read on a sanctioned mast with two
  readers, read as one line, "not a stack under any rule", and entered "in no circuit's column".
  This is well handled.

---

## 4. Numerical formula alignment

Method: `python3 -I provenance/tools/m3_metrics.py manuscript`, run from the book directory. The
script is a copy of `m2_metrics.py` with only the chapter range, the output labels and the
viewpoint map changed (diff in §7). The tokenizer, sentence splitter, syllable estimator and
every lexicon are identical, so the figures are comparable with Movement Two. "M2 repaired"
figures come from `MOVEMENT-002-RECHECK.md`. Anything marked *manual* is the reviewer's judgment.

### 4a. Sentence rhythm — **changed shape again: the long tail is gone, the median has barely moved**

| Metric | Target | **M3 all text** | M3 narration only* | M3 dialogue only | M2 repaired, all text | M2 repaired, narration |
|---|---:|---:|---:|---:|---:|---:|
| Mean words | 14.6 | **9.5** | 10.7 | 6.1 | 10.7 | — |
| Median | 11 | **7** | 7 | 4 | 6 | 7 |
| Population SD | ~26 | **7.9** | 8.9 | 5.3 | 11.2 | — |
| ≤5 words | 27.7% | **40.3%** | 37.3% | 60.1% | 44.6% | 41.4% |
| ≥40 words | 3.3% | **0.4%** | 0.6% | 0.0% | 3.6% | 6.2% |
| Longest sentence | — | **52** | — | — | 96 (pre-repair) | — |

\*Narration has quoted spans removed; leftover tags ("said Kiva.") count as short sentences.
5,700 sentences; dialogue is 29.0% of words. Mid-band (6–39 words): **59.3%** of all sentences
(M2: 49%; the source shape implies about 69%). The 8–25 band holds 38.4% overall and 40.9% of
narration. Per chapter, the short share runs from 36.4% (ch. 20) to 45.0% (ch. 24), and no
chapter exceeds 0.8% at ≥40.

**Read.** The packet's craft lesson ("write the middle; do not chain into 60-word breaths")
worked on two of three fronts:

- the short share fell 4 points
- the middle band grew by 10 points
- the 60–96-word chains are gone, and the read-aloud improvement is real

But it **over-corrected the tail**. Only 21 sentences reach 40 words, the ≥40 share is an eighth
of target, and the SD has collapsed from 11.2 to 7.9 against a target near 26. The median moved
by one word. The prose is no longer bimodal. It is now **compressed**: a mass of short and
low-middle sentences with almost no long, hierarchical sentence to contrast against. The
formula's own read warns that a manuscript without contrast "will not read the same". The
narration median of 7 is where Movement Two's was; the gain in the middle came from fewer very
short sentences and fewer very long ones, not from a longer typical sentence.

**Formula conflict, still open (owner).** Dialogue alone is 60% short. Unless the sentence
targets govern dialogue, the whole text cannot reach 27.7% short. And an SD near 26 requires a
real long tail, which the packet just told the author to remove for read-aloud reasons. These
are not reconcilable without an owner ruling on (a) dialogue, and (b) how long a "long"
sentence may be for a thirteen-year-old read aloud.

### 4b. Paragraphs and scenes — **paragraphs close; scenes much too short and too frequent**

| Metric | Target (ASR proxy) | Observed (typographic) | M2 (pre-repair) |
|---|---:|---:|---:|
| Paragraph median / mean | 18 / 26.8 | **21 / 32.2** (1,689 paragraphs; 19.4% over 60 words) | 18 / 30.8 (18.3%) |
| Section length | ~950 | **625 mean, 606 median** (87 sections; 16 under 400 words; 11 at 900 or more) | 889 |
| Breaks per 10k | ~8.7 | **16.0** counting chapter openings; **14.5** internal `---` only | 11.3 / 9.9 |

Typographic breaks are not ASR pause segments, so this comparison is directional. Even so, the
gap is large, and much of it is mechanical: several **continuous scenes are cut by `---`**,
where the beat does not change place, time or lens:

- lane 1 runs across six sections (ch. 18 §1–7)
- the high-water slack runs across three (ch. 20 §2–4)
- the Counting House evening runs across six (ch. 23 §3–8)
- the Proprietor's dinner runs across two (ch. 22 §6–7)
- the gate reading runs across three (ch. 21 §0–2)
- lane 3 runs across three (ch. 24 §1–3)

Read aloud, each `---` is a narrator's long pause, so a single fight or dinner is heard as
several scenes. The shortest sections (ch. 22 §2 at 125 words; ch. 19 §9 at 146; ch. 22 §8 at
224) are bridges that could sit inside a neighbour.

### 4c. Readability — **large drift, unchanged in direction**

| Metric | Target | M3 | M2 repaired |
|---|---:|---:|---:|
| Flesch Reading Ease | 72.3 | **96.1** | 97.0 |
| Flesch-Kincaid grade | 6.8 | **2.2** | 2.4 |
| Syllables per word (estimator) | — | 1.195 | 1.169 |

The tokenizer is regex words; the splitter is guarded for Mr./Mrs./initials; syllables come
from a vowel-group heuristic with silent-e trimming. Proper names and system terms (Saltmere,
Polglase, Peverell, Proprietor) raise the syllable rate slightly; diction is a little richer than
in Movement Two. The grade fell because sentences got shorter on average. As before, Flesch
under-reads the real difficulty, which lies in procedure (notches, cliffs, slacks, tables)
rather than in word length.

### 4d. Progression vocabulary — **mid-book density is higher than the front-load arithmetic allows**

The lexicon is unchanged from Movements One and Two (§7).

- Raw: **304 hits = 55.9 per 10k.** Doors 150, Ember 21, crossing(s) 31, Hold 19, stack 16,
  certif- 16, cliff 12, licence 7.
- **Literal and non-system hits, by reading all 150 door contexts manually:** 55–58 doors are
  literal, a measure, or the metaphor "a shut door" (warehouse doors, "at the door", "the width
  of a door", "your sponsor… there was a door"). Four "Hold" hits are the verb ("Hold it"). The
  automated literal-door phrase grep finds only 25, because it misses most of these patterns.
  - Manual adjustment: **242–245 = 44.5–45.1 per 10k.**
  - Automated adjustment: 275 = 50.6 per 10k.
  - Report the movement at about **45–51 per 10k**, with the manual figure preferred.
- Within the movement, by equal-word thirds: **122 / 64 / 118**. The dip falls in the harbour
  and coast chapters (ch. 19 late to ch. 21), where the progression system recedes behind the
  water. That suits the formula's "surface only at genuine turning points".
- Ash-economy terms: 8.1 per 10k (Movement Two: 14.1). The packet's "each figure arrives once"
  shows up in this number.
- **Cumulative and provisional.** By the plan, Movements One and Two are the book's opening
  third, at about 51–55 adjusted hits per 10k (Movement Two review). Movement Three is half of
  the middle third, at about 45 adjusted. The provisional ratio of opening third to Movement
  Three is about **1.13–1.24**, against the source's ~1.7×. The full ratio cannot be confirmed
  until Movement Four exists.
- **The Movement Two review's conflict stands, slightly worse.** A 1.7× front-load from this
  opening third needs later thirds near 31 per 10k. Movement Three runs about 45. The book can
  meet the whole-book average of 58 or the front-load shape, not both. **Owner decision.**

### 4e. Development beats

**Kiva (manual): about 37 choices or realizations, 6.8 per 10k** (target 4.5, so above). They
are spread across all eight chapters: ch. 17 ×5, ch. 18 ×5, ch. 19 ×4, ch. 20 ×4, ch. 21 ×3,
ch. 22 ×3, ch. 23 ×6, ch. 24 ×5. Representative:

- "Mine. If the captain will let me." The tin is hers to declare (ch. 17 §4).
- "It's their count. They've a right to it." (ch. 17 §2)
- "I don't know… It didn't look like an accident." (ch. 17 §7)
- "Yes. It is." Fairer, and hers (ch. 17 §8).
- "There's no gap… Carrow had to run." (ch. 18 §3)
- Watch the catcher, not the captain (ch. 18 §4–5).
- "This felt like being shown something… not a miss." (ch. 18 §8)
- She goes alone to answer Hart aloud (ch. 19 §1).
- "It's yours." Mara's risk, not hers to own (ch. 19 §3).
- The fingers as a gauge (ch. 19 §4).
- She does not ask the question (ch. 19 §6).
- Sleeve, not speech; *Far edge* (ch. 20 §1–3).
- "It went quiet… it came back before the water moved." (ch. 20 §4)
- She goes when called and does not look back (ch. 20 §5–6).
- "It's gone out of the harbour, into that." (ch. 21 §7)
- She withholds "white" from Mara (ch. 21 §8).
- Glad of the certified crossing as never of the three (ch. 22 §1).
- She sits halfway down the table, not at the far end (ch. 23 §4).
- She shows the plate properly or not at all (ch. 23 §6).
- She withholds "white" again (ch. 23 §7).
- The refusal, with reasons (ch. 23 §8).
- "Nothing came." (ch. 23 §10)
- "No. It's yours." (to Perrin, ch. 24 §0)
- "You watch hands because you are one." (ch. 24 §4)
- She learns she calls from the air (ch. 24 §8).
- *yes or no*, never *what* (ch. 24 §10).

The regex proxy (63 hits, 11.6 per 10k) is inflated by "found that" and "knew that". It is
reported only for reproducibility.

**Supporting cast (manual): at least eighteen named people get one or more beats, with no
deuteragonist.**

| Person | Beats |
|---|---|
| Perrin | "I'd be proud of it"; the defeat written "fairly"; "make it walk" credited to Kiva; asks to be read; wants a second plant; silent "like a post"; "Nought" |
| Anwen | goes alone to the Ropewalk; warns Lyle; "You're better than me"; teaches the far-end walk; won't tell Perrin |
| Jude | the sea; "what's it for?" answered by Yeo; "twenty minutes when you can see"; "I'd do it" |
| Pru | hauls; stays with Rhea; catches lane 3; "not grateful"; hands |
| Kellan | gives only the record; "she'd say it to your face"; tells Kiva; admits wanting to give |
| Noa | enters the lay as an incident; answers Perrin; won't draw a fourth column |
| Orla | does not ask; fails on the landing; tells Kiva herself; signs |
| Mara | comes without telling; "the most grown-up thing"; seals a page that can be found wrong |
| Rhea | goes short; the spring's advice; a hand on Kiva's shoulder; does not cross out |
| Pike | takes both places; "Late"; "you call from the air" |
| Aske | the price before; "soonest"; "I'd like to be wrong" |
| Hart | "There."; "badly on both sides" |
| Dray | "That's fairer"; walks |
| Carrow | adapts; "I'll think about it. I'll not stop." |
| Lyle | tries one door: "It's so loud" |
| Polglase | "I've looked now" |
| Adlam | takes no for an answer |
| The Proprietor | laughs; "I'd rather be wrong than have the low town flood" |

Perrin no longer dominates the secondary development as he did in Movement Two. The shape now
matches the formula's §5 "many small beats".

### 4f. POV word share (viewpoint segments, not name frequency)

Segmentation (manual, 0-based sections after splitting on `---`):

- Anwen: ch. 18 §12
- Orla: ch. 19 §10–11
- Rhea: ch. 20 §7–8
- Mara: ch. 21 §4–6
- Kellan: ch. 22 §6–8
- Everything else is Kiva.

Ch. 22 §9 is assigned to Kiva, as the author also counted it. It opens "Kiva was sitting on her
bed" and stays observable from her bed, though it watches Kellan closely; read as Kellan's lens,
Kiva would be 81.3%.

| Lens | M3 words | M3 share | Cumulative M1+M2r+M3 | Cumulative share | Target |
|---|---:|---:|---:|---:|---|
| Kiva | 44,806 | **82.4%** | 141,335 | **87.4%** | ~87% (85–90) |
| Anwen | 1,398 | 2.6% | 2,702 | 1.7% | 2.5–3.7% |
| Kellan | 1,828 | 3.4% | 4,284 | 2.6% | 2.5–3.7% |
| Orla | 1,871 | 3.4% | 3,950 | 2.4% | 2.5–3.7% |
| Mara | 2,426 | 4.5% | 4,662 | 2.9% | 2.5–3.7% |
| Rhea | 2,022 | 3.7% | 4,808 | 3.0% | 2.5–3.7% |

Cumulative total: 161,741 body words. Movement One figures are derived from the Movement Two
review's cumulative table; Movement Two uses the post-repair recheck figures. **The book is now
on its viewpoint target.** Anwen is the one lens under the band; she is the natural candidate if
Movement Four needs a cutaway where Kiva cannot see (for example the Longshore). Each cutaway is
anchored by name and a private cue in its first sentence, as the packet asked. The formula wants
"brief cutaways, not chapters". Mara's three sections (2,426 words) and Kellan's dinner (1,828)
are at the long edge of brief.

### 4g. Secondary signals (optional per formula §8)

| Signal | Source band | M3 | M2 (pre-repair) | Note |
|---|---:|---:|---:|---|
| "that" | 92.1 (tighten below) | **119.6** | 143.9 | improving |
| just / almost / felt / seemed | 5–25 | 1.3 / 0.6 / 4.8 / 1.3 | 0.8 / 0.2 / 5.2 / 0.2 | — |
| -ly words | ~161 | 33.7 raw; **26.5** filtered | 20.5 | "slowly" ×25 (4.6/10k, down from 6.5) |
| Quote-adjacent tags | ~41 | **56.9** (309) | 66.7 | — |
| Combat terms | ~22 | **12.3** | 29.9 | below band; mostly *cut* 26, *blade* 24 |
| "out of the" / "one of the" / "for a moment" | 2–4 | 7.2 / 0.2 / **5.0** | 2.2 / 0.0 / 2.7 | "for a moment" ×27 |
| House trigrams | — | "she did not" **16.2**, "he did not" 10.7, "there was a" 8.6, "looked at her" 7.4 | "she did not" 8.9 | negation density nearly doubled |
| Causal *since* | packet: use *because* | 5 (17:331, 17:427, 18:289, 20:85, 21:287) | 18.8/10k all uses | 4 in dialogue, 1 in narration |

**Tics and voices (raw counts in 54.4k words).**

- **"I'd like it known" 7, all Perrin.** The packet's rationing worked.
- **"tied a knot" 0, "pale eyes" 0, "something moved at the corner" 0.**
- **"I'd want…" 28, spoken by thirteen people:** Jude (×11), Orla (×3), Hart (×2), Kellan (×2),
  and once each Perrin, Kiva, Aske, Anwen, Pike, Yeo, Peverell, Mara and Pru. The shapes are
  "I'd want it said", "I'd want you to know" and "I'd want that written".
  This has become the cast's shared idiom. It blurs the voices that `CHARACTERS.md` keeps apart,
  and it shadows Anwen's own "I want it said".
- **"said nothing" 22** (Movement Two: 9). "I'd sooner" 8. "for some time" 6. "scratched his
  jaw" 4 (Jude only, which is acceptable).

---

## 5. Movement Two repair state in `STATE_LEDGER` against chapters 17–24

| Ledger item (M2 block, as repaired) | In chapters 17–24 | Result |
|---|---|---|
| Four hand-to-Ember crossings; fifth and sixth entered for the gate mast, "one in seven days… not certified until the sixth" | Fifth Thu 3rd, sixth Thu 10th, certified by Orla in the Chair's ledger (ch. 22 §1) | PASS |
| The fourth: mid-forearm, warm Wednesday the 25th, "two nights" | ch. 17 §0 ("Warm. As it was on Wednesday"); ch. 18 §9 ("sulked for two nights") | PASS |
| Aske travels south | ch. 17 | PASS |
| Disk cold, including beside Thrale | cold at every look, including near the Proprietor | PASS |
| Dream on the ferry, 112 by Pru, broke about four; "not so high"; lights "some white"; not in her book | Orla reads the fever line and no dream (ch. 19 §10); "lower… some had gone white" (ch. 21 §8) | PASS |
| Doors "lay down" near Thrale | contrasted: near the Proprietor they want to march (ch. 23 §4) | PASS |
| Flask license; handed crossing rehearsed, not live; *mine before yours* reads as one line | yard rehearsal only (ch. 24 §8); one line confirmed at the gate (ch. 21 §2) | PASS |
| Book 6.23; sealed 2.0, bound *For a hand…* | carried, declared, combed W full / I silent, offer refused on the binding | PASS |
| Repair correction: the comb (dilution on the third reed, seventh silent on old stock) | the Tarn jar: third thin, seventh silent, "The seventh's right. But it's been stretched" (ch. 17 §5) | PASS |
| Repair correction: the mill cloths | Coombe's rope (Perrin) carried; the sheets are not mentioned | n/a |
| Jude: left shin burned, left arm frosted (sling) | sling on the boat, off for lanes only on Aske's word, limping | PASS |
| Two night-van nights left in the third month; Varley at the cloth; Pike a voice; Kiva second | "two nights left" (ch. 19 §0); the Company lends Penhale in Varley's place on its own ground; one night left after the coast night | PASS |
| Pike's hands "by the fourth of next month, slow" | dressings off Friday the 4th, close halfway | PASS |
| Mara going south in the first week by the Works' transit with Rusk; Kiva not told | arrives Wednesday the 2nd with Rusk; Kiva finds her by chance (ch. 19 §2) | PASS (see C9 for one wording slip) |
| Orla going south to find Hart, "not use her to say it"; Kiva not told | Aske tells Kiva on the boat; Orla on her crate; "I'll not use her to say it" (ch. 19 §11) | PASS |
| Thrale: one door; past her gate twice; won't ask Kiva the four questions | not contradicted | PASS |
| Coombe "will be on the Longshore" | not seen; her lodger teaching travels through Anwen and Lyle | PASS |
| Mrs. Ottery (soot-cut 2669 stock) | "a woman in black with red hands", a week before the gate (correct interval) | PASS |

**The author's Movement Three ledger block and continuity file against the prose.** They agree
except for C4 (no entry), C6 ("six bags… the sixth light" is repeated in continuity §4 and
should become seven) and the unlisted plan departures C15–C17. Continuity §14.3's "79 sections"
counts internal breaks; the script's 87 includes chapter openings. Both describe the same file.

---

## 6. Repair brief — three priorities, bounded

**P1 — Continuity, arithmetic and logic line fixes (C1–C8, plus C9–C11 if convenient).**
- *Location:*
  - lane 2 tally, ch. 19:259–279
  - the catcher and the litter, ch. 18:247 and 18:269
  - Lyle's "this morning" ×2 and the wall walk, ch. 18:467 and 18:515
  - "two nights to go", ch. 23:3
  - Rhea's "six years… a second", ch. 20:355
  - "six bags… the sixth light", ch. 20:393 (and continuity §4, ledger M3)
  - "on the Ropewalk's boards", ch. 24:197
  - "a fortnight ago", ch. 24:39
  - Mara's "two days behind you", ch. 19:97; "my mother sent it on", ch. 17:167; "last night",
    ch. 21:165
- *Observed issue:* one score that does not add, one rule the page contradicts, one wrong day
  plus an event not on the page, one wrong count of nights, one internal contradiction about
  seconds, one wrong bag count, one wrong place, one wrong interval, and three logistics slips.
- *Effect on the reader:* this book trains its reader to check sums and days ("That adds" is a
  promise). C1 and C2 sit inside the movement's two lanes, where a thirteen-year-old is watching
  hardest. C5 undercuts Rhea's best scene, whose point is precisely that the second is new.
- *Proposed scope:* about ten line edits, no scene changes. Suggested fixes:
  - **C1:** add a down in carry 1 ("and a down — Jude on their blade at the hazel"), or make
    carry 3 "a point, and two downs". Do not change the board.
  - **C2:** state the reason once, in Seven's or the Chair's terms. For example: the catcher's
    hands stay off the poles while her declared door is open on the hurdle, and shutting it
    would leave the hurdle unplanted. Or change Carrow's line to the real gap ("Your catcher
    stays planted. Ours doesn't have to.").
  - **C3:** "yesterday", twice. Point the far-end walk at something Lyle saw on the page, or
    move her request after lane 2.
  - **C4:** "three nights to go".
  - **C5:** "a catcher who watched her heel, and since the first month a second who watched
    the far edge".
  - **C6:** "seven bags… the seventh light" (and the records).
  - **C7:** "on the gate's boards".
  - **C8:** "eleven days ago", or "at the gate".
  - **C9:** "and I was still at the kitchen table, two days from leaving".
  - **C10:** "wired it on".
  - **C11:** drop "last night".
- *Strength to preserve:* lane 1's three carries and "There's no gap… Carrow had to run"; the
  marshal's flat calls; Rhea's remark "That remark is the officer's. She wrote the card." and
  Pike's "It was mine. The count late."

**P2 — Rhythm and scene structure toward the formula (§4a–4b), narration only.**
- *Location:*
  - Scene breaks inside continuous action: ch. 18 §1–7, ch. 20 §2–4, ch. 21 §0–2, ch. 22 §6–7,
    ch. 23 §3–8, ch. 24 §1–3 and §7–8.
  - Long-sentence candidates where the hierarchy is easy aloud: the descriptive set pieces (the
    Saltmere arrival, ch. 17 §1; the Graving, ch. 17 §4; the pump-house hall, ch. 19 §2; the
    kiddle, ch. 20 §0; the Hoop rising, ch. 21 §4; the Counting House stair, ch. 23 §3).
  - Joining candidates: runs of three or more short narration declaratives in reflective passages
    (Kiva's thinking in ch. 22 §1, ch. 23 §7, ch. 24 §10).
- *Observed issue:*
  - median 7 against 11
  - short share 40.3% against 27.7%
  - ≥40 share 0.4% against 3.3%, with the SD collapsed to 7.9
  - sections average 625 words against ~950, with 14.5 internal breaks per 10k against ~8.7
- *Effect on the reader:* read aloud, the quiet stretches now run at an even trot with few
  breathing contrasts, and one fight or one dinner is heard as several scenes because each `---`
  is a pause.
- *Proposed scope:* a focused same-author pass on narration.
  - **Remove 15–20 intra-scene `---` breaks.** Use a one-clause transition where needed; no
    prose is cut. This alone moves breaks toward about 11 per 10k and the section mean toward
    about 800–850.
  - **Write one or two hierarchical long sentences (40–55 words) per chapter**, only in
    descriptive set pieces, with one main clause and clear subordination. No *and…and* chains.
  - **Join adjacent short narration declaratives** where the thought is continuous.
  - Interim waypoint, measured with the same script: narration median 8–9, narration short
    share about 33%, ≥40 share about 1.5–2.5%. This is an editorial waypoint, not a revised
    target.
  - Leave dialogue alone until the owner rules (§4a).
- *Strength to preserve:* the clean breath control the movement has won (no 60-word chains); the
  short beats that end scenes ("It sang." / "Nothing." / "There."); the fight rhythm of lane 1
  and the slack cut. **Do not shorten either developed contest.**

**P3 — Voices and read-aloud clarity.**
- *Location:*
  - the 28 "I'd want…" lines (grep list in §7)
  - "said nothing" (22)
  - the "she/he did not" negation runs, densest in the Kiva reflective passages of ch. 21–23
  - 5 causal *since* (17:331, 17:427, 18:289, 20:85, 21:287)
  - ch. 22:35 ("brass ones that he must have brought in the black book's spine")
  - ch. 21:301 ("eleven minutes that the low town would bear", a new figure with no setup)
  - "walls laid flat on the water" (ch. 20:399) beside the doctrine word "laid"
- *Observed issue:* a shared idiom has replaced the individual tells that `CHARACTERS.md`
  assigns. Negation density has doubled. A few phrases trip a one-pass reader.
- *Effect on the reader:* the thirteen-year-old lens loses who is speaking in multi-speaker
  scenes, and an adult notices the sameness across Hart, Orla, Peverell and Yeo, who should
  sound most unlike.
- *Proposed scope:* line edits only.
  - Keep "I'd want it said" for Jude, who has 11 of the 28 (it is his diffident form of
    Anwen's "I want it said"), and keep Anwen's own. That leaves about 16 lines to recast.
  - Recast the others in each speaker's register: Orla rough and brief; Hart plain and
    gauge-like; Mara dry; Kellan as a sum; Peverell in her columns.
  - Vary or cut about half the "said nothing" lines.
  - Replace the five causal *since* with *because*.
  - Untangle the dividers sentence.
  - Gloss "eleven minutes" in four words or cut it.
  - Write "walls lying flat on the water" in the slate.
- *Strength to preserve:* Perrin's "I'd like it known" (now his alone); Aske's "soonest"; Pike's
  "nearly smiled" (rationed to 3); Hart's turned watch; the Proprietor's dry courtesy.

**For the owner, not prioritised:**

1. Does the sentence target govern dialogue, and how long may a "long" sentence be for the
   read-aloud thirteen-year-old? (§4a)
2. The front-load arithmetic: the whole-book 58 versus the 1.7× shape (§4d).
3. The tide clock: the slack moves one minute between consecutive days (C12). Either make this
   world's tide unusual on the page, or move Wednesday's times about 50 minutes later. If they
   move, Hart's "as yesterday" staff figure and the 6.09 prediction need checking, since the
   prediction is a fortnight on and can stay.
4. The Graving used as a seeding floor (C15) and the slate template (C16): accept as departures
   or repair.
5. `BOOK_MAP` §12: move Rhea going short from Movement Four to Movement Three (C17).
6. "Nothing came" as a partial disclosure (C19), and whether the ledger should note that Aske and
   Pru now suspect.
7. Whether Seven knows how to kill a lodger (C20).
8. The 41-minute hold against a 20-minute quiet (C13); the brown-ink line (C14); "my best
   machine" (C21).
9. Combat density is the lowest of the book (12.3 per 10k). This is not a defect for a harbour
   movement, but Movement Four's Hunt should carry the action the plan promises.

**Strengths to protect in any repair:**

- "It's every count at once"
- the Tarn jar and "It isn't anybody. That's the trouble. It's just people."
- one line for two doors, and "*Laid*… as a man says *amen*"
- "There's no gap… Carrow had to run"
- Hart's barometer
- "It's yours" to Mara, and "I find that I don't care for it at all"
- the kiddle standing upright at slack
- *Far edge*, two words, once
- Rhea's remark against herself
- Orla's "She's—" and Hart's "There."
- the Hoop and "It's gone out of the harbour, into that"
- Perrin asking to be read: "The tape does not know the difference. The lodger did."
- the Proprietor's hand on the glass, "I'm not brave enough", and his laugh
- Pru's "I'm not grateful"
- *yes or no*, never *what*

---

## 7. Method — reproducible command, script hash and limits

Command, run from `/Users/drive/kindling-2680-book-02/books/book-2680-national-measure`:

```
python3 -I provenance/tools/m3_metrics.py manuscript
```

- `provenance/tools/m3_metrics.py` SHA-256 `12036c794861f73e868759a4f73c511186146e751513de7c1af8db0747eb07cd`
- Source copied from `provenance/tools/m2_metrics.py`, SHA-256 `67e20cae24cf6faf0ac09b7b0532eb851f8b14b2b6c3dddd557e48614109ef0f`
  (the same prefix as in the Movement Two review).
- Full diff between the two (only range, labels and viewpoint map changed):

```
2c2
< """Movement Two numerical pass (M1 script, same definitions; files, POV map and chapter count changed; extra block at end). Pure stdlib. Usage: python3 -I m2_metrics.py <manuscript_dir>"""
---
> """Movement Three numerical pass (copy of m2_metrics.py, same definitions; only chapter range, output labels and POV map changed). Pure stdlib. Usage: python3 -I m3_metrics.py <manuscript_dir>"""
6c6
< CHS = list(range(9, 17))
---
> CHS = list(range(17, 25))
10c10,12
< POV = {(10, 4): "Anwen", (12, 0): "Kellan", (14, 1): "Orla", (16, 3): "Mara"}
---
> POV = {(18, 12): "Anwen", (19, 10): "Orla", (19, 11): "Orla", (20, 7): "Rhea", (20, 8): "Rhea",
>        (21, 4): "Mara", (21, 5): "Mara", (21, 6): "Mara", (22, 6): "Kellan", (22, 7): "Kellan", (22, 8): "Kellan"}
> # 22/9 opens "Kiva was sitting on her bed" and stays observable from her bed, so it is Kiva (see report)
216c218
< # ---- Movement Two additions (definitions as described in the M1 review's section 7 prose) ----
---
> # ---- Movement Two additions, unchanged (definitions as described in the M1 review's section 7 prose) ----
252c254
< res["tics_m2"] = {k: len(re.findall(v, tl)) for k, v in EXTRA.items()}
---
> res["tics_m2_lexicon"] = {k: len(re.findall(v, tl)) for k, v in EXTRA.items()}
```

Chapter SHA-256 prefixes at review time (identical to `editions/movement-003-first-draft/` and
to HEAD `f529390`):

| File | Prefix |
|---|---|
| ch. 17 | 10ba1df42887 |
| ch. 18 | c127a92fe598 |
| ch. 19 | 1bcae8cd72b0 |
| ch. 20 | 060c1ed51019 |
| ch. 21 | 0a553d0113de |
| ch. 22 | 791249a2fc7b |
| ch. 23 | 08c050d7d770 |
| ch. 24 | 37b3f9017ce4 |

Supplementary checks (not in the script):

- **Literal doors:** `cat` chapters 17–24, then `grep -oiE ".{0,28}\bdoors?\b.{0,18}"`. All 150
  contexts were read and classified by hand (§4d).
- **"Hold" as a verb:** `grep -oE ".{0,30}\bHold\b.{0,20}"`; 4 of 19 are verbs.
- **Catchphrase speakers:** `grep -n -iE "I'd like it known|\bI'd want\b"` across the eight
  files.
- **Causal *since*:** `grep -n -oE ".{0,50}, since .{0,30}|since there"`, then read by hand.
- **Section lengths:** split on `\n\s*---\s*\n`, then the script's `WORD` regex.
- **Band shares** (6–39, 8–25, narration): computed by importing the script's functions unchanged.

**Uncertainty and limits.**

- The splitter, tokenizer and syllable estimator are heuristics, stable across Movements One to
  Three but not ground truth. Comparisons with the ASR-derived source are directional,
  especially for paragraphs and scene breaks.
- POV segmentation, development beats, supporting-cast beats and the literal-door classification
  are manual judgments. Ch. 22 §9 is the one segmentation call that moves Kiva's share (82.4% vs
  81.3%).
- Book-level front-loading, POV allocation and development spread are provisional at three
  movements of six. The middle third is half-written.
- A same-model review shares the drafter's blind spots. The most useful outside tests would be:
  - a real reader near thirteen, reading lane 1 (ch. 18) and lane 2 (ch. 19) aloud, to see
    whether C1 and C2 are noticed unprompted
  - a cross-family editor pass on P1's fixes
