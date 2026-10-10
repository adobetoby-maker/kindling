# Kindling 2680, Book One — Prologue + Movement One — consolidated repair report

> Built by TAC

Date: 2026-10-10
Brief performed: `editor/MOVEMENT-001-REPAIR-BRIEF.md`
Author of the repair: Claude Opus 5.5 (`claude-opus-5-5`), Monroe Jackson 1.3.0 / O'Connor 1.3.0. Same selected author and model as the first draft. New session; no subagents; Movement Two not started.

**Status: repaired, not verified.** This report does not claim the movement passed. The three priorities still need the separate targeted recheck the brief requires. Section 5 lists where the result falls short of the numerical targets.

---

## 1. What was read before editing

- The brief, in full.
- Both reviews, in full: `editor/MOVEMENT-001-EDITORIAL.md` (including the metrics appendix) and `editor/MOVEMENT-001-COLD-READ.md`.
- Updated canon and planning: `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `STATE_LEDGER.md`, `CHARACTERS.md`, `PROLOGUE_PLAN.md`, `packets/MOVEMENT-001.md`, `packets/MOVEMENT-002.md`, and the uncommitted diffs to `IDEA.md`, `SERIES_MAP.md` and `README.md`.
- `provenance/MOVEMENT-001-CONTINUITY.md` and `AUTHORSHIP.md`.
- The complete manuscript, all nine files. The frozen edition at `editions/movement-001-pre-repair/` was verified byte-identical to the pre-repair manuscript by SHA-256 before any edit, and re-verified against its `SHA256SUMS.txt` after the repair. It is untouched.

## 2. Files changed

| File | Change |
|---|---|
| `manuscript/prologue.md` | Rewritten in place (same eleven snapshots) |
| `manuscript/chapter-01.md` … `chapter-08.md` | Rewritten in place (same scenes, same section order) |
| `provenance/MOVEMENT-001-CONTINUITY.md` | Reconciled to the corrected prose |
| `AUTHORSHIP.md` | Repair record added |
| `editor/MOVEMENT-001-REPAIR-REPORT.md` | This file (new) |

Nothing else was written. Canon, plans, packets, the reviews, the brief, the frozen edition and the compiled prompts are unchanged. Nothing was committed.

### Word counts (`wc -w`)

| File | Before | After | Change |
|---|---:|---:|---:|
| `prologue.md` | 16,089 | 16,621 | +532 |
| `chapter-01.md` | 5,419 | 5,547 | +128 |
| `chapter-02.md` | 4,527 | 4,650 | +123 |
| `chapter-03.md` | 5,229 | 5,285 | +56 |
| `chapter-04.md` | 5,796 | 5,898 | +102 |
| `chapter-05.md` | 5,262 | 5,567 | +305 |
| `chapter-06.md` | 5,497 | 5,822 | +325 |
| `chapter-07.md` | 4,822 | 4,957 | +135 |
| `chapter-08.md` | 5,560 | 5,828 | +268 |
| **Chapters 1–8** | **42,112** | **43,554** | **+1,442** |
| **All nine files** | **58,201** | **60,175** | **+1,974** |

The growth comes from joining words, the Cellhouse clarifications, and three new prologue closing images. The aftermath trims in chapters 6–8 removed text, but less than the clarifications added.

### Post-repair SHA-256

| File | SHA-256 |
|---|---|
| `manuscript/prologue.md` | `cb99ac12525973ba483417b82c9a3b675e2d3fbd8747dcf8f5b840df25d21c9e` |
| `manuscript/chapter-01.md` | `33f9cfad1b7472882b3e9a594e9896000481dcfdeef6a27903a39d255975cbb8` |
| `manuscript/chapter-02.md` | `01e3154d41a7a5b7e2acb293fb9da4088a32f02e9e0099209d0d3878f7e2343d` |
| `manuscript/chapter-03.md` | `9b74bb223f8be407836204bce3fc0fa4fefc9c48e538cbbd76e64208330ca273` |
| `manuscript/chapter-04.md` | `5c7e2fe9a0c3d6b6e3491365dd95c6138462dc0a4b6c5de098516887280550a6` |
| `manuscript/chapter-05.md` | `f8e7b09d81f67efd5a857474e9aaa305f3719044e741aa4488083c6cb948dfd7` |
| `manuscript/chapter-06.md` | `cc1ac83148f805812d4b6516e8e0bd4d588a02dd6df2f331cddf423b0b00a7ff` |
| `manuscript/chapter-07.md` | `a83948c2bfdde53c4bb9d145405f1040e8272925580d35f2a39e356c9b246ff5` |
| `manuscript/chapter-08.md` | `a7afe0d10e5fd278d37bf7dec767c8351534aa24b5028017efdf742b9513ef4f` |

## 3. Confirmation that all scenes remain

Checked three ways.

1. **Structure.** Section-rule counts are identical before and after in every file (prologue 19; chapters 7, 5, 7, 9, 8, 9, 7, 7), for 87 sections in total. All eleven `## N.` snapshot headings and all nine titles are unchanged.
2. **Viewpoint guards.** The editorial script's six cutaway assertions (Mara ch 2, Orla ch 3, Kellan ch 4 and ch 6, Anwen ch 7, Rhea ch 8) pass on the repaired files, so no cutaway moved or was dropped.
3. **By hand, against the brief's preserve list.** All present:
   - All eleven prologue snapshots, with the prologue still ending on the crooked post.
   - The full Terrace Ring bout: stacked start, first touch, the fall on the step, the stop-and-watch, "he never did," the bar, the sand, the long single-door defence, the riser half-point, the Stride behind her.
   - The full Cellhouse run: briefing, role argument, the hurry, the clock calls, the declared tuning, the joy, the fear, three doors into the cell, "I've stopped. It hasn't," over the rail, "one" under impact, Perrin holding, Kellan's decision from inside his own head, the quench, the release, the board.
   - The lowest-defensible-place ending and "I hope you hate it."
   - Mara's compromised yes on the embankment and her three household conditions.
   - Kellan's legitimate excellence (Fire at seventeen, the measurement backstory, the quench).
   - Perrin's warmth and candid envy; Anwen's independence ("the score first," "I want it anyway. On my own.").
   - The ledger ethic in every era, and the planted Unroofed Sky mystery (Annick notebook, the three T-0 lines, the dream recurrence).
   - Ysra's hand on the stop, "Responder," Rhea noticing the left hand, both cards, and every consequence.

