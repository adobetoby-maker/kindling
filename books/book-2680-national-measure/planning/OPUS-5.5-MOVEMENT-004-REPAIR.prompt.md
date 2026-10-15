# Kindling 2680, Book Two — Movement Four consolidated repair

You are Claude Opus 5.5, returning as the prose author for *The National Measure*, public
byline Monroe Jackson, internal seat Monroe Jackson 1.3.0 / O'Connor 1.3.0. This is one bounded
same-author repair of the completed fourth movement (Chapters 25–32). Do not draft Chapter 33.
Do not redesign the movement. Do not launch subagents or other models; you repair and report
yourself. Read both review reports and all eight chapters before editing.

## Required evidence, in this order

1. `books/book-2680-national-measure/provenance/MOVEMENT-004-EDITORIAL-REVIEW.md` (informed,
   same-family; Section 3 arithmetic and findings C1–C20, Section 4 numbers, Section 6 brief)
2. `books/book-2680-national-measure/provenance/MOVEMENT-004-COLD-READ.md` (manuscript-only
   simulated read, same model family, not human feedback; Sections 3, 4, 5)
3. `books/book-2680-national-measure/provenance/MOVEMENT-004-CONTINUITY.md`
4. `books/book-2680-national-measure/STATE_LEDGER.md` (Movement Four block), `UNIVERSE_BIBLE.md`,
   `BOOK_MAP.md`, `CHARACTERS.md`, `packets/MOVEMENT-004.md`
5. `books/book-2680-national-measure/manuscript/chapter-25.md` through `chapter-32.md`,
   completely and in order

The exact first draft is frozen, read-only, under
`books/book-2680-national-measure/editions/movement-004-first-draft/` with `SHA256SUMS.txt`.
Never edit it. Edit only the working files `manuscript/chapter-25.md` to `chapter-32.md` and the
records named under Deliverables. Chapters 1–24 are accepted and closed: do not touch them unless a
located contradiction forces a one-line fix, and record any such touch. Line numbers in the reviews
are first-draft numbers; find passages by their text.

Measuring script: `provenance/tools/m4_metrics.py`
(`python3 -I provenance/tools/m4_metrics.py manuscript`). Run it before the first edit and after the
last. It is a heuristic, not a gate.

## Three repair priorities (the whole job)

### 1. Make the boards add up, and fix the line-level continuity (smallest edit each)

