# Targeted recheck: Movement Five ensemble repair

**Model:** Claude Opus 5.5 (`claude-opus-5-5`), fresh context, review only. No files were edited.

**Coverage:**
- **Read in full:** the repair brief, `REPAIR-REPORT.md`, staged `CONTINUITY.md`, `provenance/MOVEMENT-005-CONTINUITY.md`, and staged chs 33, 39 and 40.
- **Read in part:** staged ch 34:150–169, 35:180–239, 36:205–379, 37:1–310 and 420–476, and 38:330–437. Canonical ch 21:440–454, ch 32:530–606 and ch 41:1–60.
- **Checked by search:** the forty readings, the room readings, "Stone's full", "far bank", "stair's ash", "for the stair", "hundred and thirty/forty/ten", and the Director quote in canon, both frozen editions and the worktree.
- **Not verified:** ch 38's byte-identity (I had no shell to hash with), and ch 38:1–329.
- **Staging location:** the main checkout's `revisions/ensemble-2026-09-29/` holds the repaired text; the repaired lines match the worktree. `REPAIR-REPORT` §9 says main still has the first draft, which is out of date.

| # | Item | Result |
|---|---|---|
| 1 | Ch 33 pace, preserved plants and numbers, noon chronology | **PASS** |
| 2 | The relocated forty, chs 35–36 | **PASS** |
| 3 | Ch 39 post-kill line and breach window | **PASS** |
| 4 | Toren's 1½ settle | **PASS** |
| 5 | Callie's ch 37 setup and ch 40 realization; spoken-number anchors | **PASS** |
| 6 | Audio disambiguation; the Director's exact quote | **FAIL**: fix 1 |
| 7 | "far bank", undated pump, ch 40 "hundred and thirty", "stair's ash" | **FAIL** on "far bank" only: fix 2 |
| 8 | 32→33 and 40→41 joins; ch 38 fight core | **PASS** |

## Notes

1. **Ch 33.**
   - The plants are all present: rag cross (153), *pen, 35th* (155), Pell deciding to count (91–95), the river baseline "Seven… The room" (67), Rook's fever exchange (77–81) and Pell sitting up alone (85).
   - The council keeps 40/16/24 (295), "Twelve… Half" (311), 28 as today's line (315), the healer-lost rule (325) and "Then I don't come in" (345, 349).
   - The inventory is now one audible sentence (297). The old 48/30 comparison is now said as what it meant: five with three healers, now four with two (305).
   - Chronology is clean: third hour → council → carrier → meal → jar one → "They went in at noon" (409) → the gate note *Noon. Out: 4* (473).

2. **The forty.**
   - In room 1 the jar is now only "hot… over everything in here" (35:213). The number is taken at the pump house instead: "Forty… where the river reads seven" (36:225).
   - Against the river's 7, the forty is about 33 above background. At the corner, where the counter reads 110 (35:225), the same jar would read about 143. That is above the 140 box, so "over everything in here" holds.

3. **Ch 39.**
   - "Twenty turns of the glass, from now" (131). Dee states the rule (159), calls "back over the line" at the third turn (197), and the paper adds one sentence (369).
   - The arithmetic works: about 1.6 lifted per turn takes the fence's 13 to about 17.8 by the third turn.
   - *Once. For the Director.* is unchanged, and the time under the line is recorded as part of the same breach, not treated as normal.

4. **Toren's 1½.**
   - The page marks it twice as a stretch: Callie at 37:171 and "half as much again" at 37:233. Dee confirms "lying still".
   - Staged 33:107 defines a full stone as what you settled ("All of it"). So "Stone's full" at 41:53 after one Handful reads as "it's all there", not as a one-Handful limit. There's no contradiction on the page.

5. **Callie.**
   - Ch 37 now ends on not knowing (205–213), with "who's worth the lee", her mother's fingers and Rook's "You'll want to look. Don't" (299) all kept.
   - Ch 40 lands the realization after the act: the edge of them, choosing what to hold, the ache in the palm (163–171), and the look back (331).
   - All four anchors are plain and arithmetically true (37:175, 37:227, 40:73, 40:277).

6. **Director's wording.** The staged text should follow ch 21:
   - The Director's own speech (21:449) is "you do what you have to **do** and you come home". Canonical 33:289 and 36:343 use that wording.
   - Ch 32:543 is Dee quoting her. Staged 33:255 itself says Toren learned it by heart at the long table, while Dee only "quoted it" at the fire. So the ch 21 wording is right in-world, and Dee's dropped "do" is her paraphrase.
   - Ch 32:543 is a candidate for a later canon pass; it's outside this scope.

7. **The four phrases.**
   - **"far bank" (33:459):** a real audio hazard. In ch 33, "far bank" means the fence side (33:11, 33:169), and Rook was placed "at the near end of the bridge" (33:413). Heard aloud, "somebody laughed on the far bank" sounds like someone inside the fence.
   - **Undated pump:** safe. The checkpoint gives no date, so leaving the pump undated is correct.
   - **Ch 40:113 "a hundred and thirty":** no fix needed. It's the canonical wording (canon 40:115), it matches the fight's last reading (38:361), and it falls inside the checkpoint's "110–130 undrawn" range for Dee.
   - **"stair's ash" (33:129):** canonical (canon 33:147). "The stair" here is jar B's allotment, which canon already calls ash "for the stair" (30:263, 32:595, 38:385).

8. **Joins and the fight.**
   - **32→33:** Jab lying awake with his hand over Little becomes "asleep at last… hand flat over the left side of his coat". Toren is still counting them.
   - **40→41:** the party goes into the cut on D+49, and ch 41 opens at the mouth of the cut before light, with Toren's "two by tonight" → "two turns".
   - **Ch 38:** the line, "What do you feel?", the 130, the crossing, "This is once", jar 4, the handoff and "Mine." are coherent. It hands off cleanly to ch 39's first line. No repair needed.

## Required surgical fixes (2)

**Fix 1: the Director's exact wording.** One word restored in two lines.
- **Ch 33:257.** Replace `you do what you have to and you come home.*"` with `you do what you have to do and you come home.*"`
- **Ch 36:315.** Replace `"*you do what you have to and you come home.*"` with `"*you do what you have to do and you come home.*"`

**Fix 2: "far bank" (ch 33:459).**
- Replace `Somebody laughed on the far bank, and it was Rook.` with `Somebody laughed at the near end of the bridge, and it was Rook.`

After the fixes, update `CONTINUITY.md` §8 (the Director's wording row) to say the staged text follows ch 21. The owner questions on the pump's age and the stone capacity stay open and don't block acceptance.

## Surgical-fix closeout

Applied on 2026-09-30 exactly as specified:

- ch 33 and ch 36 now follow the Director's original ch 21 wording, `have to do`;
- ch 33 now places Rook `at the near end of the bridge` rather than on the
  misleading `far bank`;
- `CONTINUITY.md` now records the ch 21 wording as the resolved canon source.

Final repaired movement word count: **48,264**. No other manuscript line changed
during this closeout.

## Final gate

**ACCEPT**
