# Spatial, cadence and digit-count repair: chapters 15 and 19 (accepted text)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime) |
| Session | `https://claude.ai/code/session_01Ux9pqm4dAvEtor1ngMh967` (background job `f842bac9`) |
| Date | 2026-10-15, about 04:51–04:58 MDT |
| Brief | `planning/OPUS-AUDIO-SPATIAL-15-19.prompt.md` |
| Repository state | HEAD `9168241` throughout. HEAD still holds the pre-hand-count bytes of both chapters (`81f155d3…`, `0f20ea26…`). The working tree differed from HEAD only by the four uncommitted eight→three substitutions in these two chapters (word-diff checked). |
| Files edited | `manuscript/chapter-15.md`, `manuscript/chapter-19.md`, and this report. New frozen edition: `editions/audio-spatial-15-19-pre-repair/` |
| Not touched | Every other chapter, ledgers, maps, continuity files, prompts, narration (including the untracked `narration/breeze/chapter-15/` that belongs to a parallel render), scripts, existing editions, git state. No commit, push, render, subagent or worktree. |

**Scope of claim.** This is a text repair. It has not been listened to, re-narrated, re-rendered or word-locked.

## 1. Read before deciding

- All of chapters 15 and 19.
- `narration/monroe-1.2.5/calder/chapters-13-15/chapter-15/writing-monroe-feedback.md` (paragraphs 43 and 76).
- `provenance/AUDIO-HAND-COUNTS-REPAIR.md`, all of it, and §8 item 2 in particular.
- **Cadence canon.** 9:349, 9:379, 9:505, 9:511 and 9:583 (the Pit): "They stamp on one, lean on two, come back on three, stamp light on four." In chapter 15: 15:95 ("Every fourth step… One, two, three, *four.* That's light") and 15:131 ("the count of four, with a light stamp at the end").
- **Catching canon.** A cut rung drops as a heap and "runs" down the fall of the ground. The catcher throws a cloth over it "at the first cast" before it reaches a hazard: 10:179, 10:265–267, 11:121, 11:167, 13:153, 13:181. Throwing from three paces is ordinary: 15:317 (Pru), 30:249, 31:369.
- **Yard geometry in chapter 15.** The yard falls east to the race, "a hand in four" (15:141). The house is west and uphill; Anwen's wall stands between the husks and its door (15:159). The husks stand "a yard from the race's edge" (15:281, 283). The last husk falls "on the uphill side, away from the race" (15:309).
- **Hart's hand canon.** Book One 8:107 ("He lost a hand… left Meridian at nineteen with one hand"), Book One 10:269, `STATE_LEDGER.md` §11 item 1 ("one working hand and one ruined one that is still on his arm"), `CHARACTERS.md` (Hart row), and every ledger block naming Hart (M3: "Right hand turned out at the Regional's Bench").

## 2. Freeze

`editions/audio-spatial-15-19-pre-repair/` did not exist (`test ! -e` checked). I created it before any edit and copied with `cp -n` (no overwrite). The two files and `SHA256SUMS.txt` are read-only (`chmod 444`). `shasum -c` gives `OK` for both, before and after the repair. No existing edition was replaced. `editions/audio-hand-counts-pre-repair/` still verifies `OK` for chapters 15 and 19.

| File | Frozen (= source before this repair = hand-count "after") | After this repair | Lines | Words (`split()`) |
|---|---|---|---|---|
| `chapter-15.md` | `3b68f3f0fa1ec81b682e34717eb71a6fd6a2fd8101917cae5a1a4c076011bf47` | `1213d947fd4bd6671a4ff3682334645c831851eb4c8049ca21b5662d896a25bd` | 559 → 559 | 8,375 → 8,420 |
| `chapter-19.md` | `3e9e7a4c6bfe1fb2f577ba411358ed633a87a0b6ccbeb65075e886eba14f630d` | `4a633ce44804458cadd5db1f6ef616ef12a3577ae75b504fd9b9f4ef6585b9c8` | 475 → 475 | 7,611 → 7,611 |

