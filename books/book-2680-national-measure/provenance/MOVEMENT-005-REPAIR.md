# Kindling 2680, Book Two — Movement Five — consolidated repair

> Built by TAC

Date: 2026-10-15. Same-author line repair of chapters 33–40, in place. **Not rechecked, not cold-read after repair,
not accepted, not committed, not pushed, not published.** Chapter 41 was not begun. No Movement Six work.

## 0. Who, what and from what

- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This is what the runtime states;
  it cannot be verified independently from inside the session. No subagent, other model or delegated worker read,
  wrote or edited anything. No Codex or OpenAI call was made.
- Session: Claude Code background job `89938c88` (job directory `~/.claude/jobs/89938c88`). Worked in place in the
  git worktree `/Users/drive/kindling-2680-book-02`, branch `codex/kindling-2680-book-02`. No commit.
- Brief: delivered in-session. On spot comparison its text matches `planning/OPUS-5.5-MOVEMENT-005-REPAIR.prompt.md`
  (188 lines), SHA-256 `f73100865d31d3558ece9bbcd194b5cd6a01fdf23fcddcf8274978ace111d9be`.
- Read before the first edit, in this order:
  1. `provenance/MOVEMENT-005-EDITORIAL-REVIEW.md` (all 932 lines)
  2. `provenance/MOVEMENT-005-COLD-READ.md`
  3. `provenance/MOVEMENT-005-CONTINUITY.md`
  4. `STATE_LEDGER.md` (§1–§11 and the Movement Five block), `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `CHARACTERS.md`,
     `packets/MOVEMENT-005.md`
  5. `manuscript/chapter-33.md` to `chapter-40.md`, completely and in order
- Targeted checks made during the repair (read only):
  - Book Two ch. 24, the seeding lane of the 12th: the Tarn's **first** four, a full Graving, a marshal's walk-round.
  - Book Two ch. 17–32, for any earlier "no change" rule (none) and Peverell's lineage (not stated).
  - Book Two ch. 21, the Saltmere keeper's 2604 entry (the keeper's relation to Peverell is not given).
  - Book One ch. 23–24: the Pit dream came **in the Pit**, and that night's fever brought none. Kiva told it to Mara at
    ten, who wrote the page.
- Measuring script: `python3 -I provenance/tools/m5_metrics.py manuscript`, unmodified (SHA-256
  `9bb5f801c6bfb0e585cdd25897c669eb020786d5ca07d418ef7806a785f0eb49`, as recorded in the review). Run before the first
  edit and after the last. **No section was joined or split, so its first-draft viewpoint map applies unchanged and
  was not remapped.**
- Frozen first draft `editions/movement-005-first-draft/`: `shasum -a 256 -c SHA256SUMS.txt` returned **OK for all
  eight files before the first edit and after the last.** The working chapters were byte-identical to it before the
  first edit (`cmp`). Nothing in that directory was opened for writing.
- Chapters 1–32 were not touched. (`git status` shows chapters 11, 14, 15, 19 and 24 modified. Those edits were in the
  working tree before this session began; they belong to the parallel audio hand-count repair. The chapter 8–9 audio
  fixes were not touched.)

## 1. Priority 1 — the sums and the evidence chain

### 1a. Thursday's lane is 7–2 (review C1, cold read K2); preferred fix (a)

**Evidence.** The rule is on ch. 18:39: three for the litter over your own hurdle, one for a down, two halves a down,
and a point at the glass. In the third carry the page has "*Down.* The Tarn." She knelt. Then: "*Over… Three to
Seven.*" That is +1 and +3 on 3–2, which makes **7–2**. The marshal called "Six".

**Fix (prose).**
- ch. 33, the marshal: "Seven to Seven. Two to the Tarn."
- ch. 33, the board: *Seven to two.* Perrin: "Seven," … "With no fingers."
- ch. 38, the Lane read: "seventeen for, twelve against". Halden and Old Four's places now read "tenth, two points to
  the good, and Old Four eleventh, one to the good". The old "by two points" could be heard as Seven's margin, which
  is now three.
- ch. 38, Kiva's reckoning: "Seven to two with no fingers".

The down is kept and nothing in the lane's action changed.

**Re-derived bracket.**

| Day | Draw | Result (figures on the page; * = reconciliation, off the page) |
|---|---|---|
| Thu | by standing after three, 1v24 … 12v13; every lane to the higher four | Halden (1) 6–2; Old Four (2) 6–3; Holloway first (3) 7–1; Ropewalk first (4) 7–0 v the 21st; TT28 (5) 5–3; Westerley first (6) 6–3; Westerley second (7) 5–4; Holloway second (8) 5–3; **Seven (9) 7–2 the Tarn second (16)**; the Ropewalk second (10)*; the 11th and 12th*, one of them the Tarn first (39), "by a single point and the glass" |
| Fri | winners v winners, by lot | 2–0: the Ropewalk first (5–4 Seven), Westerley first 6–3, Holloway second 6–4, Halden 5–4, Old Four 5–4, Holloway first 6–3. 1–1 (W L): Seven, TT28 (4–6), Westerley second (3–6), the Ropewalk second*, the Tarn first*, the other of 11/12*. Losers v losers gives six 1–1 (L W), among them the Tarn second and the two unnamed Lane fours*, and six 0–2 |
| Sat | by lot, put back to 9 p.m. Fri | 3–0: the Ropewalk first 5–3 Holloway first; Westerley first 5–2 Old Four; Holloway second 5–2 Halden. 2–1: Halden, Old Four, Holloway first, plus the six winners of the 1–1 lanes: **Seven 6–5 TT28**, Westerley second 5–4, the Ropewalk second*, the Tarn second*, the unnamed sixth* and eighth*. No four met another twice in the Lane |

**Lane places among the nine at 2–1, by points for less points against.**

| Lane place | Four | Lanes | Diff. | Marks |
|---:|---|---|---:|---:|
| 4* | Tarn second | 2–7, then two wins off the page totalling +15* | +10 | 21 |
| 5* | Ropewalk second | off the page | +9 | 20 |
| 6* | unnamed (lost Thu) | off the page | +8 | 19 |
| 7 | Holloway first | 7–1, 6–3, 3–5 | +7 | 18 |
| **8*** | **unnamed (lost Thu)** | off the page | **+6** (was +5) | 17 |
| **9** | **Seven** | **7–2, 4–5, 6–5** (17 for, 12 against) | **+5** | **16** |
| 10 | Halden | 6–2, 5–4, 2–5 | +2 | 15 |
| 11 | Old Four | 6–3, 5–4, 2–5 | +1 | 14 |
| 12* | Westerley second | 5–4, 3–6, 5–4 | −1 | 13 |

The top three are the three 3–0 fours:
- the Ropewalk first: 17 for, 7 against, +10
- Westerley first: 17 for, 8 against, +9
- Holloway second: 16 for, 9 against, +7

Twenty-Eight (5–3, 4–6, 5–6; −1) is 14th. The sixth circuit's four is 24th.

**C10 (records only).** The Tarn first four, 39 after three, won its Thursday lane, so it stood 11th or 12th after
three. That leaves at most one unnamed four between the Ropewalk second's 46 and 39. The two unnamed Lane fours lost on
Thursday and won on Friday and Saturday. Each stood at 39 or fewer after three, so neither passes 58 in the Measure
(39 + 19, 39 + 17). The Tarn second's printed 59 stays eleventh.

**The Measure (unchanged; every printed total re-added).**

| Place | Four | After three + Lane marks | Total |
|---:|---|---|---:|
| 1 | Ropewalk first | 58 + 24 | 82 |
| 2 | Halden | 65 + 15 | 80 |
| 3 | Westerley first | 56 + 23 | 79 |
| 4 | Old Four | 64 + 14 | 78 |
| 5 | Holloway first | 59 + 18 | 77 |
| 6 | Holloway second | 54 + 22 | 76 |
| **7** | **Seven** | **53 + 16** (Bench 19 + Carry 24 + Hunt 10 + Lane 16) | **69** |
| 8 | Twenty-Eight | 57 + 11 | 68 |
| 9 | Westerley second | 55 + 13 | 68 (tie lost on best single place: Hunt third v Hunt first) |
| 10 | Ropewalk second | 46 + 20 | 66 |
| 11 | Tarn second | 38* + 21 | 59 |

**Seven is seventh by one mark, on the roll, warranted for the Slack. Every printed total in ch. 38 stands.**

### 1b. The 1 p.m. sum (C3)

ch. 38 §0. Kiva now says: "It's the Ropewalk's, if Westerley beat Old Four at two, and the Ropewalk beat Holloway's
first four at three." She adds: "Old Four's sixty-four. If they win at two, they've won three, and it's theirs."

The check: 64 + 22 to 24 is 86 to 88, more than 82.

Kellan's two raised fingers are moved, with their two following lines, to after the 3 p.m. lane ("He had done the sum
before the shouting stopped"). At 1 p.m. he now only looks toward the side door, "and Kiva knew that he had begun the
same sum and that it would not come out until three."

### 1c. The Proprietor's source (C2, K1)

ch. 39. The line now reads: "The ferry," he said. "Below the Order's house. Last month." He did not lean forward; he
could not. "Were any of the lights white?"

The *Mercury* sentence is gone. "Lower", "nearer" and "going out" were said only in Quiller's shut shop (ch. 34). Kiva
already volunteers them in her answer.

Kept word for word:
- the white disclosure
- "That was choosing a side by leaving a thing out of a column"
- the hand over his eyes
- "It doesn't prove me right"

### 1d. The Pit in every list of occasions (C4)

The page Kiva asks the Board to open records the Pit (the 29th of the fifth month, 2680). Book One ch. 23 puts the
dream in the Pit itself; ch. 24 has her tell it to Mara at ten that night.

| Place | Now reads |
|---|---|
| ch. 34, to her four | "…On Classification Day, in the hall. In the Pit last spring, and my aunt wrote that one down the same night. And on the ferry…" |
| ch. 36, to the Board | "…and on Classification Day, and in the Pit at home last spring, and on the ferry…" The next paragraph already says the aunt wrote it down "the same night, last spring", so the clause was kept short. |
| ch. 37, the *Mercury* | "He had got her name right, and the Pit and the ferry and Classification Day" |
| ch. 39, to the commission | "Not on Classification Day, not in the Pit, and not when I was thirteen." |
| ch. 39, the colour's occasions | "at thirteen and on Classification Day and in the Pit and on the ferry, every time" |

The Clerk's "at thirteen and since" (ch. 40) needed no change.

The ledger's §2 line "No recurrence since Classification Day, 2680", which was the source of the slip, is corrected
in the records (§9).

### 1e. Other corrections

| # | Where | Was | Now | Evidence |
|---|---|---|---|---|
| C5 | ch. 39 | "the one piece of the dream she had kept, even from the page" | "…she had words for and had kept…" | A second kept piece (the colour) comes 50 lines later |
| C11, K3 | ch. 35, twice | "on Saturday, against the Tarn" | "a week ago, on the Saturday, against the Tarn's first four" / "That Saturday"; "a week ago against the Tarn's first four" | ch. 24: the 12th was the Tarn first four, full, with a walk-round. Thursday's Graving was "half full". |
| K4 | ch. 38 | the girl in sea blue "behind Kiva, in the seventh row"; Dray "two rows in front" | "two rows in front of Kiva, in the seventh row"; Dray "in the fifth row, four rows in front"; "from four rows back" | Rows go by standing after three: TT28 fifth, Westerley second seventh, Seven ninth |
| C9 | ch. 38 | Anwen: "pinned it… at noon" | "this morning, after our lane" | Rhea pinned it straight after the 10 a.m. lane |
| C14 | ch. 37 | "since the bag was opened" | "since the clerk drew it" | A draw by lot |
| K5 | ch. 39 | Mara: "a girl of thirteen" | "a girl of seventeen" | The page is dated the 29th of the fifth month, 2680; ch. 40 says seventeen |
| C7 | ch. 37 | Dray: "You'll be on one in fourteen by then, if your healer's right, and you'll not spend it on a lane." (and "Not next year.") | "You'll not spend it on a lane, this year or next." | Nobody had said fourteen; it is the Slack's reserved cost |
| K10 | ch. 33 | Aske: "That's your four." | "That's your hurt four." | Anwen is whole |
| K7 | ch. 40 | Thrale: "a dram and two-tenths in her tin" | "a dram and two-tenths of it in her four's sealed tin" | The Order's 1.2 went into Seven's sealed tin, making 2.0 (ledger §3) |
| K8 | ch. 34 | "twelve fitters" | adds ": the first watch of Peverell's thirty-six, who would come to the table in three twelves before Wednesday" | Thirty-six hands are needed |
| K9 | ch. 39 | "I've had it since I was twenty-seven" (he was 26 in 2604) | "It came to me a year after the window, and I've had it since I was twenty-seven." | Ages |
| C12 | ch. 40 | "…his right over his eyes, and nobody saw him." | "…and, Kiva thought, his right over his eyes, where nobody could see him." | Anchored in Kiva's thought; the survey's music otherwise kept |
| new | ch. 40 | Peverell: "My father's father's book" | "My great-grandfather's book" | The closing survey says "great-grandfather's book" (a protected strength). Earlier chapters do not fix the relation (ch. 21). Found during this repair. |

## 2. Priority 2 — the Graving and the rules

- **The Graving's evidence run (ch. 40 §0; P2).** Compressed without cutting evidence.
  - Mara's page and Annick's notebook are kept in full, unchanged.
  - **The Ferren book** is now one sentence: "The Reader read the Ferren page for Lumb, who was two hundred miles away
    being uncivil about it: a fever of three nights, entered because the needles did it too, and the roof off the
    house, and all four-and-twenty standing up together, looking."
  - **The Saltmere book** is now one sentence: "Peverell read her house's page herself, standing, the long *s* and
    *something was attending* and the white lamps on the Long Quay, and sat down without a word."
  - **The Proprietor's evidence** is read in full in-world (so Thrale's "I've heard his reading now, from the Board's
    clerk" still holds). On the page it is reduced to:
    - its one new line for the town, *I dreamed that night*
    - Kiva's answer
    - *A thing she has no word for*
    - the Graving's reaction
  - **The order.** The returns now follow the Proprietor, with the earlier returns by clause and **the new Holloway
    return in full as the peak**. This is also the order the Clerk announces at the start of the sitting ("a sealed
    page, a notebook, two keepers' books, the Proprietor's evidence taken this morning, and the returns. It'll hear
    them in that order"), which the first draft had broken.
  - Kiva's reaction to the Holloway wire now leads straight to "It's twenty-five to three… Master."
  - The Holloway returns. The original form is read in full only once, in ch. 34, and the new wire only once, in
    ch. 40. In ch. 36 the old form is now a clause ("the night lamp-man's fever of two nights and the warden's
    question") plus its last three lines, which draw the gallery's laugh, a protected beat. In ch. 40 it is named in a
    clause.
- **"No change" (ch. 37; K6, C6, cold-read priority 2).** Option (a), the stated cost. At the box the marshal now says:
  "You know the book, Cade. A captain may still call a change after *no change.* It's a point to the other four for
  the word, and it goes on her card and yours that the word didn't hold." Perrin: "I know the book."
  - At the climax Kiva's reckoning now names the price: the lane "would probably be Seven's, even with a point given
    away for the change. It would cost that point. It would cost the word Perrin had given at the box, and the one she
    had given Dray across the beds. And it would cost Wednesday."
  - Perrin's open mouth is now his offer to take the broken word on his own name: "his word that would be broken, and
    his name the point would go against first."
  - Kept as written: the three carries at full length; Pru calling the pen; Kiva silent; the head shake; Perrin
    shutting his mouth; "the fairest lane I've ever lost".
- **Friday's change of door (ch. 35; C6).** At the marshal's call, after Perrin's "*Ember… declared, single*": "*A
  change between carries,*" said the marshal, "*declared to the box, with nothing open in the pause. It's on her
  card.*"
- **The Salt Hall's opening (ch. 36 §1).** One early moment of opposition, inside the existing exchange. After the
  Chair's minute, Halden's counsel half rises: "The foundation would note, ma'am, that a minute isn't a cause." The
  Chair: "So would Mr. Bexley. Ask him." A *hear, hear* from the gallery that nobody could assign. It hands straight to
  Noa's refusal to draw a line.
- **Colour and Thrale (owner items).** Both left as written.
  - The fever line in ch. 40 ("which had been held, she understood now, by the same thing that had held her doors
    down") is framed as Kiva's understanding, not as the narrator's fact, so "as if" was not added.
  - The colour's existence stays public, as written.

## 3. Priority 3 — paragraph mass and the shared idiom

- **Long hearing speeches, each broken once by a gesture or reaction; no words cut.**

| Speech | Beat inserted | Before | After |
|---|---|---:|---|
| ch. 36 Adlam | counsel turns a page that did not need turning | 174 | 80 + 94 |
| ch. 36 Kellan, the Hunt | the heavy Board member brings his spectacles down, at the midpoint | 207 | 138 + 71 |
| ch. 36 Kellan, what it comes to | counsel's pencil stops | 179 | 90 + 91 |
| ch. 39 the Proprietor | his counsel looks at the floor | 165 | 78 + 88 |
| ch. 40 Thrale's price | the chairman holds his watch shut | 194 | 88 + 109 |
| ch. 40 Mara's fitter's rule | Rusk takes his thumbs out of his waistcoat | 185 | 108 + 79 |
| ch. 40 the Clerk's finding | Peverell's hands close in her lap | 178 | 64 + 117 |

  Where a speech resumed after the beat, a pronoun became a name or a tag was added so the speaker stays clear
  ("Adlam took out…", "said Kellan", "said Thrale", "said Mara", "said the Clerk", "The Proprietor looked…"). Counts are
  a regex word count of each paragraph line (the "before" column is the review's / first-draft count).
- **The long chains were split at the natural pause.**
  - ch. 35 §0, 88 words: now four sentences.
  - ch. 40, 63 words ("and of… and of…"): now three.
  - ch. 40, 66 words with eight *and*s: now three.
  - Kept: the imagined crossing (ch. 37, 73 words) and the planted lean (ch. 35, 65 words).
  - The longest sentence is now 73 (was 88).
- **"I'd sooner": 13 → 6.**
  - Recast, seven:
    - Aske: "Twice for nothing is cheaper than once too late."
    - Kiva to Aske: "I wanted you to hear it from me at this window, not from the Salt Hall."
    - Perrin: "Give me the foot of the ladder, and you saying *set*."
    - Mara: "The Board should know that tonight, and not find it out at six in the morning on the landing."
    - Dray: "I wanted your crossing. I'll say that once."
    - Orla: "It wants saying before, not after."
    - Kiva to the Clerk: "I'll have it left off before I'll have it written wrong."
  - Kept, six:
    - Perrin's "I'd sooner be hated" and "I'd sooner the low town were wet"
    - Thrale's "I'd sooner a house where nothing answers"
    - Mara's "I'd sooner you weren't hot"
    - Peverell's "I'd sooner you signed"
    - Dray's last "I'd sooner you heard it from me", which now answers Kiva's "I wanted you to hear it from me"
      across the beds
- **"On the table".** The two narration restatements of the motif are cut:
  - ch. 37, "a thing set down where anybody could see it" → "a thing she had chosen, in front of Dray and the tiers…"
  - ch. 40, "a thing had been put on a table where anybody could see it" → "a thing had been said aloud"

  The decision line itself ("She would put it on the table", ch. 34) is kept, and so are the Clerk's, Orla's and
  Rhea's. The exact phrase "on the table" counts 18 before and after (case-insensitive): every remaining use is a
  literal table, a document or a character's line. "Put a thing on a table" in narration went from 2 to 0.
- **"sent for" (third use)** in ch. 37 is dropped: "They were looking at her as the Long Quay had looked at her last
  night."
- **Causal *since*: 4 → 0.** All four now read *because*: Orla (ch. 34), the Clerk (ch. 38), the Proprietor (ch. 39)
  and Mara (ch. 40).
- **"that".** Nineteen padding *found that / thought that* in narration became *found / thought*. Parallel "and that"
  clauses were left alone. Whole-word "that": 624 → 605; per 10k 113.2 → 109.2. "She found that": 10 → 3.
- **Voices.**
  - "I'd like it known" stays Perrin's alone: 1, plus Rhea quoting him.
  - "I'd want it said" stays Jude's: 2.
  - Anwen's "I want it said": 2.
  - Dialogue length was not touched.

## 4. Word counts (`wc -w`, headings included)

| Chapter | Before | After | Δ |
|---|---:|---:|---:|
| 33 | 8,547 | 8,542 | −5 |
| 34 | 6,338 | 6,369 | +31 |
| 35 | 6,000 | 6,023 | +23 |
| 36 | 8,030 | 8,147 | +117 |
| 37 | 6,554 | 6,636 | +82 |
| 38 | 6,034 | 6,135 | +101 |
| 39 | 5,573 | 5,585 | +12 |
| 40 | 8,142 | 8,060 | −82 |
| **Movement** | **55,218** | **55,497** | **+279** |

Still inside the packet's 50,000–56,000.
- Ch. 40 is shorter for the compression.
- Ch. 36–38 are longer for the beats, the rule lines and the moved fingers.

## 5. Measures (`m5_metrics.py`, before → after)

| Measure | Target | Before | After |
|---|---:|---:|---:|
| Body words (script) | — | 55,137 | 55,416 |
| Sentence mean / median, all text | 14.6 / 11 | 10.53 / 7 | 10.56 / 7 |
| ≤5 words, all text | 27.7% | 40.6% | 40.3% |
| ≥40 words, all text | 3.3% | 2.3% | 2.3% |
| Narration mean / median | — | 12.3 / 8 | 12.3 / 8 |
| Narration ≤5 / ≥40 | — | 36.9% / 3.8% | 36.6% / 3.8% |
| Dialogue ≤5 | — | 58.8% | 59.0% |
| Longest sentence | — | 88 | 73 |
| Paragraphs | — | 1,451 | 1,472 |
| Paragraph median / mean | 18 / 26.8 | 25 / 38.0 | 25 / 37.6 |
| Paragraphs over 60 words | — | 23.6% | 23.6% |
| Sections / mean | ~950 | 39 / 1,414 | 39 / 1,421 |
| Breaks per 10k, internal | ~8.7 | 5.62 | 5.59 |
| Breaks per 10k, with chapter openings | — | 7.07 | 7.04 |
| Flesch / FK grade | 72.3 / 6.8 | 93.8 / 2.8 | 93.8 / 2.8 |
| Dialogue share of words | — | 32.5% | 32.3% |
| Progression per 10k (raw) | — | 48.6 | 48.7 |
| Viewpoint: Kiva | ~87% | 87.0% (47,956) | 87.0% (48,220) |
| Cutaways (Mara, Orla, Kellan, Anwen, Rhea) | 6,500–8,500 | 7,181 | 7,196 (Mara 1,994; Orla 1,563) |

**Read.**
- The repair broke the seven long speeches and three chains it was asked to break. It did not move the paragraph
  median (25) or the over-60 share (23.6%). Those are spread across 1,472 paragraphs and are mostly narration and
  dialogue blocks the brief did not ask me to touch.
- The sentence distribution and readability are essentially unchanged, as expected for line edits.
- The script is a heuristic, not a gate.

## 6. Phrase counts (raw, ch. 33–40)

| Phrase | Before | After |
|---|---:|---:|
| "I'd sooner" | 13 | 6 |
| "on the table" (case-insensitive, all uses) | 18 | 18 (narration motif restatements 2 → 0) |
| "sent for" | 5 | 4 |
| causal *since* (dialogue) | 4 | 0 |
| "I'd like it known" | 1 | 1 |
| "I'd want it said" | 2 | 2 |
| "I want it said" | 2 | 2 |
| "She found that" | 10 | 3 |
| "that" (whole word) | 624 | 605 |

## 7. Requested items left unchanged, with the reason

- **The fever line held by Thrale (owner item 2).** Left as written. It reads as Kiva's understanding ("she understood
  now"), so the conditional "only if it reads as asserted fact" did not apply. The owner decides.
- **The colour's public existence (owner item 1).** Left as written.
- **Paragraph median and the over-60 share.** Not reached. See §5.
- **Dialogue length and sentence targets for dialogue.** Not touched, as the brief directs, pending the owner.
- **Sections.** No join or split, so the breaks stay at 5.6 per 10k (owner item: accepted for hearings and lanes).
- **The cold read's other repeated phrases** ("pressed to his side" 11, "scarlet" 12, "the warm sound" 10, "had that
  off" ×9). Outside the brief's list; left for the owner.
- **The ch. 33 l.71 Wednesday sentence the cold read found hard to parse.** Not in the brief; left.
- **K11 (the Salt Hall's 8:45 / 8:50 / 8:56 timeline).** Tight but feasible, as both reviews accept; left.
- **Ch. 21 (accepted, closed).** Mara remembers Kiva telling "what she had seen when she was thirteen and again on
  Classification Day" on the Pit night. This is not a contradiction: that night Kiva told the earlier occasions as
  well as the Pit's. No touch.
- **Kellan's Sunday white card** (cold read §3e). It is "a white one with a Halden mark", distinct from the cream card
  he answered. Left; it is Movement Six's.
- **Ch. 1–32** were not edited. No located contradiction required a one-line fix there.

## 8. Owner items (not decided here)

- whether the existence of Annick's unnamed colour may be public
- Thrale's presence holding the fever down as a new interaction property
- whether the sentence targets govern dialogue (59% short)
- the progression shape (~1.4–1.5× front-loaded against the whole-book 58)
- section rhythm (5.6 breaks per 10k)
- the open Movement Three and Four items: the 41-minute hold, the brown-ink line, "my best machine"; Penhale's ward as
  frost
- **New, from this repair, for the owner to confirm:**
  - The "no change" penalty is now a rule on the page (a point to the other four, entered on both cards). The book did
    not state it before.
  - The 2604 Saltmere keeper is fixed as Peverell's great-grandfather.

## 9. Records reconciled

- `provenance/MOVEMENT-005-CONTINUITY.md`:
  - status line
  - §0 note on "slowly"
  - §1 Thursday score and Saturday's card and fingers
  - §2 rules, score, Lane line, reconciliation and C10
  - §3 the occasions, the Proprietor's question and age, the Graving's order and compression, and Peverell's book
  - §5 the occasions
  - §6 Mara's rota and the viewpoint figures
  - §10 Mara's "bank cell"
  - §11 Orla's two knowledge rows
  - a new §15 table of every repair change
- `STATE_LEDGER.md`:
  - §2's dream line, corrected with a dated note
  - the Movement Five status line
  - M5.1 occasions
  - M5.2 score, points and the two declaration rules
  - M5.7 the Proprietor and Mara ("a bank cell")
  - M5.8 Orla
  - dated notes on the §7 and M3.7 knowledge rows
- `AUTHORSHIP.md`: a repair entry.

## 10. Hashes after the repair (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-33.md | 08763fef4ddc5d98592f666905a37ba7f682c8d96d8cfc770801755a140db746 |
| chapter-34.md | db02be11b209ceb017084cff4e5fe8f70c87360f470e43271e6c297bb2f370b3 |
| chapter-35.md | 06cb0ba9c9e6c4b945812022e5d642a632e4420e2e78d4810bc7362f36b389db |
| chapter-36.md | 502dc2e5293a6e5808f6771ae2263b43fe4dd3c52e6e55058ee0ca47af0766c0 |
| chapter-37.md | 62c3aa882679c809e0159dd3208b74710a6f87a1bac70613ec658f3915faa375 |
| chapter-38.md | 14146e401424effa5cac1e2526e234bebae925021fe71d7df3b4e109608a4462 |
| chapter-39.md | f223af04ed884268dd0b9d6b27df57b39717f61cde0547d105c995512b9a5acd |
| chapter-40.md | 0042b5badc8e0f7d8d7ba53ead472db76381a891db3600629833ca0ed8d2ce4b |

A fresh-context targeted recheck of the changed lines against the frozen edition is still owed before acceptance.

## 11. Second repair (2026-10-15)

- Brief: `planning/OPUS-5.5-MOVEMENT-005-SECOND-REPAIR.prompt.md`, SHA-256
  `94c0b14cdfdea9810bfb6062654c33df626c3813cbf9fafc461a3a96a24a8272`, from the fresh-context recheck
  `provenance/MOVEMENT-005-RECHECK.md` (job `01a5e43b`).
- **Runtime-reported model: Claude Opus 5.5, `claude-opus-5-5`**; this cannot be verified from inside the session.
  Same session as the first repair: Claude Code background job `89938c88`. No subagent or other model was used.
- **What changed: five edits, nothing else.**
  - **D1**, `manuscript/chapter-36.md` (Kellan, "what it comes to"): the missing reopening `"` inserted before "I've
    sat at the Proprietor's table".
  - **D2**, `manuscript/chapter-40.md` (Mara's fitter's rule): the missing reopening `"` inserted before "and I've known
    it since a bank on a hill".
  - Both were introduced by the first repair, where a tag was added after a mid-speech beat.
  - In `provenance/MOVEMENT-005-CONTINUITY.md`:
    - **R1**, the Tarn row: "second four 6–2" → "7–2".
    - **R2**, the viewpoint note: "48,217 of 55,413" → "48,220 of 55,416".
    - **R3**, the Orla cutaway row: "1,573" → "1,563".
  - Each figure was checked first against the final `m5_metrics.py` run of the repaired text (Kiva 48,220; body 55,416;
    Orla 1,563). The recheck's numbers were right.
