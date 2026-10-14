# Kindling 2680, Book Two — Movement One — targeted recheck

Date: 2026-10-14. Verifier: Claude Opus 5.5 (`claude-opus-5-5`, runtime-reported), Claude Code
background job `fa4d3354`, remote session `session_01AP25iUkcaVx6RLEQMrjk5p`. Fresh context: this
session holds no drafting, review or repair transcript.

## 0. Scope and method

- **This is a bounded verification, not an editorial pass.** It is a same-model-family check and
  is not independent of the drafter, reviewer or repairer. No prose was edited. The book is not scored.
  The only file written is this one.
- **Read:** `planning/OPUS-5.5-MOVEMENT-001-RECHECK.prompt.md` and
  `planning/OPUS-5.5-MOVEMENT-001-REPAIR.prompt.md`. The repair brief is read to fix what "the
  three repair priorities" are. Its SHA-256 is `e64cce9167e44259832217a4d2d032883be83de33213dac438a84c1e6ac83489`, matching
  repair report §0. Also
  read: `provenance/MOVEMENT-001-EDITORIAL-REVIEW.md`, `provenance/MOVEMENT-001-COLD-READ.md` and
  `provenance/MOVEMENT-001-REPAIR.md`, plus the `STATE_LEDGER.md` sections the repair cites: §1,
  §3, §6, §11.5, M1.2, M1.3, M1.4 and M1.5. `UNIVERSE_BIBLE.md` lines 16–17 were consulted once, to
  test that the new "doors" gloss does not change meaning.
- **Comparison:** `git diff --no-index --word-diff=plain --unified=0`, run for each chapter between
  `editions/movement-001-first-draft/chapter-0N.md` and `manuscript/chapter-0N.md`. Every hunk was
  read. Where a hunk's correctness depended on the scene, the surrounding passage was read as well:
  - the ch. 2 bag sequence, lines 139–169 and 227–277
  - ch. 1 lines 399–411
  - ch. 6 lines 160–182 and 443–509
  - ch. 7 lines 105–194
  - ch. 8 lines 41–57, 149–163, 221–279 and 349–389
- **Figure counts:** each ledger figure was counted with `grep -o -F` across both directories.
- Line numbers below are those of `manuscript/` as it stands on this date. The repair kept every
  chapter's line count except ch. 6, which is four lines shorter, after its line 451.

## 1. Checksum result — PASS

`shasum -a 256 editions/movement-001-first-draft/*.md` gives all eight hashes exactly as recorded
in repair report §7:

| File | SHA-256 | Match |
|---|---|---|
| chapter-01.md | `fb8fa7e30a0aefd2b9d490c939c778248469723cefb51c8170f056fdc872227d` | yes |
| chapter-02.md | `56adf40a2b28b17d327e2ae4e829acb06f33bd203ea6158e51afe3b9f5ee74ec` | yes |
| chapter-03.md | `c40c084aae2f903a99d37feda0bee8064d15373c873d2755fbb0e3569efaedf6` | yes |
| chapter-04.md | `b08fe5dbc93f7c3ee2d0489ce3cbd47c0d812108eb1181e03daf07013c564d60` | yes |
| chapter-05.md | `cccb13228aee1e79f73232516602c4c01cdedf51807e3c366f15b3ea499b4db6` | yes |
| chapter-06.md | `b6da97b3cdd32ece49ed5d57ee1a3034e82f42cc08e589b8084d7f794cb92bb5` | yes |
| chapter-07.md | `1457575be0cc514e17cd2fa965b8ed0e4f4230cb7d619e81b7e3503b3d438490` | yes |
| chapter-08.md | `ee7d7f93d8ecee31e78d40c3396fbb9f5a15a31ebae66d04a7b37e51845b8e56` | yes |

The frozen edition is unmodified.

## 2. Priority 1 — Restore factual trust — **FAIL (one surviving defect)**

### 2a. The surviving defect

**ch. 2 §2, `manuscript/chapter-02.md:167`** (frozen line 167). The repair changed one ordinal in
this sentence and left the second:

> It slipped a third time. On the **next** Pru got it round and it held, and she sealed at
> fifty-nine with her face the color of brick, and on the **fifth** it went from under her fingers
> like a fish.

Line 169 continues: "That's four lost in six," she said.

- **The original was coherent.** Its ordinals counted the repeats after the first bag: bag 2 was
  "It slipped", bag 5 was "On the fourth" and bag 6 was "on the fifth". Only Pru's total was wrong.
