# Hand-count repair — chapters 11, 14, 15, 19, 24 (accepted text)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime) |
| Session | `https://claude.ai/code/session_0136h4DjKQ5bHfdnawvBHrC8` (background job `98c8ed9c`) |
| Date | 2026-10-15, about 03:43–03:50 MDT |
| Brief | `planning/OPUS-AUDIO-HAND-COUNTS.prompt.md`, continuing §8 item 1 of `provenance/AUDIO-CLARITY-08-09-REPAIR.md` |
| Repository state | HEAD `f23455c` at start and `18671ce` by the end (a parallel session committed narration and planning files). The five chapters are byte-identical at both commits and to the frozen copies (hash-checked). |
| Files edited | `manuscript/chapter-11.md`, `chapter-14.md`, `chapter-15.md`, `chapter-19.md`, `chapter-24.md`, and this report. New frozen edition: `editions/audio-hand-counts-pre-repair/` |
| Not touched | Chapters 1–10 and 12–13, 16–18, 20–23, 25 onward, maps, ledgers, continuity files, prompts, narration artifacts, scripts, git state. No commit, push, render, subagent or worktree. |

**Scope of claim.** This is a text repair. It has not been listened to, re-narrated, re-rendered or
word-locked.

## 1. Read before deciding

- All of `provenance/AUDIO-CLARITY-08-09-REPAIR.md`, §8 in particular.
- `STATE_LEDGER.md` §2 *Body* and *Crossings* (lines 60–99): "The first two fingers of the left hand have
  permanently lost fine sensation. They bend, grip, and report pressure… They do not tell edge from flat,
  hot from cold". Also Aske's one-in-seven card and the sulk record in the M2 and M3 blocks.
- All of chapters 11, 14, 15, 19 and 24.
- A search of the whole manuscript for every "eight" and every counted-finger phrase (§6).

**Canon of the hand, as in the 08–09 report.** The book counts thumbs as fingers: "the eight fingers that
reported" plus "the two" makes ten across both hands (9:85, 16:329). So the left hand alone has **three**
reporting fingers and two impaired ones. Chapter 15:405 confirms it inside this scope: with "the first two
fingers" on the stone, "the cold, which her thumb told her about". The thumb is one of the three. Chapter 9,
as repaired, already uses "three" for the left hand in four places.

## 2. Freeze

`editions/audio-hand-counts-pre-repair/` did not exist. I created it before any edit, copied the files with
`cp -n` (no overwrite), and made them and `SHA256SUMS.txt` read-only. `shasum -c` gave `OK` for all five both
before and after the repair. Each frozen file is identical to `manuscript/` and to HEAD as it stood when frozen.

| File | Frozen (= accepted source = HEAD) | After repair | Words (`split()`) before → after |
|---|---|---|---|
| `chapter-11.md` | `f8cfba5b8af73bf95e858498ba447e664606ce92240d26c44f3c5fceb1f1f0d6` | `0e1e288bbdddf474ca8ac3afce7eee14c4fa53db4989251abb44a150e21f3a91` | 7,891 → 7,891 |
| `chapter-14.md` | `ebde9d5bd2958d0f52c87216f71ae3b0b45cfffbcd797323aa70dd946ec7ab30` | `b883ff96618cf23be71bef46ca3546eb35486087b75c56f0fd7308d8b02be03e` | 6,129 → 6,129 |
| `chapter-15.md` | `81f155d3ac5165c451e1d14ac2c1cf6af341a14aeab8854fb90256d74d6b0430` | `3b68f3f0fa1ec81b682e34717eb71a6fd6a2fd8101917cae5a1a4c076011bf47` | 8,375 → 8,375 |
| `chapter-19.md` | `0f20ea26daf750c8afcda43fee1e6169365f5f3c304ca80ec56da21efc644982` | `3e9e7a4c6bfe1fb2f577ba411358ed633a87a0b6ccbeb65075e886eba14f630d` | 7,611 → 7,611 |
| `chapter-24.md` | `12b01c9f8aeba25c47cfe3db0b38c785a6eb492df8febb38d0446ef61151e088` | `bf68b73a52ff1e62f35e523c2da1977bd6463d4529c33953740fde4d8e17f547` | 5,761 → 5,761 |

Line counts and character counts are also unchanged in every file ("eight" and "three" are both five letters
and one syllable).

## 3. Changes (exact)

Ten one-word substitutions, "eight" → "three". No sentence was recast, and no event, cost, sulk, limit,
voice or scene changed.

