# Kindling 2680, Book One — Movement Four (chapters 25–32) — repair report

> Built by TAC

Date: 2026-10-11
Brief performed: `editor/MOVEMENT-004-REPAIR-BRIEF.md` (SHA-256 `fcfca2d63c879bf8fed16291218fd8f6996edf6e3c307e135008438977afcb6d`)
Repairing author: Claude Opus 5.5 (`claude-opus-5-5`), the model that wrote the first draft. One session, a fork of the drafting session. No subagents.

**Status: repaired, not rechecked.** This is one bounded same-author pass. The author did not review, score or recheck the result. A separate targeted recheck is owed. Nothing was committed, pushed, published or narrated, and Movement Five was not started.

---

## 1. What was read

In full: the repair brief; `editor/MOVEMENT-004-EDITORIAL.md` (all 564 lines, including the method appendix); `editor/MOVEMENT-004-COLD-READ.md`.

By line lookup, to make repaired recollections agree with the page: chapter 7 lines 281–300 (what Kiva told Mara), the prologue lines 1215–1230 (the first dream), chapter 23 lines 249–256, chapter 16 lines 485–491 (where Kiva stopped asking the disk), chapter 8 lines 113–127 (Orla's form), chapter 2 lines 57 and 97 (Brannock).

The eight chapters were not re-read end to end in this session. The drafting conversation was in context, and each edit site was read on disk before it was changed.

## 2. Frozen edition

`editions/movement-004-pre-repair/` was verified against its `SHA256SUMS.txt` before the first edit (all eight OK, and each working chapter byte-identical to its frozen copy) and again after the last edit (all eight OK). It was not modified.

## 3. Files touched

| File | What changed |
|---|---|
| `manuscript/chapter-25.md` … `chapter-32.md` | 177 targeted in-place edits. No chapter rewritten whole. |
| `provenance/MOVEMENT-004-CONTINUITY.md` | Reconciled to the repaired prose. New section 0 lists every change. |
| `STATE_LEDGER.md` | Movement Four block only. |
| `AUTHORSHIP.md` | New section, "Movement Four consolidated repair." Nothing earlier altered. |
| `editor/MOVEMENT-004-REPAIR-REPORT.md` | This file. |

Not touched: the frozen edition, chapters 1–24, the prologue, the packet, the compiled prompts, both reviews, the brief, and the Movement One to Three records.

Method: every edit was an exact-string replacement that aborts unless the old text matches exactly once. No section break, scene or viewpoint was added, cut or moved. The movement still has 41 sections and five cutaways.

## 4. Word counts and hashes

`wc -w`; SHA-256 of the file bytes.

| File | Frozen | Repaired | Change | Frozen SHA-256 | Repaired SHA-256 |
|---|---:|---:|---:|---|---|
| `chapter-25.md` | 5,623 | 5,635 | +12 | `1d86df8aabb386b1c2c8559d67ca1ac2e4753e3d29498b1a0ff8b2bce6a2e777` | `d090c6fdd2bb6512a04c3a440d4ec6921c7f1147c203bd4e38cdf1c0b25ae9d1` |
| `chapter-26.md` | 5,490 | 5,564 | +74 | `3ec69353d966655bff9c1087254bac2243a19be6916e8e5783d011ccce01a5cb` | `68096648ee344869162ebef1887cd90122db18b7b1d9f0575300c3223a147315` |
| `chapter-27.md` | 5,157 | 5,218 | +61 | `ca62eebfb47bd0630b1b2c60f84c328f6cb8d3ea922f06e1a5f9f378fca273d3` | `620b3d397066f9ab1e4dcdc2a63586a8cd3a9e3592935f742e0d9b885e8a5276` |
| `chapter-28.md` | 5,007 | 4,964 | −43 | `23407b9493b0dbe863a8d5695b984a13998731e94418389aa7689d8991e9f668` | `5ac5909cdf857c29963880a4d8701b553296cba532997ada15bec847e3e5d941` |
| `chapter-29.md` | 5,526 | 5,571 | +45 | `f427a1dfff1a02a267eed041802a1e0725cffa5bca28024736fde365badb9d8d` | `48271630582a1d62b5590367f538eaf086e8437c4e523bb130dca8e2f478b3d9` |
| `chapter-30.md` | 5,951 | 6,075 | +124 | `0927e69af8755bfd06950087aff765a6953019fcf0a0a2b0ca7194498549771e` | `cecad59a7d2a4e54a357909ec16773faaba64c13b1d9398d0a269a4deff36f81` |
| `chapter-31.md` | 6,469 | 6,578 | +109 | `6c487c5f7c5803202750d13c9720c6c5b749c4ef906a6f8b6b7e73e04f2d4682` | `64017eaeaca52911fe23c77093d7205c6bd02ed3e9f563c695f9b9dc2c23dbe7` |
| `chapter-32.md` | 5,901 | 5,975 | +74 | `9f108691c6c71d92698823778b212afd197da998bad419fd5ee5031450e5592c` | `8f24f93343724b85aa0eccbad737af1039e4776476745e08940b427b21cea188` |
| **Total** | **45,124** | **45,580** | **+456** | | |

The movement grew by about one percent. Nearly all of the growth is Priority 1: sentences that state a fact the page had left out (the still door, the cause of the hand loss, the corrected hour, the matches in the Annick reading, the hum, the thread). Priority 2 and Priority 3 are close to word-neutral.

Secondary viewpoint after the repair: Rhea 1,654; Noa 1,622; Vane 1,021; Anwen 756; Orla 735. That is 12.7% (12.9% before). Kiva holds 87.3%.

## 5. Priority 1 — canon, physical state, knowledge paths, spatial referents

### 5a. The Annick comparison (chapter 31)

Annick's entry is unchanged. A script check confirms all 32 of its sentences are still present word for word.

| Site | Before | After |
|---|---|---|
| "paying attention" | "She had never said that last. She had not had it to say." | "She had said that. She had said it in those words, on the same hallway floor, to the one person who had ever asked her. 'Enormous, and paying attention.' She had thought the words were her own… one sentence could leave a person less alone and more frightened at once." |
| what the lamps did | "She had never seen what they did. She had only known that they did it." | "'Some went out. Some went white,' she had told Mara. 'It's the same every time.'" Then: "There had been a third kind. She had never told anybody about the third kind… so it was on no page of hers, sealed or otherwise. It was on this one." |
| where she first said *full* | "at a kitchen table, with her arm in a sling" | "sitting on the hallway floor at a quarter to three in the morning with a wet cloth to her nose" |
| high up | "high up, and apart, looking down at roads" | "high up, watching them come toward her and toward one another, and had never once been one of them" |
| read-aloud | Kiva's remembered speech in italics, like the notebook | Kiva's remembered speech in roman with quotation marks, three places. Only Annick's words are italic. |

True differences kept: Annick is among the lights (*mine*); Annick has no notes and no tick.

**One thing for the owner to weigh.** The color with no word for it is now a match Kiva cannot prove, because she never told anyone and so Mara's sealed page does not hold it. The brief allows it to "remain uniquely hers"; I read that as "unspoken, hers alone to know." If the owner meant that Annick's entry should not be allowed to share it, that cannot be done without altering the quoted entry, which the brief forbids.

### 5b. Located repairs

| Brief item | Where | What was done |
|---|---|---|
| Rhea names Brannock first | ch 31 | "Kiva knew him" removed. After Rhea's "Brannock": "Kiva knew the name. She had read it off a cell tag in Tallis Street in the spring… She had never seen the man." |
| "I heard him say so" | ch 31 | Brannock had not arrived when Pike said it. Now: "A hair. I can feel that through the canvas as well." (Cold read row 9.) |
| "found that out" memory | ch 32 | From "on a stair at the Kennel, with a tin under her arm" to "in the Old Yard, beside the crate, with the thing cold in her palm." |
| "the last name" | ch 31 | "I knew the last name in it before yours." |
| Sheds' hum planted | ch 29 | At arrival: "A low, even hum came out through the gates and down the hill, the sound of a great many cells all keeping one time." |
| Gate, sheet, tear | ch 30 | "a little over twenty paces above the place where it had come out"; "A tear fourteen paces below her." |
| Flask's other legs | ch 29 | "The Flask's fore legs took one step north, and another. Its hind legs did not move; the one that had come down stayed where it had come down." |
| Path to the caution and Adlam's gloss | ch 26 | Noa's recital in the yard now ends: "and the caution in small print beneath it, with what a pleasant man had said the caution meant, which was that a row of cells each tuned to its own business does not care to be taken by the collar." |
| Monday, not Tuesday | ch 26 | "Noa Bexley had been told what a T-0 was on Monday, and on Tuesday he learned what he had not been told." |
| "Friday night on a tram" | ch 26 | "the tram home from the Old Yard on Friday night" |
| Day count | ch 25 | "twenty-six clear days" |
| Knee | ch 25, 27 | Aske on the 6th: "The knee stays strapped, and I see it on the thirteenth before it lands on anything." On the 13th: he "passed the knee for landings… and told her that the strapping stayed on it until he said otherwise." Chapters 31 and 32 already had it strapped and now agree. |
| Orla owns fourteen | ch 27 | "you did the only thing I've set you that you've done. I set you fourteen before tonight; I don't count the foreman's." |
| Why no still door at the rescue | ch 30 | Three sentences after Rhea's "there isn't a still-door on my van": Kiva has one three paces off; her paper says *not Hold, not Carry,* and nothing open within three paces of a charged cell, on a street with a core under every doorstep; "Kiva kept her hands at her sides." |
| Cause of the wharf hand loss | ch 30, 32 | Chapter 30: "Four necks had been hauled shut across the crook of that elbow since half past two… over a nerve that had been emptied on Wednesday and had not finished filling." Chapter 32, Aske: "The wharf wasn't the mast… The mast leaves it hungry. The cord found it hungry." |
| Duration true and consistent | ch 32 | Pike's note said an hour because Pike saw only the wharf. Kiva: "It was longer… it was supper before it came back. Fifteen hours, about." Her reason for nearly not saying so is on the page: "An hour was a better number than the true one. It was in somebody else's pencil." Aske: "Now I've the right number, which is the only kind I can do anything with." His ruling is unchanged. |
| Thread is not the disk | ch 27 | After Orla's third rule: "She meant the lowest of the three raised lines on Kiva's chest… That was the meter. It had nothing to do with the disk, which hung on its cord beside it and was cold whatever anybody did." |
| Pike's table | ch 29 | Added to Pike: "And the last isn't ranked. It's what's written against your name, and it stands there whatever the other four say." Chapter 31's "where a company could not buy it back with all the tin on the table" now agrees with it. |

Stonehand reference (cold read row 10): "as it had gone on a Saturday at Stonehand" is now "once in the spring, at Stonehand," so it cannot be mistaken for the meet in chapter 28.

### 5c. Owner decisions applied

- **2661.** Orla no longer names a year for her Regional trial (ch 28: "at the Regional"). In chapter 26 she had been "four years without a candidate" by the autumn of 2664, which puts it in 2660, Jessamy Hart's second year. Her age and history are unchanged. The Pit's link being pinned in 2661 now has no twin.
- **The Pit interval.** Movement Four's prose already used eleven or twelve seconds. The continuity checkpoint and the Movement Four ledger block now say explicitly that this supersedes "about forty seconds." See 8a for what remains.
- **Dialogue direction.** Priority 2 was performed as the brief directs.

### 5d. Two optional items from the editorial review, taken

- ch 31, Orla: "Then they know what you are" is now "Then they know you've had it too" (editorial 4e).
- ch 32: Mara's visit to the yard was "a week and a half ago," not "a fortnight" (editorial 4a note; cold read row 11).

## 6. Priority 2 — speaking voices

A dialogue-only pass. Narration was not touched for this priority.

**Kept in the period idiom, unedited:** the Reader, Mrs. Cobb, Orla, Aske, Stroud, the sister, Adlam. Perrin's father keeps "I'd not put a thimble of it in my own kitchen."

**Returned to plainer forms:** Kiva, Anwen, Kellan, Noa, Pru, Perrin. Representative changes:

| Speaker | Before | After |
|---|---|---|
| Kiva | "I'll not do it tonight for anybody." | "I won't do it tonight for anybody." |
| Kiva | "I can't weigh it. I've no instrument." | "I can't weigh it. I haven't got an instrument." |
| Kiva | "I'd somebody else. I'd reasons… I'd not have thought of you by myself." | "I had somebody else. I had reasons… I wouldn't have thought of you by myself." |
| Anwen | "I don't think that you do." / "I thought that you might be." | "I don't think you do." / "I thought you might be." |
| Anwen | "then I should have to forgive you… I'd my hand up." | "then I'd have to forgive you… I had my hand up." |
| Kellan | "I think that it's lawful. I think that it's wrong." | "I think it's lawful. I think it's wrong." |
| Kellan | "I want to be let." / "If she'll not, I understand her." | "I want to be allowed." / "If she won't, I understand." |
| Noa | "I've not thought what to put instead." | "I haven't thought what to put instead." |
| Pru | "I've to give this back… with rather more warning" | "I've got to give this back… with a bit more warning" |
| Perrin | "I thought that I ought to say." / "You'll not stop." | "I thought I ought to say." / "You won't stop." |

**Made briefer:** Pike ("Nothing. Never have had. I catch by the cord… Two reasons to look."; "Had a tendon cut at thirty."; "I won't say they haven't."), Nairn ("I haven't forgotten…"; "I had my back to you"), Rhea ("Good. I won't ask."; "Keep both."; "Don't take it for a punishment."; "Nothing here for you to cut, and you won't be asked.").

**Preserved as the brief asks:** Perrin's "I mind" in every instance, and his "I'd like it said"; Pru's narration; Pike's "It's worth being asked back"; every line of the Reader and Mrs. Cobb.

**Counts**, by the editorial review's own ad hoc patterns (appendix of that review), over the eight chapters with asterisks removed:

| Pattern | Frozen | Repaired |
|---|---:|---:|
| "I'll not / I'd not / I've not" family | 64 | 27 |
| Possessive "I've a / I'd no" | 69 | 31 |
| A verb followed by "that" | 117 | 86 |
| "that," all uses | 824 | 780 |
| First-person "shall / shan't / should" | 29 | 20 |

These are counts, not a score. Every remaining instance of the first two patterns found inside quotation marks was checked by speaker: each belongs to one of the seven kept voices, to Perrin's father, or to "I've no ham."

**Judgment calls the brief does not settle.** Mara, Hollis Vane, Lowen Brask, Brannock and Team Twenty-Eight's catcher are in neither of the brief's lists. I lightened each a little ("We won't withdraw"; "They had a word for it"; "since I won't be here"; "she won't let me refill them"; "He says he won't shut it twice") and left their longer formal sentences alone. Mara keeps "I shall want it proved which was shut first" and "I shall answer two." If the owner wants Mara fully in one camp, that is a few lines either way.

## 7. Priority 3 — listener friction

**Narrator's label removed, behavior kept (four sites, as the brief suggests):**

| Site | Removed |
|---|---|
| ch 27, the pavement | "She had no answer ready… and it had not felt like a virtue." Now: "She had nothing to say. She had looked for something all the way from Coper Street and had found the place quite bare." |
| ch 28, the trough | "She had a name for what Kellan ought to do, and three reasons for it, and she was learning to know the weight of that in her mouth." Now: "Kiva said nothing. She trod." |
| ch 31, Mrs. Cobb | "Her answer had run out, and she let it." Now only "She stopped." |
| ch 32, Kellan | The paragraph beginning "She had three things ready." Now she only asks, "What do you want from us?" and he "had not come ready for" that question. |

Preserved: Stroud on the stair (ch 25), Edda's name held shut on the bench (ch 26), "I didn't want to be the next *nothing*" (ch 32), and Kiva's own book lines.

**Telegraphs removed.** Chapter 28, after Lowen's caution: the two sentences "She put it under Saturday, in the left-hand column… She did not see that it wanted a place on the right" are gone. The stack scene still explains it when it pays, and now names him: "She thought of Lowen Brask in a passage under a terrace…" Also trimmed, from the cold read's list: the clause in chapter 29 that announced Pike's look-round would matter "a quarter of an hour" later.

**Callbacks named (six):**

| Site | Now names |
|---|---|
| ch 25 | "Anwen had described that feeling to her on Saturday night, across the kitchen table, from the other end of it." |
| ch 26 | The unidentified coat page: "a sponsor's form, soft at the folds, that Orla had carried for four years with its second page blank, and had filled in at last in the Chair's office." (Chapter 8 has it carried four years, not a month.) |
| ch 26 | "Greta Stroud had told her on the infirmary stair" |
| ch 28 | "Aske's cart at the Pit's west gate" |
| ch 31 | The two earlier calls: "She had asked about a gate twice, in the Kennel and on the terrace at the Pit, and had been handed one of them both times." |
| ch 32 | "Mrs. Cobb on the wharf" |

Lighter echoes were left as texture.

**Year-count collisions.** Rhea's "twenty-two years" is now "ever since" (Kellan's mother keeps hers). A bearer's "Nothing, in twenty-two years" is now thirty-four. The shed foreman's "Thirty years" is "Man and boy," and Rhea's slate reason says "a shed foreman." The remaining "thirty years" belong to the Reader and to Orla.

