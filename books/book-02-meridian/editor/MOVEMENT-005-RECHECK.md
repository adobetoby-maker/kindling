# Movement Five — targeted post-repair recheck

> Built by TAC

## Final disposition

**Repair accepted.** The sole blocking finding below was corrected exactly as
specified: `chapter-39.md` now has the party climb twenty steps to the landing and
thirty more, matching the established descending stair order. No other manuscript
change was made after this recheck.

## 0. Reviewer and disclosure

- **Checker:** Claude Opus 5.5 (`claude-opus-5-5`), in a fresh context, acting as continuity editor, not as manuscript author. No subagents.
- **This is a same-model check.** Opus 5.5 drafted and repaired Movement Five. This is not an independent human read or a different-model read, and it probably shares the drafter's blind spots.
- **Session memory:** the session opened with automated one-line titles of the repair edits (for example "Chapter 34 stair orientation reference clarified"). They said that edits existed, not what they contained. Every verdict below comes from the files on disk.
- **Inputs read, in full:** `editor/MOVEMENT-005-REPAIR.prompt.md`, `editor/MOVEMENT-005-REPAIR-REPORT.md`, `manuscript/chapter-33.md` … `chapter-40.md`, and `provenance/MOVEMENT-005-CONTINUITY.md`. I also ran targeted greps and diffs against `editions/movement-005-first-draft/` to find out whether a slip came from the first draft or from the repair.
- **Scope:** only the eight questions in the brief. No manuscript, checkpoint or other file was edited. This file is the only file written.

## 1. Verdicts by question

### Q1 — Toren never holds Guard while Edge is lit: **PASS**

Every Edge action is staged release → light → dark → set:

- **Strand cut (D+47).** Callie takes the strut ("Taking… Mine… Letting go") before he lights the heel (`chapter-35.md:81–93`). He darkens the heel on the way back, then sets the strut (`:139`).
- **Kill for Jab's lift.** "Toren let the strut go. The husk fell forward off it, and as it came up he lit the heel and killed it" (`chapter-35.md:213`). Afterwards: "Toren let the heel go dark and set a strut" (`:251`).
- **Retreat.** He releases the strut before the lid and the exit (`chapter-35.md:535`). The door kill (`chapter-36.md:67–69`) and the stair-top kill (`:181`) happen with no strut up.
- **Entry cuts (D+48).** Both cuts are made from the corridor. He steps in, "and let the heel go dark", before the first strut (`chapter-37.md:395–401`).
- **Arm-rope cut.** "He could not keep a strut up and light the heel together." He lets the husk fall, lights, cuts, darkens, and re-sets the strut as the husk rises (`chapter-38.md:235–245`). The creature's momentary balance holds the beat.
- **Lifter's move.** He releases the husk strut, then sets one strut under the lean (`chapter-38.md:441–445`).
- **Final kill.** "Toren did not light the spike. Not with the strut up." The handoff to Callie is spoken: "I'm giving you the lean… Give it me… Letting go… Mine". Only then "Toren lit the spike" (`chapter-38.md:585–597`). Ch 39 confirms: "He was holding nothing now. One thing at a time" (`chapter-39.md:9`). The point goes dark "At the end. Not after" (`:43`).
- The two-strut roof (`chapter-38.md:283–295`) is Guard only and is priced ("twice the price").
- The checkpoint states the same rule (`MOVEMENT-005-CONTINUITY.md:19, 230–231`).
- The kill order and the team dependency survive: Callie holds the door and the last lean, Jab holds the open, Toren puts in the point.

### Q2 — D+48 jars, catches, crossing, floors and final inventory reconcile: **PASS**

**Night before (ch 37).**
- 29 inside. Settling: 1¾ + 1½ + ½ = 3¾. That leaves 25¼, with jar 2 at 1¼ (`chapter-37.md:181, 239`).
- The top-of-road halt spends ½, so ¾ remains at the gate (`:325–327`).

**Gate frame.** "Three full jars and three empties" (`chapter-38.md:11`). That is jars 3–5 full, and 1, A and C empty.

**Jar 2.**
- It runs dry during catch 2 ("Jar… That's jar two done… It went on the first two catches"). That makes four empties (`chapter-38.md:127–147`).

