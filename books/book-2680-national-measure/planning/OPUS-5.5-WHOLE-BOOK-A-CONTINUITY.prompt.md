# Whole-book review A-CONTINUITY

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

## Your layer: chronology, calendar, ash book, crossings, injuries, power limits, knowledge, facts

Read in full first: `books/book-2680-national-measure/STATE_LEDGER.md` (all six movement blocks), `provenance/MOVEMENT-001-CONTINUITY.md`
through `MOVEMENT-006-CONTINUITY.md`, `BOOK_MAP.md`, `OWNER_BRIEF.md`, `UNIVERSE_BIBLE.md`, `CHARACTERS.md`. Then verify against the prose with
targeted `grep` and reading of the located passages (and read every movement join in full: the last 100 lines of chapters 8, 16, 24, 32, 40 and
the first 100 lines of chapters 9, 17, 25, 33, 41). Book One's locked facts are in `books/book-2680-opening/` (manuscript and ledger): use them only
to check locks. Check, with arithmetic where numbers are involved:

1. **Calendar.** Every dated or weekday-named event from Monday the 17th of the tenth month 2680 to Thursday the 1st of the fourth month 2681,
   against the ledger's calendar (numbered months; no real month names; the first month of 2681 begins on a Friday; the third month begins on a
   Tuesday). The shed-door countdown, "days since", "a fortnight ago", "last Thursday" and every interval phrase you can find by grep.
2. **The team's ash book** from entry (25.53) through the warrant, every floor, crossing, hunt, lane, share and purchase, to the end; every on-page
   running total ("Held, ...") against the continuity ledgers; the sealed medical tin (0.8 → 2.0 → used 1.2 → 0.8 left); the Order's jars (44 → 41 → 40 →
   36 given → 4 left); the Slack's yield and shares. Report any figure that disagrees between chapters or with its ledger.
3. **Crossings.** Every crossing in the book (Ember to still; hand to Ember; the Slack's two): date, door, cost, how far the cold reached, the sulk in
   nights, Aske's card each time. Spacing at least seven days except the Slack's second (priced aloud); certification; the "one in fourteen" card at
   the end. Three clean three-door sequences only; no fourth.
4. **Injuries and bodies by person over time:** Kiva (left reading hand and the two impaired fingers, thumbs counted as fingers; right-hand burns; knee),
   Perrin (ribs), Jude (shin, arm), Pru (fingertips), Pike (hands), Mara (hand), Hart (the ruined right hand), Dray (leg), Anwen, Kellan, Lyle (ward),
   Penhale (dead). Any person who heals too fast, never heals, or has the wrong side or count.
5. **Knowledge boundaries over time:** who knows that Kiva dreams, the white lights, the colour with no word, Hart's card, the plate, the sealed pages,
   the Order's binding; any character who knows something before the page that gives it to them.
6. **Facts that should not drift:** ages, titles and ranks, a person's door and role, place names and distances (the Sag, the ferry, Saltmere's geography,
   the Graving, the Counting House, the pump house), the cast's physical descriptors (grep eyes, hair, height, voice tells), the rank ladder, doors
   vocabulary (plank/stack/lay/ward/hand door), tide and slack figures (the Hoop's heights), names that collide.
7. **Book One locks** in `OWNER_BRIEF.md`.

Write one report: `books/book-2680-national-measure/provenance/WHOLE-BOOK-CONTINUITY-REVIEW.md` containing: who and how (model, job id, what you read and did not
read); a numbered findings table (ID, severity, location, quoted text, problem, evidence, smallest fix); a "checked and consistent" list per area above; items
that need owner decisions; and your honest limits. Do not commit, push, repair, or draft.
