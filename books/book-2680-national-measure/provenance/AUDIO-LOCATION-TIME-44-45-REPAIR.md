# Location/time repair: Noa's desk (chapter 44) and the 6:35 gate (chapter 45)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime; not verifiable from inside the session), authenticated Max CLI |
| Session | `https://claude.ai/code/session_01UbzPdqAwZMjqZuoa3bJznY` (background job `083ca522`) |
| Date | 2026-10-15, about 17:05–17:10 MDT |
| Instruction | Owner: "Verify the two located location/time findings; reject with evidence if not real, otherwise smallest repair. Freeze and report." The owner authorised this bounded loop, in which the same author answers findings that the narration pass sent back. |
| Findings answered | `narration/monroe-1.2.5/calder/chapters-43-45/chapter-44/writing-monroe-feedback.md` (SHA-256 `208f76551f7185e593886a1f21956e1b9d2924413ec01eb0dbc0313b6b762682`), BLOCKED at 44:217 (prose para 106). `…/chapter-45/writing-monroe-feedback.md` (SHA-256 `1435d5e06ac5ea356a1346df78189c553b57e8d351f2515f66762dd2555aab43`), BLOCKED at 45:343 (prose para 166). Unit summary: `narration/DIRECT-UNIT-43-45.result.md` (`bdf9e2f2…`). |
| Read before editing | Chapters 43, 44 and 45 in full; both feedback files; the unit result; `narration/RECHECK-LOCATION-TIME-44-45.prompt.md`; every lane-mast and desk mention in the manuscript (including 42:323); every Graving-gate mention in chapters 42–46; the 6:35 anchors in chapters 45–46; acceptance rows 43–45 in `WHOLE-BOOK-RECHECK-CONFIRMATION.md`; the earlier frozen editions of 44 and 45 |
| State at start | `chapter-44.md` = `c81c8566…` and `chapter-45.md` = `f8467d4d…`. These matched both feedback headers, acceptance rows 44–45, and `sourceSha256` in `chapter-4{4,5}.performance.json` |
| Files edited | `manuscript/chapter-44.md` (1 line), `manuscript/chapter-45.md` (1 line) and this report. New frozen edition `editions/audio-location-time-44-45-pre-repair/` |
| Not touched | Chapter 43 (still `18aeddbb…`, byte-identical) and every other chapter. Every earlier report and frozen edition. Canon, continuity, maps, ledger, the acceptance table and `AUTHORSHIP.md`. Every narration artifact: feedback, direction, performance JSON, clarity review, contexts, prompts and WAVs. Scripts and git state. No commit, push, publish, render or listening. No Skill, Agent, subagent, other model or paid API. |

**Scope of claim.** This report changes two lines of text and nothing else. Nobody has listened to them, re-narrated
them or rendered them, and the narration validators have not been rerun. Both narration source hashes are now stale
(see §7).

## 1. Freeze (before any edit)

`editions/audio-location-time-44-45-pre-repair/` did not exist. I created it and copied both working files into it
with `cp -p`, and `cmp` confirmed each copy byte-identical before editing. The copies are read-only (444) and have a
`SHA256SUMS.txt`. They verified `OK` before the edits and again after.

| File | Frozen (= accepted) | After this repair | Words (`wc -w`) | Bytes | Lines |
|---|---|---|---|---|---|
| `chapter-44.md` | `c81c856671d9d99886dbdb6f7277b5111fe0beb3f18c201d46abd97a2f441ace` | `8932f4219685ddea9c0feee2d7b88b7b5bd43ef78aaa8d26b9f207dbdfa0c1cb` | 8,432 → 8,432 (0) | 43,086 → 43,084 (−2) | 499 → 499 |
| `chapter-45.md` | `f8467d4d06ab05d22f75c7efea3c034e8b4604f7f32700a22712dfa0410e1edd` | `07a7859be33cce8becfbd1fabe01ea709f03ad624ea5ff97855990ae75d92ffa` | 7,327 → 7,327 (0) | 38,125 → 38,131 (+6) | 361 → 361 |
| `chapter-43.md` (control) | `18aeddbbc35392f2fb20c6d66738b361d4a4ce138ec79c07b9b9e81c0fbd38b1` | unchanged | 5,715 | — | 319 |

Chain: accepted → `editions/audio-location-time-44-45-pre-repair/` → current. Paragraph and line counts are
unchanged.

## 2. Changes (exact)

