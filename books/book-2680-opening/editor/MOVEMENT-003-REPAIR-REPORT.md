# Kindling 2680, Book One — Movement Three (chapters 17–24) — consolidated repair report

> Built by TAC

Date: 2026-10-11
Brief performed: `editor/MOVEMENT-003-REPAIR-BRIEF.md`
Author of the repair: Claude Opus 5.5 (`claude-opus-5-5`), Monroe Jackson 1.3 Light / O'Connor 1.3.0. Same selected author and model as the first draft. New session; no subagents; Movement Four not started.

**Status: repaired, not rechecked.** This report does not claim the movement passed. The author has not reviewed or scored the repair, beyond re-running the editorial review's measurement script and mechanical checks for leftovers. A separate targeted recheck is still owed. Nothing was committed or pushed.

Locations are `chapter:line` in the repaired files, with line 1 the chapter title.

---

## 1. Files changed

| File | Change |
|---|---|
| `manuscript/chapter-17.md` | Targeted in-place edits (4 ledger fixes, 14 narration joins) |
| `manuscript/chapter-18.md` | Targeted in-place edits (4 ledger fixes) |
| `manuscript/chapter-19.md` | Targeted in-place edits (6 ledger fixes, 17 narration joins) |
| `manuscript/chapter-20.md` | Targeted in-place edits (7 ledger and lead-in fixes, 14 narration joins) |
| `manuscript/chapter-21.md` | Targeted in-place edits: the terrace rewritten in part; the tour, Monday and the kitchen trimmed or reshaped; 18 narration joins |
| `manuscript/chapter-22.md` | Targeted in-place edits (9 ledger fixes; nothing cut) |
| `manuscript/chapter-23.md` | Targeted in-place edits and five insertions; nothing cut but the card teaser |
| `manuscript/chapter-24.md` | Rewritten whole, in place, keeping every scene and every protected passage |
| `provenance/MOVEMENT-003-CONTINUITY.md` | Reconciled to the repaired prose; new section 0 lists the changes |
| `STATE_LEDGER.md` | New closing section, "Movement Three carried state" |
| `AUTHORSHIP.md` | Movement Three repair record appended; the first-draft entry's status line now points to it |
| `editor/MOVEMENT-003-REPAIR-REPORT.md` | This file (new) |

Nothing else was written. The bible, book map, cast file, packet, both reviews, the brief, the compiled prompts and the frozen edition are unchanged.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `chapter-17.md` | 5,799 | 5,833 | +34 |
| `chapter-18.md` | 5,070 | 5,106 | +36 |
| `chapter-19.md` | 5,782 | 5,868 | +86 |
| `chapter-20.md` | 6,301 | 6,413 | +112 |
| `chapter-21.md` | 5,410 | 5,857 | +447 |
| `chapter-22.md` | 3,911 | 3,961 | +50 |
| `chapter-23.md` | 6,417 | 7,084 | +667 |
| `chapter-24.md` | 6,319 | 8,571 | +2,252 |
| **Movement Three** | **45,009** | **48,693** | **+3,684** |

No chapter is shorter. Chapters 22 and 23 keep every line of their action. **Chapter 24 grew by about a third** and is now the longest chapter in the book; section 5 says why and what could come out.

Post-repair SHA-256 values are in `AUTHORSHIP.md`.

---

## 2. Priority 1 — the calendar, counts and names

### Dates

| Was | Now | Where |
|---|---|---|
| Flask on "Wednesday the 26th" (five places) | **Wednesday the 29th** | `17:179`, `20:405`, `23:525`, `24:275`, `24:443` |
| Halden man reads the tape "on the twenty-eighth of next month" | "They were posted yesterday. So I shall be reading this one on **the first of next month**" | `24:467` |
| Weir was "a fortnight ago" from the Pit | "seventeen days ago" | `22:135` |
| Anwen at the weir: "In a fortnight" | "In a little over a fortnight" | `18:253` |
| Brask at the capstan: learned the rule "on Saturday" | "in their lane" | `23:351` |
| Kiva's log: a reason "that had won on Saturday and fouled a grid on Wednesday" | "won a lane on a Saturday and fouled a grid on a Wednesday eleven days after it" | `24:543` |
| Kiva's log: "Knee, the second" | "The knee and the rest, the thirteenth" | `24:539` |
| Mara, on Tuesday: "I had the keeper show me on Tuesday" | "a week ago today" | `21:289` |

