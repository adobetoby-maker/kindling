# Whole-book review C-SEAMS

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

## Your layer: seams, scene clarity, openings and endings, repeated habits, read-aloud

Read in full first: `books/book-2680-national-measure/provenance/WHOLE-BOOK-REPETITION-DATA.md` (measured repetition across all 48 chapters), `OWNER_BRIEF.md`, and
`provenance/MOVEMENT-00{2,3,4,5,6}-RECHECK-CONFIRMATION.md` (limitations carried forward). Then read: (a) the first 80 and last 60 lines of every one of the 48 chapters; (b) every movement
join in full (the last 150 lines of chapters 8, 16, 24, 32, 40 and the first 150 lines of chapters 9, 17, 25, 33, 41); (c) chapters 1, 20, 31 and 46 in full for scene clarity and
read-aloud; (d) any passage you cite. If narration review files exist (`narration/monroe-1.2.5/calder/*/chapter-*/writing-monroe-feedback.md`), read the ones for the chapters in (a)-(c)
as a record of what a listener-preparer flagged; they are the audio session's, not yours to edit. Check:

1. **Seams:** does each movement open so that a reader who has just finished the last chapter is oriented in the first page (who, where, when, what is at stake) without a
   recap lecture; does each movement end on a turn and a pressure; any repeated, missing or contradictory handoff.
2. **Chapter openings and endings across the book:** repeated opening formulas (a ritual, a card, a clock, a weather line) and repeated closing formulas (a last survey,
   a stated lesson, a quiet image, a one-line hook): which recur often enough to be heard as a habit, with chapter numbers.
3. **Whole-book habits from the data:** which measured repetitions (the "did not say anything" / "did not look at" families, "on the table", "I'd not", "slowly", "the far edge",
   "nobody", sentence-initial patterns, similes, the same 4-word phrases) cross the threshold where a listener would hear them; propose a bounded list of line-level edits (no more
   than 60 across the whole book, ranked by read-aloud cost) that vary or cut the worst instances without touching protected strengths (the call words *Set. / Nobody. / Far edge.*,
   the ledgers' exact figures, the scene-ending short beats).
4. **Scene clarity:** in the full chapters you read, any passage where a listener cannot tell who is speaking, where people are standing, what time it is, or what rule is in
   play; the "Kiva:" chapter titles over non-Kiva sections (anchored in each section's first sentence: confirm they are).
5. **Terminology:** door vocabulary (plank, stack, lay, ward, hand door, still door), "the Hold/hold", "crossing", "the far edge", "a lodger", and any term used two ways.

Write one report: `books/book-2680-national-measure/provenance/WHOLE-BOOK-SEAMS-REVIEW.md` containing: who and how (model, job id, what you read and did not read; you did NOT read the
whole book, and say so); findings (ID, severity, location, quoted text, problem, smallest fix); the ranked bounded edit list with exact before/after wording for each (so an author can
apply it in one pass); owner decisions; and your honest limits. Do not commit, push, repair, or draft.
