# Kindling 2680, Book Two — Movement Five consolidated repair

You are Claude Opus 5.5, returning as the prose author for *The National Measure*, public
byline Monroe Jackson, internal seat Monroe Jackson 1.3.0 / O'Connor 1.3.0. This is one bounded
same-author repair of the completed fifth movement (Chapters 33–40). Do not draft Chapter 41.
Do not redesign the movement. Do not launch subagents or other models; you repair and report
yourself. Read both review reports and all eight chapters before editing.

## Required evidence, in this order

1. `books/book-2680-national-measure/provenance/MOVEMENT-005-EDITORIAL-REVIEW.md` (informed,
   same-family; Section 3 arithmetic and findings C1–C15, Section 3c the hearing, Section 4
   numbers, Section 6 brief)
2. `books/book-2680-national-measure/provenance/MOVEMENT-005-COLD-READ.md` (manuscript-only
   simulated read, same model family, not human feedback; findings K1–K11 and its priorities)
3. `books/book-2680-national-measure/provenance/MOVEMENT-005-CONTINUITY.md`
4. `books/book-2680-national-measure/STATE_LEDGER.md` (Movement Five block), `UNIVERSE_BIBLE.md`,
   `BOOK_MAP.md`, `CHARACTERS.md`, `packets/MOVEMENT-005.md`
5. `books/book-2680-national-measure/manuscript/chapter-33.md` through `chapter-40.md`,
   completely and in order

The exact first draft is frozen, read-only, under
`books/book-2680-national-measure/editions/movement-005-first-draft/` with `SHA256SUMS.txt`.
Never edit it. Edit only the working files `manuscript/chapter-33.md` to `chapter-40.md` and the
records named under Deliverables. Chapters 1–32 are accepted and closed: do not touch them unless a
located contradiction forces a one-line fix, and record any such touch. (Another session recently
made eight word-level fixes in chapters 8–9, recorded in `provenance/AUDIO-CLARITY-08-09-REPAIR.md`;
do not undo them.) Line numbers in the reviews are first-draft numbers; find passages by their text.

Measuring script: `provenance/tools/m5_metrics.py`
(`python3 -I provenance/tools/m5_metrics.py manuscript`; its viewpoint map is keyed to first-draft
section numbers, so remap it in a scratch copy if you join or split sections and say so). Run it
before the first edit and after the last. It is a heuristic, not a gate.

## Three repair priorities (the whole job)

### 1. Make the sums and the evidence chain true (line edits; no scene changes)

The movement's case rests on two things: numbers that add and a page that cannot have been borrowed.
The counting readers will test both first.

- **Thursday's lane against the Tarn (ch. 33 ~l.403–439; ch. 38 ~l.145, 187; continuity §2).** In the
  third carry the Tarn still door is downed ("*Down.* The Tarn.") and then the litter goes over for
  three, yet the marshal's tally skips the down. By the book's own rule (three over the hurdle, one for
  a down, two halves a down) the lane is 7–2, printed as 6–2. **Preferred fix (a):** keep the down and
  make it 7–2 everywhere it is spoken or printed (the marshal's call, the points-for-and-against "seventeen
  for, twelve against", "Seven to two"), then keep the Lane places consistent: the reconciled eighth four
  moves to +6 so Seven stays ninth in lane points and the printed Measure totals, Seven's seventh place by
  one mark and every printed total in ch. 38 stand unchanged. (b) only if (a) cannot be made to add: make
  the Tarn still door's fall a half that does not kneel. Re-derive the whole bracket (the three Seven lanes,
  the nine fours at 2–1, the place marks, the final totals) after your fix and show it in the report.
- **The 1 p.m. sum (ch. 38 ~l.17–27).** Kiva's sum on the tiers forgets Old Four, who still had a 2 p.m.
  lane (a win makes them 3–0 and outright first). Put the conversation after Old Four's lane, or have Kiva
  add the condition ("…if Westerley beat Old Four at two"), and make Kellan's two fingers come after
  three.