`diff editions/audio-location-time-44-45-pre-repair/chapter-4N.md manuscript/chapter-4N.md` shows only these lines.

| # | Ch:line (para) | Before | After | Words |
|---|---|---|---|---|
| 1 | 44:217 (prose para 106) | "**Ten paces inside the dock**, at his desk under the lane mast, Noa looked at his pens." | "**Ten paces off the chalk**, at his desk under the lane mast, Noa looked at his pens." | 0 (2 words changed) |
| 2 | 45:343 (prose para 166) | "…past the seam and the first stake to **the shut black gate of the Graving**." | "…past the seam and the first stake to **the grey ward across the Graving's mouth**." | 0 (5 words changed) |

The rest of both paragraphs is unchanged and keeps its word order.

## 3. Finding 1: 44:217, Noa's desk (confirmed)

**Where the desk is.** Five independent anchors put Noa's desk under the lane mast, ten paces from the third mark,
which is forty-five paces inside the dock:

- 42:323: Noa draws the third mark; "ten paces off against the dock's south wall, the Board's lane mast had been
  moved down… and set up on its feet."
- 43:153: "forty-five paces inside the dock, on Noa's long chalk line… Noa at his desk under the lane mast against
  the dock's south wall, ten paces off."
- 43:177: Kiva, on the chalk, hears "Noa, at his desk ten paces from her."
- 44:399: Kiva, back on the chalk, "Ten paces off, under the lane mast, Noa had his eyes on his pens."
- 45:179: Kiva, on the dock floor forty-five paces in, "Noa, at his desk under the lane mast, ten paces off."

**Why 44:217 contradicts them.** At 44:217 Kiva is kneeling on the sill at the dock mouth (44:185, 44:211, 44:215).
"Ten paces inside the dock" puts the desk ten paces in from the mouth, which is thirty-five paces short of where it
stands before and after.

**Readings tested and rejected.**

- **Elapsed time or a move.** No line moves the desk or the mast between 43:153 and 44:399. Noa reads both cliffs
  (44:219 at 6:11:40 and 44:401 at 6:14:50) from the same desk.
- **Narrative camera.** If the distance were measured from Kiva, it would be forty-five paces, not ten. If it were
  measured from the chalk, the anchor would say so. "Inside the dock" is measured from the mouth, where she kneels.
- **A different mast.** The only other mast is the Circuit's travelling mast, on the basin wall with Polglase at its
  desk (43:145, 44:45, 44:105). The "lane mast" is always Noa's.

**Origin.** The slip is original. It is in `editions/movement-006-first-draft/chapter-44.md:215` and
`editions/whole-book-pre-repair/chapter-44.md:217`.

**The repair.** This is the feedback's own smallest candidate. "Off the chalk" uses the relation already stated at
42:323, 43:153 and 44:399, so it adds no new measured depth for the desk. I rejected "Forty-five paces inside the
dock" for that reason. The established fact is "ten paces off the chalk", and the desk's exact depth is never given.

**Preserved.** Noa reading the first crossing as "Cliff… Eleven minutes past six and forty seconds. Read.", "The
notch at five", his voice carrying to the basin wall, and every clock, door and outcome in the chapter.

## 4. Finding 2: 45:343, the gate at 6:35 (confirmed)

**The clock.** The scene is set at 6:35 in three places: 45:325 ("at twenty-five minutes to seven"), the Proprietor's
signed line at 45:349, and the Clerk's quotation at 46:131. Two more details agree with 6:35: Kellan's pulse
reading "a quarter of an hour ago" (45:331, against 6:22 at 45:139), and Aske not yet arrived (45:265, 45:331).
The time is not the error.

**The gate.**

- 42:215–219: the gate went out at 12:20 the day before.
- 43:117–119: at dawn it lies "against the quay's edge with the Company's boats round it", and the dock mouth is
  "empty… where the gate had been."
- 45:281: "At twenty to seven the Company's two boats came out from the outer quay with the gate between them."
- 45:293: its foot touches the granite at 6:55.
- 45:297: "At four minutes past seven the gate seated."
- 45:299: only then does the black gate stand "in a shut dock."

At 6:35 nothing has come out from the outer quay. The Graving mouth is closed only by the Master's ward (44:413,
45:127, 45:275, which says the flood rises "against the Master's ward").

**Readings tested and rejected.**

- **A different gate.** The "sea gate" is the harbour entrance the flood comes "in under" (45:117, 45:269). It is
  never black, never "of the Graving", and is never shut against the flood. The line names the Graving's gate.