**The calendar.** After Weighbridge the coming Sunday and Tuesday are now stated once in dialogue and once at the close.

- In dialogue, ch 32, Orla in the passage: "A watch on Sunday, and the same day a man in a black coat with a glass on your tape. The Chair on Tuesday, with a house and a street and a shelf all wanting one bag. And an Order with a letter."
- At the close, ch 32: the paragraph beginning "Kiva had the book under her arm," unchanged.
- Removed or merged: Orla's "a man in a black coat reads a tape on Sunday" (ch 31); Adlam's "on the first" (now "shortly"); the catcher's "a hearing on the second"; Noa's "on Sunday"; Ysra's "on the 3rd" in her note to Orla (now "with the rest"); Orla's list of what "that Tuesday was going to hold" (reduced to the one thing she will have to say); Vane's three Sundays (now "its next sitting. That's three days off").
- Kept: Ysra's posted notice, "Tuesday the 3rd, at nine," which is the document itself.

**The notice board (ch 32).** Halden's claim is still quoted in full, since it names Kiva. The wardens' claim and Halloran's notice are each now a sentence or two of narration. Ysra's notice, the catcher, Selka Dray's seating and Noa's null result all remain.

**Kellan's half sheet (ch 31).** Now: the two bags, the yield of 44.8, "Half of it went into the street the same night," the team's 8.4, Finch on the Circuit's card, four signatures, one on the Sag. Removed from the sheet: the casualty-reserve and schools figures and the 116.8 line, which is on the standings board in chapter 32. The ledger arithmetic is unchanged and is carried in the records.

