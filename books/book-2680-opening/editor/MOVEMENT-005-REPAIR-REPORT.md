# Kindling 2680, Book One — Movement Five (chapters 33–40) — repair report

> Built by TAC

Date: 2026-10-11
Brief performed: `editor/MOVEMENT-005-REPAIR-BRIEF.md` (SHA-256 `93aa7e683d6794318c8370f27009555d4940b9d42208a71b32181fecf57fd2c9`)
Repairing author: Claude Opus 5.5 (`claude-opus-5-5`), the model that wrote the first draft. One Claude Code session (`433a93b1-1ba4-4c05-9e32-7132cb480100`), new, not the drafting or either review session. No subagents, no workflow, no other model.

**Status: repaired, not rechecked.** This is one bounded same-author pass under the brief's three priorities. The author did not review, score or recheck the result, and did not reread the repaired chapters end to end. A separate targeted recheck is owed. Nothing was committed, pushed, published or narrated. Movement Six was not started. Neither review report was altered.

The session's first turn did all the reading and was interrupted before any repository file was touched. The same session resumed and made every edit. It is one repair, not two.

---

## 1. What was read

In full, before the first edit: the repair brief; `editor/MOVEMENT-005-EDITORIAL.md` (SHA-256 as read `0f29cc663050edb4c7c0108c62835cded92ec8397f449678fa5c33cf633ff7c6`); `editor/MOVEMENT-005-COLD-READ.md` (SHA-256 `820ba86d57da9381cd905232540e876001943f352027cf77a299d101f353824d`); `editions/movement-005-pre-repair/SHA256SUMS.txt`; chapters 33–40; `provenance/MOVEMENT-005-CONTINUITY.md`; `STATE_LEDGER.md`; and the Movement Four and Movement Five sections of `AUTHORSHIP.md`.

The eight working chapters were byte-identical to the eight frozen files (`cmp`, all eight), so one reading covered both sets.

By line lookup only, to anchor repaired references in text already on the page: chapter 25 (167, 199, 215), chapter 27 (79–87, 201–207), chapter 28 (369), chapter 30 (203–231, 419), chapter 31 (181), chapter 32 (9–21, 341), chapters 3 and 8 (Jessamy Hart), the Movement Four checkpoint (dates of the first four goes), and a count of how chapters 1–32 name "the Works."

Not read: chapters 1–32 beyond those lines.

## 2. Frozen edition

`editions/movement-005-pre-repair/` was verified against its `SHA256SUMS.txt` five times: at the start of the session, again on resuming, after the last prose edit, after the records were reconciled, and after the authorship entry and this report were written. All eight files were OK each time. It was not modified.

## 3. Files touched

| File | What changed |
|---|---|
| `manuscript/chapter-33.md` … `chapter-40.md` | 72 targeted in-place edits (8, 5, 5, 8, 6, 9, 18, 13). No chapter rewritten whole. |
| `provenance/MOVEMENT-005-CONTINUITY.md` | 36 edits. New section 0 lists every change; sections 1–9 reconciled. |
| `STATE_LEDGER.md` | 11 edits, all inside the Movement Five block (line 274 onward). |
| `AUTHORSHIP.md` | One appended section, "Movement Five consolidated repair." 147 lines added, none changed. |
| `editor/MOVEMENT-005-REPAIR-REPORT.md` | This file. |

Not touched: the frozen edition, chapters 1–32, the prologue, the packet, the compiled prompts, the brief, both reviews, and the Movement One to Four records. `editor/MOVEMENT-005-EDITORIAL.md` already showed as modified against `HEAD` when this session began; this session did not edit it.

Method: every edit was an exact-string replacement that aborts unless the old text matches exactly once. No scene, section break or viewpoint was added, cut or moved. The movement still has 46 sections and six cutaways. One short paragraph was moved earlier inside its own scene (5d below).

## 4. Word counts and hashes

`wc -w`; SHA-256 of the file bytes.

