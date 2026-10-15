# Kindling 2680, Book Two — Movement Four targeted recheck

Act as a fresh-context targeted verifier for *The National Measure*, Movement Four
(Chapters 25–32). This is not a second editorial pass, not a cold read, and not permission to
edit prose. You are a different session from the drafting and repair sessions: do not launch
subagents or other models. Read:

- `books/book-2680-national-measure/provenance/MOVEMENT-004-EDITORIAL-REVIEW.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-004-COLD-READ.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-004-REPAIR.md`
- the frozen originals in `books/book-2680-national-measure/editions/movement-004-first-draft/`
- the repaired working files `books/book-2680-national-measure/manuscript/chapter-25.md` through
  `chapter-32.md`
- `STATE_LEDGER.md` (Movement Four block) and `provenance/MOVEMENT-004-CONTINUITY.md` only where the
  repair report cites them or where a changed line touches them

Use direct file comparison (`diff`, or `git diff --no-index --word-diff`) of each frozen chapter against
its working chapter and inspect every changed passage. Recheck only the repaired findings and changed
joins:

1. **Factual corrections.** Verify every correction F1–F18 in repair report §1 against the frozen prose,
   the repaired prose, the scene's own arithmetic and the cited evidence. In particular, re-derive the
   **Bench ranking yourself from the page**: the marking rule as the Clerk now states it; every on-page
   heat time and step time for every named and unnamed four; the printed Bench board; the after-two and
   after-three sheets (Halden 65, Old Four 64, Holloway first 59, Ropewalk first 58, Twenty-Eight 57,
   Westerley first 56, Westerley second 55, Holloway second 54, Seven 53); and that Seven is ninth, one
   mark off the roll of eight. Check the rail minute is planted before it is used; the water's direction
   at the ladder and the tail; Aske's position; when and where Kiva hears of Skerry Pill and where the
   bags are combed; Penhale's "I'll read it" in both chapters; Yeo's and Kellan's distances and clocks;
   Perrin's rehearsal climb and the ash book (4.16 → 3.85 → 3.50 → 3.11 → 6.26, with every spoken total);
   the Clerk's Hunt rule and Yeo's order; the Tuesday-evening clock in ch. 28 including the yes/no hour of
   a quarter to seven. Confirm no date, event, injury, power limit, knowledge boundary, outcome or printed
   board moved.
2. **Clarity edits.** Verify the Carry's clock (one number, said once, consistent between ch. 26 and
   ch. 27), Carrow's unlaying, why the Tarn's stow does not fold, the climax geometry at Mallow Creek
   (a fixed bearing, the sleeve's arc, the closed end mentioned before it lands on Penhale; is the staging
   now followable in one reading?), the moved Tarn-carry beat, the Chair's hand, and the Clerk's rule
   block. Flag only a concrete loss, contradiction, awkward seam, unclear referent or meaning change.
3. **Catchphrases and the aftermath.** Inspect every recast "I'd want it said" (the window speech and the
   board line must survive), the varied images, the removed telegraphing in ch. 29, the de-duplicated
   restatements in ch. 31–32 (nothing new was cut; Noa's ledger entry is the single formal record), the
   folded ch. 32 sections (the repair says no line was lost), and every join of short narrated reactions.
   Confirm each recast line sounds like its speaker, that protected beats survive (*Far edge*, once; "He
   stopped at three."; "It's a sleeve. It's got two ends. The book's for a sheet."; Yeo's "And mine. I said
   it was ground."; the night survey that closes ch. 32), and that no gesture is left dangling. Spot-check
   that dialogue was not reshaped for length.
4. **Frozen edition and records.** Run `cd books/book-2680-national-measure/editions/movement-004-first-draft
   && shasum -a 256 -c SHA256SUMS.txt` and report the result. Run
   `python3 -I books/book-2680-national-measure/provenance/tools/m4_metrics.py
   books/book-2680-national-measure/manuscript` and compare to repair report §3 as a spot check (not a
   formula gate). Confirm that the repair's notes in `MOVEMENT-004-CONTINUITY.md`, the Movement Four block
   of `STATE_LEDGER.md` and the `AUTHORSHIP.md` repair entry match the surviving prose and claim no
   recheck, acceptance or publication. List any stale line.

Write `books/book-2680-national-measure/provenance/MOVEMENT-004-RECHECK.md` with: your runtime-reported
model and session/job identifier (say plainly that you cannot verify it independently, and that this is a
same-family fresh-context check, not human review); a PASS/FAIL for each of the three repair priorities
with the evidence checked; exact locations (file and line, plus quoted text) for any surviving or newly
introduced defect; the checksum result; and an overall decision: either "accepted for Movement Five
context" or "one concrete defect requiring a second repair" (list each defect as a located, bounded fix).
Do not re-open unrelated style questions. Do not score the book. Do not edit any file other than that
report, update authorship, commit, push, publish, or draft forward.
