# Kindling 2680, Book Two — Movement Two — editorial and numerical review

Date: 2026-10-14. Reviewer: **Claude Opus 5.5 (`claude-opus-5-5`)**, Claude Code background session.

## 0. What kind of review this is

- **This is a same-model, informed editorial pass. It is not a cold read, a human read or
  independent testing.** The movement's drafting author is recorded as Claude Opus 5.5
  (`AUTHORSHIP.md` and the continuity checkpoint). This review was run in a fresh context, without
  the drafting transcript. However, the prompt supplied the plan (`BOOK_MAP.md`), the bible, the
  state ledger, the author's own continuity checkpoint and the formula, so it is **not blind**. The
  two reader lenses are simulated perspectives, not reader research. A same-family reviewer shares
  the drafter's blind spots.
- **The cross-family editor seat was not used.** The `penname-editor` skill routes chapter verdicts
  through a codex harness, one chapter at a time. You asked for a movement review in this session,
  reporting the actual model, so the codex harness was not run. No codex or OpenAI call was made.
- **Coverage.** All eight supplied files were read in chapter order, in full:
  `manuscript/chapter-09.md` to `chapter-16.md`. That is 59,623 words by `wc -w`, or 59,556 body
  words by the script tokenizer, which excludes headings and `---` lines. The files are the
  committed versions at `9a50b97` (unmodified in the worktree; SHA-256 prefixes are in §7). The
  movement is complete as planned: chapters 9–16 of 48, with chapters 1–8 before it. No later
  chapter exists.
- **Canon evidence used.** Only the supplied evidence: `STATE_LEDGER.md` (sections 1–11 and the
  Movement One and Two blocks), `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md` and
  `provenance/MOVEMENT-002-CONTINUITY.md`. Chapters 1–8 and the Book One manuscript were **not**
  read, except for one grep confirming that the van card format *Yard. Now. Finch.* is already used
  in ch. 5. Contradictions inside chapters 9–16 are reported as **verified**. Conflicts with
  Book One or Movement One are reported as **apparent**.
- **Formula source.** `/Users/drive/penname/research/ironprince-craft-formula.md` is present. Its
  SHA-256 matches the recorded `9f97e2f2…c0b8`. The embedded sections 2–6 and 8–9 were used as given.
- **No manuscript prose was changed.** No repair was made, no later chapter was drafted, nothing
  was committed, and no worktree was created.

---

## 1. Unscored reader response

**Where interest caught.** On the first page: the *44* wiped to *43* with a sleeve, and Orla's
sum, which comes out at four and not six. "It was the comfort of a sum that has been done
honestly and comes out short" is a fine line, and it sets the movement's terms. Interest catches
hard when Coombe walks down the Pit steps and ties a knot without looking. It catches again at the
pack's first heal ("one, broad, with nine legs"), and it locks at Perrin's "I was a clock." From
there the movement runs on a clean engine. Each of Coombe's three problems fails first, becomes a
drill, then comes back under pressure. The reader is always one step ahead of the cast, which is a
pleasure. Peaks:

- the lodger going into the seam between two agreeing cells (ch. 11 §4)
- the tap that never comes a second time (ch. 14 §2)
- Kiva calling *Nobody!* on the floor and Perrin shutting without asking why (ch. 13 §3)
- the mill wheel being stopped (ch. 15 §4)
- the kiln husk singing the seventh reed (ch. 15 §6)

**Where it slipped.** The handed-crossing rehearsal (ch. 11 §6–7) is the movement's densest
stretch. One line on a tape, the Chair's incident sheet, unlike and like doors, and a count and a
third all come in under a thousand words. In the Corn Exchange setup (ch. 14 §4), Rhea reads her
slate aloud at length. The money scenes recur: Jude's readings in eight places, Mara's share
explanation (ch. 14 §7), Vane's repeat of it (ch. 15 §7), and Jude's full-month reading (ch. 16 §1).
These are deliberate and in character, but they are where a reader skims. Two small factual
wobbles in ch. 16 also cost trust, in a book that trains its reader to check (§3).

**Who matters.** Kiva first. Then **Perrin**, who has the captaincy, the count, the hatch and
"I don't want this either". He becomes the movement's warmth and its best growth line. Then
**Coombe**, as a standard rather than a friend. Pike's tailboard scene (ch. 14 §6) is the
emotional high point, and he is in four scenes.

**What I expect next.** The fifth crossing at the Saltmere gate mast, and how much longer the hand
will sulk. Orla and Hart meeting. Mara arriving unannounced. The bound plain ash colliding with a
harbour that needs a jar a cell. The handed crossing used live. The dream's "not so high" detail
coming back.

**Would I continue?** Yes, under both lenses. This movement is stronger than its plan required.

---

## 2. Reader-lens scores

Anchors: 5 = understandable but inconsistent; 7 = engaging with located weaknesses; 9 =
compelling with few substantial distractions. These are editorial judgments, not measurements.
The lenses are kept separate and **not averaged** into a gate.

