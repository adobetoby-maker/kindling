# Movement Six — one bounded second repair (same author)

The fresh-context recheck (`provenance/MOVEMENT-006-RECHECK.md`, job `22f7111d`) accepted every repaired finding except four bounded line fixes and two optional ones.
Make exactly these edits and nothing else. The showrunner authorises R1 (the Tanyard edit): the brief's own "since the gate" wording was the imprecise part; this is not
owner-authored text.

1. **R1** `manuscript/chapter-47.md` ~l.299 (the Tanyard, Pike on the tailboard): "since the gate" → "since the dressings came off". Correct the matching record lines:
   `STATE_LEDGER.md` (Movement Six block, the Pike line and its "(ch. 24)" citation → "(ch. 19; ch. 24)") and `provenance/MOVEMENT-006-CONTINUITY.md` (the matching line).
2. **R2** `manuscript/chapter-41.md` ~l.239 (Yeo's plan): "The thing goes in past her, and down the dock floor…" now follows "The Master waits back on the outer quay…". Make the order true
   with one clause (for example "The thing goes in past where she'll stand, and down the dock floor…", or "By then the thing's gone in, down the dock floor, and it's planted forty-five
   paces in…"). Change nothing else in that paragraph.
3. **R3** `manuscript/chapter-43.md` ~l.305: "four feet eleven inches of it, to their chins" must agree with ~l.273 ("level with her eyes") and ~l.261 (Anwen "looking up at it"):
   "four feet eleven inches of it, level with their eyes".
4. **R4** `manuscript/chapter-47.md` ~l.153: "…each pump on its own cells, and kept there." → "…each pump on its own cells, and each to be kept there." Wording only.
5. **Optional, do them if they are one clause:** O1 `manuscript/chapter-48.md` ~l.227 "lamps lit against the grey, slate blue." → "lamps lit against the grey. It was slate blue." (or put "slate blue" back
   next to "The van"); O2 `manuscript/chapter-44.md` ~l.471 "Anwen's line stood shut on the granite" → "Anwen's line stood shut on the sill's edge".

Leave 43:121 ("seventy paces off on the basin wall") and 46:273 ("She had not known about the sister's book, or Kellan's sheet", which conflicts with 45:315–319) untouched: both go to the whole-book review.

Then run a quote-parity scan of chapters 41–48 (zero odd paragraphs), append a short "Second repair" section to `provenance/MOVEMENT-006-REPAIR.md` (what changed; the runtime-reported model and
job/session id; that the frozen edition `editions/movement-006-first-draft/` still verifies with `shasum -a 256 -c SHA256SUMS.txt`; `wc -w` of the changed chapters; the new hashes of chapters
41, 43, 44, 47, 48) and add one sentence to the `AUTHORSHIP.md` Movement Six repair entry naming the second repair. Do not touch any other prose or record, claim acceptance or publication,
commit or push. When finished, stop.
