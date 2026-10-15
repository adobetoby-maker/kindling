# Kindling 2680, Book Two — Movement Three — consolidated repair record

> Built by TAC

Date: 2026-10-15. Status: **same-author repair of chapters 17–24, in place. Not rechecked, not
cold-read after repair, not accepted, not committed, not pushed, not published.** Chapter 25 was not
drafted. No Movement Four work was done.

## 0. Who, how, and from what

- **Seat:** Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline Monroe Jackson. Requested author:
  Claude Opus 5.5.
- **Runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.**
  This is what the runtime states. It cannot be verified independently from inside the session. No
  subagent, other model or delegated worker wrote or edited any prose or record. No codex or OpenAI
  call was made.
- **Session:** Claude Code background job `8e3ee375` (job directory `~/.claude/jobs/8e3ee375`); remote
  session `session_01Qyomxormkxi2vUXobQ81Fh`. The job ran on 2026-10-15, from about 00:29 MDT.
- **Brief:** delivered in-session. On inspection its text matches
  `planning/OPUS-5.5-MOVEMENT-003-REPAIR.prompt.md` (187 lines), SHA-256
  `c0ca27554b17df3e7dc9ee0d8036cd9555183e4cf1fc750019852dc8d1b380fb`. No byte comparison of the
  delivered text was possible.
- **Isolation:** worked in place in the git worktree `/Users/drive/kindling-2680-book-02`, branch
  `codex/kindling-2680-book-02`. No commit was made.
- **Evidence read, in the brief's order, before the first edit:**
  1. `provenance/MOVEMENT-003-EDITORIAL-REVIEW.md` (in full)
  2. `provenance/MOVEMENT-003-COLD-READ.md` (in full)
  3. `provenance/MOVEMENT-003-CONTINUITY.md` (in full)
  4. `STATE_LEDGER.md` (sections 1–2 and the Movement Two and Three blocks), `UNIVERSE_BIBLE.md`,
     `BOOK_MAP.md`, `CHARACTERS.md` and `packets/MOVEMENT-003.md` (in full)
  5. `manuscript/chapter-17.md` to `chapter-24.md`, completely and in order
- **One targeted check outside Movement Three:** a search of chapters 10–16 for how a lodger is
  killed (C20). Nothing in chapters 1–16 was edited.
- **Both reviews are simulated reads by the same model family.** Neither is human reader feedback.
  This repair shares their blind spots.

## 1. Factual corrections (priority 1)

Line numbers below are first-draft numbers in `editions/movement-003-first-draft/`. Each fix is the
smallest edit that makes the line agree with its scene. No event, outcome, date, ash total, power
limit, injury, knowledge boundary or reserved disclosure changed.

