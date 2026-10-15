# Kindling 2680, Book Two — Movement Two — consolidated repair record

Date: 2026-10-14. Seat: Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson.

## 0. What this is

- **A same-author, bounded line repair of chapters 9–16, done in place.** It is not a recheck,
  an acceptance, a cold read or a review. Nothing here has been verified by anybody but the
  repairer. No chapter 17 was drafted. Nothing was committed, pushed or published.
- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** That is what
  the runtime states. It cannot be verified independently from inside the session.
- **Session:** Claude Code background job `80479656` (session file
  `80479656-0763-4f3d-9f66-f2642fb2b403`); remote session `session_01T4x7XmJ1EMJ7Cgi5u6Hx6E`.
- **No subagent, other model or delegated worker** read, wrote or edited any prose or record. No
  codex or OpenAI call was made.
- **Brief:** delivered in-session. On inspection its text matches
  `planning/OPUS-5.5-MOVEMENT-002-REPAIR.prompt.md`, SHA-256
  `fbd07ebfebb72d9e9e73a58eac3a22195ca128266fb69f955a72a9b4793c73b1`. No byte comparison of
  the delivered text was possible.
- **Evidence read, in the required order and in full:**
  1. `provenance/MOVEMENT-002-EDITORIAL-REVIEW.md`
  2. `provenance/MOVEMENT-002-COLD-READ.md`
  3. `provenance/MOVEMENT-002-CONTINUITY.md`
  4. `STATE_LEDGER.md`, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`
  5. `manuscript/chapter-09.md` to `chapter-16.md`, in order, completely

  `OWNER_BRIEF.md` and `AUTHORSHIP.md` were also read. For one Book One fact (item F11 below), I
  searched the Book One context embedded in `planning/OPUS-5.5-MOVEMENT-001.v2.prompt.md`.
- **Measuring script:** `provenance/tools/m2_metrics.py`, SHA-256 `67e20cae24cf…ef0f`. That
  matches the prefix recorded in the editorial review, §7. It was run as
  `python3 -I provenance/tools/m2_metrics.py manuscript` before the first edit and after the last.
  It is a heuristic, not a gate.
- **Line numbers:** "first draft" numbers refer to the frozen edition. "Now" numbers refer to the
  working file after repair.

## 1. Frozen edition

`editions/movement-002-first-draft/` was not opened for writing. Its `SHA256SUMS.txt` was
verified with `shasum -a 256 -c SHA256SUMS.txt` before the first edit, with all eight files OK
and the working files byte-identical to the frozen draft at that point. It was verified again
after the last edit, and again all eight were OK (§9). Chapters 1–8 were not touched.

## 2. Factual corrections (priority 1)

Every correction is the smallest edit I could find that removes the contradiction. Each was
checked against the scene and against `STATE_LEDGER.md`. No event, outcome, date, ash total,
power limit, injury, knowledge boundary or reserved disclosure changed.

| # | Where (now) | Defect | Change | Evidence |
|---|---|---|---|---|
| F1 | ch. 16 l.65, l.77, l.91, l.303 | **The comb.** Two "first silent seventh since the thaw" claims, at the ash office (Tue 24th) and at the Order (Fri 27th). Pru also blamed the silent seventh on the soot. | Ash office: the hush is kept, and the "first time" sentence is replaced. Now Kiva hears what Pru heard: the third reed "sounding yet, and it was thin". Pru: "It's plain, Mrs. Ottery. The seventh's right; it's old enough never to have heard a beat. It's the third that's wrong. It sang thin, because there's half as much in it…" Jude's entry: "silent on the seventh, thin on the third; cut with soot to about half." The Order is now the only "first", and it is qualified: "the first time since the thaw that she had heard a comb held over ash that was whole and plain: the third full, and nothing on the seventh but nothing." The spoon-on-glass image is kept, with "full" added. | Bible §1 (the seventh is cut to the Step; 2669 winter stock predates it); ledger §6. The draft already had the third reed sing "thin and faint" (ch. 16 l.67 draft, kept). |
| F2 | ch. 15 l.101, l.317, l.331, l.335 | **Pru's sheet.** The frosted cloth on the race lip is "Pru's sheet", but Kiva threw it as her second cast. Pru then throws "her own sheet" over the third heap, and the bag is tied "on her own cloth". The grey double is said to have been left at the hut. | Kiva now carries "a cloth on each shoulder, Seven's and Pru's own". Pru carries Mrs. Pryce's grey double "rolled on her back". The race-lip cloth is "Pru's sheet, the second that Kiva had carried down", and that is what is lost. Pru throws the grey double over the third heap, and the third bag is tied "on the grey double". The hut clause is removed. Pru still refuses to leave the frosted sheet behind (l.369, unchanged: "two sheets and a frosted one rolled on Pru's back"). | Ch. 16 l.37: "to replace Finch's" now agrees. Ledger M2.2 ("Finch's own purse sheet frosted and replaced"). |
| F3 | ch. 15 l.519 | **Tallies.** "Talley, four cuts" and "three cords tied". The scenes show five cuts by Jude (four at the mill, draft l.177, 191, 279, 309; one at the kiln, l.453) and four bags tied by Pru (47, 63, 51, 52). | "Talley, five cuts, 0.18." and "Finch, nothing lit; four cords tied". The 0.18 figure is unchanged. | Ch. 15 §4–6. |
| F4 | ch. 16 l.161, l.163 | **Countdown.** "Twenty" on the 25th and "Tomorrow's nineteen" both break the book's rule (44 minus the date). | "Nineteen… Nineteen days. It's the twenty-fifth." and "Eighteen," said Jude. "Tomorrow's eighteen." Perrin's comeback is kept. The closing "Sixteen" on the 28th and "Nobody had told him to count it" are untouched. | Ch. 9 (*43* on the 1st); ch. 13 (*31*→*30* on the 14th); ch. 16 close (16 on the 28th). |
| F5 | ch. 16 l.209 | "three days ago" for the kiln. | "six days ago" (Friday the 20th to Thursday the 26th). | Ch. 15 §6; ch. 16 §5. |
| F6 | ch. 15 l.73 | Tram sheds "a week ago" (the 6th, seen from the night of the 19th). | "a fortnight ago" (thirteen days). | Ch. 11 §1; ch. 15 §2. |
| F7 | ch. 14 l.189 | "Two days, three by the time we're there." The tear was Saturday the 14th, the letter came Monday the 16th, and the team reaches the hut Thursday the 19th. | "Two days, five by the time we're there." | Ch. 14 l.151 (letter); ch. 15 opening (Thursday). |
| F8 | ch. 16 l.135 | Mara: "a girl who had lost two fingers on a hill" reads as amputation. | "a girl who had lost the feeling in two fingers on a hill in the dark". | Ledger §2, Body: the fingers bend, grip and report pressure. |
| F9 | ch. 12 l.157 | "the two men on the far side, who were only Hesketh … and Kellan" (Hesketh is a woman). | "The two on the far side, who were only Hesketh…" The same sentence is also split (§4). | Ch. 12 §3 ("her wall"). |
| F10 | ch. 9 l.599 | "gone back up again with Jude's colleague's boot under his arm" (garbled). | "gone back up again with his colleague, who had seen to Jude's boot." | Ch. 9 l.443 (Aske's colleague kneeling at Jude's boot). |
| F11 | ch. 14 l.143 | Jude's spoken aside "And Sunday's, which I've not read out." has no opening quote and leaves an unpaired one. | Opening quotation mark added. An odd-quote-count scan of chapters 9–16 now flags nothing. | Editorial review §3 C9. |
| F12 | ch. 13 l.193 | "She had sat at a kitchen table on Thursday night and heard Perrin say it". It was said on the morning of Thursday the 5th, to Coombe, in the Old Yard. | "She had stood by the shed step last Thursday morning and heard Perrin say it to the Marshal". | Ch. 11 §0 (Coombe on the shed step; Perrin turns and answers; Kiva present: "Perrin looked at Kiva"). |
| F13 | ch. 11 l.345 | "It was the hill again, in the ninth month: a corner pinning Selka Dray." In Book One, the hill was Stopgate in the tenth month, where Dray *held the count* and four paces east was not clean. The corner over Dray was the Pit on the 17th of the ninth month, the day her leg was broken. | "It was the Pit in the ninth month, over again: a corner pinning Selka Dray…" | Ledger §2 (three clean: yard, **Pit, 17th of the ninth**, Old Yard) and §5 (Dray's leg, the 17th of the ninth). Book One context in `planning/OPUS-5.5-MOVEMENT-001.v2.prompt.md` (the Stopgate table, ~l.2096–2116; "I held a corner for ten in the Pit"). |
| F14 | ch. 15 l.413 | "since the second month of the autumn" (a vague phrase in a numbered-month world). | "since the autumn". | Editorial review C12. The plain phrase avoids inventing a month that the ledger does not give. |
| F15 | ch. 15 l.101 | Coombe said "You'll limp till Thursday" (ch. 9 l.307). Jude still limps on the 20th, and nothing remarks on it. | One clause: Jude's bad leg "had outlasted Coombe's Thursday by a fortnight and was better". | Ch. 9 l.307; ch. 15 §3. |
| F16 | ch. 15 l.425, l.499 | **Knock-on of P3 (§5).** With Mara's share explanation cut from ch. 14, Jude's "an eighth of it" at the kiln comes before anybody on the page has said what the share is. | "a share of it" (twice). Vane's weighing in ch. 15 §7 is now the first place the eighth is stated. | Ch. 14 §7 as repaired; ch. 15 §7. |
| F17 | ch. 14 l.219 | **Introduced by this repair and fixed in it.** My first wording of the van opener, "By the time Kiva was down off the tailboard", put Kiva outside the van during a scene that the slate and "a pause in the van" set inside it. | "By the time Kiva looked out past the tailboard". | Ch. 14 §4. |

**Ledger arithmetic preserved.** No figure, rate or total was changed: 9.64 → 6.23, the four
crossings (0.31, 0.30, 0.31, 0.30), the 59.2 hunt and its shares, the bound 2.0. A string check
confirms that every running total in Jude's entries is still on the page. The totals checked
were: nine and sixty-four, nine and thirty-three, nine and five hundredths, eight and
eighty-one, eight and fifty-nine, seven and eighty-three, seven and sixty-eight, three and
twenty-four, three and six hundredths, two and sixty, eight and ninety-three, six and
twenty-three, five and sixty-three, ten and eighty-one, seven and forty, fifty-nine drams and
two-tenths, twenty-nine and six, "Up six and a third", "Two drams".

## 3. Clarity and narration shape (priority 2)

### 3a. Rules and vocabulary

- **"Ward" as a person.**
  - Ch. 11 §4: the Pit's two "wards in brown", who are people, are now **"Pit hands"** (l.285).
    "The first ward put a hand door under it" is now "The first put a hand door…". "The
    still-door ward took his boot off" is now "The one with the stance took his boot off".
  - The same people are "two Pit hands on a sack" in Kiva's speech at ch. 11 l.405 and ch. 13
    l.351.
  - After this, "ward" in chapters 11 and 13 means only the hand door's tray.
- **Plank vs. unlike doors (ch. 13 §2).**
  - "Kiva did not understand her. Then she did." is cut to "Kiva did not understand her." Her
    "I can't put up a ward" now reads as the mishearing it is, and Anwen corrects it ("Not a ward.
    Your ground.").
  - "It was a plank. / It was a ward on a still door's ground…" is now "It was not a plank. A plank
    was two still doors on one patch of ground. / This was a ward on a still door's ground,
    Anwen's hand door on Kiva's still: two unlike doors on one thing, at once." This names the
    unlike pair and agrees with ch. 11's definition (l.317) and Jude's (l.411).
  - Ch. 13 l.375: Anwen's "put a ward under my heels" is now "put her still door under my heels".
- **The ch. 10 "since" chain (l.185–193)**, recast as short sentences:
  - "On a wharf, it ran downhill, onto the cloth, because the skin was downhill."
  - "And it's downhill when the thing faces uphill. The skin trails behind it."
- **Rung rule planted (ch. 10 l.187).** Coombe now answers: "The rung goes where rungs go. Off a
  heavy edge, it falls away from the edge that cut it. Then down, and to the low side, while it's
  open." Rhea's use of the rule in ch. 14 §4 (l.247, unchanged) is now a payoff.
- **Coombe's lodger reversal (ch. 13 l.107).** One added line, at the moment she sets the lodger
  loose, makes it read as her decision: "On Saturday I kept one off Rowan to teach a rail. This
  isn't teaching. It's a license, and the Longshore won't keep its lodgers away from her to suit a
  card." No scene was added.
- **Causal "since".** Fifteen were recast to "because" where a listener could hear time:
  - ch. 9 l.137, l.159, l.211, l.375, l.535 (Perrin, "since I've always hauled"), l.561
  - ch. 10 the chain above (2)
  - ch. 12 l.313
  - ch. 13 l.295
  - ch. 15 l.381 ("since she had been climbing", the clearest time-reading in the movement)
  - ch. 16 l.115, l.209, l.249

  Count: **112 → 95.** The remaining uses are temporal ("since the spring"), or causal in dialogue
  where the speaker's idiom is clear. These were left, as the brief directs ("not all").
- **Ch. 11 §6: each thing arrives once.** Noa's whole reading now comes in one speech: one line at
  the first pass, and "the same again at the second pass. Ember and stance. One line, for a
  count." Then comes "Whose?", and only then Kiva's recall of the Chair's incident sentence.
  Before, the second-pass reading came after "Whose?" and split the explanation.

### 3b. Point of view (anchors only; headings and scenes unchanged)

| Section | First sentence now | Cue only that person has |
|---|---|---|
| ch. 10 §4 Anwen | "Anwen Pryce went down to the Graywater hall yard … with her hands in her sleeves and the afternoon's wall still aching in both forearms." | The wall she walked that afternoon (physical). |
| ch. 12 §0 Kellan | Unchanged: "Kellan Renn had written down everything that he knew about Team Seven … on four sheets of the refinery's yellow foolscap … in the Halden locker room …" | Already anchored by name, Halden's locker room and refinery paper. An inserted clause made the opening sentence 63 words and was reverted, to keep the opening both reviews protect. |
| ch. 14 §1 Orla | "Orla Dane went up the Chair's stair … with her stick and her bad left knee…" | Her knee (ledger §5). |
| ch. 16 §3 Mara | "Mara Rowan wrote her letter … with the lamp turned down, her reading hand flat on the oilcloth, and her niece asleep…" | Her reading hand (ledger §5, M1.4). |

### 3c. Narration sentence shape (narration only; dialogue left alone)

- **Splits.** About 100 split points were made in about 90 narration sentences, nearly all at an
  existing semicolon or "; and", giving mid-length sentences.
  - **All named targets:**
    - ch. 16 §4 the road (96 words → three sentences; 67 → two)
    - ch. 16 §8 the ferry (90 → two)
    - ch. 11 §0 (87), §5 (90), §6 (90, and the 53-word rig sentence)
    - ch. 10 §0 (83, 74, 67)
    - ch. 15 §6 the moor approach (83 → two, with the landscape clause kept whole)
  - **Every other narration sentence of 60 words or more outside the protected fights.**
  - **About 40 sentences of 40–59 words in quiet or transitional passages.**
- **Joins.** About 15 runs of short narration declaratives that carried one thought were joined.
  Examples:
  - "It was cold, as she had known it would be." (ch. 9, ch. 16)
  - "Kiva had the left hem, and said nothing."
  - "Pike sat on the tailboard and did not get down."
  - "She thought that she might tell Kiva on Thursday, before the yard, and found that she did not
    want to wait so long."
- **Not touched:**
  - the fight rhythm of ch. 13 §2–4 and ch. 15 §4, apart from one-word clarity edits (the plank
    lines, one "since", one "Pit hands")
  - scene-closing short beats ("It sang." / "It's not plain.")
  - Kiva's dream (ch. 16 §9)
  - Thrale's presence (ch. 16 §6)
  - the stillness of the kiln ("It did not run… It did not lean.")
  - "a sum that has been done honestly and comes out short"
  - "It was a queer exchange. It was ash for trust."
  - "It was not a call. It was a name."
- **No breathing commas** between subject and verb were introduced. **No long sentences were
  added.**
- **The longest sentence is now 78 words** (ch. 13 §2, inside the protected floor fight). The
  longest outside a protected fight is under 60.

## 4. Rituals and readouts thinned (priority 3)

| Item | Before | After | How |
|---|---:|---:|---|
| "tied a knot" | 21 | **7** | Kept at Coombe's entrances and verdicts: ch. 9 l.231 (reading Kiva's card); ch. 10 l.111 (entrance), l.341 (to Anwen: "You found it"); ch. 11 l.325 ("Who's thinking of doing that?"); ch. 12 l.303 ("A captain says what's next"); ch. 13 l.103 (the license floor), l.421 ("that's the license"). Also kept: "tied another knot … without looking" (her first entrance), "had tied three knots in the time", "tied the last knot … and coiled it", "a great many knots in it" (ch. 12), and the rope on the step (ch. 13 l.495), which still pays off. Cut, or replaced once with "She turned to the Wren House man" (ch. 11) and "She looked down at the rope in her hands" (ch. 13 §6): the other fourteen. |
| "I'd like it known" | 11 | **10** | All ten are Perrin's. Kellan's borrowed instance (ch. 14 l.87, "as Cade says") is cut, and he says it plainly: "I've been thinking about your tap for six days…". Perrin's count is unchanged; the brief asked only that it return to him. |
| "something moved/happened at the corner [of the mouth]" | 4 phrase hits; 7 instances by hand | **2 instances, both Kellan's** | Kellan keeps his (ch. 12 l.415, l.477), because the second pays off ("this time Kiva could read it"). Coombe: "the Marshal's hands go still on her rope" (ch. 10 l.313; ch. 13 l.401). Mara: "Her pencil tapped once on the tide table / oilcloth" (ch. 9 l.585; ch. 16 l.123). Thrale: "her folded hands moved: one thumb crossed the other, and went back" (ch. 16 l.279). |
| "thirty years" (Coombe and Vane) | Coombe 2, Vane 4 | **Coombe 2, Vane 0** | Vane's marker is now his slate and the thaws he has watched: "since the Line first gave me a slate" (ch. 15 l.55); "I've watched every thaw on this ground bring them down" (l.433); "every year that I've carried a slate" (l.539); the phrase is cut at l.507. Mrs. Ottery's husband's "thirty years" (ch. 16, two uses) is a different person and was left. |
| "slowly" | 39 | **26** | Thirteen cut where the verb or a simile already carried the pace. None was cut inside ch. 13 §2–4 or ch. 15 §4. |
| "scratched his jaw" | 10 | **4** | Kept: ch. 9 l.153, ch. 11 l.411, ch. 15 l.425 ("with his good hand"), ch. 16 l.51. Ch. 9 l.485 becomes "He shifted against the dresser and winced". |
| "pale eyes" | 8 | **3** | Kept for Coombe at ch. 9 l.363, ch. 10 l.199 and ch. 13 l.389 (plus ch. 13 l.479 "The pale eyes", and ch. 9's first description "They were pale"). Rhea's "pale eyes" (ch. 14) is now "her eyes", so she does not share Coombe's descriptor. |

**Van-slate template (ch. 14 §4).**

- The scene now opens partway through the routine. "By the time Kiva looked out past the tailboard,
  Mace's four had the wall up…"
- Rhea's "What's there? Mace." round is cut, with Mace's and Nairn's answers. She goes from her
  *Before* reading straight to "Pike."
- Kept, because they are new: the level-yard exchange ("Flat." / "As a table."), the Marshal's page
  on the slate, Pike's reading, and Rhea's plan.

**Ledger and share readouts.**

- **Ch. 16 §1, Jude's month.**
  - The four full-paragraph readout is reduced to:
    - the opening totals (*held 9.64; sealed 0.8*)
    - one narration sentence saying that he read every line they had already heard
    - the new sheet line (2.40, to replace Finch's)
    - the closing totals (*held 6.23*; spent 10.81; credited 7.40)
    - the spoken-for and uncommitted line (about 0.60; 5.63)
    - "That adds", and "I've left room" for tomorrow
  - About 150 words of restated figures are gone. Every figure removed appears earlier on the page.
- **Ch. 14 §7, Mara's share explanation.** Cut to one sentence: "If it's quiet, it's a hand," she
  said.
  - Vane's weighing in ch. 15 §7 is untouched and is now the only full statement of the shares.
  - Knock-on: F16. Lost with the cut: Mara's attribution of the rule to Rusk, and "that's new this
    year".
- **Ch. 11 §6, the Chair's incident sentence.** Now follows Noa's complete reading (see §3a).

## 5. Before and after numbers

### 5a. `wc -w` (headings included)

| Chapter | First draft | Repaired | Change |
|---|---:|---:|---:|
| 9 | 8,929 | 8,917 | −12 |
| 10 | 6,233 | 6,225 | −8 |
| 11 | 7,919 | 7,891 | −28 |
| 12 | 7,383 | 7,350 | −33 |
| 13 | 7,283 | 7,315 | +32 |
| 14 | 6,357 | 6,129 | −228 |
| 15 | 8,366 | 8,375 | +9 |
| 16 | 7,153 | 7,032 | −121 |
| **Movement** | **59,623** | **59,234** | **−389** |

Ch. 13 grew by Coombe's added line and the plank clarification. Ch. 14 and ch. 16 shrank by the
readout cuts. No action scene lost a beat.

### 5b. Sentence measures (script, all text)

| Measure | Formula | First draft | Repaired |
|---|---:|---:|---:|
| Body words (script tokenizer) | — | 59,556 | 59,150 |
| Sentences | — | 5,494 | 5,518 |
| Mean words | 14.6 | 10.84 | 10.72 |
| Median | 11 | 6 | 6 |
| Population SD | ~26 | 12.55 | 11.18 |
| ≤5 words | 27.7% | 46.0% | 44.6% |
| ≥40 words | 3.3% | 4.6% | **3.6%** |
| Longest sentence | — | 96 | 78 |
| Paragraph median / mean | 18 / 26.8 | 18 / 30.8 | 18 / 30.8 |
| Paragraphs over 60 words | — | 18.3% | 18.2% |
| Flesch Reading Ease | 72.3 | 96.9 | 97.0 |
| Flesch-Kincaid grade | 6.8 | 2.4 | 2.4 |

### 5c. Narration only and dialogue only (script's quote-stripped split)

| Measure | Waypoint (editorial, not a gate) | Narration, first draft | Narration, repaired | Dialogue, first draft | Dialogue, repaired |
|---|---:|---:|---:|---:|---:|
| Sentences | — | 3,139 | 3,181 | 2,928 | 2,907 |
| Mean | — | 13.2 | 13.0 | 6.2 | 6.2 |
| Median | 8–9 | 7 | **7** | 4 | 4 |
| SD | — | 15.2 | 13.2 | 6.3 | 6.3 |
| ≤5 words | ~38% | 43.5% | **41.4%** | 63.0% | 62.9% |
| ≥40 words | 3–4% | 8.0% | **6.2%** | 0.2% | 0.2% |

Dialogue word share: 30.3% → 30.3%.

**Reading.** The long tail moved most:

- the narration long share fell from 8.0% to 6.2%
- the whole-text long share fell from 4.6% to 3.6%, against a formula figure of 3.3%
- the longest sentence fell from 96 words to 78

The short share moved two points. **The narration median did not move, and none of the three
waypoint figures was reached.** Two reasons, both structural:

1. The script's narration split keeps dialogue tags left behind when quotes are removed ("said
   Kiva.") as sentences of two or three words. There are hundreds of these, and they cannot be
   changed without touching dialogue, which the owner has not yet ruled on.
2. Many remaining 40-plus narration sentences are "and…and" chains inside the protected fights, or
   in passages the brief protects: the moor, the dream, Thrale's room. Splitting the rest would
   mean rewording, not repunctuating.

I stopped there, as the brief directs ("Do not chase the number"). The formula targets are
unchanged.

### 5d. Per chapter (script)

| Ch. | ≤5 before → after | ≥40 before → after |
|---|---|---|
| 9 | 48.2 → 47.1 | 3.9 → 3.2 |
| 10 | 45.8 → 43.9 | 4.2 → 2.9 |
| 11 | 47.8 → 45.7 | 4.5 → 3.0 |
| 12 | 46.9 → 45.7 | 4.2 → 3.0 |
| 13 | 49.3 → 48.5 | 4.5 → 4.0 |
| 14 | 41.2 → 39.4 | 3.4 → 2.4 |
| 15 | 46.2 → 44.9 | 5.9 → 4.9 |
| 16 | 39.8 → 38.6 | 6.8 → 5.2 |

### 5e. Counts asked for

| Count | Before | After |
|---|---:|---:|
| "tied a knot" | 21 | 7 |
| "I'd like it known" | 11 | 10 (all Perrin) |
| "since" (all) | 112 | 95 |
| "since" per 10k (script) | 18.8 | 16.1 |

### 5f. Other checks (script)

| Check | Before | After |
|---|---|---|
| Progression hits | 351 (58.9/10k) | 346 (58.5/10k) |
| Combat density | 29.9/10k | 29.9/10k |
| "Unroofed" | 0 | 0 |
| "Breach" | 0 | 0 |
| Real month names | none | none |

POV words by the review's segmentation:

| Lens | Before | After |
|---|---:|---:|
| Kiva | 55,504 | 55,077 |
| Anwen | 1,297 | 1,304 |
| Kellan | 1,134 | 1,134 |
| Orla | 949 | 953 |
| Mara | 672 | 682 |

Kiva's share moved from 93.2% to 93.1%, which is not a viewpoint change.

## 6. Requested items left unchanged, and why

- **The ch. 13 open thread** (did the Pit's sanctioned mast read Perrin's stance and Anwen's ward as
  one line?). **Left and recorded.** The scene names no reader at the mast that morning; Aske stands
  by it with his bag. Answering in a clause would mean deciding a sanctioned-mast procedure, whether
  a Marshal's floor is read, and so whether an incident could have been read. That is a canon fact
  with season-ending stakes for the book's rules. It is not a word the scene already supports. It
  belongs to the owner or to Movement Three's packet.
- **Perrin's own "I'd like it known" (10).** Left. The brief returns the phrase to him and does not
  ask for it to be rationed. The editorial review lists rationing as an owner item.
- **Kiva's strapped knee** (the cold read's physical note). Left. It is carried from Book One
  (ledger §2) and is not a defect.
- **"Vane's weighing" wording** (the shares) and Jude's "Up six and a third". Left exactly.
- **Sentences of 60 words or more inside ch. 13 §2–4 and ch. 15 §4** (five sentences, 63–78 words).
  Left, because the fight rhythm is protected.
- **The dream, Thrale's room and the kiln stillness.** Left, including a 50-word sentence in the
  dream (ch. 16 §9) and one of 45 words in Thrale's room.
- **The van routine in ch. 11.** Left in full. It is the template's first run. Only its ch. 14
  repeat was opened partway.

## 7. Owner items: touched or deliberately left

- **Whether sentence targets govern dialogue.** Not decided. Dialogue was not reshaped. One-word
  clarity edits inside speech were made where the brief named them:
  - the ch. 10 "since" chain
  - Perrin's "since I've always hauled"
  - "Pit hands" in Kiva's speech
  - Anwen's "her still door"
  - Kellan's dropped catchphrase
  - Jude's tallies and "a share"
  - the countdown numbers
  - Pru's comb explanation
  - the readout reductions

  Coombe's one added line is new speech, requested by the brief.
- **The front-load progression arithmetic.** Untouched (58.9 → 58.5 per 10k, from incidental cuts).
- **The plan's six-crossing calendar.** Untouched. The prose stands at four. The plan, not the
  prose, is out of step.
- **The Order's binding of the plain ash.** Untouched, word for word.
- **The lodger extended to two people's unlike doors.** Untouched. Only the people's job title
  changed ("Pit hands").
- **Viewpoint share for later movements.** Untouched. The four anchors are cues, not added words of
  lens.
- **Owner-protected wording.** No owner-authored passage was identified inside chapters 9–16. The
  only verbatim canon quotation in the records, Rhea's card, does not appear in these chapters.
  Nothing that is owner wording was restyled.

## 8. Records reconciled

- `provenance/MOVEMENT-002-CONTINUITY.md`: a dated repair note was added. The entries for the
  comb, the sheets, the tallies, the countdown, the rig's ninth-month reference, the Pit hands, the
  shares and the ledger readout were corrected to the surviving prose.
- `STATE_LEDGER.md`, Movement Two block: the status line, the equipment line (sheets), the sealed
  2.0 comb note, and a repair note.
- `AUTHORSHIP.md`: a Movement Two consolidated repair entry.

None of these claims a recheck, an acceptance, publication, or any work on Movement Three.

## 9. Frozen edition, verified after repair

`cd editions/movement-002-first-draft && shasum -a 256 -c SHA256SUMS.txt` returned
`chapter-09.md: OK` through `chapter-16.md: OK`, all eight, after the last manuscript edit.

## 10. Second repair — 2026-10-14

A bounded same-author fix of the one defect the fresh-context recheck found
(`provenance/MOVEMENT-002-RECHECK.md`, job `7508774e`, D1), plus its two record lines. Brief:
`planning/OPUS-5.5-MOVEMENT-002-SECOND-REPAIR.prompt.md`. Exactly three edits were made.

1. **`manuscript/chapter-16.md` l.135 (Mara's cutaway).**
   - Change: "lost the feeling in two fingers on a hill in the dark" became "lost the feeling in two
     fingers **in the Pit in the autumn**".
   - Why: the fingers went in the Pit in the ninth month (Book One ledger; ch. 13 "since the ninth
     month"). The hill was Stopgate, in the tenth month, and that night cost the arm, which came
     back.
   - "Autumn" for that Pit matches ch. 9 l.187. Only that phrase changed. Read aloud, the sentence
     keeps its order and stress.
2. **`provenance/MOVEMENT-002-CONTINUITY.md` l.216:** "new this year" was dropped from the Board's
   eighth, because the phrase is no longer on the page.
3. **`provenance/MOVEMENT-002-CONTINUITY.md` l.310:** "two Pit wards" became "two Pit hands".

- No other prose was touched.
- `wc -w manuscript/chapter-16.md`: **7,032** (unchanged; three words replaced three). The movement
  total is still 59,234.
- The frozen edition `editions/movement-002-first-draft/` still verifies. `shasum -a 256 -c
  SHA256SUMS.txt` returns OK for all eight files.
- Runtime-reported model: **Claude Opus 5.5, `claude-opus-5-5`**. This cannot be verified
  independently from inside the session.
- Session: Claude Code background job `fdbd4fb4` (session file
  `fdbd4fb4-e073-4ad5-884b-c2c3b3436ee6`); remote session `session_01X5eTxJATPj6Q2KLczH1fgf`.
- No subagent or other model was used.
- Not confirmed, not accepted, not committed, not published. No Movement Three work was done.
