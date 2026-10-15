# Kindling 2680, Book Two — Movement Six — consolidated repair (the ending)

> Built by TAC

Date: 2026-10-15. Same-author line repair of chapters 41–48, in place. **Not rechecked, not cold-read after repair, not
accepted, not committed, not pushed, not published.** No new book, chapter, scene or Book Three work was begun.

## 0. Who, what and from what

- **Runtime-reported model: Claude Opus 5.5, model identifier `claude-opus-5-5`.** That is what the runtime states. It
  cannot be verified independently from inside the session. No subagent, other model or delegated worker read, wrote or
  edited anything. No Skill tool, Codex or OpenAI call was used.
- Session: Claude Code background job `3311fe04` (job directory `~/.claude/jobs/3311fe04`; the session link the harness
  reports is `https://claude.ai/code/session_01S5EA7cqPazi3e8eYB3RvWK`). Worked in place in the git worktree
  `/Users/drive/kindling-2680-book-02`, branch `codex/kindling-2680-book-02`. No commit, push or publish.
- Brief: delivered in-session. Its text matches `planning/OPUS-5.5-MOVEMENT-006-REPAIR.prompt.md` (164 lines), SHA-256
  `4b57c0f2cf4f76be845487c0e05fe1e08326ac747dd767d597df08031644891c`.
- Read before the first edit, in this order:
  1. `provenance/MOVEMENT-006-EDITORIAL-REVIEW.md` (all 825 lines; §3 C1–C15 and the ending table, §4, §6)
  2. `provenance/MOVEMENT-006-COLD-READ.md` (§3 items 1–10, the open cost questions and the three priorities)
  3. `provenance/MOVEMENT-006-CONTINUITY.md`
  4. `STATE_LEDGER.md` (Movement Five and Six blocks), `UNIVERSE_BIBLE.md`, `BOOK_MAP.md` (§3, §6 Movement Six, §7, §9),
     `CHARACTERS.md`, `packets/MOVEMENT-006.md`
  5. `manuscript/chapter-41.md` to `chapter-48.md`, completely and in order
- Targeted read-only checks during the repair: Marten's and Yarrow's pronouns (both "he": ch. 2, 6, 8, 9, 32); Pike's hands
  closed halfway "as they had been closed on Friday" (ch. 24); the bible's §6 limits ("It cannot be done by strangers" is a
  limit; the caller line is under "why it was not already done").
- Measuring script: `python3 -I provenance/tools/m6_metrics.py manuscript`, unmodified (SHA-256
  `958bc9aa8e066bf64570479cb2756fd176de28e45aa064512b9d4ab155136c12`). Run before the first edit and after the last. **No
  section was joined or split**, so its first-draft viewpoint map still applies and was not remapped. Extra counts
  (and-chains, phrase counts, quote parity) came from a scratch helper outside the repository that loads the script's own
  `clean`, `sentences` and `WORD` definitions so the splitter is identical.
- Frozen first draft `editions/movement-006-first-draft/`: never edited. `shasum -a 256 -c SHA256SUMS.txt` → **OK ×8**,
  before the first edit and after the last.
- Chapters 1–40: **not touched.** No located contradiction forced a fix there. (The parallel audio-clarity edits to
  chapters 11, 14, 15, 19 and 24 were committed by another session during this job, as `69ed848`; this repair neither
  touched nor reverted them.)

## 1. Priority 1 — the climax obeys its own rules (line edits; no event, outcome, time or cost changed)