**Jar 3.**
- Opened with "Eight in it. Two whole behind it, and that's sixteen. The line" (`:163`).
- It empties at "the eighteenth three, or the nineteenth": "That's the line… Sixteen in the frame. Two whole" (`:471–483`).
- 9¼ above the line was spent, which matches the night price (`chapter-37.md:181–187`).

**Crossing.**
- Jar 4 is opened under the line, and Dee prices it at 1½ a turn, "three, for two turns" (`chapter-38.md:529–531`).
- After the kill she reports "Jar four's at five. Three under the line, inside the two turns" (`chapter-39.md:141`).

**Chronology of stones and floors.**
- Dee's stone went "at the tenth" (`chapter-39.md:137`), Callie's "at the fifteenth three" (`chapter-38.md:541`), and Toren's at the seventeenth (`:431, 455`). The order is consistent.
- Floors: Callie "at my floor… Not under" (`chapter-39.md:81, 125`). Dee is at her floor once (`:133–141`). Toren is "a hair over" (`:117`), then at his floor at the landing (`:319`).

**Recovered ash.**
- Five empties go into the lifting: 1, 2, 3, A and C (`chapter-39.md:183`).
- Gross 32: 8 + 8 + 8 + 4 clean from Toren's jar, plus 4 dirty.
- Jab's river draws take 6: Toren's 4 and 2 from Jab's second jar. That gives 22 clean (`chapter-40.md:45–49, 65`).
- Fence 13 + lifter 22 = 35 clean and 4 dirty (`:65–73`).
- Dee's night draw takes 1½, leaving 20½ (`:291`).
- Home 24 untouched (`:65`).
- The checkpoint ledger matches line by line (`MOVEMENT-005-CONTINUITY.md:142–212`).

### Q3 — The lifter's late move and Toren's single-strut hold are priced: **PASS**

- **Reserve plant.** "Two turns" is planted at the D+48 measure: "Toren's own had come back in the night to two turns, near enough" (`chapter-37.md:305`). The unit is glossed in ch 33: "in turns of the glass, as long as it would hold a strut" (`chapter-33.md:131`). The checkpoint gives a three-and-ten as about one glass turn (`MOVEMENT-005-CONTINUITY.md:230`).
- **Timing.** The move comes "At the seventeenth three" (`chapter-38.md:431`), which is about two counts before the handoff.
- **Price said aloud:** "That's the last of the stone. I'm on mine… Two turns of mine, near enough. One strut" (`:455`).
- **Cost made visible.** His reserve is shown "going under it by the breath" (`:481, 523`).
- **Rest of the ledger.** He ends "a hair over" his floor (`chapter-39.md:117`). The box strut costs him (`:261, 269`), and the ramp strut takes him to his floor: "I'm at my floor. I'm stopping" (`:317–319`). The next morning he is at "A turn. Not two" (`chapter-40.md:185`).
- No reserve appears from nowhere.
- **Non-blocking note:** the margin is thin. Two turns buys roughly two counts of a lean, plus a finger of point. The "near enough" hedges and the lean's shrinking body carry it. This is a taste question, not a leak.

### Q4 — Yard, door, stair, corridor, threshold, Callie's fall and belay: **FAIL (one small count inversion)**

**What passes:**
- **Yard:** the pipes are on Callie's left while she walks west, with the clean strip on their north side (`chapter-34.md:21–25`).
- **Stair going down:**
  - The first flight is 30 steps down east.
  - It turns at a landing against the east wall.
  - The second flight is 20 steps down west.
  - They step off facing west, with the door in front of them (`chapter-34.md:183, 271`).
- **Door and heaps:**
  - The door opens toward the stair and sweeps the stair-side heap back in a fan (`chapter-34.md:247`).
  - The corridor-side heap has its own source under the gap (`chapter-34.md:289`; `chapter-36.md:25`).
- **Corridor sides** stay consistent in both directions:
  - The tray is on the right going west (`chapter-34.md:279`).
  - Going east they walk "the right-hand wall… the room side" (`chapter-36.md:5`).
  - On D+48 they walk "on the right-hand side… under the tray" (`chapter-37.md:361`).