- **Narrative camera or prolepsis.** The 6:35 section comes after the 7:04 seating section, so it is an explicit
  cutback. Its sentence is a present observation ("The Proprietor looked across the basin. The flood was coming
  in…") and has no "afterward" marker. A listener has just heard the gate seat at 7:04 and then hears it already
  shut half an hour earlier.
- **"Shut" describing the dock rather than the gate.** The phrase is "the shut black gate", so the adjective belongs
  to the gate.

**Origin.** The slip is original. It is in `editions/movement-006-first-draft/chapter-45.md:339` and
`editions/whole-book-pre-repair/chapter-45.md:343`.

**The repair.** "the grey ward across the Graving's mouth" names what is actually there at 6:35. "Grey ward" is the
phrase Kellan's own point of view already uses at 45:127 ("the grey ward that hung across the mouth from wall to
wall"), so the repair adds nothing he could not see. It gives the Proprietor's line of sight the same end point it
had at 6:22, which is where his count went (45:127–131). That fits the next line: "Because I felt it go… Across that
water."

**Preserved.** The 6:35 writing time and its signature; the flood coming in over the mud past the seam and the first
stake; the six independent pumps; the gate arriving at 6:40, touching at 6:55 and seating at 7:04; the Master's hour
and lateness; Halden's voluntary relinquishment, its wording and Kellan's witness. No canon, mechanism or scene is
added.

## 5. Joins reread after the edits

- **44:215 → 44:217 → 44:219.** Kiva kneels on the sill under the cask. Then Noa, now at his desk ten paces off the
  chalk, looks at his pens. Then "His thin reader's voice carried… out of the mouth to the basin wall." His voice now
  comes from far up the dock, the same place the listener last heard it (43:235) and will hear it again (44:399).
  Nothing in the join implies he is near her.
- **45:341 → 45:343 → 45:345.** Kellan asks "Why?" The Proprietor looks across the basin at the flood coming in
  toward the grey ward. Then he says "Because I felt it go… Across that water." The image and his answer now point at
  the same thing. The next sentence, "Below the landing the six outfalls poured into it", still refers to the flood.
- **Checks.**
  - Each edit was an exact-once replacement.
  - A quote-parity scan finds no non-blank line with an odd number of `"` marks in either chapter.
  - "Ten paces inside the dock" and "shut black gate" no longer occur in chapters 44 or 45.
  - The frozen copies verify `OK`.
  - Chapter 43 is byte-identical.

## 6. Rejected or not acted on

- **Chapter 45, the feedback's literal wording.** It proposed "the ward across the Graving mouth". I used Kellan's
  own "grey ward" and the possessive "Graving's mouth", which the book uses elsewhere (45:127, 45:275).
- **Observed, out of scope, not changed.** At 44:219, Noa's voice "carried up the dock and out of the mouth". The book
  usually uses "up the dock" for inward and "down the dock" for toward the mouth (43:183, 44:271, 44:337, 44:349). Read
  that way, "up… and out of the mouth" is loose. It was not flagged, it does not affect location or time, and "carried
  up" also reads naturally as a voice rising. Recorded here only.

## 7. Next (not done here; not mine to do)

- **Acceptance.** Whoever holds the acceptance table should take the new hashes in place of `c81c8566…` and
  `f8467d4d…`:
  - chapter 44: `8932f421…`, 8,432 words;
  - chapter 45: `07a7859b…`, 7,327 words.
- **Narration.** `chapter-44.performance.json` and `chapter-45.performance.json` still name the old `sourceSha256`.
  `narration/RECHECK-LOCATION-TIME-44-45.prompt.md` is already staged for the independent recheck. That recheck must:
  - compare frozen and current text;
  - reread paragraph 106 of chapter 44, paragraph 166 of chapter 45 and their joins;
  - refresh the word-locked prose, paragraph reviews, direction and hashes for 44 and 45 only, with chapter 43
    kept exact;
  - check that any existing takes still match by ID, text and instruction;
  - rerun the validators before any ready marker.
- **Word stream.** Both word totals are unchanged. In chapter 44, two words change in paragraph 106. In chapter 45,
  five words change in paragraph 166 ("shut black gate of the Graving" becomes "grey ward across the Graving's
  mouth"). No sentence moves.
- **Remaining blockers in the 43–45 unit.** None in the prose that I know of. The unit stays not-ready until that
  recheck passes.