### 2a. Fluent thirteen-year-old reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 7 | ch. 9 §0 (the *43*; Orla's "Count them") | A concrete stake (four crossings, not six) comes before any explanation. But the opening is arithmetic and a calendar, and the first danger arrives three sections in. | Medium |
| Keep reading | 8 | ch. 9 §3–6 (the pack) through ch. 13 §4 (the license) | Every chapter has a local payoff and an open problem. Pressure dips at ch. 11 §6–7 and at the money readings (ch. 14 §7, ch. 16 §1). | Medium-high |
| Interest / freshness | 9 | ch. 11 §4 (the lodger and the laid pair); ch. 15 §4 (the pack keeping the wheel's time) | The monsters are puzzles with rules a reader can solve before the cast does. | High |
| Clarity / flow | 6 | ch. 11 §6–7 ("one line"; "Not a stack"); ch. 16:71 vs 16:309 (the comb) | Each system is explained once, aloud, in a rush. The comb logic contradicts itself in ch. 16. Causal *since* (18.8 per 10k) still trips a one-pass reader. | Medium |
| Character attachment | 8 | ch. 10 §4 (Anwen: "I'm frightened I'll be slow"); ch. 12 §6–7 (Perrin: "I've lost the lane") | Several friends act on their fears, and each one differently. | High |
| Humor / warmth | 8 | ch. 9 §5 ("I was a clock… with a turnip on my knee"); ch. 13 §0 ("I'll not be doing that with my eyes shut in front of a Blaze") | The comedy is character-grounded, and Perrin carries it. "I'd like it known" is close to over-used (11 times). | Medium-high |
| Action / suspense | 9 | ch. 13 §2–4 (the license floor); ch. 15 §4 (the mill) | The fights are trackable, they adapt mid-fight, they cost something, and their length is earned. The lodger reveal in ch. 13 §3 is a superb late turn. | High |
| Progression payoff | 8 | ch. 13 §5 ("under its captain's name"); ch. 13 §6 (a quarter count at both gaps) | Effort visibly changes what the four can do and what is at stake. The hand-to-Ember line is deferred, honestly. | Medium-high |
| Connection | 9 | ch. 9 §7 (Pru: "counting before it's given") → ch. 15 §4 (Perrin: "*Yours*" to Anwen); ch. 10 §2 ("make it walk") → ch. 13 §2 (south-west, not south) | Plants pay off inside the movement and carry state across chapters. | High |
| Read-aloud quality | 6 | ch. 16 §4 (96-word sentence); ch. 9:599 ("Jude's colleague's boot"); ch. 14:143 (stray quote); ch. 12:157 ("two men" for Hesketh and Kellan) | Long *and…and* chains run past a reader's breath. There are several garbled referents. Attribution in dialogue is otherwise clean. | Medium |

### 2b. Adult genre reader

| Dimension | Score | Location | Reason | Confidence |
|---|---:|---|---|---|
| Opening pull | 7 | ch. 9 §0 | The procedural start is redeemed by its thematic line. A reader of the genre will forgive the sum for "whose no it is." | Medium |
| Keep reading | 8 | across the movement; strongest ch. 12–13 | The structure is propulsive. The only longueurs are the ledger readouts. | Medium-high |
| Interest / freshness | 9 | ch. 11 §4; ch. 15 §6 (the kiln) | The spawn ecology is original and rule-bound. The kiln disappointment is a brave beat. | High |
| Clarity / flow | 7 | ch. 11 §6–7; ch. 14 §4 | It is clear to a reader who is used to systems. Two internal contradictions (§3) would be noticed. | Medium |
| Character attachment | 8 | ch. 14 §6 (Pike at the tailboard); ch. 14 §1 (Orla on the Chair's stair) | The adults carry real cost. The Orla cutaway is the best of the four. | High |
| Humor / warmth | 8 | ch. 15 §5 (the miller: "You might have knocked."); ch. 13 §6 (the rope on the step) | The warmth is dry and earned. | Medium-high |
| Action / suspense | 9 | ch. 13 §2–4; ch. 15 §4; ch. 14 §5 (the skin trying to fold Rhea) | Each fight has a contest you can track, adaptation, and a price. | High |
| Progression payoff | 8 | ch. 9 §1 → ch. 16 §0 (the cold creeping up the hand) | The escalating cost of the crossings is the best progression device in the movement. The license is earned on the page. | High |
| Connection | 9 | the laundry and the wharf (M1) → the skin (ch. 10, 13, 14) | Book-scale plants are carried and developed. | High |
| Read-aloud quality | 7 | as in 2a | The register suits an adult reader. The long chains and the slips remain. | Medium |

---

## 3. Canon, physical state, power limits, knowledge and reserved disclosures

Labels: **Verified** = contradiction inside the supplied chapters 9–16. **Apparent** = a conflict
with Book One or Movement One that cannot be checked from the supplied evidence. **Plan** =
departure from `BOOK_MAP.md` or the packet, not a canon error.

| # | Label | Location | Issue | Evidence |
|---|---|---|---|---|
| C1 | **Verified** | ch. 16:71 vs ch. 16:309 | At the ash office (Tue 24th) Kiva is at the counter when, for "the first time … since the thaw", a comb's seventh reed stays still. Three days later at the Order (Fri 27th), the narration says that was "the first time since the thaw that she had heard … nothing on the seventh." | Both lines are in the same chapter. Kiva is present at both (ch. 16 §1: "Kiva stood at the end of the counter"). |
| C2 | **Verified (logic)** | ch. 16:67, 16:83 | The comb logic is muddled. 2669 winter stock predates the Step, so a silent seventh is correct for genuine plain. Pru says it "didn't sing … because there's half as much in it to sing", which blames the seventh's silence on the soot. Dilution should show on the **third** reed, and the text already has that ("The third reed sang, thin and faint"). | `STATE_LEDGER` §6 and the bible: the seventh is cut to the Step, and stock that never heard a beat should not sing it. |
| C3 | **Verified (physical state)** | ch. 15:317, 15:331, 15:335 | Pru's named sheet is used twice. The frosted cloth on the race lip is "Pru's sheet. The one with her own name on the pole", but Kiva threw that cloth as her second. Pru then throws "her own sheet" over the third heap, and the third bag is tied "on her own cloth." 15:317 also says Mrs. Pryce's grey double was left at the hut, so there is no third sheet to explain the gap. | ch. 15 §4 (Kiva "a cloth on each shoulder"; the second cast); ch. 16 §1 (the sheet bought "to replace Finch's"). |
| C4 | **Verified (calendar)** | ch. 16:215 | "three days ago, on a stone on a moor": the kiln was Friday the 20th, and the Order is Thursday the 26th, so it was **six** days. | ch. 15 §6; ch. 16 §5; continuity §1. |
| C5 | **Verified (countdown)** | ch. 16:167–169 | On the 25th Perrin says "Twenty"; Jude replies "Nineteen. Tomorrow's nineteen." The book's own rule is 44 minus the date: 43 on the 1st (ch. 9), 30 on the 14th (ch. 13), 16 on the 28th (ch. 16). That gives **19** on the 25th and 18 on the 26th, so both lines are wrong. | ch. 9 §0; ch. 13 §6; ch. 16 §10. |
| C6 | **Verified (physical state, wording)** | ch. 16:141 (Mara) | "a girl who had lost two fingers on a hill": Kiva lost sensation in two fingers, not the fingers themselves. In free indirect style this reads as literal amputation. | `STATE_LEDGER` §2 Body: the fingers "bend, grip, and report pressure." |
| C7 | **Verified (referent)** | ch. 12:157 | "the two men on the far side, who were only Hesketh … and Kellan": Hesketh is female throughout ("her wall"). | ch. 12 §3, §9. |
| C8 | **Verified (referent)** | ch. 9:599 | "gone back up again with Jude's colleague's boot under his arm" is garbled. Aske's colleague tended Jude's boot (ch. 9 §6). | ch. 9 §6. |
| C9 | **Verified (typography)** | ch. 14:143 | Jude's spoken aside "And Sunday's, which I've not read out." has no opening quote, so it reads as narration, and the line closes on an unpaired `"`. | A scan for odd quote counts flags only this line; ch. 16's multi-paragraph quote is correct style. |
| C10 | **Verified (time and place)** | ch. 13:193 | "She had sat at a kitchen table on Thursday night and heard Perrin say it: *Pryce, when her wall's down. Talley, when he's cut.*" Perrin said this to Coombe on the shed step on Thursday the 5th, in the morning (ch. 11 §0). Ch. 13 is set on Thursday the 12th. | ch. 11 §0. |
| C11 | Apparent | ch. 11:345 | "the hill again, in the ninth month: a corner pinning Selka Dray." The ledger places the second three-door at the Pit on the 17th of the ninth month, the day Dray's leg was broken. Whether that rescue was on a hill is a Book One fact. | `STATE_LEDGER` §2 and §5. Low confidence. |
| C12 | Apparent | ch. 15:413 | "since the second month of the autumn" is a vague month phrase in a numbered-month world. The two fingers were proved on the 4th of the twelfth month (M1.1). It is not a contradiction, just imprecise. | `STATE_LEDGER` M1.1. |
| C13 | Plan | ch. 9–16 | **Four hand-to-Ember crossings, not six.** `BOOK_MAP` §7 places the sixth and certification in Movement Two. The plan's own calendar cannot allow it: one in seven days, from Sunday the 1st, with the 29th on the road. The prose handles this correctly through the Chair's ledger entry. The error is in the plan, not the prose. | `BOOK_MAP` §7; continuity §10.3. |
| C14 | Plan | whole movement | **Viewpoint 93.2% Kiva** against "near or slightly above 87%." The planned Rhea lens is absent. All four cutaways sit below the 2.5–3.7% band (§4f). | packet; `BOOK_MAP` §4. |
| C15 | Plan | whole movement | **Length 59,623** against 47,500–52,500. The plan allows more "unless scenes earn more", and the action scenes do earn it (see the instruction not to shorten fights). The overrun sits mostly in procedure and ledger readouts, not in the fights. | `BOOK_MAP` §4. |
| C16 | Plan (owner) | ch. 16 §6–7 | The Order's binding (*Not for a bank, a floor, a crossing or a sale*) now governs the only plain ash Seven holds. `BOOK_MAP` §8 and §12 plan an honest buyer for it, and the Slack needs a jar a cell. This is a deliberate future constraint. It must be honored, or broken on the page at a cost. | continuity §10.7. |
| C17 | Plan (owner) | ch. 11 §4–5 | The bible's entering form goes to "an open stack". The prose extends it to two people's unlike doors on one load. This is a reasonable, rule-bound invention, and it is the hinge of the handed crossing. It needs owner acceptance. | bible §4; continuity §5.3. |

**Checks that passed.**

- **Arithmetic.** Every running total reconciles to the hundredth. The checks: 9.64 → 9.33 → 9.05
  → 8.81 → 8.59 → 8.29 → 7.83 → 7.68 → 3.24 → 3.06 → 2.75 → 2.60 → 1.53 → 8.93 → 8.63 → 6.23.
  Shares: 59.2 = 29.6 + 4 × 7.4. Bags: 13.8 + 12.6 + 14.7 + 18.1 = 59.2. Month: spent 10.81,
  credited 7.40. Jude's "Up six and a third" checks: 8.93 − 2.60 = 6.33.
- **Weekdays.** Every weekday from Sunday the 1st to Tuesday the 1st of the third month agrees with
  `STATE_LEDGER` §1.
- **Power limits.** Kiva declares the still at every board and only plants: the lane and the
  license floor, where she refuses Anwen's plank. There is no stack on a sanctioned mast, and no
  three-door. Ember appears only as single doors in rehearsal, on the unsanctioned Low Lane mast.
  The crossings fall seven days apart. Aske holds the card after the fourth. Coombe lights only
  the cage ward. Thrale's limit is visible (the gate), as bible §9 requires.
- **Knowledge boundaries.** Kiva tells nobody the dream. Aske learns only that such a fever has
  happened before, and the continuity file records it. Mara's and Orla's decisions to go south
  stay in their cutaways, and Kiva shows no sign of knowing them. Thrale knows that Kiva's lips
  moved, which is consistent with the sister's observation in the ledger.
- **Reserved disclosures.** "Unroofed" and "Breach" appear 0 times. The disk is cold every time.
  The dream is not explained. Its one new detail ("not so high as she had been") is unexplained
  and should stay that way unless the owner directs otherwise.
- **Real month names.** None appear (M1's C1 problem did not recur).

---

## 4. Numerical formula alignment

Method: `python3 -I m2_metrics.py <manuscript_dir>`; the full script is in §7. It is the Movement
One script with the same tokenizer, sentence splitter, syllable estimator and lexicons. Only the
file range and viewpoint map were changed, and one block was added. That block covers the
narration/dialogue split, the literal-door phrase grep and the quote-adjacent tags that the M1
review described in prose, plus a few extra tic counts. Runs on the eight chapters as committed at
`9a50b97`. Anything marked *manual* is the reviewer's judgment.

### 4a. Sentence rhythm — **material drift, changed shape**

| Metric | Target | M2 all text | M2 narration only* | M2 dialogue only | M1 all text (for comparison) |
|---|---:|---:|---:|---:|---:|
| Mean words | 14.6 | **10.8** | 13.2 | 6.2 | 8.8 |
| Median | 11 | **6** | 7 | 4 | 6 |
| Population SD | ~26 | **12.6** | 15.2 | 6.3 | 7.4 |
| ≤5 words | 27.7% | **46.0%** | 43.5% | 63.0% | 43.4% |
| ≥40 words | 3.3% | **4.6%** | 8.0% | 0.2% | 0.5% |

\*Narration has quoted spans removed. Leftover tags ("said Kiva.") count as short sentences. There
are 5,494 sentences; dialogue is 30.3% of words. Per chapter, the short share runs 39.8% to 49.3%,
and the long share 3.4% to 6.8% (ch. 16 is longest at a mean of 12.5).

**Read.** The prose is now **bimodal**. Movement One was uniformly short. Movement Two keeps the
short beats (46%, higher than before) and has grown a heavy long tail in narration: 8% of
narration sentences run 40 words or more, and the longest is 96 (ch. 16 §4). The mid-length band
that the formula's median of 11 implies (6–39 words) holds only **49%** of sentences. The source
shape puts about 69% there. So the long-sentence target is now *exceeded* while the median and the
short share are still far off. Adding more long sentences will not fix that. Converting runs of
short narration declaratives into mid-length sentences would.

**Formula conflict, carried from M1 and still open.** Dialogue alone is 63% short. Whether the
sentence targets govern dialogue is still an owner decision. Without dialogue reshaping, the whole
text cannot reach 27.7% short. The SD target of about 26 is reachable only with a long tail, and
the current tail is already making the prose run on.

### 4b. Paragraphs and scenes — **close**

| Metric | Target (ASR proxy) | Observed (typographic) |
|---|---:|---:|
| Paragraph median / mean | 18 / 26.8 | **18 / 30.8** (1,933 paragraphs; **18.3%** over 60 words; M1 8.8%) |
| Section length | ~950 | **889** (67 sections) |
| Breaks per 10k | ~8.7 | **11.3** counting chapter openings; **9.9** internal `---` only |

The median matches. The mean and the share over 60 words have risen with the long sentences,
because dense narration paragraphs carry them. The longest sections are ch. 15 §6 (the moor and the
kiln, 2,291 words), §4 (the mill, 2,069), ch. 9 §7 (the kitchen, 1,875) and ch. 13 §2 (the floor,
1,840). The fights earn their length. Ch. 9 §7 carries three agendas (the book, Perrin's shame, the
sheet) and could break once.

### 4c. Readability — **large drift**

| Metric | Target | Observed (M1) |
|---|---:|---:|
| Flesch Reading Ease | 72.3 | **96.9** (98.9) |
| Flesch-Kincaid grade | 6.8 | **2.4** (1.6) |

The tokenizer and syllable estimator are those in the script: regex words, a splitter guarded for
abbreviations and initials, and a vowel-group heuristic giving 1.169 syllables per word. The
direction of drift is the M1 one: short median and monosyllabic diction. As in M1, Flesch
under-reads the real difficulty. That difficulty comes from causal *since* (18.8 per 10k, down from
28.4), the impersonal *one* (68.7 per 10k with the numeral), pluperfect chains and dense figures.
Moving the median up (§4a) will move both scores toward target.

### 4d. Progression vocabulary — **near the book average; the opening third is under the implied front-load**

The lexicon is unchanged from M1 (see §7).

- Raw: **351 hits = 58.9 per 10k**.
- All 15 case-sensitive "Edge" hits are the place name **Cowl Edge** or "the Edge" (by grep), not
  the stat. Removing them gives 336 = 56.4 per 10k.
- Literal doors: the phrase grep finds 29 (mostly "shed door(s)" ×14). Some, such as "an open
  door" and "every door that four people light", are system uses. Subtracting 23–29 gives
  **307–313 = about 52 per 10k**.
- Report the movement as **52–56 per 10k** against a book-level 58.
- Within the movement, by equal-word thirds: **98 / 155 / 98**. It peaks mid-movement (the lodger,
  the lane, the license).
- Ash-economy terms are counted separately: **14.1 per 10k**.
- **Cumulative opening third.** By the plan, Movements One and Two are the book's opening third:
  107,796 body words. Adjusted hits are about 235 (M1) and about 310 (M2), roughly **51–55 per
  10k**. The source split (900 : 471 : 514) implies an opening third near **83 per 10k**, so this
  third reaches about 62–66% of that.
- **This is a numerical conflict to bring to the owner.** For the book to show the 1.7× front-load
  from this opening third, the later two thirds would need to average about **31 per 10k**. The
  whole-book average would then come out near 38, well under 58. With an opening third this light,
  both targets cannot be met. The ratio itself cannot be confirmed until later thirds exist. The
  M1 review's point still stands: Kiva was dark for most of M1 by story design.

### 4e. Development beats

**Manual count: Kiva has about 40 choices or realizations, about 6.7 per 10k** (target 4.5, so
above). They are evenly spread: ch. 9 ×7, ch. 10 ×3, ch. 11 ×5, ch. 12 ×4, ch. 13 ×5, ch. 14 ×4,
ch. 15 ×7, ch. 16 ×5. Representative:

- "Then I'd like them on Sundays" (ch. 9 §0)
- "It isn't worse. It's nearer." (ch. 9 §1)
- Pru's count is "the same thing" as *mine* before *yours* (ch. 9 §7)
- "I've been looking for one person" (ch. 9 §7)
- the downhill-skin insight (ch. 10 §2)
- "It isn't a thing I had. It's a thing nobody had." (ch. 10 §5)
- keeping silent at Varley's hem (ch. 11 §3)
- "I am" to Coombe (ch. 11 §5)
- claims the call: "Mine… I'll not be late on my own word" (ch. 11 §7)
- "ash for trust" (ch. 11 §8)
- angry at the word, not at Kellan (ch. 12 §4)
- waits instead of absolving Perrin (ch. 12 §6)
- "That's Pike" (ch. 12 §7)
- "Shut your eyes" (ch. 13 §0)
- south-west, not south (ch. 13 §2)
- refuses the plank (ch. 13 §2)
- stands on the skin (ch. 13 §3)
- looks away from Pike (ch. 14 §6)
- won't decide what "up" means (ch. 15 §2)
- "Stop the wheel" (ch. 15 §4)
- "I'm not to be trusted about it" (ch. 15 §6)
- "It isn't for a year" (ch. 15 §7, ch. 16 §2)
- "the hand first" (ch. 16 §6)
- "I kept my mouth shut. I'd learned how." (ch. 16 §10)

The regex proxy (59 hits, 9.9 per 10k) is inflated by "found that" and "knew that". It is not
comparable to the source and is reported only so the run can be reproduced.

**Supporting cast (manual).** At least fourteen named people get one or more beats, so the beats
are distributed and there is no single deuteragonist:

| Person | Beats |
|---|---|
| Perrin | counts and hauls nothing; "says which"; the tap; "nobody stands together"; the hatch "under my name"; "I don't want this either" |
| Anwen | calls the turn; goes to Mace; "frightened I'll be slow"; tells Kiva first; ties one-handed |
| Pru | "count before it's given"; teaches the cord so that she is "nobody's cord"; "It's a sheet" |
| Jude | "what's it for" three times; holds the mark; comes off on Kellan's weight; names the handed crossing |
| Kellan | writes Seven down; tells them; "I'd like to try it again" |
| Noa | asks leave to keep the question |
| Mara | "two people and one instrument"; the letters; "brave" |
| Orla | going south; Hart |
| Pike | the cost of a craft written down |
| Varley | hears it and keeps folding |
| Rhea | stands on the skin because the second has the edge |
| Aske | "I don't know what longer means"; goes south |
| Vane | names the Order |
| Coombe | "That's why it's yours" |

Perrin runs well above the 0.1–0.7 per 10k band. He is the closest thing to a secondary arc in the
movement, and the formula's §5 shape warns against one character taking most of the secondary
development. In this movement it reads as the captaincy plot, not as a takeover. Watch it across
the book.

### 4f. POV word share (viewpoint segments, not name frequency)

| Lens | M2 words | M2 share | Cumulative M1+M2 words | Cumulative share | Target |
|---|---:|---:|---:|---:|---|
| Kiva | 55,504 | **93.2%** | 96,956 | **89.9%** | ~87% (85–90) |
| Anwen (ch. 10 §4) | 1,297 | 2.2% | 1,297 | 1.2% | 2.5–3.7% |
| Kellan (ch. 12 §0) | 1,134 | 1.9% | 2,456 | 2.3% | 2.5–3.7% |
| Orla (ch. 14 §1) | 949 | 1.6% | 2,075 | 1.9% | 2.5–3.7% |
| Mara (ch. 16 §3) | 672 | 1.1% | 2,226 | 2.1% | 2.5–3.7% |
| Rhea | 0 | 0% | 2,786 | 2.6% | 2.5–3.7% |

The cumulative share sits at the top edge of the band. Every secondary lens is now below 2.5%
except Rhea, and her share all comes from M1. This is not a reason to add cutaways to Movement Two
in repair. It does tell the Movement Three packet to plan for more viewpoint share away from Kiva.
The natural candidates are Orla and Hart, Mara at the harbour, and Rhea on a coast night.

### 4g. Secondary signals (optional per formula §8)

| Signal | Source band | Observed | Note |
|---|---:|---:|---|
| "that" | 92.1 (tighten below) | **143.9 / 10k** | Better than M1's 211.9, still high |
| just / almost / felt / seemed | 5–25 | 0.8 / 0.2 / 5.2 / 0.2 | — |
| -ly words | ~161 | 28.7 raw; **20.5** filtered | **slowly ×39** is a tic (one per 1,500 words) |
| Quote-adjacent dialogue tags | ~41 | **66.7 / 10k** (397) | — |
| Combat terms | ~22 | **29.9 / 10k** | Mostly *cut* (79); present in the background throughout, which the formula wants |
| "out of the" / "one of the" / "for a moment" | 2–4 | 2.2 / 0.0 / 2.7 | — |
| House trigrams | — | "looked at the" 9.1, "she did not" 8.9, "it was not" 7.4, "the far edge" 5.7 | register |

**Character and narrative tics** (raw counts in 59.6k words):

- **"tied a knot" 21.** This is Coombe's device, but at that density in five chapters it becomes
  mechanical.
- "I'd want" 23; "nobody" 128 (thematic — it is the call word).
- "I'd like it known" 11, making 19 across M1 and M2.
- "scratched his jaw" 10; "pale eyes" 8; "for some time" 9; "said nothing" 9; "as one…" 15.
- "something moved/happened at the corner [of the mouth]" 4.

The two catchphrases are good character comedy. At this rate they will reach about 55 each by the
end of the book.

---

## 5. Repair brief — three priorities, bounded

**P1 — Continuity and physical-state line fixes (C1–C10).**
- *Location:*
  - the comb: ch. 16:71 and 16:309, and Pru's explanation at 16:83
  - the sheet ownership: ch. 15:317, 15:331 and 15:335
  - "three days ago": ch. 16:215
  - the countdown: ch. 16:167–169
  - "lost two fingers": ch. 16:141
  - the stray quote: ch. 14:143
  - "two men" (Hesketh): ch. 12:157
  - "Jude's colleague's boot": ch. 9:599
  - "a kitchen table on Thursday night": ch. 13:193
- *Observed issue:* two contradictions in the comb, one physically impossible sheet, one wrong
  interval, one wrong countdown, one wording that implies amputation, and four referent or
  typography slips.
- *Effect on the reader:* this book trains its reader to check sums, and "That adds" is a promise.
  The comb contradiction lands in the movement's emotional close, the first silent seventh, and
  blunts it. The sheet error sits inside the movement's best fight aftermath.
- *Proposed scope:* about ten line edits, with no scene changes.
  - Pru blames the thin *third* reed; the seventh's silence is genuine.
  - At the Order, the first full third with a silent seventh, or the first *true* plain.
  - Pru throws Mrs. Pryce's double, or Kiva's second cloth was Pru's and Pru had the double. Make
    the hut clause and "her own cloth" agree.
  - "six days ago".
  - "Nineteen." / "Eighteen tomorrow." Or keep Perrin's wrong number and let Jude correct it
    properly.
  - "the feeling in two fingers".
  - Add the opening quote at 14:143.
  - "the two on the far side".
  - "with Jude's boot to see to".
  - "on the shed step last Thursday".
- *Strength to preserve:* the comb as a sound-image (the spoon on a glass); Jude's "I've never been
  so sorry not to spend anything"; the frosted sheet Pru refuses to leave behind.

**P2 — Reshape sentence length in narration toward the middle band (formula §2).**
- *Location:* the reflective and transitional narration with the longest *and…and* chains first.
  These are ch. 16 §4 (the road, 96 words), §8 (the ferry, 90), ch. 11 §0 (88), §5 (90), §6 (90),
  ch. 10 §0 (83) and ch. 15 §6 (the moor approach). Then the runs of three or more consecutive short
  narration declaratives, outside fight beats.
- *Observed issue:* median 6 against 11, short share 46% against 27.7%, narration long share 8%
  against 3.3%. The middle (6–39 words) holds 49% of sentences against about 69% in the source.
- *Effect on the reader:* read aloud, the quiet stretches alternate between staccato and run-on.
  The breath-length chains are the main read-aloud cost for the thirteen-year-old lens.
- *Proposed scope:* a focused same-author pass on narration only.
  - Split the 60-plus-word chains into two mid-length sentences.
  - Join adjacent short declaratives where the thought is continuous.
  - **Do not add long sentences.**
  - Interim aim, measured with the same script: median 8–9, short share about 38%, long share 3–4%.
    This is an editorial waypoint, not a revised target.
  - Leave dialogue alone until the owner rules on whether the sentence targets govern dialogue.
- *Strength to preserve:* the fight rhythm of ch. 13 §2–4 and ch. 15 §4 (do not shorten either
  fight); scene-ending short beats ("It sang." / "It's not plain."); the moor's long breath where it
  carries the landscape.

**P3 — Thin the repeated ledger and share readouts for the younger lens.**
- *Location:* ch. 16 §1 (Jude's full-month reading, about 230 words of figures); ch. 14 §7 and
  ch. 15 §7 (the hunt shares explained twice, by Mara and by Vane); ch. 11 §6 (the Chair's sheet
  recalled while the mast reading is still being explained).
- *Observed issue:* most figures in ch. 16 §1 are restatements the reader has already checked. The
  share rule is given in full twice in two chapters.
- *Effect on the reader:* these are the main skim points for the thirteen-year-old lens. They delay
  the road south, which is the movement's last pressure.
- *Proposed scope:* reduce ch. 16 §1 to the opening and closing totals plus the two lines that are
  new: the sheet, and room left for tomorrow. Keep Vane's weighing in ch. 15 §7 as the real moment
  and cut Mara's earlier explanation to one sentence, her "If it's quiet, it's a hand." In ch. 11 §6,
  move the Chair's incident sentence after Noa's "one line", so each thing arrives once. No action
  is cut.
- *Strength to preserve:* the ledger as character (Jude's "That adds" and his refusal to round);
  Mara's closing line on plain ash; Noa's question in his own notebook.

**For the owner, not prioritised:**

- the sentence targets and dialogue (§4a)
- the front-load arithmetic conflict (§4d)
- viewpoint allocation for Movement Three (§4f)
- Perrin's share of the secondary beats (§4e)
- tic rationing: "tied a knot", "slowly", "I'd like it known" (§4g)
- C13 (the plan's hand-to-Ember calendar)
- C16 (the binding of the plain ash)
- C17 (the lodger extended to two people)
- the dream's "not so high" detail

**Strengths to protect in any repair:**

- "a sum that has been done honestly and comes out short"
- "I was a clock"
- Coombe's fail–drill–pressure structure
- the lodger in the seam
- the tap that never comes
- "Shut your eyes"
- *Nobody!* on the floor, and Perrin shutting without asking
- Kiva on the skin
- Pike at the tailboard and the *Cost* line
- the mill wheel stopped under Perrin's name
- the kiln that sings
- Thrale's room where the doors lie down
- "I kept my mouth shut. I'd learned how."

---

## 6. Uncertainty and limits

- The splitter, tokenizer and syllable estimator are heuristics. They are stable between runs (M1
  and M2 use identical definitions) but are not ground truth. Comparisons with the ASR-derived
  source are directional.
- The POV segmentation, development beats and supporting-cast beats are manual judgments.
- The progression adjustment for literal doors is a phrase-grep range, not a hand-tagged count.
- Movements One and Two are two of six. The book-level front-loading, POV allocation and
  development spread are provisional.
- A same-model review shares the drafter's blind spots. The highest-value outside test would be a
  real reader near thirteen, reading ch. 11 §6–7 and ch. 16 §1 aloud. A cross-family editor pass
  on P1's fixes, through the codex harness, would also be more independent than this review.

---

## 7. Method — reproducible command and full script

Command, run from the book directory:

```
python3 -I m2_metrics.py manuscript
```

The script was run from the job scratch directory against
`/Users/drive/kindling-2680-book-02/books/book-2680-national-measure/manuscript`. Script SHA-256
prefix `67e20cae24cf`.

Chapter SHA-256 prefixes at review time:

| File | Prefix |
|---|---|
| ch. 9 | e43856746d41 |
| ch. 10 | 017905dfb8aa |
| ch. 11 | 06cbd37e9066 |
| ch. 12 | 9615755e6f9d |
| ch. 13 | 9f069358d599 |
| ch. 14 | 6803486cc0cd |
| ch. 15 | 928593f86be6 |
| ch. 16 | 825f2c5d1fa5 |

POV segmentation (0-based section index after splitting on `---` lines): ch. 10 §4 Anwen, ch. 12
§0 Kellan, ch. 14 §1 Orla, ch. 16 §3 Mara. Everything else is Kiva.

Supplementary greps:

- `grep -oE "Cowl Edge|the Edge|of the Edge|Edge's"` — all 15 case-sensitive "Edge" hits are place
  names.
- An odd-quote-count line scan — flags only ch. 14:143 outside ch. 16's multi-paragraph quote.

```python
#!/usr/bin/env python3
"""Movement Two numerical pass (M1 script, same definitions; files, POV map and chapter count changed; extra block at end). Pure stdlib. Usage: python3 -I m2_metrics.py <manuscript_dir>"""
import re, sys, statistics as st, json, collections, os

MD = sys.argv[1]
CHS = list(range(9, 17))
FILES = [os.path.join(MD, f"chapter-{i:02d}.md") for i in CHS]

# POV segments: (chapter, 0-based section index) -> lens. Sections split on '---' lines; section 0 includes the heading.
POV = {(10, 4): "Anwen", (12, 0): "Kellan", (14, 1): "Orla", (16, 3): "Mara"}

ABBR = re.compile(r"\b(Mrs|Mr|Dr|St|Mt)\.")
INIT = re.compile(r"\b([A-Z])\.(?=\s*[A-Z])")  # K. Rowan, J.H., M.R.

def clean(t):
    t = t.replace("—", " — ")
    t = re.sub(r"[*_]", "", t)
    return t

def sentences(par):
    p = ABBR.sub(lambda m: m.group(1) + "<DOT>", par)
    p = INIT.sub(lambda m: m.group(1) + "<DOT>", p)
    parts = re.split(r"(?<=[.!?])[\"”’')]*\s+(?=[\"“‘(]?[A-Z0-9])", p)
    out = []
    for s in parts:
        s = s.replace("<DOT>", ".").strip()
        if words(s):
            out.append(s)
    return out

WORD = re.compile(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*")
def words(s):
    return WORD.findall(s)

def syllables(w):
    w = w.lower()
    if w.isdigit():
        return max(1, len(w))  # digits rare; crude
    w = re.sub(r"[^a-z]", "", w)
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w2 = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w2 = re.sub(r"^y", "", w2)
    n = len(re.findall(r"[aeiouy]{1,2}", w2))
    return max(1, n)

chapters = []
for ci, path in zip(CHS, FILES):
    raw = open(path, encoding="utf-8").read()
    secs = re.split(r"\n\s*---\s*\n", raw)
    chapters.append(secs)

all_sents, all_pars, sec_rows = [], [], []
corpus_words = []
pov_words = collections.Counter()
for ci, secs in zip(CHS, chapters):
    for si, sec in enumerate(secs):
        lens = POV.get((ci, si), "Kiva")
        pars = [p.strip() for p in re.split(r"\n\s*\n", sec) if p.strip()]
        sec_w = 0
        for p in pars:
            if p.startswith("#"):
                continue
            c = clean(p)
            w = words(c)
            all_pars.append(len(w))
            sec_w += len(w)
            corpus_words.extend(w)
            for s in sentences(c):
                all_sents.append((ci, si, len(words(s)), s))
        pov_words[lens] += sec_w
        sec_rows.append((ci, si, lens, sec_w))

N = len(corpus_words)
sl = [x[2] for x in all_sents]
res = {}
res["words_body"] = N
res["sentences"] = len(sl)
res["sent_mean"] = round(st.mean(sl), 2)
res["sent_median"] = st.median(sl)
res["sent_pstdev"] = round(st.pstdev(sl), 2)
res["share_le5"] = round(100 * sum(1 for x in sl if x <= 5) / len(sl), 1)
res["share_ge40"] = round(100 * sum(1 for x in sl if x >= 40) / len(sl), 1)
res["max_sentence"] = max(sl)
res["paragraphs"] = len(all_pars)
res["par_mean"] = round(st.mean(all_pars), 1)
res["par_median"] = st.median(all_pars)
res["par_share_over_60"] = round(100 * sum(1 for x in all_pars if x > 60) / len(all_pars), 1)
res["sections"] = len(sec_rows)
res["sec_mean"] = round(N / len(sec_rows))
res["breaks_per_10k_incl_chapter_starts"] = round(len(sec_rows) / N * 10000, 2)
res["breaks_per_10k_internal_only"] = round((len(sec_rows) - 8) / N * 10000, 2)
syl = sum(syllables(w) for w in corpus_words)
wps = N / len(sl)
spw = syl / N
res["flesch_reading_ease"] = round(206.835 - 1.015 * wps - 84.6 * spw, 1)
res["fk_grade"] = round(0.39 * wps + 11.8 * spw - 15.59, 1)
res["syll_per_word"] = round(spw, 3)

# per chapter sentence stats
perch = {}
for ci in CHS:
    s = [x[2] for x in all_sents if x[0] == ci]
    cw = sum(r[3] for r in sec_rows if r[0] == ci)
    perch[ci] = dict(words=cw, sents=len(s), mean=round(st.mean(s), 1), median=st.median(s),
                     le5=round(100 * sum(1 for x in s if x <= 5) / len(s), 1),
                     ge40=round(100 * sum(1 for x in s if x >= 40) / len(s), 1),
                     sections=sum(1 for r in sec_rows if r[0] == ci))
res["per_chapter"] = perch
res["pov_words"] = dict(pov_words)
res["pov_pct"] = {k: round(100 * v / N, 1) for k, v in pov_words.items()}
res["sections_rows"] = sec_rows

text = " ".join(clean(open(p, encoding="utf-8").read()) for p in FILES)
tl = text.lower()

def per10k(n): return round(n / N * 10000, 1)

# Progression lexicon (project-specific; case-sensitive where the stat name collides with ordinary English)
PROG_CS = [r"\bDraw\b", r"\bHold\b", r"\bEdge\b", r"\bStance\b", r"\bWard\b", r"\bRank\b", r"\bFlame\b", r"\bFire\b",
           r"\bTorch\b", r"\bBlaze\b", r"\bGlory\b", r"\bKindled\b", r"\bEmber\b", r"\bHandful\b", r"\bFlask\b", r"\bBarrel\b", r"\bWell\b(?= class)"]
PROG_CI = [r"\brank\b", r"\branks\b", r"\bdoors?\b", r"\bcrossings?\b", r"\bcrossed\b", r"\bstack(s|ed)?\b", r"\bcertif\w*", r"\bclassif\w*",
           r"\bunclassified\b", r"\blicen[cs]e[sd]?\b", r"\bsecond step\b", r"\bfirst step\b", r"\bthimble\b", r"\bre-reading\b",
           r"\bsanctioned mast\b", r"\bcliff\b", r"\bseated\b", r"\bnational license roll\b", r"\bcolumn for\b"]
prog_hits = collections.Counter()
for pat in PROG_CS:
    prog_hits[pat] = len(re.findall(pat, text))
for pat in PROG_CI:
    # avoid double count of 'rank' already counted case-sensitive 'Rank'
    prog_hits[pat] = len(re.findall(pat, text if pat == r"\brank\b" else tl))
# 'Rank' CS and 'rank' CS are disjoint because CI pattern above for rank uses original case text (lowercase only)
prog_total = sum(prog_hits.values())
res["prog_hits"] = {k: v for k, v in prog_hits.items() if v}
res["prog_total"] = prog_total
res["prog_per10k"] = per10k(prog_total)
# by movement thirds (equal word count)
third = N // 3
idx_words = WORD.findall(text)
bounds = [0, third, 2 * third, len(idx_words)]
def prog_in(span_words):
    t = " ".join(span_words)
    n = sum(len(re.findall(p, t)) for p in PROG_CS)
    n += sum(len(re.findall(p, t if p == r"\brank\b" else t.lower())) for p in PROG_CI)
    return n
res["prog_by_movement_third"] = [prog_in(idx_words[bounds[i]:bounds[i + 1]]) for i in range(3)]
# broad tier: ash economy
ECON = [r"\bdrams?\b", r"\bash\b", r"\bheld\b(?=:)", r"\bwarrant\b", r"\bhundredths\b", r"\btenths\b"]
econ = {p: len(re.findall(p, tl)) for p in ECON}
res["econ_hits"] = econ
res["econ_per10k"] = per10k(sum(econ.values()))

# -ly words
ly = re.findall(r"\b[a-z]+ly\b", tl)
LY_EXCL = {"only", "early", "family", "likely", "ugly", "holy", "july", "reply", "apply", "supply", "fly", "belly", "jelly",
           "rally", "ally", "lily", "silly", "bully", "folly", "hilly", "curly", "oily", "lonely", "lovely", "friendly", "elderly",
           "orderly", "kindly_adj", "daily", "weekly", "monthly", "yearly", "nightly", "costly", "deadly", "lively", "comely",
           "unlikely", "wily", "jolly", "woolly", "assembly", "anomaly", "italy", "sly", "ply", "dolly", "gully", "sully", "tally",
           "rely", "imply", "comply", "multiply", "underbelly", "manly", "womanly", "homely", "surly", "burly", "chilly", "grisly",
           "measly", "steely", "princely", "stately", "unruly", "beastly", "ghostly", "leisurely", "cowardly", "scholarly",
           "kelly", "ely", "billy", "bully", "fully_never"}
ly_raw = len(ly)
ly_f = [w for w in ly if w not in LY_EXCL]
res["ly_raw_per10k"] = per10k(ly_raw)
res["ly_filtered_per10k"] = per10k(len(ly_f))
res["ly_top"] = collections.Counter(ly_f).most_common(15)

REPORT = r"\b(said|says|asked|replied|answered|shouted|whispered|muttered|murmured|added|cried|called|told)\b"
rep = re.findall(REPORT, tl)
res["reporting_per10k"] = per10k(len(rep))
res["said_per10k"] = per10k(tl.split().count("said") + len(re.findall(r"\bsaid\b", tl)) - tl.split().count("said"))
res["reporting_top"] = collections.Counter(rep).most_common(10)

COMBAT = r"\b(blade|blades|cut|cuts|cutting|strike|struck|hit|hits|kill|kills|killed|fight|fought|fighting|block|blocked|dodge|dodged|attack|attacked|lunge|swing|swung|slash|wound|wounds|hurt)\b"
cb = re.findall(COMBAT, tl)
res["combat_per10k"] = per10k(len(cb))
res["combat_top"] = collections.Counter(cb).most_common(12)

FILL = ["that", "just", "almost", "felt", "seemed", "since", "rather", "quite", "one", "a good deal"]
res["fillers_per10k"] = {f: per10k(len(re.findall(r"\b" + f + r"\b", tl))) for f in FILL}

TICS = {"I'd like it known": r"i'd like it known", "I want it said": r"i want it said", "That adds": r"that adds",
        "nearly smiled": r"nearly smiled", "scratched his jaw": r"scratched his jaw", "went pink": r"went pink",
        "went scarlet/red": r"went (scarlet|red)", "ears (went|had gone) white": r"ears (went|had gone) white",
        "a good deal": r"a good deal", "four-and-twenty style numerals": r"\b(\w+)-and-(twenty|thirty|forty|fifty)\b",
        "as one ...s (generic 'one')": r"\bas one \w+s\b", "with care": r"with care",
        "for some time": r"for some time", "said nothing": r"said nothing", "I'd sooner": r"i'd sooner"}
res["tics"] = {k: len(re.findall(v, tl)) for k, v in TICS.items()}

# 3-grams
toks = [w.lower() for w in idx_words]
tg = collections.Counter(zip(toks, toks[1:], toks[2:]))
res["top_trigrams_per10k"] = [(" ".join(k), v, per10k(v)) for k, v in tg.most_common(15)]
for ph in [("out", "of", "the"), ("one", "of", "the"), ("for", "a", "moment")]:
    res.setdefault("ref_trigrams", {})[" ".join(ph)] = per10k(tg[ph])

# development proxy (regex): Kiva/she within 120 chars of marker
MARK = r"(realized|realised|decided|for the first time|swore|no longer|found that|understood|made herself|saw that|knew that|had not known|had thought)"
prox = 0
for m in re.finditer(MARK, text):
    win = text[max(0, m.start() - 120): m.end() + 120]
    if re.search(r"\b(Kiva|she|She|her)\b", win):
        prox += 1
res["dev_proxy_markers_total"] = len(re.findall(MARK, text))
res["dev_proxy_kiva_window"] = prox
res["dev_proxy_per10k"] = per10k(prox)

# longest sentences
res["longest"] = [(c, s, n, t[:160]) for c, s, n, t in sorted(all_sents, key=lambda x: -x[2])[:6]]
# month names
res["month_names"] = re.findall(r"\b(January|February|March|April|June|July|August|September|October|November|December)\b", text)
res["reserved_terms"] = {t: len(re.findall(t, text)) for t in ["Unroofed", "Breach", "handed crossing"]}


# ---- Movement Two additions (definitions as described in the M1 review's section 7 prose) ----
DOORLIT = r"\b(by the|open|green|house|through the|at the|to the|oven|shed|colleague's|laundry|side|every|front|kitchen|cage|mill|back) doors?\b"
res["literal_door_phrases"] = len(re.findall(DOORLIT, tl))
res["door_hits_total"] = len(re.findall(r"\bdoors?\b", tl))
# narration vs dialogue split: quoted spans removed
def stats(lst):
    return dict(n=len(lst), mean=round(st.mean(lst),1), median=st.median(lst), pstdev=round(st.pstdev(lst),1),
                le5=round(100*sum(1 for x in lst if x<=5)/len(lst),1), ge40=round(100*sum(1 for x in lst if x>=40)/len(lst),1))
narr, dial = [], []
dial_words = 0
for path in FILES:
    for p in re.split(r"\n\s*\n", open(path, encoding="utf-8").read()):
        p = p.strip()
        if not p or p.startswith("#") or p == "---":
            continue
        c = clean(p)
        q = re.findall(r'"[^"]*"', c)
        for qq in q:
            dial_words += len(words(qq))
            for s_ in sentences(qq.strip('"')):
                dial.append(len(words(s_)))
        n = re.sub(r'"[^"]*"', " ", c)
        for s_ in sentences(n):
            narr.append(len(words(s_)))
res["narration_only"] = stats(narr)
res["dialogue_only"] = stats(dial)
res["dialogue_word_share_pct"] = round(100*dial_words/N,1)
TAGS = r'["\u201d]\s+(said|asked|answered|replied|called|shouted|added|told|whispered|murmured|cried)\b'
res["quote_adjacent_tags"] = len(re.findall(TAGS, text))
res["quote_adjacent_tags_per10k"] = per10k(res["quote_adjacent_tags"])
res["house_constructions_per10k"] = {k: per10k(len(re.findall(k, tl))) for k in ["there was a", "it was a", "she did not", "that she had"]}
EXTRA = {"nobody (all)": r"\bnobody\b", "tied a knot": r"tied a knot",
         "pale eyes": r"pale eyes", "like a man": r"like a man", "as one ": r"\bas one \w+", "I'd want": r"i'd want",
         "under my name": r"under (my|its|his) (own )?(captain's )?name", "for a hand": r"for a hand",
         "since (causal or temporal)": r"\bsince\b", "went red": r"went red", "went pink": r"went pink", "scarlet": r"scarlet",
         "something moved at the corner": r"something (moved|happened) at (the|one) corner", "a queer": r"\bqueer\b"}
res["tics_m2"] = {k: len(re.findall(v, tl)) for k, v in EXTRA.items()}
json.dump(res, sys.stdout, indent=1, default=str)
```
