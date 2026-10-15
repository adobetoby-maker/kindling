# Kindling 2680, Book Two — Movement Five — targeted recheck of the consolidated repair

> Built by TAC

Date: 2026-10-15. Fresh-context targeted verification of the same-author repair of chapters 33–40
(`provenance/MOVEMENT-005-REPAIR.md`). Not an editorial pass, not a cold read, not a score. No prose was edited. The
only file this session wrote is this report. Nothing was committed, pushed or published. No Movement Six work.

## 0. Who and how

- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This is what the runtime states. It
  cannot be verified independently from inside the session.
- Session: Claude Code background job `01a5e43b` (job directory `~/.claude/jobs/01a5e43b`). This is a different session
  from the drafting sessions and the repair session (job `89938c88`). It worked read-only in the worktree
  `/Users/drive/kindling-2680-book-02`, branch `codex/kindling-2680-book-02`. No subagent, other model or Codex/OpenAI
  call was used.
- **This is a same-family, fresh-context check. It is not human review.** It shares a model family with the author of
  the prose and of the repair, so it can share that author's blind spots.
- Inputs read:
  - the repair report, in full
  - the editorial review and the cold read, at the findings the repair cites (C1–C14, K1–K11, P2)
  - the frozen first draft
  - the working chapters, by `git diff --no-index --word-diff=plain` of each frozen chapter against its working
    chapter, with every changed passage read in its surrounding scene
  - `STATE_LEDGER.md` (§2's dream line and the Movement Five block)
  - `provenance/MOVEMENT-005-CONTINUITY.md` (every changed line and §15)
  - the `AUTHORSHIP.md` repair entry
- Out-of-movement reads, for evidence the repair cites: Book Two ch. 24 (the seeding lane of Saturday the 12th) and
  Book One (`book-2680-opening`) ch. 23–24 (the Pit).
- The working chapters' SHA-256 hashes match the repair report's §10 table for all eight files. What was rechecked is
  exactly what the repair left.

## 1. Priority 1 — factual corrections: **PASS**

### 1a. Thursday's lane and the Measure, re-derived from the page

**Thursday v the Tarn second four** (ch. 33:296–415). Rule (ch. 18): three over the hurdle, one for a down, two halves
make a down, a point at the glass.

| Carry | On the page | Running score |
|---|---|---|
| 1 | Anwen downed (Tarn +1); litter on the Tarn's side at the glass (Tarn +1) | 0–2 (marshal: "Two to the Tarn. Nothing to Seven") |
| 2 | the blade downed (+1); the catcher's two halves, a down (+1); the glass in Seven's half (+1) | 3–2 (marshal: "Three to Seven. Two to the Tarn") |
| 3 | "*Down.* The Tarn" (+1); "*Over… Three to Seven*" (+3) | **7–2** |

Every place the 7–2 touches now agrees:
- the marshal, 33:415: "Seven to Seven. Two to the Tarn."
- the board, 33:437: *Seven to two.*
- Perrin, 33:439: "Seven," … "With no fingers."
- the Lane read, 38:147: "seventeen for, twelve against"
- Kiva's reckoning, 38:189: "Seven to two with no fingers"

Seven's Lane is 7–2, 4–5 (ch. 35, "Five to the Ropewalk. Four to Seven") and 6–5 (ch. 37). That is 17 for and 12
against, +5.

**The nine at 2–1, by points for less points against.** The 3–0 fours take places 1–3 in this order:
- the Ropewalk first: 7–0, 5–4, 5–3 (+10)
- Westerley first: 6–3, 6–3, 5–2 (+9)
- Holloway second: 5–3, 6–4, 5–2 (+7)

The 2–1 fours on the page:

| Four | Lanes | Difference | Place | Marks |
|---|---|---:|---:|---:|
| Holloway first | 7–1, 6–3, 3–5 | +7 | 7 | 18 |
| **Seven** | 7–2, 4–5, 6–5 | **+5** | **9** | **16** |
| Halden | 6–2, 5–4, 2–5 | +2 | 10 | 15 |
| Old Four | 6–3, 5–4, 2–5 | +1 | 11 | 14 |
| Westerley second | 5–4, 3–6, 5–4 | −1 | 12 | 13 |

The four 2–1 fours above Seven but off the page are the Tarn second, the Ropewalk second and two unnamed fours (places
4, 5, 6 and 8). The page prints only Seven's place and the two below it ("tenth, two points to the good… eleventh, one
to the good"), so the reconciliation that moves the unnamed eighth four to +6 is off the page and contradicts nothing.

The Tarn second's Thursday is now 2–7. Its two wins off the page must total +15 for it to stay fourth (21 marks). That
is records-only, and it is consistent with C10 (both unnamed fours lost on Thursday and stood at 39 or below after
three).

**The printed Measure (ch. 38:157–203).** Every total is unchanged; those lines are outside the diff. Each re-adds:
- 82 = 58 + 24
- 80 = 65 + 15
- 79 = 56 + 23
- 78 = 64 + 14
- 77 = 59 + 18
- 76 = 54 + 22
- **Seven 69 = 19 + 24 + 10 + 16** (sixth, first, fifteenth and ninth: 38:189)
- 68 = 57 + 11 (Twenty-Eight, 1–2, −1, 14th)
- 68 = 55 + 13 (Westerley second)
- 66 = 46 + 20
- 59 = 38 + 21

Seven is seventh by one mark over Twenty-Eight's 68. The tie at 68 still breaks on the best single place (Hunt first v
Hunt third).

