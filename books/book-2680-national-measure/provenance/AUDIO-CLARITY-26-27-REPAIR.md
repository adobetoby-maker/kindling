# Audio-clarity repair — chapters 26–27 (accepted text)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime) |
| Session | `https://claude.ai/code/session_01VbEPh12MLwfRwnbhdM92E6` (background job `c8ca0232`) |
| Date | 2026-10-15, about 10:53–11:05 MDT |
| Brief | `planning/OPUS-AUDIO-CLARITY-26-27.prompt.md` |
| Findings answered | `narration/monroe-1.2.5/calder/chapters-25-27/chapter-26/writing-monroe-feedback.md`; `…/chapter-27/writing-monroe-feedback.md` (unit file: chapter 25 has no blocker) |
| Repository state at start | HEAD `90904e0`; `manuscript/chapter-26.md` and `chapter-27.md` identical to HEAD (checked with `git diff --quiet`) and to the accepted hashes in `provenance/WHOLE-BOOK-RECHECK-CONFIRMATION.md` |
| Files edited | `manuscript/chapter-26.md`, `manuscript/chapter-27.md`, this report. Frozen copies added under `editions/audio-clarity-26-27-pre-repair/` |
| Not touched | Every other chapter, maps, ledger, continuity files, the acceptance table, prompts, narration artifacts, scripts, git state. No commit, push, publish, render, Skill, Agent, Workflow or other model. |

**Scope of claim.** This is a text repair, not an audio repair. Nobody has listened to it. It has not been
re-narrated, re-rendered, word-locked again or validated by the narration scripts.

## 1. Read before deciding

- The O'Connor seat, version 1.3.0: `PIPELINE.md`, `VOICE.md` and `FORMULA.md` in
  `/Users/drive/penname/pennamecodexv3/pen-names/oconnor/`.
- The current whole-book acceptance, `provenance/WHOLE-BOOK-RECHECK-CONFIRMATION.md`. Chapter 26 (5,106
  words) changed in the whole-book repair; chapter 27 (7,270 words) did not.
- All of chapters 25, 26 and 27.
- Carry and Ropewalk canon: `UNIVERSE_BIBLE.md` §2–3 (the lay); `CHARACTERS.md` (Carrow is the
  "captain and laid blade"); the Tue 15th rows in `STATE_LEDGER.md` and in
  `provenance/MOVEMENT-004-CONTINUITY.md`; the M4 repair of 27:377 (P2.2) in `MOVEMENT-004-REPAIR.md`
  and `MOVEMENT-004-RECHECK.md`; and ch. 18:35 and 18:135, where the Ropewalk first four is introduced.
- Both feedback files.
- The same lines in `editions/movement-004-first-draft/` and `editions/whole-book-pre-repair/`. Both
  defects are first-draft text. They survived the movement and whole-book reviews and did not come from a
  later edit.

## 2. Freeze (before any edit)

`editions/audio-clarity-26-27-pre-repair/` did not exist. I created it and copied the two files with
`cp -n` (no overwrite). The copies are read-only (444), with a `SHA256SUMS.txt`, and verified `OK` after
the repair.

| File | Frozen (= accepted = HEAD `90904e0`) | After repair | Words (`wc -w` = `split()`) |
|---|---|---|---|
| `chapter-26.md` | `e51f0c51773bb1447c3cd4ab7201dd1e727fd600ed0ff593697e21830f327da7` | `eec3e97dc3697ef2c67e4741033095a1345b88e848ccf1c3c037a237ce6cc46e` | 5,106 → 5,106 (0) |
| `chapter-27.md` | `047cbc477953f9ad483c242c830dd6ea8e2ec49af000327fe6cbcf6abc6fdb79` | `5629a4a8bb5bf2e9f9769f92d942be639228cdeff00e994c2e9e845d441b0a1f` | 7,270 → 7,280 (+10) |

## 3. Changes (exact)

| # | Ch:line (para) | Before | After | Kind |
|---|---|---|---|---|
| 1 | 26:15 (¶7) | "After **eleven** fours have shown us how, and before eleven who'll have seen us." | "After **twelve** fours have shown us how, and before eleven who'll have seen us." | One number word |
| 2 | 27:383 (¶189) | "She lifted the head again and held it, and Tolver said *up,* and **Treen and their blade** hauled from the top," | "She lifted the head again and held it **till Lyle had it, and went up the ladder after Treen,** and Tolver said *up,* and **Carrow and Treen** hauled from the top," | Meaning change: one movement supplied, recorded as an explicit manuscript revision |

