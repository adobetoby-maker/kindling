# Kindling 2680, Book Two — Movement Six targeted recheck (the ending)

Act as a fresh-context targeted verifier for *The National Measure*, Movement Six (Chapters 41–48, the book's ending). This is not a second editorial
pass, not a cold read, and not permission to edit prose. You are a different session from the drafting and repair sessions: do not launch subagents or
other models; no Skill tool is available. Read:

- `books/book-2680-national-measure/provenance/MOVEMENT-006-EDITORIAL-REVIEW.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-006-COLD-READ.md`
- `books/book-2680-national-measure/provenance/MOVEMENT-006-REPAIR.md`
- the frozen originals in `books/book-2680-national-measure/editions/movement-006-first-draft/`
- the repaired working files `books/book-2680-national-measure/manuscript/chapter-41.md` through `chapter-48.md`
- `STATE_LEDGER.md` (Movement Six block) and `provenance/MOVEMENT-006-CONTINUITY.md` only where the repair report cites them or a changed line touches them

Use direct file comparison (`diff`, or `git diff --no-index --word-diff`) of each frozen chapter against its working chapter and inspect every changed
passage. Recheck only the repaired findings and changed joins:

1. **Factual corrections and the climax's rules.** Verify each correction in repair report §1–§2 against the frozen prose, the repaired prose, the scene's own
   arithmetic and the cited evidence. In particular re-derive from the page yourself: where the Master stands and when she comes down against her forty-pace rule
   and every still door opened at the sill; the cask's height wherever it is described (four feet eleven); the priced step and "She says she'll be late. She's
   saying it first."; Carrow's and Dray's bearing; the second plant (is it on tested granite; are Kiva's and Wace's positions picturable in one reading); the 24-minute
   deadline in both speeches; what Mara can hear from the landing; whether any section now steps outside Kiva's view; the cost of the first crossing (shown, not
   forecast and dropped); the clocks and counts (6.13/eleven minutes, Carrow's four minutes, the dock-floor run, a hundred paces, Lyle's six days, a fortnight in the shop, a
   year, a dozen masts, the comb at the gate, Pike's hands since the gate, the twelve days, Hart and the struck line, the first line of the limits, the plank of four, the daily
   hour, "sanctioned"), and Saturday's lane (Seven won 6–5). Confirm no event, outcome, time or cost changed, and that the tin (used 1.2, left 0.8, bound), Aske's card
   (one in fourteen days), the hand gone to the wrist for three weeks, the three clean doors, the cold disk, the hull and the grid order are as before.
2. **The coda.** Inspect each cut or shortened closing restatement (Pike, Anwen, Perrin, Jude, the narration and Kiva's book): the action and the image that ends each
   scene must survive; nothing the later scenes rely on may be lost. Inspect the recast "I'd want", the varied scarlet, the split summary chains, the broken long speeches, the
   compressed three-accounts paragraph and the eased heavy paragraphs. Confirm each recast line sounds like its speaker and that the protected lines survive word for word:
   the Tanyard (47 §8) apart from the three small edits the repair lists; the last section (48 §6) **word for word** from the ninth *no answer* to *The disk is cold.*; Aske's ten-count;
   Bannock's "It's water" / "Tomorrow it won't be"; Lyle's "I'm saying it before"; "It's one hold. Not two"; "Twenty-two"; the prediction read verbatim; *Used, 1.2. Left, sealed, 0.8. Bound as before.*
3. **Plan payoffs the repair added or left:** Carrow and Kiva each using a piece of the other's method; Peverell's seven columns; Hollis Vane's absence (an owner item).
4. **Frozen edition and records.** Run `cd books/book-2680-national-measure/editions/movement-006-first-draft && shasum -a 256 -c SHA256SUMS.txt` and report the result.
   Run `python3 -I books/book-2680-national-measure/provenance/tools/m6_metrics.py books/book-2680-national-measure/manuscript` and compare it to repair report §3 as a spot check (not a
   formula gate; the metrics script's viewpoint map is keyed to first-draft sections). Run a quote-parity scan of ch. 41–48 (an odd count of double quotes in a paragraph that does not open a
   multi-paragraph quotation) and report the count. Confirm the repair's notes in `MOVEMENT-006-CONTINUITY.md`, the Movement Six block of `STATE_LEDGER.md` and the `AUTHORSHIP.md` repair
   entry match the surviving prose and claim no recheck, acceptance or publication. List any stale line.

Write `books/book-2680-national-measure/provenance/MOVEMENT-006-RECHECK.md` with: your runtime-reported model and session/job identifier (say plainly that you cannot verify it independently,
and that this is a same-family fresh-context check, not human review); a PASS/FAIL for each of the repair priorities with the evidence checked; exact locations (file and line, plus quoted text) for
any surviving or newly introduced defect; the checksum result; and an overall decision: either "accepted for the whole-book review" or "defects requiring a second repair" (list each as a located,
bounded fix). Do not re-open unrelated style questions. Do not score the book. Do not edit any file other than that report, update authorship, commit, push, publish, or draft forward.
