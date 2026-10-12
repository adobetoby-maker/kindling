# Kindling 2680, Book One — Movement Three (chapters 17–24) — targeted recheck

> Built by TAC

Date: 2026-10-11
Prompt performed: `editor/MOVEMENT-003-TARGETED-RECHECK.prompt.md`
Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), one new session, no subagents.

Status: review only. This report is the only file written. No manuscript, canon, ledger, review, repair file, prompt or authorship record was edited. Nothing was committed or pushed. Movement Four was not started.

---

## 0. What kind of read this is

**A same-model informed recheck in a fresh session. It is not a human read, not a cold read, and not independent testing.** The chapters, both reviews and the repair were all produced by this model. Agreement with the repair report is weak evidence, so facts below were rebuilt from the manuscript and the report was checked against them, not the other way round.

Read in full: the eight repaired chapters; `editor/MOVEMENT-003-EDITORIAL.md`; `editor/MOVEMENT-003-COLD-READ.md`; the repair brief and repair report; `provenance/MOVEMENT-003-CONTINUITY.md`; `STATE_LEDGER.md`; the Movement Three sections of `AUTHORSHIP.md`; the frozen chapter 24. The frozen chapters 17–23 were read as a paragraph-level diff against the repaired files, which shows every changed line in both versions.

Line lookups only: chapters 6, 8, 12–16 (Aske, Halloran, the plate, the skin cuts, the referee's calls); `CHARACTERS.md`; the earlier checkpoints.

Mechanical checks run: the frozen edition's `SHA256SUMS.txt` (all eight OK; `git status` shows nothing changed under `editions/`); the eight post-repair hashes in `AUTHORSHIP.md` (all match the files on disk; total 48,693 words); leftover searches; and the editorial review's three metric scripts, extracted unchanged (hashes `462e9ac6…`, `08a6f5b2…`, `e07e81fb…` as recorded) and run read-only from a scratch folder.

Disclosed: session start-up injected a few lines of project status memory, none used as evidence. A name search across the repository listed two untracked files, `packets/MOVEMENT-004.md` and `planning/OPUS-5.5-MOVEMENT-004.prompt.md`. Another process wrote them. I did not open either.

Locations are `chapter:line` in the repaired files, with line 1 the chapter title.

---

## 1. Verdict

| Priority | Verdict |
|---|---|
| 1 — calendar, arithmetic, identity, knowledge | **PASS** |
| 2 — dark-floor decision and relationship cost | **PASS** |
| 3 — chapter 24 flow and read-aloud clarity | **PASS** |
| **Overall** | **PASS. No second prose repair is justified.** |

Every located finding the brief carried forward is resolved on the page, and the repair introduced no contradiction of substance. There is **one required correction, and it is in the continuity checkpoint, not the manuscript**: a stale row that still dates the knee's ban to the 2nd (section 5, R1). Everything else in section 5 is optional.

---

## 2. Recheck 1 — calendar, arithmetic, identity, knowledge

### 2a. The calendar, rebuilt from the page

Weekdays as narrated: Friday the 17th (`19:187`); the Return on the eighteenth, a Saturday (`17:195`); Monday night in the yard (`20:413`); the Tuesday floor (`20:497`); Wednesday night (`20:465`); Thursday at the Pit (`21:5`); Monday's companies (`21:201`); Tuesday (`21:215`); Wednesday (`21:301`). That Wednesday is the 29th. After it: Thursday grading (`24:153`), Friday's findings and standings (`24:201`, `24:241`), Saturday's vote (`24:267`), Sunday's yard (`24:479`), which are the 30th, 1st, 2nd and 3rd.

The thirty-day month is not asserted on the page, but two independent fortnights require it: the infirmary's "before the second of next month" from the 18th (`20:403`), and Aske's fortnight from the 29th ending on "the thirteenth" (`24:33`, `24:481`, `24:495`, `24:539`). The tape date rests on the same month length and agrees with it.

### 2b. Original findings

Editorial findings are C1–C17 and K1; cold-read items are CR1–CR13 where they are not duplicates.

| Finding | Status | Evidence on the repaired page |
|---|---|---|
| C1 / CR1 Flask dated the 26th | **RESOLVED** | "Wednesday the 29th" at `17:179`; "the twenty-ninth" `20:405`; "the 29th" `23:525`; "Wednesday the twenty-ninth" `24:275`; "*The Pit, 29th*" `24:443`. No "26th" remains in chapters 17–24. |
| C1 dependents | **RESOLVED** | Weir "seventeen days ago" (`22:135`; 12th to 29th). "In a little over a fortnight" (`18:253`). Lane to Pit "eleven days after" (`24:543`; 18th to 29th). "The one three days old" on Saturday (`24:293`). |
| Pit tape date | **RESOLVED** | Standings posted Friday (`24:241`); the Halden man, on Saturday: "They were posted yesterday… the first of next month" (`24:467`). Noa has been at the tape "two days" since Thursday's copy (`24:403–405`). Thirty days from Friday the 1st on a thirty-day month. |
| Aske's stood-down date | **RESOLVED** | "A fortnight" from the cart (`24:33`); "until the thirteenth" (`24:481`); "till the thirteenth" (`24:495`); "The knee and the rest, the thirteenth" (`24:539`). The infirmary's own date is honoured where it is still in force (`22:327`, `24:487`). |
| C2 / CR4 crooked post's age | **RESOLVED** | "older than the school that had grown up round it" (`17:67`). No figure; nothing now conflicts with the three-hundred-year New Lane (`19:239–249`). |
| C3 Rhea and the plate | **RESOLVED** | "four times, six weeks ago" (`23:419`); matches `08:257`. |
| C4, C5 Jude's meets; when he heard | **RESOLVED** | "since Friday, when Bexley told me… four meets" (`19:89`). |
| C6 floors | **RESOLVED** | "three times" (`18:9`); "three floors and a field" (`19:211`). |
| C7 Kellan's skin cuts | **RESOLVED** | "met that skin twice in my life, and I was early the first time" (`17:291`); matches `12:329–331` and `13:319–321`. |
| C8 the field dram's age | **RESOLVED** | "half an hour ago, at a gate" (`23:213`); "the best part of half an hour" (`24:409`). |
| C9 / CR3 sixty paces | **RESOLVED** | "forty-odd paces" (`22:115`), agreeing with "Thirty paces. Forty." (`22:99`) and `22:125`. |
| C10 / CR9 the countdown | **RESOLVED** | Sixty (`22:311`), fifty-two (`22:329`), "Fifty now" (`22:339`); 48, 44, 40, 36 (`23:5–29`); "thirty counts off" (`23:33`); 22 and 16 on the hobble (`23:57`); 8 at the lip (`23:69`). The call takes about two, her own count runs One to Five, and at her *Six* the count of iron "stands at one" with the cords "at the head of the ramp" (`23:133–135`). It closes to the count. |
| C11 Dunmore's position | **RESOLVED** | "from the rim, halfway round to his stair, with the whole ring in front of him" (`24:283`). |
| C12 / CR10 Mara's Tuesday | **RESOLVED** | "a week ago today" (`21:289`), spoken on Tuesday the 28th; agrees with Dunmore's "on Tuesday" said on Thursday the 23rd (`21:81`). |
| C13 Old Four's wall | **RESOLVED** | "five paces off the thing's southern flank, between it and their own sheet" (`22:149`). |
| C14 duplicate healer description | **RESOLVED** | "a stout, unhurried woman with ink on her cuff, who wrote the whole time she talked" (`20:403`); her account is "in the hand of somebody who wrote the whole time she talked" (`24:487`). |
| C15 Halloran's pronoun | **RESOLVED** | "she" throughout the grading scene (`24:157–183`), as at `14:13` and `14:33`. |
| C16 Tolliver / Talley / Tilling; Merrin / Perrin | **RESOLVED** | Gower (11 uses), Edda (5), Sedge (1, then "the warden"). None of the three old names remains. None of the three new names appears anywhere else in the repository's canon or manuscripts. I hear no close collision with the standing cast. |
| C17 Kiva's disk note | **RESOLVED** | She writes *Began after*, stops, and corrects it to *First felt* (`24:143–147`). The page Orla reads says "First felt after… Don't know when it began" (`24:501`), and Orla names the crossed word (`24:509–513`). |
| K1 / cold read: Noa and the register entries | **RESOLVED** | "She has three more of those in hers" is gone. Kiva hides both papers from the team (`24:303`). The keeper gives Noa "a remark about his lamps" (`24:405`), and Noa writes "Find out what a T-0 is" (`24:443`). |
| CR2 tins from 51.2 drams | **RESOLVED** | "eight tins, and part of a ninth" (`23:601`, `23:607`); six drams a tin by `17:153`. |
| CR5 aisle width | **RESOLVED** | "an aisle of three" (`19:243`); agrees with `19:305` and the twelve-pace floor. |
| CR6 what "Half!" names | **RESOLVED** | The referee states it before the bell (`19:255`). All five calls then read one way: `19:313`, `19:361`, `19:369`, `20:169`, `20:291`. It matches chapters 15 and 16 (`15:99`, `15:215`, `16:157`). Scores unchanged: 2–3, 4–7, 9–8. |
| CR7 "Renn. You're a Carry" | **RESOLVED** | "You've nothing here to cut. You're my Carry. Get her out." (`22:255`), and Kellan declares it (`22:261`). |
| CR8 eight cuts | **RESOLVED** | "Eight rungs, and seven of the cuts were hers… All seven" (`18:335`). Seven at seven-tenths is under six seconds. |
| CR11 "a branch, a fortnight" | **RESOLVED** | "A branch, six hours. The Pit, a fortnight." (`24:537`); restored at four (`24:205`). |
| CR13 Anwen's two hours forty | **RESOLVED** | "most of them in the dark before anything had come out of the blue at all" (`18:223`). |
| Dray "too far away to have heard" | **RESOLVED** | Thursday's line stands (`21:197`). On the day she "heard you call it" from the rail and the reserves told her whose notion it was (`23:551`). |
| Mara "I heard a girl tell" | **RESOLVED** | She has it from Orla (`24:133–137`); she was across the road (`24:141`). |
| Four adults saying "I want that understood" | **RESOLVED** | None says it. `17:167`, `21:265`, `23:555`, `24:29` are four different sentences. The wider construction is down to five uses, all Anwen's or Perrin's (script count reproduced). |
| CR12 chapter headings read "Kiva:" on chapters with cutaways | **OPEN, by design** | Unchanged. Not in the brief; it is the book's convention in all three movements. |
| Cold read: live cords three paces below an open stance | **OPEN, owner decision** | Unchanged (`23:135`). Not in the brief. The board still clears her on the struck event, not on distance (`24:231`). |
| Cold read: Brask and Rhea write nearly the same note | **OPEN, owner decision** | Unchanged (`20:23`, `23:421`). Not in the brief. |

Nothing is PARTIAL.

### 2c. The items the prompt names

- **Sequence clock and draw.** 10:12, 10:22, 10:23, 10:24 agree in the slate (`22:211`, `23:33`, `23:627`), Mara's pump-house reading (`24:71`), the board (`24:231`), the keeper's book (`24:275`) and the tape ("nearly twenty-four minutes past ten", `24:409`). The tape is 0.02 + 0.26 + 0.03 = 0.31 (`24:413–425`); "a third" of the dram (`23:213`); two drams is six goes (`24:355`).
- **Shares.** 51.2 gives 25.6, 6.4, 9.6, 9.6 (`24:245`). The vote spends 2.0 + 1.0 + 3.0 + 2.0 + 1.6 = 9.6 (`24:385`). Standing 72.0 (`24:249`).
- **Dark-floor geometry.** Mark ten paces from the race, ten from the terrace, twenty-two from the lattice house (`21:119–121`, `21:281`, `21:345`). The string goes ten paces west to the race (`22:125`, `22:137`). Table five short of the sump and fourteen east of the race (`22:107`, `22:295`); thirteen paces to the lip (`23:53`).
- **Link before lid.** "It's the lid first" (`22:289`); the trade stated in the direction (`23:33`); Kiva's lapse (`23:47`); the lid "a third of the way down" at her call (`23:313`); the slate (`23:627`); Vane aloud (`23:629`); Kiva's column (`24:549`). All agree.
- **Noa's actual knowledge.** The tape; the keeper's remark; the slate; Rhea's draft card by the Chair's leave (`24:431`). He does not know of the register entries or what a T-0 is. One soft spot predates the repair: his list also holds "A plate in a meadow. A seventh reed." (`24:439`) with no handoff shown. Both are reachable through Kiva's book, which he now reads and wrote in on Thursday (`24:427`, `24:435`). Optional note O7.
- **Kiva's disk chronology.** Still door shut (`23:199`); fingers find the warmth (`23:219–223`); fist closed, nothing asked (`23:227–229`); still warm after the fragment (`23:277`); cooling at the top of the road stair and cold by the gate (`23:561–563`); told the same morning as "when she had first felt it" (`24:59`); written and corrected that night (`24:143–147`); the keeper's line added "in Saturday's pencil" because she did not have it until Saturday (`24:507`). One chain, no gap.
- **The 10:24:40 pattern and the disk stay unresolved evidence.** Nobody on the page connects the warmth, the fragment, the lamps, the tick and the reed. Kiva asks the disk nothing and it does nothing (`24:79–85`, `24:503`). The sequence is complete before she feels any warmth, so the disk teaches no technique. The fragment gives no tactic. The words *Unroofed*, *filter*, *Glory*, *Satori*, *Makers* and *Annick* do not occur in chapters 17–24 (searched).
- **Physical state.** Knee, fingers, nosebleed, Perrin's ribs and Stroud's hands carry consistently from chapter 23 through `24:535–539`.

### 2d. Do the records match the page?

`STATE_LEDGER.md`, Movement Three section: **matches** on every line checked (dates, the sequence, the disk, the stand-down, the team book, the tape date, knowledge, names, lane calls).

`AUTHORSHIP.md`: hashes, word counts and the measurement table **match** what I computed. Chapter 24 narration reproduces at mean 13.09, 29.7% at five words or fewer, 4.64% at forty or more; the movement's narration at 12.03 and 2.00%.

`provenance/MOVEMENT-003-CONTINUITY.md`: **matches, with one stale row.** Section 8, "Left knee | No landings until the 2nd of next month." The page, and this same file's calendar rows for the 2nd and the 13th, its section 2 and its section 11, all say the 13th. This is R1.

Two wording points, neither needing a fix to prose:

- The repair report says the link opens "with about a grating in hand." On the page it is about one count, a quarter of a grating (`23:133`). The checkpoint words it correctly ("her count of iron stands at one").
- The checkpoint twice says the fragment came "about 40 s after the link opened." That is the keeper's estimate (`24:277`). By Kiva's and Dray's count on the shelf the blade lifts on *Five* (`23:121`) and Dray is at seventeen to nineteen when Kiva comes back from "three counts, four" (`23:261–273`), which is nearer ten or twelve counts. Both lines are in the frozen draft and neither review raised it. I am not asking for it to be reconciled, since the owner has ruled the pattern stays unexplained; I record it so that Movement Four does not treat forty seconds as measured.

### 2e. Contradictions newly introduced by the repair

None of substance. Two small strains are listed as optional notes O2 and O3: the cords' position relative to Kiva once they are "at the head of the ramp," and the gap under the lid now that "a third down" is stated four times.

---

## 3. Recheck 2 — the dark-floor decision and its cost

Read as one chain: the Kennel floor (`20:497–543`), the terrace (`21:125–197`), Monday (`21:201–213`), the field (`22:95–143`, `22:207–263`), the direction (`23:1–49`), the table (`23:567–655`), and chapter 24.

**Is the choice credible on the evidence available at the time? Yes.** Kiva has three stated reasons (`21:139`), a count fourteen better on a dark Kennel floor (`20:525`), and Brask's support from the lane (`21:165`). Against her she has the custom, Bettan's rule, Anwen's question and her own weir note. The race is now raised by Gower in so many words (`21:167`). Kiva reads the note aloud as "half a reading, and it's against me" (`21:171`). Bettan answers from what she has seen and limits it: "I'll swear to that much, and not to what I haven't seen" (`21:177`). Vane agrees (`21:179`). Kiva's inference, that a bus carries a tune and has none (`21:181`), is wrong for a reason nobody present could have had. The slate records objection and answer (`21:195`).

Her mark no longer contradicts her. She keeps clear of gratings and benches because spilled ash there "is swept, not tinned" (`21:117`); the feeder line is gone. The hindsight nudges are gone: no "idle thought" at `21:95`, no "most of an answer" at `20:543`, no Bettan looking at the cinders. The link is described once, by its keeper (`21:67–71`); Mara's line at `21:289` judges it and does not re-describe it. The Monday paragraph (`21:213`) gives the dark floor an honest second motive without claiming it.

Seven cautions remain (Bettan, Anwen twice, Druce, Vane, Gower, Monday's custom). They no longer read as five people saying one thing, because each now carries different content and the other side of the scale has weight on it.

**Is responsibility shared without excusing Kiva? Yes.** She says "It was mine" to Dray (`23:553`) and to Stroud (`24:43`), and her column names Anwen's two questions and her own relief at being answered (`24:533`). The professionals keep theirs: Vane on the gate, "my line on the slate as much as yours" (`23:629`); Vane alone on the lid (`23:33`, `23:629`); Rhea on the ward (`23:407`); Bettan's answer on the slate under her name (`21:195`). Kiva records the foreman's trade as his and adds "I'd have gone anyway. That part is mine" (`24:549`). Nobody is let off and nobody is made a scapegoat.

**Distinct human consequences.**

| Person | What is on the page | Where |
|---|---|---|
| Anwen | Her list, turned round. "I'm not going to be let off it, and I'm not letting you off it either, and a dram at par doesn't do it." Nothing is settled; Kiva writes "Anwen, I don't know." | `24:321–341`, `24:539` |
| Gower | Two springs' wait, and his rung cut by somebody else on his own catcher's word. "It doesn't seem to be a thing I can use." | `23:611–621` |
| Rhea | "That was Rhea's." The first of her notions paid for with another woman's hands; she goes to the stretcher to say so. | `23:407`, `23:459`, `23:527` |
| Stroud | Confirms Rhea came. On the dark floor: "I've six weeks of somebody else buttoning my coat in which to make up my mind about that. I'd not hurry me." | `24:41–45` |
| Vane | The trade in his own name in the direction, on the slate and aloud; Cade's ribs "under my name"; his name first in the finding. | `23:33`, `23:627–629`, `24:209` |
| The healers | Aske: eased inside the hour, "I haven't cured anything," a fortnight. The infirmary healer: an account that charges for the opinion not taken; Orla pays; Kiva carries the crate. | `24:21–33`, `24:483–495` |
| An unqualified team | Team Twenty-Eight's catcher. His father shut the shop. "I expect you are." Kiva counts eleven empty lines. | `24:255–263` |

They do not sound alike. Gower is sardonic, Stroud flat, Anwen level and exact, the catcher without heat, the healer's bill dry. That also answers part of the cold read's note about one shared adult register.

**Does successful action stay developed and trackable? Yes.** The diff shows chapter 22 changed in nine short places and lost no line of its action. Chapter 23's shelf sequence, the lid crew and Rhea's seven rungs are word for word apart from the corrected counts and the insertions above. Both lane carries are unchanged apart from the three clarified calls. Vane's longer direction falls inside the countdown and the countdown was re-cut to carry it.

No required fix. One optional note (O1) is in this priority's inserted text.

---

## 4. Recheck 3 — chapter 24

Read straight through, once, at 8,571 words in eight sections.

**Does it breathe? Yes.** The quiet passages are now complete thoughts: the look at Stroud's hands (`24:51`), the fever (`24:107–111`), the page she writes alone (`24:143–149`), the eleven lines (`24:263`), the two papers held to the lamp (`24:293`), the platform image (`24:399`), the walk down the yard (`24:481`). Measured with the review's script, narration is at a 13.09-word mean with fifteen sentences of forty words or more, where the first draft had 8.72 and none. I read all nineteen sentences of thirty-eight words or more. Each is additive and parses in one pass; none is a manufactured run-on. Length was not counted against it, as instructed.

**Are reports and withheld mysteries distinguishable? Yes.** What is reported is closed inside its scene: Aske's verdict, the grade and card, the findings, the shares, the keeper's line, the Halden offers, the account. What stays open now has one holder and one next step each:

| Open question | Who holds it | Next step on the page |
|---|---|---|
| The seventh reed | Halloran, who does not know: "I can't tell you what that means" (`24:183`) | Halden is asking |
| The lamp ring and the 2446 margin | Kiva, with Mara | "I'll ask her… by myself first" (`24:295–299`) |
| The cliff on the tape | Noa | "Find out first," before the first of next month (`24:467–475`) |
| The bearer's book and the earlier hand | Orla and Vane | Orla has asked; Vane cannot yet read it (`24:513–525`) |

Only one person who knows something defers it: Orla at the cart, with a date (`24:93`), and she pays it on that date (`24:513`). Mara's deferral is merged into one delivery (`24:271`). The stacks echo and Rhea's card teaser are gone.

**Does at least one thread resolve on the page? Yes, several.** The healer's account, promised at `20:403`, is sent, paid and answered (`24:483–495`). Orla's Sunday promise is kept. Kiva's question in the cart about how such ash is written (`24:51`) is answered by Halloran (`24:187–197`) and spent at the vote (`24:313`).

**Does Kiva act between reports? Yes.** She studies the hands and resolves to ask; writes and corrects her own page; asks Halloran her own question and keeps the answer two days; counts the board; decides to see the Library's reader alone; reads Anwen's conditions back and rewrites the third (`24:377`); adds her own heading to the columns (`24:549`).

**Changed joins.** I checked every changed paragraph in chapters 17–23 and all of chapter 24 for one-pass syntax, attribution, referents and cadence. Attribution holds in each inserted exchange (the terrace, Gower at the table, Halloran and Kiva, the catcher, Anwen). The sixty-odd narration joins in chapters 17, 19, 20 and 21 change no fact and read cleanly. Four sentences are a little knotty for the ear and are listed as optional notes O1, O4, O5 and O6. None misleads.

**Protected beats.** Confirmed intact by reading both versions and by string comparison: every line Ysra speaks; "Show me six"; Perrin's "I'd like it said… that I mind" and "And I vote yes"; Anwen's three conditions; Kellan's "Two drams is six goes"; the team-book entry; Noa's "They're her numbers… I measure. I don't own"; the seventh-reed scene (Halloran's pronoun and "I can't tell you" are the only changes); the bearer's book and "somebody had been there before him"; and the last four paragraphs, which are identical.

No required fix.

---

## 5. Corrections

### Required

**R1. Continuity checkpoint, section 8, row "Left knee."** `provenance/MOVEMENT-003-CONTINUITY.md` still reads "No landings until the 2nd of next month." Change to the 13th, to agree with the page (`24:491–495`, `24:539`) and with the same file's calendar, section 2 and section 11. A record fix by whoever next maintains that file. No prose is involved.

That is the only required correction.

### Optional taste notes

None of these justifies a repair pass. Each is one word or one clause if the owner wants it.

- **O1.** `23:407` "That was Rhea's, and she did not dress it." It follows "her hands in wet cloth," so a listener may hear *dress* as a wound-dressing for a beat. This is the line that carries Rhea's ownership. "Dress it up" or "soften it" removes the echo.
- **O2.** `23:135` The cords now lie "at the head of the ramp, three paces below her and a pace north." The head of the ramp is at the far lip of a trench three paces wide (`21:61`, `23:61`), so it is nearer two or three paces north of the shelf. Low confidence; the old "on the ramp" fitted the offsets better.
- **O3.** `23:331` The gap under the lid is "as high as a man's waist" a few counts after the lid was "a third of the way down" (`23:313`). The line predates the repair, but "a third down" is now stated at `23:33`, `23:627` and `24:549`, and a counting reader may set them side by side. Low confidence, because the doorway's height is never given.
- **O4.** `24:241` "…*Purse sheet and poles: 3.0,* which Kiva saw on the way in, and did not think that anybody had put there for them." The relative clause reaches into an embedded one. Two sentences would be easier aloud.
- **O5.** `19:279` "…leaning on the rail, who had not come out of loyalty." The *who* sits next to *rail*.
- **O6.** `21:213` "One of those two teams" has only "Twice she thought that she saw" to point back to.
- **O7.** `24:439` Noa's list holds the plate and the reed with no handoff shown. A clause ("out of her book") would close it. Predates the repair.
- **O8.** `24:287–291` and `24:525` Two old pages in a hand nobody present can read now sit two hundred lines apart. They are told apart by holder and place. If they are the same hand that is a plant and should stay; if not, one adjective would keep them separate for a listener.
- **O9.** `23:13` "Dane!" and `23:33` "Dray!" are still shouted twenty lines apart. The editorial review noted it; the brief did not carry it.
- **O10.** Repair report, section 2: "about a grating in hand" should read "about a count." Record wording only.

### Owner decisions, unchanged by this recheck

Those listed in the repair report's section 7 stand as written: Aske as "he"; the three names; the Monday forty-nine paragraph; chapter 24's length; the tape date's thirty-day month; and the 13th falling three days after Anwen leaves.

---

## 6. Limits

- Same model as the drafting, review and repair seats. I may share their blind spots, and an affinity for this prose cannot be ruled out.
- Read-aloud judgments are from the page. Nothing was voiced or timed.
- Chapters 1–16 were consulted by line lookup only. Where a finding rests on them (`08:257`, chapters 12–16), I checked the cited lines and no more.
- "PASS" here means the three repair priorities are met and no specific defect remains that needs prose. It says nothing about how the movement lands with a real reader.