- **The Proprietor's source (ch. 39 ~l.197 vs ch. 37 ~l.19, ch. 36 ~l.301–311, ch. 34 ~l.113).** "The
  *Mercury* says you were lower than before, and that the lights were nearer, and that some were going out"
  cites a paper for ferry details only Seven heard in a shut shop. Use the editorial's fix: he asks "The
  ferry. Below the Order's house. Last month. Were any of the lights white?" and Kiva volunteers *lower* and
  *nearer* in her answer, which she already does at ~l.217. Keep the white disclosure, her reasoning ("That
  was choosing a side by leaving a thing out of a column"), the hand over his eyes and "It doesn't prove me
  right" word for word.
- **Kiva's public list of occasions omits the Pit (ch. 34 ~l.107; ch. 36 ~l.307; ch. 39 ~l.217).** She lists
  "at thirteen… on Classification Day… and on the ferry", including to the Board, but the sealed page she
  asks the Board to open records the Pit on the 29th of the fifth month, 2680. Add the Pit to each list in one
  clause ("at thirteen… on Classification Day… in the Pit last spring, the night my aunt wrote it down… and on
  the ferry"; at ch. 39: "Not on Classification Day, not in the Pit, and not when I was thirteen"). Correct
  the ledger's account of occasions in the Records step.
- **"It was the one piece of the dream she had kept, even from the page" (ch. 39 ~l.207)** is falsified fifty
  lines later by a second kept piece. → "It was the one piece of the dream she had words for and had kept, even
  from the page."
- **Weekdays and clocks:** ch. 35 ~l.89 and ~l.265 "On Saturday, against the Tarn" (the Tarn lane was
  Thursday the 17th; the seeding lane on the 12th was a different Tarn four): fix to "Thursday" or add "a week
  ago" so the reference is the seeding lane. Ch. 38 ~l.171/173: Westerley "seventh row, behind Kiva" while Seven
  stands in the ninth row, and Dray is "two rows in front": put the sound in a row behind Seven (the tenth or
  lower) or change "behind" to "ahead", and make the rows agree. Ch. 38 ~l.287 Anwen: "Rhea Sorn pinned it at the
  baize at noon, after our lane" → "this morning". Ch. 37 ~l.3 "since the bag was opened" for a draw by lot →
  "since the clerk drew it".
- **Ages and sources:** ch. 39 ~l.301 Mara: "a girl of thirteen said with a wet cloth on her chest" does not
  match the page dated the 29th of the fifth month, 2680 (she was seventeen): make it agree.
  Ch. 37 ~l.321 Dray: "You'll be on one in fourteen by then, if your healer's right" quotes the Slack's
  future cost from nowhere: cut the figure ("You'll not spend it on a lane, this year or next") or attribute
  it to Aske's sulk arithmetic said earlier on the page.
- **Smaller, only if one word or clause does it:** ch. 33 ~l.149 Aske "That's your four" omits Anwen (say "your
  hurt four" or add her); ch. 40 ~l.185 Thrale: "a dram and two-tenths in her tin" vs the team's sealed
  "two drams" (make clear they are different tins or agree the figure); ch. 34 ~l.193 vs ch. 36 ~l.211 "twelve
  fitters" vs thirty-six hands (one clause: a training rota); ch. 39 the Proprietor "twenty-six" in 2604 vs "since
  I was twenty-seven" (let the reading form a year later); ch. 40 ~l.363 "nobody saw him" in the closing survey:
  accept, or anchor it in Kiva's thought.
- **Records, not prose:** the ledger and continuity say Mara "has not touched a cell"; she lays her reading hand
  on training cells twice: make it "a bank cell". Orla read the Ferren keeper's leaf "over your aunt's shoulder
  in the autumn" and the Saltmere entry through Kiva's book; add Orla to the ledger's knowledge rows.

### 2. Make the Graving a sequence that builds, and give the rules one line

- **Compress the restated evidence (ch. 40 §0, ~l.95–155; editorial P2, cold-read tradeoff).** In ch. 39–40 the
  dream's content is spoken by about eight voices; the Holloway return is read in full three times (ch. 34,
  ch. 36, ch. 40) and the Proprietor's evidence is re-read to a Graving that saw it five hours earlier.
  Compress, do not cut evidence: summarise the Ferren and Saltmere keepers' entries in one sentence each
  ("Peverell read her house's page herself, the long *s* and the white lamps, and sat down without a word");
  reduce the Proprietor's re-read to its one new line, Kiva's answer, and the Graving's reaction; keep
  Annick's line and Mara's page in full (the two documents the hearing exists to open); let the new Holloway
  return land as the peak of the evidence run (read it in full there; elsewhere refer to it in a clause).
- **The "no change" declaration (ch. 37 ~l.149 and the climax ~l.255–271; ch. 35 ~l.203–205; cold-read
  priority 2, editorial C6).** The marshal's "Then I'll hold you to it" makes the third-carry crossing look
  unavailable, so Perrin's open mouth and Dray's waiting for the count weaken Kiva's refusal. Add two to four
  sentences so the choice is real: either a stated cost for changing after declaring "no change" (a penalty
  point and a broken word to Dray) so that the crossing would have won the lane but cost a point and her word;
  or keep it binding and make the climax Kiva refusing to *break* the declaration when breaking it would win,
  with Perrin offering to take the penalty himself. Keep the three-carry lane at its full length, Pru calling
  the pen with Kiva silent, Kiva shaking her head, Perrin shutting his mouth, and Dray's "the fairest lane I've
  ever lost".
- **Friday's change from stance to Ember between carries (ch. 35 ~l.203–205):** add one line at the marshal's
  call that makes it a declared change with nothing open in the pause, on her card ("*A change between
  carries, declared to the box, with nothing open in the pause. It's on her card.*"), consistent with the
  Chair's conditions of the seventh month.
- **The opening of the Salt Hall (ch. 36 §1):** the first fifteen hundred words are a run of exhibits before
  anyone opposes anyone. Give one early moment of opposition or surprise (a line from counsel, the chairman, or
  Adlam) inside the existing material, without adding a scene.
- **Colour and Thrale (owner notes, do not decide):** the existence of Annick's unnamed colour is now public;
  Thrale's presence holding the fever down is a new interaction property. Leave both as written; if the
  fever line reads as asserted fact, soften only with "as if". Record both for the owner.

### 3. Paragraph mass and the new shared idiom (narration and speeches; line edits)

- **Long hearing speeches** over about 150 words (ch. 36 ~l.161, 183, 189; ch. 39 ~l.161; ch. 40 ~l.193, 241,
  251): break each once with a gesture, an interruption or a reaction from the room. No words cut.
- **The two long chains** that break the packet's 45-word rule (ch. 40 ~l.143 and ~l.295; ch. 35 ~l.19, 88
  words): split at the natural pause. Keep the long sentences of the imagined crossing (ch. 37 ~l.257) and the
  planted lean (ch. 35 ~l.263).
- **"I'd sooner" (13):** recast about half, keeping Perrin's "I'd sooner be hated" and "I'd sooner the low town
  were wet", and Thrale's "I'd sooner a house where nothing answers". **"On the table" (18):** cut two or three
  of the narration restatements; keep the Clerk's, Orla's and Rhea's. **"sent for" (third use, ch. 37 ~l.127):**
  drop. **Causal "since" (4, all in dialogue: Orla ch. 34 ~l.337, the Clerk ch. 38 ~l.143, the Proprietor ch.
  39 ~l.233, Mara ch. 40 ~l.241):** *because*. "that" is dense (113 per 10k): thin where it is padding.
- Give each person their own voice (Jude diffident, Anwen "I want it said", Perrin alone "I'd like it known",
  Pru scarlet, Aske's price speeches, Orla rough and brief, Hart plain and gauge-like, Mara dry, Kellan sums,
  Coombe drills, Dray flat). Leave dialogue length alone until the owner rules.

## Strengths to protect

*After D. Penhale, catcher… who went in by the book.*; "It's the week's crossing… If I spend it on a lane, I
can't have it back."; "I'd have given you a week more if you'd lied to me about it." / "That's why it's one
day."; "It's trying very hard… at sitting."; "Elbows… I've carried coal like that."; "She was not reading the
lane. She was being read for."; "It gets easier. That's not the same as better."; "A seal is not for keeping a
thing safe. It is for being opened in front of people."; Mara's "Mine." at the training cell; Hart: "It's let be
asked one thing. *Quiet,* or *not.*"; Kellan's "every dram but the dry tenth", 1,175.1, and "Well done, Renn";
Perrin: "It's two drams against a word."; "*Rowan, Ember, declared, single, by her captain's voice, and no
change.*"; Dray's face that "was not a door" and "the fairest lane I've ever lost"; "Not one mark of it was three
doors."; the Reader: "The guard asked whether it was a cat."; "I'd been keeping it from you. That's not the same
as keeping it."; the Holloway reply; "for want of a better"; the two hands on the bone knife; Mara's
fault-report voice; Noa's *N.B.*; Thrale's price and Peverell's pencil in her great-grandfather's book; the
third *Witnessed* line; *Put it on the table herself, under her own name, before anybody asked.*; *Fever, the
third. Nothing came. Said so.* **Do not shorten any lane, the Counting House scene, or the exchange with Dray.**
Keep the short calls (*Set.* / *Elbows.* / *Walk.*) and the closing survey's music.

## Boundaries

- No change to any event, outcome, date, ash total, power limit, injury, knowledge boundary or reserved
  disclosure beyond the located corrections. The final Measure (Ropewalk first four first, Halden second, **Seven
  seventh by one mark, on the roll, warranted for the Slack**), the printed totals in ch. 38, the crossing
  calendar (no crossing in the Lane week; the sixth was Thursday the 10th; next possible Thursday the 17th and
  kept), the sealed prediction unopened until noon on the 23rd, the disk cold, "Breach" unused, no Slack, no
  point of light, no hull all stay.
- No new chapter, scene, revelation, named person, power or subplot. No wholesale rewrite.
- Do not modify plans or canon to excuse prose errors. Owner-protected wording stays exact.
- **Owner items — not for you to decide; record any you touched or left:** whether the existence of Annick's
  unnamed colour may be public; Thrale holding the fever down as a new interaction property; whether sentence
  targets govern dialogue (59% short); the progression shape (about 1.4–1.5× front-loaded against the
  whole-book 58); section rhythm (5.6 breaks per 10k, below 8.7: accepted for hearings and lanes); the open
  Movement Three and Four items (41-minute hold, brown-ink line, "my best machine"; Penhale's ward as frost).

## Deliverables

1. Repair the working files `manuscript/chapter-33.md` through `chapter-40.md`, in reading order.
2. Write `provenance/MOVEMENT-005-REPAIR.md`: runtime-reported model and session/job identifier (say plainly if
   unverifiable); each factual correction with its evidence (for the Lane, show the full re-derived bracket and
   places); what was compressed, clarified, broken and recast, by chapter and section; before/after `wc -w` per
   chapter and for the movement; before/after metrics from the script (all text, narration, paragraph median
   and share over 60 words, breaks per 10k); counts before and after for "I'd sooner", "on the table", "sent
   for", causal "since", "I'd like it known", "I'd want it said"; every requested item left unchanged, with the
   reason; confirmation that the frozen edition was not modified (`shasum -a 256 -c SHA256SUMS.txt`).
3. Reconcile `provenance/MOVEMENT-005-CONTINUITY.md` and the Movement Five block of `STATE_LEDGER.md` to the
   surviving prose where a repair changed what they state (the Lane score and bracket, the Proprietor's source,
   the occasions list, Mara's "bank cell", Orla's knowledge). Add a repair entry to `AUTHORSHIP.md`. Do not claim
   recheck, acceptance, publication, or any Movement Six work.

When finished, stop. Do not commit, push, publish, or draft forward.
