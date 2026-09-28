# Movement Five — editorial review (chapters 33–40)

> Built by TAC

## 0. What this is, and what it is not

- **Kind of review:** a **fresh-context, same-model editorial review**. The reviewer is Claude Opus 5.5 (`claude-opus-5-5`), which is the same model that drafted Movement Five.
  - It is **not** a human read and **not** an independent model. A same-model reviewer shares the author's habits and may not notice them.
  - It is not a blind cold read. The prompt supplied the continuity checkpoints for Movements Four and Five, the book map, the canon bible, both name registries and the formula. I read all of them before judging.
  - The drafting reasoning was not in this context. The session did open with automated memory summaries: one-line titles such as "Chapter 37 revised: Toren's cutting sequence reordered" and "Chapter 39 corrected: Tongs location fixed". They told me the draft existed and had been lightly self-corrected, not how it was made. One finding (§3, item 1) looks like residue from the ch 37 revision that title describes. I say so rather than pretend I found it blind.
  - I did **not** open `editor/MOVEMENT-005-COLD-READ.md`, which now exists, so that it would not steer these findings.
- **Coverage:** all eight chapters, read in order (`chapter-33.md` to `chapter-40.md`; 46,193 words by `wc -w`). Every evidence section in the prompt was also read. The movement is complete as supplied.
  - The manuscript files are byte-identical to `editions/movement-005-first-draft/` (SHA-256 checked, all eight), so this review is of the first draft.
- **Where the canon verdicts come from:**
  - Only the evidence supplied.
  - A claim supported only by the plan is labelled **plan adherence**, not a canon error.
  - A fact the evidence cannot settle is labelled **unverifiable here**.
  - A few manuscript `grep`s outside Movement Five checked plants and names. They are cited where used.
- **Nothing was edited.** The only file written is this one. The metric script ran from stdin; its definitions are in Appendix A.

---

## 1. Reader response (unscored), then two lenses

**Where interest caught:**
- Rook's fever in the first page of ch 33, and "Then I don't come in" (`chapter-33.md:379`).
- The steel door's shriek (ch 34).
- The sink in ch 35: "It thought he was a hole in it" (`chapter-35.md:335`). It is the movement's best scene, and it connects the creature to Jab's whole history with Tonk.
- Pell's pump and its flap (ch 37). It is a plain physical idea, told by the right person, and it becomes the fight's logic.
- The catch-by-catch fight in ch 38. It is trackable, it adapts, and each catch has a cost.

**Where interest slipped:**
- The long morning in ch 33 (water, floors, coats, the rag, the bridge, the gate, the rules, the carrier) runs about 6,000 words before the gate opens. Rook's fever carries it, but only just.
- The plan-and-price conversation in ch 37 (`:105–195`) retells what the reader has just watched.
- The grading at the fire in ch 40 (`:35–83`) is a tally the reader has mostly already done.
- Inside the fight, a slower reader loses track of what "Three" means (§3, item 9).

**Who matters most:**
- Jab: at the rope, and then deliberately not coming off at the end.
- Dee: the watch who takes his hands nineteen times with nobody taking hers.
- Callie: in the door with her back to all of it.

**What I expect next:**
- The wash crossed in pieces at first light on D+50, if the wind drops.
- Senna's D+54 cycle missed.
- The sky that has "lost its count" turning into the Sag surge at home.

**Would I continue?** Yes.

**Scores.** These are editorial judgements, not measurements. Anchors: 5 = understandable but inconsistent, 7 = engaging with located weaknesses, 9 = compelling with few distractions. The two readers are not averaged into a gate.

| Dimension | Fluent 13-year-old | Adult genre reader | Exact location | Reason | Confidence |
|---|---:|---:|---|---|---|
| Opening pull | 8 | 8 | `chapter-33.md:3–7` "Toren woke before the light and counted them… something about Rook was wrong." | A person to worry about before any logistics | High |
| Keep reading | 9 | 8 | `chapter-35.md:505` "Something was coming along the rope."; `chapter-38.md:567` "Toren lit the spike." | Every chapter ends on pressure. The adult notices a second "Tomorrow we decide" (`chapter-36.md:395`) | Medium-high |
| Interest / freshness | 8 | 9 | `chapter-37.md:29–71` (the flap); `chapter-35.md:335` | A creature defined by a mechanism the characters share, not by size | High |
| Clarity / flow | 6 | 6 | `chapter-37.md:389–391`; `chapter-34.md:183, 271`; `chapter-38.md:185–197` | A self-contradicting sentence pair, an unfollowable stair, and overloaded numbers in the fight | High |
| Character attachment | 8 | 9 | `chapter-35.md:469` "He could not find where he stopped. Dee had had to find it for him." | Each lead's gift is shown as its danger | High |
| Humor / warmth | 7 | 8 | `chapter-36.md:353–357` "It's got my job"; `chapter-39.md:377` "That's furniture." | The humour comes from the characters and is well timed. It is sparse in chs 38–39, rightly | Medium |
| Action / suspense | 8 | 7 | `chapter-38.md` catches 1–19; `chapter-38.md:439–449` | The contest is trackable and it adapts. The adult is pulled out by Toren's reserve lasting far past its stated size (§4) | Medium-high |
| Progression payoff | 8 | 8 | `chapter-38.md:329` "He did not come off late again."; `chapter-40.md:171` | The D+47 failure becomes the D+48 technique | High |
| Connection | 8 | 7 | `chapter-38.md:445` "That's the cart."; `chapter-39.md:43` "At the end. Not after." | Callbacks are earned. The adult notices the frame counts and the jar curve (§4) | Medium |
| Read-aloud quality | 7 | 7 | `chapter-38.md:185–217`; `chapter-40.md:269–271` | The short beats land. Numbers carry two meanings, and there is one double attribution | Medium |

