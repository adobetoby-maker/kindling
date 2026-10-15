# Physical-continuity repair: the jar cart (chapter 40) and the tun's bottom (chapter 41)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime; not verifiable from inside the session), Max CLI |
| Session | `https://claude.ai/code/session_01TJCtfuBkGyCoVgq5hrYS2h` (background job `64f974d4`) |
| Date | 2026-10-15, about 16:00–16:05 MDT |
| Instruction | Owner: "Verify and minimally resolve only loaded-cart and water-before-bottom contradictions; freeze and report." The owner authorised this bounded loop, in which the same author repairs the findings the narration pass sent back. |
| Findings answered | `narration/monroe-1.2.5/calder/chapters-40-42/chapter-40/writing-monroe-feedback.md` (SHA-256 `6a49b904e1c02768500240faf797c765fc2f96855cdc9aa0fcd00d95699d39fb`), BLOCKED at 40:227 (prose para 113). `…/chapter-41/writing-monroe-feedback.md` (SHA-256 `769e15f00a4b78d823ffa94fc78c0e011ce4b2333a363590709a8d93cfee3c18`), BLOCKED at 41:291 (prose para 141). |
| Read before editing | Chapters 40, 41 and 42 in full; both feedback files; `WHOLE-BOOK-RECHECK-CONFIRMATION.md` rows 40–42; `WHOLE-BOOK-REPAIR.md` WB-19/F19 and WB-20; the tun and cart mentions in chapters 42–48; the earlier frozen editions of 40 and 41 |
| State at start | `manuscript/chapter-40.md` and `chapter-41.md` matched the accepted hashes in `WHOLE-BOOK-RECHECK-CONFIRMATION.md` rows 40–41, and matched `sourceSha256` in both `chapter-4{0,1}.performance.json` |
| Files edited | `manuscript/chapter-40.md` (1 line), `manuscript/chapter-41.md` (2 lines) and this report. New frozen edition `editions/audio-physical-40-41-pre-repair/` |
| Not touched | Chapter 42 (still `6d9e7dca…`, byte-identical) and every other chapter. Every earlier report and frozen edition. Maps, ledger, canon/continuity files, the acceptance table and `AUTHORSHIP.md`. Every narration artifact: feedback, direction, performance JSON, clarity review, contexts, prompts. Scripts and git state. No commit, push, publish, render or listening. No Skill, Agent, subagent, other model or paid API. |

**Scope of claim.** This report changes the text only. Nobody has listened to it, re-narrated it or rendered it, and
the narration validators have not been rerun. Both narration source hashes are now stale (see §6).

## 1. Freeze (before any edit)

`editions/audio-physical-40-41-pre-repair/` did not exist. I created it and copied both working files into it with
`cp -p`. The copies are read-only (444) and have a `SHA256SUMS.txt`. They verified `OK` before the edits and again after.

| File | Frozen (= accepted) | After this repair | Words (`wc -w`) | Bytes |
|---|---|---|---|---|
| `chapter-40.md` | `4c32f991450a9104fe9cc37615346469383cc72753fb715dc7d451530fc11aee` | `bcad51d91d6ca13904beaaae4d30f92c4b0c693533c9dbac83d9cc246d48f38d` | 7,972 → 7,971 (−1) | 40,878 → 40,872 (−6) |
| `chapter-41.md` | `a67ed23f4ac8db2330dce78c4f0521211f32435e5bb662484dde23bc32efd104` | `260de2fc655313a0cc45dde3581ab6a52ff0b40f5d707adedeb449c89a6f58ae` | 7,231 → 7,229 (−2) | 37,503 → 37,500 (−3) |
| `chapter-42.md` (control) | `6d9e7dca70bead9dae377f17c457607434da5e0e690bce5ebb5a286a8e179506` | unchanged | 6,896 | — |

Chain: accepted → `editions/audio-physical-40-41-pre-repair/` → current. The paragraph and line counts are
unchanged in both chapters.

## 2. Changes (exact)

`diff editions/audio-physical-40-41-pre-repair/chapter-4N.md manuscript/chapter-4N.md` shows only these lines.

