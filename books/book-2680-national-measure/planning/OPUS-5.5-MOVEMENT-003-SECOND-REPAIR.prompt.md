# Movement Three — one bounded second repair (same author)

The fresh-context recheck (`provenance/MOVEMENT-003-RECHECK.md`, job `a495af2f`) accepted every
repaired finding except one located defect (D1). Make exactly this one edit and nothing else.

1. `manuscript/chapter-23.md` line 195: the repair removed the `---` break before the Proprietor's
   introduction, and the line "He was not what she had expected." now directly follows a sentence
   about Perrin ("Perrin cleared his throat and took the rope off his shoulder."), so "He" reads as
   Perrin. Change that sentence to "The Proprietor was not what she had expected." Change nothing else.

Then append a short "Second repair" section to `provenance/MOVEMENT-003-REPAIR.md` (what changed;
the runtime-reported model and job/session id; that the frozen edition `editions/movement-003-first-draft/`
still verifies with `shasum -a 256 -c SHA256SUMS.txt`; `wc -w` of chapter 23) and add one sentence to
the `AUTHORSHIP.md` Movement Three repair entry naming the second repair. Do not touch any other prose
or record, claim acceptance or publication, commit or push. When finished, stop.
