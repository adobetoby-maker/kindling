# Kindling 2680, Book One — Movement Two (chapters 9–16) — targeted recheck

> Built by TAC

Date: 2026-10-10
Prompt performed: `editor/MOVEMENT-002-TARGETED-RECHECK.prompt.md`, read in full.
Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), one session, no subagents.
Status: review only. This report is the only file written. No manuscript, canon, planning, provenance, authorship, prior report or prompt file was changed. Nothing was committed.

Locations are `chapter:line` in the repaired files (`13:415` is `manuscript/chapter-13.md`, line 415). Frozen-edition lines are marked "frozen".

---

## 0. What kind of read this is

**An informed, same-model recheck in a fresh session. It is not a human read and it is not an independent read.** I am the model that drafted and repaired these chapters. I did not have either transcript, but I read both reviews, the brief, the repair report and the author's own checkpoint before judging the page. Agreement with those files is weak evidence. Section 2e lists every place I disagree with them.

### Read before judging

Read complete: the editorial report (including its script appendix), the cold read, the repair brief, the repair report, both continuity checkpoints, `UNIVERSE_BIBLE.md`, `BOOK_MAP.md`, `STATE_LEDGER.md`, `packets/MOVEMENT-002.md`, and repaired chapters 9–16 in order.

Frozen chapters 9–16: read through a line-numbered comparison of each chapter. It showed every repaired paragraph and, beside it, every frozen paragraph that differs (95 frozen paragraphs against 102 repaired ones). All other paragraphs are byte-identical between the editions, so each frozen chapter was covered in full, but as a comparison and not as a second end-to-end prose read.