- **The repair switched to counting bags but changed only half the sentence.** It made Pru count
  bags ("four lost in six") and changed "On the fourth" to "On the next". Repair report F5 itself
  lists "Bags 1–6 are sealed (54), slip, slip, slip, sealed (59), slip". By that count, "the next"
  is bag 5, so the bag that goes "like a fish" is the sixth. The sentence still calls it "the fifth".
- **What a first-pass reader meets.** Counting in the scene, a reader reaches five bags with the
  held one. Then the narration calls the next bag "the fifth". Then Pru, in the very next line,
  says "in six".
- **Why it matters.** The repair report says the edit was made "so the count reads one way on a
  single pass". It does not yet do so. In a book that trains its reader to check counts ("That
  adds"), this is a located tally error, and it sits exactly where Priority 1 was meant to restore
  trust.
- **Smallest fix:** "on the fifth" → "on the sixth", or "on the one after". It is one word or
  phrase on one line, and changes no event, figure or outcome. Nothing else in the passage
  depends on the ordinal: "Since the third bag" (`:265`) is true under either count, and the
  totals, 17 thrown and 12 sealed, already assume the sixth bag slipped.

### 2b. Corrections verified correct

| # | Location (repaired) | Verified against | Result |
|---|---|---|---|
| F1 | ch. 4:7, "The eleventh month was going by" | Ledger §1 (numbered months). The scene falls inside the eleventh month (the packet comes on Friday the 3rd of the twelfth, ch. 4:127), so "going by" is right where "had gone by" was not. | Correct |
| F2 | ch. 5:483, "It's the first month." | Ledger §1; M1.3 (the night of the 9th). The 1st of the first month is a Friday, so the 9th is a Saturday. | Correct |
| F3 | ch. 8:99, "The second month," said Pike | M1.3: "two in the second month". | Correct |
| F4 | ch. 1:311, "six of them" | Pumps 3, 5, 7; list 5, 6, 8, 9, 10, 12, 14. Only 8 shares no factor. Mara's own spoken enumeration names exactly six. | Correct |
| F5 | ch. 2:169 and :295 (tally, entry) | Bags 1–6 give 2 sealed and 4 lost; bag 7 sealed (56, `:227`); then 9 of 10 (`:277`). Thrown 6 + 1 + 10 = 17; sealed 2 + 1 + 9 = 12. The spends 0.16 + 0.07 + 0.09 = 0.32 and the held 25.21 are untouched. | Correct, except the ordinal at `:167` (§2a) |
| F5a | ch. 5:485, "lose four in the cold" | Follows F5. Kiva means the session before the thumb fix. | Correct |
| F6 | ch. 1:409, "And three days." | The scene is Tuesday the 18th (`:333`, `:347`, `:375`). On 30-day months, 13 + 30 + 30 + 1 = 74 days from the 17th and 73 from the 18th. 73 days is 10 weeks 3 days, against "ten and four days" on Monday the 17th (`:67`). | Correct |
| F7 | ch. 3:297, drum twenty-nine | Ledger §6 ("Drum twenty-nine is fouled … on boxes for about a month from the 6th of the tenth month"); §11.5 (the seven drums are 19–21 and 25–28; twenty-nine is fouled, not stepped); M1.5 (its streets came off on the 6th of the eleventh). Saturday the 6th of the eleventh checks, since the 1st is a Monday. The relative clause attaches to the drum, not the streets. | Correct; date and event unchanged |
| F8 | ch. 8:95, "the night before last" | M1.3: the wharf was the 22nd–23rd of the first month, Friday into Saturday. Ch. 8 is Sunday afternoon. | Correct |
| F9 | ch. 8:349, "My own habit, that Brask was reading like a signpost." | ch. 6:329 ("It was a signpost. She had been putting one up at every floor that she stood on."). The held mark stays Perrin's: ch. 6:395 "Mine … I thought of it" and ch. 8:261/311 "You thought of it. I didn't." Jude's "four things" (`:357`) still counts four. | Correct; the overclaim is removed |
| F10 | ch. 4:7, "the twenty-fourth" | ch. 1:97 "One a day"; drum nineteen out on Tuesday the 18th (`:347`); "Six to do. Twenty tomorrow" (`:343`). Seven consecutive days end on Monday the 24th. M1.4 says "by the 25th", which is still true. No skipped day was invented. | Correct |

### 2c. Ash ledger — reconciles; nothing moved