---

## 2. Canon, power limits, knowledge boundaries and reserved truths

### Verified consistent with the supplied evidence

- **Sustain recalls active burden only; fixed damage stays.**
  - Jab's palm: "That's in the done part. I can't draw it" (`chapter-35.md:403–405`; `chapter-36.md:279–289`).
  - Rook's infection: "That's not Sustain. That's Sowerby's" (`chapter-33.md:51`).
  - This matches the bible's owner ruling of 2026-09-27 ("does not reverse old tissue damage once that damage has fixed").
- **The bible's five visible constraints on recall all appear on the page:**
  - exposure time (the room at 110–130);
  - ash quantity (the jars);
  - working depth (floors);
  - venting and rotation ("Off before the ten"; the watch takes the worker's leftovers);
  - active burden versus damage done.
- **Running out of ash puts the healer on their own reserve and risks making them the next casualty.** Dee at her floor (`chapter-39.md:131–139`) and sick in the night (`chapter-40.md:109–129`) is that rule, dramatised.
- **Ward stops matter, not radiation.**
  - The lee stops the crawling threads and the rope (`chapter-35.md:151–165`; `chapter-37.md:425–427`).
  - It does nothing for the room's reading, which keeps climbing inside it (`chapter-38.md:111, 495`).
  - Consistent with the owner ruling recorded in the M4 checkpoint.
- **The sustain-echo (bible, `PLANNED`, owner ruling 2026-09-27):**
  - It recalls loose ash and reconstitutes spawn (`chapter-34.md:461–473`; `chapter-35.md:21–37`).
  - It makes no ash from nothing ("It was everybody else's", `chapter-40.md:99`).
  - The kill is the locked team solution:
    - **Ward** isolates the current (`chapter-37.md:403–411`);
    - **Guard/Edge** opens and holds the route (`chapter-37.md:391–397`; `chapter-38.md:91, 211`);
    - **Sustain** senses and interrupts the pulse (`chapter-38.md:43–47, 535–553`).
  - Its ash refills the rotation **after** the kill, not before (`chapter-39.md:177–237`), as the map requires.
- **Plan adherence: the adults do not take the solution.**
  - Pell explains a pump.
  - Callie asks the decisive question, "And if somebody shut the river?" (`chapter-37.md:61`).
  - Jab turns it into "on the push" (`:85–87`), and Toren puts it in order (`:109–169`).
  - In the fight Dee confirms the principle Jab has already found ("She had known it before he said it", `chapter-38.md:149`). This passes, but narrowly; see §8, item 8.
- **Yield.**
  - Rook grades the lifter "a Flask. Maybe… with its hand in everybody's pocket" (`chapter-40.md:99`), and the Barrel stays unspent.
  - This is consistent with the bible's Yield table (`POSSIBLE`), where the Barrel/Breach is reserved.
- **Reserved truths stay reserved:**
  - the disk (not mentioned);
  - the Makers and Cinder;
  - Dee's door count;
  - Rook's third door;
  - Katori's words.
  - "Vell had one. On the heel of his hand" (`chapter-36.md:289`) adds a detail about Orrin Vell (`CANON`, Homura's lead researcher). It reveals no reserved truth. Whether Vell practised Sustain is **unverifiable here**.
- **Knowledge boundaries hold:**
  - Nobody knows whether the sky kept the lifter's time or the other way round ("I don't know which", `chapter-39.md:357`; `chapter-40.md:145`).
  - Nobody passes room 1. Dee's "nobody past the third door" is written (`chapter-33.md:311`).
  - The home Flasks never cross the bridge (`chapter-37.md:193–195`; `chapter-40.md:65`).
- **Hounds are not generalised.** "Husks come at a light" (`chapter-34.md:161`) is about husks. It does not conflict with the Book One exception for verge-hounds.

### Apparent tensions: evidence cited, owner ruling needed

1. **Toren holds a Guard strut while his Edge is lit.** This is the decisive kill's mechanics.
   - `chapter-38.md:207–211`: he "left the husk on its strut, pinned… lit the heel" and cuts the arm-rope.
   - `chapter-39.md:3–25`: with the lifter leaning on his strut, he "lit the point" and puts it in.
   - The bible's non-negotiable canon: "The Ember does not erase… the one-configuration limit below unbound mastery."
   - The bible's Guard paragraph (`POSSIBLE`) allows exactly this for a practitioner who can blend Edge and Stride, "once Guard is known and trained". It records Toren's Book One blend as "not yet a repeatable technique".
   - The non-negotiable "plant before climax" rule requires the solution to be demonstrated in training first.
   - A search of chs 18–37 found no scene in which Toren holds a strut while his Edge is lit. In ch 35 Callie takes the strut *before* he lights (`chapter-35.md:81–93`).
   - **Owner decision (§8, item 1):** permit it, and plant it in M5 before ch 38; or forbid it, and restage the two moments.
2. **Plan adherence: "Ward-at-scale."** The map's M5 row lists "Ward-at-scale" under training. The page deliberately does the opposite: a door and a bit, with nobody inside it (`chapter-37.md:213–219`). The bible's planned description of Callie's Ward ("not a projected field over a group or a room") supports the page over the map. I record the deviation and do not recommend a repair.

---

## 3. Continuity and action geometry

Each item gives the location, the problem, and the evidence.

1. **Sentences that contradict each other** (`chapter-37.md:389–391`).
   - The text reads: "Toren went in over the threshold. He lit the heel as he went. He did not go in over the threshold. He stopped in the corridor…"
   - The second version is the staged one: he cuts the ceiling rope from the corridor first. This looks like residue from the reordering.
   - A reader cannot tell which sentence to believe, at the fight's first beat.
2. **The steel door cannot sweep the heap to the far side** (`chapter-34.md:247`; `chapter-36.md:25`).
   - The door opens toward the stair (`chapter-34.md:249`; `chapter-36.md:105`). A door swinging toward you pushes the heap on your side back into the flat place. It cannot "spill into the dark on the other side".
   - `chapter-36.md:25` builds on that error ("The door had swept it through when they pulled it open"), and so does the corridor husk.
   - The right source is already planted: the grey "going under" the knife-blade gap "for twenty years" (`chapter-34.md:213–215`). Its corridor-side heap would be there anyway.
   - `chapter-36.md:87` (shutting the door sweeps the killed husk's heap into the corridor) is geometrically correct and should stay.
3. **The pipes are on the wrong side** (`chapter-34.md:21`: "on her right").
   - The river runs from the north (`chapter-33.md:73`). The bridge rail is on the upstream, north side (`:185`). The pipe crossing is "below the bridge, downstream" (`:187`), so it is south of the gate.
   - Walking west into the yard, the pipes are on her **left**. The "north side of the blocks" clean strip (`chapter-34.md:23`) is then correct.
4. **The stair can't be pictured** (`chapter-34.md:183, 271`).
   - Flight one runs "along the right-hand wall"; flight two goes "the other way"; the door at the bottom faces them; and the corridor beyond runs west.
   - Callie's deduction, "The stair had come down along the building's east wall and turned, and the door faced back the way they had come in", cannot be followed. Flights running *along* the east wall would leave them facing north or south, not west.
   - One sentence naming the direction each flight runs would fix it.
5. **Callie's fall onto her own hook** (`chapter-39.md:89–99`).
   - Toren sees "the pale of the curve on the threshold go grey and ordinary". Four lines later, "The last of the Ward was still in the steel… still fixed."
   - The injury depends on the conduit still being fixed. The order has to be: the lee goes out, the curve stays fixed for a breath, then her legs go.
6. **The injured belay** (`chapter-39.md:305–307`).
   - Minutes after cracking two ribs, Callie is the backup rope on a lead-loaded sledge: "the end of the back rope round her waist… holding".
   - This breaks Pell's own rule, "a rope round something that doesn't move" (`chapter-33.md:413`), which the chapter quotes two lines earlier (`chapter-39.md:303`).
   - It also breaks her body state. Dee's "not allowed to lift" comes at `chapter-39.md:187`, and "nothing heavier than a counter" at `chapter-40.md:193`.
   - The yellow rail or the top ring would do the job; Callie can still call it.
7. **Rope sides on the way out** (`chapter-36.md:5, 47`). Heading east, "the left-hand wall" is the tray (north) side. Earlier they kept away from the tray on purpose (`chapter-34.md:323`). This is minor and optional.
8. **The time markers on D+47 disagree.**
   - Pell's deadline "by the time the sun's on the gate" (`chapter-33.md:373`) is used for a noon entry. At `chapter-36.md:301` the same phrase is his start marker ("from the sun on the gate").
   - The gate stands at the hill's east foot, so the sun leaves it in the afternoon (`chapter-36.md:201`: "The sun was over the drum behind them").
   - Pell also says "That's four hours". That sits badly with the day's ledger: two halts, and 3¼ spent at forty turns (`chapter-34.md:397`). See §4.
9. **Numbers carry two meanings in the fight** (`chapter-38.md:185–197`).
   - "Three" is the push ("'Three,' said Jab, before she did") and, twelve lines later, the catch count ("'Three,' said Dee").
   - "Three in four" (`:217`) cannot be decoded on one hearing.
   - This is the movement's main read-aloud cost.
10. **Kneeling inside the fence.**
    - Jab "did not kneel… Dee had said that went for knees" (`chapter-35.md:215`). Dee first says it 230 lines later (`:445`).
    - Callie then kneels, uninjured, on the stair top (`chapter-36.md:167`). Jab kneels three times in the D+48 fight with Dee beside him (`chapter-38.md:255, 313, 463`).
    - Dee's restatement at `chapter-39.md:183` half-absorbs this. The earlier breaches should either be "crouched" or be noticed.
11. **Small arithmetic and wording slips:**
    - `chapter-40.md:343`: "the road they had come on, two days ago, at dusk". They arrived at dusk on D+46 and it is now D+49, so it was **three** days ago.
    - `chapter-40.md:297`: "That's two days of Sowerby dosing her". D+55 is one day past the D+54 cycle; D+57 is three.
    - `chapter-40.md:269` and `:271` are consecutive paragraphs, both "said Pell". The first is probably meant for another speaker; otherwise merge them.
    - `chapter-36.md:323`: "that Toren had killed", inside Toren's own viewpoint.
    - "on its sides" (`chapter-34.md:409`; `chapter-39.md:253`) reads as a typo for "side".

**Staging that works and should be protected:**
- The gate that pushes inward (`chapter-33.md:515`) planting the door that "opens toward you" (`chapter-36.md:105`).
- The lean-to "the wrong way up" over the hole (`chapter-37.md:409–411`), which is exact.
- The lifter dragging itself along the only rope it has left, toward Callie's heels (`chapter-38.md:431–445`).
- The copper twist left loose "so they would come" (`chapter-36.md:229`; `chapter-39.md:369`; `chapter-40.md:349`).

---

## 4. Ash-ledger audit

**The totals reconcile.** The page and the M5 checkpoint agree at every stated total:

| Point | Page | Check |
|---|---|---|
| Entry D+47: 40 inside (5 whole), line 16, 24 to work; home 24 | `chapter-33.md:325` | ✔ |
| Jar 1 opened at the pump house: "Eight in it. Four whole." | `:443` | ✔ |
| Halt 1: 1¼ spent → 6¾. Halt 2: 2 spent → 4¾; "three and a quarter" at forty turns | `chapter-34.md:95, 395–397` | ✔ |
| The lift, the sink and Dee's long draw empty jar 1 → "thirty-two, and two open" | `chapter-35.md:427` | ✔ (4¾ on one lodging-scale emergency, which is plausible) |
| Retreat and river: jar 2 8 → 5 → 29, "one over today's line" (11 of the 12 spent) | `chapter-36.md:259` | ✔ |
| Night settling 1¾ + 1½ + ½ = 3¾ → 25¼, 9¼ above the line, jar 2 at 1¼ | `chapter-37.md:177, 235` | ✔ |
| D+48 top of road: ½ → jar 2 at ¾ | `chapter-37.md:321` | ✔ |
| Jar 4 opened under the line, 8 → 5 | `chapter-38.md:511–513`; `chapter-40.md:39` | ✔ total; see (b) |
| Lifted 32: Jab 8 + 8, Callie 8 + 4 dirty, Toren 4, in five empties (1, 2, 3, A, C) | `chapter-39.md:181, 215, 295`; `chapter-40.md:45–57` | ✔ The rates match "Jab filled a jar while he filled a quarter" |
| River draws 6 (Toren's 4, then 2 of Jab's second) → 22 clean; "Thirty-five clean. Four dirty." | `chapter-40.md:45–65` | ✔ |
| Dee's night draw 1½ → 20½ clean; D+50 priced at 10–12 → about 10½ | `chapter-40.md:285–289` | ✔ The magnitude matches D+47's room rate |
| Vent jars: 2 used D+47 (left by the stone), 3 used D+48 (left under the racks) | `chapter-33.md:447`; `chapter-37.md:379`; `chapter-39.md:285`; `chapter-40.md:31, 65` | ✔ |
| Home 24 never crosses the bridge | `chapter-37.md:193–195`; `chapter-40.md:65` | ✔ |

**Where the ledger breaks: the D+48 fight's internal distribution.**

a. **The cost curve runs backwards.**
   - Jar 2 enters the room with ¾ of a Handful (`chapter-37.md:321`). It carries catches one to ten ("'Jar,' said Jab, at the tenth", `chapter-38.md:363`), which is about 0.08 a catch. These are the early pushes, the "palm's worth, and a little more" (`chapter-38.md:43`).
   - Jar 3's 8 then carries catches of roughly eleven to eighteen or nineteen (`chapter-38.md:387–461`), about 1 a catch.
   - Meanwhile the page says each push is getting smaller: "It's less… The husk's less" (`chapter-38.md:399`); "It pushed what it had. It was very little" (`:543`).
   - The per-catch price jumps more than tenfold as the work gets lighter. During the fight nobody else draws from the jar: Dee takes Jab's leftovers off her own stone (`chapter-39.md:135`).
b. **"Three under the line for two turns"** (`chapter-40.md:75`; Toren's record, `chapter-39.md:409`).
   - On the page the crossing lasts from "The glass is running" (`chapter-38.md:509`) to the kill at Dee's "Six. Seven." (`chapter-39.md:21–25`). That is less than one count.
   - "Two turns" was the **allowance**. The elapsed time was shorter, and 3 Handfuls in one count needs the long final push to justify it.
   - This is fixable in wording ("inside two turns") once (a) is fixed.
c. **Toren's own reserve lasts five to ten times longer than its stated size** (`chapter-38.md:449` → `chapter-39.md:115`).
   - At "the fourteenth three" his stone is gone and he has "a turn of mine. And a bit". He then holds **two** struts: one under the lifter's lean ("That's the cart", `:445`) and one pinning the husk. He holds them until after the nineteenth three and the crossing, which is about five or six counts.
   - The page's own clock says a count is about a glass turn: "twenty turns and more" for about twenty threes (`chapter-40.md:161`).
   - The book's rates, from the M4 checkpoint:
     - Toren's own reserve is measured as "how long it would hold a strut with no stone under it" (ch 26).
     - Under the cart's lean his own came to "Two turns of the glass of that, and a bit, and then I'm at my floor" (ch 31).
     - Two struts are "twice the price" (ch 31).
   - A turn and a bit of his own therefore buys about one turn of one strut under a lean, or about half a turn under two. He still ends "a hair over" his floor (`chapter-39.md:115`) and then sets two more struts.
   - His stone *before* the fourteenth three is plausible. By the M4 rate ("Ninety breaths of wheel for a half"), 1½ Handfuls covers roughly twenty strut-turns, which is about what the husk and the roof used.
d. **Callie's door is unpriced, not contradicted.**
   - She carries 2 Handfuls (`chapter-37.md:229`). At the M3 still-door rate the M4 checkpoint records ("a Handful in six or seven glass turns"), that is 12–14 turns of a *plain* door. A door and a bit, with a husk and two heaps against it, costs more.
   - She holds more than twenty turns (`chapter-40.md:161`). The page never shows her stone running out, or what her own reserve costs afterwards. The wash in M4 did show it: cold hands, ringing ears.
   - The blood on her lip (`chapter-38.md:347`) and "I've got two turns. I've not got three" (`:523`) are the right signals. They need one line fixing when the stone went.
e. **The frame counts are wrong twice.**
   - `chapter-38.md:11`: "Four full jars and two empties and a broken socket". On D+48 the frame holds **three** full (jars 3, 4, 5) and **three** empties (jar 1, A, C). Jar 2 is open in Dee's arm.
   - `chapter-38.md:371` ("two full jars… and two empties") should be three and three. She opens "the third" from those three full jars, which leaves "Two whole" (`:387`).
   - `chapter-39.md:181` (five empties) is correct.
f. **Vent-jar capacity is unstated.** The first vent jar is "full. Near enough" after four catches (`chapter-38.md:233`). The other two then take about fifteen. Smaller late pushes make that possible, but the page never says so. This is minor.

**Settled stones on D+47 are plausible.**
- Toren: full (`chapter-33.md:129`) → "less than half" after the long husk hold (`chapter-36.md:133`) → gone at the door → his own at "a turn. And a bit" (`:265`).
- Callie: 1 → ¼ (`chapter-36.md:275`), covering the hook hold, the lee test (¼, `chapter-35.md:173`), the corridor hold and the stair top.
- Dee: 1 → ½.

---

## 5. Body state

**Consistent:**
- **Toren's forearm** is kept in its cuff and never used as a lever. He does everything one-handed (`chapter-33.md:509`; `chapter-34.md:229`; `chapter-36.md:79–93`; `chapter-39.md:201`).
- **Jab's palm:** the white place fixes (`chapter-35.md:399–409`). He draws "round it" (`chapter-36.md:287`; `chapter-38.md:41`). It is red with a blister by D+49 (`chapter-40.md:199`). His floor is never breached.
- **Rook:**
  - The infection declares on D+47 as M4 predicted ("Tomorrow we'll know").
  - Papers 4 → 1: `chapter-33.md:53`, `chapter-37.md:293`, `chapter-40.md:219`.
  - He stays "off". The poles are "furniture" (`chapter-39.md:377`), dragged on his knees without lighting anything.
- **Pell:** toes checked, strip loosened (`chapter-33.md:99–101`). He stays on the cart and directs.
- **Dee:**
  - Water skin empty (`chapter-33.md:65`).
  - At her floor once (`chapter-39.md:131`), sick from the room (`chapter-40.md:115`), a finger over her floor on D+49 (`:209`).
- **Duchess:** sound, never taken across the river.
- **Callie after D+48:** ribs strapped, walks with the hook, holds the counter one-handed (`chapter-40.md:7, 193, 341`).

**Needs a touch:**
- **Callie's bruised ribs on D+47.** The M4 checkpoint gives them "a week" and a twinge at the lip. On D+47 she pulls the lead sledge up the Z with the rope over her shoulder (`chapter-34.md:55`), and hauls on the steel door with her whole weight on the hook (`:247`). Neither draws a word. One twinge would carry the plant into the D+48 crack ("the side she had walked into it on the forty-fourth", `chapter-39.md:97`).
- **Callie's injured belay** (§3, item 6).
- **Toren's own reserve** (§4 c).

---

## 6. Numerical formula alignment (informed, not blind)

### Method

- **Definitions:** Movement Three's `metrics.py` definitions are reused verbatim (Appendix A of `MOVEMENT-003-EDITORIAL-REVIEW.md`, abridged in Appendix A below), with the same tokenizer, the same `syl` estimator and the `syl2` check.
- **Rates:** per 10,000 words of whitespace `wc`.
- **Narration subset:** paragraphs that do not open with a quote mark.
- **Sections:** `---` markers plus chapters.
- **Development beats:** counted **by hand**. The regex proxy is **UNMEASURED**.
- **Viewpoint shares:** chapter-heading viewpoints, not name frequency. Every chapter has a single viewpoint.
- **A lexicon artefact, new in M5:**
  - The `teach` lexicon counts `floors?`. Movement Five takes place on a concrete floor. 180 "floor(s)" hits make up most of `teach`.
  - A context regex (possessive or "at/under/over the" + floor; "Floor's a finger") finds about 38 in the reserve sense. This is approximate.
  - I report the raw figure and the adjusted one.

### Results

| Metric | Target | Observed (M5) | Note |
|---|---|---|---|
| Sentence mean / median / SD | 14.6 / 11 / ~26 | **9.0 / 6 / 7.9** (5,148 sentences) | **Narration only: 11.7 / 9 / 9.0** (2,838) |
| Share ≤5 words / ≥40 words | 27.7% / 3.3% | 45.5% / 0.4% | **Narration: 32.1% / 0.7%.** Short beats are slightly above target in narration; long sentences are nearly absent |
| Dialogue | — | 20.4% of words in quotes; 27.8% in dialogue-led paragraphs | About the same as M4 (19.7 / 26.8) |
| Paragraph mean / median | 26.8 / 18 (ASR pauses) | 26.1 / 14 (1,765 paragraphs) | Typography is not pause segmentation |
| Section length | ~950 words; ~8.7 breaks per 10k | **405 words; 22.9 markers per 10k** (106) | M4 (repaired) 478. Shorter again; ch 39 is 311 |
| Flesch Reading Ease / FK grade | 72.3 / 6.8 | **100.6 / 1.4** (`syl2`: 100.7 / 1.4) | Chapters range 98.5–101.8 |
| Progression core+teach | ~58 per 10k | **Raw 75.6** (core 27.7, teach 47.8). **About 45** with only reserve-sense floors | Raw by movement: M1 25.7, M2 55.1, M3 64.9, M4 49.6, M5 75.6. The M5 rise is mostly concrete floors. +m3 lexicon: 108.9 |
| Front-loading | First third ≈1.7× later thirds | **Provisional: inverted, ≈0.60×** | Equal-word thirds of chs 1–40 (268,994 words): 38.5 / 67.0 / 61.1. Coverage is about 90% of the owner's ~300k, and the floor artefact inflates the final third |
| Lead development beats | 4.5 per 10k, spread evenly | **About 33 by hand, 7.1 per 10k across three co-leads** (Callie ≈12, Jab ≈11, Toren ≈10), about one every 1,400 words | Every chapter has beats for its own viewpoint lead (examples below) |
| Supporting-cast beats | 8–10 characters, small beats each | **3 on the page:** Pell, Rook and Dee. Tonk, Callie's mother and Senna appear in memory | The expedition structure limits it, as in M4 |
| Viewpoint share | Lead ~87% (formula); M5 plan "true three-way rotation" | **Callie 36.9, Toren 35.4, Jab 27.7** | A plan deviation, flagged by the author. Cumulative (verified): C 34.5, T 33.4, J 32.0 |
| "that" | 92.1 (tighten below) | 66.7 | Below the source rate |
| "-ly" suffix | ~161 (optional) | 21.2 | A suffix count, not an adverb count |
| Reporting verbs | ~41 | "said" 174.3; wider set 195.7 | A register choice that suits reading aloud |
| Combat vocabulary | ~22 | **50.4** (ch 38 97.9, ch 35 79.2) | The movement's action promise shows in the numbers |
| Fillers | 5–25 band | just 1.5, almost 0, felt 15.2, seemed 0 | Below or inside the band. "felt" is concentrated in Jab's sensing chapters (35: 41.9; 38: 37.9) |
| Repeated phrases | 2–4 per 10k background | "the way (you\|a\|somebody\|he\|she)" 64 (**13.9**, level with repaired M4's 14.0); every "the way" 139 (30.1); "flat" 79 (17.1); "hand's width" 19 (4.1); "the colour of" 16 (3.5); "did not know" 14 (3.0); "bottom of a pond" 8; "Nobody said anything" 7; "He heard his own voice / himself" 7; "at the rate it came" 6 | "The way…" holds at M4's repaired level. "flat" is the next habit a listener will hear |

**Hand-counted beats, examples:**
- **Toren:**
  - "Twelve… We come out at twenty-eight whatever we've got" (33).
  - Holding the door, then letting go "three breaths after" (36).
  - Realising *everybody back* may mean leaving the thing everyone needs (36).
  - "It'll be mine" (37).
  - "We cross it… It's mine. Write it" (38).
  - "Two. Not three. The third's open" (39).
  - "Nobody carries a wheel through a drift at their floor" (40).
- **Callie:**
  - "Then we'll count doors" (33).
  - "It's never been the floor. The rope's fast" (35).
  - "And if somebody shut the river?" (37).
  - "Tomorrow the lee was not for anybody" (37).
  - Looking once and turning back (38).
  - "I can lift" (39).
  - "choosing what to hold" (40).
- **Jab:**
  - "It vents where it wants a thing" (35).
  - "It's got no floor… I'd not have stopped either" (35).
  - "On the push" (37).
  - "Pick the one" (38).
  - "He did not come off late again" (38).
  - "The difference between him and it was one word, and Dee" (38).
  - Staying on the open vent past *off* (38).

### Departures

None of these is an automatic repair.

1. **Sentence rhythm.** Narration's short-beat share (32.1%) is near target. The whole-text miss comes from dialogue. The narration mean (11.7) is short of 14.6, and the SD target of ~26 still cannot be reached in punctuated prose. This is the standing owner conflict.
2. **Reading ease** is 100.6: monosyllabic fight prose at 1.14 syllables per word. This is the standing voice-versus-formula conflict.
3. **Front-loading is inverted.** On equal-word thirds (first reported this way now that coverage is about 90%) the ratio is about 0.60. This is not comparable to M4's half-book figure of 0.76. It is the planned consequence of the ash ladder sitting in M2–M3, and cannot be fixed by an M5 repair.
4. **Viewpoint** falls about 5.6 points short of a third for Jab in M5. The cumulative share is within 2.5 points of even. I recommend no padding inside M5 (§8).
5. **Section length** is about 2.3× short of the proxy. It is low priority, because typography is weak evidence against ASR pauses.
6. **Length** is 46,193 words, inside the packet's 42–48k and under the map's 48–55k allowance. No decision needed.

No formula finding takes a repair slot. The three priorities below are ledger, staging and tally repairs.

---

## 7. Repair brief: three priorities, for the same author

This is a bounded, same-author repair. The developed action the owner requested stays: no catch, adaptation or kill is cut. Punctuation and small restaging are preferred over shortening.

### Priority 1: price the D+48 fight by the book's own rates

- **Location:**
  - `chapter-38.md:363–389` (jar 2 runs dry "at the tenth");
  - `chapter-38.md:429–449` (the lifter moves "at the fourteenth three"; Toren has "a turn of mine. And a bit");
  - `chapter-38.md:559`; `chapter-39.md:9, 115`;
  - `chapter-40.md:75` and `chapter-39.md:409` ("for two turns" / "Under the line: 2 turns");
  - optionally `chapter-38.md:345` or `:523` (Callie's stone).
- **Observed issue:**
  - The per-catch cost rises more than tenfold as the pushes shrink: ¾ for ten catches, then 8 for about eight (§4 a).
  - Toren runs two struts under a lean for about five or six turns on about one turn of his own reserve (§4 c).
  - "Two turns" under the line is stated as elapsed time when it was the allowance (§4 b).
  - This is the same class of problem as M4's first priority (the wash's long holds). It is recurring.
- **Effect on the reader:** a reader who has learned the ledger since M2 stops trusting the numbers exactly where the book asks them to feel the cost: Toren's floor, the line and the crossing.
- **Proposed scope:** numbers and a few sentences in chs 38–40, then the M5 continuity checkpoint. For example:
  - (i) Move jar 2's "Jar" to about the second or third catch. The quiet "last one above the line" beat (`:363–389`) moves with it unchanged. Jar 3 then carries about sixteen catches at about ½ each, and jar 4's 3 pays for the long final open push.
  - (ii) Re-time the lifter's move to about the seventeenth three, **and** have Toren let the husk strut go when he sets the strut under the lean (the husk is "the size of a boy" by then, `:401`). One strut under a shrinking lean for two or three turns fits "a turn and a bit". Alternatively, give him "two turns" of his own after the D+47 night's sleep. The page never measured it on D+48.
  - (iii) Change "for two turns" to "inside two turns".
  - (iv) One line saying when Callie's stone went and what her own reserve cost. Dee's "My stone went at the tenth" can stay.
- **Strength to preserve:**
  - The catch-by-catch rhythm.
  - "Off before the ten" and the late seventh catch.
  - The two adaptations ("It learned").
  - Toren's crossing speech and Dee's "It's my line".
  - Jab staying on the open vent.

### Priority 2: fix the stagings a reader can't follow

- **Location:**
  - `chapter-37.md:389–391` (the contradicting sentences);
  - `chapter-34.md:247` and `chapter-36.md:25` (the door heap);
  - `chapter-34.md:21` ("on her right" → left);
  - `chapter-34.md:183, 271` (stair directions);
  - `chapter-39.md:89–99` (the order of Callie's fall);
  - `chapter-39.md:305–307` (Callie belaying with cracked ribs).
- **Observed issue:** the six items in §3 (1–6). Two of them sit at the movement's highest-stakes moments: the fight's first beat, and the injury that ends Callie's hold.
- **Effect on the reader:** a reader who stops to rebuild the geometry misses the beat. The belay also undercuts both Pell's rope rule and the new injury in the same paragraph.
- **Proposed scope:** sentence-level. Delete "Toren went in over the threshold" and open with the corridor cut. Give the corridor heap its planted source: twenty years under the gap. Change one word for the pipes. Add one sentence naming the flight directions. Reorder three sentences in the fall. Put the back rope through the top ring or round the rail post, with Callie calling it.
- **Strength to preserve:**
  - The gate/door push–pull plant and payoff.
  - The lean-to "the wrong way up".
  - "Pull the door" as a grace.
  - The ramp-and-ring logistics.
  - Nobody lifting a box in their arms.

### Priority 3: make the tallies, clocks and calls agree

- **Location:**
  - `chapter-38.md:11, 371` (frame counts: three full and three empties, not four and two, then two and two);
  - `chapter-36.md:297–307` with `chapter-34.md:137` and `chapter-36.md:213` (the sky count);
  - `chapter-33.md:373` and `chapter-36.md:301` ("sun on the gate");
  - `chapter-40.md:343` ("two days ago" → three);
  - `chapter-40.md:297` ("two days of Sowerby");
  - kneeling: `chapter-35.md:215`, `chapter-36.md:167`, `chapter-38.md:255, 313, 463`;
  - read-aloud: `chapter-38.md:185–197, 217`; `chapter-40.md:269–271`; `chapter-36.md:323`; "on its sides" at `chapter-34.md:409` and `chapter-39.md:253`.
- **Observed issue:**
  - Pell reports 7 falls in "four hours" and says "Then she saw what I saw". Callie counted 1 and then 2 in twelve counts. At a count to a turn, her rate predicts about 20–40 falls in four hours. And four hours inside does not fit the day's two halts and 3¼ at forty turns.
  - This count is the one thing the Director asked for ("count what comes out of it and write it down"). It should agree with itself.
  - The rest are small slips listed in §3 (8–11) and §4 (e).
- **Effect on the reader:** each slip is small, but together they wear down the trust the count ritual has built since ch 25.
- **Proposed scope:** local edits only.
  - Make Pell's time and fall numbers match Callie's rate, or have him say he missed some ("I'd look down to mark it").
  - Pick one sun marker.
  - Change the knee breaches to "crouched", or have Dee see one.
  - Label the catches so that "three" means only the push (e.g., Dee says "That's three in the jar").
  - Give 40:269 to its intended speaker.
- **Strength to preserve:** Pell's heartbeat method ("sixty to a turn if you sit still"), Callie's refusal to claim a trend from two counts (`chapter-36.md:219`), and the nightly *Out/In* lines.

---

## 8. Owner-only decisions (not for the author repair)

1. **Toren's Guard strut held while his Edge is lit** (`chapter-38.md:207–211`; `chapter-39.md:3–25`).
   - The non-negotiable one-configuration limit conflicts with the Guard paragraph's allowance for a blending practitioner "once Guard is known and trained". The plant-before-climax rule applies too.
   - If permitted, the author should plant a brief, priced demonstration before ch 38. The D+47 husk hold (`chapter-35.md:179–183`) or the steel-door hold (`chapter-36.md:111–121`) would carry it.
   - If forbidden, the cut at `:211` and the point at `chapter-39.md:25` need restaging: Toren releases, then lights. The kill's order can survive that.
2. **The D+48 return under the Director's narrow permission.**
   - D+47 is plainly "If it comes to you" (`chapter-36.md:335–339`).
   - D+48 is a planned return to kill the creature where it lies, in the approved room, short of the third door. The checkpoint treats this as permitted.
   - Does the owner read "You are not going looking for whatever's under it" the same way?
3. **Crossing the signed abort line on purpose** (`chapter-38.md:503–513`).
   - The signed rule "Two Flasks left inside: everybody out" (`chapter-33.md:347`) is broken deliberately, with the watch co-signing.
   - The book frames it as a paid choice, and Movement Six will set it before the Director. Is that precedent intended?
4. **Viewpoint allocation.**
   - M5 is Callie 36.9 / Toren 35.4 / Jab 27.7 against the map's "true three-way rotation". The cumulative split is even within 2.5 points.
   - Options: accept, or have M6 lean Jab. I do not recommend padding M5.
5. **Plan adherence to confirm:**
   - (a) "Ward-at-scale" (map) versus a door and a bit (page; §2, tension 2).
   - (b) Is the map's "proof the rip is changing" satisfied by "lost its count" with falls continuing (`chapter-39.md:341–349`; `chapter-40.md:137–149`)? And is that the intended setup for M6's Sag surge "caused by the distant rip's collapse"?
   - (c) Do two wheel boxes, against the Director's "Two, three if you can", count as "the machine part" for M6?
6. **Names and grades on the page.** "The lifter" is the creature's name; the bible leaves the final name as a drafting decision. Rook grades it a Flask; the Yield ladder is still `POSSIBLE`. Should both be confirmed as canon?
7. **The standing formula conflicts:** Flesch ~100 against 72.3; the sentence SD; section length at about 2× the proxy; inverted front-loading; three co-leads against the formula's single ~87% lead. These are unchanged from M2–M4. I recommend no repair without an owner ruling.
8. **"Adults may not steal the solution" and Pell's pump.** My reading is that it passes: Callie asks the decisive question and the three build the plan. The line "It'd pump itself dry" (`chapter-37.md:65`) is close, though. The owner may judge it differently.

---

## 9. Uncertainty and limits

- **Same model:**
  - This review was written by the model that drafted the movement, with drafting-summary titles visible at session start.
  - It may share blind spots with the author, especially on prose habits and on how clear a staging is.
  - A human or an independent model should check §3 and the §1 scores.
- **The scores are judgement.** The two reader lenses are lenses, not demographic evidence, and no sales inference is intended.
- **The page's clock is inferred.**
  - "A count ≈ a glass turn" rests on `chapter-40.md:161` ("twenty turns and more" for about twenty threes) and the fight's structure. The M5 page never states the equivalence outright.
  - If the owner intends a different ratio, the size of §4 c changes, but its direction does not.
- **Rates carried from earlier movements** (the still-door rate; Toren's own reserve as glass-time; two struts at twice the price) come from the M4 continuity checkpoint's summary of chs 26–31. I did not re-read those chapters.
- **Some metrics are approximate:**
  - The reserve-sense "floor" count uses a context regex and is approximate.
  - The syllable estimators undercount by about 3.5% (M3's validation). Proper names and system terms affect Flesch.
  - Front-loading is provisional until the book is finished.
  - The beat counts are one reader's selection.
- **Not checked:** chapters outside 33–40 were not re-read, except for targeted `grep`s: the "be asleep" plant (chs 5, 22, 24, 32), Dee's crooked wrist (ch 9), "eighteen days" (chs 2, 11), the Edge+strut search (chs 18–37), and name use. Canon beyond the supplied evidence is **unverifiable here**.

---

## Appendix A: how the metrics were run

- The script ran from the book directory as `python3 - <<'EOF' … EOF`, with no file written.
- It uses Movement Three's `metrics.py` logic (`MOVEMENT-003-EDITORIAL-REVIEW.md`, Appendix A), including `syl2`.
- Below is an abridged version of the definitions that affect results:

```python
import re, statistics
def chapters(a,b): return [f'manuscript/chapter-{i:02d}.md' for i in range(a,b+1)]
ABBR = re.compile(r'\b(Mr|Mrs|Ms|Dr|St)\.\s')
INIT = re.compile(r'\b([A-Z])\.\s(?=[A-Z0-9(])')
def clean(t): return [l.strip() for l in t.split('\n') if l.strip() and l.strip()!='---' and not l.strip().startswith('#')]
def words(s): return re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)*", s)
def sentences(p):
    p=ABBR.sub(lambda m:m.group(1)+'<DOT> ',p); p=INIT.sub(lambda m:m.group(1)+'<DOT> ',p); p=p.replace('*','')
    parts=re.split(r'(?<=[.!?])["”’)\]]*\s+(?=["“(]?[A-Z0-9])',p)
    return [s.replace('<DOT>','.').strip() for s in parts if words(s)]
# syl / syl2 exactly as in M3 Appendix A.
# FRE = 206.835 - 1.015*(W/S) - 84.6*(Syl/W); FKGL = 0.39*(W/S) + 11.8*(Syl/W) - 15.59
# Lexicons (count / wc * 1e4):
#  core   (case-sens) \b(Ward|Sustain|Stride|Guard|Edge|Ember|Handfuls?|Flasks?|Barrel|Kindl\w*|struts?)\b
#  teach  (re.I)      \b(floors?|settle[ds]?|settling|ash|bucket|reserve|measured?|measuring)\b
#  m3     (case-sens) \b(vent(?:s|ed|ing)?|recall(?:s|ed)?|rotation|working depth|draw(?:s|ing|n)?|lodg(?:e|ed|ing)|counter|ticks?)\b
#  report (re.I)      \b(said|says|say|asked|told|answered|called|shouted|whispered|replied|agreed)\b
#  combat (re.I)      \b(husks?|hounds?|blades?|knife|spike|cut|cuts|struck|hit|hits|strike|fight|fought)\b
#  that \b[Tt]hat\b   ly \b[A-Za-z]+ly\b   said \bsaid\b   fillers (re.I) just|almost|felt|seemed
# Narration subset: paragraphs not starting with a quote mark. Sections: count of ^---$ lines + chapters.
# Reserve-sense floors (approximate, M5 addition):
#  (my|your|her|his|their|own|a|at the|under the|below his|below the|over the|over her|over his)\s+floors?\b(?!\s+of) | Floor's | floor's a finger   (re.I)
# Thirds: whitespace tokens of chs 1–40 concatenated, split into three equal-count segments.
# Viewpoint: word count by the viewpoint name in each '# Chapter N — POV: Title' heading.
# Quoted words: words inside "…" on one line; dialogue-led paragraphs: paragraphs opening with '"'.
```

Checks and commands:
- Word counts: `wc -w manuscript/chapter-3[3-9].md manuscript/chapter-40.md` (46,193, matching the checkpoint).
- Edition identity: `shasum -a 256 manuscript/chapter-NN.md editions/movement-005-first-draft/chapter-NN.md` for NN = 33…40 (all eight match).