Nothing else in either paragraph changed. The rest of 27:383 ("…steady and fast, with Tolver laid at the
bottom keeping him off the stone. It was beautiful. It was the fastest thing anybody had done all
morning.") is exact. No quotation marks were added or removed. The italic *up,* is kept.

## 4. Finding 1 — 26:15, the thirteenth run "after eleven fours" — **real; repaired (change 1)**

- **Arithmetic.** Twenty-four fours run (26:243; 27:395, "Twenty-four fours run"). The order is reverse
  seeding (notice, 26:13; the Clerk, 26:259). Seven is the twelfth seed, so it runs 24 − 12 + 1 = 13th. That
  puts **twelve** runs before Seven and **eleven** after it.
- **The prose agrees with twelve and eleven everywhere else.** "The eleventh run went. The twelfth was a
  Tarn four" (26:299), and then "*Team Seven*" (26:303). "There were eleven fours still to run" (27:249).
  "Eleven," says Anwen (27:253). "The fourteenth run went" (27:265). Halden goes "second to last", the 23rd
  (27:339). The Ropewalk goes last, after "twenty-three fours before them" (27:371). Continuity
  (MOVEMENT-004-CONTINUITY, Tue 15th) also says "Reverse seeding; Seven runs thirteenth."
- **Why this word.** "Eleven" is the only number that disagrees, and punctuation cannot fix it, as the
  feedback says. Changing the first "eleven" to "twelve" makes 12 + 1 + 11 = 24. "Thirteenth" and the
  second "eleven" stay. Perrin's balanced "after … and before …" line and its rhythm are unchanged. This is
  the feedback's proposal exactly.

## 5. Finding 2 — 27:383, "Treen and their blade" haul from the top — **real; repaired (change 2)**

### Positions at the haul, from the prose

| Person | Declared (27:359) | Where they are at the moment of "up" (before repair) |
|---|---|---|
| **Carrow** | edge and stance, laid. She is the Ropewalk's blade (CHARACTERS.md: "laid blade"), so "their blade" means Carrow | At the foot of the ladder, holding the head (27:369, 377, 383) |
| **Lyle** | ward and stance, laid | At the foot, with the Purser against the wall (27:369) |
| **Tolver** | stance | At the foot. He ties the rope (27:369, 373), then is "laid at the bottom keeping him off the stone" (27:383) |
| **Treen** | ward (the catcher, 18:35) | At the top. She went up alone with the rope (27:363) |

So the only person at the top is Treen, and "their blade" is at the bottom with the head in her hands. A
listener cannot place a second hauler without imagining a movement that is not written, or a fifth
teammate. The defect is real.

### Why not "Treen hauls alone" (the feedback's first option)

That would delete three words, but it breaks the book's own physical constraints:

- Treen is "a small dark girl" whose catcher's ward "would not have stopped a child" (18:35, 18:135). The
  Purser is eighty-five kilos of wet sand, "and the water made him heavier" (27:37). The book counts this
  weight carefully ("Twenty-two times your arms take eighty-five kilos", 26:63).
- The Ropewalk's own second four, on the same ladder, used two haulers: "Their catcher went up the north
  ladder … and their blade went up after her. At the top the two of them hauled" (26:287). One small catcher
  hauling alone, "steady and fast", with "the fastest thing anybody had done all morning", would beat a
  two-person haul.
- The next sentence, "They ran him to the mark" (27:385), needs more than one person at the top. Treen alone
  would also have to carry 85 kg twenty paces.
- The sentence as drafted names two haulers. The author meant two at the top and simply did not send the
  second one up. Perrin's forecast ("They'll put a girl up it with the rope, and haul him from the top",
  26:27) has a plural subject. It fits both readings, so it does not decide the question.

### What the repair does

Change 2 sends the Ropewalk's blade up the ladder after their catcher, as their second four did, and makes
the handover of the head explicit before Tolver's "up" ("establish the transfer before up", feedback):

