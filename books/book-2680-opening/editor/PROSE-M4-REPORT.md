# Prose pass, Movement Four (*The Real Call*), Chapters 25–32

Ticket M4, 2026-10-28. Author seat O'Connor 1.3.x (Monroe Jackson), Claude Opus 5.5.
Branch `feature/2680-prose-m4`, base `origin/main` 4677a03. Canon used: `universe/SEED-2680.md`
§2, §3, §6 (items 4 and 5), §8, §11, §12; `editor/MOTIF-BUDGET-REVISION.md` §5 (beats 6–11), §6,
§8.4, §8.5, §8.7; `BOOK_MAP.md` §8; `packets/MOVEMENT-004.md`; `CHARACTERS.md`; seat `VOICE.md`.
Continuity, read only: M1 on main (Ch 2, 3, 7, 8), M2 Ch 13 (`kindling-2680-m2`, the Line's four
cart questions), M3 Ch 22–24 (`kindling-2680-m3`, exit state). Style reference: the pilot's prologue
and Ch 1. Base copies and check output are in `.foreman/scratch/` (not committed).

## 1. Numbers, before → after

`grep -oiE` per file, as in the pilot. *count\** is `\bcount(s|ed|ing)?\b`. *nine/eleven* are raw word
counts; after the pass every remaining one is a fixed quantity (noted). *X/Y* is the hand count of
"It was not X. It was Y." / "It did not X. It Y." after the pass, dialogue included.

| Ch | Words | write-it-down | ledger | notebook | record* | count* | nine | eleven | Measure | aloud / out loud | to … face | book/col/card/page | X/Y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | 5,635 → 4,294 (−23.8%) | 2 → 0 | 1 → 0 | 2 → 0 | 5 → 0 | 1 → 0 | 6 → 0 | 4 → 0 | 0 → 0 | 1 → 0 | 3 → 0 | 50 → 0 | 0 |
| 26 | 5,564 → 5,137 (−7.7%) | 1 → 0 | 1 → 0 | 7 → 0 | 2 → 0 | 4 → 0 | 3 → 0 | 3 → 0 | 1 → 0 | 1 → 0 | 1 → 0 | 22 → 0 | 1 |
| 27 | 5,218 → 4,151 (−20.4%) | 3 → 0 | 4 → 0 | 0 → 0 | 1 → 0 | 7 → 0 | 2 → 0 | 5 → 0 | 0 → 0 | 2 → 0 | 0 → 0 | 20 → 0 | 1 |
| 28 | 4,964 → 4,878 (−1.7%) | 2 → 0 | 1 → 0 | 2 → 0 | 0 → 0 | 7 → 0 | 2 → 0 | 7 → 0 | 0 → 0 | 1 → 0 | 1 → 0 | 12 → 0 | 3 |
| 29 | 5,571 → 5,382 (−3.4%) | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 7 → 0 | 3 → 0 | 1 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 10 → 5 | 2 |
| 30 | 6,075 → 6,097 (+0.4%) | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 25 → 0 | 2 → 0 | 0 → 0 | 0 → 0 | 2 → 1 | 0 → 0 | 6 → 2 | 3 |
| 31 | 6,578 → 5,553 (−15.6%) | 0 → 0 | 3 → 0 | 3 → 0 | 0 → 0 | 8 → 0 | 3 → 0 | 4 → 0 | 0 → 0 | 1 → 0 | 1 → 1 | 33 → 0 | 2 |
| 32 | 5,975 → 5,601 (−6.3%) | 7 → 0 | 2 → 0 | 0 → 0 | 0 → 0 | 3 → 0 | 4 → 3 | 2 → 0 | 1 → 0 | 1 → 0 | 1 → 0 | 50 → 6 | 1 |
| **M4** | **45,580 → 41,093 (−9.8%)** | 16 → 0 | 12 → 0 | 14 → 0 | 8 → 0 | 62 → 0 | 25 → 3 | 26 → 0 | 2 → 0 | 9 → 1 | 7 → 1 | 203 → 13 | ≤3 each |

Residue, all checked by eye: Ch 32's three *nine*s are fixed (the hearing "at nine", Mara's "ninth
month" re-sit, "the twenty-ninth"); free nine 0, free eleven 0. Ch 30's one *aloud* is Rhea
re-declaring roles (the Call, seed §3). Ch 31's *to her face* is physical ("from her wet knees to
her face"). The 13 book/col/card/page hits are a Flask's grey column, playing cards, Pru's yellow
Circuit card, and the team's ash book once (prop, one clause). Three chapters exceed −15%: Ch 25,
27 and 31 lost the Library (the Reader, the record hand, the settlement, the Annick box, the
request book), Vane's Tansy Wold tracing, Mrs. Cobb's ledger lore and the written debriefs, all
exposition or record business. New scene was added only where canon asks for it.

