# Audio-clarity repair — chapters 8–9 (accepted text)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime) |
| Session | `https://claude.ai/code/session_016PdiKpwCF9c2zg44aweDNg` (background job `9ab8514b`) |
| Date | 2026-10-15, about 02:47–03:00 MDT |
| Brief | `planning/OPUS-AUDIO-CLARITY-08-09.prompt.md` |
| Findings answered | `narration/monroe-1.2.5/calder/chapters-07-09/chapter-08/writing-monroe-feedback.md`; `…/chapter-09/writing-monroe-feedback.md` |
| Repository state at start | HEAD `2c0c73b`; `manuscript/chapter-08.md` and `chapter-09.md` identical to HEAD (hash-checked) |
| Files edited | `manuscript/chapter-08.md`, `manuscript/chapter-09.md`, this report. Frozen copies added under `editions/audio-clarity-08-09-pre-repair/` |
| Not touched | Every other chapter, maps, ledgers, continuity files, prompts, narration artifacts, git state. No commit, push, render, subagent or worktree. |

**Scope of claim.** This is a text repair, not an audio repair. Nobody has listened to it, and it has
not been re-narrated, re-rendered or word-locked again.

## 1. Read before deciding

All of chapters 7, 8, 9 and 10; all of `STATE_LEDGER.md` (§1 calendar, §2 body, M1 and M2 blocks);
all of `provenance/MOVEMENT-001-CONTINUITY.md` and `provenance/MOVEMENT-002-CONTINUITY.md`; both
feedback files. I also searched the whole manuscript for every finger count and crossing count, so that
a fix here would not contradict text that survives elsewhere (§6).

## 2. Freeze

`editions/audio-clarity-08-09-pre-repair/` did not exist. I created it and copied the files with
`cp -n` (no overwrite). The copies are read-only, with a `SHA256SUMS.txt`, and verified `OK` after the
repair.

| File | Frozen (= accepted source = HEAD `2c0c73b`) | After repair |
|---|---|---|
| `chapter-08.md` | `da17e21338a4a6fbb9fc7d1a8e146262642615f75d82abf8c5ed1052e909e8f0` | `2cf6a1091908ef2c91b399da139ab3a5291856f922e804fcb16e62d09e1b858c` |
| `chapter-09.md` | `60912ab028ead67c8e29741478d7434c1c4cb8d7a5ae1863e03cdb1f7f10f236` | `3a2316f2ef3e3e8f2f0da99b110d29cc27690b6c23d2610ef6f8740788728c0d` |

