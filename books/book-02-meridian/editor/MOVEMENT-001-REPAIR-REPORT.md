# Movement One — consolidated same-author repair report

- Prompt executed: `editor/MOVEMENT-001-REPAIR.prompt.md`
- Model that actually ran the repair: **Claude Opus 5.5 (`claude-opus-5-5`)**, writing as Monroe Jackson (Monroe 1.3.0 / O'Connor seat). This was one session and no other model wrote prose. The model ran in Claude Code (Agent SDK harness), and no subagents were used.
- Date: 2026-09-27
- Scope: surgical line-level edits inside the existing scenes of `manuscript/chapter-01.md` through `chapter-08.md`. No scene, character, fight, briefing or later-book teaching was added, and no successful scene was cut.
- Not touched: the frozen first draft (`editions/movement-001-first-draft/`), the reviews, source pool, book map, universe bible and name registry.
- No human cold read took place. The only reader evidence is the existing AI simulated cold read and the AI editorial review.

## Reading coverage (stated honestly)

- **Read in full:**
  - VOICE.md and FORMULA.md
  - the Movement One packet
  - the continuity checkpoint
  - NAME_REGISTRY.md
  - the cold read
  - editorial review §3.3–§5 (continuity, formula alignment and repair brief)
  - all eight manuscript chapters
- **Consulted by targeted search, not read end to end:**
  - the rest of the editorial review (methods appendices)
  - BOOK_MAP.md, UNIVERSE_BIBLE.md, and Book One ch. 53 and ch. 52. The search in ch. 52 was for the twelve-foot sibling cord.
- The governing rulings in the prompt settled the Jab/Verge-hound fence rule, the name Vera Kess and the machine's pre-Fall age. None of those three was changed.

## Priority 1 — continuity and object-state fixes, by chapter

**Chapter 1**
- Hallet's count now reads: eight persons in the pen; seven went out through the north yard gate; the eighth, Jab, came in off the road and "waits" because he is the first item.
- Wyck is strapped "from the collarbone down to the wrist".

**Chapter 2**
- The Meridian street is four hundred yards, which matches Hallet's line.
- Wyck's strapping reaches "collarbone to wrist" on his ward entrance.

**Chapter 3**
- Toren's memory of the south-gate window reads "three days ago", not two. The window was D-2 and this scene is D+1. The review did not list this slip; it turned up in the reread.

**Chapter 4**
- "Night before last" and the paces misattribution are replaced. Dessa now cites what the reader actually saw on D-0 night: Tonk counting the lamps out loud down the dip. Callie corrects the count to seven. Dessa's "you're all as bad as each other" is kept.
- Tilda on D+2 now has "eleven days before the fourteenth".
- The summons card is eleven days away, and Callie notices it falls on her mother's review day, D+13.

**Chapter 5**
- The long coat says the Sag walk was "three nights ago" (D+3 referring to D-0).
- The Rook step conversation moves from "an hour later" (mid-morning) to "the late afternoon, when the light had started to go". Its dusk landing is intact: the lamp comes on and Dessa calls "Forty minutes".
- The first appearance of the tether now names it the twelve-foot long cord from the road, "not the short neck cord the metal hung on" (Book One ch. 52).
- Wyck's strapping reaches collarbone to wrist, and his hand comes out of the strapping at the wrist.

**Chapter 6**
- An explicit rewind signpost opens the chapter: "Back on the second day, the afternoon of Tonk's operation".
- "Tuesdays" is attributed to Senna, "the night Rook told them he was staying".
- The flash-forward ("when Dessa asked him years afterward") is removed. Toren now knows only that he will never tell anyone.
- Wyck: collarbone, an arm strapped "all the way down to the wrist", and the last two fingers numb.
- Rook's Vera-stone step scene is now "after full dark", after Ch. 5's dusk scene ends. Twelve's door is dark "since Jab went back up to the long building", so the two same-day step scenes no longer collide.

**Chapter 7**
- The day holder stays at the south lip. She lets her hands drop and rests while Rook holds. After an hour, "the day holder, who had never left the south lip," takes the whole line back.
- "Thirty years" becomes "Thirty years old … and you turned your head like a boy". It now reads as his age, not as lifting experience.
- The knife returns into "the metal on its neck cord".

**Chapter 8**
- The tether's physical state is coherent all the way through:
  - Overnight, Tonk's end is knotted at his wrist and Jab's end is tied to the bed rail, as every night since D+2.
  - Jab arrives from hut twelve and moves the rail end to his own wrist.
  - On the rolling-bed trip the long cord runs wrist to wrist, while the metal lies in the tray "on its short neck cord".
  - At the yellow line Jab unties the cord from himself and gives Tonk the loose end.
  - At night he again ties his end to the rail when turned out.
- From twelve, eleven is "one door down".
- The unsupported "the way Callie said hers did" is removed.
- Two further clarity fixes:
  - Senna's appointment is "first light" (the cold read flagged "the first hour").
  - Jab's memory of the long coat's words matches the Ch. 5 rewording.

**Unchanged by design:** all other medical clocks, injuries, power limits and reserved disclosures. These include Senna D+10/D+21, Tonk D+16, the reviews on D+13/D+14, Rook's eleven days and the eight nights of the cord. The continuity checkpoint now records the D+3 ordering, the repair notes and the two-cord object state.

## Priority 2 — cadence (narration only; dialogue lines kept)

In each chapter, runs of three or more same-subject short declaratives were joined into single sentences with audible hierarchy at reflective, spatial and procedural turns. Examples:
- Toren's sum (ch. 3)
- the warm stone (ch. 6)
- Jab's countdown and the closing heap thought (ch. 8)
- the knocking corridor (ch. 4)
- the street at night (ch. 2)

Impact lines, child dialogue, comic timing, section breaks and emotional beats were kept short. Examples include "That's one.", "That's ten.", "She did not count." and "I'm Rook."

The script below is a rough re-run of the review's splitter logic (paragraph end = sentence end). It is not the Appendix A script verbatim, so it is directional only.

| Measure | First draft | Repaired |
|---|---|---|
| Words | 39,524 | 39,562 |
| Sentences | 4,763 | 4,626 |
| Mean sentence length | 8.30 | 8.55 |
| Narration-only mean (no quotation mark in the sentence) | 9.45 | 9.94 |
| Sentences ≥30 words | 57 | 80 |
| Sentences ≥40 words | 3 | 14 (max 44) |
| "did not" | 205 | 148 (−28%) |

The movement has moved in the formula's direction, but it is still far from the 14.6 mean and 3.3% ≥40-word share. That was deliberate: the prompt forbids forcing a numerical score, and the packet's one-hearing listening rule governs. No target was broadened or reported as met. This repair changes prose only. It does not train or alter any model's weights, and further gain would need another deliberate same-author pass.

## Priority 3 — adult registers

Hallet keeps the column idiom: "no column for it", "It's only a column", and his exact ordering, now with "he's the first thing, so he waits". Pell keeps one column line in ch. 4. Other borrowed column lines were re-voiced:
- Callie: "They've got a bin for it."
- Sowerby: "a line for it on this form".
- Otto relaying Pell: "that's never an accident".
- Wyck: "That's the bit I don't believe."
- The long coat: "a line on the register … very little written on it". Jab's memory in ch. 8 was updated to match.

"I'd like that understood/noted/minuted" now belongs to Senna, plus Hallet's single "noted … no column" line. It was removed or re-voiced for:
- Rook: "Let me be wet sitting down first"; "I'm putting it down now"; "A boy on a wall set it, and I keep it", which replaces his echo of Senna's "best rule".
- Dessa: "Put down *I can't really move*." and "Add that up."
- Tilda: "She wants it known…" and "Nobody says it for me again."
- Mrs Lask: "So who did?"
- Senna's own later repeats were thinned in ch. 6 and ch. 8. Her deliberate "Nobody runs in here. I'd like that understood." callback in ch. 8 was kept.

"Extremely rude" is now kept only for Senna (ch. 3) and Tilda's intentional "I've been practising" echo (ch. 4). Other uses changed:
- Keel is brisk and physical: "Perfectly ordinary. Runs about. Rude about my handwriting."; "Furious is the best sign in the world. Enjoy it."
- Wyck: "I was a pig about it."
- Rook: "a very good arrangement".

The "the way you say the road goes left / door is on the left / read out a weight" simile family is now down to its first use. Pronoun and object-noun anchors were added where a listener could lose the action: the long cord versus the neck cord, the day holder's position, and Rook versus Jab on the steps. No recap paragraphs were added.

## Files changed

- `manuscript/chapter-01.md` … `chapter-08.md`
- `provenance/MOVEMENT-001-CONTINUITY.md`: the D+3 ordering, the repair notes and the two-cord object state
- `AUTHORSHIP.md`: repair marked complete
- `editor/MOVEMENT-001-REPAIR-REPORT.md`: this file

## Post-repair check

The changed passages were reread in context, then checked by targeted search:
- no "night before last" in chs. 4–5
- no "thirteen days" and no "two hundred yards"
- "Tuesdays" is Senna's
- no flash-forward
- "Thirty years old"
- "One door down" in ch. 8
- no Callie knowledge attribution in ch. 8
- Wyck's wrist is present
- every tether mention in chs. 5–8 is the long cord or clearly Tonk's fist cord, and every metal mention is the neck cord

Movement Two was not started.
