# Kindling 2680, Book One — Movement Six (chapters 41–48) — targeted recheck addendum

> Built by TAC

Verified 2026-10-12, about 02:40 MDT, by Claude Opus 5.5 (`claude-opus-5-5`). Review only. This file is the only thing written in the repository.

## Verdict: PASS

| What was asked | Verdict |
|---|---|
| R1 applied correctly, no broken join | **PASS** |
| R2 applied correctly, no broken join | **PASS** |
| R3 applied correctly | **PASS** |
| Protected and frozen checks claimed in the correction note | **PASS** |

The three corrections are on the page exactly as `editor/MOVEMENT-006-TARGETED-RECHECK.md` specified, and nothing else in the manuscript moved. One statement in the correction note is slightly too strong; it is a record-keeping point and does not affect the verdict (section 4).

## 0. Scope and method

- **Scope.** R1, R2 and R3, the joins they touch, and the mechanical claims in the post-recheck correction note. The note appears in three places: `editor/MOVEMENT-006-REPAIR-REPORT.md` section 10, `AUTHORSHIP.md` lines 1744–1779, and section 0 of `provenance/MOVEMENT-006-CONTINUITY.md`. I did not look at the optional notes or reread the movement.
- **Who.** The same session that wrote the recheck (`12e22edd-c1ec-4ca7-9da2-f9a57349a8a4`), resumed, and the same model that wrote and repaired the chapters. Not independent and not a human read.
- **How the "before" texts were obtained.** I had kept no copy of the post-repair chapters, only their hashes and my diffs. I rebuilt chapters 44 and 48 as they stood at the recheck by patching the frozen files with those diffs, and confirmed each rebuilt file hashes to the post-repair value recorded in the repair report (`24c2ce49…bab7` and `86f18032…3b4f`). The current files were then diffed against those.
- **Scratch files.** Written to `/tmp/m006-recheck.MnOksZ`, outside the repository, and left there.

## 1. The corrections

A full `diff` of each rebuilt post-repair chapter against the current file shows three changed lines in the whole manuscript, and no others.

| | Where | Before | Now | Finding |
|---|---|---|---|---|
| R1 | `manuscript/chapter-44.md`:17 | "And across the shaft, a foot above the water," | "And across the wall side of the shaft, back under the post, a foot above the water," | Matches the recheck's wording exactly. |
| R1 | `manuscript/chapter-44.md`:33 | "and a pace to one side." | "and a pace back toward the wall." | Matches exactly. |
| R2 | `manuscript/chapter-48.md`:251 | "I asked the week before last what ash was for," | "I asked last week what ash was for," | Matches exactly. The date phrase is the frozen draft's again. |
| R3 | `provenance/MOVEMENT-006-CONTINUITY.md`:196 (was 186) | "the six-month mistake" | "the four-month mistake" | Matches. "six-month" no longer occurs in the file. |

Occurrence counts across current chapters 41–48:

| String | Count |
|---|---:|
| "across the shaft" | 0 |
| "across the wall side of the shaft, back under the post, a foot above the water," | 1 |
| "a pace to one side" | 0 |
| "and a pace back toward the wall." | 1 |
| "the week before last" | 0 |
| "I asked last week what ash was for," | 1 |

## 2. Joins

- **44:17.** The sentence still runs from the main at the bottom of the shaft to the gate, and still ends on "like a window in its sash." Mara's next line follows it unchanged: the gate is "hanging on a screw," and the screw "goes up through the brick, on a slant." A gate at the wall side, back under the post, is where a slanting screw to the post would hang it.
- **44:33.** The fitter has "gone round to the wall side" at 44:29, and now says the gate is "a pace back toward the wall." A straight spindle from there comes up a pace out from the row and goes on leaning toward the lane, which is the lean 42:107 and 42:469 describe. "It was never crooked. It's aimed" is untouched and now true of the drawing.
- **Lines R1 depends on, all unchanged and still consistent.** The lid on the lane side of the post's foot (44:9); the east and west grooves (45:59, 45:323); the arm going down on the lane side (45:361, 46:135); the plate striking bottom under the bar (46:403).
- **48:251.** "I asked last week what ash was for, and a man told me" reads cleanly. Jude speaks on Saturday the 15th of a Tuesday the 4th, and it now agrees with the bursar's "last week" at 48:47. The knot clause in the same line ("two knots down the hill from mine") is as the repair left it.