Dates that follow from the 29th and are not written as numbers on the page: grading Thursday the 30th, the board and standings Friday the 1st, the vote Saturday the 2nd, the Old Yard Sunday the 3rd. Aske's fortnight ends on the 13th, which the page now says twice (`24:481`, `24:495`). No weekday moved and no scene moved.

The tape date assumes the coming month also has thirty days. That is the only month length the book has stated.

### Counts, elapsed time and physical state

| Item | Was | Now | Where |
|---|---|---|---|
| Crooked post | "two hundred years old" | "older than the school that had grown up round it" (no figure) | `17:67` |
| Kellan and the skin | "cut that skin once" | "met that skin twice in my life, and I was early the first time" | `17:291` |
| Kiva's cloths on the settling floor | "twice" | "three times" | `18:9` |
| Orla at the hearing | "two floors and a field" | "three floors and a field" | `19:211` |
| Rhea Sorn's light at the weir | "Eight cuts… All eight" | "Eight rungs, and seven of the cuts were hers… All seven" | `18:335` |
| Anwen behind the line | two hours forty "every time the wall took the weight" | most of it "in the dark before anything had come"; worse since the Flask stood | `18:223` |
| Jude's meets on the 13th | "five" | "four" | `19:89` |
| When Jude heard she ran dry | "since Thursday" | "since Friday" | `19:89` |
| New Lane aisle | "hardly broader than a doorway" | "an aisle of three" (paces); `19:305` already said three | `19:243` |
| Rhea and the plate | "three times, a month ago" | "four times, six weeks ago" | `23:419` |
| Field dram whole | "an hour ago"; "for ninety minutes" | "half an hour ago"; "for the best part of half an hour" | `23:213`, `24:409` |
| Walk to the table | "sixty paces" | "forty-odd paces" | `22:115` |
| Terrace vote | "fifteen people who had put up their hands" | "fifteen people, and most of them had put up their hands" | `22:139` |
| Old Four's wall | "five paces from the thing's north flank" | "five paces off the thing's southern flank, between it and their own sheet" | `22:149` |
| Countdown to the link | 30 and 28 on the hobble, 24 at the lip; cords already "on the ramp" at her *Six* | 22 and 16 on the hobble, **8 at the lip**; at *Six* her count of iron stands at one and the cords lie "at the head of the ramp" | `23:57`, `23:69`, `23:133–135` |
| Tins from 51.2 drams | "nine tins, and part of a tenth" | "eight tins, and part of a ninth" | `23:601`, `23:607` |
| Dunmore and the lamps | "saw it from the road stair" | "from the rim, halfway round to his stair, with the whole ring in front of him" | `24:283` |
| Cost of the branch | "A branch, a fortnight" | "A branch, six hours. The Pit, a fortnight." | `24:537` |

The countdown now reads: 48, 44, 40, 36 during the exchange; Vane says "thirty counts off"; four counts lost to his direction and Dray; 22 and 16 across thirteen paces; 8 at the lip; two for the call and five for her own count, so the link opens with about a grating in hand. Vane's 10:22, 10:23 and 10:24 are untouched.

### Names, pronouns and roles

- **Tolliver is now Gower** (11 uses in chapters 21–24; the first draft had 6, and Gower now speaks at the terrace and the table). **Merrin is now Edda** (5 uses). **Warden Tilling is now Warden Sedge** (1 use; a second mention became "the warden"). All three were searched as whole words in `universe/`, books 1–3, and this book's manuscript and provenance, with no match.
- **Halloran is "she"** throughout the grading scene, as in chapter 14 (`24:153–197`).
- **The infirmary healer no longer shares Halloran's description.** She is "a stout, unhurried woman with ink on her cuff, who wrote the whole time she talked" (`20:403`). The account she later sends is in that hand.
- **Healer Aske is "he"**, three times (`24:21`, `24:33`). The earlier ruling was no pronoun unless the prose needed one; this brief said to supply one where the prose was avoiding it. The choice of "he" is the author's and is easy to reverse.
- **Vane's order to Kellan** is now a field reassignment: "You've nothing here to cut. You're my Carry. Get her out." (`22:255`).

### What "Half!" means