## 3. Findings and changes (exact)

All three reported issues are real. Three paragraphs changed. No event, outcome, dram figure, power, limit or voice changed.

### 3.1 Chapter 15:93: track cadence (feedback ¶43)

**Verified real.** "every third print… deeper" contradicts the next line ("Every fourth step… One, two, three, *four*"), 15:131 ("the count of four") and the Pit canon (9:505). There is no reading in which "third" is right. With a heavy stamp on one and a light stamp on four, the deep prints do not fall every third print either.

- Before: `There were three lines of them, side by side, and every third print in each line was deeper than the others.`
- After: `There were three lines of them, side by side, and every fourth print in each line was a little deeper than the others.`

"third" → "fourth" is the brief's fix. I added "a little" (two words) so that the listener hears "deeper", then "That's light", and the two agree: the print is a stamp, and a light one. Three parallel tracks are kept. Perrin's count, "Like the Pit", and the switch to the wheel's two at 15:131 are unchanged.

### 3.2 Chapter 15:161: catching ground, reach and direction (feedback ¶76)

**Verified real.** Kiva is "west of the husks, on the uphill side". A rung that ran "east down the fall" would therefore run *away* from her, toward the race, not "toward her cloth". The sentence gives opposite directions for one catch. The rest of the scene fixes the actual layout, from west to east: house, Anwen's wall, Kiva, the husks, then the race lip a yard beyond them (15:159, 281, 283). The first catch (15:177) and the failed second catch (15:287, "She threw it from her knees… at a heap that was moving") are both **throws**.

The fix therefore keeps her where she is. It states why she is there (no standing room below the husks), how far off she is, which way a rung runs, and that she must throw east to cover it before it reaches the lip.

- Before: `Kiva went to her ground. She had chosen it from the field: a place on the cobbles west of the husks, on the uphill side, between them and the house, where a rung that fell would run east down the fall toward her cloth before it got to the race. She tested it, clean, and planted, and stood with her cloth on her shoulder.`
- After: `Kiva went to her ground. She had chosen it from the field. There was nowhere to stand below the husks; the lip of the race was a yard past their feet. So she had taken a place on the cobbles three paces west of them, on the uphill side, between them and the house. A rung that fell would run east, down the fall, away from her and toward the race, and she would have to throw east after it and have her cloth over it before it got to the lip. She tested her ground, clean, and planted, and stood with her cloth on her shoulder.`

**Preserved:**
- The eastward slope ("a hand in four") and the race hazard: the second heap still loses ash into the water, so Grade Second and the frosted sheet are unchanged.
- The first catch, "at the first cast".
- The order of the fight and every cut.
- "between them and the house".
- Her planted still door. Nothing else is lit.

**No new ability.** A thrown cloth from three paces is the catcher's ordinary act (15:317; 31:369). "Room" was deliberately avoided, because it is a still-door term in this book (6:327, 15:447). "She tested it" became "She tested her ground" because "it" would otherwise attach to "the lip".

### 3.3 Chapter 19:175: Hart's digit count (hand-count report §8 item 2)

