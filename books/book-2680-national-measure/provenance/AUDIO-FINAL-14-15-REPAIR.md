# Final audio repair: chapters 14 and 15 (the two surviving recheck defects)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime). Same author as `AUDIO-HAND-COUNTS-REPAIR.md` and `AUDIO-SPATIAL-15-19-REPAIR.md`. |
| Session | `https://claude.ai/code/session_01RuZYDaDf3fKGYUYtEMMWrK` (this session continues background job `f842bac9`, which wrote the spatial repair under `session_01Ux9pqm4dAvEtor1ngMh967`) |
| Date | 2026-10-15, about 05:50–05:55 MDT |
| Brief | `planning/OPUS-AUDIO-FINAL-14-15.prompt.md` |
| Findings resolved | The two remaining concerns of `narration/HAND-AND-SPATIAL-RECHECK.md` (14:393 and 15:93) |
| Repository state | HEAD `2cc3e4c`. Both chapters were byte-identical to that recheck's "current source" hashes before editing. |
| Files edited | `manuscript/chapter-14.md`, `manuscript/chapter-15.md`, and this report. New frozen edition: `editions/audio-final-14-15-pre-repair/` |
| Not touched | Every other chapter, maps, ledgers, continuity files, prompts, every narration and Breeze file, the recheck's validator and refresh scripts, earlier editions, git state. No commit, push, render, publish, subagent or worktree. |

**Scope of claim.** This is a text repair. It has not been listened to, re-narrated, re-rendered or word-locked.

## 1. Read before deciding