Word counts (`split()`): chapter 8, 6,977 → 6,977 (0). Chapter 9, 8,917 → 8,918 (+1, from "Three
*more*"). All six defects below were already in the first-draft editions
(`editions/movement-001-first-draft/chapter-08.md`, `editions/movement-002-first-draft/chapter-09.md`).
They survived review, repair and recheck. None came from a later edit.

## 3. Changes (exact)

Eight one- or two-word substitutions. No sentence was recast, and no event, cost, injury, limit, voice
or scene changed.

| # | Ch:line (para) | Before | After | Finding |
|---|---|---|---|---|
| 1 | 8:33 (¶16) | "He reached," said Pike. "**Three** words. | "He reached," said Pike. "**Two** words. | Nonblocking count |
| 2 | 8:167 (¶82) | to its name, on the **thirtieth** day of the first month, | to its name, on the **twenty-fifth** day of the first month, | BLOCKING ¶82 |
| 3 | 9:127 (¶62) | all of it, the **eight** fingers as well as the two, | all of it, the **three** fingers as well as the two, | BLOCKING ¶62 |
| 4 | 9:145 (¶71) | "Five more. **Four** in this city. | "Five more. **Three** in this city. | Self-found; same arithmetic as ¶293 (§5) |
| 5 | 9:167 (¶81) | The other **eight** are slow to shut, | The other **three** are slow to shut, | BLOCKING ¶81 |
| 6 | 9:323 (¶156) | the two dead fingers on the cold metal and the other **eight** held off it. | …and the other **three** held off it. | BLOCKING ¶156 |
| 7 | 9:599 (¶292) | The **eight** fingers shut when she told them, and the two stuck out, as before. | The **three** fingers shut when she told them, … | BLOCKING ¶292 |
| 8 | 9:601 (¶293) | *Five more wanted. **Four** can be had here.* | *Five more wanted. **Three more** can be had here.* | BLOCKING ¶293 |

## 4. Each finding, checked against prose and canon

### Chapter 8, ¶82 — Monday called "the thirtieth" — **real; repaired (change 2)**

- **Prose:** the scene opens "on Monday evening" (8:111). Later in the chapter: "*Friday the 29th*" (8:383),
  "Tomorrow's the thirtieth" (8:441) and "the last day of a month" (8:563, Saturday). Kellan's line uses the
  present tense ("That's what this team **has** to its name, on the thirtieth day"), so a listener hears it
  as today's date. Read that way, it puts Monday after Friday.
- **Canon:** `STATE_LEDGER.md` §1 says the first month of 2681 begins on a Friday, so its Mondays are the
  4th, 11th, 18th and **25th**. Ledger M1.6 names "The Rowan table of the 25th". MOVEMENT-001-CONTINUITY
  §1 lists "**Mon 25th** — The Rowan kitchen table", and §2 has "as she says it to Jude on the 25th". Other
  details in the scene agree with the 25th: "A week ago Friday" is the conditions of the 15th, and "He'll
  have my name tomorrow" is Birch on Tuesday the 26th.
- **Why "twenty-fifth" and not the proposal.** The feedback offered "before the end of the first month" *or*
  establishing the Monday date in canon. Canon already establishes it, so I matched the prose to canon. The
  dated figure suits Kellan, who dates every line in the book. The proposed phrase would also blur what
  3.84 means. I considered a second reading: "the thirtieth" as the entry deadline ("entries by Saturday the
  30th", ch. 6). I rejected it because the line is in the present tense and nothing in this scene names
  the 30th as a deadline.
- Preserved: 9.64 held, 5.8 spoken for, 3.84 uncommitted, the 0.8 sealed and every other figure.

### Chapter 8, ¶16 — "He reached" called three words — **real; repaired (change 1)**

"He reached" is two words. Pike says it to give Kiva the line, and she writes *Went wrong: he reached.*
(8:45), which is also two words. Nothing in the scene presents the miscount as character (Pike is exact
about counts everywhere else). It was an authorial slip. "Two words" also echoes Rhea's "Two words" (ch.
7) and the standing line *Two words, once*, which suits the chapter. The feedback's caution, "do not silently
correct spoken words", is addressed here: the change is in the source and recorded in this report, not left
to the narrator.

### Chapter 9, ¶62, ¶81, ¶156, ¶292 — one left hand counted as "eight" plus "two" — **all four real; repaired (changes 3, 5, 6, 7)**

- **Canon of the hand:** ledger §2 says the first two fingers of the left hand have permanently lost fine
  sensation. Ten fingers in all, thumbs counted as fingers (as the book does in "the eight fingers that
  reported" + "the two"), leaves eight reporting fingers across **both** hands. The **left hand alone** has
  the two impaired fingers and three others.
- **Scope of each passage:** after the crossing the cold is in one hand ("the rest of the hand", 9:105). Kiva
  "held up her left hand" (9:125). Aske "took her left wrist" (9:165). She "laid the hand flat" (9:323, after
  "her left hand", same sentence). She "held up her left hand to the lamp" (9:599). Each passage is about one
  left hand, and none says anything about the right. So "eight" in these four places is physically
  impossible, and the correct figure is **three**.
- **Wording:** each fix replaces one number word. For ¶62 and ¶292 I wrote "the three fingers" rather than
  the proposed "the other three fingers". "As well as the two" and "and the two stuck out" already supply the
  contrast. "Three" plus "two" makes the "all of it" in ¶62 add up to a hand, and the one-word change keeps
  the rhythm the narration was directed for. For ¶81 and ¶156, "the other three" follows the feedback
  exactly.
- **Preserved:** the slow shut, the cold to the knuckle, warm by noon, Aske's uncertainty ("I don't yet know
  what longer means"), the light two-finger test, the two fingers unchanged ("as before"). No sensation is
  restored and no healing is implied.
- **Checked and left alone:** 9:85, "it lay across the eight fingers that reported". This is **correct**. The
  hand door is a ward that lies across both palms: "a penny of silver between her right palm and her left"
  (9:93), felt "in the bones of both wrists at once" (9:95). Eight is the right count there. Same for
  ch. 5:49 and ch. 16:329 ("her hands on the rail…, both of them").

### Chapter 9, ¶293 — four local crossings left after the first was spent — **real; repaired (change 8)**

- **Prose:** Kiva counts the month's dates: "Today, the eighth, the fifteenth, the twenty-second, and the
  twenty-ninth. And on the twenty-ninth I'll be on the road" → "Four. In this city." (9:35–39). These are
  totals, said **before** the first crossing. Today's crossing (the 1st, 0.31) is then made and recorded. What
  remains in the city is the 8th, 15th and 22nd: **three**. Six are wanted in all, so five remain.
- **Canon:** MOVEMENT-002-CONTINUITY §2 says "No sixth was manufactured; the calendar and the card allowed four
  in Meridian" (the 1st, 8th, 15th, 22nd). Ledger M2.1 and M2.6 put the fifth and sixth at the Saltmere gate.
  Aske's card allows one in seven days at most (9:175, "Your next is Sunday").
- Took "Three more can be had here" as proposed. Kept "Five more wanted". Jude's "one and forty-nine left" on
  the 1.8 line (9:149) is unchanged and still covers five crossings at about 0.30.

## 5. Found while verifying and repaired — chapter 9, ¶71 (Orla, 9:145)

**Not in the feedback.** Orla says "Five more. Four in this city." straight after the first crossing. This is
the same arithmetic the brief asked me to verify ("the remaining local crossing count after the first of four
local dates has been spent"), and it makes the same overstatement as ¶293. "Five more" is a remaining count,
so "four in this city" next to it is also heard as remaining, and only three are. If I had repaired ¶293 and
left this, Orla's figure and Kiva's note would disagree two pages apart. I changed one word: "Three in this
city." Orla's clipped voice, the "won't round down" line and her pre-crossing totals (9:37–41) are
unchanged. **The fresh recheck should confirm or reject this one explicitly, since it was not a reported
finding.**

## 6. Joins and rechecks

| Changed paragraph | Previous paragraph | Next paragraph | Calendar / body / arithmetic |
|---|---|---|---|
| 8:33 | 8:31 Kiva "did not want to write it" | 8:35 "I was a count late." | 8:45 *Went wrong: he reached.* (two words) agrees |
| 8:167 | 8:163–165 Kellan's crossing line; "I've not asked for that" | 8:169 Jude, "I said in the tenth month…" | Monday the 25th → Fri 29th → Sat 30th "the last day of a month"; the first "thirtieth" now falls on Friday, where it belongs |
| 9:127 | 9:125 "Kiva held up her left hand." | 9:129 Pru takes "the wrist" | One hand; 3 + 2 = "all of it"; white to the wrist after the crossing; nothing healed |
| 9:145 | 9:143 "It costs the hand" | 9:147 Jude writing | 1 done; 8th, 15th, 22nd left in the city; 29th on the road; 5 more of 6 |
| 9:167 | 9:165 left wrist held a minute | 9:169 "It did that in the summer." | Knuckle cold, palm warm, the two as they were, the three slow until noon |
| 9:323 | 9:321 "Closer." | 9:325 *Pushing. And not.* | Same light test as 9:253 and ch. 7; left hand only |
| 9:599 | 9:597 the white *why* | 9:601 the note | Warm since noon (Aske, 9:171); the two "as before" |
| 9:601 | 9:599 | 9:603 "Then, because it was true…" | Agrees with Orla at 9:145 after the repair |

Chapter 10 opens on Tuesday the 3rd and says nothing about finger or crossing counts that depends on these
lines. Its "two dead fingers lying on the canvas" (10:271) is consistent.

## 7. Findings rejected

**None rejected on substance.** All six reported problems are real. In three places I departed from the
proposed *wording*, for the reasons in §4:

- ¶82: "twenty-fifth" instead of "before the end of the first month". This is the feedback's own second
  option, since canon already fixes the date.
- ¶62 and ¶292: "the three fingers" instead of "the other three fingers".

## 8. Unresolved items and surviving canon that needs the same change

1. **The same one-hand "eight" survives in eight places outside this brief's scope** (not edited, by
   instruction). In each, only the left hand is raised, laid down or examined:
   - ch. 11:503 ("the eight fingers went slower")
   - ch. 14:17 ("the eight fingers shut when she told them")
   - ch. 14:387 ("her left hand flat on the oilcloth… where the eight fingers could feel the warmth")
   - ch. 15:109, 15:381, 15:399 ("the eight held off it" / "the eight held off" / "the other eight held off")
   - ch. 19:345 and ch. 24:361 ("all eight fingers that reported came in to the palm… and the two that did not")

   **Other surviving canon changes are therefore required** to make the book agree with chapter 9 as
   repaired. Each is a one-word fix ("three" for "eight"). Chapters 11–24 belong to accepted Movements Two and
   Three, and narration of chapters 10–12 will meet the ch. 11 and ch. 14 instances next. This needs an owner
   assignment, and it must not overlap Sonnet's supervision of later movements. Chapters 5:49, 9:85 and
   16:329 are two-hand uses and are correct.
2. **Ch. 7:591** (Rhea: "a child with eight fingers") is a figure of speech for both hands' reporting fingers.
   It is consistent with canon. No change recommended.
3. **Noticed, not changed, not reported by narration:** ch. 8:25, Pike's "on Tuesday week" for a past Tuesday
   (the craft was written the 10th–12th). In some dialects "Tuesday week" means a future date, so a listener
   might stumble. Left for the Codex recheck to judge. It is not a canon conflict.
4. **Narration artifacts are now stale for chapters 8 and 9.** Source hashes changed, chapter 9 gained one
   word, and `chapter-0{8,9}.narration.md`, `performance.json` and the word lock still carry the old wording.
   They need refreshing by the narration owner. I did not touch them.
5. `planning/COMPLETION-LOOP-STATE.md` showed as modified in `git status` during this session. I did not edit
   it. It belongs to the parallel supervisor.

**Ledgers and continuity:** no change is required. `STATE_LEDGER.md` (§1, M1, M2) and both continuity files
already record the 25th, four Meridian crossings and the two impaired left fingers. The repaired prose now
agrees with them.

## 9. Readiness

**Ready for a fresh Codex clarity recheck of chapters 8–9.** The recheck should:

- Confirm all eight changes against the frozen copies (`SHA256SUMS.txt` above).
- Confirm or reject the self-found ¶71 change (§5).
- Re-derive the narration word lock from the new source hashes.

Nothing here is human-tested and nothing has been re-rendered. Item 1 in §8 is open and owner-gated.