| # | Ch:line (para) | Before | After | Words |
|---|---|---|---|---|
| 1 | 40:227 (prose para 113) | "…with the two sisters a step behind her, and the empty cart left standing by the gate, and the thirty-six jars on it in their straw." | "…with the two sisters a step behind her, and the cart left standing by the gate, and the thirty-six jars on it in their straw." | −1 |
| 2 | 41:291 (prose para 141) | "…standing on end with no head in it. They lowered it down the Graving's ramp on rollers and stood it on the stone of the dock floor at the seaward end, on the chalk where the lane pen had been, and the Company's men filled it from the fire main with a canvas hose until the water stood in it level with the top hoop. Then they nailed a board across its bottom from the outside, because a tun with no head and no bottom would not have held a cupful." | "…standing on end with no head in it. Boards had been nailed across its bottom from the outside, because a tun with no head and no bottom would not have held a cupful. They lowered it down the Graving's ramp on rollers and stood it on the stone of the dock floor at the seaward end, on the chalk where the lane pen had been, and the Company's men filled it from the fire main with a canvas hose until the water stood in it level with the top hoop." | −1 |
| 3 | 41:319 (Kiva to Treen; follows from #2) | "It held because it's a tun with a board nailed under it." | "It held because it's a tun with boards nailed under it." | −1 |

The opening of 41:291 ("The Company's cooper sent it down … a brewer's tun with eight iron hoops, as wide across as a
big man is tall,") is unchanged. In #2 the bottom sentence moved and was recast. Every other word in the paragraph
stands in its original order.

## 3. Evidence

**40:227: a cart called empty with jars on it (confirmed).** The sentence called the cart empty and then put the
thirty-six jars on it. Every other reference agrees that the jars stay on the cart:

- 40:183: the jars stand "in their straw in rows" on "the low flat cart";
- 40:185: "There are thirty-six on that cart";
- 40:373: "On a cart at the seaward end of the Graving, under a grey cloth, thirty-six jars stood in their straw";
- 42:351: the sisters take the loaded cart back to the Mole;
- 43:49 and 43:61: the cart is called "empty" only after the fitters have taken the jars off it.

The adjective was the only error. Deleting it keeps the cart, the gate, the count, the straw and Thrale's departure
by the seaward ramp with the two sisters. Origin: the slip is original. It is in
`editions/movement-005-first-draft/chapter-40.md:223` and `editions/whole-book-pre-repair/chapter-40.md:227`.

**41:291: water before bottom (confirmed).** The men filled the headless tun to the top hoop and only then ("Then")
nailed on the bottom, and the same sentence said the tun could not hold a cupful without one. That order cannot hold
the water. The repair puts the existing bottom in place before the tun is lowered, stood on end or filled. It uses the
past perfect ("had been nailed") and states no new agent, place or method. The tun arrives with its bottom on, as it
leaves the cooper's yard.

- **"Boards", not "a board".** The tun is "as wide across as a big man is tall". One narrow board nailed across it
  could not close it. "Boards … across its bottom" describes a bottom made of boards, which is what holds the water
  for the rest of the scene and in chapter 42.
- **"Board" family kept, "plank" not reintroduced.** `WHOLE-BOOK-REPAIR.md` WB-19/F19 deliberately changed this
  tun's "plank" to "board" at 41:291 and 41:319. That keeps "plank" for the like-doors team term taught at 41:249.
  This repair keeps the accepted word and changes only its number.
- **41:319 follows from #2.** Kiva's "a tun with a board nailed under it" brought back the single-board picture that
  #2 removes. Making it plural keeps her line and its point (the tun holds only because something is nailed under
  it) consistent with 41:291. This is the only change outside the two located lines. A reviewer can reject it on its
  own, and #2 still stands without it.
- **Origin.** The order slip is original. `editions/movement-006-first-draft/chapter-41.md:283` has "Then they nailed
  a plank across its bottom" after the filling. WB-19 changed only the noun.

## 4. Preserved

- **Chapter 40.**
  - Preserved: the cart and its position by the gate; the thirty-six jars in their straw; Thrale's exit by the
    seaward ramp; the two sisters a step behind her.
  - Unaffected: the given/brought distinction, Peverell's book line, the Committee's signature and the Board's
    warrant.
- **Chapter 41.**
  - Same prop: the cooper's brewer's tun with eight iron hoops, standing on end with no head, and its nailed-board
    bottom.
  - Same delivery and placement: the dray, the ramp and rollers, the seaward end of the dock floor, the chalk where
    the lane pen had been.
  - Same fill: the Company's men, the fire main, the canvas hose, water level with the top hoop.
  - Brask's "It's got a bottom" and Coombe's "It's got weight", the rehearsal purpose (weight and slop, not fold or
    time), and every pass, call, slop and outcome after it.