No scene was shortened to solve a continuity problem.

## 4. Material decisions

### Owner rulings, as applied

1. **Two-door overlap (ch 6).** Now stated on the page as a failed transition: she opens the still door with the Ember caught in the doorway, "nothing passed from one door to the other," and it holds once under impact at a cost. Kiva's own reflection, Orla on the tram ("you jammed the Ember in the still door's frame … you're not to try") and Rhea's viewing and card ("Not a hand-off, and not to be expected twice") all say the same thing. The physical feat (standing a husk off Perrin with the hand door deliberately shut) is intact. Movement Three's first true two-door sequence is not spent.
2. **Transient register (ch 8).** All three entries and the margin note stay. Kiva no longer supposes that someone dreamed in 2446 or 2604. She notes that the old books show only lamps, a time and "no fault found," and she writes *Why: unknown.* The pre-Kiva dream fragment is still reserved.
3. **Fingers.** The dullness is written as temporary and improving: prickling at 02:44, "thin gloves" on Saturday morning, "better than on Saturday and still not right … more each day" on Monday. The medic's warning ("Next time it might not") is kept. The last image is "two half-woken fingers," not "two dull fingers."
4. **POV share.** Measured on chapters 1–48 terms only: Kiva 87.3% of chapters 1–8 after repair (87.2% before).
5. **Snapshot 4** stays in 2152. The T.V. / T. Vey echo is untouched and unconfirmed.
6. **Readability.** See section 5. Vocabulary was not inflated.
7. **Yield versus grade.** "Handful-grade" (ch 5) is now "the kind the yield books called a Handful." "Graded Barrel" and "Barrel-grade spawn" (prologue 9) are now "a Barrel yield" and "Barrel-yield spawn." "Grade First/Second/Third" is kept for purity. One consequence: the first draft's "est. 200 bbl" and "two hundred barrels" could not stand beside a Barrel yield class, so the lost recovery is now "one full Barrel" / "a whole Barrel of clean ash."
8. **Rename.** Bram Oduya is now **Femi Oduya** throughout snapshot 8 and in the continuity record. "Femi" has no match anywhere in this repository or in the research corpus. Apart from the notes that record the rename (this report, the continuity record and `AUTHORSHIP.md`), the only remaining "Bram Oduya" strings are in frozen records: the pre-repair edition, the two compiled review prompts and the brief.

