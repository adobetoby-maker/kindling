# Kindling 2680, Book Two — whole-book consolidated repair (located defects only)

You are Claude Opus 5.5, returning as the prose author for *The National Measure* (chapters 1–48, about 326,000 words), public byline Monroe Jackson, seat Monroe Jackson 1.3.0 /
O'Connor 1.3.0. Every movement has already been reviewed, repaired and rechecked. Three fresh-context whole-book reviews (same model family; simulated; not human feedback) then found
defects that cross movements. This is one bounded same-author repair of those **located** defects. It is not a polish pass and not a rewrite: do not chase style, formula scores or
anything not listed. Do not launch subagents or other models; no Skill tool is available. You may edit accepted, closed chapters **only** at a located finding below, with the smallest
edit that fixes it. Never touch the last section of chapter 48 (from the ninth *no answer* to *The disk is cold.*), the call words (*Set. / Nobody. / Far edge.*), the ledgers' exact figures
and card wording ("Then we look again, and either of us may say no."; "Not for a bank, a floor, a crossing or a sale."), or any scene-ending beat the reviews name as a strength.

## Required evidence, in this order

1. `books/book-2680-national-measure/provenance/WHOLE-BOOK-CONTINUITY-REVIEW.md` (findings W1–W18; record defects §3; plan differences §2)
2. `books/book-2680-national-measure/provenance/WHOLE-BOOK-PROMISES-REVIEW.md` (findings P1–P6; owner decisions §11)
3. `books/book-2680-national-measure/provenance/WHOLE-BOOK-SEAMS-REVIEW.md` (findings WB-01–WB-22 with exact fixes F01–F19; the ranked edit list R01–R50; owner decisions §9)
4. `books/book-2680-national-measure/provenance/WHOLE-BOOK-REPETITION-DATA.md`, `STATE_LEDGER.md`, `BOOK_MAP.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`
5. Every chapter passage you edit, plus enough surrounding scene to judge the edit. Book One (`books/book-2680-opening/`, manuscript and ledger) is the authority where a Book One lock is at issue.

The whole book is frozen, read-only, at `books/book-2680-national-measure/editions/whole-book-pre-repair/` (`SHA256SUMS.txt`). Never edit it. Edit only `manuscript/chapter-NN.md` and the records
named under Deliverables. Line numbers in the reviews are from the working files before the last bounded Movement Six edits and the audio-clarity edits settled; **find every passage by its quoted text**,
and where a reviewer's "before" string no longer occurs exactly once, locate the sentence by sense and say so in your report. The audio-clarity edits to chapters 8, 9, 11, 14, 15, 19, 24 are accepted (see
`provenance/AUDIO-*-REPAIR.md`); do not undo them.

## What to do

### A. Prose defects to fix (each a located phrase, number or sentence)

Apply, with the reviewers' suggested fix unless you judge another wording smaller or better (record what you did):

- **Continuity review:** W1 (the sealed page records the **Pit**: 21:263, 3:149, 16:353), W3, W5 (see decisions), W6 = WB-08, W7, W8, W9, W10, W12, W13, W14, W15, W17, W18, and W2, W4, W11, W16 under the decisions below.
- **Promises review:** P1 (see decisions), P2, P3 (see decisions), P4, P5. P6: leave.
- **Seams review:** WB-01 through WB-19 (apply fixes F01–F19, except where they duplicate a continuity or promises fix above: WB-06 = P1, WB-08 = W6; apply each once), WB-20 as decided below. WB-21 and WB-22 are handled by R01–R08.
- Where two reviews give different fixes for the same line, use the one that agrees with the surrounding scene and say which.

### B. The owner-level choices, decided by the showrunner (record them as decided; do not reopen)

- **W2 (Kellan's Hunt totals vs the Hunt board's rule).** Fix the figures, not the board. Restate the combed, red and clean figures at 36:29 and 36:193 (and the claims-ledger line "The Measure to date", and any later
  repetition in ch. 38 or 40; grep `371.3`, `412.4`, `41.1`) so the clean total is at least what the board's own rule implies and red stays about nine-tenths (the reviewer's example: combed 4,513.0; red 4,061.7; clean
  451.3; reconcile against the board yourself and keep Seven's 3.15 and "Nine Bags in Ten"). Correct the ledger M5.7 and `MOVEMENT-005-CONTINUITY` §3 lines.
- **W4 (Pettit and Yarrow).** Book One governs. Read the Book One passages the review cites. Choose the smaller edit that leaves Book One untouched (for example roles or doors in the 12:111 entry and the 44:285 line); if
  honouring Book One would need more than about eight changed lines across chapters 6, 12 and 41–44, do **not** change the chapters: record it as an unresolved owner item with the exact options.