These figures occur the same number of times in the frozen and repaired texts: 0.32, 0.16, 0.07,
0.09, 25.21, 0.57, 24.64, 15.0, 9.64, 3.84, 0.8 (three times), "sixty-four hundredths", "nine and
sixty-four", "Five and sixty-four", and "That adds" (three times).

The ch. 8 §4 entry no longer itemises the written 4.0 and 1.8 as separate figures. It reads
"Spoken for, as at the table: 5.8" (ch. 8:387).
- 4.0 + 1.8 = 5.8, which is ledger M1.2's "Spoken for" line.
- 9.64 − 5.8 = 3.84.
- Both components are still spoken in full at the table: "that's four drams" (ch. 8:159) and
  "One and eight-tenths" (ch. 8:163).

The chain reconciles end to end:

> 25.53 − 0.32 = 25.21; − 0.57 = 24.64; − 15.0 = 9.64; − 4.0 − 1.8 = 3.84. Sealed 0.8 is unopened.

No valid date, event or outcome moved. There are no real month names in `manuscript/`.

## 3. Priority 2 — One-pass clarity without reducing the story — **PASS**

- **Kellan, ch. 6 §6 / ch. 8 §2.**
  - *Removed from ch. 6:* the "weak corner" articulation, "I'll never learn that here", the nine
    rungs and nine red tags, the stepped-floor consequence and the Talley tenth-knot line.
  - *Still in ch. 8:* every removed item reappears there. "I want to know what I am" is at `:221`.
    The weak corner and "I'll never learn that here" are at `:225`. The tenth knot is at `:229`.
    The cuff, the nine red tags, the stepped floor and "Halden doesn't care" are at `:269–275`.
    Ch. 8 therefore now reveals rather than repeats.
  - *Kept in ch. 6:* the decision ("You'll have my name", `:493`), the sum weighed both ways
    (`:471–483`), "It had no shine on it whatever" (`:487`), "There was not one" (`:489`), and
    Birch's lines and Kellan's reply (`:501–503`).
  - *Seams:* the new seam at `:485–487` reads cleanly. "under the sum there was a reason that he
    had not yet put into words" sets up "It had no shine on it" and "looking for something better
    underneath" without a gap. At `:451`, "He had the figures … two of them in his cuff" leaves
    the figures unnamed on purpose, and they are inferable from the red tag at `:445–449`.
  - *Continuity:* ch. 8's "since Thursday" (`:271`) agrees with ch. 6 §6 ("on Thursday", `:417`).
    No loss, no contradiction.
- **Warrant, ch. 6 §3 / ch. 8 §2 / §4.**
  - *ch. 8 table (`:155–163`):* the one full sum stays here, with Kellan's motive.
  - *ch. 6 (`:167`, `:177`):* now "Out of five-and-twenty, if nobody lights anything tomorrow",
    and Perrin's "Then we hold less" (`:171`) still answers it. "Nineteen at the least" now leaves
    15 + 4 to the listener, but "a dram a head … four heads on a floor" sits in the preceding line,
    so it is recoverable.
  - *ch. 8 §4:* checked in §2c.
- **Ch. 7 far edge (`:155`, `:173`).**
  - "down the fall toward the river" and "on the river side of the heap" fix the downhill hem.
  - "at the head of the cloth, uphill by the thing's legs" fixes Pike, and agrees with `:133`
    ("its four feet at the head of Pike's cloth").
  - The count, the shut teeth (`:171`), "Nobody had it." (`:175`), the call (`:179`), the reach,
    the haul and the fold are unchanged. Nothing in the wharf was shortened.
- **Ch. 1 glosses (`:67`, `:69`, `:175`).**
  - *thimble:* agrees with ledger §3 ("Kiva's own weekly half dram") and ch. 8:163.
  - *doors:* agrees with bible lines 16–17 (Ember, hand door, still door).
  - *dark:* "having every door shut" agrees with the scene.
  - *catcher:* the clause agrees with how catching is staged in ch. 2 and ch. 5.
  - The Hythe stair exchange is untouched (no hunk falls in ch. 1:1–63).
- **Causal *since*.** Every replacement was read in place. None changes meaning, and none turns
  a temporal *since* into a causal one. Several unambiguous causal *since*s remain as register, as
  intended; for example ch. 2:365 and ch. 3:95.
- **Archaic numerals.** "-and-(twenty|thirty|forty|fifty)" forms fell from 24 to 16, as reported.
  Character-voice forms remain: Mara's "four-and-twenty" at ch. 1:97 and ch. 4:7, and Pike's and
  Rhea's "six-and-twenty".