- **Threshold:** the cuts are made from the corridor, then Toren steps in (`chapter-37.md:397–401`).
- **Callie's fall order:**
  - The lee goes out first, and the curve stays pale.
  - Her legs go, and she falls onto the still-fixed conduit.
  - Only then does the Ward leave the steel (`chapter-39.md:89–101`).
- **Belay:**
  - Both ropes are pulled from above.
  - The back rope runs through the landing ring and twice round the rail post.
  - Callie only calls it (`chapter-39.md:311`).
  - The ropes are moved "up to the ring at the top" (`:315`).

**What fails:**
- **`chapter-39.md:305`:** "It went up. Thirty steps' worth of smooth concrete, to the landing, and twenty more."
- Going **up** from the door, the party first climbs the lower (second, west-running) flight of **twenty**, then the upper flight of **thirty**. The line gives the numbers in going-down order.
- The slip is in the first draft (`editions/movement-005-first-draft/chapter-39.md:301`). The repair did not introduce it.
- The repair did make the stair explicit and compass-clear in ch 34, and it rewrote the very next paragraph of ch 39. So this is now a direct numerical contradiction inside the brief's named picture, not a taste question.
- It moves no body and no mechanic.

**Non-blocking notes (no change required):**
- **Lifter against the curve.** "The lifter leaning on the room side of the same steel a foot from her heels" (`chapter-39.md:17`) is picturable, because the curve spans more than her stance.
- **Lantern.** The corridor-floor lantern "where Miss Wren had put it" (`chapter-37.md:425`) is never shown being set down.

### Q5 — Sky samples, Pell, sun markers, Sowerby papers and day labels agree: **PASS**

**Sky samples.**
- Callie: D+47 going in, 1 in 12 (`chapter-34.md:137`). Coming out, 2 in 12, and she refuses to call it a trend (`chapter-36.md:213–219`). D+48 going in, 1 in 12 (`chapter-37.md:329–331`). After the kill, no count (`chapter-39.md:345–353`).
- Pell: he counts "From noon… two hours and more" and sees "Seven", admitting "I missed some… Then she saw more than I did… I'd not swear to it" (`chapter-36.md:301–311`). Overnight there is no count (`chapter-40.md:141`).
- His heartbeat method is kept: "sixty to a turn" (`chapter-36.md:301`).

**Sun and time markers.**
- The deadline is "by the time the hill's shadow's on the gate" (`chapter-33.md:375`). The start is noon (`:435, 523`).
- The D+47 exit is "the middle of the afternoon", with the sun over the drum (`chapter-36.md:201`).
- On D+48 they enter "at the end of the morning" (`chapter-37.md:323`) and exit in the middle of the afternoon (`chapter-39.md:329`).
- The fight uses "since they came in" and "the whole fight" (`chapter-39.md:19, 131, 165`).

**Sowerby's papers.**
- Four papers (`chapter-33.md:53`): the first on D+47, the second on D+48 (`chapter-37.md:297`), the third on D+49, "One left" (`chapter-40.md:219–221`).

**Day labels.**
- "Three days ago… on the forty-sixth" (`chapter-40.md:345`).
- Sowerby "a day past the cycle. Or three", which matches D+55 or D+57 against D+54 (`:299`).
- "Eight days" from home (`:361`).

### Q6 — No-kneeling, names, mare, vent jars, speakers and numeric calls: **PASS**

**Kneeling.**
- Jab crouches by his own sense (`chapter-35.md:215`). His collapse is caught: "That goes for knees" (`:389, 445`).
- Callie is "crouched" at the stair top (`chapter-36.md:167`).
- Jab crouches through the D+48 fight. When he goes to his knees at the kill, Dee catches it: "Jab. Up off your knees" (`chapter-39.md:69, 185–187`).
- Callie's injury exception is stated (`:189–191`).
- Every other kneel is outside the fence.

**Names.**
- Callie's narration uses "Miss Wren" throughout chs 34, 37 and 40. The Toren and Jab chapters use "Dee".
- Dessa is planted before her payoff (`chapter-33.md:527` → `chapter-40.md:333`).

**Mare.** Duchess is planted (`chapter-33.md:97`) and paid off (`chapter-39.md:407`; `chapter-40.md:311, 325`).

