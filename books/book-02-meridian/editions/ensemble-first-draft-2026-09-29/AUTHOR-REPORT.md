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

---

*The Chapter 45 ensemble run appends its own section below this line.*