- **W5 (Thrale's forty paces on Monday against the Graving).** Choose (b): edit 40:167 and 40:229 so Kiva's doors lie down as Thrale passes the bench and get up as she walks on to the gate, and give the fever's hold a
  cause that does not need a new rule (or soften with "as if"). Do not add a new rule at ch. 41.
- **W11 (the yes/no hour).** 42:359 "every morning" → "every day". At 41:3 add one clause: from this Monday she takes the quarter to seven in the morning (Sunday's had been Pru's, written for her). Record the hour once in the ledger.
- **W16 (the name Sedge).** Rename Twenty-Eight's Hold at all thirteen places (37:143; 41:125, 301, 307, 311; 42; 43; 44). Choose a short, unvoiced name that appears nowhere in either book's manuscript, planning or provenance files or in
  `universe/` (check by search first) and that is not an aural collision with an existing name; record it.
- **P1 / WB-06.** "Mrs. Yeo told me on Saturday" → "Mrs. Yeo told me on Wednesday night" (Yeo was at the board on Wednesday night, 35:50; she came to tell the mother first).
- **P3 (the Barrel's weight).** Choose option (a): raise the one figure at 46:125 above the Flask scale the book teaches at 2:71 and below a Well (read 2:47 and 2:71; the cadence "…and four-tenths" may stay: "Six hundred and eighty-six drams and
  four-tenths" is acceptable), and carry it to `STATE_LEDGER.md` M6.3 and `MOVEMENT-006-CONTINUITY.md` §8. No share depends on it. Do not change ch. 2.
- **P4.** "seventy-seven" → "seventy-six" at 47:183 and 47:233; leave 47:225 ("waited seventy-seven years to see the lamps do it again", counted from the window).
- **WB-20 / OD-5.** Choose (a): add one clause at the first Movement Six use of *plank* widening it to "like doors on one load"; and at 41:319 "a tun with a plank nailed under it" → "a board" (F19).
- **R-list owner decisions:** OD-1 resolved **yes, vary**: apply R01, R06, R07 **and** R08 (keep the town-count refrain whole once, at ch. 24; vary the ends of 32 and 40 without losing their turns). OD-2 keep (Aske opening nine chapters). OD-3 no
  action; the book's last line stays. OD-4 apply R02–R05. OD-6, OD-7, OD-8, OD-9: no action.

### C. The habit edits (seams review §5.2, R01–R50)

Apply R01–R22 (identical text at movement ends and in the fever echo; same-page silence clusters; identical tag sentences). Then apply R23–R50 **only where** the edit removes an audible repetition without touching a protected strength or a speaker's
distinctive voice; skip and record any you decline, with the reason. Keep "nearly smiled" Pike's (R34–R36), and apply R50 (Anwen's use of Jude's tag). Where a reviewer's "after" wording does not read as the author would write it, write your own smaller fix and say so.

### D. Records

Reconcile `STATE_LEDGER.md` (every movement block a change touches), the six `provenance/MOVEMENT-00N-CONTINUITY.md` files, `BOOK_MAP.md` if a plan line is now wrong, and `CHARACTERS.md` if a descriptor changed (Pike's face; Adlam's age; Lyle's face; the renamed Hold) to the surviving prose. Correct
the record defects in the continuity review §3 (the Thrale jar count in `MOVEMENT-002-CONTINUITY`; Sedge "no collision"; Kellan's totals; Orla's "a season"; the yes/no hour; the numbering of the Slack's crossings as the eighth and ninth in Book Two). Do not edit the frozen editions.

## Boundaries

- No change to any event, outcome, date, ash total, power limit, injury, knowledge boundary or reserved disclosure beyond a located correction. The Measure's printed totals and Seven's seventh place, the crossings and cards, the tin, the sealed page's contents, the prediction, the Slack's course, the grid
  order, the commission, the four's choices, the hull and the disk stay. No new chapter, scene, revelation, named person (except the renamed Hold), power or subplot. Three doors remain three clean; "Breach" stays unused; the colour with no word stays Kiva's alone.
- Do not edit prose merely to improve it. If a finding cannot be fixed without a larger change than its review proposes, leave it and record it as an owner item.
- **Owner items to record, not decide:** the colour "brushed twice"; the certificate precedent; new interaction properties (reading a count through a still door; "one hold"; Thrale's ward holding water; no fever after two masters); the revised bible §6; Hollis Vane's absence; whether the sentence targets govern
  dialogue; the progression density; the Home Line roll turn dropped; the tide clock; the 41-minute hold; the brown-ink line; "my best machine"; Penhale's ward as frost; the Order's six questions left open; whether Book Two's last page should lean outward (the hull).

## Deliverables

1. Edit the working chapters at the located findings only.
2. Write `provenance/WHOLE-BOOK-REPAIR.md`: your runtime-reported model and session or job id (say plainly if unverifiable); a table of every finding ID (W1–W18, P1–P6, WB-01–WB-22, R01–R50) with its disposition (applied: chapter and before/after quoted; modified: what and why; declined or deferred: why); the decisions in §B as applied
   (including the new name of the Hold and the new Barrel figure); the list of chapters changed with before/after `wc -w` and SHA-256; counts before and after for the tic families you thinned ("did not say anything", "did not look at", "nearly smiled", "slowly", "pressed to his side", "for a long time/moment", the Clerk's tag lines);
   a quote-parity scan of all 48 chapters (an odd count of double quotes in a paragraph that does not open a multi-paragraph quotation) returning zero new odd paragraphs; the frozen-edition check (`cd editions/whole-book-pre-repair && shasum -a 256 -c SHA256SUMS.txt`); and a short list of anything you saw that needs an owner decision.
3. Reconcile the records in §D. Add a whole-book repair entry to `AUTHORSHIP.md`. Do not claim recheck, acceptance or publication.

When finished, stop. Do not commit, push, publish, or draft forward.