Chapter 15, already accepted, uses the calls this way: **"Half!" names the side that earned it; "Down!" names the side that lost a fighter.** The repair keeps that and has the referee say it once before the bell (`19:255`). The three calls the cold read could not assign now read:

- `19:313`: Jude's blade scrapes a forearm; "Half! Crooked Line."
- `20:167–169`: Brask's free palm goes past the edge and lands on Jude's forearm; "Half! Stonehand. On the arm."
- `20:291`: Brask takes a hand off the poles and meets Jude's blade late, with his wrist; "Half! Crooked Line."

No score changed: 2–3, 4–7, 9–8.

### Knowledge

- **Noa.** "She has three more of those in hers" is gone. The keeper lets him in "with a grunt and a remark about his lamps," and Noa writes: "*The keeper says he wrote it down as T-0 and can't say why. Find out what a T-0 is.*" (`24:405`, `24:443`). Kiva still hides both papers from the team (`24:303`).
- **Kiva's disk page.** She writes "*Began after*," stops, crosses it out, and writes "*First felt*" (`24:143–147`). The page Orla reads says "*First felt after I shut the still door… Don't know when it began*" (`24:501`). The keeper's T-0 line is added "in Saturday's pencil," since she did not have it on Wednesday night (`24:507`).
- **Dray** was "too far away to have heard" the vote. She now says she heard Kiva call the floor dark from the rail, "and there wasn't a reserve along that rail who couldn't tell me whose notion it was" (`23:551`).
- **Mara** no longer says "I heard a girl tell eleven hundred people"; she was across the road and has it from Orla (`24:137`).
- **Anwen** cites "it likes a gate" from Kiva's own book, since she was inside the tape when Bettan said it (`20:511`).

---

## 3. Priority 2 — the dark-floor decision

Kept whole: the vote, Vane's slate speech, Druce's question about the loudest thing, "Nobody had said *nearest*," the bus, and everything from the Kiln opening to the lever.

### Before

Kiva set her mark away from "the board's feeder," then argued fifty lines later that there was nothing on the floor for a string to want. Nobody named the race. Five people and the narrator told her to leave a gate. Afterward Anwen never mentioned it again, the one dissenter had no line, Rhea did not think about her own suggestion, the eleven teams were a clause, and the link was opened before the lid was down without anyone saying so.

### After

**The false belief has one stated basis** (`21:167–185`). Gower puts the race to the company: "It's live from one end of this floor to the other, and it's a good deal handier than a kiln." Kiva reads her own weir note aloud, "half a reading, and it's against me," and turns to Bettan, who saw it. Bettan answers from what she has seen: strings stand on tram rails and drain covers and go on to whatever is lit; "There's no pattern in a bar. It's only a road for somebody else's. I'll swear to that much, and not to what I haven't seen." Vane agrees. Kiva reasons that a bus carries a tune and has none, and that the cells are over the road. Gower votes against "on a dislike." The company slate records the objection and the answer (`21:195`). In chapter 22 she remembers being "glad of the answer" (`22:135`).

**Her mark no longer contradicts her.** She keeps the heap clear of gratings and benches because "what goes down through a grating or in under a bench is swept, not tinned" (`21:117`). The geometry is unchanged: ten paces from the race, ten from the terrace, twenty-two from the lattice house.

**Hindsight and repetition cut.**

- "*Nobody could land on that*… It was an idle thought" is gone, with the paragraph that looked the shelf over a second time (`21:95`).
- Mara no longer describes the link again or adds "I don't suppose it's ever mattered" (`21:289`). The link is described once, by its keeper.
- "On Tuesday night that had seemed like most of an answer" is gone (`20:543`).
- "Bettan… was looking at the floor. Kiva thought she was looking at the cinders" is gone.
- Perrin's "The old woman said it likes a gate" is folded into Anwen's line (`20:511`).
- Monday's "Not one company tried a dark floor," and Kellan's exchange about the book, are gone. The custom is still shown in one paragraph (`21:211`).

The adult disagreement stands: Vane says he would leave a gate and writes that down; Druce points at the loudest thing; Bettan's "always leave it a gate" is still at the weir.

**One addition the owner should weigh** (`21:213`). On the Monday, Kiva thinks she sees a heap lift toward the lit wall, and one of those teams comes out at forty-nine. She does not know the gate cost the dram and leaves the *why* column empty. It makes the choice a real trade and not only a mistake. It is one paragraph and can be cut without touching anything else.

**The cost between people.**