**§8.5 / §6 mechanical checks** (run on Ch 25–32; output `.foreman/scratch/prose-m4-checks.txt`):
banned phrasings 0; ledger/notebook/column-as-record 0; theme words (remember, passed on…) 0;
closing `*Why:` 0; time in counts 0; counting as habit/tactic 0; free nine 0 (window filter hits
only "at nine", an hour); free eleven 0; fixed nines posts/rings 0/0; decimals 0 (readouts are
spoken in words: "two hundredths", "a dram and a quarter"); Measure Hall / Rule Nine / Team Eleven
0; no chapter ends on a count; the saying 0 (correct for M4).

## 2. §4b self-check (counts after the pass)

| Sibling device | Count | Note |
|---|---|---|
| Call/condition repeated back so it counts | 0 | Messages are relayed once (Rhea's runner, Ch 28; the Home Line boy via Mara, Ch 31). |
| Reading/instrument decides a beat | 0 | Ch 28 stack: the beat turns on Kiva's warm thread she did not call and on Noa saying no to a figure he wanted. After fix 1, Orla credits his choice, not "you and your pen". |
| Kept/preserved/sealed thing saves someone | 0 | Mara's sealed dream page and the Reader's wax are gone. |
| Number refrains renumbered; countdowns; timing closes; tallies | 0 | "About a dozen seconds" once (Ch 26); "every ten minutes" once (Ch 29); seal times, throw tallies, "Two." tallies, "Four. Five. Six." holds, all cut. |
| Spoken-record phrases ("I'd like that said/known", "understood between us", "All of it, in order", "to his face", "I'll say so on Tuesday", "to anybody who asks", "the Chair included", "Crest hears this… as it was") | 0 | The first pass had four of the newer kind; fix 1 cut them (§9). |
| Meter/gauge simile tics | 0 | |
| Witnessed-by-a-crowd as payoff | 0 | Cut "every assessor in the building", "In front of her", "in front of a tuner/Chair", a second "in front of two schools". |
| Read-backs ("one at a time", "nobody had a figure wrong") | 0 | Kellan's read-back copy gone. |
| Counting as structure (distance countdowns, try tallies, watch settling a beat) | 0 | Pru's paces and Kellan's watch-count on the wharf replaced (Pru narrates the Flask; Kellan watches Rhea's light lengthen). |
| Ritual question list as structure/title; chapter ending on debrief answer | 0 / 0 | Orla's debrief heard twice as a scene (Ch 28, one question; Ch 31, three, in conversation). One *section* closes on its answer (Ch 28 §3). The Line's cart list appears once, when Vane adds the cost (Ch 27). |
| Documents as evidence | 0 | Halden's claim is said by Adlam in person; no pinned papers; no tag quoted; no file. |
| Timing objects as arbiter | 0 | The bench time glass is cut. |
| Shared speech tics | — | *I'll not / I'd not / I'd as soon / shan't*: Orla, Mara and Vane only. *I'd like*: Pru 4, Vane 1, Kiva's remembered line 1. *I want*: Anwen 2, Rhea 2 (commands), Kellan 2. |
| "It was not X. It was Y." >3 in a chapter | 0 | Max 3 (Ch 28, 30). |
| Refrains | — | haul 3 in M4; slack 1; beat 4 (Halloran's Step lesson, the stepped bag); steady 10 across 8 chapters. |

Further refrains, after fix 1: "answer ready" 2 (both in Ch 25: Anwen's quoted line and Stroud's stair), so Ch 48's "speech ready" stays fresh. Kellan's "speech" is cut. Annick's images are given in full once (the Warden, Ch 25, with the colors held back); Ch 31 has one brief echo with the held-back parts; Kiva's read-back to Orla is cut. Kellan's mother's cups appear once (Ch 31). The Line's four cart questions are listed once (Ch 27, Vane's speech); Ch 29's company board is a separate thing.

Closing gestures by section: one section closes on a debrief answer (Ch 28 §3); one on Mara's
third word ("Hers. It always was.", Ch 32 last section, then the cup handle). No kind closes
two sections, and none closes two in a row. Every chapter ends on plain action.

## 3. Main changes

**Ch 25 *Asked Nicely*.** The right-hand-column line, Noa's notebook, the T-0 "Transient
Register" and the Hanley Street clerk are cut. Noa asks for Kiva's leave aloud, for the new month
and for a new term (nothing to any house without her leave). Kiva answers *T-0* as "what a keeper
chalks… fault, no cause found". The answer is true and ready, and she is holding back the two lamp
nights and the dream. The Library section is replaced by **the Warden at Coper Street** (§5 beat
7). The Order wants her for a year, one door, the others shut, and the hand would rest. The cost
is the year: no Regional Gates, no team. Asked why the Order does it, the Warden gives Annick's
images: every road, the lights that touch, the sky not torn but gone like a roof, full and paying
attention, every lamp in Meridian. Kiva recognizes them and calls *Hand, cold* under her breath.
The Warden mentions that Orla sat in that chair by her window sixteen years ago, which is how Kiva
learns Orla withheld it. The Warden holds back the colors and the waking for the house. Aske's
Library leave becomes leave to watch Saturday from a bench.

**Ch 26 *However Produced*.** Orla's confession is about the Warden's chair in 2664, not a
notebook. Orla turns it back on Kiva ("The dream… was it yours?… Who knows?"). She will not tell
Kiva what the Warden gave her, so Kiva goes up the hill unprimed. The Hanley Street register, the
clerk's cough and "Rowan Instruments" borrowing volumes are cut (lines 57, 97, 109, 277). Noa finds
the notch on every pen and the blank Low Lane tape. Halloran explains a stepped bank. Adlam says the
claim, *however produced*, and its caution aloud, with no patent-room document. In the drying yard
Kiva tells the team, unasked, the two lamp nights and the Warden's offer. She **keeps the dream itself**: "There's a part I see, when it happens. I'm keeping that part," per packet 004 (fix 1).
Anwen's "I'm not done" stands.

**Ch 27 *One Crossing*.** Anwen's "write me the counts" becomes "Don't come out to the culverts."
The Library tracing, Tansy Wold, E.K. and the request book are cut (§5 beat 8). Vane goes to the
Wren House about Cade's ribs. Aske asks whether he came about the fingers, which nobody at the cart
had told him about. At the yard Vane recites the Line's four cart questions (Ch 13), says the cost
was never one, and asks Kiva aloud what it cost. He then makes it the cart's fifth thing on his
floors: "What it cost, and to whom, before anybody's let go home." Orla makes her own rules with no
inherited ledger. A new short Coper Street scene has Mara refuse to say yes or no for Kiva ("I said
no for you once, to Ilse Corran") and plan her two sentences to Orla; that visit pays off in Ch 32.
The go is called "Rowan. Ember, to still." with no *One/Two* count calls.

**Ch 28 *The Cheap One*.** Count calls and "Four… Eight" holds are cut. "She gave it a number"
becomes she named it. The stack is "a tenth and a hair", so the accounts still reconcile: 0.03,
0.30, 0.11, 0.31, leaving 1.25. Kellan's jar becomes his mother's cups put down (M1). Orla's
finger count becomes watching the flush come back "inside your minute". "Two." tallies are cut.
Rhea's card is now a runner's message. The chapter ends on Mara's nightly finger press (M1 Ch 8),
not on copying a sheet to Anwen.

**Ch 29 *The Night Van*.** The standings keep *Closed. Lives. Works. Tinned.* plus *Faults* in
chalk (packet: violations), not "Remarks… written against your name". Pike's throw tally, "slower
by a count", seal times, "count twenty" and "Dark! One." are cut. Rhea's slate is now "Nothing open.
Van." Anwen's half-sheet is cut. The chapter ends on Rhea's order, not "That's a remark… it's mine."

**Ch 30 *What's Behind You*.** All 25 *count* hits are converted: a breath, a moment, "for as long
as it takes to walk it to the wharf", "slow cart's pace". "It's a school's count. I had it off a
man who had it off them" becomes Perrin's "It's what we say at a lid." Pru's distance countdown
becomes narration. Kellan's watch-count becomes watching Rhea's light lengthen. Rhea's slate,
"under my name", "I'd have it written" and the file/card are cut. Rhea sits with her face in her
hands.

**Ch 31 *Come Back Clean*.** Mrs. Cobb has no ledger, no installer's *Why* and no copied tag. Her
building's rule is her own. She takes the second rung on Kiva's and Pike's word and names whose
doors she will knock on: Hand. Perrin reports that the Pellow cupboard lamp came on. Rhea's slate
is cut, and her "wrong two words" are thoughts, not a card (M1 Ch 8). The Library box is replaced
by **the Order's house at evening practice** (§5 beat 9). Kiva stands at the back wall. The Warden
tells the sisters the Unroofing, adding Annick's own light among them, the color with no word and
the waking before she found out. Kiva tells the Warden she had the color and answers "not this
year". The Warden: "We'll ask again… when your hand is worse." Orla's debrief at the lane covers
the Weighbridge, with the cost said. At the stove Kiva says the canonical four sentences.

**Ch 32 *Held of the Line*.** Aske learns of the wharf from Pike in person, not a tin-tag letter.
The pinned papers are cut: Adlam tells Kiva of the Halden claim and Tuesday's hearing. Kellan's
list, jar and "in writing" are cut, and the Order's letter is cut. Orla's bench keeps Mara's two
sentences, and Ysra's note is now spoken. The bearer's book is replaced by **the watch's first
sitting** (§5 beat 10). Kiva asks "Why me?" The Ferren, in the chair in 2669, tells what Corran
said: the stair after the Tallow fire, *Will they say why?*, a month for a better reason, sealed
to the Kindling day. She says Mara was asked and said no and the watch went round her. The
Ferren's question then makes the scene new beyond the prologue's "I told her no": "Did she tell you
that we went round her?" Nobody ever went to tell Mara. Kiva lays the plate on the oak and says it
warmed once. The River Flats gives notice of a recall motion for Sunday, with cause to be said
before the watch and before her. **Vane goes to Coper Street** with his hat off and tells Mara. She
asks the plate's meter, shutdown path and hand. Vane: no meter; recall on a vote; "Hers. It always
was."

## 4. Renames applied

Measure Hall → **the Placement Hall** (Ch 32, the basement board). Old Ch 26's "Measure Hall
annex" patent room was cut. Rule Nine and Team Eleven: 0 uses. Numbered rules kept: Rule Fourteen
(Ch 26, 32), Rule Nineteen (Ch 32). Tournament: "your school's Regional Gates" (Ch 25), with bare
"the Regional" as the cast's shorthand.

## 5. Dependencies fixed (from the ticket)

- 25:23, 25:43–59, 25:157, 25:173, 25:303: column, field book, notebook, Transient Register, Hanley
  Street clerk, all cut.
- 25:285: Orla's "bearer's book… another hand in a ledger" now follows Ch 24 ("the watch… a favor
  twenty-five years old").
- 25:35: "consent in writing" becomes spoken leave.
- 26:57/97/109/277: cut. The Library and Reader do not appear in M4.
- Ch 27: the cost-at-the-cart beat now rests on Ch 13's four questions, which omit the cost.
- Ch 27 "eleven hundred": becomes "a full Pit".
- Ch 31: the Annick read is gone; Kiva stands at the wall while the Warden says what Annick saw.
- Ch 32: the watch sits; the Ferren speaks; it is not redundant with the prologue.

## 6. Canon conflicts flagged (nothing invented)

1. **Seed §2 vs. Ch 2.** Resolved in fix 1 by changing the seed (§9 item 6).
2. **Ch 28 stack.** Resolved in fix 1: the beat now credits Noa's choice.
3. **Length.** M4 is 41,093 words, below the packet's 45–55k working length (the coordinator accepts it; no padding). Ch 25 (−24%), 27
   (−20%) and 31 (−16%) are over −15%; the cuts were record exposition.
4. **Packet 004** still says "three written conditions" and "Team Seven's accounts stay exact…
   written supervision". The prose has spoken conditions and spoken direction.
5. **The Warden.** The 2680 Warden is unnamed. She is the 2664 Warden by her own words ("a chair by
   my window"), and a different person from Ottilie Sand (2603).

## 7. Dependencies created for later movements

- **Ch 33** must drop its bearer's-book reading ("Fourth column", "Warm, once", "Write", Thirza
  Bly, the bursar answered "out of the fourth edition"). Its whole Coper Street scene is now in
  Ch 32: Vane and Mara, the good cup, meter, shutdown path and hand, "give me tea and not forgive
  me". The River Flats gave notice in Ch 32 and Kiva said she would come, so Ch 33's sitting should
  have her present to hear the cause. The vote is two to five against.
- **The Order** sent no letter. Ch 33:115 "the Order's grey letter" and Ch 34:229's unsigned
  written offer need reconciling. Kiva answered "not this year" in Ch 31, and the Order said it
  will ask again when her hand is worse. The Order now knows she has had the dream, including the
  color with no word. Aske said (Ch 32) he will ask the Order what they mean by rest, which fits
  Ch 40:271 if "wrote" becomes asked.
- **Halden's claim** was spoken by Adlam. The hearing is Tuesday the 3rd at nine, with the
  Weighbridge wardens and the grader asking to be heard. Ch 34 must not quote pinned papers or
  call for "the catcher's book".
- **Mrs. Cobb keeps no book.** Ch 36:155's written receipt "E. Cobb, Warden" should go.
- **Vane's fifth cart question** is "What it cost, and to whom, before anybody's let go home"
  (Ch 27). Ch 47 should match it.
- "*I did not ask it anything. It did not do anything.*" is not used in M4; it is kept for Ch 47.
- **Nothing was sent to Anwen** (no half-sheet, no "counts"), and she asked Kiva not to come to the
  culverts. Perrin goes out Saturday with the runner to tell her about Halden and the Weighbridge
  share. Later Anwen scenes must not cite a sheet.
- **Kellan** rides on the Halden license team for the Regional and stays on Seven; no half-sheet
  or list.
- **Accounts.** The team ash after Ch 28 is 1.25 drams in hand, enough for four crossings at
  0.31 with a hundredth over. The Weighbridge share waits on Anwen.
- **The Reader** (Lettice Arkwright) is not introduced in M4. Ch 48 introduces her with the cast.

## 9. Fix round 1 (verifier FAIL, coordinator list)

1. **§4b, spoken-record and witness lines cut or turned to action.**
   - 32:37: Kiva tells Adlam "I couldn't weigh it. I still can't."
   - 32:95: Kellan's "I'll say what I saw… to anybody" is cut, along with the Adlam reply and the cups. He says yes to Halden and would hold the corner again.
   - 31:177: Rhea's advice is now "Hold on to that. Most people let go of it the first time a ward does what they say."
   - 28:231: "Crest hears this… as it was" becomes Orla rolling the tape herself and putting it in her coat for the Placement Hall stair.
2. **28:227.** Orla credits Noa's choice ("You said no to a figure you'd wanted… with your ears red"), not the pen.
3. **31:341–345.** Orla's debrief asks "What did it cost?" as it always has (Ch 3). Kiva gives the street's cost. Orla: "Not only the street's. Yours as well. I've asked you that at this lane since the first night." The Vane line is cut.
4. **Tape opening.** 32:67 now reads "on Sunday, when it opens"; 32:261 "opens to chartered parties on Sunday".
5. **27:97.** "three years after she was dead".
6. **Seed §2 (~line 113).** Corran hauls Rhea, a Graywater probationer of nineteen, out of a Ferren culvert by the collar. After the Tallow fire she sits an hour on the Coper Street stair with the child. 32:287 now reads "It'll go down any culvert after anybody, and never once think to knock on a door afterward."
7. **31:191.** Matches Ch 8: a hand down through a grating; afterward, on the bank, *Something I carry*. "It didn't do anything. She did." becomes "I've wondered since whether it was why she was at that grating… I think she was only the sort who is."
8. **26:267.** Kiva keeps the dream from the team (packet 004). Ch 28 Pru now knows of "lamps that go out when you do, and a house on a hill".
9. **Refrains and tics.** As listed in §2. Stroud, Aske, Perrin's father, Mrs. Cobb and Adlam no longer use *-'ll not / I'd not*. "Did not make a speech of it" is varied.
10. **Dependencies added to §7** (below).

Additional §7 dependencies:
- **M5 Ch 36:335.** Mara's meter / shutdown path / hand "in two sentences" must match Ch 32. Her two sentences to Orla in the Old Yard (Ch 32 §3) are *You kept a thing from my table. Don't do it twice.* Her meter, shutdown path and hand question goes to Vane at Coper Street (Ch 32, last section).
- **M6 Ch 47:223–231.** The cart must run the Line's four (Was it closed. Who was hurt. What still works in the morning. What we tinned.) plus Vane's "What it cost, and to whom" (27:157), not Orla's five.
- **The team does not know the dream** at the end of M4. They know the two lamp nights, the Warden's offer, and Orla's 2664 visit. Any M5 scene that has them reacting to the dream's content needs a beat where Kiva tells them.
- **Seed §2 now credits the culvert rescue to Rhea.** Any canon doc repeating "pulls a child from a culvert after the Tallow fire" should follow.

Re-run after fix 1 (`.foreman/scratch/prose-m4-fix1-checks.txt`):
- banned phrasings 0;
- ledger/notebook 0;
- theme words 0;
- time in counts 0; counting habit 0;
- free nine 0 (three fixed: an hour, two dates); free eleven 0;
- Measure / Rule Nine / Team Eleven 0;
- no chapter ends on a count;
- X/Y ≤3 per chapter.

## 8. Commit

Single commit on `feature/2680-prose-m4` (sha in the ticket reply). Not pushed.