- **Powers and outcomes.** No door, ward, ember, still door, count or result is touched in either chapter.
- **Chapter 42** is byte-identical. Its tun references (42:125, 147, 157 "on its plank", meaning the still-door team,
  171, 185, 193, 311, 345) and the cart at 42:351 all still agree.

## 5. Joins reread after the edits

- **40:225 → 40:227 → 40:229.** Thrale's last speech to Kiva, then her exit with the cart now simply "the cart" and
  the jars on it, then the town's count returning through the bench. The listener keeps one picture: a loaded cart
  left by the gate. This matches the night image at 40:373.
- **41:289 → 41:291 → 41:293.** "What was nearest to a cask full of water … was a cask full of water." Then the tun
  arrives with its bottom already boarded, is lowered, set on the chalk and filled to the top hoop. Then Brask,
  looking at it: "It's got a bottom." He is now reacting to a bottom stated two sentences earlier, so his line
  contrasts the stand-in with the real ring ("no head and no bottom", 41:161). It does not follow a nailing just done.
- **41:317 → 41:319 → 41:321.** "It held," then Kiva's "a tun with boards nailed under it", then Treen going pale.
  The meaning and rhythm are unchanged.
- **Checks.** Each edit was applied as an exact-once replacement. In both chapters, a quote-parity scan finds no
  non-blank line with an odd number of `"` marks. "empty cart" no longer occurs in chapter 40. Chapter 41 has no
  "plank" on the tun lines. The frozen copies still verify `OK`.

## 6. Rejected or not acted on

- **Feedback proposal for 41 (not taken literally).** The feedback proposed moving "the existing bottom-board action
  before filling the tun". I moved it before the lowering as well, in the past perfect. The literal version would
  have the men nail a bottom on from the outside after the tun stands on end on the dock stone, and that is
  physically awkward. I also made the board plural, as §3 explains.
- **Considered and rejected for 40.** I considered "the cart left standing by the gate, the thirty-six jars still on
  it". I rejected it because it adds a word and changes the rhythm, and the feedback's one-word deletion is enough.
- **Observed, out of scope, not verified or changed.** 45:307 says the cart "had carried thirty-six jars along the
  Long Quay on Saturday", but the jars are revealed in the Graving on Sunday (chapter 40). I have not checked whether
  the cart went along the quay on Saturday before it was shown. This report records the line and does not repair it.

## 7. Next (not done here; not mine to do)

- **Acceptance.** Whoever holds the acceptance table should take the new hashes in place of `4c32f991…` and
  `a67ed23f…`:
  - chapter 40: `bcad51d9…`, 7,971 words;
  - chapter 41: `260de2fc…`, 7,229 words.
- **Narration.** `chapter-40.performance.json` and `chapter-41.performance.json` still name the old `sourceSha256`.
  `narration/RECHECK-PHYSICAL-40-41.prompt.md` is already staged for the independent recheck. That recheck must:
  - compare the frozen and current text;
  - reread paragraph 113 of chapter 40, paragraph 141 of chapter 41, line 319 and their joins;
  - refresh the word-locked prose, paragraph reviews, direction and hashes for 40 and 41 only, with chapter 42
    preserved;
  - rerun both validators before any ready marker.

  Changes to the word stream:
  - chapter 40 loses one word;
  - chapter 41 loses two words, and in paragraph 141 one sentence moves ahead of two others.
