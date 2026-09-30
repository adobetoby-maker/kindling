# Ensemble revision — author report

> Built by TAC

## 1. Run identity

| Field | Value |
|---|---|
| Actual runtime model | **Claude Opus 5.5 (`claude-opus-5-5`)**. This is the selected author, not a coordinating model. It resolves the prompt's "Actual runtime model: not yet verified." |
| Seat | Monroe Jackson 1.3.0 / O'Connor seat 1.3.0 (internal seat `oconnor`) |
| Public author | Monroe Jackson |
| Packet | `packets/MOVEMENT-005-ENSEMBLE-REVISION.md` |
| Compiled prompt | `editor/MOVEMENT-005-ENSEMBLE-OPUS-5-5.prompt.md` (2,650 lines), read in full |
| Formula source | `/Users/drive/penname/research/ironprince-craft-formula.md`, SHA-256 `9f97e2f2…30c0b8` as recorded in the prompt |
| Source edition | Canonical `manuscript/chapter-33.md` … `chapter-40.md`. Their SHA-256 hashes matched `editions/ensemble-pre-revision-2026-09-29/MANIFEST.md` before drafting, and they still match after the run (§9) |
| Output edition | Staged ensemble revision of chapters 33–40. **Not canon.** For orchestrated review |
| Date | 2026-09-29 |
| Method | One continuous author session. No subagents, no Agent tool, no delegation. No additional skill was loaded; the compiled prompt was executed as given. The movement was read whole first, then rewritten in reading order, then read once together, with only blocking repairs |

### Where the files are (read this first)

This session ran as a background job, and the harness required edits to be isolated in a
git worktree. The staged files therefore sit at the **same relative paths inside the
worktree**, not yet in the main checkout:

```
/Users/drive/kindling-repo-stage/.claude/worktrees/meridian-m5-ensemble/books/book-02-meridian/revisions/ensemble-2026-09-29/
    manuscript/chapter-33.md … chapter-40.md
    CONTINUITY.md
    AUTHOR-REPORT.md
```

Nothing was committed or pushed, per the run instruction. The worktree branch
`worktree-meridian-m5-ensemble` has no commits, and the files are untracked. To put them
where the orchestrator expects them, run this. It merges into the existing staging folder
and leaves its `README.md` alone:

```
cp -R /Users/drive/kindling-repo-stage/.claude/worktrees/meridian-m5-ensemble/books/book-02-meridian/revisions/ensemble-2026-09-29/. /Users/drive/kindling-repo-stage/books/book-02-meridian/revisions/ensemble-2026-09-29/
```

Keep the worktree until that copy is made.

## 2. Files read

In the brief's order, all in full:

1. `editor/MOVEMENT-005-ENSEMBLE-OPUS-5-5.prompt.md`: author profile, formula §§2–6 and 8–9,
   the task, the packet, and the embedded evidence below.
2. `manuscript/chapter-32.md`, the entry seam. The embedded copy matches the file on disk,
   apart from one trailing blank line.
3. `manuscript/chapter-33.md` … `chapter-40.md`, read in full, in order, from disk after
   checking their hashes.
4. `provenance/MOVEMENT-005-CONTINUITY.md` (embedded copy identical to disk).
5. `manuscript/chapter-41.md`, the exit seam (embedded copy identical to disk).
6. `editor/MOVEMENT-005-REPAIR-REPORT.md` and `editor/MOVEMENT-005-RECHECK.md` (embedded),
   including the accepted ch 39 ascending-stair fix.
7. The owner voice layer (embedded).

Also opened, for housekeeping only: `revisions/ensemble-2026-09-29/README.md`,
`editions/ensemble-pre-revision-2026-09-29/MANIFEST.md`, and
`packets/CHAPTER-045-ENSEMBLE-REVISION.md`. That last one was read only to confirm that the
Chapter 45 run *appends* to this report and writes no other file of mine.

## 3. Files written

| File | Status |
|---|---|
| `revisions/ensemble-2026-09-29/manuscript/chapter-33.md` … `chapter-40.md` | New. Eight complete chapters |
| `revisions/ensemble-2026-09-29/CONTINUITY.md` | New. Day/scene map, camera settles, ledgers, preserved facts, changed joins, ch 41 exit state |
| `revisions/ensemble-2026-09-29/AUTHOR-REPORT.md` | New. This file |

**Not touched:** the canonical `manuscript/`, `provenance/`, `editions/`, `packets/`,
`editor/`, `BOOK_MAP.md`, other books, and `AUTHORSHIP.md`. The compiler's generic task text
says to record the run in `AUTHORSHIP.md`, but the packet and the owner's instruction limit
this run's writes to the staging paths. The authorship record is §1 of this file instead,
and it can be copied into `AUTHORSHIP.md` if the staged edition is promoted.

## 4. Word counts (`wc -w`)