- **Isolation check.** With each new quotation mark removed, chapters 36 and 40 hash to their §10 values. So the only
  change to either file in this pass is the one character.
- **Quote-parity scan of ch. 33–40.** The check counts straight double quotes per paragraph and excludes paragraphs that
  open or continue a multi-paragraph quotation.
  - **0 odd paragraphs.** None needed the exclusion.
  - The frozen edition also gives 0.
- **Frozen edition.** `editions/movement-005-first-draft/`: `shasum -a 256 -c SHA256SUMS.txt` gives OK for all eight
  files (exit 0).
- **Word counts.** `wc -w`: chapter 36 is 8,147 and chapter 40 is 8,060, both unchanged, because a quotation mark is not
  a word. The movement is still 55,497.
- **New hashes (SHA-256), superseding §10 for these two files:**
  - chapter-36.md: `12a152b5c534548360d8dbe5f8353bc2751fb0726f7bb5c17812f04978734dd8`
  - chapter-40.md: `b23b1a3f0229fcba82e1ab832903115bb1a553a0cbc5e85d7fc2438767edc5e3`
  - The other six are as in §10.
- **Status.** Not accepted, not committed, not pushed, not published. The recheck's advisories (a)–(c) were left
  untouched, as the brief directs. Whether the movement is accepted is the owner's call.