| Brief item | What is on the page now | Where |
|---|---|---|
| What Anwen wrote | Kiva could read the list upside down on the terrace and chooses not to. At the vote Anwen turns it round: "*Tues., Kennel. Asked about the gate. Answered with the Sag.*" and "*Thurs., the Pit. Asked why they leave one. Nobody could say. Put my hand up.*" | `20:515`, `21:189`, `24:321–325` |
| One unforgiving exchange | "both times you'd your answer ready before I'd finished… I'm not going to be let off it, and I'm not letting you off it either, and a dram at par doesn't do it. I'll vote for the dram." Kiva asks what would do it. "I don't know. Not having your answer ready would be a start." Nothing is settled. Later Kiva reads each of Anwen's conditions back to her and rewrites the third. | `24:327–341`, `24:377` |
| Gower after the result | He stops at the table with the rung Rhea Sorn cut for him. He did not foresee the bus either. "I'm sorry." / "Yes. I thought you would be. It doesn't seem to be a thing I can use." | `23:611–621` |
| Rhea owns the ward slide | "That was Rhea's, and she did not dress it." She is "in no position this morning to be superior about other people's notions," and after the last rung she walks to the stretcher. Stroud confirms it from the cot. | `23:407`, `23:459`, `23:527`, `24:41` |
| Stroud and the dark floor | "They tell me the dark floor was yours." / "It was mine." / "I've six weeks of somebody else buttoning my coat in which to make up my mind about that. I'd not hurry me." | `24:41–45` |
| One of the eleven teams | A Wren House catcher from Team Twenty-Eight at the standings. His father shut the shop to watch. "I expect you are." Kiva counts the eleven lines with nothing after them. | `24:255–263` |
| Vane owns the trade | In the direction itself: "The lid's not down. I said the lid first… Pumps before doorway. I've eight still-doors on the bar to stand in it. That's the foreman's trade, and it's on the slate as his." On the slate at the table, and aloud: "The line under it is mine alone… Mr. Cade's ribs are in the sum, and they're in it under my name." Perrin: "Brask told me first. Before he asked. I'd recommend it." | `23:33`, `23:627–635` |
| Kiva records it | She realizes she had been told three times what the lever does and had not thought of it. Her book gets a heading of its own, "*The link, before the lid*," with his reason as his and "I'd have gone anyway. That part is mine." | `23:47`, `24:549` |
| The healer's account | The infirmary healer bills Orla: "strapping, twice. One opinion, which was not taken. One further fortnight, which will be." Orla has paid it. "You'll carry my crate in and out of that shed till the thirteenth. At a walk. I'd like to see anybody make a bill out of that." | `24:483–495` |

Kiva's responsibility is not reduced: her *What went wrong* column now names Anwen's two questions and her own relief at being answered (`24:533`). The professionals' is not removed: Bettan and Vane gave the answer she relied on, Rhea proposed the ward, and Vane chose the link.

The board's findings were left word for word. They do not mention the lid; the trade lives on the slate, in Vane's mouth and in Kiva's book.

---

## 4. Priority 3 — chapter 24

### Shape

| Before (9 sections) | After (8 sections) |
|---|---|
| Aske's cart | Aske's cart **and** the foot of the cart, one section |
| Foot of the cart: Mara, Orla, "Show me six" | (merged above) |
| Fever; Mara's page; keeper's book deferred to Saturday | Fever; Mara's page; **Kiva writes Orla's page alone** |
| Grading | Grading, the procedure told in narration; the reed scene whole; Kiva asks how ash is returned at par |
| The board | The board, word for word, **and** the ash office and standings, with the Team Twenty-Eight catcher |
| Ash office; Mara's keeper's book and the 2446 copy | Mara's keeper's book and the 2446 copy, deferral merged; Kiva decides what to do with them |
| The vote | The vote, with Anwen's list |
| Noa | Noa |
| Old Yard | Old Yard: the account, the page, the bearer's book, the columns |

### Announce-and-withhold