| Ch | Heading (revision) | Source POV | Source | Revision | Δ |
|---|---|---|---:|---:|---:|
| 33 | Out: Four | Toren | 6,730 | 6,992 | +262 |
| 34 | The Yellow Stair | Callie | 6,550 | 6,537 | −13 |
| 35 | A Hole in It | Jab | 6,483 | 6,522 | +39 |
| 36 | The Door That Opens Toward You | Toren | 5,196 | 5,469 | +273 |
| 37 | The Flap | Callie | 5,905 | 6,895 | +990 |
| 38 | Off Before Ten | Jab | 6,917 | 5,909 | −1,008 |
| 39 | The Point | Toren | 4,869 | 4,941 | +72 |
| 40 | Graded | Callie | 4,936 | 4,997 | +61 |
| **Total** | | | **47,586** | **48,262** | **+676 (+1.4%)** |

The 37/38 swing is the camera restart being removed (§6, item 3). Together the two chapters
come to 12,804 words against the source's 12,822, so the fight keeps its developed length.
No catch, adaptation, kill, cost or scene was cut. Section breaks: 53, against the source's
105.

## 5. How the brief was carried

**Company camera.** The narrator stays at Caul Hill with the bodies and reports what the
party can see, hear, count and say: positions, hands, faces, the counter's numbers, the glass,
the calls. Group statements are used only for shared knowledge ("Nobody said the count out
loud. Nobody needed to."). Private interiority happens only after a clean settle into one
person, and it returns to the company through an action or someone else's line. No paragraph
holds two people's private thoughts. The settle map is in `CONTINUITY.md` §4. There is no
essaying narrator; the few short glosses that remain are anchored to something happening now
(for example, how Dee measures Toren's own in glass turns).

**Headings.** All eight headings are exactly as the packet lists them, with no protagonist
names.

**Naming.** The narrator calls her **Dee** throughout, and Callie and Pell still say "Miss
Wren" aloud. The source's Callie chapters used "Miss Wren" in the narration. One narrator
needs one name, and it keeps listeners from hearing two people.

**Three indispensable competencies, made interdependent on the page.**
- **Callie, access and current control.** She reads the yard, the bridge, the river and the
  floors, and finds the clean way and the stone under the plank. She realises the pump
  principle means shutting the river. She holds the door and a bit so the room becomes the
  drum. She holds the stair top so Toren can come up, and she takes the final lean so Toren
  can light.
- **Jab, survival and pulse recognition.** He hears the ten and three. He feels the vent,
  the swell, the push, "it learned", "it's missing" and "nearly dry". He catches on the push
  and comes off before the ten, and his "What do you feel?" answer makes the crossing
  possible.
- **Toren, moving defence and physical severance.** He sets struts: the plank stone, the
  ramp strut, the door, the roof, the lean. He makes the cuts that turn ropes into holes, and
  he puts in the point.
- **The handoffs are spoken on the page:** *Taking / Yours / Mine / Letting go*; *Callie.
  Hold the front one*; *Get the stump. I've got the roof*; *I'm giving you the lean. / Give
  it me. / Letting go. / Mine.*

**Adults inside the field.** Dee is authority throughout: the glass, the line, the watch, the
limits, the co-signed breach. Her floor and her sickness are costs the party shares. Rook sets
the outside rule, gives the warning not to look round, names the lifter, lays the poles
("furniture") and grades the Yield. Pell builds the sledge, explains the pump, tips the cart,
counts the sky, makes the cautious case "so it's been said", and turns the cart into pieces.
None of them solves the fight. Pell teaches the pump; Callie, Jab and Toren find the use and
carry it out.

**Legible geometry.** Directions are now given from landmarks that don't change with the
reader's facing: the *tray wall* (north) and the *room side* (the wall with the doors in it,
south), east toward the stair and west toward the drum. The D+48 room gets one clear still
picture before the first three: door in the north wall; cabinets right, with the frame and
the bag on the two nearest; racks and boxes left; the lifter three paces in over the carrier,
hump to the south-east corner; the second heap at the far end of the cabinets; the stump from
the threshold; three arm-ropes; Toren a pace behind Callie. The corridor lantern is now set
down by Dee and picked up again, and the counter moves to her shoulder on the page.

**Collective identity before a name.** The procedural calls are the party's shared language
("Turn", "Set", "the three", "One caught", "Jar", "Off"). The humour stays task-bound: "We're
both of us wrong"; "Not the three. My three."; "A board doesn't care"; "Sliding," a breath
late; "That's furniture"; "She's always right. She's a horse." There is disagreement (Callie
and Pell on going home with nothing; Toren and Dee at the line) and watching of limits (Dee
measuring, Jab's "Busy", Callie's "I've got two turns", Toren's "I'm stopping"). There is
accepting someone else's risk (Dee letting Jab touch the rope; Toren giving Callie the lean;
Callie working with her back to all of it). The word "company" is never used as a label.

**Audio clarity.** Each speaker is named where there could be doubt. No paragraph pair gives
two speeches to the same speaker (checked by script). No comma splices (scanned). Long
sentences put the subject and verb first and build with *and*. Unclear pronouns have become
names (for example, "She saw Dee sit back…" and "to Dee"). In ch 36 "the others" and "the
three" no longer sit side by side.

## 6. Material departures from the source

None changes an event, a cost, a count or an outcome.

1. **Camera.** Single-POV chapters in rotation are now one company narrator with settles.
2. **Headings.** POV names removed; ch 38 is "Off Before Ten", as the packet lists it.
3. **The 37/38 restart is removed.** The source retold the D+48 entry twice, once from Callie
   (ch 37) and once from Jab (ch 38). Ch 37 now runs the entry, the frame onto the cabinet,
   the lee, Dee's count and the whole first three once, with the door and the room both on
   camera. Ch 38 opens at the next beat. The lines "It's a shelf. Not a floor." and "It's
   where it was." moved from 38 into 37.
4. **Openings and closings widened.** Ch 33 opens on all six before the light instead of
   inside Toren. Ch 36 opens on all four leaving in order. Ch 39 opens on the point and one
   still picture, without the recap. Ch 40 closes on the whole moving party, with Toren
   counting at the back; the source closed on Callie hearing him.
5. **Section breaks** are down from 105 to 53, and fall at changes of place, time or task.
6. **Visible beats the source only implied** (no new events):
   - ch 36: Callie chooses to lay the hook across the top step after "We're up!" ("He's got
     a light on his belt…"), and Dee does not overrule her;
   - ch 37: Dee sets the lantern on the corridor floor and takes the counter ("You'll not see
     it. I will.");
   - chs 34 and 37: Toren holds his lantern out at the room door;
   - ch 39: Dee picks the lantern up on the way out;
   - ch 40: Jab draws from Toren's jar first, then his own second, which the grading
     already implied.
7. **Interior made audible.** Some private deductions are now said aloud, so the party knows
   them and listeners hear them:
   - Callie's "West" reasoning on the stair (34);
   - "The boxes are in the grey. And the grey's in the boxes." (34);
   - Jab's "It lies there for ten" (35);
   - Jab's "Something's on it. Coming." (35);
   - Callie's "It's going in. It's feeding the room." (37).
8. **Speaker attribution.** A few unattributed interjections now have speakers: Callie's
   "Toren—" (36), Dee's "Toren—" (38), Toren's "Why?" (38).
9. **Small reactions added for texture:**
   - Jab's nod when Callie keeps the *pen, 35th* tag (33);
   - Jab's hand going to the fish at the yellow rail (34);
   - Callie looking longest at Pell's rows of strokes after the gatehouse chalk (36).
   - Rook and Pell have no new dialogue.
10. **Corrections to source slips** (also in `CONTINUITY.md` §9):
    - "thirty-two, and two open" → "thirty-two. Jar two's open." (35);
    - "the four of them" (five listed) → "the five of them" (36);
    - "eight jars" → "a frame of jars" (40; the frame holds seven);
    - the lantern holder at the room door (34, 37).

## 7. Formula comparison (target vs observed)

Method: my own scripts. Sentences are split on terminal punctuation, including dialogue
fragments. Flesch uses a heuristic syllable count. Words are counted by a regex tokenizer
(48,159, against 48,262 by `wc -w`). Source and revision were measured the same way. The
source's §3 paragraph and scene figures are ASR-pause proxies, and its §5 development counts
are heuristic, so the comparison is directional, as the formula itself says.

| Metric | Formula target | Source (chs 33–40) | Revision | Direction |
|---|---|---:|---:|---|
| Mean sentence length | 14.6 words | 9.0 | 10.1 | toward, short of target |
| Median sentence length | 11 | 6 | 6 | unchanged |
| Sentence SD | ~26 | 7.9 | 9.6 | toward (see note) |
| Sentences ≤5 words | 27.7% | 45.4% | 44.2% | barely moved |
| Sentences ≥40 words | 3.3% | 0.5% | 1.7% | toward |
| Paragraph median / mean | 18 / 26.8 | 14 / 26.5 | 16.5 / 29.4 | toward / slightly over |
| Words per section | ~950 | ~420 | ~790 | substantially toward |
| Breaks per 10k words | ~8.7 | 22.1 | 11.0 | substantially toward |
| Flesch Reading Ease | 72.3 | 100.4 | 99.1 | not reached |
| Flesch–Kincaid grade | 6.8 | 1.5 | 1.9 | not reached |
| POV shares | 87% lead / 13% cutaways | 3 × ~33% rotating | ensemble camera; settles ≈17% of words (Jab ~8%, Callie ~5%, Toren ~4%) | **owner exception** for chs 33–40 |
| "that" per 10k | ≤92.1 (tighten) | 49.6 | 52.5 | within |
| just / almost / felt / seemed per 10k | 5–25 band | 1.7 / 0 / 14.6 / 0 | 2.1 / 0 / 10.8 / 0 | felt in band; others below (secondary) |
| -ly adverbs per 10k | ~161 (optional register) | 11.6 | 11.0 | Monroe register; not chased |
| Dialogue tags per 10k | ~41 | 175.9 | 179.7 | well above (see conflicts) |
| Combat vocabulary per 10k (own list) | ~22 | 52.3 | 51.3 | above (set-piece movement) |
| Progression vocabulary per 10k (own list) | ~58 book-wide, receding after the first third | 109.4 | 105.4 | not comparable; did not add, did not recede |
| Reflection markers per 10k (own list) | protagonist 4.5 | 3.6 | 3.1 | heuristic only |

**Conflicts, reported rather than scored as passes:**

1. **Sentence distribution against preserved dialogue and approved cadence.** About half the
   short sentences in this movement are the party's procedural calls and turn-by-turn
   dialogue, which the packet asks me to preserve and which the ensemble direction puts at
   the centre. Narration was lengthened, with 2–3 clause sentences and a few 40+ sentences
   that keep an audible hierarchy. The distribution cannot reach 27.7% short or a median of
   11 without rewriting preserved dialogue into longer tagged speech, which works against
   the owner voice ("readable, controlled sentences") and the packet's read-aloud cadence.
2. **Flesch and FK against the Monroe word register.** At a 14.6-word mean, Flesch 72.3 needs
   about 1.4 syllables per word. This voice runs near 1.15–1.2 because of its plain
   one-syllable vocabulary. Reaching the target would mean changing word choice across the
   book, not just in this movement.
3. **SD target.** An SD of ~26 against a 14.6 mean and an 11 median needs a very heavy long
   tail. As the formula instructs, I left the figure unchanged and flag it for the
   source-book audit.
4. **Dialogue tags (~180 vs ~41).** Audio clarity for a six-person party needs explicit
   speakers, and the packet makes that an explicit improvement goal.
5. **Progression and combat density in the final third.** Chs 33–40 open the book's last
   third, where the formula expects progression vocabulary to recede. This movement is a
   mechanics-driven set piece at a genuine turning point. The revision added no mechanics
   exposition, but it did not reduce the vocabulary either.
6. **POV allocation.** Suspended for these eight chapters by the owner's explicit exception.

## 8. Anything needing editorial judgment

1. **Does it still read as rotation?** The base narration is company camera (~83%). But the
   longest settles still sit where the source's private beats sit: Jab's sink (35) and fight
   (38), Toren's door (36) and point (39), Callie's settling (37) and night (40). They are
   binding emotional costs, so I kept each in its owner's head. Reviewers should judge
   whether that concentration still sounds like the old rotation. If it does, the likeliest
   lever is shortening, not moving, the ch 35 sink settle and the ch 40 door reflection.
2. **Jab now has the largest private share** (~49% of settle words), because pulse
   recognition is the one sense that can't be observed from outside. The source had him
   lowest (28.2%). The owner's M5 ruling allows M6 to lean toward Jab; this changes that
   baseline.
3. **Narrator's "Dee" in Callie's settles.** Keep it, or let Callie's settled passages use
   "Miss Wren" as a signal that the camera has entered her?
4. **Chapter lengths after removing the restart:** ch 37 is 6,895 words and ch 38 is 5,909.
   If the owner wants the fight to *open* ch 38, the seam can move back before "Toren lit
   the heel" without any retelling.
5. **The new stair-top beat (ch 36).** Callie chooses to hold the top step and Dee lets her.
   It makes a handoff visible, and it slightly extends an "everybody out" moment. Please
   confirm it stays inside the rules as the owner reads them.
6. **Watched phrases.** "the way" appears 142 times (source 141); "Nobody said anything" 7
   (source 7). I did not thin them. That is an editorial option, not a camera issue.
7. **Formula drift** (§7) is for the owner to accept or to direct a focused repair on.
8. **Items carried over from the M5 repair report, unchanged:**
   - Dee's "1½ a turn" rate for holding an open;
   - Callie's still hook taking the lean;
   - whether Jab is bound by the one-configuration limit;
   - Toren's thin reserve margin;
   - Director review of the breach (for M6 to stage).

## 9. Verification performed

- **Canon untouched.** After the run, the SHA-256 of `manuscript/chapter-33.md` …
  `chapter-40.md` in the main checkout still equals `MANIFEST.md`:
  - `ef060d0c…e893`, `8f191bcd…7ca6`, `0d1ba2cf…581b`, `85a1b120…8c74`;
  - `84e32d25…09bd`, `29282e3b…4c90`, `cdfe47d5…b136`, `55606718…4c19`.
  - `chapter-41.md` was not touched either.
  - Worktree `git status` shows only the new `revisions/` folder.
- **Ledger.** Every jar call, halt, catch label, crossing price, floor, grade and exit total
  was checked line by line against the checkpoint (`CONTINUITY.md` §5). All match.
- **Geometry.** The stair is 30 down east, landing, 20 down west, and 20 then 30 going up.
  Pipes are on the left walking in, with the clean strip on their north side. The door
  opens toward the stair and pushes from the corridor. Cuts are made from the corridor
  before Toren steps in. Callie's fall order is lee, then her legs, then the Ward. The belay
  runs through the landing ring and twice round the rail post.
- **Rules.**
  - One configuration for Toren: every Edge action is release → light → dark → set, and the
    final lean goes to Callie's hook before the spike is lit.
  - Nobody kneels inside the fence: Jab's two lapses are caught ("That goes for knees" /
    "Up off your knees"), and Callie is allowed her knees because she is hurt.
  - Ward stops matter, not the room's reading.
  - Sustain draws active burden only.
- **Camera and canon precision.** In the read-through I found and removed several group
  statements that would have turned one person's knowledge into everyone's: who had watched
  the yellow line, who had heard Senna, who knew the label's hand, and who had noticed the
  corner heap. Each now carries only what the source establishes.
- **Joins.** 32→33 and 40→41 were checked against the seam chapters; ch 41's opening state
  holds.

## 10. Consolidated repair

| Field | Value |
|---|---|
| Brief | `editor/MOVEMENT-005-ENSEMBLE-CONSOLIDATED-REPAIR.md`, read in full |
| Author | Claude Opus 5.5 (`claude-opus-5-5`), the same author session resumed; Monroe Jackson 1.3.0 / O'Connor 1.3.0 |
| Date | 2026-09-29 |
| Method | One session, no subagents, no delegation. The inputs were read in the brief's order: staged chs 33–40, `CONTINUITY.md`, this report, `EDITORIAL-REVIEW.md`, `COLD-READ.md`, canonical chs 32 and 41, and `provenance/MOVEMENT-005-CONTINUITY.md` |
| Baseline | The frozen first draft, `editions/ensemble-first-draft-2026-09-29/` in the main checkout. §§1–9 above describe that draft and are left as written |
| Written | Staged chs 33–37, 39 and 40; `CONTINUITY.md` (changes marked **(CR)**); this section; `REPAIR-REPORT.md`. **Ch 38, the fight, is byte-identical to the first draft** |

### Exact changes (first draft → repair)

**Ch 33 — Priority 1, plus the Director's wording from Priority 2**

1. **Water.** The skins are counted once, aloud. The narrated count and "One and a third"
   become: "Toren went to the cart and hefted the other two where they hung from the rail
   behind the driver's bench. / "One full," he said. "One a third."" Callie's river reading
   is one sentence. The wood and the fever cup lose their restated reasons ("Boiling meant a
   fire, and a fire meant wood…"). Kept: "Seven… The room" and "Nine. Our wash is in it";
   "That's one pot… Maybe two"; Rook's fever exchange; Pell sitting up alone and deciding to
   count.
2. **Coats.** "Senna's rules said coat off, shake it, wash at the river, and they had done
   all that the night before; but they had done it at dusk, in the last of the light" →
   "They had washed at dusk by Senna's rules, but dusk was dusk". Jab's "Eight" stays
   spoken. "Dee's coat was twelve. Callie's own was fourteen." → "Dee's coat and Callie's
   read twelve and fourteen." Pell's twenty and Toren's thirty → "Sixteen" are kept.
3. **Hook.** The curve's eighteen and the scoured eleven move into narration: "Its curve
   read eighteen from the loose bank and the lip, but it was the grip that Callie frowned
   at" and "it came down to eleven". The spoken "Thirty-four… It's the rag." is kept, and so
   are the one-strip cut, the burial under the chalk cross and the *pen, 35th* tag.
4. **The Director's words:** the consolidated repair initially followed Dee's ch 32
   quotation, but the targeted recheck restored the Director's own canonical ch 21 wording:
   "you do what you have to do and you come home" in chs 33 and 36.
5. **Council.** Callie opens: "Inside, forty," she said. "The line's sixteen. That leaves
   twenty-four to work with." … "Home, three, on the cart. Not to be touched." The container
   list becomes one narrated sentence: "The rest of what they had sat in the frame and on
   the cart: two empty jars in the frame, the road jar empty in its rack, five vent jars in
   the straw, and the socket where jar B had broken." Settled ash: "A Handful each in you
   and me and Toren," said Callie. The old price ("We priced forty-eight for five people…
   The rooms were thirty") → "What we priced was for five of us going in, with three
   healers. It's four, with two, and one of the two has to be the jar and the watch…".
   Unchanged: "Twelve… Half", "Twelve spent is twenty-eight left", "Twenty-eight's today's
   line… Sixteen's the line. Both.", the healer-lost rule and "Then I don't come in".
6. **Chronology.** "They went in at noon." moves from above the eating paragraph to the end
   of the section, after the meal, the first jar ("Dee opened the first jar there, not at
   the gate") and the gear. "They ate first, at the pump house" → "They ate at the pump
   house".

Ch 33 net: −229 words (6,992 → 6,763, −3.3%; source 6,730).

**Ch 34 — Priority 2 (audio).** "She's been looking at that line for five weeks," said
Toren → "Gran's been looking…".

**Ch 35 — Priority 2 (counter logic).** "Forty," she said. "At a hand. It's hot. It's the
floor in a jar." → "It's hot," she said. "At a hand it reads over everything in here. It's
the floor in a jar." Room 1 read 65 by the dead boxes and 100–110 near the corner and the
door, so a hot forty was off the scale. Dee's echo is kept.

**Ch 36 — Priority 2**
- The checkpoint's forty now comes at the pump house: "Callie held the counter to the other
  one, the jar from the first lift, at a hand. / "Forty," she said. "Out here, where the
  river reads seven." / Dee carried them both…"
- Rook's quotation: "have to do" → "have to".
- The *come back without it* passage now says what the line meant: "She had been saving
  that. She had not said *come back without it*, and she had not needed to. She had known
  his father, and his father's father, and she had told him where the boxes were anyway,
  knowing what he would do: *I know what every man in that line does with a number once
  he's got it.* He goes and gets it, she had said. With a paper and three ifs." Those are
  Senna's words in canonical ch 14:73 and 14:77.

**Ch 37 — Priorities 2 and 3**
- Pump: "It had not moved in seventy years." → "It had not moved in a long time".
- Toren's 1½ is marked twice. In Callie's price: "A Handful and a half in Toren, and that's
  more than he's carried too." At the watch: "It was half as much again as he had ever
  carried. Dee had sat with him through the last of it… put two fingers on his wrist and
  said it was lying still."
- Anchor after the price: "It's not twelve," said Callie. "It's less than today cost us."
  D+47 cost eleven (40 → 29).
- The settle stops short of the lesson. "She understood it now… She would be holding the
  door so that they could carry it." → "She did not know who that was, tomorrow. She did not
  know what a lee was for, if it was not over anybody. She had never held anything she
  could not see." The wall sentence now ends "…doing things she could not see, and she would
  not know how they were until one of them said so." After her mother's fingers: "Callie
  had not known then what she meant, and she did not know now." Kept: "who's worth the
  lee", the fingers opening, and Rook's "You'll want to look. Don't."
- Anchor after the settle: "Callie said it back. Everything above the line was what
  tomorrow could cost. The line itself was for getting out."
- Rook: "the lifters behind me" → "the people lifting behind me".

**Ch 38 — unchanged.**

**Ch 39 — Priority 2**
- "In one working turn. Twenty of the glass, from now." → "Twenty turns of the glass, from
  now."
- After "More than we can lift in twenty", Dee sets the rule for the window: "Then it's what
  gets us back over the line… The fence is at thirteen. That's under. What we lift goes in
  the empties, and what's in a jar counts. Three turns of lifting puts us back over
  sixteen. If it doesn't, we go at the third, with what's in the jars." … "It doesn't make
  the crossing right. It's the same once, and it goes on the paper with the rest."
- In the lifting: "Three," said Dee. … "That's us back over the line."
- Paper: *Once. For the Director.* is now followed by *Still under after the kill; back over
  by the third turn of lifting.*

**Ch 40 — Priorities 2 and 3**
- Dee at night: "It's the room… the room coming out… the room for a day" → "that room",
  three times. "The room" stays the counter's word for background.
- Anchor after the grading: Pell's "And two boxes." → "Five short, clean. For two boxes."
- The realization lands once, here. "Under the hill she had held a door. She had held the
  rest of the world off three people so that they could do the thing only they could do,
  where she could not see them do it." → "Under the hill she had held a door, and the three
  of them had done the work behind her back." Unchanged: "the edge of them", choosing what
  to hold, the ache in her palm, and the look back.
- Anchor after the route price: "That's half the lifter's, for one hour in the wash. The
  rest is for the road." Then she went on. "We'd be on the old line…".

**My own slips, fixed before closeout**
- Ch 37: the first anchor ended "and today we ran". Ch 36 opens "Nobody ran", so the clause
  is cut.
- Ch 33: the first coat compression, "read in the teens", misstated Dee's twelve. It now
  reads "twelve and fourteen".
- Two intermediate wordings were caught during the repair and never survived: "Callie's own
  read…" (heard aloud, "own" is the reserve) and "half of what we lifted" (the lifter's jars
  hold 20½, not the 32 lifted).

### Final word counts (`wc -w`)

| Ch | Source | First draft | Repair | Δ vs first draft |
|---|---:|---:|---:|---:|
| 33 | 6,730 | 6,992 | 6,767 | −225 |
| 34 | 6,550 | 6,537 | 6,537 | 0 |
| 35 | 6,483 | 6,522 | 6,527 | +5 |
| 36 | 5,196 | 5,469 | 5,527 | +58 |
| 37 | 5,905 | 6,895 | 6,949 | +54 |
| 38 | 6,917 | 5,909 | 5,909 | 0 |
| 39 | 4,869 | 4,941 | 5,047 | +106 |
| 40 | 4,936 | 4,997 | 5,001 | +4 |
| **Total** | **47,586** | **48,262** | **48,264** | **+2** |

Against the source, the accepted repair is +678 (+1.4%). Chs 37 + 38 come to 12,858 words (source
12,822), so the fight keeps its developed length. Section breaks: 53, unchanged (7, 7, 6,
6, 8, 6, 7, 6).

### Verification

- **Canon untouched.** The SHA-256 of canonical `manuscript/chapter-33.md` … `chapter-40.md`
  still equals `editions/ensemble-pre-revision-2026-09-29/MANIFEST.md` (`ef060d0c…e893` …
  `55606718…4c19`).
- **Frozen edition untouched.** All eight chapters match
  `editions/ensemble-first-draft-2026-09-29/MANIFEST.md`. That edition's `AUTHOR-REPORT.md`
  (`5280f69c…6cef`), `CONTINUITY.md` (`2eae46be…f4fa1`) and `MANIFEST.md` (`3f673479…b011`)
  match their pre-repair hashes.
- **Git.** Nothing was committed or pushed. Worktree `git status` shows only untracked
  staging and editor files; no tracked file is modified.
- **Where the files are.** The accepted repaired files are in the main checkout at
  `revisions/ensemble-2026-09-29/`. The worktree preserves the author's pre-targeted-recheck
  repair; the main checkout additionally contains the two exact surgical fixes required by
  `TARGETED-RECHECK.md`.

---

*The Chapter 45 ensemble run appends its own section below this line.*

## 11. Chapter 45 ensemble run — Everybody Back

| Field | Value |
|---|---|
| Actual runtime model | Claude Opus 5.5 (`claude-opus-5-5`), the same author session |
| Seat | Monroe Jackson 1.3.0 / O'Connor 1.3.0 |
| Packet | `packets/CHAPTER-045-ENSEMBLE-REVISION.md`, read in full. It exists only in the main checkout |
| Source | Canonical `manuscript/chapter-45.md`, SHA-256 `98f3aa73…4daca`, equal to the pre-revision manifest |
| Output | `revisions/ensemble-2026-09-29/manuscript/chapter-45.md`. Staged, not canon |
| Date | 2026-09-30 |
| Method | One session, no subagents, no delegation. I read everything first, then drafted the chapter whole, then reread it and repaired it against an inventory of the canonical chapter |

**Read, in this order:**
1. The packet, and `packets/MOVEMENT-005-ENSEMBLE-REVISION.md` for the camera discipline it
   points to.
2. The accepted staged chs 33–40 in full, as they stood after the targeted recheck's two
   surgical fixes.
3. The staged `CONTINUITY.md`, `TARGETED-RECHECK.md` (ACCEPT) and `README.md`, and this report.
4. Canonical chs 44, 45 and 46 in full. All three match the pre-revision manifest.
5. `provenance/MOVEMENT-006-CONTINUITY.md` in full.
6. By search: the ch 45 items in `editor/MOVEMENT-006-REPAIR-REPORT.md`,
   `editor/MOVEMENT-006-RECHECK.md` and `editor/BOOK-LEVEL-REVIEW.md`.
7. By search, the canon behind two plants: ch 15 (Jab's hand on the day holder's chest, D+25)
   and ch 24 (Katori: "I've not said the rest").

**Written:** the staged chapter; `CONTINUITY.md` (its coverage line, one row of §1, and a new §11);
and this section. Nothing else.

### How the packet was carried

- **Heading:** `# Chapter 45 — Everybody Back`.
- **Company camera:** everything is company camera except eight short settles. There are seven
  into Toren and one into Jab, about 5% of the words. The list is in `CONTINUITY.md` §11. Callie's
  lesson at the corner stays spoken, as it is in canon. Dessa, Katori and the rest of the watch
  appear only through what they do and say.
- **One field:**
  - The chapter opens on the whole bowl as the six can see it.
  - At the corner, Ines's arrows from the west rim take the husks standing against Callie's
    lean-to, so the lee and the arrows hold the road together.
  - The line opens and closes for the cart. The six hear the watch using their handoff words.
  - A roll call of every post comes before the big push, and the push itself moves across every
    post.
  - The draw station is on camera, including Jab's chosen stop, while Toren holds the lane with
    his back to it. That reverses Caul Hill, where Callie had her back to the room.
- **"Everybody back" as doctrine and as return:**
  - It is Dessa's call at every push.
  - "Behind the lamps." / "They were behind the lamps."
  - After her count: "It was the call she had given across the Sag all day, for a push. Nobody
    moved for it now. They were all behind the lamps already, the watch and the six together."
  - The last walk keeps the lamps lit and the watch on them.
- **Dessa commands throughout.** Toren states what the party has, asks, and assigns only inside
  her orders ("Who comes off, and who takes their place?"). His stake stays in his settles and in
  the count at the gate.
- **Preserved:** a 163-item check of canonical lines, numbers, costs and plants found every item
  present. The accepted Movement Six repairs are kept:
  - "sick inside an hour of it coming up" and "since the fourth hour";
  - "Two days" and "thirty paces";
  - "I felt it go round you, from the road";
  - Jab's late call backed by Callie;
  - Callie's ch 39 bridge;
  - the six lines spoken for the ear.
- **Audio:**
  - every speaker is named where it could be in doubt;
  - there are no semicolons in the narration;
  - one sentence runs past 40 words, and it is canonical;
  - two sentences I had merged were split back to canon's form;
  - there is one consecutive same-speaker pair (Wyck's "I'm cleared tomorrow" and then
    "*Taking*"). It is kept as canon has it, with an explicit tag.

### Material departures

None changes an event, a cost, a count or an outcome.

1. **Camera and heading:** the POV name is gone. The chapter no longer passes the whole hold
   through Toren's ears.
2. **Breaks:** 14 → 7, falling at changes of place or task.
3. **Visible beats added:** the opening sightline; the line reforming, with every head turned but
   Katori's; the station roll call; Callie kneeling beside the hook again at the top of the made
   road; Dee putting the fence's fourth to Jab's palm; Jab's nod; Dee at the wheel on the way to
   the gate. The full list is in `CONTINUITY.md` §11.
4. **Two new procedural calls:** Jab's "Clean" as he finishes Otto, and Katori's "Now", which
   keeps her own "I'll say".
5. **Jab's stop is shown from inside,** in one settle, instead of being heard only by Toren.
   Toren's line about the silence is kept, as his settle at the lane.
6. **Canonical lines re-split or retagged for the ear.** For example, "Callie," said Toren.
   "Ground." In the south-lip greeting, "He had not seen her face since the forty-first" becomes
   "None of the six had seen her face since the forty-first."

### Word count and metrics

| | Canon | Staged |
|---|---:|---:|
| Words (`wc -w`) | 7,065 | 7,593 (+528, +7.5%) |
| Section breaks | 14 | 7 |
| Words per section (script) | 470 | 948 (formula proxy ~950) |
| Mean / median sentence | 7.6 / 5 | 8.3 / 5 |
| Sentences ≤5 words | 56.2% | 52.5% |
| Flesch / FK | 102.4 / 0.9 | 101.4 / 1.2 |
| "the way" / "for a long time" / "did not say anything" / "It was not" | 24 / 3 / 0 / 4 | 23 / 3 / 0 / 4 |

### Needs editorial judgment

1. **Length.** The chapter is 7.5% longer, against 1.4% for chs 33–40. Almost all of the growth is
   the one-field material and Jab's settle. If the owner wants parity, the likeliest trims are
   the station roll call and the opening sightline, about 120 words. But those are what carry
   the one-field direction.
2. **Callie at the top of the made road.** She kneels beside the hook, which canon leaves
   unstated. That fits her corner lesson and ch 46's "On the steel. Not on me."
3. **Jab's stop shown from inside.** Is one settle right here, or should the stop stay audible
   only?
4. **"A stone. Full."** Toren still says this after holding the corner strut for four breaths.
   It is canon's wording, and I kept it.
5. **The gloss at the count.** Check that the "Everybody back" line after Dessa's count reads as
   the company's moment and not as the narrator explaining.

### Verification

- **Canon untouched.** Canonical chs 33–40 and 44–46 still equal the pre-revision manifest. The
  frozen first draft and its three records match their hashes. No canonical file was opened for
  writing.
- **Accepted chs 33–40 untouched.** They and the shared records were identical in the worktree
  and the main checkout when this run started, and I did not edit the chapters.
- **Git.** Nothing was committed, pushed or promoted. `git status` shows only untracked staging
  files.
- **Where the files are.** The staged `chapter-45.md` and the updated `CONTINUITY.md` and
  `AUTHOR-REPORT.md` are in the worktree only. The main checkout's staging folder has no ch 45
  yet. Also, §10's note that the worktree holds the pre-recheck text is out of date: both copies
  carry the recheck fixes. To mirror this run into the main checkout, copy these three files:
  ```
  cp /Users/drive/kindling-repo-stage/.claude/worktrees/meridian-m5-ensemble/books/book-02-meridian/revisions/ensemble-2026-09-29/manuscript/chapter-45.md /Users/drive/kindling-repo-stage/books/book-02-meridian/revisions/ensemble-2026-09-29/manuscript/
  cp /Users/drive/kindling-repo-stage/.claude/worktrees/meridian-m5-ensemble/books/book-02-meridian/revisions/ensemble-2026-09-29/CONTINUITY.md /Users/drive/kindling-repo-stage/.claude/worktrees/meridian-m5-ensemble/books/book-02-meridian/revisions/ensemble-2026-09-29/AUTHOR-REPORT.md /Users/drive/kindling-repo-stage/books/book-02-meridian/revisions/ensemble-2026-09-29/
  ```

### Fresh-context closeout

The Chapter 45 seam recheck returned `ACCEPT AFTER SURGICAL FIXES`. Both required local fixes
were applied: the lamp-line is again on the east slope, and the Sag-bottom paragraph now
acknowledges that all six crossed it on D+41. The final gate is `ACCEPT`; no broad rewrite or
optional polish followed the recheck.
