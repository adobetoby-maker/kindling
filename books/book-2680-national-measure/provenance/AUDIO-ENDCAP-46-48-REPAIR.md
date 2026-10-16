# End-cap consistency repair: the sister's book (chapter 46) and Rhea's officer years (chapter 48)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime; not verifiable from inside the session), authenticated Max subscription CLI |
| Session | `https://claude.ai/code/session_01QdGpvPHTYtNZwKMqfTmQpv` (background job `5b45fa0e`) |
| Date | 2026-10-15, about 18:01–18:06 MDT |
| Instruction | Owner: "Verify and minimally resolve only sister-account prior knowledge and officer-tenure findings; reject false flags with evidence, freeze and report." The owner authorised this bounded loop, in which the same author answers findings that the narration pass sent back. |
| Findings answered | `narration/monroe-1.2.5/calder/chapters-46-48/chapter-46/writing-monroe-feedback.md` (SHA-256 `2dc2f3739fbc9a266c1208f7ac414f18dabdafa0f73d1a2d2af3e2f3762ceb9e`), BLOCKED at 46:273 (prose para 131). `…/chapter-48/writing-monroe-feedback.md` (SHA-256 `41c8d392fcb1e4f243f141ef55f6ef15971f60b9e7c3674a6b057853f81a3e80`), BLOCKED at 48:81 (prose para 38). Unit summary: `narration/DIRECT-UNIT-46-48.result.md` (`8abbc994…`). Each chapter's `clarity-review.jsonl` has exactly one `writing-change-needed` row: 46 para 131 and 48 para 38. |
| Read before editing | Chapters 46 and 48 in full. Chapter 45 from the dock-floor count to the end (45:150–379), including 45:189, 45:193, 45:315–319 and the Proprietor's fault-paper scene at 45:327–379. Chapter 47's sheet and fault-paper mentions. 03:205–225 and 07:300–318. Every "officer for", "eleven years" and "twenty years" hit in the manuscript, including 37:373. Both feedback files, the unit result, `narration/RECHECK-ENDCAP-46-48.prompt.md`, `STATE_LEDGER.md` (whole-book note at line 963), `WHOLE-BOOK-REPAIR.md` WB-01, `WHOLE-BOOK-RECHECK.md` WB-01, acceptance rows 46–48 in `WHOLE-BOOK-RECHECK-CONFIRMATION.md`, and the earlier frozen editions of 46 and 48 (`movement-006-first-draft`, `whole-book-pre-repair`). |
| State at start | `chapter-46.md` = `8b6b8de0…` and `chapter-48.md` = `0e8c628e…`. These matched both feedback headers, acceptance rows 46 and 48, and `sourceSha256` in `chapter-4{6,8}.performance.json`. `chapter-47.md` = `6e3de61e…`, which matches row 47 and its performance JSON. |
| Files edited | `manuscript/chapter-46.md` (1 line), `manuscript/chapter-48.md` (1 line) and this report. New frozen edition `editions/audio-endcap-46-48-pre-repair/` |
| Not touched | Chapter 47 (still `6e3de61e…`, byte-identical) and every other chapter, including the working 44/45 of the separate loop. Every earlier report and frozen edition. Canon, continuity, maps, ledger, the acceptance table and `AUTHORSHIP.md`. Every narration artifact: feedback, direction, performance JSON, clarity review, contexts, prompts, ready markers and WAVs. Scripts and git state. No commit, push, publish, render or listening. No Skill, Agent, subagent, other model or paid API. |

**Scope of claim.** This report changes two lines of text and nothing else. Nobody has listened to them, re-narrated
them or rendered them, and the narration validators have not been rerun. The narration source hashes for 46 and 48
are now stale (see §6).

## 1. Freeze (before any edit)

`editions/audio-endcap-46-48-pre-repair/` did not exist. I created it and copied both working files into it with
`cp -p`, and `cmp` confirmed each copy byte-identical before editing. The copies are read-only (444) and have a
`SHA256SUMS.txt`. They verified `OK` before the edits and again after.