Not read: the prologue and chapters 1–8 (one line looked up, `chapter-08.md:85`, for the wording of Ysra's condition), `AUTHORSHIP.md`, and the compiled prompts.

### Integrity checks

- **Frozen edition:** all eight files verify against `editions/movement-002-pre-repair/SHA256SUMS.txt` (`shasum -a 256 -c`, eight OK).
- **Working manuscript:** the eight SHA-256 values match the repair report's table exactly, so I rechecked the bytes the repair described.
- **Word counts (`wc -w`):**

| File | Frozen | Current | Change |
|---|---:|---:|---:|
| `chapter-09.md` | 6,596 | 6,764 | +168 |
| `chapter-10.md` | 6,734 | 6,733 | −1 |
| `chapter-11.md` | 5,939 | 6,121 | +182 |
| `chapter-12.md` | 6,093 | 6,156 | +63 |
| `chapter-13.md` | 7,439 | 7,837 | +398 |
| `chapter-14.md` | 6,705 | 6,371 | −334 |
| `chapter-15.md` | 5,475 | 5,608 | +133 |
| `chapter-16.md` | 7,019 | 7,043 | +24 |
| **Movement Two** | **52,000** | **52,633** | **+633** |

  By the editorial script's word rule the movement is 51,899 before and 52,536 after. Sections: 71 before, 71 after.
- **Metrics:** the editorial's two scripts extracted from the reports with the published hashes (`462e9ac6…a308`, `08a6f5b2…9617`). Run on both editions, they reproduce every figure in the repair report's section 5.

---

## 1. Verdict

| Priority | Verdict | One-line basis |
|---|---|---|
| 1 — trust the numbers and rules | **PASS** | Fourteen of the fifteen C-items and all thirteen cold-read rows are closed on the page; C14 is softened. Every rebuilt chain agrees. Three one-phrase corrections remain (section 5). |
| 2 — friction and distinct voices | **PASS** | Three resistance beats sit inside existing scenes and two of them cost Kiva something. One authority stays unpersuaded. The shared `hm` is down to Druce and one marked echo. |
| 3 — escalation and chapter 14 | **PASS** | The two trends are set side by side twice and remarked on once. Nothing is proved. Chapter 14 has a stake from its eleventh line and every protected element is intact. |

**No second repair pass is justified.** I found no continuity, clarity or read-aloud defect that needs a scene reworked. I found three small ones that need a phrase each, and one of those three was introduced by the repair. They are line corrections that a diff can verify, not a pass.

The formula distance is unchanged and is not a reason for a pass under the owner's ruling (whole text: mean 9.93 against 14.6; narration alone 13.09, 28.2% short, 3.06% long).

---

## 2. Priority 1 — trust the numbers and rules

### 2a. C1–C15, one by one

| Item | Repaired page | Status |
|---|---|---|
| C1 Friday/Saturday | `11:71`: Kiva goes "early on Saturday, before the others." Agrees with `10:349`, `10:467` and `11:81`. | Closed |
| C2 Home Line and dark hands | `13:415`: the ward-holder drops her wall and steps back three paces, the neighbouring walls close behind the husk, the blade lights for the cut and runs home. | Closed on the rule. Wording wobble, R3 |
| C3 Draw and 0.93 | Defined once at `11:31`, five chapters before `16:419` needs it. Arithmetic in 2c. | Closed |
| C4 third-carry start | `16:13`: "went down her own two steps and no further." Agrees with `15:45`. | Closed |
| C5 team count | `13:77`: thirteen from the bottom of the call, plus Nineteen in place of a team not passed fit, makes fourteen; a fifteenth waits. Agrees with `12:161`, `12:433`, `13:135`, `13:469`. | Closed |
| C6 live-cell scope | `09:287`: "any charged cell, and … a held rift, and … the Kennel lattice, which is a rift in a cage." | Closed |
| C7 number/position coincidences | Nineteen stands 18th (`09:281`), Eleven 9th (`10:389`), "twenty-two places" (`10:453`, and 40 − 18 = 22), log reads T33, T14, T26 (`13:83–87`). | Closed |
| C8 eleven catchers | `10:5`: "one from each team in that afternoon's section." Agrees with `12:207`. | Closed |
| C9 the cloth | `13:369`: "Kiva's cloth." | Closed |
| C10 Orla's second condition | `11:131–133` shows six seals, each called and turned over. Cited at `11:155` and in the certificate at `11:335`. | Closed |
| C11 Team Eleven | `13:67`, `13:103`, `13:465`, `13:503`: Vane shuts the tear; Eleven leaves without a floor. Owner-accepted. | Closed |
| C12 "four drams" on Monday | `14:105`: "a whole Handful of it." | Closed |
| C13 "held its eyes" | `13:309`: "blind face … did not give it an inch." | Closed |
| C14 sandbag count | `12:7`: "forty." `11:5` still says every school has "a dozen." | Softened, not closed; taste note |
| C15 Jude's hold | `16:237`: 6.4 in the spring. Agrees with "six and a half on a good day" (`09:37`). | Closed |

Cold-read rows not already covered: the Kennel book hangs on a hook and is unhooked (`10:81`, `11:181`, `12:353`); Kiva's "better part of half a minute" against Kellan's twenty-eight seconds (`11:93`, `11:103`); Perrin's lanes (`16:361`); Pru's post reading no longer carries a tap count (`16:239`); Kellan's first six of twenty-one drams (`12:135`); the cold-room reveal now plays fair, since Kiva sees the blade "low and lit" (`12:67`, `12:125`); Anwen cites what chapter 9 shows (`12:227`); Druce enters the uncalled blade against himself (`12:113`). The editorial's two smaller questions are also closed (`15:21–23`, `12:135`). All closed.

### 2b. Rules

- **Dark hands.** Stated at `09:201`. Enforced at `12:113–129`, `13:99`, `13:149`, `13:379–385` and `13:391`. The Home Line now keeps it at `13:415`. No lit door sits inside three paces of open ash inside a count anywhere in the movement. The page gives three paces for the ward-holder; it does not give a distance for the walls that close behind the husk. I accept that as shown, not stated.
- **Ysra's scope.** `09:287` matches the Movement One wording word for word ("No live-cell events", `chapter-08.md:85`) and widens it once, plainly. Everything after follows: Kiva is on the settling floor only for dead-ash drill before Orla signs; the sponsor's floor runs under its own rule (`11:141`); she declares "Door declared: none" at `11:179` and `13:227`; the certificate at `11:333` and Ysra's summary at `16:401` say the same thing.
- **Power boundaries.** No two-door sequence. Disk cold at `11:377`, `13:543`, `16:487`. Fingers dull and recovering, failing once (`14:105`, `16:163`).

### 2c. Rebuilt from the page

**Calendar.** Tue 16th to Mon 6th on a thirty-day month. Every relative reference I could test agrees after the repair: `09:45`, `09:109`, `10:89`, `11:59`, `11:65`, `11:71`, `11:81–113` (five squares, Saturday to Wednesday), `11:151` (seven nights), `11:349`, `11:375`, `12:83`, `12:129`, `12:247`, `13:31`, `14:83`, `14:154`, `15:233`, `16:345`, `16:397`, `16:445`, `16:483`. **One break: `16:437`** (R2).

**License day.** Mast six at ten to three, five and seven at six minutes to (`12:427`, `13:33`). Fourteen teams called, so thirteen forty-minute gaps (`13:361`). Nineteen in at half past three, thirteenth of fourteen, husk at 3:40 (`13:135–139`). Seven's husk at 4:22 (`13:239`). Second husk eleven minutes later. Eleven leaves about 5:15; closing crew at 5:30 (`13:501–503`). Vane's "I've had fourteen" (`13:469`) matches. The count reads cleanly on one pass.

**Meet.**

| Carry | Crooked Line | Stonehand | Board | Kiva's dram |
|---|---|---|---|---|
| 1 | 2 downs | 1 down + carried (3) | 4–2 (`15:145`) | 0.38 |
| 2 | 2 downs | 1 down + carried (3) | 8–4 (`15:313`) | 0.87 |
| 3 | 2 downs + litter (1) | 1 down | 9–7 (`16:177–179`) | 0.98 |

"Four touches to their two" (`15:325`) and "we're on five" (`16:93`) are right. Left in the dram: thirteen hundredths (`16:23`), seven at the minute (`16:131`), two (`16:275`).

**Draw.** Under the owner's ruling (ash spent against the book's expectation; 1.0 standard; lower is thriftier):

