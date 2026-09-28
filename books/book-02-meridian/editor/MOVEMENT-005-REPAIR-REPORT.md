# Movement Five — consolidated same-author repair report

> Built by TAC

- **Author run:** Claude Opus 5.5 (`claude-opus-5-5`), the same selected manuscript author, writing as Monroe Jackson 1.3.0 / O'Connor 1.3.0.
- **Brief:** `editor/MOVEMENT-005-REPAIR.prompt.md`, including its owner/orchestrator rulings.
- **Method:** one run, no subagents, no Agent tool.
- **Reading order:**
  1. `manuscript/chapter-33.md` … `chapter-40.md` in full, in order;
  2. `editor/MOVEMENT-005-COLD-READ.md`;
  3. `editor/MOVEMENT-005-EDITORIAL-REVIEW.md`;
  4. `provenance/MOVEMENT-005-CONTINUITY.md`.
  The packet and the M4 checkpoint were not needed. The rates I relied on (Toren's own reserve measured in glass turns of strut; the still-door rate; two struts at twice the price) are the ones quoted in the editorial review and the M5 checkpoint.
- **Scope:** only the three priorities and the owner rulings. After the edits I read the whole repaired movement once, in order. That read found three small contradictions introduced by the repair itself, and I fixed them (§6). I did not open a broader pass.

## 1. Files changed

| File | Change |
|---|---|
| `manuscript/chapter-33.md` … `chapter-40.md` | Sentence- and passage-level repairs, listed in §3 |
| `provenance/MOVEMENT-005-CONTINUITY.md` | Updated to the repaired page (§5) |
| `editor/MOVEMENT-005-REPAIR-REPORT.md` | This file (new) |

**Not touched:**
- the frozen edition `editions/movement-005-first-draft/`;
- the cold read, the editorial review, all prompts, the packet, the map and the bible;
- `AUTHORSHIP.md`, which is not a deliverable of this brief;
- all other books and all chapters outside 33–40.

**Frozen-edition check.** I took SHA-256 hashes of all eight frozen files before editing and compared them after the last edit. There were no differences (`shasum -a 256 editions/movement-005-first-draft/* | diff - <before>` gave empty output). For example, `chapter-33.md` is still `dd6e4cae…88cd`.

## 2. Word counts (`wc -w`)

| Ch | POV | Before | After | Δ |
|---|---|---:|---:|---:|
| 33 | Toren | 6,637 | 6,730 | +93 |
| 34 | Callie | 6,483 | 6,550 | +67 |
| 35 | Jab | 6,442 | 6,483 | +41 |
| 36 | Toren | 5,059 | 5,196 | +137 |
| 37 | Callie | 5,681 | 5,905 | +224 |
| 38 | Jab | 6,336 | 6,917 | +581 |
| 39 | Toren | 4,662 | 4,869 | +207 |
| 40 | Callie | 4,893 | 4,936 | +43 |
| **Total** | | **46,193** | **47,586** | **+1,393** |

- The total stays inside the packet's approximate 42,000–48,000.
- No catch, adaptation, kill or scene was cut. The fight is the same length or longer.
- Scene breaks: 105 (was 106). One `---` went when the "last one above the line" beat moved from the middle of ch 38 into the catch-two section.
- **Viewpoint after repair:** Callie 36.5%, Toren 35.3%, Jab 28.2%. The owner accepted this allocation, and I did not rebalance it. **Cumulative, chapters 1–40** (270,387 words): Callie 34.5%, Toren 33.4%, Jab 32.1%.

## 3. Exact changes, by priority

### Priority 1 — the D+48 mechanics now obey the ash and configuration rules

**One configuration at a time (owner ruling).** Toren never holds a Guard strut while his Edge is lit. Each Edge beat is now staged as release → light → dark → set. No untrained blend is planted.

| Where | Before | After |
|---|---|---|
| ch 35, strand cut and re-set | He re-set a strut while the heel was still lit | "letting the heel go dark as he came, and set a strut" |
| ch 35, the kill for Jab's lift | He killed a husk that was leaning on his strut | "Toren let the strut go. The husk fell forward off it, and as it came up he lit the heel and killed it" |
| ch 35, after the lift | He set a strut with the heel still lit | "Toren let the heel go dark and set a strut" |
| ch 37, entry cuts | He cut with the heel, then struts at the first three | He cuts both ropes, steps in, then "let the heel go dark" before the first strut |
| ch 38, husks turn to worked things | "Toren's heel, still lit a hand's width" | "Toren's hands, with a strut just gone out of them" |
| ch 38, the near arm-rope cut | "He left the husk on its strut, pinned… lit the heel" | "one thing at a time." He lets the husk's strut go at the top of a ten, and the husk falls on its front. He lights, cuts, darkens, then re-sets the strut as the husk rises. This is the creature's momentary balance holding the beat |
| ch 38, the lifter moves | Toren kept the husk strut **and** set the lean strut | "I can't hold the husk and the lean both." He **releases the shrinking husk strut** and sets one strut under the lean. The husk rises. **Jab kills it at the end of a ten and catches its grey at the three**, and it does not stand again |
| ch 38 end / ch 39 opening, the point | He lit the point with the lifter leaning on his strut | "Toren did not light the spike. Not with the strut up." He hands off: "Callie. I'm giving you the lean." — "Give it me." — "Letting go." The lifter slides the last pace against the **room side of her still curve** on the threshold, and she says "Mine." **Then** he lights. Ch 39 opens with the lifter against Callie's curve and Toren "holding nothing now". After the kill he lets the point go dark: "At the end. Not after." The old "His strut had nothing on it. He let it go" beat is gone |

**Kill order and team dependency are preserved.** Callie isolates the room and holds the final lean. Jab holds the open push. Toren puts in the point.

**Repricing the catches.**
- **Frame at the D+48 gate** (ch 38 opening): "Four full jars and two empties" → "**Three full jars and three empties**". Jar 2 is open in Dee's arm.
- **Jar 2's ¾ is now spent on catches one and two only.** During catch two Jab feels "the pour at the bottom of the jug" and says "Jar," before it is dry.
  - The whole "last one above the line" beat moves here, otherwise unchanged. Dee says: "That's jar two done… It went on the first two catches, and they were the biggest… They'll not all be that big. It's less every time." The frame now holds four empties. She opens jar 3: "Jar three. Open. Eight in it. Two whole behind it, and that's sixteen. The line."
  - The original beat at "the tenth" was removed.
- **Jar 3 funds catches two to about eighteen**, the diminishing middle, at about half a Handful per catch and falling.
- **The lifter's move** is re-timed from "the fourteenth three" to "**the seventeenth three**".
- **Jar 3 empties** ("the line") at "the eighteenth three, or the nineteenth". That text is unchanged.
- **Jar 4 funds the final open push.**
  - Dee prices it aloud: "Holding on an open's not a catch, Jab. It'll pull on this the whole time you're on it. A Handful and a half a turn, near enough. Three, for two turns. Not a grain more."
  - During the push: "The clean cold came in at his left palm hard and fast, faster than it had come all the fight… he could feel the jar going down under it."
  - After the kill Dee says: "Jar four's at five. Three under the line, inside the two turns. That's what it cost. That's what gets written."
- **Preserved:** the catch-by-catch rhythm, the late seventh catch, both adaptations ("It learned"; "It learned again"), the line crossing, and "off before the ten".

**Toren's reserve.**
- Dee measures Toren on D+48 morning in ch 37: his own "had come back in the night to two turns, near enough". The first draft never showed this.
- At the move: "That's the last of the stone. I'm on mine… Two turns of mine, near enough. One strut."
- He holds one shrinking lean on his own for about two counts, then hands it to Callie. That leaves him "a hair over" his floor for the finger of point, the box strut and the ramp strut, all as before.
- In ch 39 Dee's summary becomes: "You held two struts, and then that thing on one… On your own, the last of it. And lit the point after."
- "Stone's half" at the first adaptation was removed, because it could not last to the seventeenth three.

**"For two turns" → "inside two turns"** wherever the words mean the allowed window:
- Toren's crossing: "Inside two turns of the glass. Not three";
- Dee: "Inside two turns under the line, and not a breath more";
- the ch 39 paper;
- Dee at the grading (ch 40).

**The signed-line breach is priced, recorded and carried forward (owner ruling).**
- Ch 37, night: Dee says "the rule's still the rule, after. Two Flasks left inside, everybody out. If you say it, it's once. It goes in front of her at home with both our names on it."
- Ch 38: Toren says "And the rule's still the rule. This is once." Dee says "Written tonight, and put in front of her at home with both our names on it."
- Ch 39 paper: *Under the line on purpose, inside 2 turns: 3 Handfuls (jar 4). T. and D. W.'s call. Once. For the Director.*
- Ch 40: "That goes in front of her with our names on it. Not as a thing we'll do again. As a thing we did."
- Toren's choice and Dee's co-signature are unchanged.

**Callie's settled ash and her floor.**
- At the crossing (ch 38) she says: "My stone went at the fifteenth three. I'm on my own. I've got two turns. I've not got three."
- She takes the lifter's final lean on her still steel.
- At her floor (ch 39) she has blood in her voice and "hands… white to the wrists".
- Ch 40 reflection: "with the stone going out of her into a door and a bit until it was gone, and then her own".

**Dee's costs.** Her stone "went at the tenth [three]" and she ends at her floor once. Her night sickness is unchanged, which keeps it bounded and visible.

**D+48 is inside the Director's narrow permission (owner ruling).** Ch 37, night: Dee says "It's in the first room… The room she sent us to, and the box she sent us for. It came at us there. So we go to the first door and no further. Not the second, not to look. Nowhere near the round one. We're not going hunting for anything. If it's not in the first room in the morning, we don't go looking for it. We come out." On arrival: "It was lying on what they had come for."

### Priority 2 — the six broken physical pictures

1. **Ch 37 threshold contradiction.** Deleted "Toren went in over the threshold… He lit the heel as he went." It now reads "Toren lit the heel. He did not go in over the threshold. He stopped in the corridor…", so he cuts from the corridor first.
2. **Ch 34/36 door heap.**
   - Ch 34: the opening door now "swept the heap at its foot back across the flat place toward the stair, in a long grey fan, and they stepped back out of it".
   - Ch 34, corridor side: "There was a heap on this side of the door too, against the steel where the gap was, a hand deep. It was twenty years of what had come under the gap in threads."
   - Ch 35: "from the old heap inside the door".
   - Ch 36: "There had been a heap on the corridor side of the door since before any of them was born: twenty years of grey come under the gap in threads."
   - The ch 36 closing sweep, which pushes the killed husk's heap toward the corridor, was already correct and is kept.
3. **Ch 34 pipes.** "on her right" → "on her left". The north-side clean strip stands.
4. **Ch 34 stair.**
   - It now reads: "The first flight went down east, toward the front of the building, thirty steps along the right-hand wall. It came to a landing against the building's east wall and turned back on itself, and the second flight went down the other way, west, twenty more, back under the corridor above."
   - Callie's deduction now reads: "…they had stepped off the last step facing west, with the door in front of them. The corridor went away from it the same way, into the hill."
5. **Ch 39 fall order.**
   - "He saw the lee go out first… The ridge… slid in over the threshold… round the curve and over it."
   - "The curve itself was still pale. The last of her was still in it."
   - Then her legs go, she falls onto the still-fixed conduit, and only then does the Ward leave the steel.
6. **Ch 39 belay.**
   - Toren and Jab pull from the landing, above the load.
   - "The back rope went from the tail of the board up through the iron ring at the landing and twice round the foot of the yellow rail's post, so that if the front rope went, the ring and the post would hold the sledge, not anybody. Dee took in the slack round the post… Callie stood on the landing beside her and called it, *pull* and *hold*, with one hand on the last of the tail… and nothing else."
   - At the landing "they moved both ropes up to the ring at the top".

**Preserved:** the gate/door push–pull plant, the lean-to "the wrong way up", "Pull the door", the ramp-and-ring logistics, and the rule that nobody carries a box in their arms.

**Optional minor item fixed (one clause).** On the ch 36 retreat they now walk "along the right-hand wall of the corridor, the room side, away from the tray".

### Priority 3 — counts, calls and small continuity slips

- **D+48 frame:** three full and three empties (above). The chain of openings and emptyings is 2 → 3 → 4. The five empties used for lifting after the kill (1, 2, 3, A, C) are unchanged and correct.
- **Pell's sky count** (ch 36).
  - Start marker: "From noon, when you went through the gate". Duration: "two hours and more".
  - "Seven that I saw… I missed some. I'd look down to mark one, and look up, and not know if I'd missed the next. And you can't look at that edge long."
  - "Then she saw more than I did." "More toward the end than the start. I'd not swear to it."
  - The paper note is changed to match. "Pell had been counting since noon."
  - The heartbeat method is preserved, and so is Callie's refusal to claim a trend.
- **One sun marker.** Pell's deadline is now "by the time the hill's shadow's on the gate" (ch 33), which cannot be read as a start time. The start is "noon".
- **D+48 time of day.**
  - Entry is "at the end of the morning" (ch 37).
  - "All morning" inside the fight becomes "since they came in" or "the whole fight" (chs 38, 39, 40).
  - Exit stays "the middle of the afternoon".
- **"Two days ago" → "three days ago"** (ch 40).
- **Sowerby days** (ch 40): "That's two days of Sowerby dosing her" → "That's Sowerby dosing her off her blood, badly, a day past the cycle. Or three." This matches D+55 or D+57 against the D+54 cycle.
- **Kneeling.**
  - Ch 35: Jab keeps to a crouch by his own sense ("a knee on that floor was as near sitting as he wanted to go"). The rule is no longer attributed to Dee before she says it. His collapse in the sink stays, and Dee catches it ("That goes for knees").
  - Ch 36: Callie is "crouched" at the stair top.
  - Ch 38: Jab crouches throughout; the knee references are removed.
  - Ch 39: Jab goes to his knees when the lifter falls, and Dee catches it: "Nobody kneels… Jab. Up off your knees." He "got up onto his heels".
  - Callie's injury exception stands.
- **Numerical labels.**
  - Jars: "Jar one… Four whole left in the frame" (ch 33); "Jar two… Three whole left" (ch 35); "Jar three…", "Jar four…" (ch 38).
  - Catches: "One caught / Two caught / Three caught / Four caught / Seven caught".
  - Vent jars: "the first vent jar full… Two vent jars left. They'll hold more than that one did. It's giving less every time". This also answers the vent-jar capacity point.
  - Push calls: "The three," said Jab; "Nine… The three."
  - "Three in four" → "The three's in four breaths."
- **"Turn" as reserve** is glossed once, at its first appearance (ch 33): "That was how she measured his own: in turns of the glass, as long as it would hold a strut with no stone under it." "Inside two turns of the glass" marks glass-time. "Turn" as a rope round a pipe block was already self-evident.
- **Names.**
  - Ch 37, Callie's narration: all 19 narrative "Dee"s → "Miss Wren", matching chs 34 and 40. Other characters' dialogue is untouched.
  - Ch 36: "that Toren had killed" → "that he had killed".
  - Ch 39: "She knew it before Toren said it" → "Toren saw her know it before he said it".
  - **Dessa** is introduced before the ending pays her off (ch 33, at the gate): "At home, in the big book at the shed, Dessa had left six lines blank at the foot of the departure page, for *back*."
- **Plants re-established.**
  - **Duchess** (ch 33): "tied to the near wheel by her rope halter, cropping the thin grass along the foot of the pump house wall. She had not looked at the hill once."
  - **The two vent jars by the stone** (ch 36): Dee stands them "beside the flat stone with the chalk cross on it… 'They're not going on the cart.'"
  - **The three spare vent jars** (ch 37): packed from the cart on D+48 morning.
- **Read-aloud slips.**
  - Ch 40: the consecutive "said Pell" now has "And you?" said Toren between the two speeches.
  - Ch 34: the plate/paper doubt resolved to "the paper in his hand, the one he had copied the plate onto… holding the paper to it".
  - "on its sides" → "lying on its side" (ch 34) and "that had read a hundred and six" (ch 39).
  - Ch 35: "Lid… Leave it" → "Lid on it… Leave the box."
  - Ch 36: first "Ward" glossed as "the still steel of the hook".
  - Ch 38: the second "He did not know how he knew" was removed.
- **Not restyled:** the counting ritual, the three-lead voice, the reading ease and the developed length.

## 4. Preserved in substance (checked on the final read)

- **Injuries:** Rook's fever and wound (papers 4 → 1), Pell's ankle, Dee's crooked wrist, Callie's cracked ribs.
- **The sequence:** the first failed entry, the night planning, the second entry, the full developed fight, the team kill, two live wheel boxes, the three vent jars left under the hill, the ash lifting, the grading, and the D+49 departure.
- **The lifter:** the ten-and-three mechanism, the adaptations, the shrinking body, the open vent, and every husk collapsing when it dies.
- **The ledger:** the three home Flasks untouched, and the clean/dirty totals unchanged. Fence 13, lifter's 22 clean and 4 dirty at the fire, 20½ after Dee's night.
- **The road home:** still cut, the wash crossed in pieces, D+55 at best.
- **The sky** loses its count, and its cause stays unresolved.
- **Held back:** no rip entry, no third door, no Cinder or disk, no new continuing named character, no miracle cure, no infinite ash, no second hidden power.

## 5. Continuity checkpoint

`provenance/MOVEMENT-005-CONTINUITY.md` now:
- says it describes the repaired page, and that the frozen draft is unchanged;
- adds an **owner-rulings table** saying how each ruling is carried on the page;
- corrects the stair orientation, the two door heaps, Pell's sky count and its start, the time markers, Dessa and Duchess, the call labels and the kneeling rule;
- rewrites the **D+48 ledger**: frame 3 + 3; jar 2 dry during catch 2; jar 3 over catches 2 to about 18; jar 4's three priced as 1½ a turn for the open, inside two turns;
- rewrites the settled/own spends: Toren's own two turns on D+48 morning, stone gone at the seventeenth three, one strut; Callie's stone gone at the fifteenth three, the final lean, her floor costs; Dee's at the tenth three;
- rewrites the catch list and the fight sequence, marking the Guard/Edge handoffs, and the kills;
- updates Callie's fall, the belay, Toren's paper, the word counts, viewpoint, scene breaks and the watched phrase;
- adds the breach as an open M6 item for Director review.

## 6. Final read-through: problems the repair introduced, and their fixes

1. **Ch 38:** at the open push, "At the husk on the strut, which shivered". That husk no longer exists, because Jab has already killed and caught it. Now: "At the husk's grey by the cabinets, which shivered and did not stand."
2. **Ch 39:** my new "Jar four's at five" line created two consecutive "said Dee" paragraphs. I merged it into her preceding speech.
3. **Ch 36:** my first vent-jar plant repeated the ch 39 image of Dee "holding the counter to the bag and not saying the number". I replaced it with "stoppered and heavy and hot, and one of them was the jar from the rope."
4. **Ch 34:** I tightened "back under the hall" to "back under the corridor above", because the stair opens off the corridor, not the hall.

I found no other blocking contradiction.

## 7. Left unchanged on purpose

- **"Seventy years" (ch 37):** a setting constant, not an error (cold read #10).
- **Ch 36:** "the gap… against the left-hand wall" at the steel door. It is geometrically possible, and nobody asked for it to change.
- **Callie's bruised ribs on D+47** (review §5): a possible one-line twinge. It is outside the three priorities, so I did not add it.
- **The formula figures** (Flesch, sentence SD, section length, front-loading): these are standing owner conflicts, and the brief accepts the voice.

## 8. Unresolved owner-only issues

1. **Director review of the breach.** The crossing is recorded as "once" and is waiting for her. How she rules is Movement Six's to stage.
2. **New on-page rate:** Dee prices "holding on an open" at about **1½ Handfuls a glass turn**. I derived it to explain jar 4's three Handfuls. Should the owner confirm it as a working rate, or keep it as Dee's field estimate?
3. **Handing the lean to Callie's hook.** For the few breaths of the point, Callie's still curve holds the lifter's lean from the room side. I judged this to be the same "door and a bit", not Ward-at-scale, and it is what takes her to her floor. The owner should confirm.
4. **Jab's own configuration.** Jab lights his knife, kills, darkens, and only then catches (ch 38, twice). The page keeps these steps apart, but the canon has not stated whether Jab is bound by the same one-configuration limit.
5. **Toren's reserve under the lean.** On D+48 morning his own is "two turns, near enough", and it pays for about two counts of one shrinking lean. That rests on the reading that one count is about one glass turn (review §9), which the page implies but never states outright.
6. **Plan-level items carried from the review (§8), unchanged:**
   - viewpoint accepted, with M6 possibly leaning toward Jab;
   - two boxes accepted as the machine part;
   - "the lifter" is a field term, and Rook's Flask grade applies only to its own Yield;
   - the lost sky count is sufficient proof that the rip changed.
