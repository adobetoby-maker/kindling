# Kindling 2680, Book Two — Movement Three targeted recheck

Act as a fresh-context targeted verifier for *The National Measure*, Movement Three
(Chapters 17–24). This is not a second editorial pass, not a cold read, and not permission to
edit prose. You are a different session from the drafting and repair sessions: do not launch
subagents or other models. Read:

- `books/book-2680-national-measure/provenance/MOVEMENT-003-EDITORIAL-REVIEW.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-003-COLD-READ.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-003-REPAIR.md`
- the frozen originals in `books/book-2680-national-measure/editions/movement-003-first-draft/`
- the repaired working files `books/book-2680-national-measure/manuscript/chapter-17.md` through
  `chapter-24.md`
- `STATE_LEDGER.md` (Movement Three block) and `provenance/MOVEMENT-003-CONTINUITY.md` only where
  the repair report cites them or where a changed line touches them

Use direct file comparison (`diff`, or `git diff --no-index --word-diff`) of each frozen chapter
against its working chapter and inspect every changed passage. Recheck only the repaired findings
and changed joins:

1. **Factual corrections.** Verify every correction F1–F20 in repair report §1 against the frozen
   prose, the repaired prose, the scene's own arithmetic and the cited evidence. In particular:
   lane 2 now totals 6–4 by its carries and agrees with the seeding board ("twelve for, sixteen
   against"); lane 1's rule about the catcher and the poles is one rule that fits carries 1 and 3;
   Lyle's "yesterday" and what Anwen is shown doing; "three nights to go" on the Friday and "one
   night to go" on the Sunday; seven bags with the seventh light, everywhere it is stated; the
   Hoop's Tuesday times and minutes; the order of Thursday's events in ch. 22; whether Seven stands
   at Monday's Bench, consistently in both ch. 24 lines; Hart's line about Mara; the interval and
   place slips; Mara's logistics line; and the countdown. Confirm the ash book still reconciles to
   the hundredth (6.23 → 4.16, with the page's 4.70 and 4.28 waypoints), that the fifth crossing is
   Thursday the 3rd and the sixth Thursday the 10th, and that no date, event, injury, power limit,
   knowledge boundary or outcome moved. Confirm C20 (a lodger can be killed) against ch. 13.
2. **Scene structure and sentence work.** The repair removed intra-scene `---` breaks (list in
   repair report §2). For every join confirm the seam is clean: no cut prose, no orphaned
   transition, no change of place, time or lens hidden by the join, every non-Kiva section still
   opens on its lens by name, and no removed break sits before or after a cutaway. Check the new
   long sentences (about eight) for hierarchy, grammar and read-aloud breath, and every join of short
   declaratives. Check the ch. 17 rule-history beats, the "hand door" clarifying clauses and the
   "Hold" role/reading mark. Flag only concrete loss, contradiction, awkward seam, unclear referent
   or meaning change.
3. **Voices and tics.** Inspect every recast "I'd want …", "said nothing / did not say anything",
   scarlet/red, "in two stages", causal "since" and the three reflective negation recasts. Confirm
   each recast line sounds like its speaker and keeps its meaning; that Perrin's "I'd like it known"
   (7), Aske's "soonest", Pike's "nearly smiled" and Pru's scarlet survive; and that the cuts left
   no dangling gesture or unattributed line. Spot-check that dialogue was not reshaped for length.
4. **Frozen edition and records.** Run `cd books/book-2680-national-measure/editions/movement-003-first-draft
   && shasum -a 256 -c SHA256SUMS.txt` and report the result. Run
   `python3 -I books/book-2680-national-measure/provenance/tools/m3_metrics.py
   books/book-2680-national-measure/manuscript` and compare it to repair report §3 as a spot check
   (not a formula gate). Confirm that the repair's notes in `MOVEMENT-003-CONTINUITY.md`, the
   Movement Three block of `STATE_LEDGER.md`, `BOOK_MAP.md` §12 and the `AUTHORSHIP.md` repair entry
   match the surviving prose and claim no recheck, acceptance or publication. List any stale line.

Write `books/book-2680-national-measure/provenance/MOVEMENT-003-RECHECK.md` with: your
runtime-reported model and session/job identifier (say plainly that you cannot verify it
independently, and that this is a same-family fresh-context check, not human review); a PASS/FAIL
for each of the three repair priorities with the evidence checked; exact locations (file and line,
plus quoted text) for any surviving or newly introduced defect; the checksum result; and an overall
decision: either "accepted for Movement Four context" or "one concrete defect requiring a second
repair" (list each defect as a located, bounded fix). Do not re-open unrelated style questions. Do
not score the book. Do not edit any file other than that report, update authorship, commit, push,
publish, or draft forward.