| File | Frozen | Repaired | Change | Frozen SHA-256 | Repaired SHA-256 |
|---|---:|---:|---:|---|---|
| `chapter-33.md` | 5,091 | 5,211 | +120 | `5281e17f923323e2caf6b0ec51c66acc46e46a20160210306bd039fd0fe845d7` | `a85120c11223b76906ec49d54ef6c6bcadafe9d2f90e8f32ef25db9ffb335b03` |
| `chapter-34.md` | 5,844 | 5,849 | +5 | `3534b5522d932feee76e8b993a48d63b792592865b03bf15726285eee317cf32` | `92ccd37798c12cf65a2cd25202e6c32b01bf8b063d6a0f23fc14a29b30c20353` |
| `chapter-35.md` | 5,703 | 5,715 | +12 | `4d579032f3b4c527f8b4ab37129f7e25d43d5575d3e0725d3bc2a051808d8106` | `2ca89608564470b1fc6602f6980904ede07d5ec3badd92720f871bac96d27cf3` |
| `chapter-36.md` | 5,764 | 5,817 | +53 | `feceff1a75401d58f1e4f5c361abc1d07e3cd552c8ee455e5c804fe69fa74ccd` | `a7447f5e648b1cf7eceaa01620e36e9f4809d7aec1cb6ed0be127e5cd2fc89b3` |
| `chapter-37.md` | 5,179 | 5,238 | +59 | `734f49c14cb94e2c402feb30ce1922f773db2ba321de2cd653c4e385bc8fd9d3` | `df3d4e59758cd08d5cdde2c3a0ab5c1426e2d8952743301387762979553475df` |
| `chapter-38.md` | 4,959 | 5,047 | +88 | `6da5913a77af4de57f94befcba77d5e6ca6407653c2826909fdfa933c4e2f9a3` | `38b1392ec4fcea2fd4f6256b0f806662b228aa7be26642b29c2c4d38914c27cd` |
| `chapter-39.md` | 6,384 | 6,555 | +171 | `b6fdda5700f577ee72028e1aa08b03c517cfe94d5b4084dc67ac9daf759a9b9d` | `7ace9058c3849434bd458e5d8f06b980cc8efcf1df0faee699a1b7a5e9a55234` |
| `chapter-40.md` | 6,699 | 6,829 | +130 | `5a2c428f2c7bfd4a78b3ab7170eb8a0f4577b13da51e9a01f56c5e6e33a29371` | `cd92f4b78c121a6c3b388246c0ae8cf94dd8f140ba0f6324dba0df90f33e0d08` |
| **Total** | **45,623** | **46,261** | **+638** | | |

The movement grew by 1.4 percent. Nothing was cut for length. About two-thirds of the growth is in chapters 38–40, where the clock, the map and the notch are stated; the rest is the stake paragraph in chapter 33 and short appositives.

## 5. Priority 1 — one physical clock and map for the Regional and the Pit

### 5a. One distance for the corner

The Pit is forty paces across with the race down the middle, and the square is eight paces on a side astride the race. Its south-east corner is therefore sixteen paces from the east wall, and eighteen from a student standing a little along it. Eighteen was the one figure of the three that the page's own map supports.

| Site | Before | After |
|---|---|---|
| ch 38, Kiva's section | "Kiva saw it from thirty paces" | "from eighteen paces" |
| ch 38, to Dray | "across forty paces a minute ago" | "across eighteen paces a minute ago" |
| ch 39, the walk | "It was eighteen paces." | unchanged |

Left alone because they measure other things: Kellan's rung "forty paces off" (the west side), Vane "forty paces off, at the load board," Perrin's forty paces to the west gate, and Kiva's "forty paces of a spring morning," which is the spring event.

### 5b. The knot clock

The brief says the rate, the budget, the knots shown, the set-up and Perrin's five minutes cannot all stand. I counted the words spoken between each pair of knot sightings and took them at speaking pace. That gives about 200 counts from the tear opening to Vane's remark, and roughly 500 more to the fall of the hold. These are estimates, not timings. The one round rate that fits all three sightings is a hundred counts a knot.

| Beat | Before | After | Knots elapsed (at 100 counts) |
|---|---|---|---:|
| Vane's remark | "Three grey knots… and a fourth was coming." | "Two grey knots… and a third was coming." | about 2.2 |
| Rate and budget | "A knot to twenty counts… I've perhaps a hundred." | "A knot to a hundred counts… I've six hundred, perhaps. Ten minutes." | |
| Limits, sponsor, healer, Chair | no clock beat | "A third knot had come clear while the three of them answered him" | 3 to 3.9 |
| Vane writes and reads | "with twenty counts going by to every knot" | "the fourth stood whole behind the frost before he held the slate up" | 4.1 to 4.6 |
| Set-up | "It took less than a minute to set" | "It took two minutes to set" | to 5.8 |
| Kiva reaches Dray | "four grey knots now, and a fifth beginning" | "five grey knots now, and the sixth all but clear" | about 5.9 |
| Exchange with Dray, catch, hold, "Back" | | unchanged | to about 7.3 |
| The hold is down | "It had seven knots. The eighth was coming up" | unchanged | |
| Perrin's section | "the best part of five minutes" | "the best part of a quarter of an hour" | |

