# Kindling 2680, Book Two — whole-book targeted recheck

Act as a fresh-context targeted verifier for *The National Measure* (chapters 1–48). This is not a new review, not a cold read, and not permission to edit prose. You are a different session from the drafting, review and
repair sessions: do not launch subagents or other models; no Skill tool is available. A same-author repair has just applied located whole-book findings across 35 chapters. Read:

- `books/book-2680-national-measure/provenance/WHOLE-BOOK-REPAIR.md` (every disposition, the showrunner's decisions in §1, the W2 reconciliation in §3, owner items §5, records §6)
- `books/book-2680-national-measure/provenance/WHOLE-BOOK-CONTINUITY-REVIEW.md`, `WHOLE-BOOK-PROMISES-REVIEW.md`, `WHOLE-BOOK-SEAMS-REVIEW.md` (the findings and the exact fixes they proposed)
- the frozen pre-repair book `books/book-2680-national-measure/editions/whole-book-pre-repair/` (48 chapters, `SHA256SUMS.txt`) and the repaired working files `manuscript/chapter-01.md` through `chapter-48.md`
- `STATE_LEDGER.md`, `CHARACTERS.md` and the six `provenance/MOVEMENT-00N-CONTINUITY.md` files only where the repair report says it reconciled them

Use direct file comparison (`diff`, or `git diff --no-index --word-diff`) of every chapter against its frozen copy and inspect **every changed passage**. Then check:

1. **Nothing unlisted changed.** Every changed paragraph must trace to a disposition in the repair report (a finding ID W/P/WB/R, a decision in §1, or a record). Report any change that does not.
2. **Every applied fix solves its defect** without breaking its scene: the sealed page's contents (W1: the Pit in all three places, morning not afternoon); Kellan's Hunt figures against the Hunt board's marking rule and the "nine-tenths" claim (W2: re-derive the board's implied clean total from the printed
   places and shares; confirm 466.0 clean is at least what it implies, that Seven's 3.15 and 12.6 still hold, and that nothing else quotes the old figures); Orla and the eighth-month crossing (W3); Thrale's doors in the Graving against the Monday plan (W5); the ferry-transit day (W6); Dray's sticks (W7); the soot-cut jar count (W8);
   "ten days" (W9); who said the eight-tenths line (W10); the yes/no hour in every place (W11: 41:3, 41:7, 42:359, 47:49 and the ledger); the thirteenth-month knowledge slip (W12); the right-hand writing (W13); a winter, not a year (W14); Lyle's face (W15); **the rename of Twenty-Eight's Hold to Shapter at every place, with no stray old name left in Book Two
   and no collision with any other name in either book** (grep both manuscripts); a fortnight for Coombe (W17); Coombe's new rope (W18); Wednesday night (P1); "no counsel twice" (P2); the Barrel's weight 686.4 against 2:47 and 2:71 and the records (P3); seventy-six (P4); Birch (P5); the weeks-and-days line (WB-17); Pike's face, Adlam's age,
   Rhea's eleven years, Anwen's blush, Jude's writing hand and the other WB fixes. Confirm the deferred W4 (Pettit and Yarrow) is genuinely unchanged and recorded as an owner item.
3. **The habit edits (R01–R50)** removed repetition without removing protected strengths: the call words (*Set. / Nobody. / Far edge.*), the ledgers' exact figures, card wording, "nearly smiled" being Pike's, the town-count refrain whole once at the end of chapter 24, and every scene-ending beat. Every cut or merged paragraph must leave
   a grammatical join with clear referents and no orphaned speech tag; check the joins at each cut. Chapter 48's last section (from the ninth *no answer* to *The disk is cold.*) must be byte-identical to the frozen copy.
4. **No new defect introduced:** quote parity across all 48 chapters (an odd count of double quotes in a paragraph that does not open a multi-paragraph quotation; report new odd paragraphs against the frozen copy), real month names (none), the word "Breach" (none), dates and weekdays touched by the edits, counts and sums touched by the edits.
5. **Records and checks.** Run `cd books/book-2680-national-measure/editions/whole-book-pre-repair && shasum -a 256 -c SHA256SUMS.txt` and report it. Confirm the repair's record reconciliations (ledger, continuity files, CHARACTERS, BOOK_MAP, AUTHORSHIP) match the surviving prose and claim no recheck, acceptance or publication. List any stale line.

Write `books/book-2680-national-measure/provenance/WHOLE-BOOK-RECHECK.md` with: your runtime-reported model and session or job identifier (say plainly that you cannot verify it independently, and that this is a same-family fresh-context check, not human review); a PASS/FAIL per area above with the evidence checked; exact locations
(file and line, plus quoted text) for any surviving or newly introduced defect; the checksum result; and an overall decision: either "accepted: the book is ready for final publication" or "defects requiring a bounded second repair" (list each as a located, minimal fix). Do not re-open style questions. Do not edit any file other than that report,
update authorship, commit, push, publish, or draft forward.