### Priority 1 — numbers, days, space, knowledge

**Terrace Ring (ch 4).** The first touch now lands on the collarbone for a full point. The calls run "One. Renn," "Renn leads, two," "Renn wins, three to a half." Kiva's book entry and the thought "cost her a point" agree. No exchange was added or removed.

**Cellhouse clock (ch 5–6).** The four board times are unchanged (3:31, 3:38, 3:44, 4:41). Everything else was rebuilt to meet them. The full table is in the continuity record, section 1. In short:

- The hurry visibly accelerates: Kiva times a tenth in ten seconds and the next in nine, and the narration later gives seven and then five. Untuned, the cell would trip at about 2:50.
- Her calls now match that curve: "under two minutes" at 6.3, "seventy seconds" at 6.7, "fifty seconds" at 7.0, forty seconds left at 7.2.
- The intervention is now necessary on the page: with forty seconds left, Perrin needs thirty only to clear the housing, and Anwen would still be inside when the winch died.
- The chute is "four releases to a run" (1:10, 1:55, 2:40, 3:25). The duplicated release at the end of chapter 5 is gone.
- The tune holds for about twenty seconds (Kellan and Orla both now say twenty, not thirty).
- **Perrin's hold is about forty seconds** (3:38 to roughly 4:20), in his note and in his own lines.
- Rhea runs the plate from the three-and-a-half-minute mark, then from 3:31, and the disk swings out at 3:34. Chapter 6 now shows the disk swinging out at the moment of impact.

**Cellhouse space (ch 5–6).**

- Mezzanine height is 2.5 m everywhere.
- Kiva reads the cell with her **left** palm; the bar forms on her right fist. "Both hands" is gone.
- From the rail she sees only Perrin on the threshold. Everything inside the pump room now reaches her by Anwen's voice.
- Perrin lies on his back **along the threshold** under the shutter's edge, which makes his hands, his shoulder under the housing, and the final roll toward Kiva agree. "Drops on my legs" is "drops on me."
- The dummy comes out head-first by the collar, past Perrin's boots; its heels pass Kiva last.
- The husk's limb scrapes her forearm from the elbow down to the cuff and skids over the slab; the cuff leather is scored.
- Kellan's stair: wall on his left and rail on his right while he faces down it; the mezzanine is above and behind him. His vault has a reason (seven slick steps with a husk at his heels is three seconds; the rail is one). He then drops off the mezzanine edge to reach Kiva. In the first draft he came down the stair past the live husk.
- Perrin now closes his fist on his dram instead of swallowing it.
- The gallery is "four hundred people" in chapters 5–8. The first draft's three thousand did not fit one wall of a forty-pace hall.

**Dates and times.** Brannock's tunes are dated the 13th, 20th and 27th of last month. "The draw bench on Wednesday." "He said so on Classification Day." "Five days to get higher." The core trips at 02:44, reports at once, and resets "a little after half past three." Ysra reads the page "from that morning." Mara "filed it. Ours, from last night." The 2676 Kindling now says the group was called "well past two in the afternoon," so the 14:52 entry and Mara's clock agree with a seven o'clock courier.

**Other corrected items.** Draw "worse, up from two-nine." Kellan's Draw "near eight-tenths." Paper cell books "since the first licensed cells, more than four hundred years ago"; the register "more than four hundred years of it"; the stance stone "five hundred years of feet." Torch is "as far as her own door had ever taken her" for both Orla and Rhea, not a cap on one-door rank. Corbel Reach: before 2170 only scavengers went closer than the far bank, which fits the 2152 crew. Abel: "you come out at forty-one again." Sponsorship takes "one form and my stamp," and Orla "hasn't filed," which fits the stamped form in chapter 8 and her restored standing. The laundry is next door in every chapter. Orla is placed at the kitchen doorway on Wednesday morning. "Ten thousand times" is gone. Orla's hint in chapter 2 no longer calls the student "her."

**Knowledge leaks closed.** Kellan now thinks "she had not said it would call them" and credits only what she did say. Kiva asks "When did this come?" instead of stating that the letter came in the winter. Rhea's Saturday card says "Placement not yet posted." Orla has wondered about Ilse's choice for four years, since the seal was broken, not eleven.

**Two additions that create new facts.** Please confirm or strike.