- Low Lane: 0.09 against the book's tenth is 0.9 (`11:23–31`).
- Carry three: the board shows 0.87 to 0.98, which is 0.11. The book's figure for a four-minute contested hold is 0.12. 0.93 × 0.12 = 0.1116, which is "eleven hundredths and a hair" (`16:419`). Kellan's rounder "eleven hundredths" (`16:333`) is the board figure. The three numbers are now compatible in sum and in speech.
- Direction is consistent elsewhere: class median near 1.0 and "lowest Draw … nought point seven" as the best (`14:226`, `14:234`).

**Ash.** 20.8 → 10.4 / 2.6 / 3.9 / 3.9, in the ledger's order (`14:113–117`). Spend 0.5 + 1.0 + 1.0 + 1.4 = 3.9 (`14:196`). 3.9 at 0.7 is "five releases and a bit" (`14:150`). Yields: 14.6 plus about 9 (`11:319`, `11:405`); 21.0 (`12:83`); 15.3, "under … by nearly five" (`12:355`); 20.8, "three and a bit" short of 24 (`14:29`).

**Hold posts.** Jude 6.4 → 4.1 is a fall of 36%, "a bit more than a third." Kiva's stance 6.2 → 4.9 is 21%, "a fifth, a bit more" (`16:237`, `16:265–269`).

**Geometry.** Kennel print scene: cloth west of the south tank, tank and bridge to Kiva's right, Kellan on the bridge (`11:165`, `12:31`, `12:67`). Sag Line: cloth in the lee of the shed's east wall, bean poles behind Kiva, east corner beyond them (`13:195–201`, `13:251`, `13:365–369`). Long Terrace third carry (`16:13–21`). All drawable.

