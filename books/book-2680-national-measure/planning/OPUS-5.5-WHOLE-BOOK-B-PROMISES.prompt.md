# Whole-book review B-PROMISES

You are a fresh-context reviewer of the complete novel *The National Measure* (Kindling 2680, Book Two, chapters 1-48,
about 326,000 words, by Claude Opus 5.5 using the Monroe Jackson 1.3 / O'Connor seat). You are a same-model-family simulated reviewer:
state that plainly, and never describe your read as human reader feedback or independent testing. Do not launch subagents or other
models; no Skill tool is available. Do not edit any manuscript chapter, ledger, map or canon file; you write exactly one report file.
Every movement (chapters 1-8, 9-16, 17-24, 25-32, 33-40, 41-48) has already had an informed editorial review, a simulated cold read, a
same-author repair and a fresh recheck, so your job is the WHOLE-BOOK layer only: defects that cross movements or that no movement-sized
review could see. Do not re-litigate style, do not chase formula scores, and do not propose rewrites. Report concrete, located defects
(chapter:line, a short quoted phrase, the problem, the evidence for it, and the smallest edit that fixes it) and list what you checked and
found consistent. Mark each finding BLOCKING (a reader or listener would be misled), CONTRADICTION (two passages disagree), or CLARITY
(one pass is unclear). Separate defects of the prose from plan differences (BOOK_MAP/packets) and from owner decisions. Never treat
protected owner wording or an accepted closed chapter as editable without a located reason. Line numbers are from `grep -n` on the
working files in `books/book-2680-national-measure/manuscript/` at the start of your run. Recent accepted audio-clarity edits to
chapters 8, 9, 11, 14, 15, 19, 24 are in the files; do not flag them as unexplained (see `provenance/AUDIO-*-REPAIR.md`).

## Your layer: promises and payoffs, relationships, progression, reserved boundaries, the ending, threads

Read in full first: `books/book-2680-national-measure/BOOK_MAP.md` (especially §3 Complete ending, §7 ladder, §9 relationships, §10 action promises, §11
evidence ladder, §12 plant and payoff ledger, §13 reserved), `OWNER_BRIEF.md`, `SERIES_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md` (§7-9),
`STATE_LEDGER.md` (final blocks), and `provenance/MOVEMENT-006-CONTINUITY.md`. Then verify against the prose with targeted `grep` and reading of located
passages (read chapters 1, 2, 47 and 48 in full; read every other passage you cite). Check:

1. **Plant and payoff table (BOOK_MAP §12), row by row:** is each plant on the page, is each payoff on the page, in the right movement, and does the payoff
   pay what the plant promised? List unpaid, mispaid, or paid-twice rows. Also list threads the book opens and never closes (named objects, people, offers, lines
   of dialogue that promise a later scene), and payoffs that arrive without a plant.
2. **Relationship arcs (BOOK_MAP §9):** for each pair, one line on where the arc starts, the turning scenes (chapter references) and where it ends; flag any arc
   that stalls, reverses without cause, or is told rather than shown.
3. **Kiva's ladder (§7) and the action promises (§10):** is each rung earned on the page with its cost; are the ten promised action/learning set pieces all
   present and developed; does any capability appear at the climax without an earlier price?
4. **Evidence ladder for the filter and the dream (§11):** does the evidence accumulate fairly movement by movement; does anything explain what is reserved?
5. **Reserved items (§13 and OWNER_BRIEF):** grep and read for any spent reserved truth (the filter's full loss; pure Glory presence; the cause of the Fall; the disk's
   origin; the colour with no word; Annick's fate; returning figures; a doctrine that obsoletes the schools; international resolution; the word "Breach"; Kiva's
   classification). The one deliberate exception to confirm: "the unroofed sky" is first named at the Board's finding in chapter 40.
6. **Repeated shapes and power inflation:** do the movements' set pieces repeat one shape; do stakes inflate without a new idea; do secondary characters arc evenly
   (no one takes the secondary story); is any person a villain; is a Glory master's limit visible each time.
7. **The ending against BOOK_MAP §3:** every promise there, and whether the ending is satisfying and complete without becoming a bridge novel.

Write one report: `books/book-2680-national-measure/provenance/WHOLE-BOOK-PROMISES-REVIEW.md` containing: who and how (model, job id, what you read and did not read);
the plant/payoff table with a verdict per row; the relationship table; findings (ID, severity, location, quoted text, problem, evidence, smallest fix, and note when
the fix is one clause or one line); owner decisions; and your honest limits. Do not commit, push, repair, or draft.
