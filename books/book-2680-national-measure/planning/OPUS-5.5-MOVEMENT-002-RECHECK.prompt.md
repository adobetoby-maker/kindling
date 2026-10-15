# Kindling 2680, Book Two — Movement Two targeted recheck

Act as a fresh-context targeted verifier for *The National Measure*, Movement Two
(Chapters 9–16). This is not a second editorial pass, not a cold read, and not
permission to edit prose. You are a different session from the drafting and repair
sessions: do not launch subagents or other models. Read:

- `books/book-2680-national-measure/provenance/MOVEMENT-002-EDITORIAL-REVIEW.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-002-COLD-READ.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-002-REPAIR.md`
- the frozen originals in `books/book-2680-national-measure/editions/movement-002-first-draft/`
- the repaired working files `books/book-2680-national-measure/manuscript/chapter-09.md`
  through `chapter-16.md`
- `STATE_LEDGER.md` and `provenance/MOVEMENT-002-CONTINUITY.md` only where the repair
  report cites them or where a changed line touches them

Use direct file comparison: `diff` each frozen chapter against the working chapter and
inspect every changed line (about 210 lines in total). Recheck only the repaired findings
and changed joins:

1. **Factual corrections.** Verify every correction F1–F17 in repair report §2 against
   the frozen prose, the repaired prose, the scene's own arithmetic and the cited ledger
   evidence. Specifically confirm: the comb now has exactly one "first" full silence of
   the seventh reed (at the Order) and Pru's explanation attributes dilution to the
   thin third reed; the sheet, cloth and bag chain in ch. 15 §4–§6 and the ch. 16
   replacement line agree; Jude's cut and cord tallies equal what the scenes show; the
   countdown (44 minus the date) is right everywhere it is spoken or chalked (1st: 43,
   14th: 30, 25th: 19, 26th: 18, 28th: 16); every interval phrase ("six days ago", "a
   fortnight ago", "five by the time we're there") is arithmetically right. Confirm the
   ash ledger still reconciles to the hundredth (9.64 → 6.23; four crossings 0.31, 0.30,
   0.31, 0.30; 59.2 clean with the 7.40 share; sealed 2.0) and that no date, event,
   injury, power limit, knowledge boundary or outcome moved. Check that F13 (Pit, not
   hill) is consistent with the ledger and the Book One facts it cites.
2. **Clarity edits.** Verify the "Pit hands" replacement, the plank/unlike-door
   wording in ch. 13, Anwen's "her still door", the ch. 10 slope chain recast, the planted
   rung rule and its payoff in ch. 14, Coombe's added lodger line, the recast causal
   "since" instances, the ch. 11 §6 re-ordering of Noa's reading, and the four
   point-of-view anchors. Flag only a concrete loss, contradiction, awkward seam,
   unclear referent or meaning change. Does the added Coombe line contradict any earlier
   statement about why she kept a lodger off Kiva?
3. **Every changed line.** Inspect every narration join and split the repair made.
   Confirm grammar, referents, punctuation, read-aloud hierarchy, and preservation of
   meaning. Look in particular at the ch. 14 van opener (does the slate scene still sit
   inside the van?), the ch. 14 §7 and ch. 16 §1 reductions (does anything now read as
   missing, or does a later line refer to cut material — see F16), the knot, "I'd like it
   known", "slowly", "scratched his jaw" and "pale eyes" thinning (is Coombe's rope still
   paid off in ch. 13? did a cut leave a dangling gesture?), and any dialogue changes.
   Do not demand movement-wide formula compliance from this bounded pass; report the
   repair's before/after sentence figures only as a spot check (run
   `python3 -I books/book-2680-national-measure/provenance/tools/m2_metrics.py
   books/book-2680-national-measure/manuscript` and compare to repair report §5).
4. **Frozen edition and records.** Run `cd books/book-2680-national-measure/editions/movement-002-first-draft
   && shasum -a 256 -c SHA256SUMS.txt` and report the result. Confirm that the repair's
   notes in `MOVEMENT-002-CONTINUITY.md`, the Movement Two block of `STATE_LEDGER.md` and
   the `AUTHORSHIP.md` Movement Two repair entry match the surviving prose and claim no
   recheck, acceptance or publication. List any stale line.

Write `books/book-2680-national-measure/provenance/MOVEMENT-002-RECHECK.md` with: your
runtime-reported model and session/job identifier (say plainly that you cannot verify it
independently, and that this is a same-family fresh-context check, not human review); a
PASS/FAIL for each of the three repair priorities with the evidence checked; exact
locations (file and line, plus quoted text) for any surviving or newly introduced
defect; the checksum result; and an overall decision: either "accepted for Movement
Three context" or "one concrete defect requiring a second repair" (list the defect(s),
each as a located, bounded fix). Do not re-open unrelated style questions. Do not score
the book. Do not edit any file other than that report, update authorship, commit, push,
publish, or draft forward.