### 2d. Checkpoint against the page

`provenance/MOVEMENT-002-CONTINUITY.md` agrees with the repaired manuscript on every row I tested: calendar, license-day clock, meet table, hold posts, Draw, shares, the two-oddities section and the plants. It no longer repeats C1 or C5. One row will need touching if R3 is applied (license-day clock, count 51).

### 2e. New or surviving contradictions

**Introduced by the repair**

1. `14:13`. The new paragraph at `14:11` is about Anwen and ends on her. The next paragraph still opens "She was a brisk, freckled woman called Halloran." In the frozen text "She" followed the grader. Now a listener hears Anwen for half a sentence. (R1)
2. `13:415`. "The second husk came apart on bare grass. A grey-haired woman was already on her knees beneath it with a cloth spread." Bare grass and a spread cloth cannot both be where it falls, and "beneath it" is left over from the wall. The rule is kept; the picture is not clean. (R3)

**Survived the repair; missed by both reviews**

3. `16:437`. On Monday the 6th Ysra says the Kennel "has thrown husks this month." The four Kennel skins fell on the 4th, 12th, 17th and 27th of the month before (`14:83`). Four paragraphs later she uses "this one" for the new month (`16:445`). The frozen "It says …" read as the report's own words; the repaired "tell me that" makes it hers. (R2)
4. `13:167`. Vane summons Seven and Eleven with Nineteen (`13:165`): twelve people. The line that follows is "twenty-odd candidates." The repair made the head count exact, which makes this more visible. Low. (R4)

**Disagreements with the repair report (records only)**

5. Its item 7 says the new paragraphs over 150 words are speeches by "Dray, Vane, Ysra." By the script they are `14:33`, `14:105`, `16:393` and `16:437`. Dray's and Vane's are under 150.
6. "Not unkindly, three to one" is true of the exact phrase. The family is five to three: `10:407`, `12:161` ("did not say it unkindly"), `14:350` ("was not unkind").

---

## 3. Priority 2 — friction and distinct voices

### 3a. The three resistance beats

**Kennel, chapter 9** (`09:97`, `09:181`, `09:221`). Two empty benches; a dozen heads turning when Druce mentions cells; a neighbouring team carrying its kit to the far wall. It is wordless, it comes from fear and not malice, and "Druce saw them go. He let them" stops an adult from tidying it. This is the quietest of the three and the nearest to set dressing, because Kiva is given no response to the first or the third. It still does its work: it puts Jude's "half this school" (`09:37`) on the page in the chapter where he says it.

**Sag Line, chapter 13** (`13:181–185`, `13:505`). The strongest. Selka Dray speaks at the moment of her own public failure, to the line and not to Kiva. Half of what she says is true, and Kiva knows it: "she had nothing to say, because the part about the cell was true." Nobody answers. Kellan does not move. Dray leaves unconvinced by 20.8. This is pressure with a cost and no resolution, and it makes her a person.

**Stonehand, chapter 15** (`15:17`, `15:239`, `15:303`). A father moves his daughter away from the western porch. Then the crowd learns her declared word and sings it back. The second half is the better idea: the hostility attaches to the exact mechanism Brask is using against her.

Judgment: real social pressure, not decoration. None is a new scene and none is a bully.

### 3b. An authority who stays unpersuaded

The referee signs the card clean and tells Kiva to her face what she wrote on the back: "isn't safe. She's supervised" (`16:207`). Ysra reads it and says nothing (`16:393`). It is not answered by the end of the movement. Institutional fairness is intact, since the dissent is declared and the clean card still goes up. Smaller cases hold: the bored clerk (`14:123`), and Halloran, who "did not say whether she believed a word of it" (`14:67`).

### 3c. Voices