| Was | Now |
|---|---|
| Mara: "Not tonight. Saturday." then the same book on Saturday | One delivery: "I've had this since Wednesday night… I've read it three times. I'm sure of it." (`24:271`) |
| Orla at the cart: "I know there's something to know." Orla on Sunday: a thing in the stacks, "Not tonight." | The cart line stays and now has a date: "Bring me the page on Sunday, and you shall have what I've got." She pays it on Sunday. **The stacks remark is gone.** (`24:93`, `24:513`) |
| Rhea's private two-word card | Removed from this movement (`23:527`). Her memory of Ilse Corran's fist stays. |
| Halloran: "I'm not going to tell you what that means" | "I can't tell you what that means. I grade ash." She does not know. (`24:183`) |
| Vane "wouldn't tell me in a corridor" | "He doesn't know yet. It isn't a hand he's seen, and he'll not put a year on a page he can't read." (`24:525`) |

The 2446 margin is mentioned once, by Mara. In place of Orla's echo, Kiva says she will ask the Library's reader herself, alone first (`24:293–301`).

One thing resolves on the page: the healer's account.

### Kiva between the reports

She looks at Stroud's hands until she will know them again (`24:51`). She writes the disk page and corrects it (`24:143–147`). She asks Halloran a question of her own and keeps the answer for two days (`24:185–197`). She counts eleven lines on a board (`24:263`). She decides what to do with the two papers (`24:293`). She reads conditions back and rewrites one (`24:377`). She adds a heading to her own columns (`24:549`).

### Preserved, checked by search against the frozen text

A paragraph-by-paragraph comparison with the frozen chapter found these unchanged: every line Ysra speaks, from "*Was it closed*" to "I have every confidence"; "Show me six"; Perrin's "I'd like it said… that I mind" and "And I vote yes"; Anwen's three conditions; Kellan's two drams and "six goes"; the team-book entry and its arithmetic (2.0 + 1.0 + 3.0 + 2.0 + 1.6 = 9.6); Noa's "They're her numbers… I measure. I don't own"; the bearer's book and "somebody had been there before him"; and the last four paragraphs of the chapter. Three narration beats inside those passages were touched: "Vane said nothing, and inclined his head"; "Kellan wrote the last line and turned the book"; and, in the seventh-reed scene, Halloran's pronoun ("She turned the comb a little in her careful fingers"). Everything Halloran says about the reed is as it was, except that "I'm not going to tell you" is now "I can't tell you."

### The shared construction

"I want that understood" was said by four adults. It is now said by none: Druce, "You'll oblige me by knowing that" (`17:167`); Mara, "Don't read that wrong" (`21:265`); Dray, "Get that straight" (`23:555`); Aske, "Don't carry away anything kinder than that" (`24:29`). Jude's, Brask's and Kellan's uses, and one of Perrin's, were also revoiced. The wider family is down from 12 uses to 5, all Anwen's or Perrin's, which earlier rulings protect.

---

## 5. Narration, and the numbers

The brief's owner ruling asks for narration outside action back toward a thirteen-word mean and about three percent forty-word sentences, without run-ons. Measured with the editorial review's script, unchanged:

| Slice | Before | After |
|---|---:|---:|
| Narration, whole movement: mean / ≤5 / ≥40 | 10.85 / 31.2% / 0.78% | 12.03 / 29.7% / 2.00% |
| Narration, chapter 24 | 8.72 / 36.5% / 0.00% | 13.09 / 29.7% / 4.64% |
| Narration, chapter 21 | 11.22 / 32.3% / 0.35% | 13.06 / 30.3% / 1.87% |
| Narration, chapter 17 | 11.32 / 27.7% / 2.10% | 12.59 / 27.3% / 4.17% |
| Narration, chapter 18 | 12.68 / 30.2% / 2.30% | 12.78 / 30.2% / 2.95% |
| Narration, chapters 19 / 20 / 22 / 23 (means) | 10.67 / 10.94 / 10.74 / 10.72 | 11.77 / 11.82 / 10.85 / 11.01 |
| All sentences: mean / ≤5 / ≥40 | 8.46 / 44.6% / 0.38% | 9.03 / 43.8% / 0.95% |
| Flesch–Kincaid grade | 2.1 | 2.4 |
| Kiva's share | 87.0% | 87.6% |
| Sections; mean words | 59; 761 | 58; 838 |

**The aim is met in chapter 24 and close in the three other chapters without a set piece. It is not met for the movement as a whole.** The lane, the Pit and the shelf were left at fight cadence, as the brief requires, and they are half the movement. Whole-text targets are missed as before; dialogue was not lengthened.