- **Ysra's written condition.** In chapter 1 she says a multi-door incident closes Kiva's file for the season. The first draft never came back to it. Chapter 8 now has Ysra name the condition, say it is hers to enforce or set aside, and set it aside in writing on the strength of the book.
- **Dram line on the results board** (ch 6): Renn 0.41, Pryce 0.55, Cade 0.93, Rowan 0.96, no overspend. This answers the cold read's note that draw vanished at the trial.

A third small addition: after the run, clerks gather the husk ash into sealed tins for the Wren House graders (the first draft had them rake it off the floor). Kellan still ignores the ash mid-run; the text now says recovery is scored "once a run was safe."

### Priority 2 — sentence rhythm

Fragment runs were joined in exposition, interiority, backstory, aftermath and spatial setup across all nine files, starting with the passages both reviews named (the four axes, Mara's evening, Orla's, Kellan's and Rhea's cutaways, the Cellhouse layout, the license conversation, prologue snapshots 4, 7 and 10). Short paragraphs were kept. Hard fragments were kept at impacts, reversals, ledger lines and chapter endings ("The thing hit nothing." "She went." "Holding. Holding. Holding." "No," said Mara.). Results are in section 5.

### Priority 3 — voices, revelation, aftermath

- **Anwen owns "I want it said"** (ch 1, ch 6, ch 8). It is removed from Perrin (ch 3, ch 7) and Mara (ch 8).
- **Mara owns saying it out loud** (ch 2, ch 4, ch 5, ch 7, ch 8).
- **Ysra** speaks through file, items, record and standing ("the file is what I am permitted to rule on," "That is outside my office").
- **Kellan** speaks in rates and columns ("That's a rate, not an insult," "They don't add").
- **Perrin** jokes and the joke fails ("the joke keeps coming out jealous," "it's just the jealous left"). The lines that named the borrowing from Anwen are gone.
- **Orla** tells it as a field story she would rather not tell (the Ferren levee ward-holder; "I'm the fool in most of them. This is the one I never told"). "Not a good reason. The true one" is gone from both places.
- The "I'm not saying X, I'm saying Y" frame was reworded for Ysra, Mara (twice), Kellan and Anwen.
- **Jessamy Hart.** Chapter 3 keeps Orla's fear, the sealed file, the unanswered letter and the unsigned second page. The hand, the two burned students, the crowd of four thousand and the south coast are withheld there and delivered once, in her chapter 8 confession.
- **Aftermath trims.** Kellan after the board, Orla on the tram, Anwen with Mace, Ysra's questions and Rhea's viewing each keep the judgment that belongs to that speaker and drop the shared beat list. Kellan's ring cutaway no longer re-narrates the riser.
- **Prologue endings.** Three snapshots now close on an image with the record still present earlier in the scene: 5 (the camp at dusk and the unopened panel), 8 (one yellow light seen from the dark street) and 9 (the rescued girl and the dog on deck).

### Smaller read-aloud fixes taken while in the text

The board stutter is described instead of spelled out. The bout board says "requested" instead of a star. "Lost, 3 to a half." "Scram pulled, P. Morrow." Mara glosses 14:52 aloud as "eight minutes to three in the afternoon." Sustain and "the filter" each get one short gloss. Snapshot 9 uses meters and kilometers to match the chapters.

## 5. Numerical result — target against observed

Measured with the editorial review's own script, extracted unchanged from its appendix (SHA-256 `462e9ac63f3d831ce8465b78598e32ed0a95b25b25adef9373d1495dc402a308`) and run against the frozen edition and the repaired manuscript.

### All sentences

| Metric | Target | Before | After | Reading |
|---|---|---:|---:|---|
| Mean sentence length | 14.6 | 8.30 | **10.33** | Moved; still well short |
| Median | 11 | 6 | **7** | Moved a little |
| Five words or fewer | 27.7% | 45.1% | **41.5%** | Moved a little |
| Forty words or more | 3.3% | 0.30% | **1.67%** | About halfway |
| Flesch Reading Ease | 72.3 | 92.4 | **90.4** | Barely moved |
| Flesch-Kincaid grade | 6.8 | 2.4 | **3.2** | Still far from seventh grade |
| Syllables per word | about 1.41 implied | 1.254 | 1.253 | Unchanged by choice |