**Protected text.** Confirmed by comparison with the frozen files: Annick's entry; Mrs. Cobb's first leaf; Ilse's reason; Kiva's fourth-column entry; and the last two paragraphs of chapter 32, which are byte-identical.

## 8. Items declined, partly done, or outside the brief

### 8a. Not possible inside the brief's scope

- **The forty-second interval outside Movement Four.** Kiva's own book line in chapter 24, the Movement Three checkpoint, the Movement Three block of `STATE_LEDGER.md` and the packet's "10:24:40" still say forty. The brief limits edits to chapters 25–32 and Movement Four's records, so I recorded the supersession there and changed nothing else. "The catcher's book will be wanted" on the 3rd; the owner should decide whether she amends that line on the page in Movement Five.

### 8b. Raised by a review, not carried into the brief, and left alone

- One rule for numbers in ledger and board lines (editorial, Priority 3).
- Chapter headings reading "Kiva:" over chapters with cutaways (cold read).
- Shortening the Brannock exchange so Mrs. Cobb arrives sooner (cold read). The exchange now carries two Priority 1 repairs, and the brief warns against compressing near Mrs. Cobb's leaf.
- Dropping the inventory paragraph at the close (cold read). The brief says to preserve the close.
- "Eight minutes to two" echoing "eight minutes to three" (cold read row 13). Left as drafted; it is the sealed hour in two records.
- The 2471 entry being read twice, once to Vane and once in the yard (editorial 4f).
- Whole-text sentence and readability targets. Not in the brief; the owner has ruled on them.

