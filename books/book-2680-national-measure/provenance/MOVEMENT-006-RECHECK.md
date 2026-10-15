# Kindling 2680, Book Two — Movement Six — targeted recheck of the consolidated repair (the ending)

> Built by TAC

Date: 2026-10-15. A fresh-context, targeted check of the same-author repair of chapters 41–48
(`provenance/MOVEMENT-006-REPAIR.md`). It is not an editorial pass, a cold read or a score. No prose was edited. This report
is the only file the session wrote. Nothing was committed, pushed or published, and no work was drafted beyond chapter 48.

## 0. Who and how

- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This is what the runtime reports. The
  session cannot verify it independently.
- Session: Claude Code background job `22f7111d` (job directory `~/.claude/jobs/22f7111d`). The session link the harness
  reports is `https://claude.ai/code/session_011HWhTF4ULSybxWcxuTNTxJ`. The session is separate from the drafting session
  (job `35fbff1b`), the editorial review (job `6e915e3e`) and the repair (job `3311fe04`). It worked read-only in the
  worktree `/Users/drive/kindling-2680-book-02` on branch `codex/kindling-2680-book-02`. No subagent was used, and no other
  model, Skill tool, Codex or OpenAI call.
- **This check is same-family and fresh-context. It is not human review.** The model family is the same as the prose's
  author and the repair's author, so this check can share their blind spots.
- Inputs read:
  - the repair report, in full
  - the editorial review, in full (§3 C1–C15, §3c, §5, §6)
  - the cold read, in full
  - each frozen chapter compared with its working chapter by `git diff --no-index --word-diff=plain`, with every changed
    passage read inside its scene. The scenes read in full were 43 §4–§8, 44 §2 and the run, 45 §0–§1 and §4, 46 §1 and
    §5–§7, 47 §2–§4 and §6–§8, and 48 §1, §3 and §5.
  - the repair's diffs to `STATE_LEDGER.md` (Movement Six block), `provenance/MOVEMENT-006-CONTINUITY.md` and `AUTHORSHIP.md`