No section break, scene or line count changed: chapter 44 is still 369 lines with 4 breaks, and chapter 48 is 481 lines with 5.

## 3. Protected and frozen checks claimed in the note

| Claim in the note | Result |
|---|---|
| The frozen edition matches its `SHA256SUMS.txt` | Confirmed. All eight OK. |
| Chapter 48 from "Miss Dane says that we're to run it" to the end is byte-identical to the frozen file | Confirmed. Frozen from line 393 and current from line 395 both hash to `41a0691f…49e4`. |
| Orla's cutaway with Hart's card is byte-identical | Confirmed. Frozen 301–335 and current 303–337 both hash to `471d2584…7a40`. |
| Each replacement matched exactly once | The outcome is confirmed: each new string occurs once and each old string not at all (section 1). I cannot observe the edit run itself. |
| Chapter 44 is 5,583 words, `0503075f…9010` | Confirmed. |
| Chapter 48 is 6,566 words, `b1b58353…d27b` | Confirmed. |
| Movement total 51,677 words, +811 on the first draft | Confirmed. The change from the repair is +9 and −2. |
| Chapters 41, 42, 43, 45, 46 and 47 unchanged | Confirmed. Their hashes equal the post-repair values. |
| `STATE_LEDGER.md` unchanged, `26db4775…b97a` | Confirmed. Its line on the post is still true of the page. |
| Checkpoint hash `760c9bd1…ff6d` | Confirmed. |
| Report hash with its section 10, `3c75f849…9182` | Confirmed. |
| Report sections 1 to 9 left as written | Confirmed. The first 193 lines hash to the report's pre-note value, `ace0219a…720e`. |
| `AUTHORSHIP.md` gained one appended note and nothing above it changed | Confirmed. The first 1,742 lines hash to the file's pre-note value, `0a2e5116…3a7a`. |
| Only five files changed | Confirmed. Both reviews, the brief, the recheck prompt and the recheck itself keep their hashes; `git status` shows no new modified file. |
| Nothing committed | Confirmed. `HEAD` is still `7877842`. |

## 4. One statement that is slightly too strong

The checkpoint's new paragraph says "No other line of this file was changed," and the report lists the checkpoint's changes as the R3 line, the sluice entry, item 19 and a new paragraph in section 0.

There is a fifth edit. In section 0, lines 49–50, the parenthesis about Noa's mistake was extended from "(his page dates from the sixth month)" to "(his page dates from the sixth month; the line in section 2 was corrected to match after the targeted recheck)".

- **How I know there are exactly five.** I reversed those five edits in a temporary copy. The result is 749 lines and hashes to `60ddf404…d208`, the checkpoint's hash at the time of the recheck.
- **Whether it matters.** The added clause is true and harmless. Only the "no other line" sentence is inaccurate, by that one clause. The acceptance entry can note it; it needs no prose change.

The other record edits follow the page. The sluice entry quotes both new phrases exactly and places the lid "on the lane side of the post's foot," as 44:9 does. Item 19 gives 51,677 words.

## 5. Still open, as the note itself says

The "not rechecked" status lines in the checkpoint, the ledger and the authorship entry are unchanged and wait for the acceptance entry. The optional notes in the recheck were not acted on and were not examined here.

## 6. Not done

I did not edit the manuscript or any record, review, report or prompt. I did not repair, broaden the review, commit, push, publish, narrate, draft Book Two or use subagents.