**Verified real; there is no six-digit canon.** No file in either book says Hart has six digits. That covers both manuscripts, `STATE_LEDGER.md`, `CHARACTERS.md`, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `SERIES_MAP.md`, planning, provenance and packets. The only occurrence of "five fingers and a thumb" is this line and the prompts that quote it. The book counts thumbs as fingers (9:85, 16:329; Pike's "all ten", 19:15), so the line gives a hand six digits.

- Before: `It had five fingers and a thumb, and the shape of it was a hand's shape.`
- After: `It had four fingers and a thumb, and the shape of it was a hand's shape.`

This is one word with the same syllable count. The following are unchanged:
- "It was a whole hand… the first surprise", which still answers Book One's "lost a hand" in the way ledger §11 reconciles it.
- The permanent impairment: waxy skin, curled fingers that do not straighten, "It doesn't feel… It doesn't hold" (19:181).
- The ache near anything that keeps time.
- The revelation and the scene.

## 4. Joins and rechecks

**Mechanical recheck (script, against the frozen copies).** A word-level diff shows changes only on 15:93, 15:161 and 19:175, and exactly the words quoted above. No other line changed, and line counts are equal.

**Earlier hand-count repairs are intact.** All four that live in these chapters are present and unchanged:
- 15:109 "the three held off it"
- 15:381 "the three held off"
- 15:399 "the other three held off"
- 19:345 "all three fingers that reported"

The other six (11:503, 14:11, 14:17, 14:387, 14:393, 24:361) are in files this session did not open for writing. A residual search for "eight" in both chapters finds only "*eighty-eight*" (15:381), "eight and ninety-three" (15:519) and "thirty-eight" (19:219). None is a finger count.

**Joins (read in full, after the edit):**

| Changed line | Previous paragraph | Next paragraph | Agreement checked |
|---|---|---|---|
| 15:93 | 15:91 they find the track | 15:95 Perrin: "Every fourth step… *four.* That's light" | Four-count; deeper, but light; three lines. 15:131 "count of four, with a light stamp at the end" agrees. |
| 15:161 | 15:159 Anwen's wall between the husks and the house door | 15:163 Perrin counts the wheel's *and* | West to east: house, wall, Kiva three paces off, husks, lip a yard past them. The rung runs east, and she throws east. This sets up 15:177 (first cast), 15:281–287 (a yard from the edge; thrown from her knees) and 15:309 (the walked husk falls uphill and does not run). |
| 19:175 | 19:171 "He took his right hand out of his jacket." (then the section break) | 19:177 "The Bench," he said… | A whole, ruined right hand; five digits. 19:181 (no feeling, no grip) is unchanged. |

**Ledgers and continuity:** no change is required. Nothing in `STATE_LEDGER.md` or the continuity files records the print interval, Kiva's standing place in the mill yard, or a digit count.

## 5. Findings rejected

None of the three was rejected. Two alternative fixes were considered and not used:

- **Move Kiva east/downhill of the husks (the feedback's first option).** Rejected. The text gives no ground there (the race lip is a yard off), and it would break 15:287, where she throws past Anwen's wall and Jude's legs from the first hem. That would redesign the fight.
- **"five fingers" alone at 19:175.** Rejected in favour of "four fingers and a thumb". That keeps the sentence's rhythm and is unambiguous under either way of counting.

## 6. Remaining blockers and consequential items

1. **Narration derived from the old bytes is now stale.** It needs refreshing by its owners; none of it was touched here.
   - **Chapter 15:** the Calder/Monroe unit for chapters 13–15 (`narration/monroe-1.2.5/calder/chapters-13-15/chapter-15/`: narration, performance JSON, clarity review), the direct unit (`narration/DIRECT-UNIT-13-15.result.md`), and the untracked parallel render in `narration/breeze/chapter-15/`.
   - **Chapter 19:** any chapters 19–21 unit or word lock built from `3e9e7a4c…`.
   - The chapter 15 feedback file asks for these steps next: reread both paragraphs and their joins (done here), refresh the hashes (§2), regenerate the track, and rerun validation.
2. **Published reader copies** of chapters 15 and 19 still carry the old text.
3. **The hand-count repair's own open items stand.** Its §8 item 1 (stale narration for 11, 14, 15, 19, 24) and item 3 (a recheck to confirm the self-found changes at 14:11 and 14:393) are not resolved by this report. Its item 2 is resolved here (§3.3).
4. Nothing is committed. The whole working-tree difference for these two chapters against HEAD `9168241` is now the four hand-count substitutions plus the three changes above.

## 7. Readiness

**Ready for a fresh clarity recheck of 15:93, 15:161 and 19:175.** That recheck should confirm them against `editions/audio-spatial-15-19-pre-repair/SHA256SUMS.txt`, then re-derive narration and word locks from the new hashes. Nothing here is human-tested, re-rendered or committed.