1. Carrow lifts the head again after the face (as before).
2. She holds it **till Lyle had it**. Lyle is already at the foot, so nobody new is placed.
3. She **went up the ladder after Treen**.
4. Tolver says *up*.
5. **Carrow and Treen** haul from the top. I used names instead of "their blade", because "their blade" was
   the phrase a listener could not resolve. Tolver is still laid at the bottom keeping him off the stone.
6. "They ran him to the mark" now has two people at the top.

**Power constraints.** Carrow "had shut both doors" because "a laid girl cannot walk" (27:377, the M4 P2.2
repair). She is therefore free to climb with nothing open, and the repair needs no new door use. It also
gives the M4 line its purpose: she unlaid so that she could move. Lyle only has to hold a head while
standing still. The book allows lifting while laid (26:287; M4 recheck), so no door claim is needed for her
either. Nothing is lit on the casualty. One rope and the Board's sling are kept (26:13).

**Preserved exactly.** The face penalty and its cause (Carrow holding with nothing open, chin down, "*Face*",
27:377–379). The fast raw time "*Two minutes and fifty-nine seconds … Ten for the face. Three minutes and
nine*" (27:387). The Clerk's order (27:395) and Seven first by one second (27:417). Treen up alone at
"Twenty" (27:363–365). No fifth teammate and no new technique. The canon row (MOVEMENT-004-CONTINUITY: "2:59
raw, 'Face,' 3:09") does not say who hauls, so the repair contradicts no record.

**Time budget.** Treen is up by about 0:20, and the face comes after the sluices go full at one minute. A
quick unlaid climb of twenty-two rungs fits easily inside the 2:59 raw time. The prose gives no moment-by-
moment clock for the Ropewalk, so nothing stated is contradicted.

## 6. Changed paragraphs and both joins

| Changed paragraph | Previous paragraph | Next paragraph | Check |
|---|---|---|---|
| 26:15 | 26:13, the Carry notice ("…Reverse order of seeding.") | 26:17, "Is that good?" | 12 before, 13th, 11 after = 24. Agrees with 26:299–303 and 27:249–265, 339, 355, 371, 395 |
| 27:383 | 27:381, "It was flat. It was the only flat thing in the whole roar." (and 27:377, Carrow unlaid, "*Face*") | 27:385, "They ran him to the mark." | Carrow lifts, hands to Lyle, climbs; Tolver's "up"; two haulers; "They" at the top is now two people; 2:59 + 10 = 3:09 unchanged |

The whole-book repair WB-09 at 26:63 ("And Wednesday's the Longshore. If they go on Tuesday, you don't plant
on Wednesday.") is present and unchanged. No other accepted repair is in either changed paragraph (the M4
P2.2 sentence at 27:377 is untouched). No owner-protected wording is involved.

## 7. Noted, not repaired (outside the two findings)

- **"Laid" used of Tolver.** Tolver is declared "stance" only (18:41, 27:359, 35:107). The bible defines a lay
  as two doors opened together and twisted to agree (UNIVERSE_BIBLE §3). Yet the prose calls him laid at
  26:27 ("Tolver can hold anything you like laid at the bottom"), 27:363 ("with his stance, laid") and in the
  unchanged tail of 27:383. All three are first-draft text. Writing Monroe did not flag them. Changing only
  27:383 would make it disagree with 27:363 and 26:27. A listener hears "laid" as "planted", so this is not a
  narration blocker. It is a terminology question for the fresh recheck or the owner.

## 8. Remaining blockers and next steps (not done here, by brief)

- **Acceptance table.** `provenance/WHOLE-BOOK-RECHECK-CONFIRMATION.md` still lists the pre-repair hashes for
  chapters 26 (`e51f0c51…`) and 27 (`047cbc47…`). **It needs a later explicit addendum recording the new
  hashes, after a fresh-context recheck** of these two changes and their joins. I did not edit the table.
- **Fresh recheck owed.** It should confirm or reject both changes, especially change 2, which adds a movement
  (Carrow's climb, Lyle taking the head).
- **Narration.** The unit's feedback files, `clarity-review.jsonl`, performance files and narration markdown
  in `narration/monroe-1.2.5/calder/chapters-25-27/` reference the old source hashes. They need refreshing and
  validating against the new text before chapters 26–27 render. I touched none of them.
- **Maps and ledger.** No change is needed. Canon does not record who hauled for the Ropewalk.
- No other real blocker was found in chapters 25–27.