**The ash book still adds.** 6.26 − 0.31 = 5.95. 5.95 − 0.42 = 5.53. 5.53 − 0.38 = 5.15. Spoken at 38:225–227: "thirty-one,
forty-two, thirty-eight. A dram and eleven. Held, five and fifteen." The sealed tin is 2.0, and Thrale's "a dram and
two-tenths of it in her four's sealed tin" (40:185) now names the 1.2 that went into it.

### 1b. The 1 p.m. sum (38:17–27)

Kiva's line is now conditional on Old Four: "if Westerley beat Old Four at two, and the Ropewalk beat Holloway's first
four at three". She adds: "Old Four's sixty-four. If they win at two, they've won three, and it's theirs."

That holds. 64 plus at least 22 is at least 86, above the Ropewalk's 82 and Holloway first's 59 + 24 = 83.

Kellan's two fingers now come after the 3 p.m. lane (38:65–67): "Two. By two marks." That is 82 against Halden's 80.
At 1 p.m. he only looks at the side door. No line elsewhere quotes the old 1 p.m. gesture. The continuity file's
Kellan row (l. 346, "held up two fingers to Kiva from the floor") is still true.

### 1c. The Proprietor's question (39:201)

The line now reads: "The ferry," he said. "Below the Order's house. Last month." … "Were any of the lights white?" It
no longer cites a paper.

His sources are all public:
- the ferry and the Order's house: Kiva's Salt Hall statement, 36:325, and the *Mercury*, 37:19
- lamps going white or out: the keepers' and his own reading

"Lower", "nearer" and "going out" were heard only in the shut shop (34:115). Kiva now volunteers them herself
(39:221).

The protected lines survive verbatim:
- the white disclosure
- the column line
- the hand over his eyes
- "It doesn't prove me right"

### 1d. The Pit in every list of occasions

| Place | Reads |
|---|---|
| 34:107 | "In the Pit last spring, and my aunt wrote that one down the same night." |
| 36:325 | "and in the Pit at home last spring" |
| 37:19 | the *Mercury*: "her name right, and the Pit and the ferry and Classification Day" |
| 39:221 | "Not on Classification Day, not in the Pit, and not when I was thirteen." |
| 39:261 | "at thirteen and on Classification Day and in the Pit and on the ferry, every time" |