- Out-of-movement reads, limited to evidence the repair cites:
  - ch. 17:245–263 (the tin combed at the gate)
  - ch. 19:3–15 (Pike's dressings come off)
  - ch. 24:219 (Pike's hands "as they had been closed on Friday")
  - ch. 37 (the Saturday lane, 6–5)
- **Hashes:** the SHA-256 of all eight working chapters matches the repair report's §11 table, so this check covers exactly
  what the repair left. Chapters 1–40 show no diff against `HEAD`.

## 1. Priority 1 — the climax obeys its own rules: **PASS**

Each correction below was re-derived from the page. No event, outcome, time or cost was changed. Two changed joins need a
small tidy (R2, R3 in §6).

**The Master and her forty paces.**
- *Positions.* Yeo's plan (41:239) has the Master wait "back on the outer quay till the last plant's called". At 5.50 she
  stops "by the gate's moorings… sixty paces from the sill, where she had said she would wait" (43:117). The map puts her
  "Back along the outer quay, sixty paces from the sill" (43:151). 44:299 ("would not come down to the sill until the plant
  was called") is unchanged and now agrees with these.
- *The plants against her forty.*
  - The sill plank (Bannock and Wace, open from about 6.10) and Kiva's still door in the sill (6.11.40 to about 6.13) are
    at least sixty paces from her.
  - The first stake (Brask and Tolver) is twenty-five paces farther out into the basin.
  - The third plant is planted at 6.14.50 (44:401), and she comes "along the outer quay and down the steps" after it (44:407,
    409). At that point the open still door (Kiva's, at the chalk) is forty-five paces from the sill. That is outside forty,
    and its pull is still felt (44:421), as the first draft had it.
- *Result.* No still door opens within forty paces of her. **PASS.**

**When she comes down, and the step.**
- 6.15: she comes down to the sill (44:407–409).
- 6.50: "At the sill the sister turned her head and spoke up the dock… 'She says she'll be late. She's saying it first.'"
  (45:287–289). The sister stood with Kiva at ten to six (43:123), and the line keeps 43:123's "she'd say so first".
- 6.55: the one pace back now costs something visible: "The grey across the mouth shivered from wall to wall as she went,
  and the flood against it came a hand nearer before it held." (45:295). "She did not move, because she could not" (45:279)
  stands, now with a visible price for the single exception. **PASS.**

**The cask's height (4 ft 11).**

| Place | Now | Who and posture | Holds? |
|---|---|---|---|
| 43:273 | "level with her eyes" | Kiva, standing | ✓ for a girl of about 5 ft 3 |
| 43:305 | "to their chins" | Anwen and Kiva | ✗ against 43:273, **R3** |
| 44:25 | "taller than a child and as wide as a cart" | — | ✓ |
| 44:75 | "standing to his shoulder" | Jude, "a tall young man" | ✓ |
| 44:139 | "higher than their heads where they knelt" | the catchers, kneeling (44:123) | ✓ |
| 44:193, 211 | "a foot above her head", "over her head" | Kiva, kneeling | ✓ |

No line still says "over their heads" or "the height of a man".

**Carrow's and Dray's bearing.** The bearing now reads "Back along the wall toward the pump house, above the place where
the tear would be open" (43:147). The tear is at the ring, ten paces from the outfalls, and Polglase's mast is above the
first stake, toward the Graving. The bearing is now consistent. **PASS.**

**The second plant.**
- *Is the plant on tested granite?* Yes.
  - 43:243: Kiva tests the sill "on the granite between Bannock's boots and Wace's… where the iron of the gate's seating
    went into it", at about 6.08½ (the third mark had been read at 6.08, 43:235).
  - 44:185: she steps up "onto the granite at its outer edge, where the gate's iron seating went into the stone, the place
    her two fingers had called good three minutes before". About 6.11½, so the three minutes holds.
  - 44:211: the still door goes "into the granite of the sill, into the stone she had tested."
- *Can Kiva's and Wace's positions be pictured on one reading?* Yes.
  - Wace stepped back off the granite at "Far edge" (44:167). He comes up again "a pace in from its outer edge" (44:175).
  - Kiva is at the outer edge, with Wace "a pace behind her on the stone" (44:185, 201, 211).
  - She goes round the cask's north side, past the younger Pascoe. That is correct, because the north side sank with the
    younger one (44:157).
  - She takes the cask at "the west rim, where the cask hung nearest the sill". That is correct: the sill is west of the
    stake (42:317).
  - She kneels "on the sill's edge" (44:193). The first ward line takes the cask from the dock-floor side (44:241, 257, 261).
- *Follow-on wording.* "Wet stone", "on the granite", "her knees soaked through from the slurry" and "legs that had waded
  slurry" (45:309) all agree. **PASS.**

**The 24-minute deadline.** Mara (45:83): "If you've let go by twenty-four minutes past, there's time. At twenty-four, if
you've not, I'll call it off." Kellan (45:101): "If you lift at twenty-two, there's time. If you lift after twenty-four,
there's not." Both speeches now give the same limit. The sum is the slack's end at 6.30, with the still water needed to
6.28. Mara's "on my name at twenty-four minutes past six" (46:355) agrees. **PASS.**

**What Mara can hear from the landing (45:9).**
- She hears Noa's *cliff*. 44:219 says his voice "carried… out of the mouth to the basin wall", and 46:355 has her say she
  heard it twice.
- She hears Lyle's *I can't*. 44:327 says "the whole basin had heard Lyle".
- Then "a long quiet", then "Perrin Cade's voice from the wall, declaring". Perrin is on the basin wall above the first
  stake, roughly forty paces from the landing and much nearer than the sill. Aske's unraised count, from the sill (44:317),
  is no longer among what she hears. The ranges now agree with ch. 43, where Kiva on the dock floor cannot hear Perrin.
  **PASS.**

**Outside Kiva's view.**
- 44:221 now reads "She knew afterward that on the basin wall… She did not see it."
- Every other added line stays inside Kiva's view: the sister's line, the ward shivering, Aske's knuckles, Carrow, and Yeo's
  plan at the trestle.
- No section now steps outside Kiva's view. **PASS.**

**The cost of the first crossing.** 44:223 now carries the forecast ("would begin within the hour, at the knuckle… It had
not begun"). Aske settles it at 46:25: "The seventh's cold never started. It hadn't come up the arm when you lit again, and
the second took it with it: one bill, not two, and this is it." This agrees with 41:71 ("Past the elbow, five nights"). It
is resolved on the page by the healer, not left as a forecast. **PASS.**

**Jude's and Gower's fists.** 46:15 reads "white across the backs and not taken", which agrees with 44:75 and 48:241.
**PASS.**

**Kiva's doors.** 45:145 "since the cut" (the cut at 6.16, 44:479); 45:303 "forty-eight minutes" (6.16 to 7.04). **PASS.**

## 2. Priority 2 — sums, clocks and records: **FAIL on one item (R1); all others PASS**

| Item | On the page now | Re-derived | Result |
|---|---|---|---|
| Saturday's lane (41:281) | "Twenty-Eight's blade had beaten Seven's catcher… Halden License had beaten nearly everybody" | ch. 37:289 (Kiva lost the exchange to Dray), 37:307/343 (Seven 6, Twenty-Eight 5) | PASS |
| 6.13, "eleven minutes" (44:305) | "made it at eleven minutes past" | made 6.11.40; Lyle speaks after the ward line takes the cask at 6.12+ | PASS |
| Carrow's four minutes (48:57) | "four minutes on that seam" | down off the wall after the ring lifted (about 6.10, 44:91); tear closed 6.14 (44:113) | PASS |
| The run (44:349–373) | "She ran up the dock floor"; caught them at 34; walked 11 to the chalk | 34 + 11 = 45 | PASS |
| A hundred paces (43:211) | "a hundred paces off" | 10 + 40 + 45 ≈ 95–105; agrees with 43:171, 185, 289 | PASS |
| Lyle (42:169) | "six days ago" | Skerry Pill Wed 16th → Tue 22nd | PASS |
| The shop (48:211, 215) | "A fortnight in the shop" / "like it for three days and hate it for the rest" | transit Fri 2nd → commission 15th = 13 days | PASS |
| Orla (46:299) | "Hers for a year" | "since the spring of last year" (46:283) | PASS |
| Masts (44:205) | "a dozen times on sanctioned masts" | ledger: thirteen | PASS |
| The comb (46:63) | "It had been combed at the gate the day they came" | ch. 17:245–263, a Board clerk at the gate | PASS |
| **Pike's hands (47:299)** | **"half closed, the way they had been since the gate"** | ch. 19:3–15: the dressings came off at eight on **Friday** the 4th, **in the Company's van yard**, and the fingers "came about halfway… and stayed"; ch. 24:219: "as they had been closed on Friday". No gate is involved. In this book "the gate" is the Board's combing gate (46:63, 46:125, 47:357). | **FAIL (R1).** "Since the second month" was wrong. "Since the gate" names an event the cited evidence does not support, and reads opaquely. |
| Twelve days (46:259) | "sealed twelve days before it came" | 11th → 23rd | PASS |
| Hart and the struck line (46:317) | "I thought she might. I heard both crossings called this morning, from the landing." | struck at four (46:281); Hart at the grating all morning; Mara heard *cliff* twice from the same landing | PASS |
| First line of the limits (41:283) | "It's on Rowan's sheet, under the limits." | Kiva's plan names the caller first (41:249); 47:133, 48:171 and 48:233 make it the first line | PASS |
| Plank of four (43:251) | "Pru and Treen and Marten and Yarrow" | the 43 map and 44:123 | PASS |
| Daily hour (48:273) | added: "She had let the morning's go by on the Long Quay, at Anwen's van, and the clock had a quarter to seven twice a day." | van at seven Thu 1st (48:225); the ninth *no answer* is unchanged | PASS. The evening hour now has a reason. Whether it softens Hart's "same hour" lesson is a matter of taste, not a defect. |
| "Sanctioned" (46:297) | "read from the same sanctioned mast. Not an incident: the mast was sanctioned, but a warranted response is not a sanctioned event" | both crossings were read by Noa at the Board's lane mast (44:219, 401; 42:325) | PASS |
| Wrong, once and twice (46:253, 259) | "By my hand, once… By what we did, twice… Write both"; the Clerk: "once by the hand on the grating and twice by the operation's own doing" | ch. 23:31's instrument is the hand; the planks from 6.09, the pumps 6.16–6.22 | PASS |
| "The man who held it before me" (45:95) | as written | ch. 23 | PASS |

**Confirmed unchanged:**
- The tin: *Used, 1.2. Left, sealed, 0.8. Bound as before.* (one hit before and after; 48:23 "Sealed 0.8, bound as before").
- Aske's card, one in fourteen (41:77 "A fortnight between"; 47).
- The hand gone to the wrist for three weeks (46:25).
- The three clean doors, refused (43:91–109).
- The cold disk, and the hull (inside the byte-identical span, §3).
- The grid order's content: every clause of the original order is still present in 47:153–155. Only the sentence breaks
  changed.

## 3. Priority 3 — the coda and the house voice: **PASS (one split left a broken clause, R4)**

**Closing restatements:**
- 41 §4 ends on Kiva's two book lines.
- 46 §4 ends with Jude standing on a grating that "went three and a quick under his boots, and two".
- 47 §3 now has Kiva say the lesson aloud to Ivey (47:115), so the book entry (47:133) only names the wrong line. The
  corrected line appears once, in the second edition (48:233).
- 47 §7 ends "He looked at the sea."
- 47 §8 ends "I watched yours. You watched mine." and "Twenty-six years… the corner-hand."
- 48 §5 ends on "Write and tell me what you get wrong first", and then the van.

In each case the action and the closing image survive. Nothing a later scene depends on was lost:
- 48 §3's first condition restates the caller lesson in Kiva's voice.
- 46:367 ("Rhea Sorn told me at the box. Four and a rest") still holds.
- The identities in the three accounts are shown in ch. 45 (45:139 Kellan's sheet, verbatim; 45:189 Rhea; 45:315–319 the
  Master).

**Recast "I'd want":** raw count 23 → 7, not counting the one "I'd wanted". The seven kept are the ones the brief names:
- Jude ×4 (43:25, 44:75, 46:155, 46:205)
- Dray "I'd want that clear" (48:49)
- Rhea "every card" (48:157)
- the Proprietor "where it happened" (45:337)

Each recast line sounds like its speaker:
- Aske, clipped: "A fortnight between…", "Remember you heard me say it."
- Perrin, who owns "I'd like": "What I'd like to know is…"
- Dray: "Put my name on whatever gets written."; "I'm telling you I asked"
- the Proprietor, dry: "I'd ask the same, in your place."
- Jude: "Put it on my card…"
- Mara: "Write that line as…"; "Both are in my book. Not yours."
- Hart: "Write both."
- Kellan: "I was told where I was wanted, and went. Every time.", which echoes his own line before it
- Carrow, Rhea and Anwen: short and in character
- Orla: "Nobody taught you that on the Line."

**Scarlet:** used three times in all chapters (41:113, 44:115, 48:13), plus "scarlet" at 48:269. Chapter 48 now has two.
"She held the book tighter." and "held it as though it were still warm" both read cleanly.

**Split chains and broken speeches:** all were read at their joins and all read correctly, except:
- **47:153** "Each cell was to keep its own, no two alike in any house, each pump on its own cells, and kept there." In the
  first draft, "and kept there" hung on "be put on its own count". After the split it has no verb to attach to. **R4.**
- **48:227** "with its horses in and its lamps lit against the grey, slate blue." "Slate blue" now ends the sentence and can
  be read as describing "the grey". Optional, O1.

The rest are clean: 41:75–77, 139–141, 237–239 and 249–251; 42:169, 339 and 359; 43:95–99, with the new beat "Out at the
head of the basin the outfalls went on pouring, four and four."; 46:105, 117, 139, 217–233 and 259; 47:53–55, 105, 181–183
and 257–259; 48:5, 81 and 169–171. The Proprietor's quoted slip (47:183) is unchanged.

**The three accounts (46:265)** are now one sentence that names the three sources: "…each saying that somebody counted and
that the writer doesn't know what." This matches 45:189 (Rhea, "I don't know what"), 45:139 and 45:315. **PASS.**

**Lines protected word for word (string counts before → after, all 1 → 1 unless stated):**
- Bannock's "It's water" / "Tomorrow it won't be"
- Lyle's "I'm saying it before"
- Aske's ten-count, 44:315–333 (no diff)
- "It's one hold" (and "Not two", 3 → 3)
- "Twenty-two" (2 → 2)
- the prediction's six quoted lines (46:225–249, no diff)
- *Used, 1.2. Left, sealed, 0.8. Bound as before.*
- "Write that you counted, and that you don't know what."
- "the way a lamp goes when somebody turns the key the whole way down"
- "Davy never did the corners"
- "Graywater's mine. You're not."
- "That's a better first line than mine was"
- "I'm only certain I let go"
- "four seconds behind"
- "I did not"
- *Held 5.15*
- "not tested, by design"
- "I've never been early, and I was early"
- "That's a better record than most sealed papers"
- "Don't stop"
- "Then we look again, and either of us may say no" (2 → 2)

**The Tanyard (47 §8, 47:297–357).** The diff has exactly three changed lines: 47:297 (the householder chain), 47:299 ("since
the gate", see R1) and 47:345 (Pike's restatement). The rest of the section is identical, including "It went the whole way,
this time", "That's a second. I'd not had a better.", the slate, the unseen line and "That's the card done".

**The last section (48 §6).** The span from the ninth *no answer* through *The disk is cold.* (7,998 characters) is
byte-identical to the frozen draft, and so is everything after it. The one added sentence sits in §6's first paragraph,
before the span. **PASS.**

## 4. Plan payoffs

| Payoff | On the page | Result |
|---|---|---|
| Carrow ↔ Kiva, each using a piece of the other's method | Carrow uses Kiva's declared, single, read door (44:43). Kiva (48:63): "Your lay's how the planks kept her count… Four of them agreeing on one voice, and holding till it was time. I had that off your floor." Carrow: "Then we're square." This rests on Carrow's own definition of the lay at 41:323 ("You hold till the other agrees"). | PASS. Paid both ways in two lines. The connection is told rather than shown, which suits a farewell. |
| Peverell's seven columns (41:189) | 48:211, in Mara's report: "Peverell's already put her seven columns on it in front of the Board, as she said she would, and he's copying them in first." Reported, not staged; no date given; nothing conflicts. | PASS |
| Hollis Vane | Absent from ch. 41–48 (no hits). CHARACTERS.md: "Directs the Line's part at the Slack." Carried as an owner item in repair §8, ledger M6.10 and AUTHORSHIP. | Correctly left as an **owner item**; not a repair failure |

## 5. Frozen edition, measures and records

**Checksum.** `cd editions/movement-006-first-draft && shasum -a 256 -c SHA256SUMS.txt` →
`chapter-41.md: OK` … `chapter-48.md: OK`: **OK ×8.**

**Metrics spot check.** `python3 -I provenance/tools/m6_metrics.py manuscript` (script SHA-256 `958bc9aa…c12`, unchanged).
Every figure in repair §5's "After" column was reproduced exactly:

| Measure | Value |
|---|---|
| Body words | 56,267 |
| Sentences | 4,766 |
| Sentence length, mean / median / SD | 11.81 / 7 / 11.71 |
| Short (≤5) / long (≥40) | 38.7% / 4.4% |
| Longest sentence | 77 |
| Narration, n / mean / median | 3,030 / 13.6 / 8 |
| Narration, short / long | 35.7 / 6.4 |
| Dialogue, mean / median / short / long | 6.9 / 4 / 59.3 / 0.7 |
| Dialogue share of words | 26.9% |
| Paragraphs, count / mean / median | 1,444 / 39.0 / 24 |
| Paragraphs over 60 words | 26.4% |
| Sections, count / mean | 55 / 1,023 |
| Breaks per 10k, internal / with chapter openings | 8.35 / 9.77 |
| Flesch / FK grade | 93.3 / 3.2 |
| Progression hits / per 10k | 264 / 46.9 |
| Kiva viewpoint (script) | 48,010, 85.3% |
| Lexicon "I'd want" / "scarlet" | 8 / 5 |

Notes:
- There are still 55 sections, so the script's first-draft viewpoint map still lines up.
- Counting whitespace tokens with the same map reproduces the continuity and AUTHORSHIP figures exactly: Kiva 48,005 of
  56,261 (85.33%), cutaways 8,256 (Mara 2,240, Kellan 2,735, Anwen 1,419, Orla 1,020, Rhea 842).
- `wc -w` gives 56,569 → 56,373, matching repair §4 chapter by chapter.

**Quote parity, ch. 41–48:** **0** paragraphs with an odd number of double quotation marks, excluding paragraphs that open a
multi-paragraph quotation. The frozen draft also has 0. The files contain no curly quotation marks.

**Records against the surviving prose:**
- `STATE_LEDGER.md` Movement Six block: the status line reads "**Not rechecked, not accepted.**" (962). M6.1, M6.3, M6.4,
  M6.5, M6.9 and M6.10 match the page. This includes the 6.50 sister's line, the 6.55 priced pace, "since the cut" and 48
  minutes, Carrow on Tue 29th, Peverell reported on the 30th, and Jude's and Gower's knuckles.
  **One stale line:** 1100, "Pike's hands half closed since the gate (ch. 24)". Ch. 24:219 says "on Friday", and ch. 19 has
  the event in the Company's van yard (R1).
- `provenance/MOVEMENT-006-CONTINUITY.md`: the status line (8) claims no recheck or acceptance. §0's two *(repair)* notes,
  §1's Wed 23rd and Thu 1st rows, §2's 6.11, 6.15 and 6.40–7.04 rows, §5, §6, §7 and §15 match the page.
  **One stale line:** 349, "Pike's hands 'since the gate'" (R1).
  - Line 26 ("Kiva on the basin wall **seventy** paces from Thrale") agrees with the prose (43:121). See O3 for the geometry.
- `AUTHORSHIP.md` repair entry: describes itself as "Not rechecked, not cold-read after repair, not accepted, not committed,
  not pushed, not published." Its scope, word counts, viewpoint figures, quote parity and hashes match. No stale line.
- None of the three records claims a recheck, acceptance or publication.

## 6. Defects found

**Required (each a located one-clause fix; no event, time, outcome or cost moves):**

- **R1 — Pike's hands (protected Tanyard, the C4k edit).**
  - Location: `manuscript/chapter-47.md:299`, "And Pike sat on the tailboard with his hands on his knees, half closed, the
    way they had been since the gate."
  - Problem: the evidence (ch. 19:3–15; ch. 24:219) places the closing at the dressings coming off, Friday the 4th, in the
    Company's van yard. "The gate" in this book is the Board's combing gate.
  - Fix: replace only "since the gate" with "since the dressings came off" (or "since Friday the 4th"). This edit replaces
    the brief's own C4k wording, so the owner should approve it because the Tanyard is protected.
  - Record lines to match: `STATE_LEDGER.md:1100` (and its "(ch. 24)" citation → "(ch. 19; ch. 24)") and
    `provenance/MOVEMENT-006-CONTINUITY.md:349`.
- **R2 — Yeo's plan, the changed join.**
  - Location: `manuscript/chapter-41.md:239`, "The Master waits back on the outer quay till the last plant's called, well
    clear of the sill. Then she holds the mouth till the gate's back. The thing goes in past her, and down the dock floor…"
  - Problem: the inserted sentences come right before the unchanged "goes in past her". The sentence order now says the cask
    passes the Master, who by then is waiting sixty paces back. That is the very rule this priority fixed.
  - Fix: one clause. For example, "The thing goes in past where she'll stand, and down the dock floor…", or "By then the
    thing's gone in, down the dock floor, and it's planted forty-five paces in…".
- **R3 — The cask's height, the two repaired phrases disagree.**
  - Location: `manuscript/chapter-43.md:273` "the held water standing level with her eyes" (Kiva) and
    `manuscript/chapter-43.md:305` "four feet eleven inches of it, to their chins" (Anwen and Kiva). 43:261 has Anwen
    "looking up at it".
  - Problem: three heights for one cask within forty-five lines.
  - Fix: make 43:305 agree with 43:273 and 43:261. For example, "four feet eleven inches of it, as high as their faces", or
    "…of it, level with their eyes".
- **R4 — The grid order, the split chain.**
  - Location: `manuscript/chapter-47.md:153`, "Each cell was to keep its own, no two alike in any house, each pump on its own
    cells, and kept there."
  - Problem: after the split, "and kept there" has no verb to attach to.
  - Fix: "…each pump on its own cells, and each to be kept there." Wording only; the order's content is unchanged.

**Optional (not blocking):**
- **O1** — `chapter-48.md:227`: "lamps lit against the grey, slate blue." could read "…lamps lit against the grey. It was
  slate blue." or put "slate blue" back next to "The van".
- **O2** — `chapter-44.md:471`: "Anwen's line stood shut on the granite" disagrees slightly with the repaired 44:241 ("on the
  dock floor at the sill's inner edge"). The line may have stepped up in the four minutes between, so this is optional.
  "On the sill's edge" would settle it.
- **O3 (apparent; geometry the repair did not touch)** — `chapter-43.md:121`: "Kiva, seventy paces off on the basin wall". The
  Master was moved sixty paces back from the sill, so "seventy" now requires Kiva to stand on the basin wall near the mouth at
  5.50. The page places her nowhere more precisely, and the editorial review judged the line could stay. Recorded for the
  whole-book review; no fix is required.

**Outside this recheck's scope (an unchanged line, not caused by the repair; for the whole-book review):** at 46:273, "She had
not known about the sister's book, or Kellan's sheet." But at 45:315–319, the Master tells Kiva, "My sister says I did… The
man on the outfall walk will have a clerk who'll say he did… My sister's written it for me, in my words." Both lines are
first-draft text, and neither review raised the conflict.

## 7. Decision

**Defects requiring a second repair.** Four bounded line fixes (R1–R4) and the two matching record lines for R1:

1. `chapter-47.md:299`: "since the gate" → "since the dressings came off" (owner approval, as the Tanyard is protected), with
   `STATE_LEDGER.md:1100` and `MOVEMENT-006-CONTINUITY.md:349` corrected to match.
2. `chapter-41.md:239`: the order of "The thing goes in past her" in Yeo's plan.
3. `chapter-43.md:305`: "to their chins" made to agree with 43:273 and 43:261.
4. `chapter-47.md:153`: "and kept there" → "and each to be kept there".

Everything else in the repair passes:
- Priority 1's rules, re-derived on the page: the Master's sixty paces and the 6.15 descent, the step and "saying it first",
  the bearing, the second plant on tested granite, the deadline, what Mara hears, Kiva's view, the first crossing's bill.
- Priority 2's clocks and records, apart from R1.
- Priority 3's cuts, recasts and protections, including the byte-identical last section.
- The plan payoffs.
- The frozen edition (OK ×8), the metrics, and quote parity (0).

After the four edits, a confirmation diff of those lines alone is enough. No full recheck is needed. The work stays as it
is: not committed, not pushed, not published, and not accepted until that confirmation.
