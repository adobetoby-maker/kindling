# Kindling 2680, Book Two — Movement Two consolidated repair

You are Claude Opus 5.5, returning as the prose author for *The National Measure*, public
byline Monroe Jackson, internal seat Monroe Jackson 1.3.0 / O'Connor 1.3.0. This is one bounded
same-author repair of the completed second movement (Chapters 9–16). Do not draft Chapter 17.
Do not redesign the movement. Do not launch subagents or other models; you repair and report
yourself. Read all eight chapters and both review reports before editing.

## Required evidence, in this order

1. `books/book-2680-national-measure/provenance/MOVEMENT-002-EDITORIAL-REVIEW.md` (informed,
   same-family review; Section 3 canon table, Section 4 numbers, Section 5 brief)
2. `books/book-2680-national-measure/provenance/MOVEMENT-002-COLD-READ.md` (manuscript-only
   simulated read; same model family; not human feedback)
3. `books/book-2680-national-measure/provenance/MOVEMENT-002-CONTINUITY.md`
4. `books/book-2680-national-measure/STATE_LEDGER.md`, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`
5. `books/book-2680-national-measure/manuscript/chapter-09.md` through `chapter-16.md`,
   completely and in order

The exact first draft is frozen, read-only, under
`books/book-2680-national-measure/editions/movement-002-first-draft/` with `SHA256SUMS.txt`.
Never edit it. Edit only the working files `manuscript/chapter-09.md` to `chapter-16.md` and
the records named under Deliverables. Chapters 1–8 are accepted and closed: do not touch them
unless a located contradiction forces a one-line fix, and record any such touch.

The measuring script is `provenance/tools/m2_metrics.py`
(`python3 -I provenance/tools/m2_metrics.py manuscript`). Use it for before/after numbers.
It is a heuristic, not a gate.

## Three repair priorities (the whole job)

### 1. Restore factual trust: continuity and physical-state line fixes

Smallest edit that solves each. A word or phrase each; no restructuring; no new events. Verify
every edit against the scene and `STATE_LEDGER.md`. Located defects (line numbers are first-draft
numbers; find by text):

- **The comb (ch. 16).** Both reviews place the first silent seventh reed at the ash office on the
  Tuesday and again, as "the first time since the thaw", at the Order on the Friday. Make the
  first full silence happen once and say so once. Also correct Pru's explanation: the seventh is
  silent in genuine plain ash because the Step is the beat the stock never heard; dilution with
  soot shows on the thin third reed (the text already has the third reed sing thin). Keep the
  spoon-on-glass sound-image and the emotional weight of the first true silent seventh.
- **Pru's sheet (ch. 15 §4 and the ch. 16 ledger).** The frosted cloth on the race lip, whose
  sheet it was, and the "her own sheet / her own cloth" throws, contradict each other and the
  line that Mrs. Pryce's grey double was left at the hut. Make who threw which cloth, and what is
  lost, agree across ch. 15 and the ch. 16 replacement line. Keep Pru refusing to leave her sheet
  behind.
- **Talley and cords (ch. 15 ~l.519).** Four cuts at the mill and kiln versus Jude's stated count;
  four bags tied versus "three cords". Make the spoken tallies equal what the scenes show.
- **The countdown (ch. 16).** The book's rule is 44 minus the date: 43 on the 1st, 30 on the 14th,
  16 on the 28th. The 25th is nineteen and the 26th eighteen. Fix both lines; keep the closing
  "Sixteen" on the 28th and "Nobody had told him to count it".
- **Intervals.** "three days ago" for the kiln becomes the true interval (Friday the 20th to
  Thursday the 26th); the tram sheds "a week ago" in ch. 15 (the 6th to the 19th); ch. 14
  "Two days, three by the time we're there" (the tear Saturday, the team's arrival Thursday).
- **Referents and wording.** ch. 16 Mara: "a girl who had lost two fingers on a hill" must not
  imply amputation (the fingers report pressure; the feeling is what is lost). ch. 12: "the two men
  on the far side, who were only Hesketh … and Kellan" (Hesketh is a woman). ch. 9 "Jude's
  colleague's boot" is garbled (Aske's colleague tended Jude's boot). ch. 14 Jude's aside
  "And Sunday's, which I've not read out." lacks its opening quotation mark and leaves an unpaired
  one.
- **Time and place.** ch. 13 says Kiva heard Perrin's who-hauls plan at "a kitchen table on
  Thursday night"; it was said on the shed step to Coombe on the morning of Thursday the 5th
  (ch. 11 opening). Correct to what the scenes show.
- **Smaller notes to resolve only if one clear word does it:** ch. 11 "the hill again, in the
  ninth month" against the ledger's second three-door (check Book One facts in the ledger before
  touching); ch. 15 "since the second month of the autumn" (numbered-month world: use a
  numbered month or a plain phrase); the physical note that Coombe predicts Jude will "limp till
  Thursday" and he limps on the 19th (let one clause acknowledge it).

Preserve the ledger arithmetic, which both reviews verified to the hundredth: 9.64 → 6.23, the
four crossings, the 59.2 hunt, the bound 2.0. Do not change any total.

### 2. One-pass clarity and narration shape

**Rules and vocabulary (cold read, priority 2).**
- "Ward" must stop meaning both a person-held ward and a still door's ground. In ch. 13 (floor
  scene; Anwen's "put a ward under my heels") and ch. 11 (plank), use the established terms
  precisely: a plank is two like doors, a stack/lay is unlike doors; name the unlike pair where
  ch. 13 calls a ground ward a plank. Change single words and short clauses, not scenes.
- Turn the one "since" chain in ch. 10 (the skin/slope logic, ~l.193) into two short sentences so
  uphill/downhill reads on one pass. Recast the other located causal "since" where a listener
  would hear time (about 100 uses across the movement; fix the ambiguous ones, not all).
- Plant the rung rule ("falls away from the edge that cut it", ch. 14 ~l.247) as one earlier line.
- Give Coombe one line in ch. 11 or 13 saying why a licence floor with a lodger is a different
  thing from a demonstration, so setting a lodger on Kiva's floor five days after refusing it
  reads as her decision. Do not add a scene.
- The ch. 13 open thread (a sanctioned tape would read Perrin's stance and Anwen's still door as
  one line; did the mast read it?): answer in one clause if the scene allows, otherwise leave
  and record.

**Point of view.** The chapter titles all begin "Kiva:". Four sections are written from another
lens (ch. 10 §4 Anwen; ch. 12 §0 Kellan; ch. 14 §1 Orla; ch. 16 §3 Mara). Do not change chapter
headings, add scenes, or add a lens. Anchor each in its first sentence by name and a physical
or mental cue only that person has, so a reader knows whose knowledge is on the page. Keep the
Kellan opening of ch. 12, which both reviews rank among the strongest pages.

**Narration sentence shape (editorial priority 2).** Measured: median 6 against the formula's
11; 46% at five words or fewer against 27.7%; narration at 8% of sentences of forty or more
against 3.3%, with a 96-word and a 90-word sentence in ch. 16, and chains of 83–90 words in
ch. 10 §0 and ch. 11 §0, §5, §6. The prose is bimodal: short beats plus a long run-on tail,
with too few middle-length sentences. Make a narration-only pass:
- Split sentences over about 60 words into two clear mid-length sentences, starting with
  ch. 16 §4 (the road) and §8 (the ferry), ch. 11 §0/§5/§6, ch. 10 §0, ch. 15 §6 approach.
- Join runs of three or more consecutive short declaratives in quiet, reflective or
  transitional narration where they carry one thought.
- Do not add long sentences. Do not create run-ons. No breathing commas between subject and verb.
- **Leave dialogue alone** (owner decision pending on whether sentence targets govern speech).
- Do not touch the fight rhythm of ch. 13 §2–4 or ch. 15 §4, scene-closing short beats
  ("It sang." / "It's not plain."), or the moor's long breath where it carries landscape.
- Editorial waypoint, not a gate and not a replacement target: narration median 8–9, short
  share nearer 38%, narration long share 3–4%. The formula (mean 14.6, median 11, ~27.7% at five
  or fewer, ~3.3% at forty or more) is unchanged. Do not chase the number.

### 3. Thin the repeated rituals and readouts

Line-level cuts and substitutions only; nothing a scene needs is removed.
- **"tied a knot"** (21–23 uses, ch. 9–13): keep about a third, at Coombe's entrances and
  verdicts, and keep enough that the rope left on the step in ch. 13 still pays off. Vary or cut
  the rest.
- **"I'd like it known"** (11 in this movement, 19 with Movement One): return to Perrin alone;
  other speakers get their own idiom. Do not add it elsewhere.
- Other mannerisms: "something moved at the corner of her mouth" (give each person a different
  tell or cut), "thirty years" used for both Coombe and Vane (give Vane another marker),
  "slowly" (39 uses), "scratched his jaw" (10), "pale eyes" (8).
- **Van-slate repetition.** Open the ch. 14 van scene partway through the routine instead of
  re-running the template already run in ch. 11.
- **Ledger and share readouts.** Reduce ch. 16 §1 (Jude's full-month reading, ~230 words of
  restated figures) to the opening and closing totals plus the two lines that are new (the sheet;
  room left for tomorrow). Keep Vane's weighing in ch. 15 §7 as the real moment; cut Mara's
  earlier share explanation (ch. 14 §7) to one sentence ("If it's quiet, it's a hand."). In
  ch. 11 §6 move the Chair's incident sentence after Noa's "one line" so each thing arrives once.

## Strengths to protect

"a sum that has been done honestly and comes out short"; "I was a clock"; Coombe's
fail–drill–pressure structure; the lodger in the seam; the tap that never comes; "Shut your
eyes"; *Nobody!* on the floor and Perrin shutting without asking; Kiva on the skin; Pike at the
tailboard and the *Cost* line; the mill wheel stopped under Perrin's name; the kiln that sings;
Thrale's room where the doors lie down; "I kept my mouth shut. I'd learned how."; Jude's
"I've never been so sorry not to spend anything"; the Kellan opening of ch. 12; the Orla cutaway.
Retain Kiva's voice, the crew's warmth, character agency, and every developed action scene at
its full length. Do not shorten the Pit pack, the lane, the Flask floor, the mill or the kiln.

## Boundaries

- No change to any event, outcome, date, ash total, power limit, injury, knowledge boundary or
  reserved disclosure. The hand-to-Ember count stays four; the bound 2.0 stays bound; the dream's
  "not so high" detail stays unexplained; "Unroofed Sky" stays unused; the disk stays cold.
- No new chapter, scene, revelation, named person, power or subplot. No wholesale rewrite.
- Do not modify plans, maps or canon to excuse prose errors.
- Owner-protected wording (see the owner/canon protections recorded in the ledger and bible) stays
  exact. If a repair would touch it, leave it and record why.
- Items for the owner, not for you to decide: whether sentence targets govern dialogue; the
  front-load progression arithmetic; the plan's six-crossing calendar (prose is right); the Order's
  binding of the plain ash; the lodger extended to two people's unlike doors; viewpoint share for
  later movements. Record any you touched or deliberately left.

## Deliverables

1. Repair the working files `manuscript/chapter-09.md` through `chapter-16.md`, in reading order.
2. Write `provenance/MOVEMENT-002-REPAIR.md`: runtime-reported model and session/job identifier
   (state plainly if unverifiable); each factual correction with its evidence; what was
   clarified, thinned and reshaped, by chapter and section; before/after `wc -w` per chapter and
   for the movement; before/after sentence measures from the script (all text and narration);
   counts of "tied a knot", "I'd like it known" and "since" before and after; every requested
   item left unchanged, with the reason; confirmation that the frozen edition was not modified
   (re-verify `SHA256SUMS.txt`).
3. Reconcile `provenance/MOVEMENT-002-CONTINUITY.md` and the Movement Two block of
   `STATE_LEDGER.md` to the surviving prose where a repair changed what they state (comb, sheets,
   tallies, dates). Add the repair entry to `AUTHORSHIP.md`. Do not claim recheck, acceptance,
   publication or completion of Movement Three.

When finished, stop. Do not commit, push, publish, or draft forward.
