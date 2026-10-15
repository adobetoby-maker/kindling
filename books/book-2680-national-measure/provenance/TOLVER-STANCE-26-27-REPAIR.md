# Terminology repair — Tolver called "laid" at the Carry (chapters 26–27)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime) |
| Session | `https://claude.ai/code/session_014gow3vgE5xVejBL67NJ9ar` (background job `6148611b`, forked from the session of job `c8ca0232`) |
| Date | 2026-10-15, about 11:57–12:05 MDT |
| Instruction | Owner: "Resolve only the residual Tolver stance terminology findings, retaining previous two repairs exactly. Freeze and report." |
| Finding answered | `provenance/AUDIO-CLARITY-26-27-REPAIR.md` §7 ("Laid" used of Tolver: 26:27, 27:363, 27:383) |
| State at start | HEAD `90904e0`. Chapters 26–27 = the post-repair text of `AUDIO-CLARITY-26-27-REPAIR.md` (hashes below), uncommitted |
| Files edited | `manuscript/chapter-26.md`, `manuscript/chapter-27.md`, this report. Frozen copies added under `editions/tolver-stance-26-27-pre-repair/` |
| Not touched | Every other chapter (including 41:323), the earlier report and its frozen edition, maps, ledger, continuity files, the acceptance table, narration artifacts, scripts, git state. No commit, push, publish, render, Skill, Agent, Workflow or other model. |

**Scope of claim.** This is a text repair only. It has not been listened to, re-narrated, rendered or
validated by the narration scripts.

## 1. Freeze (before any edit)

`editions/tolver-stance-26-27-pre-repair/` did not exist. I created it and copied the two working files with
`cp -n`. The copies are read-only (444), with a `SHA256SUMS.txt`, and verified `OK` after the edit. The frozen
text is the text of the first audio-clarity repair, so the chain is recoverable:
accepted → `editions/audio-clarity-26-27-pre-repair/` → this edition → current.

| File | Frozen (= after the first 26–27 repair) | After this repair | Words (`wc -w`) |
|---|---|---|---|
| `chapter-26.md` | `eec3e97dc3697ef2c67e4741033095a1345b88e848ccf1c3c037a237ce6cc46e` | `1ecc21951e2bd781d1e38843691b2564dc564ee0de0e1ab13b6d0707b444d6d3` | 5,106 → 5,106 (0) |
| `chapter-27.md` | `5629a4a8bb5bf2e9f9769f92d942be639228cdeff00e994c2e9e845d441b0a1f` | `e18bed0e5fa3cf86a3f197953c6b914ce7de0c53080f4cb81dd4945298a9af83` | 7,280 → 7,280 (0) |

Accepted text (`WHOLE-BOOK-RECHECK-CONFIRMATION.md`), for reference: ch. 26 `e51f0c51…`, ch. 27 `047cbc47…`.
`editions/audio-clarity-26-27-pre-repair/` still verifies `OK`.

## 2. Changes (exact)

There are three changes, each replacing one word ("laid" → "planted"). The punctuation is unchanged and no
sentence was recast.