All of these agree with the page Kiva asks the Board to open: dated 29th of the fifth month, 2680, "told at the kitchen
table after a fever" (40:65). The Clerk's "at thirteen and since" (40:263) needs no change. Advisory (b) in §5 has one
nuance.

### 1e. The other located corrections

- **"the one piece of the dream she had words for and had kept"** (39:211). It no longer collides with the colour she
  has no word for (39:261).
- **The Tarn lane (ch. 35:89 and 35:267).** It now reads "a week ago, on the Saturday, against the Tarn's first four"
  and "That Saturday". This matches ch. 24: Saturday the 12th, the Tarn's first four, a marshal's walk-round at 24:105.
  Ch. 24:33 says "The Graving was full", which is consistent with "Kiva had thought it was full… She had been wrong."
  "A week ago" for six days before Friday the 18th is acceptable usage.
- **Rows (38:173–181).**
  - Rows go by standing after three: Twenty-Eight 5th, Westerley second 7th, Seven 9th (38:141).
  - The girl is "two rows in front of Kiva, in the seventh row".
  - Dray is "in the fifth row, four rows in front", and Kiva watches her "from four rows back". All three agree.
- **"this morning, after our lane"** (38:289). This agrees with the Rhea cutaway, which pins the card at the baize
  straight after the 10 a.m. lane (ch. 37: "on a floor this morning… I'll pin this at the baize").
- **The draw by lot.** "since the clerk drew it" (37:3).
- **Mara's page and her age.**
  - Mara now says "a girl of seventeen" (39:305), matching 40:91, Thrale's "a girl of seventeen" (40:165) and the
    ledger's age.
  - The four years at the kitchen table (39:211) run from Kindling at thirteen.
- **Dray's "fourteen"** is cut (37:325: "You'll not spend it on a lane, this year or next"). No other line in ch. 33–40
  quotes a Slack cost. The only "one in seven days" lines are Aske's, which were already there (33:63, 37:37).
- **Aske, "your hurt four"** (33:149). His list leaves Anwen out, correctly.
- **Twelve fitters and thirty-six hands** (34:193): "the first watch of Peverell's thirty-six, who would come to the
  table in three twelves before Wednesday". The "thirty-six" at 34:187 means cells. The "who" at 193 marks people, so
  the referent is clear.
- **The Proprietor's age.** The current year is 2681 (33:17; the ledger span: the 17th of the third month, 2681).
  - He was 26 on the night in 2604, and his reading "came to me a year after the window", "since I was twenty-seven"
    (39:185).
  - "A hundred and three" and "seventy-seven years" (39:145, 39:189, and the new 40:127) all agree with 2604 + 77.
- **The closing survey** (40:375): "and, Kiva thought, his right over his eyes, where nobody could see him." It is
  anchored and reads cleanly.
- **Peverell's "great-grandfather's book"** (40:203) now matches the survey. Raised as an owner item; it was not fixed
  earlier in the book.

**Nothing moved beyond the located corrections.** Every hunk in the eight word-diffs was checked. No date, event,
injury, power limit, knowledge boundary or outcome changed except at the corrections listed in repair §1, §2 and §3.

The repair introduces three new facts, and the repair report flags each one:
- the "no change" penalty rule (an owner item)
- Peverell's lineage (an owner item)
- the three-twelves rota for the thirty-six

## 2. Priority 2 — the Graving and the rules: **PASS**

### 2a. The evidence run (ch. 40:33–157)

The order now matches the Clerk's announcement at 40:33: "a sealed page, a notebook, two keepers' books, the
Proprietor's evidence taken this morning, and the returns. It'll hear them in that order".

- **Mara's page** (40:65–85) and **Annick's line** (40:107–115) are read in full, unchanged. The two hands on the bone
  knife (40:53) are intact.
- **The keepers** take one sentence each (40:123, 40:125).
- **The Proprietor's re-read** is reduced to "*I dreamed that night*", Kiva's answer, *A thing she has no word for* and
  the Graving's reaction (40:127–137).