Outside chapter 24, the lengthening is 63 sentence joins in quiet passages (chapter 17: 14; 19: 17; 20: 14; 21: 18). They change no fact. The longest sentence in the movement is 62 words and was already in the first draft; five sentences that came out over 56 words in this pass were split again.

**Chapter 24's length.** It carries most of what Priority 2 asked to be paid afterward. If the owner wants it shorter, the candidates, in the order the author would cut them, are: Kiva's exchange with Halloran about returning ash (about 130 words; the vote works without it); the paragraph in which she counts the eleven lines (about 80); and her exchange with Mara about the Library (about 60 of 170). The Anwen exchange, the catcher, the account and the columns are what the brief asked for.

---

## 6. Deliberately left unchanged, and why

- **Both fights, the weir, the shelf, and the chapter break between 22 and 23.** The brief protects them. Chapter 22 gained 50 words and lost no line of its action.
- **The tour of the Pit** (`21:3–95`). The reviews found it long. The brief asked for the idle thought and the repeated link to go, and they have. The apparatus is all used.
- **Druce's question, Vane's slate speech, "Nobody had said *nearest*," the 10:12 to 10:24 clock, the lane geometry, the 9.6 split, the 0.31 transfer.** Named in the brief as closing arithmetic or as strengths.
- **The 10:24:40 coincidence** (disk, fragment, lamps, tick). Kept as a planted pattern and not explained, by owner ruling.
- **The board's findings.** Protected. See section 3.
- **Live cords three paces below Kiva's open stance** (`23:135`), against a certificate that says three paces from open ash. The cold read asked for a deliberate decision. The board clears her because the event was struck. Not in the brief; left for the owner.
- **Brask and Rhea each writing nearly the same note** about the trial plate ("don't expect it again" / "Not to be expected twice"). Possibly intended; not in the brief.
- **Chapter headings that say "Kiva:"** on chapters with cutaways. This is the book's convention in all three movements.
- **Noa Bexley's pronoun.** The brief's Priority 1 list says "gives her that knowledge." Every earlier ruling keeps Noa he/him, so the manuscript does too.
- **Jude Talley's name.** Owner-locked. The collision was removed from the other side.
- **Blended ashcraft**, which the book map names for this movement and the draft does not contain. An owner decision in the editorial review; not in the brief.
- **Flesch grade and whole-text sentence length.** Not chased, by standing ruling.
- **Dates in the previous month** (mast six on "the twenty-eighth," the panel quenched "since the thirteenth"). Correct as they stand.
- **Movement One and Two chapters, the bible, the book map, the cast file and the packet.** Out of scope. The book map's Movement Three row still mentions blended ashcraft.

---

## 7. For the owner

1. Healer Aske's pronoun (he).
2. The three new names: Gower, Edda, Sedge.
3. The Monday forty-nine paragraph (`21:213`): keep or cut.
4. Orla's stacks remark and Rhea's card teaser are out of this movement. Both are in the frozen edition if Movement Four needs either planted here.
5. Kiva's intention to visit the Library's reader herself (`24:295`). It leans on Movement Four's opening.
6. The tape date and its thirty-day month.
7. Chapter 24 at 8,571 words.
8. The stood-down date is now the 13th, three days after Anwen leaves on the 10th. None of the six funded tries can happen with Anwen in Meridian. The page does not remark on it.
9. The standing owner questions in the editorial review's section 7 that this pass did not touch: the secondary-viewpoint roster (held at eight, none added), reading level, and blended ashcraft.

---

## 8. Frozen edition and verification

- `editions/movement-003-pre-repair/` holds eight manuscript files and `SHA256SUMS.txt`, committed at `6057f6e`.
- Before the first edit: `shasum -a 256 -c SHA256SUMS.txt` reported all eight OK, and `cmp` showed each working chapter byte-identical to its frozen copy.
- After the last edit: `shasum -a 256 -c SHA256SUMS.txt` again reported all eight OK, and `git status` shows no change under `editions/`.
- **The frozen pre-repair edition was not touched.**
- Mechanical checks run on the repaired chapters: no remaining "26th," "twenty-sixth," "Tolliver," "Merrin," "Tilling," "nine tins," "an hour ago," "ninety minutes," "three more of those," "idle thought" or "I want that understood"; all six cutaways still open on the words the review's script expects; the script runs clean.
- Not done: no review, cold read, recheck or scoring of the repair by its author; no commit; no push; no Movement Four.