- **The Bench places (ch. 25 heats at ~l.151 and ~l.283; continuity §3).** This is the one slip that
  changes a result. Seven is sixth on the Bench with a 4:10 find ("the slowest in the heat by a
  minute") and a step at 8:40. The only rule that puts a stepped four above other stepped fours is
  ranking by length of hold; under that rule the page's own times put three unnamed fours (heat one's
  "stepped at eight minutes, and another at six"; heat three's "At six, one of the three Kiva did not
  know") above Westerley second (5:20) and Holloway second (5:00), and Seven (53) would stand seventh,
  on the roll, contradicting the movement's exit (ninth). Fix on the page, **not by changing the
  printed boards or Seven's ninth place**: have the Clerk say the marking rule once in her opening
  (for example, "A four that holds is marked by its find. A four that steps is marked by how long it
  held."), then make the heat times obey the reconciliation: heat one's unknowns step before 5:00
  ("A four Kiva did not know stepped at four minutes, and another at three"); heat three's unknown
  steps before 5:00 ("At four, one of the three…"); give the Tarn's step on the page between 5:00 and
  5:20 ("The Tarn's went at five and ten; Trewin did not move."). Verify every on-page step time
  against the printed Bench ranking and the after-two and after-three sheets (Halden 65, Old Four 64,
  Ropewalk first 58, Seven 53, Holloway second 54 …); the sums must hold. If you find a cleaner
  consistent fix, use it and record it.
- **The rail minute (ch. 25 ~l.169 vs the Clerk's rules ~l.23–29).** Kiva says there is "a minute at
  the rail, between the quench and the tune. The Clerk read it out this morning." The rules as quoted
  do not include it. Add one clause to the Clerk's opening ("…and a minute at the rail between the
  quench and the tune, as at home") or show Halden take and waive it in heat one.
- **The water's direction (ch. 27 ~l.217 vs ~l.89).** At the ladder the water pushes at the backs of
  their legs "as it went down the chamber toward the tail"; walking to the tail it is "running against
  them now… like walking up a river". Make one direction true (the water is entering at the head and
  runs with them toward the tail); keep the river image only if it belongs to wading against the press
  at the stair.
- **Aske's position (ch. 27 ~l.241):** "I felt it go from the bottom of the ladder; everybody did" →
  "I heard it go from the lip; everybody did." (He was on the quay.)
- **Orla's reading (ch. 25 ~l.233 vs ch. 32 ~l.513):** make the two agree ("with her lips moving, the
  way Pru always did" or change the ch. 32 line).
- **When Kiva hears about Skerry Pill (ch. 30 ~l.183 vs ch. 32 ~l.129 and ch. 29 ~l.31):** narration
  says "not until three o'clock, at the gate"; Kiva later says "I heard. On the causeway." Make the
  places agree ("until the cart, on the causeway") and keep the combing place consistent (ch. 29
  "landward end of the causeway" vs ch. 32 "the gate on the timber pond"; combing begins at four).
- **Penhale's "When it's printed, I'll read it" (ch. 32 ~l.445 vs ch. 29 ~l.349):** Coombe says he said
  it "on the causeway this morning, in the queue"; the page shows him saying it to Kiva in the channel
  on Mallow Creek. Make the two sources agree (Coombe heard it the same way, or he said it twice).
- **Yeo's clock (ch. 31 ~l.371):** "Forty minutes later" → "Half an hour later" (near post 12:14; Penhale
  under the fold at about 12:45), and "twenty past twelve" → "a quarter past twelve".
- **Kellan's distance (ch. 30 ~l.61 vs ~l.3):** "forty paces off" → "sixty paces off".
- **Perrin's rehearsal climb (ch. 26 ~l.39):** twenty-two plants "came up with my door open" are not on
  the book. Add "off his own thimble" (do not change any held figure).
- **The Clerk's rule (ch. 29 ~l.49) vs Kiva and Pru going under the posts (~l.301–331):** "A four does
  not go onto the mud below a form on running water" has no officer exception; add "but on its
  officer's word".
- **Smaller:** ch. 25 the Tarn's bank "was going well" in Seven's heat, then missing from the five that
  held: credit the step in one clause. Ch. 28 18:00–18:45 evening is over-compressed: loosen the clock
  (a later hour for the closing strike, or fewer drills named) so what happens fits the time given,
  without cutting the scene. Ch. 26 "the Harbour Committee wrote to the Clerk" → "wrote to the Works"
  (the Clerk is the Clerk of the Measure). Ch. 28 Trewin's "flat hand on Sunday morning" is not shown in
  ch. 24; make it consistent (off-page is acceptable if stated).
- **Do not touch (record only):** Perrin lifting against Aske's card with no consequence on the page —
  carried to Movement Five; Penhale's ward left as frost (C18) — an owner note; Monday's "It was the
  neap" (accept or "near the neap"); Orla's "by sight for a fortnight" (C17); "Skerry Pill" and the
  Halden clerk's patent line (cold read H): it is the planned disclosure, leave it.

### 2. One-pass clarity at the teaching moments (one sentence each; no new scenes)

- **The Carry's clock (ch. 26 ~l.273; ch. 27 "a minute's start"):** remove the dead conditional ("If
  it's full sooner, a minute and twenty") and let Kiva and Jude say one number: "Half for a minute,
  then full. At full it reaches his face at a minute and twenty."
- **Carrow's unlaying (ch. 27 ~l.377):** "She was holding it with nothing open, because she was laid"
  contradicts itself on one pass. Say: she was holding it with nothing open. A laid girl cannot walk,
  and to lift and walk she had shut both doors.
- **Why the Tarn's stow does not fold (ch. 30 ~l.317):** Kiva's "Ours was cut short. Theirs isn't. It's
  still got a post to stand on." does not explain the difference. Either name what she saw ("Ours had a
  post cut short before the slack. It never stood true after.") or let her say she does not know ("I
  don't know. Ours folded. It should.").
- **The climax geometry (ch. 30 ~l.373–377 and the first two paragraphs of ch. 31; cold-read
  priority 1):** at the most important moment the sleeve swings "across the channel, to face the sea",
  yet comes down "on the mud on the west side of the channel". Give one fixed bearing for the far post
  ("on the west side of the bend"); replace "across the channel" with the arc the sleeve actually
  travels (from downstream to inland, over the west mud); mention the closed end once *before* it
  lands on Penhale. Word order and punctuation; add nothing to the scene's length. Keep the slack still
  holding ("the grass stood up straight"), Penhale going in "as a man goes to a gate he has opened every
  day of his life", and Kiva's unanswered "*Far edge*."
- **The Tarn's carry (ch. 27 ~l.311):** "Then he did a thing that made the whole quay go quiet. He bent
  and picked up the Purser by himself…" repeats Brask three runs earlier; the quiet belongs to the
  planting on every step two paragraphs later. Move the beat.
- **Ch. 25 "He asked her, in her hand" (~l.405):** make clear it is the Chair's hand.
- **The Clerk's rule block in ch. 25** is the movement's densest exposition. Keep it, add only the two
  clauses priority 1 requires, and break it, if natural, around the first heat so the reader gets a
  rule just before it matters.
- Leave the "Kiva:" chapter titles as they are; every non-Kiva section already opens on its lens by name.

### 3. Thin the catchphrases and the aftermath's shape (narration only; line edits)

- **Jude's "I'd want it said" (16: ch. 28 ×6, ch. 32 ×7, others):** cut to about two uses a chapter and
  save it for his weightiest lines. Keep the window speech ("I'd want it said that I've seen it come in
  now. Over somebody.", ch. 32 ~l.567) and the board line (~l.343). Recast the rest in the speaker's
  register (Jude diffident but plain; Kellan as a sum; Pettit direct; Pru short; Perrin his own "I'd
  like it known", which also appears as "I'd like that known" variants: keep Perrin's, vary others).
  Also "expect nothing else" (4): keep Kellan's.
- **Repeated images:** "frost on a window" (×3, ch. 30–31), "like a sack going into a loft" (ch. 26 and
  ch. 27, twice), "as though nodding were a thing that had to be done properly" (ch. 27 and ch. 32), "the
  way a referee holds up a hand" (ch. 25 and ch. 27), "the warm low sound" (×3), "before the water" (8):
  give each image one home and vary or cut the others.
- **Telegraphing in ch. 29 and restatement in ch. 31–32 (cold-read priority 2):** Penhale twice says he
  has never gone onto the mud (ch. 29 ~l.169 and ~l.341) plus "I'll not, likely": remove one, keep "my
  mother likes it" once and let Yeo echo it once in ch. 31. In ch. 32, the facts that the stow "turned
  before the water" are restated eight times across the movement (Yeo's slate, the Rhea/Yeo yard scene,
  Noa's ledger, Kiva to Ivey, Coombe's "I'll read it"): cut each restatement to what is **new**
  (the far edge is "when the thing decides", a sleeve has two ends, the book is written for a sheet); keep
  Noa's ledger entry as the single formal record. Cut only exact restatements of facts already on the
  page; preserve every new fact and every protected beat.
- **The aftermath's shape (ch. 32):** twelve sections, five under 650 words. Fold §6 (Dray, 316 words) and
  §7 (the *Mercury*, 294) into the board scene (§5) as one walk along the boards, removing two breaks and
  keeping every line.
- **Rhythm (narration only):** the short share rose to 46% (median 6); ch. 28 (median 5, 50.5% short)
  and ch. 32 (49.2%) trot. Join adjacent short narrated reactions where the thought is continuous
  ("Kiva did not answer." / "It's said." / "Nobody said anything."), chiefly in ch. 28 §0, §2, §5 and
  ch. 32 §1, §2, §11. Vary about a third of "slowly" (43). Do not add run-ons; leave dialogue alone.
  Waypoint (not a gate): narration short share nearer 38%. The formula (mean 14.6, median 11, ~27.7% at
  five or fewer, ~3.3% at forty or more) is unchanged.

## Strengths to protect

"Don't give them yours." / "That's why they'll want it."; the torn page caught "as if it had been a
rung"; "I want it in your voice, so I've got it twice"; "Is there anything in the rule about the
jacket?" / "If your cells run hot, that's your hold, not mine."; "I'm not on a ladder at all. I'm on
twenty-two little pieces of the earth"; "Say the price." / "I'm only the word."; the eleventh rung and
"You waited for my heel"; "It's not better… It's just the other side of the same thing."; "There are no
squares on a ladder."; Trewin's "It's horrible" / Pru's "It gets more usual. That's not the same.";
"What happens in the gap?"; *Far edge*, once, and the fold lying down where Kiva had been; "It's a
sleeve. It's got two ends. The book's for a sheet."; "Let it come to you… Be the nearest thing."; "He
stopped at three."; Yeo's "And mine. I said it was ground."; Pike's "He had nobody at his far edge.";
Coombe's still hands and the type set "like somebody counting"; Ivey's curlew; *Before. D. Penhale…*;
the night survey that closes ch. 32. **Do not shorten the climb (ch. 27 §0), the Skerry Pill fight
(ch. 30) or the pass (ch. 31 §0).** Keep the short call beats (*Set.* / *Nobody.* / *Fold.*). Retain
Kiva's voice, the crew's warmth, character agency and the death's weight.

## Boundaries

- No change to any event, outcome, date, ash total, power limit, injury, knowledge boundary or reserved
  disclosure. The printed boards, the standings (Halden 65, Old Four 64, Ropewalk first 58, Seven 53,
  Holloway second 54; Seven ninth, one mark off eighth), the ash book (4.16 → 3.85 → 3.50 → 3.11 → 6.26),
  Penhale's death, Lyle's lost ward, the pass holding, Carrow learning to declare, the disk cold, the dream
  private, "Unroofed Sky" and "Breach" unused all stay.
- No new chapter, scene, revelation, named person, power or subplot. No wholesale rewrite.
- Do not modify plans or canon to excuse prose errors. Owner-protected wording stays exact.
- **Owner items — not for you to decide; record any you touched or left:** whether sentence targets govern
  dialogue (64% short); the progression-vocabulary trend (29 per 10k, below the book average); Perrin's
  lift against Aske's card (carry to Movement Five); the frost-shape of Penhale's ward; the Movement Three
  open items (41-minute hold; brown-ink line; "my best machine").

## Deliverables

1. Repair the working files `manuscript/chapter-25.md` through `chapter-32.md`, in reading order.
2. Write `provenance/MOVEMENT-004-REPAIR.md`: runtime-reported model and session/job identifier (say
   plainly if unverifiable); each factual correction with its evidence (for the Bench, show the full
   re-ranking check); what was clarified, joined, folded and recast, by chapter and section; the breaks
   removed; before/after `wc -w` per chapter and for the movement; before/after metrics from the script
   (all text, narration, sections, breaks per 10k); counts before and after for "I'd want it said",
   "I'd like it known", "slowly", "before the water", "frost on a window"; every requested item left
   unchanged, with the reason; confirmation that the frozen edition was not modified
   (`shasum -a 256 -c SHA256SUMS.txt`).
3. Reconcile `provenance/MOVEMENT-004-CONTINUITY.md` and the Movement Four block of `STATE_LEDGER.md` to
   the surviving prose where a repair changed what they state (Bench heat times and places, the rail
   minute, Seven's thimble, the clocks, Penhale's quote source). Add a repair entry to `AUTHORSHIP.md`.
   Do not claim recheck, acceptance, publication, or any Movement Five work.

When finished, stop. Do not commit, push, publish, or draft forward.