- **The Holloway return.** The old returns are named in a clause (40:139). The new wire is read once, in full, as the
  peak (40:147). Kiva's reaction then leads straight to "It's twenty-five to three… Master" (40:157).

**Nothing the later scenes rely on was lost in compression.** Each later reference is still supported:
- Thrale's "I've heard his reading now, from the Board's clerk" (40:169) rests on "every word… in a flat careful
  voice" (40:127).
- The Clerk's "eleven times since" (40:263) is on the page at 39:169.
- "three readings… this afternoon" (40:267): the Proprietor's in-world, Thrale's and Mara's.
- Peverell's "the page after the night the lamps went white" (40:203) still has "the white lamps on the Long Quay" in
  her one-line reading.
- The clock still runs 2:00 → 2:35 → 2:50 → ~3:00.

**The Holloway return is read in full once.** The original form appears in full only in ch. 34 (34:37–59). In ch. 36:139
it becomes a clause plus its last three lines, and the gallery's laugh (36:143–145) survives. In ch. 40 it is named in
a clause.

### 2b. "And no change" (ch. 37:155–163 and the climax)

The marshal's line now makes the third-carry choice real: "A captain may still call a change after *no change.* It's a
point to the other four for the word, and it goes on her card and yours that the word didn't hold." Perrin answers "I
know the book."

The climax agrees with it at every point:
- **Kiva's reckoning** (37:265) names the costs: the point, Perrin's word, her word to Dray "across the beds" (37:55–83)
  and Wednesday.
- **Perrin's open mouth** (37:269) becomes his offer to take the broken word on his own name.
- **Dray watching Perrin's mouth** for the count (37:275), and her "I was waiting on three" (37:315), now follow from a
  rule that leaves the count possible.
- **The head shake** (37:271) and "the fairest lane I've ever lost" (37:337 ff.) are kept.

The actual third carry adds up: 4–4, then Kiva down (4–5), then Twenty-Eight down (5–5), then the glass to Seven: 6–5
(37:307).

### 2c. Friday's change and the Salt Hall's opening

- **Friday's change** (35:207) now has the marshal's line: "*A change between carries… declared to the box, with nothing
  open in the pause. It's on her card.*" That answers C6: it is a change, not a second door. It agrees with Saturday's
  rule.
- **The Salt Hall's opening** (36:119–123): counsel's "a minute isn't a cause"; the Chair's "So would Mr. Bexley. Ask
  him."; the unassignable *hear, hear*. It sits inside the existing exchange and hands cleanly to Noa's refusal to
  draw a line (36:133). Counsel's seat on the front bench agrees with 36:93.

## 3. Priority 3 — paragraph mass and idiom: **FAIL** (one defect class, two locations)

### 3a. The defect: two resumed speeches lost their reopening quotation mark

Where a gesture beat was inserted mid-speech and the speech resumed with a new tag, two paragraphs now close the
quotation at the tag and never reopen it. The rest of the speech reads as narration.

A quote-parity scan of every paragraph confirms this is new. The frozen edition has **0** paragraphs with an odd count
of `"` in ch. 33–40. The working chapters have **2**, both at these seams:

| # | Location | Text now | Fix (one character each) |
|---|---|---|---|
| D1 | `manuscript/chapter-36.md:207` (Kellan, "what it comes to", after the beat at 36:205) | `"I'm not saying the house wants that," said Kellan. I've sat at the Proprietor's table four times…` | `…said Kellan. "I've sat at the Proprietor's table…` |
| D2 | `manuscript/chapter-40.md:249` (Mara's fitter's rule, after the beat at 40:247) | `"I know one thing," said Mara, and I've known it since a bank on a hill went into step…` | `…said Mara, "and I've known it since a bank on a hill…` |