| File | Frozen (= accepted) | After this repair | Words (`wc -w`) | Bytes | Lines | Paragraphs |
|---|---|---|---|---|---|---|
| `chapter-46.md` | `8b6b8de0ac006f9c9229284f38997c5b671d9be30e536dd396725af875ae05af` | `a548da2293408fff6dcdd7d095eb7470dce7cbd474765444a342a557f40504c6` | 7,121 → 7,117 (−4) | 36,967 → 36,945 (−22) | 379 → 379 | unchanged |
| `chapter-48.md` | `0e8c628ef774bcf31a7acfb0b8014c9be67c86bdfb5a1ed2614c0aa33c1a0315` | `0adc917ed84018fbf4e1bc2a010b846d8edaee1de2e178379bf01541d89a18fe` | 6,429 → 6,429 (0) | 32,918 → 32,918 (0) | 341 → 341 | unchanged |
| `chapter-47.md` (control) | `6e3de61edfe18bdba53b0e7f25a0e4a1fc71eb667d07c94c945443172f0dc1c5` | unchanged | 7,175 | — | 357 | — |

Chain: accepted → `editions/audio-endcap-46-48-pre-repair/` → current. Paragraph indexes were counted as non-blank
lines, excluding the chapter heading and `---` breaks. The same method gives 106 for the earlier 44:217, which
agrees with that record, and it agrees with the clarity-review rows.

## 2. Changes (exact)

`diff editions/audio-endcap-46-48-pre-repair/chapter-4N.md manuscript/chapter-4N.md` shows only these lines.

| # | Ch:line (para) | Before | After | Words |
|---|---|---|---|---|
| 1 | 46:273 (prose para 131) | "Rhea had said *I've written it.* She had not known about **the sister's book, or** Kellan's sheet." | "Rhea had said *I've written it.* She had not known about Kellan's sheet." | −4 (deletion only) |
| 2 | 48:81 (prose para 38) | "She had been an officer for **twenty** years." | "She had been an officer for **eleven** years." | 0 (1 word changed) |

The rest of both paragraphs is unchanged and keeps its word order.

## 3. Finding 1: 46:273, the sister's book (confirmed)

**What Kiva has already seen and heard before noon.** Kiva knew the sister's account existed, and she knew roughly
what it said:

- 45:193 (Kiva's lens, on the dock floor, straight after the nine seconds): "Her sister had taken a small book out of
  her sleeve and was writing in it, standing, very fast." Kiva sees the book and sees it being written in.
- 45:315: Thrale to Kiva at the cart: "My sister says I did. Your officer will say you did. The man on the outfall
  walk will have a clerk who'll say he did."
- 45:319: "Write that you counted, and that you don't know what. My sister's written it for me, in my words." This
  gives the existence of the account (it has been written), who wrote it (the sister), and its gist (the Master
  counted and does not know what).

The Clerk's wording at 46:265, "in the Order's book in the Master's words", repeats Thrale's "in my words". The only
detail it adds is where the account was written, and Kiva had already watched that book being written in. Saying
"she had not known about the sister's book" because it names the Order's book would still contradict 45:193.
Current 45 differs from the frozen 44–45 edition only at 45:343, so none of these anchors depends on the separate
44/45 repair.

**The three kinds of knowledge, kept apart.**

| Account | Existence known before noon? | Contents known? | Source |
|---|---|---|---|
| Rhea's slate | Yes. "I've written it." | Partly. "I'll not write what. I don't know what." | 45:189 |
| The sister's book | Yes. Seen being written, then named by Thrale | The gist: the Master counted and does not know what | 45:193, 45:315, 45:319 |
| Kellan's sheet as a counting account | No | No | See below |

**Why the Kellan clause stays.** Thrale only predicted "a clerk who'll say he did" (45:315), and it was a future
guess about an unnamed clerk. Kiva was not on the outfall walk (45:325–379 is Kellan's scene). At 46:131 she does
hear the Clerk speak of "a line on the harbour pump house's fault paper in the Proprietor's own hand, witnessed".
That is the relinquishment line. The Clerk does not name the witness and does not say the paper records counting.
The aside at 46:129 says that Kellan "had given the Clerk a folded sheet of fault paper". That is narration, and it
does not establish what Kiva knew of the sheet's contents. The first time Kiva hears that "Mr. Renn's sheet of fault
paper" says somebody counted is the Clerk's line at 46:265. "She had not known about Kellan's sheet" is true in that
sense, so I kept it.

**"She had not known about the three accounts" stays.** The first draft already used this to mean the set of three
together: the very next sentence says she knew of Rhea's. With the sister's clause gone, the paragraph reads in a
straight line. She did not know there were three. She had heard of Rhea's. She had not known about Kellan's. She had
thought she was counting by herself. That last thought is placed "sitting on the dock floor", which is before Thrale
speaks at the cart (45:315), so it is still true.

**Readings tested and rejected.**

- **"Book" as the Order's book in particular.** Rejected, because 45:193 shows Kiva watching the sister write in "a
  small book".
- **Acted uncertainty, or a pause before "the sister's book".** Rejected. The narration pass rightly ruled that
  already-heard knowledge needs a change in the words.

**Origin.** The slip goes back to the first draft. It is in `editions/movement-006-first-draft/chapter-46.md:271`
and `editions/whole-book-pre-repair/chapter-46.md:273`.

**The repair.** This is the feedback's own smallest candidate: delete "the sister's book, or". I considered adding
"The Master had said her sister had." (+3 words net). I rejected it because the elliptical "had… had" is unclear
when heard aloud, and because the paragraph needs no new words to be consistent.

**Preserved.** The Clerk's revelation of three separately written accounts (46:265) and of three people counting in
the same nine seconds (46:269). The accounts' independence ("written separately before any of them had spoken to the
others"). Kiva's not knowing about Kellan's sheet. Her belief on the dock floor that she counted alone. Hart's line
that follows (46:275–277). Mara's later "three accounts of three people counting" (46:371). Both joins (46:271 →
273 → 275) read cleanly.

## 4. Finding 2: 48:81, Rhea's officer years (confirmed)

**The established figure is eleven.** Every passage that gives Rhea's years as an officer says eleven:

- 03:217 (Rhea, on the 1st of the eleventh month 2680): "I've been an officer of this company for eleven years."
- 07:311 (Rhea's lens): "Rhea had been an officer for eleven years."
- 07:385, 14:389 ("an officer of eleven years"), 20:351, 31:365 and 31:401 agree, and 6:57 and 11:133 tie Pike's
  eleven years at her heel to the same span.
- `WHOLE-BOOK-REPAIR.md` WB-01 changed 20:351, 31:365 and 31:401 from "six years" to "eleven years". 
  `WHOLE-BOOK-RECHECK.md` passed WB-01. `STATE_LEDGER.md` (whole-book note) records "Rhea has been an officer eleven
  years."

Chapter 48 takes place on the 30th of the third month 2681, five months after 03:217. That is not enough time to
reach twelve years, let alone twenty.

**Why "twenty" appeared.** 37:373 (Rhea's lens) gives her "a Torch's hands… from twenty years of cutting from behind
a skin". She has been cutting for twenty years and an officer for eleven. The draft used the cutting figure where it
needed the officer figure. Changing the number brings back the existing distinction and does not touch 37:373.

**Readings tested and rejected.**

- **"Officer" in a looser sense of service.** Rejected. 07:311 uses the same words, "had been an officer for", with
  eleven.
- **Officer elsewhere before this company.** Rejected. 03:217 says "of this company", but 07:311 and 31:365 have no
  such limit, and no passage gives Rhea earlier officer service.

**Origin.** The slip goes back to the first draft. It is in `editions/movement-006-first-draft/chapter-48.md:77` and
`editions/whole-book-pre-repair/chapter-48.md:81`. WB-01's search found "six years" passages, so it did not catch
this "twenty".

**The repair.** "twenty" → "eleven", the feedback's own candidate. Eleven is the figure that 03, 07 and the ledger
already state, so no new number is introduced.

**Preserved.** Her realisation on the Lane's fourth tier ("thought *mine*… and known it for what it was"). Her
knowledge of how an officer keeps a girl, which still has eleven years behind it. The hypothetical "At the end of
five years", which is not a career figure and is unchanged. Her own past as a second ("Rhea had had a second like
that once. Before Pike. She had been the second."). That past lies before her officer years and does not conflict
with eleven. The joins 48:79 → 81 → 83 read cleanly. All outcomes of the chapter are untouched: Coombe's line, both
noes, Kiva's two conditions, Mara's signature, Anwen's departure and the hull.

## 5. Owner-level items: not decided

This loop answered only the two located findings. It made no owner-level universe choice and added no scene. Every
open owner item carried in both feedback files stays open exactly as listed in `WHOLE-BOOK-RECHECK-CONFIRMATION.md`:
Pettit/Yarrow doors, the unnamed colour and the brushed-twice wording, the certificate precedent, new interaction
properties, "caller need not have crossed", Vane/Home Line, sentence and progression targets, the tide clock and the
41-minute hold, brown ink, "my best machine", Penhale frost, the Order questions, the yield scale, Shapter, 76/77 as
written, and the outward ending. The separate 44/45 loop is untouched.

## 6. Remaining blockers and next step

- **Narration source hashes are stale for 46 and 48.** `chapter-4{6,8}.performance.json` still carry `8b6b8de0…`
  and `0e8c628e…`. The clarity-review rows 46/131 and 48/38 still say `writing-change-needed`. There are no ready
  markers for 46 or 48, and none should be written until the recheck passes.
- **Independent recheck owed.** `narration/RECHECK-ENDCAP-46-48.prompt.md`: a fresh check of these two corrections
  against 45–48, the frozen-to-current differences and both joins, saved as
  `provenance/AUDIO-ENDCAP-46-48-RECHECK.md`. Only after that: freeze the old 46/48 narration evidence, refresh only
  46/48 prepared prose, reviews, direction, contexts and hashes, keep 47 byte-exact, and rerun the word locks and
  validators.
- **Acceptance.** An explicit acceptance addendum for the new 46/48 hashes belongs to the supervisor after the
  recheck. The historical acceptance rows 46 and 48 were not edited.
- **Nothing listened to.** No take exists for the changed lines.

## 7. Commands run (verification)

```bash
cd books/book-2680-national-measure
shasum -a 256 manuscript/chapter-4[5-8].md manuscript/chapter-03.md manuscript/chapter-07.md
E=editions/audio-endcap-46-48-pre-repair
mkdir $E && cp -p manuscript/chapter-46.md manuscript/chapter-48.md $E/
cmp manuscript/chapter-46.md $E/chapter-46.md && cmp manuscript/chapter-48.md $E/chapter-48.md
(cd $E && shasum -a 256 chapter-46.md chapter-48.md > SHA256SUMS.txt && chmod 444 * && shasum -a 256 -c SHA256SUMS.txt)
# edits (two Edit calls, one line each)
diff $E/chapter-46.md manuscript/chapter-46.md; diff $E/chapter-48.md manuscript/chapter-48.md
wc -w -c -l manuscript/chapter-46.md manuscript/chapter-48.md
grep -n "sister's book\|officer for twenty" manuscript/*.md   # → none
diff editions/audio-location-time-44-45-pre-repair/chapter-45.md manuscript/chapter-45.md   # → only 45:343
```