Kept as written: the ten-count hold (Dray's "You held it ten," Vane's "held for ten," Kiva's "planted for ten counts"). With the other four figures changed it no longer conflicts with anything, and it is what makes the eleven-second interval true (5d).

On this clock the tear opens a little after 2:21, Vane speaks at about 2:25, and the catch falls at about 2:33. The slate's times (2:20, 2:21, 3:10), Aske's "half past two" and Kiva's "about half past two" all stand. No line of the consent, the set-up, the catch, the carry, the cut or the rescue was removed.

### 5c. The third rung, and where the wall stands

**The rung.** Halden's husk comes "a minute after" its rung, which is to say after the bag is sealed. Twenty-Eight's now follows the same order. Added in Rhea's section, before the shout from the Kiln: "The boy at the hem drew the neck in and called it sealed, well inside his sixty." Her inventory changes from "sixty drams lying open on a sheet for a slow sixty" to "a rung only just sealed on the third sheet." Dray's later "You've a bag open" is the husk's ash, as before.

**The wall.** This is the one place where a clause was not enough, and the owner should look at it. The first draft carried the corner four paces south-east, out along the diagonal. Both walls of the hold swing outward when that corner moves, and they cross every point near the old corner, where Dray lies and Perrin and Marten kneel. Brask has just said that hands go into that wall.

The repair carries the corner **four paces east, along the line of the hold's south side.** The south wall then stays exactly where it stands and only lengthens. Only the east wall swings, across cinders that nobody is on. It is still four paces outward.

| Site | Before | After |
|---|---|---|
| Kiva's proposal | "go with the throw, four paces out, that way." She pointed south-east, across empty cinders. | Adds "A curved ward turns a shove, and I'd bend mine to turn that one east." She points "east, along the line of the hold's south side." Adds "The south wall stays where it stands, and she's on the open side of it." |
| Dray on the ground | "with her red head on the cinders" | "with her red head to the south, on the open cinders" |
| Kiva's stance | "a pace from her hip, on the south-east side" | "on the east side, facing the way that she meant to go" |
| Perrin and Marten | "Neither of them said a word." | Before it: "They were both south of the white line, on the open side, where the wall would not cross them when its corner went east." |
| Perrin's order | "along the ground; we don't lift till she's ten paces off" | "along the ground, straight back from the wall; we don't lift…" |

**The outward force.** The brief allows one clause. The clause is Kiva's, above. It rests on what chapter 36 already shows: the sandbag comes from her left, the curve of the ward turns it round her shoulder and into her back, and it "aimed her at the post." At the Pit the cord's north leg rises on her left, the ward is at her left hip, and she faces east. It is the yard's geometry turned a quarter. Every count of the catch, carry and plant is unchanged.

A side effect worth noting: Dray's eyes are "fixed on something behind him and to his left" while Perrin has his back to the hold. With the corner planted to the east, that is where Kiva stands.

### 5d. The notch, the eleven seconds and the lamps

By the page's own counts, eleven seconds after the second cliff is the instant Kiva says "Back": one count to the plant, ten of hold. The first draft showed the lamps a minute or more later, and had Noa and Adlam describe a floor with nothing lit at a moment when three blades were cutting.

- **The lamps move to that instant.** The paragraph "every lamp on the rim of the Pit… like forty eyes opening and closing" now follows the three cuts and the fall of the frost: "In that same breath every lamp on the rim of the Pit had shown a point of light, once, and gone out. She had caught it at the edge of her eye." Its wording is otherwise the first draft's.
- **Vane's question stays where it was,** after the string is on Anwen's gate: "He had a string on a gate now, and breath to ask. 'The rim. As she said *back.* Did I see that?'" The noise in the terraces "had begun when the lamps winked, and it had not stopped."
- **Noa now describes the pens as they were.** "That's the instant you said *back.* Three of those pens were blades cutting a post. Four were wards bringing up a gate. Two were running with a casualty, and one was the casualty. Five were standing dark against a wall. One was you, with everything just shut. It's the same hair on every one, lit and dark alike." That is sixteen.
- **Adlam's letter** says he "saw sixteen pens move together, on hands lit and dark alike."

The notch is kept as evidence and is stronger for it, as the editorial review suggested. The dead ring is unchanged: the race was dropped at 2:21 and the keeper says so.

### 5e. Rhea's stand

| Site | Change |
|---|---|
| ch 38, Kiva's section, after "shouting about corners." | "Nor did the Torch's *stand* reach her as an order. It came across the floor tangled in Kiva's own shout, when the boy's hand had already begun to fall." |
| ch 40, the slate | "The foreman had not called a stand. **The safety officer called one to that team as the catcher's hand fell, too late to govern.** The remark is the event's." |
| ch 40, Vane to Dray | "A Torch keeping a floor safe may stand any student on it, and Sorn did, and it reached you with your foot already going down." |

So the page now says what authority the Torch had (she may stand any student on a floor she is keeping safe) and why the order did not govern (it arrived on a falling hand). Rhea's shout in her own section is untouched. Dray's account, that she was listening to Marten, stands.

### 5f. Anwen's interval

Mace's "best part of twenty minutes" could not be the whole time: the gate goes up at about 2:34 and Anwen is still calling the step for Seven's rung at half past three. The repair names the interval he is measuring: "from the fall of that hold until the tear was shut, the best part of forty minutes." That is the stretch before any blade was free to cut on her gate. "At the end" becomes "at the south end," which is what chapter 39 shows and removes a time-or-place ambiguity when heard.

## 6. Priority 2 — canon, state and knowledge paths

| Brief item | Where | Before | After |
|---|---|---|---|
| Perrin's clearance date | ch 38 | "had been passed to the shoulder on Wednesday" | "had been passed to the shoulder for a fortnight and more" (agrees with ch 36, the 29th of the eighth month, and with Gerald) |
| Perrin's true first | ch 39 | "the first weight that he had put above his own waist since the twenty-ninth of the fifth month. It went onto his shoulder…" | "She was the first person that he had lifted since the twenty-ninth of the fifth month. Gerald did not count, and nor did a dummy on a ladder. The weight of her went onto his shoulder…" The joy, "he could have sung" and the back-turned carry are untouched. |
| Counted goes | ch 35 | "we've two counted goes that'll never be six" | "five counted goes" |
| Crossings since the stack | ch 33 | "I've done two since that were the dear kind, and one of them I chose…" | "I've done one since that was the dear kind, and I chose it…" (the stack was the 18th; the dear ones were the 15th, before, and the 20th, after) |
| Thirteen | ch 34 | "a girl of fourteen in the house" | "a girl of thirteen" |
| Kellan's question | ch 37 | "How often are you let?" / "One in a week." / "And that was—" | "Then a go that doesn't land still spends the hand." / "It spends it the same." / "And you've one in the week. So that was—" Then: "I didn't know it took the week whether you landed or not." |
| Anwen's half sheet | ch 35 | "The third had come on Thursday." | "The third had come on Thursday the fifth, and she had carried it a fortnight." |
| Rhea's burned card | ch 40 | "I burned that card." | "I burned that card. The one with two words on it about you." (chapter 31, line 181) |

**Which Works.** Chapters 1–32 use the bare "the Works" mostly for the municipal body and "the Halden Works" for the house. Movement Five had the bare form for both.

| Site | Now |
|---|---|
| ch 33, the notice under the weight; Noa on the recorder | "the Halden Works' notice"; "a recorder of Halden's own" |
| ch 34, Adlam's first words; the refinery gate and its device; "as the … wanted a bag" | "The Halden Works is grateful"; "the Halden refinery gate"; "the Halden Works' device"; "as the Halden Works wanted a bag" |
| ch 36, Mara's practical | "the examiners' room at the Municipal Works" |
| ch 39, Birch; Adlam to the keeper | "the Halden Works' license yard"; "The Municipal Works has a bank of four-and-twenty across the road, in the Ferren pump house" |
| ch 40, the slate; Adlam at the load board | "that is the Municipal Works' to enter, and I have sent to tell them so"; "It was Halden's glass that had found it. He inclined his head." |
| ch 40, the pot; Noa on the letter; Mara twice; Kellan's letter | "The Halden Works does not object"; "not Halden's"; "It's the Municipal Works'"; "the best of the Municipal Works"; "The Halden Works releases Mr. Renn" |

The pump bank that is in step is the Municipal Works'. Halden's man found it and does not own it.

**Knowledge paths.** Each uses a person or paper already in the scene.

| Who knows what | Path now on the page |
|---|---|
| Selka Dray, Hart's hand (ch 33) | "the thing that ended Jessamy Hart's hand at the Regional. Marten had that story from the Wren House; they tell it to anybody who's to stand a Bench." |
| The Chair, the night clerk R. (ch 40) | "a night clerk called R., whose margin Mr. Bexley copied into the note that I have on file" |
| Anwen, E.K.'s lost column (ch 36) | "Perrin told me about the watch officer's ledger, at the Sag." Perrin heard Orla quote E.K. in the yard (ch 28) and took the book to the Sag on the 30th. |
| Vane, the same sentence (ch 39) | "and the Reader told me that somebody had tidied it away." The phrase is the Reader's, said to Vane in chapter 27, which is why he and Anwen share it. |
| Rhea's "first-year with wax on her back" (ch 38) | "Finch had taught her to, on the Weighbridge, sitting on a curb with wax all down her back." (chapter 30, line 207) |

**Other located slips.**

| Slip | Where | Change |
|---|---|---|
| "*Sedge!*" heard as a call to someone | ch 38 | "It was a shout from the Kiln, and the name was the shouter's own, given as a hand gives it before a report." |
| T-0 opaque | ch 39 | "T-0. Lit, and nothing feeding it. I'll write it…" |
| "Dane" opaque | ch 36, ch 39 | "not Orla either"; "Orla's shouting it from the rail" (the team calls her Orla elsewhere) |
| "night hand" against Movement Four's "record hand" | ch 33, ch 36 | "the old record hand, the one the night clerks wrote"; Bly's line: "I put this in the record hand" |
| Pettit moved to Carry, then takes a husk | ch 38 | "Kellan took it on the cloth. Pettit carried a dummy across the race" |
| "five people and a brass weight" | ch 35 | "three people" (Kellan, Anwen, Perrin) |
| Rhea's second "on a sixth rung" | ch 35 | "on a fifth rung" (chapter 30: a full second, then a second and two) |
| "seven times on a mast" | ch 37 | "six times on a mast, and a seventh as the back half of a longer thing" |

**Records owed a correction** (editorial section 3): the checkpoint no longer says the knee is unmentioned after the 3rd; Pettit's kill is corrected; "about 2:25" now names Vane's remark and the catch is "about 2:33."

## 7. Priority 3 — handholds for a one-pass reader and listener

**The stake in chapter 33.** One paragraph, after "He had never read to the watch." and before the room's customs:

> He knew what a reading could come to. The seven might vote the plate back into its box, for cause written, and the cause would be the line that he was about to read. A girl of seventeen had worn that small cold disk on a cord for four years. It was the one thing that anybody had trusted her with before they knew what she was. If the vote carried, he was the officer who would have to go and take it off her neck.

"Four years" is chapter 32's figure. "Before they knew what she was" is the appointment of 2669. The last sentence is what Vane himself promises Mara later in the chapter. The editorial review suggested reordering the scene instead; the brief asks for the stake to be stated, so nothing was moved.

**Lane scoring, once.** In Jude's chalk talk (ch 36), before any lane: "Circuit rules: three for the litter over your own line, one for a down, and the most points over the three carries goes through." These values are taken from the scores already on the page. They fit all six carries (4–0, 4–2, 4–1; 2–3, 1–4, 3–1), the first Halden carry being a scramble settled on downs with no litter home.

**The aggregate, as little as needed.** Also in the chalk talk: "Every board's marked by place, sixteen for the first four down to one for the last, and the three are added." And at noon on Saturday, Jude: "And Old Four's second, that we put out at ten yesterday. A first on any board's sixteen marks, and they had one this morning." I checked that the page's results can all hold under this rule (Seven sixth after two boards, sixth on the Carry, fourth by one mark; Old Four second after losing its first lane; Twenty-Eight third). They can: at least one consistent set of places exists. It is not on the page, and no further standings were printed.

**The lane counter.** Second carry against Old Four: "He had a wall on his shoulder, and this time he had walked into her stop before he knew that it was set. A man who is leaning cannot slide out from under what he carries." In the first carry Brask stopped a foot short of her and slid the wall off; this says why he cannot do it again.

**Names where a description stood.**

| Site | Before | After |
|---|---|---|
| ch 36, "passengers" | "A square man had said it to her in a hall yard" | "Pike had said it to her in the Graywater hall yard" |
| ch 36, Orla's cutaway | "as a woman in a work apron had told her months ago" | "as Mara Rowan had told her months ago, in a work apron" |
| ch 37, the benches (twice) | "a girl with cropped red hair"; "the red-haired girl" | "Selka Dray… her cropped red head bent over it"; "Selka Dray" |
| ch 33, Orla on the Chair | "asked to sign his entry" | "asked to sign Jessamy Hart's entry" |

**Heard referents.** "from this Thursday I draw its stipend" (ch 34); "Tuesday, isn't it? The sixth of the six." (ch 35).

**Figure clustering.** One site, the worst in the front half (ch 33): "Kiva had a week's ration in her, and thirty-one hundredths out of a glass with four names on it, and there were ninety-four left when that was gone" is now two sentences that say what the figures are. The paper trail, the seven rulings, the placement argument, the stack and every ledger and tape entry are as drafted.

The elders' manner was not touched, and no dialogue-style pass was opened.

## 8. Protected text

Checked by exact-string count against the frozen files; each is present once in both: "I'm frightened… I'd like that written as well" and "Then yes."; "Ask me."; "Mine," said Anwen, and went; "*Mine.*"; "She was counting in fives. Brask had it in fours."; Perrin's list line ("…and I'm putting it on the list"); "I can hold both. I've been practicing."; "the stack had ever come to her dressed as thrift"; Aske's "That's gone."; "*Rowan, K. Catcher. Hand as before.*"

Perrin's section still has him forbidden to look, standing with his back to it and shouting "Clear!" without turning round. The causal chain is unchanged: Kiva's called corner on Friday, Dray's cut on her catcher's word, the cord, the strike, the five refusals, the direction with cost first, the catch, the carry, the plant, the rescue, the cut on "back," the gate, the closing.

## 9. Formula measurement

Kept apart from the repair. Nothing was edited to move a number.

**Method.** One stdlib script, `metrics_m005.py` (SHA-256 `39339c2a0c51e5678c4d370df9c8ac326a10ab13b224aec391afe706e1b3f67e`, printed in the appendix). It loads the Movement Three script's definitions unchanged; that script loads Movement Two's, which imports Movement One's. The four earlier scripts were re-extracted from the appendices of the four editorial reviews and their hashes match those recorded there (`462e9ac6…`, `08a6f5b2…`, `e07e81fb…`, `17665a6a…`). So Movement Five is measured with the same definitions as Movements One to Four:

- *Words:* the token regex `[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*`. Asterisks and underscores are removed first. Headings are dropped.
- *Sentences:* a sentence ends at `.`, `!` or `?` (plus closing quotes) followed by whitespace and a capital, digit or opening quote. A lower-case continuation after a closing quote does not split, so a line of dialogue and its tag are one sentence. Listed abbreviations ("Mr.", "Mrs.") and single capital initials ("K.") do not split. "Tues. and Thurs." does not split, because the next word is lower-case. A paragraph end always ends a sentence.
- *Syllables:* the heuristic vowel-group estimator from the Movement One script. Names and system terms are not special-cased.
- *Flesch Reading Ease and Flesch–Kincaid grade:* the standard formulas over those counts.
- *Paragraphs:* written paragraphs, split on blank lines. *Sections:* blocks between `---` rules.
- *Viewpoint:* by section, identified by reading and guarded in the script by each section's first words. The six secondary sections are Vane (ch 33, first), Kellan (ch 34, third), Anwen (ch 35, second), Orla (ch 36, fifth), Rhea (ch 38, fifth), Perrin (ch 39, third).
- *Narration, speech, ledger:* the rule used since Movement One's recheck. Any sentence containing a quotation mark is speech; a paragraph wholly in italics is ledger.

**Coverage.** All eight chapters, complete, frozen and repaired. The frozen run was made on copies of the frozen files placed outside the repository; their hashes match `SHA256SUMS.txt`.

| Measure | Target | Frozen | Repaired |
|---|---|---:|---:|
| Word tokens | — | 45,549 | 46,187 |
| Sentences | — | 5,026 | 5,067 |
| Mean sentence length | 14.6 | 9.06 | 9.12 |
| Median sentence length | 11 | 7 | 7 |
| Spread (population s.d.) | ~26 | 7.67 | 7.69 |
| Sentences ≤5 words | 27.7% | 42.5% | 42.2% |
| Sentences ≥40 words | 3.3% | 0.40% | 0.39% |
| Longest sentence | — | 53 | 53 |
| Syllables per word | about 1.41 implied | 1.228 | 1.228 |
| Flesch Reading Ease | 72.3 | 93.8 | 93.7 |
| Flesch–Kincaid grade | 6.8 | 2.4 | 2.5 |
| Written paragraphs | — | 1,623 | 1,624 |
| Mean / median paragraph | 26.8 / 18 (pause-derived) | 28.1 / 19 | 28.4 / 19 |
| Sections | — | 46 | 46 |
| Mean section | ~950 (pause-derived) | 990 | 1,004 |
| Shortest / longest section | — | 256 / 2,205 | 256 / 2,207 |
| Protagonist share | ~87% | 86.3% | 86.1% |
| Secondary share | ~13%, 4–5 lenses at 2.5–3.7% | 13.7%, six lenses | 13.9%, six lenses |

Secondary sections, repaired, by word tokens: Vane 1,462 (3.2%); Anwen 1,208 (2.6%); Rhea 1,139 (2.5%); Kellan 988 (2.1%); Perrin 855 (1.9%); Orla 759 (1.6%).

By kind of sentence, repaired (frozen in brackets):

| Kind | Share of sentences | Mean | ≤5 words | ≥40 words |
|---|---:|---:|---:|---:|
| Narration | 42.5% (42.5%) | 11.69 (11.64) | 30.5% (30.8%) | 0.84% (0.84%) |
| Speech | 54.7% (54.7%) | 7.24 (7.19) | 50.6% (50.9%) | 0.07% (0.07%) |
| Ledger | 2.7% (2.7%) | 6.59 (6.59) | 55.8% (55.8%) | 0% (0%) |

Narration by chapter, repaired (mean / ≥40): 33: 11.98 / 0.53%. 34: 11.92 / 1.36%. 35: 11.26 / 0.77%. 36: 10.99 / 0%. 37: 12.79 / 1.72%. 38: 12.35 / 1.36%. 39: 11.25 / 0.57%. 40: 11.15 / 0.42%.

**What the numbers say.**

- **Sentence rhythm and reading level are missed, by about the margin of the earlier movements.** The mean is 9.1 against 14.6; the Flesch–Kincaid grade is 2.5 against 6.8. Speech is 54.7% of sentences, with a mean of 7.2 words, and it was left clipped, as the owner has already ruled for this book. Narration alone runs 11.7 with 30.5% short sentences, nearer the target but not on it. Long sentences are rare everywhere (0.39% against 3.3%).
- **The repair did not move them** and was not meant to. The brief forbids chasing them by inflating dialogue or cutting action.
- **Paragraph and section sizes sit close to their targets** (28.4 and 19 against 26.8 and 18; 1,004 against about 950). Those targets come from pauses in audio, not from typography, so the comparison is directional only.
- **Viewpoint share is on target and slightly over** (13.9% against about 13%). The lens count is six in one movement, against four or five described for a whole book. The repair added 0.2 points, nearly all of it the stake paragraph in Vane's section.

**Uncertainty.** The syllable estimator is heuristic and probably a little low on this vocabulary, which would flatter both readability figures. The speech rule counts a narrated sentence as speech if it contains any quotation mark. Sentence counts depend on the tokenizer's treatment of dialogue tags. The frozen paragraph count (1,623) reproduces the editorial review's hand count exactly, which is some check on the splitter.

**Not measured:** progression vocabulary per 10,000 words, the development-moment proxy, and the optional signals (`-ly` words, reporting verbs, combat terms, fillers). The brief names five measures and those five were run. The earlier lexicons are in the extracted scripts if the recheck wants them.

## 10. Items declined, partly done, or outside the brief

### 10a. Declined, with reasons

- **Changing the ten-count hold.** The brief lists it among figures that cannot all stand. Once the rate, budget, sightings, set-up and Perrin's minutes were changed, it conflicts with nothing, and it is the figure that puts "Back" eleven seconds after the second cliff. It is also in three people's mouths and in the bearer's book. Left as written. The rescue inside it is tight: a ten-pace drag and a lift in ten slow counts. I did not shorten the drag.
- **Reordering chapter 33's first scene** (editorial review). The brief asks for the stake to be stated; a paragraph does that without moving anything.
- **"A quarter of a dram" in narration against the tape's twenty-six** (cold read, item 7). An approximation in the narrator's voice; the tapes are exact. Left.
- **"She had carried the thing for four years"** (cold read, item 12). Checked against chapter 32, line 341: the disk has lain against her breastbone for four years. The appointment is eleven years old; the wearing is four. Not a slip.
- **Old Four's Bench place and a printed table of standings.** The brief says to clarify the aggregate only as far as the reader needs. A rule and one line of Jude's do that.
- **Whole-text sentence and readability targets.** Not chased, by the brief and by standing ruling.

### 10b. Outside the brief and left alone

- The elders' shared voice, the nine turns of the go ritual, the summary treatment of three Regional boards and chapter 40's long coda. Both reviews note them and neither puts them in the brief.
- Perrin "went backward on his knees" while having "his back to it." The two phrases pull against each other. No review flagged it, and it sits inside the protected carry.
- Anwen's gate "fifteen paces south-west of that corner." Not rechecked against the sheet positions; nobody flagged it.
- "Kiva: Price First" and the other headings over chapters with cutaways.

### 10c. Partly done

- **"The Works" inside the hearing.** Qualified at Adlam's first words and at the refinery; the short form is left in his mouth, the Chair's and Mrs. Cobb's for the rest of that scene, and in the quoted rulings, where the referent is fixed. If the owner wants every instance qualified, that is nine more words.
- **Front-half figure clustering.** One site reduced. The ledger entry of the 25th and Perrin's arithmetic are the paper trail and the joke; both were kept, with only the wrong "two" corrected.

### 10d. For the recheck

- **The moved corner is the largest change** and should be tested first: does east along the south side read as "four paces outward," and does the page now say clearly enough which side Dray and her carriers are on?
- **The clock was built from speaking-pace estimates,** not from anything timed. The sightings are consistent with each other at a hundred counts a knot; a reader who paces the dialogue faster or slower will still find them in order.
- **Line numbers in both reviews no longer match** chapters 33, 38, 39 and 40, where paragraphs were added or moved.
- **"About 2:33" is not on the page.** It is a record figure derived from the clock.

## 11. Records reconciled

- `provenance/MOVEMENT-005-CONTINUITY.md`: edition line; new section 0; the Regional's scoring; the Carry note; the Pit timeline rows (third rung, Rhea's stand, knot rate, 2:25, set-up, 2:33 and the eastward carry, the drag, the lamps at "Back," the pens lit and dark); Kiva's knee; Anwen's interval; Perrin's clearance and first person; Kellan's discovery; Noa's notch; Dray's source; Rhea; Rusk; Bly's hand; the Chair's source; the hold's items 5, 8 and 11; the slate; length and viewpoint figures; the "seven times" check; "deliberately not done." SHA-256 after reconciliation: `9f0c7f8e170435b6c461b1bfe05dca53e4b566da0f7e0fdcf38bacb0c46d297e`.
- `STATE_LEDGER.md`, Movement Five block only: status line; Bly's hand; Regional scoring; the unlanded crossing; the hold (clock, eastward carry, Anwen's forty minutes, Rhea's stand); the instrument evidence; the grid's owner; Perrin; words. Earlier blocks are unchanged.
- `AUTHORSHIP.md`: one appended repair section with hashes, word counts and the measurement table.