| # | Ch:line | Before | After | Source |
|---|---|---|---|---|
| 1 | 11:503 | …and opened and shut it, and the **eight** fingers went slower than they had gone a week before | …the **three** fingers went slower… | §8 list |
| 2 | 14:11 | She shut the fingers. They went slowly, all **eight** of them, like a gate in a wind. | …all **three** of them… | **Self-found** (§5) |
| 3 | 14:17 | it was cool, and the **eight** fingers shut when she told them, nearly at once. | …the **three** fingers shut… | §8 list |
| 4 | 14:387 | her left hand flat on the oilcloth… where the **eight** fingers could feel the warmth of it and the two could not. | …the **three** fingers could feel… | §8 list |
| 5 | 14:393 | her hand had closed on the oilcloth, all **eight** of the fingers that would close; | …all **three** of the fingers that would close; | **Self-found** (§5) |
| 6 | 15:109 | with the first two fingers on the cold grit and the **eight** held off it. | …and the **three** held off it. | §8 list |
| 7 | 15:381 | a hand flat on a stone… light, the two fingers on it and the **eight** held off. | …and the **three** held off. | §8 list |
| 8 | 15:399 | her left hand flat on a stone… with the first two fingers on it and the other **eight** held off | …the other **three** held off | §8 list |
| 9 | 19:345 | opened and shut the hand, and all **eight** fingers that reported came in to the palm | …all **three** fingers that reported… | §8 list |
| 10 | 24:361 | opened the hand and shut it. All **eight** fingers that reported came in to the palm | All **three** fingers that reported… | §8 list |

## 4. Each reported location, checked against context

All eight reported locations are **real one-hand errors**. None is a two-hand use or a figure of speech.

- **11:503.** The second crossing (Sunday the 8th). "The hand was white to the wrist… Kiva held it up…
  opened and shut it". One hand, the crossing hand. It also follows 9:167 as repaired ("The other three are
  slow to shut"), a week earlier, so "slower than… a week before" now compares like with like.
- **14:17.** Aske's noon/four/nine checks after the third crossing: "At nine that night… it was cool, and the
  eight fingers shut". "It" is the hand, cold to the knuckle at four. One hand.
- **14:387.** "her left hand flat on the oilcloth… where the eight fingers could feel the warmth of it and the
  two could not". Named as the left hand, so three. The two still cannot feel warmth, which keeps the ledger's
  "do not tell… hot from cold".
- **15:109.** "her left hand flat on the top stone of the wall… the first two fingers on the cold grit and
  the eight held off it". One left hand.
- **15:381.** "a hand flat on a stone… the two fingers on it and the eight held off". "A hand" is singular,
  and the two fingers fix it as the left. One hand.
- **15:399.** "her left hand flat on a stone… the first two fingers on it and the other eight held off". One
  left hand. Line 405 ("her thumb told her") confirms the count.
- **19:345.** "Aske held the hand… Kiva sat on the bed and opened and shut the hand, and all eight fingers
  that reported came in to the palm… and the two that did not came in with them." One hand.
- **24:361.** Same construction after Aske's fourth-night check: "opened the hand and shut it. All eight
  fingers that reported". One hand.

**Preserved in every case:** each sulk (knuckle → wrist → inch above → mid-forearm → elbow), every warm-by
morning, Aske's cards and counts ("Five of six", "Six of six"), the light two-finger tests, the two fingers'
permanent loss ("the two could not", "the two that did not", "two dead fingers"). The two still bend and come
in with the others, as the ledger says they "bend, grip". No sensation is restored, no healing is implied and
no power changes.

