# Kindling 2680, Book Two — Movement Five targeted recheck

Act as a fresh-context targeted verifier for *The National Measure*, Movement Five
(Chapters 33–40). This is not a second editorial pass, not a cold read, and not permission to
edit prose. You are a different session from the drafting and repair sessions: do not launch
subagents or other models. Read:

- `books/book-2680-national-measure/provenance/MOVEMENT-005-EDITORIAL-REVIEW.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-005-COLD-READ.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-005-REPAIR.md`
- the frozen originals in `books/book-2680-national-measure/editions/movement-005-first-draft/`
- the repaired working files `books/book-2680-national-measure/manuscript/chapter-33.md` through
  `chapter-40.md`
- `STATE_LEDGER.md` (Movement Five block) and `provenance/MOVEMENT-005-CONTINUITY.md` only where the
  repair report cites them or where a changed line touches them

Use direct file comparison (`diff`, or `git diff --no-index --word-diff`) of each frozen chapter against
its working chapter and inspect every changed passage. Recheck only the repaired findings and changed
joins:

1. **Factual corrections.** Verify each correction in repair report §1 against the frozen prose, the
   repaired prose, the scene's own arithmetic and the cited evidence. In particular re-derive **the Lane and
   the Measure from the page yourself**: Thursday's lane score under the book's rule (three over the hurdle,
   one for a down, two halves a down, a point at the glass), every place the 7–2 now touches (the marshal's
   call, the board, the points for and against, Kiva's reckoning, the Lane read in ch. 38), the nine fours at
   2–1 and their place marks, and that the printed Measure totals (82, 80, 79, 78, 77, 76, **Seven 69**, 68, 68,
   66, 59) and Seven's seventh place by one mark are unchanged and still add. Check the 1 p.m. sum now
   accounts for Old Four's 2 p.m. lane; the Proprietor's question and its source (nothing cites a paper for
   what only Seven heard); every list of Kiva's occasions includes the Pit and agrees with the page she asks
   the Board to open; "the one piece of the dream she had words for"; the weekdays and rows and clocks (the
   Tarn lane Thursday; the Westerley girl's row against Seven's ninth; "this morning" for Rhea's pinning; the
   draw by lot); Mara's reference to the page and her age; Dray's "fourteen" figure and anything that
   quotes the Slack's future cost; the smaller fixes (Aske's "your four", the two tins, twelve fitters vs
   thirty-six hands, the Proprietor's age, the closing survey). Confirm no date, event, injury, power limit,
   knowledge boundary or outcome moved beyond the located corrections, and the ash book (6.26 → 5.95 → 5.53 →
   5.15, with every spoken total) still adds.
2. **The Graving and the rules.** Verify the compressed evidence run in ch. 40 (Annick's line and Mara's page
   still read in full; the keepers summarised; the Proprietor's re-read reduced to its new line; the Holloway
   return lands once, as the peak, and is not read in full three times); that nothing the later scenes rely on
   was lost in compression. Verify the "no change" declaration now makes the third-carry choice real
   (stated cost or binding rule, consistent with Perrin's open mouth, Dray's waiting, Kiva's head-shake and
   "the fairest lane I've ever lost"), Friday's change from stance to Ember between carries, and the new
   moment of opposition at the opening of the Salt Hall. Flag only a concrete loss, contradiction, awkward
   seam, unclear referent or meaning change.
3. **Paragraph mass and idiom.** Inspect each broken long speech (the break is a gesture or interruption and no
   words are cut), the two split chains, the recast "I'd sooner", the cut "on the table" restatements, the
   dropped third "sent for", and the four causal "since" now "because". Confirm each recast line sounds like its
   speaker, protected beats survive (*After D. Penhale…*; "It's trying very hard… at sitting"; the two hands on
   the bone knife; "for want of a better"; Thrale's price; the Holloway reply; *Fever, the third. Nothing came.
   Said so.*), and that no gesture is left dangling. Spot-check that dialogue was not reshaped for length.
4. **Frozen edition and records.** Run `cd books/book-2680-national-measure/editions/movement-005-first-draft
   && shasum -a 256 -c SHA256SUMS.txt` and report the result. Run
   `python3 -I books/book-2680-national-measure/provenance/tools/m5_metrics.py
   books/book-2680-national-measure/manuscript` and compare to repair report §3 as a spot check (not a formula
   gate; note the metrics script's viewpoint map is keyed to first-draft sections). Confirm that the repair's
   notes in `MOVEMENT-005-CONTINUITY.md`, the Movement Five block of `STATE_LEDGER.md` and the `AUTHORSHIP.md`
   repair entry match the surviving prose and claim no recheck, acceptance or publication. List any stale line.

Write `books/book-2680-national-measure/provenance/MOVEMENT-005-RECHECK.md` with: your runtime-reported model and
session/job identifier (say plainly that you cannot verify it independently, and that this is a same-family
fresh-context check, not human review); a PASS/FAIL for each of the three repair priorities with the evidence
checked; exact locations (file and line, plus quoted text) for any surviving or newly introduced defect; the
checksum result; and an overall decision: either "accepted for Movement Six context" or "one concrete defect
requiring a second repair" (list each defect as a located, bounded fix). Do not re-open unrelated style
questions. Do not score the book. Do not edit any file other than that report, update authorship, commit, push,
publish, or draft forward.