Per file after repair (mean / five-or-fewer share): prologue 11.18 / 36.0%; ch 1 10.60 / 42.6%; ch 2 10.60 / 41.9%; ch 3 9.18 / 46.0%; ch 4 11.84 / 37.0%; ch 5 10.28 / 41.7%; ch 6 10.43 / 42.0%; ch 7 8.56 / 50.2%; ch 8 9.32 / 44.2%.

**The overall targets are not met.** The selected formula is still a long way off on every whole-text measure.

### Where the remaining gap sits

I split the same tokenizer's sentences into narration, quoted speech and italic ledger lines. This split is mine, not the review's, and a recheck should reproduce it before relying on it.

| Slice | Share of sentences (after) | Mean before → after | Five or fewer before → after | Forty or more before → after |
|---|---:|---|---|---|
| Narration | 54% | 9.93 → **13.82** | 35.4% → **26.7%** | 0.43% → **2.97%** |
| Quoted speech | 41% | 5.84 → 6.26 | 59.8% → 58.6% | 0.04% → 0.08% |
| Ledger and board lines | 5% | 5.86 → 6.15 | 61.3% → 60.5% | 0.67% → 0.68% |

Narration median went from 7 to 10. So the narration now sits close to the formula, and almost all of the remaining distance is dialogue: 41% of sentences are spoken, and 59% of those are five words or fewer. The review's own cross-check (quoted speech stripped, tag stubs left in) agrees in direction: mean 9.06 → 12.01, short share 41.9% → 36.5%.

I did not lengthen the dialogue. The clipped speech is how these characters talk, and the brief says not to hit numbers by damaging good prose. **Whether to change spoken cadence is an owner decision.** So is vocabulary: grade cannot reach about 6.8 at 1.25 syllables per word without either longer dialogue or more polysyllabic diction.

### Tics

| Phrase | Before | After | Note |
|---|---:|---:|---|
| "looked at" | 130 | 3 | **Overshot.** The guidance was to thin by about half. I varied nearly every one. A recheck should confirm the substitutes do not form a new tic. |
| Narration fragments opening "Not …" | 78 | 39 | Halved, as asked |
| "it was not" | 34 | 41 | **Rose.** Some "Not X." fragments became "it was not X" clauses when joined |
| "did not" | 248 | 246 | Left alone, as asked |
| "said" per 10,000 words | 92.4 | 88.7 | Little change; tag density was not a priority in the brief |
| "for a long time/moment/while" | 21 | 20 | Not thinned |

Other measures: paragraphs 2,258 → 2,255 with median 15 words (unchanged); section breaks 15.0 → 14.5 per 10,000 words; progression vocabulary 115.3 → 111.5 per 10,000.

## 6. Left as drafted, or needing the owner

- **Prologue snapshot 1.** The white light and first colours still precede the blackout by a few lines. The editorial review marked this low-priority plausibility. I left a strong opening alone.
- **Prologue scale.** Snapshot word counts are now 1,069; 986; 1,266; 968; 1,759; 1,800; 1,372; 1,677; 1,510; 1,248; 2,887 (16,542 by the script's count). Snapshots 5, 6, 8 and 11 exceed the 900–1,600 guide. Snapshots 5 and 8 grew because of the new closing images.
- **Prologue length before Kiva appears.** Both reviews named it the largest reader risk and both left it out of the repair brief as structural. It is unchanged.
- **Chapter 3's three tutorials and chapter 8's six endings.** Flagged as slow spots. Left intact because every scene is preserved.
- **"Kindled" and "Ember" each carrying several meanings.** Not addressed.
- **Units.** Miles remain in the 2085 snapshot.
- **Gallery size.** I chose four hundred. Any figure that fits one wall of the hall will do.
- **The two new facts in section 4** (Ysra's set-aside, the dram line) need a yes or no.

## 7. Verification still owed

A separate targeted recheck against the changed files should confirm, at minimum:

1. **Priority 1.** Every clock time, reading and spoken countdown in chapters 5–6 against the table in the continuity record; the bout score; each date; each sightline and hand; the knowledge boundaries for Kellan, Kiva, Orla and Rhea.
2. **Priority 2.** The numbers in section 5, the narration/speech split, and a read-aloud check that the joined sentences keep clear hierarchy and that impact fragments still land.
3. **Priority 3.** That each of the six voices is distinct on a cold read, that chapter 8 now carries Jessamy's particulars as new information, and that no aftermath scene lost its own judgment.

This was a same-author repair by the model that wrote the draft. Its blind spots overlap the draft's.
