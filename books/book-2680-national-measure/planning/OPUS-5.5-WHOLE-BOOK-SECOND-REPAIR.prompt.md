# Whole book — one bounded second repair (same author)

The fresh-context recheck (`provenance/WHOLE-BOOK-RECHECK.md`, job `59421479`) accepted the whole-book repair except four located items (its §7–§8). Make exactly these edits and nothing else. The showrunner authorises D3
(it is outside P4's stated scope but follows the decision already made: the book gives one figure for the age of the Proprietor's reading, seventy-six).

1. **D1** `manuscript/chapter-33.md` ~l.71: cut the sentence "Thirty-six hands would be on thirty-six glass cases." so the paragraph reads "…the basin would go still for twenty minutes. Somewhere in it, if anybody asked her, she would be
   calling…" (check that "it" still refers to the still basin). Update the matching ch. 33 line in `MOVEMENT-005-CONTINUITY.md` and the ledger if either records the sentence.
2. **D2** `manuscript/chapter-42.md` ~l.207: "She did not go red, because she never did." → "She did not go red."
3. **D3** `manuscript/chapter-39.md` ~l.189: "I've been sure of it for seventy-seven years." → "I've been sure of it for seventy-six years." Leave 39:145 and 39:251 (they count from the window). Extend the `BOOK_MAP.md` P4 note (if it exists) to name the three lines
   now at seventy-six (39:189, 47:183, 47:233).
4. **D4** `provenance/MOVEMENT-006-CONTINUITY.md` ~l.121, 143, 147: "Sedge" → "Shapter". Add one dated line to `provenance/WHOLE-BOOK-REPAIR.md` correcting its §4.2 refrain figures to 4 → 2 if the recheck's note is right (check first).

Then run a quote-parity scan of chapters 33, 39 and 42, append a short "Second repair" section to `provenance/WHOLE-BOOK-REPAIR.md` (what changed; your runtime-reported model and job or session id; that the frozen edition
`editions/whole-book-pre-repair/` still verifies; `wc -w` and new hashes of chapters 33, 39 and 42), and add one sentence to the whole-book repair entry in `AUTHORSHIP.md`. Touch nothing else. Do not claim acceptance or
publication, commit or push. When finished, stop.