- `narration/HAND-AND-SPATIAL-RECHECK.md` in full, with its evidence table and the rows for 14:393 and 15:93.
- All of chapter 14 and chapter 15 as they currently stand.
- **Body canon.** `STATE_LEDGER.md` §2 *Body*: "The first two fingers of the left hand have permanently lost fine sensation. They bend, grip, and report pressure… They do not tell edge from flat, hot from cold".
- **Repaired usage elsewhere.** 9:85 and 16:329 ("the eight fingers that reported and the two that did not", for both hands). 19:345 and 24:361 ("all three fingers that reported came in to the palm… and the two that did not came in with them"). 14:387 ("the three fingers could feel the warmth of it and the two could not").
- **Cadence canon (the Pit).** 9:349 ("They stamp on one… There's a stamp on four that isn't as heavy as the one on one"), 9:379 ("the light stamp, the fourth"), 9:505 ("stamp light on four"), 9:583. In chapter 15: 15:95 (Perrin's count) and 15:131 ("the count of four, with a light stamp at the end").
- My earlier reports, `AUDIO-HAND-COUNTS-REPAIR.md` and `AUDIO-SPATIAL-15-19-REPAIR.md`.

## 2. Freeze

`editions/audio-final-14-15-pre-repair/` did not exist (`test ! -e` checked). I created it before any edit and copied with `cp -n` (no overwrite). The two files and `SHA256SUMS.txt` are read-only (`chmod 444`). `shasum -c` gives `OK` for both, before and after the repair. No existing edition was replaced. `audio-hand-counts-pre-repair` (five files) and `audio-spatial-15-19-pre-repair` (two files) still verify `OK`.

| File | Frozen (= recheck's current source) | After this repair | Lines | Words (`split()`) | Bytes |
|---|---|---|---|---|---|
| `chapter-14.md` | `b883ff96618cf23be71bef46ca3546eb35486087b75c56f0fd7308d8b02be03e` | `67950efe8ea329d1d1118bcf2e2ad733b6678a6ddc4db5df3d6b0d15a2ca044d` | 397 → 397 | 6,129 → 6,134 | 31,079 → 31,101 |
| `chapter-15.md` | `1213d947fd4bd6671a4ff3682334645c831851eb4c8049ca21b5662d896a25bd` | `bbee01a321528b1c509c062eef91f9bd3d5a59a995128156115044815f667916` | 559 → 559 | 8,420 → 8,423 | 42,770 → 42,792 |

**Hash chain for these two chapters (all four stages are recoverable):**
- Chapter 14: `ebde9d5b…` (hand-count freeze) → `b883ff96…` (after the hand-count repair; this freeze) → `67950efe…` (now).
- Chapter 15: `81f155d3…` (hand-count freeze) → `3b68f3f0…` (spatial freeze) → `1213d947…` (this freeze) → `bbee01a3…` (now).

## 3. Findings and changes (exact)

Both findings are verified as real. Two sentences changed, one in each chapter. No event, count of crossings, sulk, card, dram figure, power, limit or voice changed.

### 3.1 Chapter 14:393: closing versus feeling

**Verified real.** "all three of the fingers that would close" says that only three fingers can close. The ledger says the two impaired fingers still "bend, grip". In the book's own later scenes all five close: at 19:345 and 24:361 "the two that did not came in with them". Nothing in chapter 14 gives a new motor loss, and the hand had been warm since Tuesday (14:19). The "three" is right as a count of the fingers that *feel*. It is wrong as a count of the fingers that *move*.

- Before: `…so badly that her hand had closed on the oilcloth, all three of the fingers that would close; and she opened it again, deliberately, and laid it flat.`
- After: `…so badly that her hand had closed on the oilcloth, all three of the fingers that reported and the two that did not; and she opened it again, deliberately, and laid it flat.`

"would close" is replaced by "reported and the two that did not": two words out, seven in. The hand-count correction's "three" is kept. It now counts sensation, in the book's established term ("fingers that reported"), and the clause closes all five digits. The permanent loss is untouched: the two "did not" report. Nothing is healed and no power changes.

### 3.2 Chapter 15:93: which print is deep

**Verified real.** My spatial repair fixed the *interval*, third to fourth. But "every fourth print… a little deeper" made the deep print the fourth step. The surviving canon makes the *one* the heavy stamp and the *four* a lighter one (9:349, 9:379, 9:505). Perrin counts from the deep print ("That's the one… One, two, three, *four.* That's light"), so the deep print has to be the one.

The fix rewrites only the track sentence, as a sequence a listener can follow. Perrin's dialogue is unchanged and now agrees.

- Before: `There were three lines of them, side by side, and every fourth print in each line was a little deeper than the others.`
- After: `There were three lines of them, side by side, and in each line the prints went deep, shallow, shallow, a little deeper, and then deep again.`

**How the sentence maps to the canon:**
- **deep** is the stamp on one. Perrin: "Stamp. That's the one." The heavy stamp comes "every fourth step".
- **shallow, shallow** are the lean on two and the step back on three.
- **a little deeper** is the stamp on four, lighter than the one ("That's light. They're stamping light on four. Like the Pit").
- **deep again** is the next one.

**Preserved:**
- Three parallel tracks, and each print's three marks.
- The four-count and the light fourth stamp.
- The switch to the wheel's two at 15:131.

"Plain" was deliberately not used for the shallow prints, because in this chapter "plain" means ash without the hair (15:425, 435–439).

## 4. Joins and rechecks

**Mechanical recheck (script, against the new freeze).** A word-level diff finds exactly two changed lines, 14:393 and 15:93, with the words quoted above. Line counts are unchanged. All three frozen manifests verify.

**The ten hand-count corrections are intact, each checked at its line:**

| Site | Text now |
|---|---|
| 11:503 | "the three fingers went slower" |
| 14:11 | "all three of them, like a gate in a wind" |
| 14:17 | "the three fingers shut when she told them" |
| 14:387 | "the three fingers could feel the warmth of it and the two could not" |
| 14:393 | "all three of the fingers that reported and the two that did not" (the word "three" is kept; only its qualifier changed, as above) |
| 15:109 | "the three held off it" |
| 15:381 | "the three held off" |
| 15:399 | "the other three held off" |
| 19:345 | "all three fingers that reported" |
| 24:361 | "three fingers that reported" |

**The eastward-cast repair (15:161) is intact.** It is byte-unchanged since the spatial repair; its key clause occurs once.

**Joins (read in full, after the edit):**

| Changed line | Previous paragraph | Next paragraph | Agreement checked |
|---|---|---|---|
| 14:393 | 14:391 "All of it had been a thing coming toward something that kept time." | 14:395 "Thursday," she said. | Same left hand as 14:387. The three that feel the lamp's warmth and the two that do not now close together, then are laid flat. This agrees with 19:345 and 24:361 and with the ledger's "bend, grip". |
| 15:93 | 15:91 they find the track a quarter mile down | 15:95 Perrin: "That's the one. Every fourth step… *four.* That's light." | Deep = one (the heavy stamp, every fourth step); a little deeper = the light four. 15:97–99 (their own count up here) and 15:131 ("count of four, with a light stamp at the end") agree. |

**Ledgers and continuity:** no change is required. The ledger already states the motor and sensory facts the repair now matches. No ledger records print depth.

## 5. Findings rejected

None. Two alternatives were considered and not used:

- **14:393, "all five fingers" or dropping the count.** Rejected. It would remove the hand-count correction's "three", which the recheck asked to keep. It would also lose the sensation contrast that 14:387 sets up six lines earlier.
- **15:93, rewriting Perrin's dialogue instead of the track.** Rejected. His count matches the Pit canon word for word; only the physical description was wrong.

## 6. Remaining blockers and consequential items

1. **Narration is stale again for both chapters. None of it was touched.**
   - **Chapter 14.** Its existing marker, preparation review and prepared text derive from `b883ff96…`, and line 393 has changed. The recheck had already said not to consume that marker.
   - **Chapter 15.** The refreshed preparation from the recheck (`chapter-15.narration.md` `0ec3d891…`, Breeze s044, and preparation-review hashing `1213d947…`) now differs from the source at 15:93. The paragraph-43 blocker in `writing-monroe-feedback.md` is addressed by this text. It has to be cleared by the recheck owner, not by me.
2. **Next steps, outside this brief:** re-derive the chapter 14 and 15 prepared text and word locks from the new hashes; rerun `narration/validate_hand_spatial_recheck.py` and the 13–15 harness validation; then do a fresh clarity recheck of 14:393 and 15:93. The validator reconstructs earlier stages against fixed hashes, so it will now report a source change for 14 and 15 until its owner adds this stage.
3. **Published reader copies** of chapters 14 and 15 carry the earlier text.
4. Nothing is committed.

## 7. Readiness

**Ready for a fresh recheck of 14:393 and 15:93** against `editions/audio-final-14-15-pre-repair/SHA256SUMS.txt`. On a pass, chapters 14 and 15 can be re-prepared for narration. Nothing here is human-tested, re-rendered, published or committed.
