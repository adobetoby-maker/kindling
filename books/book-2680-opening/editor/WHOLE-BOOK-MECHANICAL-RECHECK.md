# Kindling 2680 Book One — final mechanical record recheck

> Built by TAC

Date: 2026-10-12. Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), review-only, no subagents.
This is the same session that wrote `editor/WHOLE-BOOK-TARGETED-RECHECK.md`; it did not make
the fixes checked here.

Read: `editor/WHOLE-BOOK-TARGETED-RECHECK.md` (its owed list) and the current
`provenance/MOVEMENT-005-CONTINUITY.md` at every changed hunk, with a search of the whole file
for every month label.

## The two owed fixes

**1. Calendar note, lines 81–82 — correct.**

- Before: "the month of Classification Day and the Pit is the **fifth**, the month of the
  Weighbridge the **sixth**…"
- Now: "Classification Day is in the **fourth** month and the Pit is in the **fifth**, the
  month of the Weighbridge the **sixth**, then the **seventh**, **eighth** and **ninth**."

This matches the manuscript's day chain (Classification Day on Wednesday the 3rd; the Pit on
the 29th of the following month, which chapters 38 and 39 call the fifth) and the "fourth
month" now spoken in chapters 44 and 47.

**2. Section 9, item 1, lines 628–630 — correct.**

- Before: a request that a reviewer check "that nothing in chapters 1–32 contradicts spring as
  the fifth month."
- Now: "**Resolved in the whole-book reconciliation:** Classification Day is in the fourth
  month, the Pit is in the fifth, and chapters 1–32 contain no numbered month that contradicts
  the day chain."

That is true: the only numbered month in chapters 1 to 32 is "the ninth month" for Mara's
re-sit (chapter 17), which agrees.

## Complete, and no new contradiction

- The checkpoint now agrees with itself. Its other month labels are all consistent with the
  corrected note: the panel quenched "the 13th of the fourth month" (line 271), the Pit and
  Perrin's last lift on "the 29th of the fifth month" (lines 50 and 309), Vane's entry of "the
  30th of the fifth month" (line 478), and the sixth to ninth months in the calendar table.
- No line in the file still places Classification Day in the fifth month.
- Against `HEAD`, the checkpoint differs in exactly three hunks: these two fixes and the
  hall-panel date already passed in the targeted recheck. Nothing else in it changed.
- The other records are byte-identical to their state at the targeted recheck:
  `STATE_LEDGER.md`, the Movement One, Two, Three, Four and Six checkpoints, and
  `editor/WHOLE-BOOK-REPAIR-REPORT.md` all carry the same hashes. `AUTHORSHIP.md` still shows
  82 added lines and none removed.

One consequence to know about, not a fault: the repair report and the authorship entry record
the Movement Five checkpoint's hash as `13b42349…`. After these two fixes it is `28411648…`.
Both documents describe the file as it stood when they were written, and the authorship entry
already says the calendar note was left for a later fix, so neither is made false.

## No manuscript file changed after the targeted recheck

- Chapters 8, 24, 44, 47 and 48 carry the same SHA-256 values recorded in the targeted recheck
  and the repair report (`94b38e29…`, `07bab974…`, `71c3c9fa…`, `457397c2…`,
  `a9258326…`).
- The other 44 manuscript files are byte-identical to the frozen edition.
- The book is still 305,131 words.
- All 49 frozen files verify against `SHA256SUMS.txt`, and nothing under `editions/` is
  modified.

## Not done

No file other than this report was written. No prose, record, authorship, planning or frozen
file was edited. Nothing was scored, drafted, committed, pushed, published or narrated.

OVERALL: PASS — Book One reconciliation is complete