| Signal (editorial script) | Frozen | Repaired |
|---|---:|---:|
| "Hm" / "Huh" as a spoken line | 9 | 4 |
| "want it said / noted / known / understood" | 12 | 4 |
| "It's said" replies | 3 | 3 |
| "not unkindly" (exact) | 3 | 1 |
| "did not soften" | 2 | 1 |
| "nearly / almost smiled" | 3 | 2 |

- **`Hm`.** Druce (`10:53`), Perrin imitating him (`10:55`), Agnes Roake as the marked echo (`13:131`), and Kellan's own "Huh" (`11:107`). Vane, Halloran, Brask and Ysra each now answer in their own way: "It would be." / "Are you, now." / "'No,' said Brask, as if she had handed him something." / "So they are."
- **Declared motive.** The phrase is Anwen's again (`10:405`, `10:439`, `11:125`, `16:349`), with Perrin's one answering use (`13:431`). No adult uses it. The ethic survives in other grammar: Jude (`09:37`), Orla (`11:155`), Ysra (`16:401`), Kellan (`14:154`), Noa (`16:219`), Brask (`15:41`).
- **Still recognizable.** Druce: soft, exact, counting. Brask: courteous, reading her, untouched by the repair apart from one reply. Jude: the opening speech less one clause. Anwen: the list and the phrase. Perrin: now has his own formula, "Somebody put that in the book" / "Somebody write that down" (`12:11`, `13:427`), which sounds like him.

### 3d. New long speech, checked aloud

Read for syntax and attribution: Kellan (`09:287`), Noa (`11:27–31`), Druce (`12:113`), Dray (`13:181`), Vane (`13:465`), Aske (`14:105`), the referee (`16:207`), Ysra (`16:393`, `16:419`, `16:437`). Each has one speaker, a tag or action near its start, and no clause that has to be re-read. Dray's long sentence parses on one breath because her look at Kiva is set before she speaks. The only attribution fault in new text is narration, not speech: R1.

---

## 4. Priority 3 — escalation and chapter 14

### 4a. The seeding

| Witness | Frozen | Repaired |
|---|---|---|
| Noa | Both facts on one page; three sentences denying a link | Both on one page; "He drew no line between anything on it" (`14:242`) |
| Rhea | Both facts on one card; "nothing to do with each other" | Tear count only, on the back of the card (`16:317–319`) |
| Ysra | Both reports; "I mention it only because…" | Both reports, given as the two grounds for moving the Flask (`16:437–441`) |

The facts are set side by side twice and remarked on once. "Strong year" appears twice (`14:236`, `15:175`), and the second costs Perrin something. "Dirty spring" appears once and is the Home Line's phrase. No character connects the trends, nothing is measured against anything, and Kiva learns no filter explanation. Orla lifting her head (`16:439`) is the only reaction. **Seeded, not paired three times, not proved.**

### 4b. Chapter 14, read straight through

**The early want.** Anwen is carrying "subject to the tins" from line 11, with the cost named: no license, no Graywater, Kellan back at the bottom of a call. Her hand shuts at `14:33` and opens on "Sixty." This gives the grading lesson a stake. It is spent by about the seven-hundredth word. After that the chapter is carried by a chain of open questions: Halloran's "How did you know?" and her disbelief; her request for half a dram; Aske's "next time"; the size of the share; then the vote.

**Movement.** Aske is one exchange. The ash-office sum is five slate lines and Perrin's "Is that all?" Noa's cutaway is 844 words against 1,196, and it goes: the thing he came to check, the column that stopped him, the page, what he wants, what he decides.

**Against the cold reader's exact concern.** The concern was about 2,600 words of adults explaining before any of the four wants something, and a skimmed sum. The want now arrives about 160 words in, and the sum is a slate. The cold read's own proposed scope was carried out item by item. What did not change is the length and the shape: the stretch from the grading room to the ash office is 2,629 words against 2,610, and it is still five scenes led by an adult who knows more than the team. I read it without skimming. I also know the system already, so I am not the test for that.