Advisory notes, not defects. None blocks acceptance.
- **ch. 7:173.** "under the middle of the canvas; from where he knelt it was the far edge of his
  own cloth". Literally, a line under the middle is not at the cloth's edge, and the cloth's far
  hem is where Purvis and Hobday hold, in the next sentence. The intended sense is that the line
  is the *folding* edge, beyond the heap from Pike, which matches the laundry rule at `:161`. A
  careful reader resolves this, but it is a small middle/edge pull in the passage that was meant
  to need no re-reading. If ch. 2 is reopened, "the far edge of the fold" would remove it. That is
  optional.
- **ch. 1:97 (Mara, dialogue).** "I mean to do them as I did four-and-twenty on a wall, as I know
  of no other way" puts a manner *as* next to a causal *as*. It is a slight echo when read aloud,
  not an ambiguity that changes meaning.
- **Report bookkeeping.** Repair report §3 counts seventeen *since* replacements. The diff shows
  eighteen: ch. 1:97 carries two (→ *as* and → *because*), listed once without "×2". This does not
  affect the prose.

## 4. Priority 3 — Sentence-length range in narration (changed joins) — **PASS**

Every narration join in the diff was read for four things: grammar, referent, punctuation and
read-aloud hierarchy. The joins cover:

| Chapter | Location | Lines |
|---|---|---|
| ch. 2 | §3 | :289 |
| ch. 2 | §4 | :307–371 |
| ch. 3 | §2–3 | :57–173 |
| ch. 4 | §1 | :7, :127–131 |
| ch. 4 | §2 | :147–231 |
| ch. 4 | §4 | :413 |
| ch. 5 | §1 and §6 | :27, :523 |
| ch. 6 | §1–2 | :5–145 |
| ch. 6 | §3 | :207 |
| ch. 6 | §6 | :419–477 |
| ch. 8 | §1 | :9–95 |

- No join changes who does what or what is known.
- Pronoun ambiguity was removed where a join could have made it worse. At ch. 2:341, "The girl
  had written it down" replaces "She" in Orla's viewpoint.
- Lists became colon and semicolon series: ch. 4:131 ("four things: a letter …; a report …; a
  list; and a card") and ch. 4:199.
- Short terminal beats survive: "That was his." (ch. 6:5), "She had told nobody." (ch. 2:331),
  "There had been no roof." (ch. 3:149), "Nobody had it." and "There was not one."
- No dialogue was lengthened.
- No breathing comma was placed between a subject and its verb.
- The wharf (ch. 7 §2–4) has no rhythm edits.

Advisory notes, not defects:
- **ch. 2:337.** "…and a healer's card, and eleven weeks of nothing, and one did not hand a thing
  like that card to somebody in a sling." The last *and* opens a new clause after a list of three
  *and*-items, so a listener can briefly hear a fourth item. A full stop or semicolon before
  "one" would clear it.
- **ch. 2:307.** "because a Chair had written that she should, in a level hand under a
  certificate" puts the comma-set phrase where it can briefly attach to "should". It reads
  correctly on a second beat.
- **ch. 4:203.** Dropping the comma in "the sea came and went as she knew that the moon did"
  allows a second reading, the sea coming and going *as the moon did*. Both readings are true in
  the world, so the meaning is not damaged.

The movement-wide formula figures were not re-measured and are not required of this pass.

## 5. Decision

**One concrete defect requiring a second repair.**

- `manuscript/chapter-02.md:167`: "and on the fifth it went from under her fingers like a fish"
  must read "on the sixth" (or "on the one after"). Without it, the Low Lane count the repair set
  out to fix still contradicts itself across lines 167 and 169.

Everything else needs no further work before Movement Two context:
- Every other factual correction in repair report §2 is verified.
- The ash ledger reconciles, and no valid date, event or outcome moved.
- The Kellan, warrant, far-edge, gloss, *since* and numeral changes hold.
- The narration joins are sound.
- The frozen edition matches its recorded hashes.

The advisory notes in §3 and §4 are optional and are not conditions of acceptance. Once the
one-word fix is made and confirmed by a diff limited to `chapter-02.md:167`, Movement One can be
accepted for Movement Two context without another full recheck.

Not done here, by instruction: no prose edit, no score, no update to `AUTHORSHIP.md`, no commit,
push or publication, and no drafting forward.