## 12. Mechanical checks run (not a review)

- Frozen edition checksums: OK at five points (section 2).
- All 72 prose edits and all 47 record edits matched exactly once.
- Each edit site read in a diff against the frozen file after the edits were applied.
- Protected lines: present once each, frozen and repaired (section 8).
- Section rules per chapter: 4, 4, 4, 6, 4, 5, 4, 7, the same as frozen.
- Quotation marks: two lines with an odd count, both in chapter 34's quoted rulings, where a quotation runs across paragraphs. Both are as in the frozen file.
- Residual search for the replaced figures ("twenty counts," "perhaps a hundred," "thirty paces," "forty paces," "five minutes," "twenty minutes," "night hand," "first weight," "Dane," "south-east"): none left except unrelated uses (the south-east corner by name, the first husk's road, Gerald's twenty minutes, the Row and the grading room at thirty paces, the spring's forty paces, Perrin's forty paces to the gate).
- Word counts, hashes and the measurement in section 9.

Not run: any read-through for sense beyond the edit sites, any scoring, and the targeted recheck.

## 13. Working-tree state

Uncommitted in the working tree, on `worktree-kindling-2680-prologue-m001-opus55` at `a0922ea`: the eight chapters, the continuity checkpoint, the state ledger, the authorship record and this report. `editor/MOVEMENT-005-EDITORIAL.md` was already modified against `HEAD` before this session and is not part of this repair.