**Intact:** Halloran's shelf and its hand-lettered card (`14:71–91`); the comb and "curved" (`14:45–67`); the ward-trace dram and Aske's warning (`14:105`, `14:164`, `14:196`); the share arithmetic; the kitchen vote entire, with Kellan's jar speech and Perrin's sum (`14:137–216`); Noa's consent ethic (`14:248–254`, paid at `16:219–227` and `16:423–427`).

---

## 5. Required mechanical corrections

Each is one phrase. None changes an event.

| # | Location | Correction | Origin |
|---|---|---|---|
| R1 | `14:13` | Name her: "The grader was a brisk, freckled woman called Halloran…" | Introduced by the repair |
| R2 | `16:437` | "this month" → "in the past month" | In the frozen text; exposed by the rewording |
| R3 | `13:415` | Make the fall one picture: drop "bare" or the cloth, and drop "beneath it." Then match the checkpoint's count-51 row. | Introduced by the repair |

Recommended, low severity, not gating:

| # | Location | Correction |
|---|---|---|
| R4 | `13:167` | "twenty-odd candidates" → "a dozen candidates" |

Records, for whoever next updates them (not manuscript): items 5 and 6 in section 2e.

---

## 6. Optional taste notes

Not defects. Not grounds for any pass.

- `11:5` against `12:7`: "a dozen" in every school, "forty" at the Hall. Reads as the body school having more, or as Perrin.
- `14:105`: Aske's "Mm." is a hum from a fourth adult. To a single narrator it is close to Druce's.
- `11:155` and `16:401`: Orla's and Ysra's replacements share one construction ("Don't go home thinking…" / "Don't carry it out of this room…"). `09:205` and `12:313` both use "I mention it."
- `14:222`: "the only signature on the card" arrives without the card. `14:33`: "The hand came open" needs a beat to be Anwen's.
- `14:11` reports Anwen's worry from inside a Kiva section. It reads as Kiva knowing her friend.
- `09:97`, `09:221`: giving Kiva one small reaction would tie the Kennel beats to her.
- `16:15`: "It was no distance at all, and she took it at her own speed" is a slightly odd join now that the sixteen paces are gone.
- Chapter 14's first third is under pressure but no shorter. If the owner still feels drag there, the shelf scene and the grading scene are where the words are.
- The narrator's rule for reading decimals is still unset, and the slate adds five digit rows.

Owner items carried, unchanged by this recheck: the referee's note is an open thread; Team Eleven's outcome makes Anwen's choice lucky and the page does not say so; "the book's twelve" is now canon by ruling.

---

## 7. Limits

- Same model, informed read. The voice findings in section 3 are the kind a same-model reviewer under-reports. Treat the counts as measured and the judgments as one reader's.
- Whether a first-time reader still skims the opening of chapter 14 cannot be settled by this recheck.
- I verified against the Movement One checkpoint, not against chapters 1–8.
- Items R2 and R4 were missed by two earlier reviews. Others of that size may remain.

---

## Appendix — method

Python 3, standard library, read-only against the repository. All scratch files were written outside it.

1. `shasum -a 256 -c SHA256SUMS.txt` in `editions/movement-002-pre-repair/`; `shasum -a 256` and `wc -w` on the working chapters.
2. Edition comparison: `difflib.SequenceMatcher` over lines of each frozen and repaired chapter, printing every repaired line with its number and every differing frozen line beside it.
3. Metrics: `metrics_m001.py` and `metrics_m002.py` extracted with the `awk` commands in the editorial's appendix, hashes checked, run once on the working book root and once on a shadow root holding the frozen chapters 9–16.
4. Phrase locations (`hm`, the "said" family, approval tags, pairing phrases, team counts, Draw figures, "this month"): regular-expression search over chapters 9–16, then each hit read in place.
5. Chapter 14 section lengths and paragraphs of 150 words or more: the same word rule as the editorial script, by line number.

Every verdict in sections 2 to 4 is a reading of the cited lines. The scripts supplied counts and locations only.