| Item | Where (ch. §) | Was | Now |
|---|---|---|---|
| **Master's forty paces** (C1) | 41 §3, Yeo's plan | "The Master holds the mouth till it's back." | "The Master waits back on the outer quay till the last plant's called, well clear of the sill. Then she holds the mouth till the gate's back." |
| | 43 §4 | "past the black gate… and stopped on the stone above the dock mouth. / She stood there, high above the sill… She looked down at…" | "…and stopped well back from it, by the gate's moorings, where the black gate lay against the quay's edge…: sixty paces from the sill, where she had said she would wait. / She stood there with the harbour at her back. She looked along the quay at…" |
| | 43 §5, the map | "High above the sill on the outer quay, the Master." | "Back along the outer quay, sixty paces from the sill, the Master, waiting for the last plant to be called." |
| | 44 §5 | "On the outer quay, high above the dock mouth, the Master… came down the steps. / Kiva did not see her come down… felt the Master come down the steps" | "The Master… came along the outer quay and down the steps. / Kiva did not see her come… felt the Master come along the quay and down the steps" |
| **Cask's height** (C2) | 43 §8 | "the held water standing over her head" | "…standing level with her eyes" |
| | 43 §8 | "four feet eleven inches of it over their heads" | "four feet eleven inches of it, to their chins" |
| | 44 §0 | "This was the height of a man and as wide as a cart" | "This was taller than a child and as wide as a cart" |
| | 44 §0 | "with its water over his head" (Jude) | "with its water standing to his shoulder" |
| | 44 §2 | "a cask as tall as a man" | "a cask that stood higher than their heads where they knelt" (the catchers kneel) |
| **The Master's limit priced** (C5) | 45 §4, the gate | step back unpriced | added: "The grey across the mouth shivered from wall to wall as she went, and the flood against it came a hand nearer before it held." ("she did not move, because she could not" kept: the one pace now costs something visible) |
| | 45 §4, ten to seven | "Nobody on the dock floor said anything." | the sister, at the sill, "spoke up the dock, flatly…": "*She says she'll be late. She's saying it first.*" / "Nobody on the dock floor answered." (keeps 43:119, "if she couldn't keep to it she'd say so first") |
| **Carrow and Dray's bearing** (C7) | 43 §5 | "Further along the wall toward the Graving, above the place where the tear would be open" | "Back along the wall toward the pump house, above…" |
| **"Lying down" since the cut** (C11) | 45 §2 | "lying down since the Master's ward came up" | "lying down since the cut" |
| | 45 §4 | "lying down for forty-nine minutes" | "forty-eight minutes" (6.16 → 7.04) |
| **The second plant** (cold read P1) | 44 §2 | Wace "alone, a pace back on the dock floor"; Kiva kneels "in the slurry at the foot of the sill"; still door "into the granite at the sill's foot" (untested); her fist "at the north side, where the elder Pascoe's had been" (the younger, his sister, was on the north side) | Wace "had shut and stepped back off the sill when Pru called. Now he came up onto the granite again, a pace in from its outer edge"; new short paragraph: Kiva goes round the cask's north side through the slurry and steps up "onto the granite at its outer edge, where the gate's iron seating went into the stone, the place her two fingers had called good three minutes before. Wace was a pace behind her on the stone."; fist "at the west rim, where the cask hung nearest the sill"; knees "to the granite"; "She knelt on the sill's edge…"; still door "into the granite of the sill, into the stone she had tested". Consequential: "kneeling in mud" → "on wet stone"; "knelt in the slurry" → "knelt on the granite" (×2, the second "…soaked through from the slurry"); "from the slurry" → "from her knees on the sill"; "got up off her knees out of the slurry onto the granite" → "got up off her knees on the granite"; the first ward line now stands "on the dock floor at the sill's inner edge"; "lying on her knee in the slurry" → "lying on her knee"; 45 §4 "legs that had knelt in slurry" → "had waded slurry" |
| **The deadline** (C4h, cold read 1) | 45 §1 | Kellan: "If you lift at twenty-four, there's not." | "If you lift after twenty-four, there's not." (Mara's "by twenty-four… there's time" kept; it is the right sum) |
| **What Mara hears** (cold read 8) | 45 §0 | "and a healer's say *one,* and then *ten,* and Perrin Cade say that it was his as well" | "and then a long quiet, and then Perrin Cade's voice from the wall, declaring, and saying that it was his as well" (Aske's unraised count removed from what she hears. Noa's *cliff* is kept: 44 §2 states his voice carried out of the mouth to the basin wall, and 46 §7 has Mara say she heard it) |
| **Outside Kiva's view** (cold read 9) | 44 §2 | "On the basin wall… Perrin had his hand… Orla… The Chair… writing. / Kiva did not see any of them." | "She knew afterward that on the basin wall… Perrin had had his hand pressed hard to his side; that Orla… had not moved at all; that the Chair… had opened her ledger… and written. She did not see it." |
| **Cost of the first crossing** (cold read open question) | 46 §1, Aske at the sill | the forecast cost of the seventh never resolved | added two sentences: "The seventh's cold never started. It hadn't come up the arm when you lit again, and the second took it with it: one bill, not two, and this is it." |
| **Jude's and Gower's fists** (cold read open question) | 46 §1 | "after he had finished with Bannock." | "…with Bannock, and with Jude's and Gower's knuckles, which were white across the backs and not taken." (already implied: 46 §2 and 47 §3 show Jude's white knuckles; ledger "cold, not taken") |

## 2. Priority 2 — sums, clocks and records

| Item | Where | Was | Now | Evidence |
|---|---|---|---|---|
| Saturday's lane (C3) | 41 §3 | "Twenty-Eight had beaten Seven in a lane on Saturday" / "Halden License had beaten everybody" | "Twenty-Eight's blade had beaten Seven's catcher in a lane on Saturday" / "…beaten nearly everybody" | ch. 37: Seven won 6–5, Dray beat Kiva; Halden second in the Measure |
| C4a | 44 §3 | "made it eleven minutes ago" | "made it at eleven minutes past" | made 6.11.40; it is about 6.13 |
| C4b | 48 §1 | Carrow "eleven minutes on that seam" | "four minutes" | off the wall about 6.10; tear closed 6.14 |
| C4c | 44 §4 | "She ran forty paces up the dock floor" | "She ran up the dock floor" | caught at 34, carried 11, chalk at 45 |
| C4d | 43 §7 | "a hundred and forty paces off" | "a hundred paces off" | 43:167, 181, 225, 233, 285 all say a hundred; continuity §0 claimed this was fixed and it was not |
| C4e | 42 §1 | Lyle hurt "eight days ago" | "six days ago" (and the sentence split at the semicolon) | Skerry Pill Wed 16th; said Tue 22nd |
| C4f | 48 §4 | "Three weeks in the shop" / "like it for a week and hate it for two" | "A fortnight in the shop" / "like it for three days and hate it for the rest" | transit Fri 2nd; Meridian the 15th = 13 days. The second line changed only so the sum still holds |
| C4g | 46 §6 | Orla "Hers for a year and a half" | "Hers for a year" | "since the spring of last year" in the same section |
| C4i | 44 §2 | "six times on sanctioned masts" | "a dozen times on sanctioned masts" | ledger: thirteen gaps on sanctioned masts |
| C4j | 46 §2 | "He had combed it at the gate on the first day of the Measure" | "It had been combed at the gate the day they came" | ch. 17: a Board clerk combed it on arrival |
| C4k | 47 §8 | Pike's hands "half closed… since the second month" | "since the gate" | ch. 24: closed halfway from Friday the 4th of the third month (the brief's exact wording used) |
| Clerk's "ten days" (cold read 7) | 46 §5 | "sealed ten days before it came" | "twelve days" | sealed the 11th; slack the 23rd |
| Hart hears at noon (cold read 3) | 46 §6 | "I heard. Noa Bexley told the landing at noon." | "I thought she might. I heard both crossings called this morning, from the landing." | the line was struck at four; at noon Hart was at the box. He now learns the strike from Orla and knew the crossings from the landing, as Mara did |
| The first line of the limits (cold read 4) | 41 §3 | Perrin: "I'd want that known. It's on Rowan's sheet. It's the first line under the limits." | "It's on Rowan's sheet, under the limits." | 47:133 and 48:227 name the caller line as the first; Kiva says it at 41:243; the bible's §6 lists "cannot be done by strangers" as a limit, not the first line |
| "four girls and Yarrow" (cold read 5) | 43 §7 | "four girls and Yarrow" | "Pru and Treen and Marten and Yarrow" | the plank is four; Marten and Yarrow are both "he" |
| The daily hour (cold read 6) | 48 §6, first paragraph (before the protected span) | "Thursday evening… because it was the hour." | one sentence added: "She had let the morning's go by on the Long Quay, at Anwen's van, and the clock had a quarter to seven twice a day." | morning hour at 41 §0 and 46 §0; the van left at seven that morning. The staging and the count (ninth *no answer*) are unchanged |
| "Sanctioned" and "not sanctioned" (cold read 10) | 46 §6, the Chair's second entry | "…on the officer's warrant; read. Not an incident: not a sanctioned event, and the rate is the healer's to enforce." | "…read from the same sanctioned mast. Not an incident: the mast was sanctioned, but a warranted response is not a sanctioned event, and the rate is the healer's to enforce." | the distinction (a mast, an event) now reads as one; the precedent itself is unchanged (owner item) |
| "Wrong, twice" (C6, optional — done) | 46 §5 | Hart: "Wrong. Twice. By our own hands…" | "Wrong. By my hand, once: the ache from sixteen past to twenty-two past… By what we did, twice: from nine past, the wards and the Embers and the still doors on the mud kept Miss Dray's count… and my hand never felt that from the grating… Write both." The Clerk's record follows: "wrong in its last line, once by the hand on the grating and twice by the operation's own doing" | ch. 23:31: the paper's instrument is "the hand on the grating" |
| "The two who held it before me" (C9) | 45 §1 | "Not the two who held it before me, that I was ever told." | "Not the man who held it before me." | ch. 23: "the man who kept it before me died with his hand on this glass"; continuity §0 claimed this was removed and it was not |
| Carrow and Kiva (BOOK_MAP §9, plan) | 48 §1 | Kiva's half not shown | two lines after "That's why I wanted it.": Kiva: "Your lay's how the planks kept her count… Four of them agreeing on one voice, and holding till it was time. I had that off your floor." / Carrow: "Then we're square," | the planks' leaning together on one voice is shown in 42 §1 and 43 §8 |
| Peverell's seven columns (plan) | 48 §4 | promise (41 §3) unpaid | one clause in Mara's speech: "Peverell's already put her seven columns on it in front of the Board, as she said she would, and he's copying them in first." | reported, not staged; no new event dated |

## 3. Priority 3 — the coda's repeated shape and the house voice

**Closing restatements cut or shortened (action and final image kept):**
- **41 §4** (after the rope drill): cut the narration's lesson ("She had only been the one who could hear both gaps… somebody
  else would be able to stand there next time.") and "She had not thought of that before."; the book keeps *The call's not
  mine.* and *Somebody else will have to call it. Teach it so they can.* (cut: *It wants to be a word anybody can hear*,
  which repeats the scene's last paragraph).
- **46 §4** (Jude): cut "I think that's what it's for. The ash. I think it's for that. I'm going to find out." The scene now
  ends on the grating going "three and a quick under his boots, and two". Jude's "I'd want it said… both. In a week." kept
  (one of his four).
- **47 §3** (the yard): narration cut to "Kiva stood in the yard and watched her for a while. Then she took her book out and
  wrote"; the entry cut to *…Ivey called the pass, three strangers, a sack. Tamsin counted.* and *My sheet's wrong on the
  first line of the limits. Write it again.* (Kiva had just said the lesson aloud to Ivey; the corrected line is stated once,
  in the second edition at 48 §5.)
- **47 §7** (Perrin): ends "I'd like it known that I was nearly wrong, and wasn't." He looked at the sea. (cut: "That's a
  thing with only my name on it… That's how I know it's mine.")
- **47 §8** (Pike): "I watched yours. You watched mine." … "Twenty-six years, I've been doing it, with nobody at my far edge
  but the corner-hand." (cut: "That's the whole of it. Two people watching the other one's far edge, so neither of them has
  to." and "I'd not known it was the whole of it until tonight.")
- **48 §5** (Anwen): cut "And you're going to find out what you are on a commission. In two places. Not one of us for the
  other."; her "I want it said that I'd not have had it any other way" kept; "And I'd want you to write and tell me…" →
  "Write and tell me what you get wrong first."

**"I'd want" recast (16 of 23; kept: Jude ×4, Dray's "I'd want that clear", Rhea's "I'd want it on every card", the
Proprietor's "where it happened"):** Aske 41 §1 ("A fortnight between…"), 43 §0 ("Remember you heard me say it."); Perrin
41 §3 ×2 ("What I'd like to know is…"; the second removed with the first-line fix); Dray 42 §0 ("Put my name on whatever
gets written."), 48 §1 ("I'm telling you I asked"); the Proprietor 42 §4 ×2 ("I'd ask the same…"; "In your book, that you
asked before."); Jude 46 §4 ("Put it on my card…"); Mara 46 §5 ("Write that line as…"); Hart 46 §5 ("Write both."); Kellan
47 §6 ("I was told where I was wanted, and went. Every time."); Carrow 48 §1 ("I asked Polglase for the tape."); Rhea 48 §3
("You should know that."); Kiva 48 §3 ("I want you there."); Anwen 48 §5 (above).

**Pru "went scarlet" in ch. 48 (four uses → two):** kept 48 §0 "She had gone scarlet from the collar…" and 48 §5 "'I did
not,' said Pru, scarlet". 48 §0 "She went scarlet all over again, to the hair." → "She held the book tighter."; 48 §5
"Pru took it. She went scarlet." → "Pru took it in her capped hand and held it as though it were still warm."

**Resolution endings varied (scenes kept):** Mara 46 §7 ("I'd like both of those written…" / "You've written them." /
"I've written them." → "Both are in my book. Not yours."); Orla 47 §2 ("I'd liked to say I taught you that…", which she had
said to Hart the day before, → "Nobody taught you that on the Line."); Kellan 47 §6; Perrin 47 §7; Pike 47 §8; Carrow 48
§1 (now ends on an exchange, "Then we're square"); Anwen 48 §5.

**Summary chains split:** 47 §4 the grid order (the 85-word sentence and its 188-word paragraph → shorter sentences in two
paragraphs, wording kept); 47 §8 the householder (70); 46 §4 the water (65); 48 §2 "It looked like a seat…" (76). Also split
at their natural joins: 42 §1 (Lyle, 51), 42 §5 (testing, 54), 42 §6 (the bedstead, 72), 43 §8 (the four walls, 56), 46 §3
(two: 74 and 49), 46 §5 (the paper, 60; the Clerk's record, 83 → three sentences), 47 §3 (the yard, 59), 47 §6 (Kellan, 46),
48 §0 (the book, 55), 48 §5 (the van, 61).

**Heavy paragraphs and long speeches broken once at a gesture or pause (no words cut):** 41 §1 Aske's price (at "He did not
raise his voice."); 41 §3 the roster (at "And beside Noa…"); 41 §3 Kiva's plan (at "She looked at Yeo's lines in the
dust."); 41 §3 Yeo's map (at "The gate's floated out…"); 43 §3 the refusal (a beat added: "Out at the head of the basin the
outfalls went on pouring, four and four."); 46 §5 the Clerk's thing on no line (at "She did not change her voice."); 47 §1
Hart (at "He turned the hand over."); 47 §4 counsel (at "He looked at the Clerk."); 47 §6 Kellan (at "He looked at the
sea."); 48 §3 Kiva's first condition (at "She held the sheet in her right hand."). After the repair no paragraph containing
dialogue exceeds 150 words.

**Re-reported evidence:** the three accounts at the box (46 §5) are now one sentence naming the three sources ("…on
Graywater's officer's slate, in the Order's book in the Master's words, and on Mr. Renn's sheet of fault paper, each saying
that somebody counted and that the writer doesn't know what."). The opening of the sealed paper trimmed where it re-reported:
the witnesses at the writing, the Clerk's list of four records, Hart's restatement of the clocks for 6.08 ("Miss Rowan's
hand had it a breath before mine."), Mara's "We took it off the water at ten past and cut it… at sixteen past", Hart's
restatement of where the thing was. The verbatim reading, every line's judgment, "I've never been early, and I was early",
"not tested, by design" and the Clerk's "better record" are unchanged. The ch. 43 position map eased by two sentences (how
Kiva drew the map; "Halden's counsel had gone with his master.") with every bearing kept.

**Chapter 43's clock (C8):** "At a quarter to six Yeo had blown one long note… and everybody had gone to where they had
been put."

## 4. Word counts (`wc -w`, headings included)

| Chapter | Before | After | Δ |
|---|---:|---:|---:|
| 41 | 7,262 | 7,197 | −65 |
| 42 | 6,911 | 6,904 | −7 |
| 43 | 5,742 | 5,728 | −14 |
| 44 | 8,350 | 8,431 | +81 |
| 45 | 7,275 | 7,327 | +52 |
| 46 | 7,242 | 7,134 | −108 |
| 47 | 7,387 | 7,201 | −186 |
| 48 | 6,400 | 6,451 | +51 |
| **Movement Six** | **56,569** | **56,373** | **−196** |

Inside the packet's 52,000–60,000. No pass in ch. 44 and nothing in the lift in ch. 45 was shortened; those chapters grew only by
the located clarifications (the second plant, the Master, the sister's line).

## 5. Measures (`m6_metrics.py`, before → after; heuristic, not a gate)

| Metric | Before | After |
|---|---:|---:|
| Body words (script tokenizer) | 56,463 | 56,267 |
| Sentences | 4,781 | 4,766 |
| **All text:** mean / median / SD | 11.81 / 7 / 11.98 | 11.81 / 7 / 11.71 |
| All text: ≤5 words / ≥40 words | 38.9% / 4.6% | 38.7% / 4.4% |
| Longest sentence | 85 (47 §4) | 77 (44 §1, the threads; kept) |
| **Narration:** n / mean / median | 3,019 / 13.6 / 8 | 3,030 / 13.6 / 8 |
| Narration: ≤5 / ≥40 | 35.9% / 6.8% | 35.7% / 6.4% |
| Dialogue: mean / median / ≤5 / ≥40 | 6.9 / 4 / 59.3% / 0.7% | 6.9 / 4 / 59.3% / 0.7% |
| Dialogue share of words | 27.0% | 26.9% |
| Paragraphs / mean / **median** | 1,430 / 39.5 / **24** | 1,444 / 39.0 / **24** |
| **Share over 60 words** | 26.5% | 26.4% |
| Paragraphs over 110 words | 96 | 91 |
| Sections / mean | 55 / 1,027 | 55 / 1,023 |
| **Breaks per 10k** (internal / with chapter openings) | 8.32 / 9.74 | 8.35 / 9.77 |
| Flesch / FK grade | 93.3 / 3.2 | 93.3 / 3.2 |
| Progression hits / per 10k | 265 / 46.9 | 264 / 46.9 |
| **And-chains** (>45 words, ≥5 *and*; script splitter) | 27 | 10 |
| Viewpoint (script): Kiva | 48,218 (85.4%) | 48,010 (85.3%) |

- Viewpoint by whitespace tokens (the continuity file's method): Kiva 48,213 → **48,005**; cutaways 8,244 → **8,256** (Mara
  2,236 → 2,240; Kellan 2,740 → 2,735; Anwen 1,420 → 1,419; Orla 1,004 → 1,020; Rhea 844 → 842). Kiva **85.33%**, still inside
  the packet's 85–88%.
- The paragraph median did not move. The repair broke only the located heavy paragraphs and speeches; the median is set by
  hundreds of mid-length paragraphs that are not defects. It is not chased here.
- **The ten remaining and-chains:** nine are inside the climax passes (44:13, 44:87, 44:171, 44:181, 44:299, 44:329, 44:349
  the run, 45:41, 45:131 the count going out of the Proprietor), left whole under "do not shorten any pass in ch. 44 or the
  lift in ch. 45" and the editorial review's advice to keep 44:349 and 45:131; one (48:313, the lamps of Saltmere) is inside
  the owner-protected last section.

## 6. Phrase counts (raw, ch. 41–48)

| Phrase | Before | After |
|---|---:|---:|
| "I'd want" (excluding "I'd wanted") | 23 | **7** |
| "I'd want" (the script's lexicon, which counts "I'd wanted") | 24 | 8 |
| "did not say anything" | 21 | 20 |
| "went scarlet" (all chapters) | 5 | 3 |
| "scarlet" (all; ch. 48 alone 4 → 2) | 7 | 5 |
| "on the table" | 11 | 11 |

## 7. Requested items left unchanged, or done differently, with the reason

1. **Yeo's line (C1).** The brief's example was "She'll wait back on the outer quay till the sill's planted." Written as "The
   Master waits back on the outer quay till the last plant's called, well clear of the sill." The sill (M2) is planted at
   6.11 with Kiva's and Wace's doors in it; the cask leaves it at about 6.13 and is planted at M3 at 6.14.50; the Master comes
   down at 6.15, and 44:299 already says she "would not come down to the sill until the plant was called". "The sill's
   planted" would have put her within forty paces of two open still doors. The subject is named because "She" followed the
   gate.
2. **The Tanyard (47 §8) is protected "entire", and the brief also asks for three edits inside it:** C4k ("since the gate"),
   the householder summary chain (P3), and Pike's closing restatement (P3). All three were made, at the smallest size; the
   rest of §8 is byte-identical (checked by diff): the cellar, the far edge, "It went the whole way, this time", "That's a
   second. I'd not had a better.", the slate, the unseen line and "That's the card done".
3. **The ch. 44 and ch. 45 long sentences** (§5 above) were not split. Not shortening the passes or the lift was read to
   cover their rhythm.
4. **Dialogue length** left alone (owner ruling pending), so the median and short share do not move toward the targets.
5. **"did not say anything" and "on the table"** were counted, not targeted; one "did not say anything" went out with the 47 §3
   narration cut.
6. **Hart's "a fortnight while the sea gate's table walked"** (41 §3; editorial §5 "APPARENT", recommend "at the springs") is
   not in this brief. Left.
7. **The Clerk's "The Board has it from four places"** (46 §5) left as written; not raised by either review.
8. **44:113, the tear's close (167 words),** is narrative, not in the brief's list of heavy paragraphs. Left.
9. **The prediction's last line (C6)** was optional and was done (Hart's once/twice; the Clerk's record follows it).
10. **The daily hour** was given a reason in one sentence rather than moving the evening scene, because the last section's
    staging is protected.
11. **The first line of the limits** was reconciled by changing Perrin's ch. 41 line rather than ch. 47–48, because Kiva's own
    plan (41:243) and both later passages agree that the caller line is the first.

## 8. Owner items (not decided here; touched or left)

- **The colour "brushed twice"** (45 §2; 48 §6): untouched.
- **The certificate precedent:** untouched in substance. The Chair's second entry was reworded (§2) only so that "sanctioned
  mast" and "not a sanctioned event" read as a distinction; the second crossing still carries no Board consequence and "the rate
  is the healer's to enforce".
- **New interaction properties** (reading a count through the still door; "one hold"; Thrale's ward holding the water and the
  flood; packs keeping no count after the bank came out; no fever after two masters touching): untouched. The priced step adds
  no property; it shows the existing limit (the ward holds the flood) costing something when she moves.
- **The revised bible §6** (the caller need not have crossed): untouched; the 47 §3 entry now states only that the first line is
  wrong, and 48 §5's second edition carries the corrected line.
- **Hollis Vane's absence from the Slack:** left.
- **Whether the sentence targets govern dialogue; the progression shape and density:** carried, unchanged.

## 9. Records reconciled

- `provenance/MOVEMENT-006-CONTINUITY.md`: §0 notes on the two corrections it had claimed and which were not made until this repair;
  the §1 calendar, §2 rules, bearings and Slack table, §5 prediction table, §6 viewpoint, §7 people and §14 items reconciled; a new
  §15 summarises the repair.
- `STATE_LEDGER.md`, Movement Six block: status line; M6.1 (the sill plant on tested granite; the Thursday hour), M6.3 (the Master's
  position, her late hour said first and the priced step; Kiva's doors 6.16–7.04; the prediction's last line), M6.4 (the Chair's
  entry), M6.5 (Carrow, Peverell, Jude and Gower); new M6.9 (repair reconciliation, including the Saturday-lane line, which touches
  the Movement Five record) and M6.10 (owner items carried).
- `AUTHORSHIP.md`: a repair entry appended.

## 10. Checks

- **Frozen edition:** `cd editions/movement-006-first-draft && shasum -a 256 -c SHA256SUMS.txt` → OK ×8 (before and after).
- **Protected last section (48 §6, from the ninth *no answer* to *The disk is cold.*):** byte-identical to the first draft
  (string comparison of that span, and of everything after it). The one added sentence sits in §6's first paragraph, before the
  protected span.
- **Strengths listed in the brief:** each probed by string search after the repair; all present verbatim.
- **Quote parity** (an odd count of double quotes in a paragraph that does not open a multi-paragraph quotation), ch. 41–48:
  **0** (before: 0).
- **Chapters 1–40:** `git diff --stat` empty for them; none touched.

## 11. Hashes after the repair (SHA-256)

| File | SHA-256 |
|---|---|
| chapter-41.md | 64313e5dec406d2fa60234334f3db212f7e21b5a72a09602fdcf2da182dd3a4e |
| chapter-42.md | 7ff5d82ec7129b91ba3f522673511034a7e73ca6bd5b44527a6bc97ac91386e6 |
| chapter-43.md | 6601ea020939c9f28b9b89a8b6020cd4de60a6cb91af7e8d611115ae4fd0194c |
| chapter-44.md | e55f88e1c57ff062f7df7cae669f2002b74e30c4c1a18672a4a449b6c4bc11a0 |
| chapter-45.md | f8467d4d06ab05d22f75c7efea3c034e8b4604f7f32700a22712dfa0410e1edd |
| chapter-46.md | 3de722446b1d292259b33607c851e83d1631251e7fbca8b6e2d3435641d2f582 |
| chapter-47.md | bbe72fb2c162acab9398c4a677be7bb006a12cd63de3bb416c4726ccd0f45ce4 |
| chapter-48.md | d4d03fbe91f9cc8b2dd16b2af542d402c26207caa524a7ec81d46ee3ef579d7a |

Status: **repaired, not verified.** A separate recheck of the three priorities is owed before acceptance.

## 12. Second repair (2026-10-15)

Bounded same-author line repair from the fresh-context recheck (`provenance/MOVEMENT-006-RECHECK.md`, job `22f7111d`), brief
`planning/OPUS-5.5-MOVEMENT-006-SECOND-REPAIR.prompt.md`. **Runtime-reported model: Claude Opus 5.5 (`claude-opus-5-5`)**,
not independently verifiable from inside the session; Claude Code job `1a27a443` (a fork of job `3311fe04`), session
`https://claude.ai/code/session_015cREQVdW5hJXsrqtMtPdmj`. No subagent or other model. Not rechecked, not accepted, not
committed, not published.

- **R1** ch. 47 §8 (the Tanyard; authorised by the showrunner): Pike's hands half closed "since the gate" → "since the dressings
  came off". Matching record lines corrected: `STATE_LEDGER.md` M6.9 (citation now "(ch. 19; ch. 24)") and
  `provenance/MOVEMENT-006-CONTINUITY.md` §15.
- **R2** ch. 41 §3 (Yeo's plan): "The thing goes in past her" → "The thing goes in past where she'll stand", so the order holds
  after "The Master waits back on the outer quay…". Nothing else in the paragraph changed.
- **R3** ch. 43 §8: "four feet eleven inches of it, to their chins" → "…level with their eyes" (agrees with "level with her
  eyes" and Anwen "looking up at it").
- **R4** ch. 47 §4: "…each pump on its own cells, and kept there." → "…and each to be kept there." Wording only.
- **O1** (optional, done) ch. 48 §5: "lamps lit against the grey, slate blue." → "lamps lit against the grey. It was slate blue."
- **O2** (optional, done) ch. 44 §5: "Anwen's line stood shut on the granite" → "…on the sill's edge".
- Left untouched as directed: 43:121 ("seventy paces off on the basin wall") and 46:273 ("She had not known about the sister's
  book, or Kellan's sheet"); both go to the whole-book review.
- Checks: quote-parity scan of ch. 41–48 → **0** odd paragraphs. The frozen edition `editions/movement-006-first-draft/` still
  verifies (`shasum -a 256 -c SHA256SUMS.txt` → OK ×8).

| Chapter | `wc -w` | SHA-256 |
|---|---:|---|
| 41 | 7,199 | 39187cd04eb9b527936d09ba274380896202a40b9193e6fdd40f648de4a77850 |
| 43 | 5,729 | 28e0228f08f475bfa4dcd77ca80538733d0a73b69e84e302b4abd74f3bca8270 |
| 44 | 8,432 | aec986b8e1595681c2ab57830ce40c17badd95eef5ea37a9177b44da7efeb316 |
| 47 | 7,206 | a6f4a501b7837fec4150223a3d4e9c1ebf42ef17987e4b4d157992e542b4d0a0 |
| 48 | 6,453 | b9fba4d1a77d56751434d0d865ffbb260e8f7dcc5d19ebf4a8e30f72d86e4002 |

Chapters 42, 45 and 46 are unchanged from §11.