| # | Where | Was | Now | Evidence |
|---|---|---|---|---|
| F1 | ch. 19:259, 269 (lane 2, carries 1–2) | Carry 1: three to Seven, no down. Carry 2: "Four to three, to them." Carry 3: "Six to Seven." The carries summed to 5–4. | Carry 1 now shows the down: "Their blade shut and ran for the hazel to stop it, and Jude was there first and put the flat of his edge on him before he could open again… three to Seven and a down". Carry 2 now ends "Four all." Carry 3 is unchanged. Total 4 + 2 = **6–4**. The board (ch. 24, "twelve for, sixteen against") is untouched and now agrees. | Review C1; cold read A1. The down follows the lane-1 lesson (a laid player must shut to run). |
| F2 | ch. 18:229, 247, 269 (lane 1, carry 3) | "Kiva had her still door declared and no hands for a litter. That was the rule." This seemed to contradict carry 1, where Carrow carries with nothing open. | One stated rule, in Seven's terms: Kiva is "at the hurdle with her door open on it, holding it planted"; "Seven's catcher kept her hands off the poles while her door was open; if she shut it to lift, the hurdle would stand unplanted with Carrow two paces off. That was the rule, and Seven had chosen it." Carrow's line now reads "Not while your door's on the hurdle, and it's the only one you're let open." | Review C2. Carrying needs no door (carry 1 stands as legal). The constraint is Seven's chosen use of its only declared catcher's door. |
| F3 | ch. 18:467, 515, 525 (Anwen cutaway, Thursday evening) | Lyle: "This morning" ×2, and "I saw you do it this morning… You walked it from the far end." Narration: "that morning in the lane." | "Yesterday" (lane 1 was Wednesday). Lyle now points at what she did see on the page, Anwen's lean: "Somebody taught you to lean from the floor. Did they teach you to walk a wall as well? On your own?" Narration: "yesterday in the lane". No scene added. | Review C3. The brief listed two "this morning"s. A third ("that morning in the lane", 18:525) was found and fixed. |
| F4 | ch. 23:3 (Friday morning) | "That's two nights to go" | "That's **three** nights to go". The sixth was Thursday morning and warmth came Monday at seven: Thursday, Friday, Saturday and Sunday nights. Sunday's "One night to go" was already right. | Review C4; cold read A3. |
| F5 | ch. 20:355 (Rhea at dawn) | "for six years she had had a catcher who watched her heel and a second who watched the far edge" | "a catcher who watched her heel, and since the first month a second who watched the far edge". This now agrees with Pike's "I did both for twenty years before there was ever a second in this van" and with the slate line dated from the first month. | Review C5; ledger M1.3. |
| F6 | ch. 20:393 (Rhea's slate) | *Tinned: six bags… The sixth bag light.* | *Tinned: **seven** bags… The **seventh** bag light.* Three purses were shut at the high-water slack (posts 1–3) and four at dawn (5, 6, 7, then the fourth, light). | Review C6; cold read A2. Records reconciled (§6). |
| F7 | ch. 21:229 (the Hoop, Tuesday) | Quiet at 6.12, ring down at 6.35, but "stood for twenty-one minutes" (23 by the clock). | "At six thirty-three". Now 6.12 + 21 = 6.33. Wednesday (6.13 to 6.33, twenty minutes) is unchanged. The slack's start times are untouched (see §5, C12). | Cold read A4. The prediction's 18–22-minute window is unaffected. |
| F8 | ch. 20:319 (Rhea at dawn) | "at twenty past six", with the slack a few minutes off, then "Low water slack: a quarter past six". | "at **ten** past six". | Cold read T1. |
| F9 | ch. 22 (Thursday's order) | The noon hand check, with its 4 p.m. and 10 p.m. follow-ups, came before Adlam's 11.30 visit. Adlam's line had to say "that morning, before the noon". | The hand-check block moved, unchanged except for its opening clause, to just after the wire scene: "Aske had the hand at noon, when they came back up the loft stair, by the north window." Adlam's line now reads "at half past eleven, as he had promised". The day now reads forward: 7.00 crossing, 7.15 signing, 11.30 Adlam, the wire, noon, then 4 p.m. and 10 p.m. in summary, then Kellan at 7 p.m. No new scene. | Cold read T2. |
| F10 | ch. 24 (Monday morning, the Bench) | Perrin on Sunday: "If my ribs go on the Bench tomorrow"; Perrin on Monday: "watch Halden do it, and Old Four, and Twenty-Eight". | Monday's line is now "watch **us** do it, and Halden, and Old Four, and Twenty-Eight". By the book's structure Seven is entered and stands at the Bench without Kiva (`BOOK_MAP` Movement Four: "The Bench, without Kiva"; the Chair's condition "not at the Bench" binds Kiva only). Perrin's Sunday line was correct, so it is unchanged. | Cold read T3. Who stands in Kiva's place is not stated on the page and was not invented. |
| F11 | ch. 21:349 (Hart, Wednesday) | "Your aunt said the same thing yesterday… On the gallery." On the page Mara said only "It's the bank's" and "How", and it was Hart who said "as if the count goes out of the harbour… and into that". Hart's "I never said it to anybody" also contradicted the page. | "Your aunt asked me *how* yesterday… On the gallery. I told her what it looks like. It was the first time in six months I'd said it aloud, because I couldn't prove it… You've said it without being told. And you've said more than I did… That goes in my book. Somebody else got there by herself." | Cold read K1. The recast also removes one "I'd want" (§4). |
| F12 | ch. 24:197 | Trewin: "plant on the Ropewalk's boards on Tuesday" | "on the **gate's** boards". The reading was at the gate mast in the timber pond (ch. 21). | Review C7. |
| F13 | ch. 24:39 | "at the gate, a fortnight ago" | "at the gate, **eleven days** ago" (Tuesday the 1st to Saturday the 12th). | Review C8. |
| F14 | ch. 19:97 (Mara) | "I was on a transit two days behind you". At the fever (Friday the 27th) she was still in Meridian. | "Then I meant to write to you at the house of the Even Hand. Then you had a fever on the ferry, and I heard of it at the kitchen table with my bag not yet packed". This also makes clear that "at the house of the Even Hand" meant by letter. No day count is given, so none can be wrong. | Review C9. |
| F15 | ch. 17:167 (Kellan) | "My mother sent it on." | "My mother **wired** it on." | Review C10. |
| F16 | ch. 21:165 (Carrow) | "Maud told me last night." | "Maud told me." | Review C11; cold read K2. |
| F17 | ch. 19:245 (Hart) | "Your sponsor's in town," he said. | "Your sponsor's in town?" he said. | Cold read §5. |
| F18 | ch. 22:35 | "a pair of brass ones that he must have brought in the black book's spine" | "The old man had his own dividers out, a small brass pair, and he had measured before Noa had." | Review P3. |
| F19 | ch. 21:301 (Mara) | "eleven minutes that the low town would bear on a making tide" (unexplained) | "the eleven minutes **without pumps** that the low town would bear" (two words of gloss). | Review P3. |
| F20 | ch. 20:399 (slate) | "walls laid flat on the water" | "walls **lying** flat on the water". This keeps *laid* for the doctrine. | Review P3. |

**C20 checked, not edited.** "She had not told Lyle that a lodger could be killed, or how" (ch. 18).
Chapter 13 shows Coombe's order "There's a lodger. Kill it." and Jude's kill "through the grey cord
lying on" the coping, with Anwen on the floor (ch. 13:341, 357; logged in the license book at 13:501).
Seven knows that a lodger can be killed and how. The line agrees, so it was left.

**"Nothing came" (ch. 23), C19.** No prose change, as the brief instructs. Recorded in the ledger and
the continuity file: Aske and Pru now suspect that Kiva expected something to come with a fever. They
know nothing of the content.

## 2. Structure and sentences (priority 2), by chapter

### 2a. `---` breaks removed: twenty

Section numbers are 0-based first-draft numbers, after splitting on `---`. Each join keeps the place,
the time (within minutes) and the lens. No prose was cut at any join. Transitions added: one clause in
ch. 18 ("It was the third carry, and…"). Elsewhere the existing first sentence already carried the
join.

| # | Chapter | Join | Scene |
|---|---|---|---|
| 1 | 18 | §1 \| §2 | lane 1: "Go," and Lyle in the pen |
| 2 | 18 | §2 \| §3 | lane 1: after carry 1 ("Seven stood behind its hurdle in silence") |
| 3 | 18 | §4 \| §5 | lane 1: "Watch the catcher" / the pause between carries |
| 4 | 18 | §5 \| §6 | lane 1: into carry 3 ("It was the third carry, and Carrow saw it") |
| 5 | 18 | §6 \| §7 | lane 1: the tally / Carrow at the hurdle |
| 6 | 19 | §8 \| §9 | the 146-word Sunday bridge (Aske, "Warm") folded into the Yeo section |
| 7 | 20 | §2 \| §3 | high-water slack: first post / second post |
| 8 | 20 | §3 \| §4 | high-water slack: the third purse / the slack's end |
| 9 | 21 | §0 \| §1 | gate reading: "No," said Perrin / everybody looked at him |
| 10 | 21 | §1 \| §2 | gate reading: the Clerk's "Then read it" / the reading |
| 11 | 22 | §2 | the 125-word noon hand check moved and folded into the wire section (F9) |
| 12 | 22 | §3 \| §4 | Adlam: the bench books / the offer (one speech, interrupted only by the break) |
| 13 | 22 | §6 \| §7 | the Proprietor's dinner |
| 14 | 22 | §7 \| §8 | the 224-word walk back (Kellan's lens) folded into the dinner section |
| 15 | 23 | §3 \| §4 | the Counting House: the stair / the long room |
| 16 | 23 | §4 \| §5 | the long room / "He was not what she had expected" |
| 17 | 23 | §5 \| §6 | drawing out the cord / laying the disk |
| 18 | 23 | §7 \| §8 | the window / the ask |
| 19 | 24 | §2 \| §3 | lane 3: second carry / third carry |
| 20 | 24 | §7 \| §8 | the van yard: the plan / "Pru folded at ten past ten" |

**Breaks kept on purpose inside the targeted runs:**
- ch. 18 §3 | §4, after "Carrow had to run." The pause after a protected beat.
- ch. 23 §6 | §7, after the disk goes back "cold", before "Seventy-seven years tonight."
- ch. 24 §1 | §2, after the declaration murmur, before "She had never watched Seven from above."

Every break before and after a non-Kiva cutaway was kept. The joins stopped at twenty to stay inside
the brief's 15–20 range. Some continuous joins were not used, for example ch. 18 §9 | §10 ("There's a
notch" / "He said it very quietly"), kept as the revelation's pause.

Internal breaks: **79 → 59.**

### 2b. Long hierarchical sentences written (40–55 words, descriptive set pieces only)

Word counts use the script's tokenizer.

| Chapter | Set piece | Words | Shape |
|---|---|---:|---|
| 17 §1 | the Mole | 49 | "It was a great curved wall… which came out… and bent round…, so that the sea broke white along its outside while the water within it lay flat and brown, crowded with masts." |
| 17 §4 | the Graving | 55 | "…with stone steps going down its sides in tiers like the seats of a theatre, so that a whole town could sit on its walls and look down at whatever was done on its floor." |
| 18 §0 | the Ropewalk | 43 | "Then, when she saw the chimneys…, where somebody was boiling tar, she understood that it was a building, and that it went on along the ridge…" |
| 19 §2 | the pump-house hall | 46 | "…with windows high in its roof from which the light came down onto two rows of cells…, that stood along a gallery…" |
| 20 §0 | the kiddle | 45 | "…when they first saw one, because it was the old coast word for a fish weir, the kind of fence of stakes that men had once driven across a creek…" |
| 21 §4 | the Hoop rising | 53 | "Although there was nothing to hold it but a ring of grey set on the mud like a wall round a pond, it stood up inside the ring…, as though the ring were a cup and somebody had filled it." |
| 23 §3 | the Counting House stair | 43 | "Whether they hung on brass brackets or stood in glass globes… or burned in the great iron ring…, every one of them was white, and not one of them flickered." |
| 24 §1 | the Graving full | 46 | "The iron and glass roof went over all of it, so that the light, which came down through the glass… as it comes into a church, fell alike on green and buff and on the white chalk of the pen eighty feet below." |

Chapter 22 already had one (the Counting House exterior, 46 words), and none was added. Each new
sentence has one main clause and no *and…and* clause chain. The longest sentence in the movement is
now 55 words (ch. 17, the Graving). One 46-word sentence that came out of the F2 fix, in the middle of
lane 1's action, was split in two so that no long sentence sits in a fight.

### 2c. Short narration declaratives joined (reflective passages)

- **ch. 22 §1** (the certified crossing): three paragraphs of 5–10-word sentences joined into 20–35-word
  sentences ("It was certified: two crossings now…, in her name, on her certificate, on ordinary
  terms"; "Pru could fold; Perrin could carry, in his way; a girl in the Ropewalk…"). "She found that
  she was glad of it in a way that she had never been glad of the three" is unchanged.
- **ch. 23 §7** (the window): "She had told nobody, not even Mara…"; "Her jaw ached; she had her teeth
  together so hard…, and her hands in her lap were hot." "She kept her mouth shut." stands alone, as
  before.
- **ch. 24 §10** (the yes/no book): "That was all: one line, which told her only what she had known since
  the first night…"; "…wherever she was, and the day after, and the day after that."
- **ch. 21 §8**, the same kind of run (see §4, negation).

### 2d. First-read footholds (cold-read priority 3)

- **ch. 17 §6, the rule's history.** The single paragraph is now three beats around Carrow's walk to the
  cross:
  1. before the clerk calls: what the rule is and how it reached the Board
  2. after Orla names Carrow and Lyle: "The rule had been written for Kiva… Now a girl with a rope on
     her sleeve had walked out under a mast of the same kind, in her own town."
  3. after "Hush.", just before "Carrow went to the white cross": Dray's request, "it said *any
     candidate*", and the Board reading it as written

  The text is the same apart from the one bridging sentence in beat 2.
- **"Hand door", first use (ch. 18, the fifth crossing).** After "*Hand,*… *To Ember*", this is added:
  "*Hand,* on a reader's list, meant her hand door: the ward, the low tray that a catcher lifts and
  folds a load on. It did not mean the left hand at the end of her arm, though that was the one that
  would pay."
- **"She's a hand door" (ch. 24).** After Aske's line, this is added: "Aske meant Pru's one door, the
  ward, the tray she lifted and folded with, and not a hand like the cold one in Kiva's own blanket."
- **"Hold" as a reading (ch. 22, Kellan's recital).** "Her Hold reads Edge three-one…" is now "On the
  Hold rig she reads Edge three-one…". The rig marks it as a measurement, not Anwen's role.
- The "Kiva:" chapter titles are unchanged. Every cutaway already opens on its lens by name.

## 3. Measures, before and after

Command, run from the book directory before the first edit and after the last:
`python3 -I provenance/tools/m3_metrics.py manuscript`. The script was not modified (SHA-256
`12036c794861f73e868759a4f73c511186146e751513de7c1af8db0747eb07cd`, the same before and after). It is a
heuristic, not a gate.

### 3a. `wc -w` (headings included)

| Chapter | First draft | Repaired | Change |
|---|---:|---:|---:|
| 17 | 7,120 | 7,158 | +38 |
| 18 | 8,055 | 8,132 | +77 |
| 19 | 7,577 | 7,611 | +34 |
| 20 | 7,090 | 7,091 | +1 |
| 21 | 6,578 | 6,562 | −16 |
| 22 | 5,810 | 5,784 | −26 |
| 23 | 6,517 | 6,511 | −6 |
| 24 | 5,735 | 5,761 | +26 |
| **Movement** | **54,482** | **54,610** | **+128** |

The rise is the two footholds, the rule beat, the lane-2 down and the long set-piece sentences. The `---`
lines removed account for −20 words in the counts.

### 3b. Script output

| Measure | Target (formula) | First draft | Repaired |
|---|---:|---:|---:|
| Body words (script tokenizer) | — | 54,351 | 54,499 |
| **All text:** sentences | — | 5,700 | 5,678 |
| All text: mean | 14.6 | 9.54 | 9.6 |
| All text: median | 11 | 7 | 7 |
| All text: population SD | ~26 | 7.92 | 8.05 |
| All text: ≤5 words | 27.7% | 40.3% | 40.3% |
| All text: ≥40 words | 3.3% | 0.4% | 0.5% |
| All text: longest | — | 52 | 55 |
| **Narration only:** median | waypoint 8–9 | 7 | 7 |
| Narration: mean | — | 10.7 | 10.8 |
| Narration: SD | — | 8.9 | 9.1 |
| Narration: ≤5 words | waypoint ~33% | 37.3% | 37.1% |
| Narration: ≥40 words | waypoint 1.5–2.5% | 0.6% | 0.8% |
| Dialogue only: median / ≤5 / ≥40 | (not reshaped) | 4 / 60.1% / 0.0% | 4 / 60.3% / 0.0% |
| Paragraph median / mean | 18 / 26.8 | 21 / 32.2 | 22 / 32.2 |
| **Sections** (including chapter openings) | — | 87 | 67 |
| Section mean / median | ~950 | 625 / 606 | **813 / 644** |
| Sections under 400 / at 900+ | — | 16 / 11 | 8 / 19 |
| **Breaks per 10k**, internal `---` only | ~8.7 | 14.54 | **10.83** |
| Breaks per 10k, including chapter openings | — | 16.01 | 12.29 |
| Flesch Reading Ease / FK grade | 72.3 / 6.8 | 96.1 / 2.2 | 96.0 / 2.2 |
| Progression hits per 10k (raw) | 58 | 55.9 | 56.3 |
| "she did not" per 10k (house trigram) | — | 16.2 | 14.5 |
| Reserved terms: "Unroofed", "Breach"; real month names | 0 | 0, 0; none | 0, 0; none |

**Read.** The scene-structure priority moved as intended. Sections average 813 words and internal breaks
are 10.8 per 10k, against a formula of about 950 and 8.7. That is the editor's estimate of what
removing 15–20 breaks would do. **The sentence waypoint was not reached.** The narration median is
still 7, the short share 37.1% and the long share 0.8%. The repair wrote eight long sentences and joined
four reflective runs, as instructed, and did not chase the number. Because the brief limits long
sentences to descriptive set pieces and leaves dialogue alone, they cannot move a 5,678-sentence
distribution much. Whether to go further is the owner's question in §5.

### 3c. Viewpoint

The script's viewpoint map is keyed to first-draft section numbers. After the joins, it attributes the
wrong sections; unmodified, it reports Kiva at 94.7%, which is an artefact. The shares were recounted
with a scratch copy of the script in which only the map changed. That copy is not kept in the
repository. Its SHA-256 is `f2fcf5db6cf0b2afdce6a01a7a2e2f918d8168b72e4e073ea4077cdcabd5a09f` and its
whole difference from the original is:

```
POV = {(18, 7): "Anwen", (19, 9): "Orla", (19, 10): "Orla", (20, 5): "Rhea", (20, 6): "Rhea",
       (21, 2): "Mara", (21, 3): "Mara", (21, 4): "Mara", (22, 4): "Kellan"}
```

| Lens | First draft | Repaired |
|---|---:|---:|
| Kiva | 44,806 (82.4%) | 44,955 (82.5%) |
| Anwen | 1,398 (2.6%) | 1,393 (2.6%) |
| Orla | 1,871 (3.4%) | 1,870 (3.4%) |
| Rhea | 2,022 (3.7%) | 2,026 (3.7%) |
| Mara | 2,426 (4.5%) | 2,423 (4.4%) |
| Kellan | 1,828 (3.4%) | 1,832 (3.4%) |
| Cutaways | 9,545 | 9,544 |

The cutaways remain 44 words over the packet's 9,500 ceiling, as recorded at drafting. Nothing was
trimmed for it.

## 4. Voices and read-aloud (priority 3)

### 4a. Counts, before and after

Counts are grep counts over chapters 17–24. The frozen edition is "before". Definitions:
- "I'd want" is the literal substring, so it includes Jude's "I'd wanted". This matches the review's 28.
- "Blush red" uses the regex `(went|gone|going|very|dull) red\b|not red any`. "Scarlet" is counted
  separately.
- "Causal *since*" counts the five sites listed in the review.

| Phrase | Before | After |
|---|---:|---:|
| "I'd want" | 28 | **14** |
| "want it said" | 11 | 11 |
| "I'd like it known" (Perrin's) | 7 | 7 |
| "said nothing" | 22 | **10** |
| "did not say anything" | 14 | **5** |
| "scarlet" | 9 | **7** |
| blush "red" | 12 | **3** |
| "in two stages" | 5 | **2** |
| "so that it's said" | 3 | **2** |
| causal *since* | 5 | **0** |
| "she did not" / "he did not" | 88 / 58 | 79 / 55 |
| "nearly smiled" (Pike) | 3 | 3 |
| "soonest" (Aske) | 6 | 6 |

### 4b. What was recast, and in whose register

- **"I'd want…", fourteen recast:**
  - Perrin (ch. 17, the litter): "I'd pay money to know…"
  - Kiva (ch. 17, the comb): "Please write that beside whatever the comb says."
  - Pike (ch. 19): "The first wants them all the way to the palm, and the second wants the thumb hard."
  - Yeo (ch. 19): "I mean to know before the sea does."
  - Peverell (ch. 21), in her columns: "Enter that in your book before you go any further."
  - Hart (ch. 21, F11): "That goes in my book."
  - Kellan (ch. 22), as a sum: "That's one side. The other side is that I told you this anyway." /
    "Add that in."
  - Mara (ch. 23), dry: "that goes in too."
  - Orla (ch. 23), brief: "Mark that, in this house."
  - Pru (ch. 24): "You should know that."
  - Orla (ch. 24): "You'll hear it from me and not from him." / "I've never signed anything I was
    gladder to."
  - Hart (ch. 24), plain: "I've said so now. To somebody."
- **"I'd want…", kept:**
  - Jude's twelve (his diffident form)
  - Anwen's "I'd want somebody to tell me… I want it said"
  - Aske's price speech before the fifth ("I'd want you to know that I think so, and that I've written
    it on the card already"), because it is about price
  - The three "I want it said" are all Anwen's and stay.
- **"so that it's said":** kept for Aske's price (ch. 22) and Kiva before the Counting House (ch. 23).
  Perrin's in ch. 18 is now "I'm saying it out loud."
- **"said nothing" / "did not say anything":** about half cut or varied: "held her tongue", "was quiet",
  "kept it to himself", "without a word", "left it there", or the sentence dropped where the next
  action carries the silence. Kept:
  - the fingers' "said nothing" (the slack motif, ch. 20)
  - Pike's "said nothing, because it lay down"
  - Rhea's closing line in ch. 20
  - Hart's two pauses
  - the Proprietor's "You've said nothing" (dialogue)
  - Rhea's "said nothing at all" on the tailboard
- **Scarlet and red:** all of Pru's are kept: scarlet ×7, "went red" ×2, "without going red". Others now
  have their own tells:
  - Perrin: a jaw set at the hinge (ch. 18, 21), rubbing the back of his neck (ch. 19, 24), looking at
    his big hands (ch. 23), clearing his throat (ch. 23), shifting the rope on his shoulder (ch. 24)
  - the Tarn reserve: "Her chin had begun to shake"
  - the Ropewalk child: "his face screwed up tight"
  - Yarrow: "had put his fork down"
- **"in two stages":** all five were Orla getting up. Kept at its first use (ch. 18) and on her crate in
  ch. 24. The other three now read "got up off it", "got up off the crate" and "got up, stick first".
- **Causal *since* → *because*:** all five (17:331, 17:427, 18:289, 20:85, 21:287). Four are in dialogue
  and were changed because the brief names them.
- **Negation runs:** recast into positive statements in Kiva's three densest reflective passages:
  - ch. 21 §8: "She trusted Mara. What she lacked was any knowledge of what she had seen…"
  - ch. 23 §7: "She had told nobody, not even Mara… What she had seen was still a thing without a
    name…"
  - ch. 23 §10: "she had told him nothing in return… she had no idea what she would have told him"

  "She had not told anybody. She had not told Mara. / She did not tell Mara now." (ch. 21) is kept, as
  the beat that matters.
- **Protected and untouched:** Perrin's "I'd like it known", Aske's "soonest", Pike's "nearly smiled"
  (3), Hart's turned watch, the Proprietor's courtesy, and every strength the brief lists, including
  "It's every count at once", the Tarn jar, "*Laid*… as a man says *amen*", "There's no gap… Carrow had
  to run", the barometer, "It's yours", *Far edge*, Rhea's remark, "She's—" / "There.", the Hoop line,
  "The tape does not know the difference. The lodger did.", the hand on the glass, Pru's "I'm not
  grateful", *yes or no*, and the scene-ending beats.

## 5. Requested or flagged items left unchanged, with reasons

| Item | Left because |
|---|---|
| C12 / T4: the harbour slack moves one minute between consecutive days (6.12 Tue, 6.13 Wed) | Owner and Movement Four item, by the brief. Recorded here and in the continuity file. F7 changed only the Tuesday *end* time (6.35 → 6.33). No slack start time moved. |
| C13: the 41-minute hold against a twenty-minute quiet | Owner item. Unchanged. |
| C14: the brown-ink "temperature" line as a keeper's-book gloss | Owner item; needs a Book One check. Unchanged. |
| C21: "my best machine" | Owner item. Unchanged. |
| C19: "Nothing came" | A decision made on the page. No prose change; knowledge recorded (§6). |
| C20: "a lodger could be killed, or how" | Agrees with ch. 13 (§1). |
| C15: the Graving used as a seeding floor (lane 3) | Recorded as an accepted departure in the continuity file, as the brief directs. The owner may revisit it. |
| C16: Rhea's slate template written out again | Recorded as an accepted departure, as above. The only slate change is F6 / F20. |
| C17: `BOOK_MAP` §12 maps Rhea going short to Movement Four | A one-line dated note added to the map. The plan row itself is not rewritten. |
| Sentence targets for dialogue, and how long a read-aloud "long" sentence may be | Owner item. Dialogue was not reshaped for length. The few dialogue lines changed were for voice or fact. |
| Front-load progression arithmetic (whole-book 58 against 1.7×) | Owner item. Not addressed. Raw density is 56.3 per 10k, unchanged in substance. |
| Aske's "a four that's been waiting a fortnight for you" (ch. 24, Saturday) | Not flagged. Spoken loosely, and the eleven-day count is now on the page in narration (F13). Noted for a recheck. |
| T5: the first fever broke "on the barge" against "on the ferry" | Not in this brief, and possibly settled in Movement Two (ferry, then barge). Unchanged. |
| Cutaways 44 words over the 9,500 ceiling | Recorded at drafting. Not trimmed. |
| Chapters 1–16 | Not touched. No located contradiction required it. |

## 6. Records reconciled

- `provenance/MOVEMENT-003-CONTINUITY.md`:
  - lane 2 by carry
  - the catcher rule
  - seven bags
  - Hoop times 6.12–6.33 on Tuesday
  - Hart's and Mara's lines on the Hoop
  - Thursday's order
  - Seven at the Bench
  - the "three nights" count on Friday
  - Lyle's "yesterday"
  - Mara's kitchen table
  - the "Nothing came" knowledge row
  - C12 and C13 as open owner items
  - C15 and C16 as accepted departures
  - sections and breaks after repair

  Each is marked *(repair)*.
- `STATE_LEDGER.md`, Movement Three block: status line; lane 2 tally; the catcher rule; Seven at the
  Bench; the Hoop's Tuesday times; seven bags; the "Nothing came" row; open owner items.
- `BOOK_MAP.md` §12: one dated note (C17).
- `AUTHORSHIP.md`: a repair entry.

## 7. Frozen edition and integrity

- `editions/movement-003-first-draft/` was not modified. `shasum -a 256 -c SHA256SUMS.txt` returned OK
  for all eight files before the first edit and after the last.
- Repaired chapter hashes (SHA-256):

| File | SHA-256 |
|---|---|
| chapter-17.md | 1aaa7d0c5dca778d9ee417ec3d150dc699d0f8d42e535df3a3bd4ad40ce9e0e2 |
| chapter-18.md | 4a4aba68311d38d78c443740d506c1a6303f9144a098da4bf1130d24460aadf9 |
| chapter-19.md | 0f20ea26daf750c8afcda43fee1e6169365f5f3c304ca80ec56da21efc644982 |
| chapter-20.md | e5e81ac2b8101dc8ff9027b01eac6126525c9f4afc021b2ccb4ebea57ad4b4b4 |
| chapter-21.md | a3684d2b25cf7dc4cd3029819d632c3aa582663b35e50a9611e704b4aaca5dcb |
| chapter-22.md | 9d66769d01be3e55e481533c179e45957b0d47c0e79182f0bbdd86ff4821b9f6 |
| chapter-23.md | 8d50b38a60665d6b842c7a9dcb1ed80c58595fe7168e62e030e3bf998b25ec0a |
| chapter-24.md | 12b01c9f8aeba25c47cfe3db0b38c785a6eb492df8febb38d0446ef61151e088 |

- Files this job wrote or edited: `manuscript/chapter-17.md` to `chapter-24.md`, this file,
  `provenance/MOVEMENT-003-CONTINUITY.md`, `STATE_LEDGER.md` (Movement Three block only), `BOOK_MAP.md`
  (one line in §12) and `AUTHORSHIP.md` (appended).
- During the job, two other files in the book directory changed. Neither was written or read by this
  job: `planning/COMPLETION-LOOP-STATE.md` (modified) and `packets/MOVEMENT-004.md` (new).
- Not done: recheck, acceptance, commit, push, publication, narration, any Movement Four work.

## 8. What a recheck should look at first

1. Lane 1 carry 3 and Carrow's line (F2). Does the stated rule read as natural to a thirteen-year-old,
   and does it square with carry 1 without a second reading?
2. Lane 2 (F1). Can the reader sum to 6–4 unprompted?
3. The ch. 22 order (F9). Does the noon check after the wire land as a quiet close before the Kellan
   cutaway?
4. The joined sections in ch. 18 and ch. 23 read aloud. Is any pause missed?
5. The new long sentences in ch. 17 and ch. 21, read aloud at speed.

## 9. Second repair (2026-10-15, about 01:00 MDT)

- **Why:** the fresh-context recheck (`provenance/MOVEMENT-003-RECHECK.md`, job `a495af2f`) found one defect,
  D1. Removing the ch. 23 §4 | §5 break (join 16 in §2a) left "He was not what she had expected." directly
  after a sentence about Perrin, so "He" read as Perrin.
- **Brief:** `planning/OPUS-5.5-MOVEMENT-003-SECOND-REPAIR.prompt.md`, SHA-256
  `e7a51af56f2753b465f6c8825c2468d96c5a25916105e1dcd54d0909ad2fad0a`.
- **What changed (one line, nothing else):** `manuscript/chapter-23.md:195`, "He was not what she had expected."
  → "**The Proprietor** was not what she had expected." Reversing that one line reproduces the first-repair
  hash of chapter 23 (`8d50b38a…`), so no other byte changed. New SHA-256:
  `71245a038c63cc2a06efe176402c6e56c41aad36e556ac56b70d448c9ae2b712`.
- **Word count:** chapter 23 is now 6,512 (`wc -w`; was 6,511). The movement is 54,611.
- **Runtime model, as reported by the session:** Claude Opus 5.5 (`claude-opus-5-5`). This cannot be verified
  independently. The work was done in the same conversation as the first repair (job `8e3ee375`), resumed as
  Claude Code background job `ca51c377` (job directory `~/.claude/jobs/ca51c377`); remote session
  `session_017cMe7z5eyXr3a7VbYBFSiv`. No other model or worker was used.
- **Frozen edition:** `editions/movement-003-first-draft/` still verifies with `shasum -a 256 -c SHA256SUMS.txt`
  (8 of 8 OK).
- Not done: no further recheck, acceptance, commit, push or publication.