**Wording.** I kept each original frame exactly ("the three fingers", "the other three", "all three fingers
that reported") rather than adding "other" where it was absent. The contrast with "the two" is already in
each sentence, and a one-word change keeps the rhythm the narration will be directed for.

## 5. Found while verifying and repaired — chapter 14, lines 11 and 393

**Not in the §8 list.** In the same chapter as two listed instances:

- **14:11.** After the third crossing: "The hand was white past the wrist. Kiva held it up… She shut the
  fingers. They went slowly, all eight of them". This is the identical one-hand count, six lines above 14:17.
- **14:393.** "her hand had closed on the oilcloth, all eight of the fingers that would close; and she opened
  it again… and laid it flat". It is the same left hand laid flat at 14:387, six lines earlier.

If I had repaired 14:17 and 14:387 and left these two, chapter 14 would count the same hand as three and as
eight within a few lines, and a listener would hear both. Each is a one-word change in a file this brief
allows, and it applies the brief's own rule ("where the actual context truly describes one left hand").
This follows the 08–09 report's precedent for its self-found ¶71. **The fresh recheck should confirm or
reject changes 2 and 5 explicitly, since they were not reported findings.**

## 6. Joins and rechecks

**Mechanical recheck (script, against the frozen copies).** A word-level diff of all five files shows exactly
ten opcodes, every one `replace ['eight'] -> ['three']`, on lines 11:503, 14:11, 14:17, 14:387, 14:393,
15:109, 15:381, 15:399, 19:345 and 24:361. No other byte changed. Line, word and character counts are equal.
The frozen `SHA256SUMS.txt` still verifies. `git status` shows only the five chapters modified and the new
edition untracked, besides files that belong to other sessions. A residual search for "eight" near
finger/held/reported wording in the five chapters finds only "*eighty-eight*" (Pru's pulse count, 15:381).

**Joins (read in full, before and after).**

| Changed line | Previous paragraph | Next paragraph | Body / count agreement |
|---|---|---|---|
| 11:503 | 11:501 Orla, "*Two,*" | 11:505 "She thought about the yard…" | One hand; slower than 9:167 "the other three are slow to shut" |
| 14:11 | 14:9 Orla, "*Three,*" | 14:13 Aske at seven on Monday | White an inch past the wrist; one hand |
| 14:17 | 14:15 Aske's noon/four/tonight | 14:19 "On Tuesday at seven it was warm." | Wrist → knuckle → cool; the three shut nearly at once |
| 14:387 | 14:385 Jude, "That's what it's for" | 14:389 the skin, the pack, the officer | Left hand; the three feel the lamp and the two do not (permanent) |
| 14:393 | 14:391 "toward something that kept time" | 14:395 "Thursday," | Same left hand closes, then is laid flat again |
| 15:109 | 15:107 *Creak. Slap.* | 15:111 *Pushing. And not.* | Two on the grit, three held off: the standard light test |
| 15:381 | 15:379 "nothing that kept time" | 15:383 "Then nothing again." | Same test; Pru's pulse 88 unchanged |
| 15:399 | 15:397 "Kiva went forward alone." | 15:401 "She waited." (15:405 thumb feels cold) | Three held off, the thumb among them |
| 19:345 | 19:343 Aske's card, "Five of six" | 19:347 "Three nights." | One hand; the two come in with them, unfelt |
| 24:361 | 24:359 Aske, "She's had a knee for twenty years." | 24:363 Perrin at the foot of the bed | One hand; "Six of six; certified" unchanged |

One audio note, not a defect: 19:345 now ends a sentence on "…came in with them." and the next paragraph
opens "Three nights." The word "three" falls about twenty words apart, in two different senses. I judged it
acceptable and left it. The narration director may want a beat at the paragraph break.

**Ledgers and continuity:** no change is required. `STATE_LEDGER.md` §2 and the M2/M3 blocks record only "the
first two fingers of the left hand" and "the two fingers as before". The repaired prose now agrees with them
and with chapter 9.

## 7. Locations rejected or preserved (and why)

**Inside the five chapters.** No reported location was rejected. Other finger counts there are correct and
untouched: every "two fingers" / "two dead fingers" (14:163; 15:439, 489, 531; 19:49, 149, 167; 24:315,
321, 387), "the first two fingers of her left hand" (24:315, 387), and "eight-tenths" (14:177, a dram
figure). Pike's "all ten" (19:15) is his own two hands and correct.

**Outside the five chapters (reported, not touched, by instruction):**

| Location | Text | Verdict |
|---|---|---|
| 4:317 | "She had a pulse in those two fingers as she had in the other eight." | **Correct.** A general statement about all her fingers on both hands, with no single hand in view. |
| 4:385 | "They did the eight." | Not fingers: the remaining eight trials of Mara's proof. |
| 5:49 | "the other eight held it" (the ward at her right hip) | **Correct, two-hand.** The hand door is held across both palms (cf. 9:85, 9:93). |
| 6:7 | "longer than the other eight together" | Not fingers: entries. |
| 7:591 | "a child with eight fingers" | **Figure of speech** for both hands' reporting fingers. Correct. |
| 9:85 | "the eight fingers that reported" | **Correct, two-hand** (already ruled in the 08–09 report). |
| 16:329 | "her hands on the rail… both of them, the eight fingers that reported and the two that did not" | **Correct, two-hand.** |
| 18:379; 32:171, 173; 34:39 | "the eight pens", "all eight lines" | Not fingers: mast pens. |
| 36:133 | "the eight *nothing found*" | Not fingers: house returns. |

**Result:** no one-hand "eight" survives anywhere in the manuscript (chapters 1–40 as they stand), so the later
movement review has no instance of this defect to repair.

## 8. Consequential unresolved items

1. **Narration and published copies are now stale for chapters 11, 14, 15, 19 and 24.** Source hashes have
   changed (word counts have not). Anything derived from the old bytes still carries "eight": narration
   scripts or word locks for units 10–12 and 13–15 (`narration/DIRECT-UNIT-13-15.prompt.md` was queued during
   this session), the Breeze pipeline for these chapters, and the reader copies published at 1.18.41. These
   need refreshing by their owners. I did not touch them.
2. **19:175, Hart's hand: "It had five fingers and a thumb".** By the book's own convention (thumbs counted as
   fingers), that is six digits. Many readers take the phrase as an idiom for a whole hand, but a listener may
   hear six. It is outside this brief (not Kiva's hand, not a one-hand "eight"), so I have not changed it.
   One possible fix is "It had four fingers and a thumb". That is an owner or recheck call.
3. **Self-found changes 2 and 5 (14:11, 14:393)** await explicit confirmation or rejection by the fresh
   recheck (§5).
4. `provenance/MOVEMENT-005-COLD-READ.md` and `provenance/tools/m5_metrics.py` appeared untracked during this
   session. They belong to a parallel session, and I did not open or edit them.

## 9. Readiness

**Ready for a fresh clarity recheck of the ten changes.** The recheck should:

- Confirm the ten substitutions against `editions/audio-hand-counts-pre-repair/SHA256SUMS.txt`.
- Confirm or reject the self-found 14:11 and 14:393 changes.
- Re-derive any narration word lock or published copy from the new source hashes.

Nothing here is human-tested and nothing has been re-rendered. Nothing is committed.