The other five broken speeches reopen correctly:
- Adlam (36:171), as narration: "Adlam took out…"
- Kellan's Hunt (36:197): `said Kellan, "the house…`
- the Proprietor (39:165), as narration then a quote
- Thrale (40:197): `said Thrale. "If…`
- the Clerk (40:263): `said the Clerk, "that night…`

### 3b. Everything else in Priority 3 checks out

- **No words cut from the seven broken speeches.** The word-diff shows only inserted beats, and pronouns becoming names
  or tags. Each gesture is anchored:
  - counsel's folder (36:93, 36:155)
  - the heavy member's pushed-up spectacles (36:107, 36:135)
  - counsel's pencil
  - the Proprietor's counsel standing behind his chair (39:161)
  - the chairman's gold watch (continuity: "gold watch")
  - Rusk's thumbs, set in his waistcoat at 36:99
  - Peverell's crabbed hands
- **The chains** are split at natural pauses: 35:19, 40:153, 40:307. The longest sentence is 73.
- **"I'd sooner": 13 → 6.** The six kept are exactly the repair's list: Perrin ×2 (33:247, 36:279), Thrale (40:173),
  Mara (39:313), Peverell (40:209) and Dray (40:369).
  - Each recast sounds like its speaker: Aske's "Twice for nothing is cheaper than once too late", Perrin's "Give me
    the foot of the ladder", Orla's "It wants saying before, not after", Dray's "I wanted your crossing".
  - Dray's last "I'd sooner you heard it from me" still answers Kiva's "I wanted you to hear it from me. To your face,
    across the beds" (37:55).
- **"On the table".** The count stays 18 → 18. Both narration restatements are gone (37:289, 40:355). The decision line
  and the characters' uses are kept.