| # | Ch:line (para) | Before | After |
|---|---|---|---|
| 1 | 26:27 (Perrin's forecast) | "…and Tolver can hold anything you like **laid** at the bottom." | "…and Tolver can hold anything you like **planted** at the bottom." |
| 2 | 27:363 (the Ropewalk's run) | "Tolver took the spar off the shins with his stance, **laid**." | "Tolver took the spar off the shins with his stance, **planted**." |
| 3 | 27:383 (the haul) | "…steady and fast, with Tolver **laid** at the bottom keeping him off the stone." | "…steady and fast, with Tolver **planted** at the bottom keeping him off the stone." |

## 3. The finding, verified (and one correction to the earlier report)

- **What a lay is.** "Open both doors together and twist them to agree: a lay, laid doors" (UNIVERSE_BIBLE §3).
  The manuscript says the same: "Two laid is two hands on the rope" (18:469). "She's not laid now, she's one
  door" (41:323).
- **Tolver's declaration at the Carry.** "*Carrow, edge and stance, laid. Lyle, ward and stance, laid. Tolver,
  stance. Treen, ward.*" (27:359; the same at 18:41). Carrow and Lyle are declared with two doors and
  "laid". Tolver is declared with one door, stance, and not laid. The Carry runs on declared roles: Seven
  declares "Rowan, stance, declared" (26:311), and the ledger records "stance at the Carry". So narrating
  Tolver as laid in that run, two paragraphs after his declaration, has him using a lay he did not declare.
  Nobody remarks on it. A listener hears the contradiction.
- **Correction to `AUDIO-CLARITY-26-27-REPAIR.md` §7.** That report said Tolver "only has one door". That
  goes beyond canon. Carrow says at 41:323 that she "was laid for four years, and so was I, and so were Lyle and
  Tolver". Tolver's door count is therefore not settled as one, and I have not settled it here. The defect is
  the narrower one above: "laid" contradicts his declared single stance **at the Carry**. 41:323 is about
  his training years. It is consistent with this repair and was not touched.
- **Why "planted".** It is the book's word for a still door holding, and the Carry's own: "Trewin took the spar
  off the Purser's shins with his still door planted" (27:311). Perrin, a Meridian still door, says "planted"
  throughout his own Carry scenes. A planted door holds and cannot walk. That is exactly what Tolver does: he
  lifts the spar off the shins, as Perrin and Trewin do while planted (27:31–33, 27:311), and he stays at the
  foot steadying the Purser while Carrow and Treen haul.
- **26:27 is the softest of the three.** It is Perrin's forecast before anyone declares, not narration of the
  run. I changed it with the other two so that the forecast and the run use the same word for the same job,
  and because it was one of the three sites the earlier report named. "Planted" is also Perrin's own word.

## 4. Previous repairs retained exactly

Each line was checked by exact-string match after this edit (count = 1):

- 26:15 — "After twelve fours have shown us how, and before eleven who'll have seen us." (audio-clarity change 1)
- 27:383 — "held it till Lyle had it, and went up the ladder after Treen, and Tolver said *up,* and Carrow and
  Treen hauled from the top," (audio-clarity change 2). Change 3 above alters only the later word "laid"
  in the same paragraph.
- 26:63 — "And Wednesday's the Longshore. If they go on Tuesday, you don't plant on Wednesday." (whole-book WB-09)
- 27:377 — Carrow's unlaying (M4 P2.2) is unchanged.

`diff` against the frozen edition shows exactly three changed lines (26:27, 27:363, 27:383), each differing by
one word.

## 5. Joins

| Changed paragraph | Previous | Next | Check |
|---|---|---|---|
| 26:27 | 26:25 "Everybody will take the stair." | 26:29 "And Halden?" | The forecast now matches the run (27:363, 383) |
| 27:363 | 27:361 "The bell went." (after the declaration at 27:359) | 27:365 "Twenty," … | Lyle "laid" (declared laid) is unchanged; Tolver planted, as declared |
| 27:383 | 27:381 "It was flat…" | 27:385 "They ran him to the mark." | The haul repair is intact; Tolver holds at the foot, planted |

No occurrence of Tolver with "laid" remains in the manuscript (`grep "Tolver[^.]*\blaid\b"`: none).

## 6. Left alone, and what is still owed

- **26:287, the Ropewalk second four's unnamed carry ("Their carry, laid … stood laid at the bottom").** That
  person is not Tolver, and their doors and declaration are never given, so a two-door lay is possible. It is
  not part of this finding and is not a contradiction.
- **The acceptance table** still lists the accepted hashes for 26 and 27. It needs one explicit addendum after a
  fresh-context recheck of all five 26–27 changes: the two audio-clarity changes and these three. Not edited.
- **Narration artifacts** for chapters 25–27 still reference the accepted source hashes and must be refreshed
  and validated before 26–27 render. Not touched.
- **Maps and ledger:** no change is needed. Canon records no lay for Tolver at the Carry.