### 8c. Partly done

- **"That."** Reduced where it followed a speech or thought verb in the younger cast's mouths. It was not hunted in narration or in the seven kept voices, so the total fell by about five percent, not by half.
- **Year collisions.** Three were changed. "Twenty-six" (Pike's years, Corran's years, Noa's days, a cliff) was left; the nouns already tell them apart and they are chapters apart.

### 8d. Consequences for the recheck

- **The metrics script's viewpoint guard will fail as written.** `metrics_m004.py` identifies Noa's cutaway by its first words, "Noa Bexley had learned what a T-0 was on Tuesday." The brief required that sentence to change. The new opening is "Noa Bexley had been told what a T-0 was on Monday." Whoever reruns the script must update that one key.
- **Line numbers in both reviews no longer match** chapters 26 to 32, where lines were added or removed.

## 9. Records reconciled

- `provenance/MOVEMENT-004-CONTINUITY.md`: edition line; new section 0; the calendar rows for the 13th and for Selka Dray; Kiva's knee and hand; Orla's history note; the fourth-edition quotation; the Annick "matches / cannot prove / differs" list, rewritten; the shed foreman; the board papers; the district table; the ledger note; plants; length and viewpoint figures; elapsed-time phrases; "deliberately not done."
- `STATE_LEDGER.md`, Movement Four block: status line; calendar (Selka Dray undated); the dream's matches; the hand; the interval's supersession.
- `AUTHORSHIP.md`: a new repair section with hashes and word counts.

Movement Three's records were not edited.

## 10. Mechanical checks run (not a review)

- Frozen edition checksums, before and after: all OK.
- Annick's entry: all 32 sentences present word for word.
- Protected passages compared with the frozen files: identical.
- Quotation-mark balance: no line with an odd count in any repaired chapter.
- The idiom counts in section 6.
- Word counts and hashes in section 4.

Not run: the editorial review's full metrics script, any read-through for sense beyond each edit site, any scoring, and the targeted recheck.

## 11. Working-tree state

Uncommitted in the working tree: the eight chapters, the continuity checkpoint, the state ledger, the authorship record, and this report. During the first-draft session another process, committing under the owner's name, committed and pushed chapter files as they were written. It had not committed anything from this repair when this report was written (`HEAD` was `9d6c76f`). If it does, that is not the author's action.