- **"sent for": 5 → 4.** At 37:127 "the thing Perrin had said in the shop" still points back to 34:149 ("as though you'd
  been sent for"), and "as the Long Quay had looked at her last night" has its referent at 36:363.
- **Causal *since*: 4 → 0.** All remaining uses are temporal.
- **"that" (whole word, case-insensitive): 624 → 605.** "She found that": 10 → 3.
- **Protected beats survive verbatim:**
  - *After D. Penhale…* (33:17)
  - "It's trying very hard… at sitting" (33:355)
  - the two hands on the bone knife (40:53)
  - "for want of a better" (40:267, 40:351)
  - Thrale's price (40:193–197)
  - the Holloway reply (40:147)
  - *Fever, the third. Nothing came. Said so.* (40:335)
- **Dialogue length.** Not reshaped. Outside the listed recasts and the tag insertions, no dialogue line changed.

## 4. Frozen edition and records

### 4a. Checksum

```
$ cd books/book-2680-national-measure/editions/movement-005-first-draft && shasum -a 256 -c SHA256SUMS.txt
chapter-33.md: OK
chapter-34.md: OK
chapter-35.md: OK
chapter-36.md: OK
chapter-37.md: OK
chapter-38.md: OK
chapter-39.md: OK
chapter-40.md: OK
```

Exit 0. **The frozen first draft is intact.**

### 4b. Metrics spot check

`python3 -I provenance/tools/m5_metrics.py manuscript` was run with the script unmodified (SHA-256 `9bb5f801…0eb49`,
matching the review). As the repair notes, the script's viewpoint map is keyed to the first-draft sections. No section
was joined or split, so it still applies. This is a spot check, not a gate.

| Measure | Repair §5 after | Recheck run |
|---|---:|---:|
| Body words | 55,416 | 55,416 |
| Sentence mean / median | 10.56 / 7 | 10.56 / 7 |
| ≤5 / ≥40 | 40.3% / 2.3% | 40.3% / 2.3% |
| Longest sentence | 73 | 73 |
| Paragraphs; median; over 60 | 1,472; 25; 23.6% | 1,472; 25.0; 23.6% |
| Sections / mean | 39 / 1,421 | 39 / 1,421 |
| Breaks per 10k, internal / with openings | 5.59 / 7.04 | 5.59 / 7.04 |
| Flesch / FK | 93.8 / 2.8 | 93.8 / 2.8 |
| Dialogue share | 32.3% | 32.3% |
| Progression per 10k | 48.7 | 48.7 |
| Kiva; cutaways | 48,220 (87.0%); 7,196 | 48,220 (87.0%); 7,196 |

The same script on the frozen edition reproduces the repair's "before" column: 55,137; Kiva 47,956; longest 88; 1,451
paragraphs. Chapter `wc -w` counts match repair §4. **Repair §3–§5 is accurate.**

### 4c. Records

All three records say the repair is **not rechecked and not accepted**, and none claims publication:
- the continuity status line
- the Movement Five block of `STATE_LEDGER.md`
- the `AUTHORSHIP.md` repair entry

Their repair lines match the surviving prose:
- 7–2, 17/12, +5, ninth
- the two rules
- the occasions with the Pit
- the Proprietor's question and age
- the Graving order
- the bank cell
- the three twelves
- Orla's two knowledge rows
- §2's corrected dream line

**Stale lines (records only):**

| # | Location | Says | Should say |
|---|---|---|---|
| R1 | `provenance/MOVEMENT-005-CONTINUITY.md:358` (People table, The Tarn) | "second four 6–2 to Seven" | "second four 7–2 to Seven" |
| R2 | `provenance/MOVEMENT-005-CONTINUITY.md:269` (viewpoint note) | "Kiva 48,217 of 55,413 body words" | "Kiva 48,220 of 55,416 body words" (the script's output, and repair §5) |
| R3 | `provenance/MOVEMENT-005-CONTINUITY.md:267` (cutaway table, Orla row) | "1,573" | the script gives 1,565 before and 1,563 after; the Mara row was updated, this one was not. Optional |

The Halden "6–2" at continuity:97 is Halden's own Thursday lane and is correct.

## 5. Advisories (non-blocking; not defects; no repair required)

- **(a) ch. 34:107 pre-spends a beat.** The new clause "and my aunt wrote that one down the same night" tells the four
  about Mara's page, then 34:137 answers Perrin's "Stop how?" with "Mara wrote it down, the night it came, last
  spring…" as though new.
  - It is a small repetition, not a contradiction.
  - If the owner wants the reveal to land once, the clause can be dropped, leaving "In the Pit last spring."
- **(b) "With a fever" over the Pit.** In Book One the Pit vision came awake, in the Pit (ch. 23), and the fever that
  night "did not come" with a dream (ch. 24:105–107).
  - Kiva's lists at 34:107 and 36:325 sit under her umbrella "With a fever." The page itself says "told… after a
    fever", so the lists agree with the page.
  - The looseness is Kiva's own public framing (and the Clerk's), and it was already in the first draft. Owner's call.
- **(c) Kiva's hypothetical at 37:265.** "probably be Seven's, even with a point given away" is 6–5 if Twenty-Eight's
  down falls as it did, or 5–5 if not. "Probably" covers this, as Kiva's own estimate.

## 6. Decision

**One concrete defect requiring a second repair.** It is one defect class, the dropped reopening quotation mark at a
tag inserted mid-speech, in two places. Both are bounded, one-character fixes. Nothing else in the three priorities
needs repair.

Bounded fixes:
1. **D1** — `manuscript/chapter-36.md:207`: insert `"` before "I've sat at the Proprietor's table".
2. **D2** — `manuscript/chapter-40.md:249`: insert `"` before "and I've known it since a bank on a hill".
3. **Records, in the same pass:**
   - R1 — continuity:358: "6–2" → "7–2"
   - R2 — continuity:269: "48,217 of 55,413" → "48,220 of 55,416"
   - R3 (optional) — continuity:267: Orla "1,573" → "1,563"

After these fixes, a quote-parity scan of ch. 33–40 should again return zero odd paragraphs. If it does, and the frozen
edition's checksums still pass, the movement can be taken as accepted for Movement Six context without a further full
recheck. That last call is the owner's.