**Vent jars.**
- Two go by the stone (`chapter-36.md:251–253`). Three are packed on D+48 (`chapter-37.md:305`).
- The first is full at catch 4 (`chapter-38.md:265`). The last is used at the kill (`chapter-39.md:45`).
- Three stay under the racks with a chalk cross (`chapter-39.md:287–291`), and they agree with `chapter-40.md:31, 65, 357`.

**Speakers.**
- There is no consecutive same-speaker attribution. I checked with a scripted scan, and the ch 40 Pell pair is split by "And you?" said Toren (`chapter-40.md:271`).

**Numeric calls.**
- They are labelled: "Jar *N*… Open", "*N* caught", "The three's in four breaths", "first vent jar".
- **Non-blocking note:** "We're at thirty-two, and two open" (`chapter-35.md:427`, unchanged from the first draft) can be heard as "two jars open". It means "jar two open". Dee's next line ("Four more, and we're at today's line") makes the sum clear.

### Q7 — Route, breach, boxes, home Flasks and `lifter` are clearly preserved: **PASS**

- **Approved route only.** Dee: "we go to the first door and no further. Not the second, not to look. Nowhere near the round one. We're not going hunting" (`chapter-37.md:117`). The creature is found "lying on what they had come for" (`:367`). The drum is never entered. The third-door boundary is set at `chapter-33.md:313`.
- **Breach as a one-off.**
  - Planted the night before: "the rule's still the rule, after… it's once… both our names on it" (`chapter-37.md:195`).
  - Said at the crossing: "This is once" (`chapter-38.md:525–527`).
  - Written on the paper: *Once. For the Director.* (`chapter-39.md:413`).
  - Restated after: "Not as a thing we'll do again" (`chapter-40.md:75`).
  - The checkpoint carries Director review into M6 with the standing rule unchanged (`MOVEMENT-005-CONTINUITY.md:21, 401–403`).
- **Two wheel boxes.** "Two. Not three. The third's open" (`chapter-39.md:281`), and they are carried out in lead (`chapter-40.md:359`).
- **Home Flasks untouched.** "The home three don't cross the bridge" (`chapter-37.md:197–199`), and "Home, twenty-four. On the cart. Not touched" (`chapter-40.md:65`).
- **`lifter` as a field term.** It is named because "nobody had a better word" (`chapter-36.md:365`). Rook's grade is hedged, "That was a Flask. Maybe" (`chapter-40.md:99`), and written with its source attached: "a Flask (R.)" (`:101`). The checkpoint confirms it is a creature term, not a character (`MOVEMENT-005-CONTINUITY.md:23, 68–69, 415`).

### Q8 — No new blocking contradiction introduced by the repair: **PASS**

- I diffed the ch 39 repair against the frozen draft and read every repaired passage in context.
- The four self-introduced problems listed in the repair report (§6) are fixed on the page. For example, the husk's grey "by the cabinets, which shivered and did not stand" is at `chapter-38.md:549`, and Dee's jar-four line is merged at `chapter-39.md:141`.
- The Q4 stair inversion is in the first draft, not introduced by the repair.

**Checkpoint wording nit (non-blocking, documentation only).** "The steel door: standing open against the lobby wall" (`MOVEMENT-005-CONTINUITY.md:338`). The page calls this space "the flat place" at the foot of the stair (`chapter-37.md:339`).

## 2. Verdict

**Repair not accepted.** Seven of the eight questions pass. Q4 fails on a single first-draft numerical inversion in the stair picture. The repair made that picture explicit, so the inversion is now a contradiction rather than a taste question.

**Smallest exact correction needed:**

- **File:** `manuscript/chapter-39.md:305`
- **Replace:** `It went up. Thirty steps' worth of smooth concrete, to the landing, and twenty more.`
- **With:** `It went up. Twenty steps' worth of smooth concrete, to the landing, and thirty more.`

No checkpoint change is required: `MOVEMENT-005-CONTINUITY.md:52` already records the stair in going-down order, 30 then 20. After this one-word swap, the repair can be accepted without a further read.

**Optional, owner's call.** None of these is required for acceptance:
- Toren's thin reserve margin (Q3).
- The lantern that is never shown being placed (Q4).
- "thirty-two, and two open" (Q6).
- "lobby wall" in the checkpoint (Q8).
