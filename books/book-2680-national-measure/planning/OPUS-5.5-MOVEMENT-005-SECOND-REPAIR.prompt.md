# Movement Five — one bounded second repair (same author)

The fresh-context recheck (`provenance/MOVEMENT-005-RECHECK.md`, job `01a5e43b`) accepted every
repaired finding except two one-character prose defects (one class: a dropped reopening quotation mark where
a tag was inserted mid-speech) and three record lines. Make exactly these edits and nothing else.

1. `manuscript/chapter-36.md` ~line 207: insert the missing opening `"` before "I've sat at the Proprietor's table".
2. `manuscript/chapter-40.md` ~line 249: insert the missing opening `"` before "and I've known it since a bank on a hill".
3. Records: `provenance/MOVEMENT-005-CONTINUITY.md` ~line 358 "6–2" → "7–2"; ~line 269 "48,217 of 55,413" →
   "48,220 of 55,416"; ~line 267 Orla "1,573" → "1,563" (check each against the recheck report and the surviving files
   first; if the recheck's number is wrong, say so and use the right one).

Then run a quote-parity scan of chapters 33–40 (an odd count of straight double quotes in a paragraph, excluding
paragraphs that open or continue a multi-paragraph quotation) and confirm zero odd paragraphs. Append a short "Second
repair" section to `provenance/MOVEMENT-005-REPAIR.md` (what changed; the runtime-reported model and job/session id;
that the frozen edition `editions/movement-005-first-draft/` still verifies with `shasum -a 256 -c SHA256SUMS.txt`;
`wc -w` of chapters 36 and 40) and add one sentence to the `AUTHORSHIP.md` Movement Five repair entry naming the second
repair. Do not touch any other prose or record, claim acceptance or publication, commit or push. When finished, stop.