## Appendix — `metrics_m005.py`

Run as `python3 metrics_m005.py BOOK_ROOT FROZEN_ROOT metrics_m001.py metrics_m002.py metrics_m003.py`, where `FROZEN_ROOT/manuscript/` holds copies of the eight frozen files. The three earlier scripts are extracted from the editorial reviews' appendices with the `awk` lines given in `editor/MOVEMENT-004-EDITORIAL.md`.

```python
#!/usr/bin/env python3
"""Movement 005 numerical alignment - Kindling 2680 Book One, chapters 33-40.

Stdlib only. Read-only against the manuscript. Loads the Movement Three script's
definitions unchanged (it loads Movement Two's, which imports Movement One's), so the
word regex, sentence tokenizer, syllable estimator, both Flesch formulas, the section and
paragraph splitters and the narration / speech / ledger rule are the ones used for
Movements One to Four.
Usage: python3 metrics_m005.py BOOK_ROOT FROZEN_ROOT metrics_m001.py metrics_m002.py metrics_m003.py
FROZEN_ROOT is a directory holding manuscript/chapter-33.md ... chapter-40.md copied from
editions/movement-005-pre-repair/.
"""
import re, sys, io, statistics, hashlib, contextlib

ROOT, FROZEN, M1PATH, M2PATH, M3PATH = (a.rstrip('/') for a in sys.argv[1:6])
RUN_MARK = "print('SHA-256 (first 16) / whitespace words')"
src = open(M3PATH, encoding='utf-8').read()
src = src[:src.rindex(RUN_MARK)]
sys.argv = [M3PATH, ROOT, M1PATH, M2PATH]
g = {'__name__': 'm3defs'}
with contextlib.redirect_stdout(io.StringIO()):      # the earlier scripts print their own runs on load
    exec(compile(src, M3PATH, 'exec'), g)
m1, words, clean, sections, sentences, split_rule = (g[k] for k in
    ('m1', 'words', 'clean', 'sections', 'sentences', 'split_rule'))
paragraphs, syllables = m1.paragraphs, m1.syllables
M5 = ['chapter-%02d' % i for i in range(33, 41)]

# Movement Five viewpoint map, identified by reading every section; guarded by first words
POV5 = {
    'Hollis Vane had read a great many things aloud': 'Vane',
    'Kellan Renn had never liked the': 'Kellan',
    'Anwen Pryce held the end of a wall for the last time': 'Anwen',
    'Orla Dane sat on in the yard': 'Orla',
    'Rhea Sorn stood a long pace behind': 'Rhea',
    'Perrin Cade had never in his life wanted': 'Perrin',
}


def measure(root, label):
    m1.ROOT = root
    print('\n================ %s ================' % label)
    secs, pov, found = [], {}, set()
    allsent, allwords, paras, syl = [], 0, [], 0
    for f in M5:
        raw = m1.load(f)
        print('  %s sha256 %s  wc-w %d' % (f, hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16], len(raw.split())))
        for s in sections(raw):
            n = len(words(clean(s)))
            secs.append(n); allwords += n
            who = 'Kiva'
            for k, v in POV5.items():
                if clean(s).startswith(k):
                    who = v; found.add(k)
            pov[who] = pov.get(who, 0) + n
            ps = paragraphs(s)
            paras += [len(words(p)) for p in ps]
            allsent += sentences(s)
            syl += sum(syllables(w) for w in words(clean(s)))
    assert found == set(POV5), 'viewpoint guard failed: %s' % (set(POV5) - found)
    lens = [len(words(clean(x))) for x in allsent]
    n = len(lens)
    wps, spw = allwords / n, syl / allwords
    print('  word tokens %d; sentences %d' % (allwords, n))
    print('  sentence mean %.2f median %.1f pstdev %.2f <=5 %.1f%% >=40 %.2f%% max %d' % (
        statistics.mean(lens), statistics.median(lens), statistics.pstdev(lens),
        100 * sum(1 for x in lens if x <= 5) / n, 100 * sum(1 for x in lens if x >= 40) / n, max(lens)))
    print('  syllables/word %.3f; Flesch Reading Ease %.1f; Flesch-Kincaid grade %.1f' % (
        spw, 206.835 - 1.015 * wps - 84.6 * spw, 0.39 * wps + 11.8 * spw - 15.59))
    print('  written paragraphs %d; mean %.1f median %.1f words' % (len(paras), statistics.mean(paras), statistics.median(paras)))
    print('  sections %d; mean %.0f words; shortest %d longest %d' % (len(secs), statistics.mean(secs), min(secs), max(secs)))
    sec2 = allwords - pov['Kiva']
    print('  protagonist share %.1f%%; secondary %.1f%% (%s)' % (
        100 * pov['Kiva'] / allwords, 100 * sec2 / allwords,
        ', '.join('%s %d (%.1f%%)' % (k, v, 100 * v / allwords) for k, v in sorted(pov.items(), key=lambda kv: -kv[1]) if k != 'Kiva')))
    res = split_rule(M5)
    tot = {k: [len(words(clean(x))) for f in M5 for x in res[f][k]] for k in ('narration', 'speech', 'ledger')}
    for k in ('narration', 'speech', 'ledger'):
        ls = tot[k]
        print('  %-9s sentences %4d (%4.1f%%) mean %5.2f median %4.1f <=5 %4.1f%% >=40 %4.2f%%' % (
            k, len(ls), 100 * len(ls) / n, statistics.mean(ls), statistics.median(ls),
            100 * sum(1 for x in ls if x <= 5) / len(ls), 100 * sum(1 for x in ls if x >= 40) / len(ls)))
    print('  narration by chapter (mean / >=40): ' + '; '.join(
        '%s %.2f / %.2f%%' % (f[-2:], statistics.mean(l), 100 * sum(1 for x in l if x >= 40) / len(l))
        for f, l in ((f, [len(words(clean(x))) for x in res[f]['narration']]) for f in M5)))


measure(FROZEN, 'FROZEN editions/movement-005-pre-repair')
measure(ROOT, 'REPAIRED manuscript/')
```
