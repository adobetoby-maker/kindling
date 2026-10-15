# Kindling 2680, Book Two — Movement Four — consolidated repair record

> Built by TAC

Date: 2026-10-15. Status: **same-author repair of chapters 25–32, in place. Not rechecked, not cold-read
after repair, not accepted, not committed, not pushed, not published.** Chapter 33 was not drafted. No
Movement Five work was done.

## 0. Who, how, and from what

- **Seat:** Monroe Jackson 1.3.0 / O'Connor 1.3.0. Public byline: Monroe Jackson. Requested author:
  Claude Opus 5.5.
- **Runtime model, as reported by the session: Claude Opus 5.5, model identifier `claude-opus-5-5`.** This
  is what the runtime states. It cannot be verified independently from inside the session. No subagent,
  other model or delegated worker wrote or edited any prose or record. No codex or OpenAI call was made.
- **Session:** Claude Code background job `647704f1` (job directory `~/.claude/jobs/647704f1`); remote
  session `session_017hq6UNUu29qY4gquWotNEW`. The job began at about 02:18 MDT on 2026-10-15.
- **Brief:** delivered in-session. Its text matches `planning/OPUS-5.5-MOVEMENT-004-REPAIR.prompt.md`
  (196 lines), SHA-256 `82226e2e2e3c91a71a338c3fe91fc5bd3ad5eda1089812d9c901dbbe03520c36`. That was
  checked by spot comparison of distinctive lines, not byte for byte.
- **Isolation:** worked in place in the git worktree `/Users/drive/kindling-2680-book-02`, branch
  `codex/kindling-2680-book-02`. The EnterWorktree tool was not available in this session, and prior
  movements worked in the same place. No commit was made.
- **Evidence read, in the brief's order, before the first edit:**
  1. `provenance/MOVEMENT-004-EDITORIAL-REVIEW.md` (in full)
  2. `provenance/MOVEMENT-004-COLD-READ.md` (in full)
  3. `provenance/MOVEMENT-004-CONTINUITY.md` (in full)
  4. The Movement Four block of `STATE_LEDGER.md` (with the M3.9 open items); `UNIVERSE_BIBLE.md` and
     `CHARACTERS.md` (in full); `BOOK_MAP.md` (the Movement Four section and the related lines);
     `packets/MOVEMENT-004.md` (in full)
  5. `manuscript/chapter-25.md` to `chapter-32.md`, completely and in order
- **One targeted check outside the movement:** a search of `chapter-24.md` for Trewin's Sunday scene (C16).
  Chapters 1–24 were not edited.
- **Both reviews are simulated reads by the same model family.** Neither is human reader feedback, and this
  repair shares their blind spots.
- **Measurement:** `python3 -I provenance/tools/m4_metrics.py manuscript`, run before the first edit and after
  the last. The script was not modified (SHA-256 `d38a4760e55d9ef0cdf5397c3c136e199062f57eb3c34019328f68669c645a55`).

## 1. Factual corrections (priority 1)

Line numbers are first-draft numbers in `editions/movement-004-first-draft/`. Each fix is the smallest edit
that makes the line agree with its scene. No event, outcome, date, ash total, power limit, injury, knowledge
boundary or reserved disclosure changed. The printed boards are untouched.

| # | Where | Was | Now | Evidence |
|---|---|---|---|---|
| F1 | ch. 25:39, 53 (the Clerk) | The marking rule was unstated: "A four is marked by the time to find and by the hold, and by nothing else." | That sentence is cut from the opening block. Just before heat one: "A four that holds is marked by its find. A four that steps is marked by how long it held, and by nothing else." | Review C1. This is the only rule that places Seven sixth. It is now said once, just before it matters (P2, the rule block). |
| F2 | ch. 25:151 (heat one) | "A four Kiva did not know stepped at eight minutes, and another at six." | "…had stepped at four minutes, and another at three." | C1. Both now fall below Holloway second's 5:00. |
| F3 | ch. 25:281–283 (heat three) | "Three minutes. Four." / "…At six, one of the three Kiva did not know." The Tarn's step was never given. | "Three minutes. At four, one of the three Kiva did not know stepped." / "…The Tarn's went at five and ten; Trewin did not move." | C1; cold read F (the Tarn's bank "going well" is now credited). Steps are told in clock order. |
| F4 | ch. 25:39 (the rail minute) | Kiva: "The Clerk read it out this morning." The rules as quoted did not include it. | The Clerk's opening adds: "It may take a minute at the rail between the quench and the tune, as at home." | C2. The minute is optional ("may"), so Halden's heat one, which goes straight to the tune, stays legal. |
| F5 | ch. 27:217 (the water) | "…running against them now… It was like walking up a river." | "…running with them now, pushing at their backs, pouring in from the head…". The river image is cut (it had no home at the stair). | C3. The water enters at the head; they walk to the tail. |
| F6 | ch. 27:241 (Aske) | "I felt it go from the bottom of the ladder; everybody did." | "I heard it go from the lip; everybody did." | C4; cold read D. |
| F7 | ch. 25:233 (Pru reading) | "with her lips moving, the way Orla read the book" | "with her lips moving, the way she read everything". Ch. 32:513 (Orla "with her lips shut") stands, and ch. 27 ("the way Pru read") agrees. | C5. |
| F8 | ch. 30:183 (when Kiva hears of Skerry Pill) | "She would not hear it until three o'clock, at the gate." | "She would not hear it until the cart, on the causeway." This agrees with ch. 32:129 ("I heard. On the causeway."). | C6; cold read B. |
| F9 | ch. 32:71 (the comb place) | "The Board combed the Hunt at the gate on the timber pond from four…" | "The Board combed the Hunt's bags back at the gate on the timber pond, as the Clerk had said it would, from four…". The morning tin-combing stays at the causeway tent (ch. 29); the Clerk's "Every bag is combed at the gate" (ch. 29) now visibly names the place. | Cold read B (the second half). Combing begins at four. |
| F10 | ch. 29:349; ch. 32:445 (Penhale's "I'll read it") | Coombe cites the causeway queue; the page shows Penhale saying it only in the channel. | Ch. 29: "When it's printed, I'll read it. I've told half the causeway so. I'm not one for reading. But I'll read that." Coombe's line is unchanged. He said it twice. | Cold read C. Coombe's protected beat stays exact. |
| F11 | ch. 31:371 (Yeo's clock) | "She called it at twenty past twelve… Forty minutes later" | "…at a quarter past twelve… Half an hour later" | C7. The near post was cut at 12.14 and Penhale was under the fold at about 12.45. |
| F12 | ch. 30:61 (Kellan's distance) | "a blade, forty paces off" | "a blade, sixty paces off" | C8. Halden's stow is 40 above the kiddle and Lyle 20 below it. |
| F13 | ch. 26:39 (Perrin's rehearsal climb) | "then I came up with my door open." It was not on the book. | "…with my door open, off my own thimble." No held figure changes. | C9. |
| F14 | ch. 29:49 (the Clerk's Hunt rule) | "A four does not go onto the mud below a form on running water." | "…on running water, but on its officer's word." | C10. Seven's purse-setting at 11.30 was on Yeo's order with Penhale leading. |
| F15 | ch. 26:205 | "the Harbour Committee wrote to the Clerk three times" | "…wrote to the Works three times" | C14. "The Clerk" is the Clerk of the Measure everywhere else. |
| F16 | ch. 28:165, 189 and 323–327 (Tuesday evening) | Kellan 6.15, Anwen 6.25, the yard at 6.30 after Perrin's very slow walk; twenty dry passes and Bridie's talk, then the three-quarters. | Kellan "at ten past six", Anwen "at a quarter past six". The three-quarters strike, with the stave touch and its log line unchanged, now comes after the first ten passes (Trewin's laugh). The next ten passes and Bridie's question follow it, and then the lamp. | Cold read E. The yes/no hour (a quarter to seven) is fixed by Hart's method, so the clock was loosened around it. Nothing was cut from the scene. |
| F17 | ch. 28:235 (Trewin's hand) | "He held out his hand, flat, as Trewin had held out his own on Sunday morning, at the top of the loft stair." | "He held out his hand." | C16. Ch. 24 (searched) shows Trewin nodding, not offering a flat hand. The false reference is removed and nothing is invented off-page. |
| F18 | ch. 32:533 (found during repair) | Kiva to Ivey: Penhale said it "At half past ten, when the upper one leaned before a gust." | "This morning, when the upper one leaned before a gust." | Ch. 29: the gust came "At ten minutes to eleven"; half past ten was Pru seeing the tear. Not in either review. |

### 1a. The Bench re-ranking check (C1)

The rule on the page: held fours are ranked by find, faster first; stepped fours are ranked by hold, longer
first; every held four ranks above every stepped four.

**Held (on the page):** Halden 1:40, Holloway first 2:00, the Ropewalk first 2:10, Old Four 3:05, Westerley
first 3:30. These are places 1–5.

**Stepped, with hold lengths on the page after repair:** Seven 8:40; Westerley second 5:20; the Tarn first
5:10; Holloway second 5:00; heat one unnamed 4:00 and 3:00; heat three unnamed 4:00. **Off the page**
(the author's reconciliation, consistent with the page): the Ropewalk second and Twenty-Eight both stepped
between 4:00 and 5:00, the Ropewalk second the longer. Every other four stepped sooner.

| Place | Four | Bench marks | Carry (marks) | After two | Hunt (marks) | After three | Printed |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Halden License | 24 | 3 (22) | 46 | 6 (19) | 65 | 46 / 65 ✓ |
| 2 | Holloway first | 23 | [7] (18) | 41 | [7] (18) | 59 | 41 / 59 ✓ |
| 3 | the Ropewalk first | 22 | 2 (23) | 45 | 12 (13) | 58 | 45 / 58 ✓ |
| 4 | Old Four | 21 | 5 (20) | 41 | 2 (23) | 64 | 41 / 64 ✓ |
| 5 | Westerley first | 20 | [9] (16) | 36 | [5] (20) | 56 | — / 56 ✓ |
| 6 | **Team Seven** (8:40) | 19 | 1 (24) | **43** | 15 (10) | **53** | 43 / 53 ✓ |
| 7 | Westerley second (5:20) | 18 | [10] (15) | 33 | 3 (22) | 55 | — / 55 ✓ |
| 8 | the Tarn first (5:10) | 17 | 4 (21) | 38 | 24 (1) | 39 | 38 / — ✓ |
| 9 | Holloway second (5:00) | 16 | [8] (17) | 33 | [4] (21) | 54 | — / 54 ✓ |
| 10 | the Ropewalk second [4:00–5:00] | 15 | [11] (14) | 29 | [8] (17) | 46 | — / 46 ✓ |
| 11 | Twenty-Eight [4:00–5:00] | 14 | 6 (19) | 33 | 1 (24) | 57 | — / 57 ✓ |

Bracketed places are the author's reconciliation, unchanged from continuity §3. The check was run as a
script over the table: every printed figure on the after-two sheet (Halden 46, the Ropewalk 45, Seven 43,
Old Four 41, Holloway first 41, the Tarn 38) and on the after-three sheet (Halden 65, Old Four 64, Holloway
first 59, the Ropewalk first 58, Twenty-Eight 57, Westerley first 56, Westerley second 55, Holloway second
54, Seven 53, the Ropewalk second 46) is reproduced. **Seven stands ninth after three, one mark off eighth.**
A four outside the table can score at most 13 + 13 + 16 = 42, so the printed top ten is complete. Under the
first-draft times, the unnamed 8:00, 6:00 and 6:00 steps would have outranked places 7–9 and put Seven
seventh. That conflict is gone.

## 2. Clarity at the teaching moments (priority 2; one sentence each, no new scenes)

| # | Where | Change |
|---|---|---|
| P2.1 | ch. 26:273–279; ch. 27:63 (the Carry's clock) | The dead conditional is removed. Kiva: "Half for a minute… Then full. At full it reaches his face at a minute and twenty." Jude: "So we've a minute and twenty." Perrin: "Then a minute and twenty's long." Ch. 27: "A minute, by the customs house clock. They had beaten the water to his face by most of a minute, and it did not matter now." (Out at 0:26, against 1:20.) |
| P2.2 | ch. 27:377 (Carrow) | "But she was holding it with nothing open. A laid girl cannot walk, and to lift and walk she had shut both doors." |
| P2.3 | ch. 30:317 (why the Tarn's stow does not fold) | Kiva no longer claims a difference that does not explain it: "It's still on a post." … "I don't know why. Ours folded. It should." |
| P2.4 | ch. 30:317, 373, 401; ch. 31:107 (the climax geometry) | The far post has one bearing: "on the west side of the bend, in the deep water". The swing: "…came round after it, its closed end last… swung round on the standing post like a door on its hinge, out of the downstream and inland over the west mud, its mouth to the sea that had not yet begun to come in." Later: "still swinging round on the post over the west mud" and (ch. 31) "had swung round on its post over the west mud". "Across the channel" is removed wherever it described the swing. It is kept where the sleeve truly spans the channel (from Trewin's boots to the post). The closed end is named before it lands on Penhale. Net length about +4 words. The slack still holds, Penhale goes in "as a man goes to a gate…", and the unanswered "*Far edge*" are unchanged. The first two paragraphs of ch. 31 were read against the new bearing and needed no change ("the grey fold lying on the west mud across the channel" is Kiva's view from the east bank). |
| P2.5 | ch. 27:311–313 (the Tarn's carry) | "Then he did a thing that made the whole quay go quiet" is removed from the shoulder lift (Brask's move three runs earlier). The quiet now falls on the planting: "He planted on every step he took, and the whole quay went quiet." |
| P2.6 | ch. 25:405 (the Chair's hand) | "He asked her to ask for it in the Chair's hand, as you told him the country could." |
| P2.7 | ch. 25 §1 (the rule block) | Kept. It gains one clause (the rail) and loses one sentence (the marking rule, which moves to just before heat one). The block is broken around the first heat. |
| — | Chapter titles | The "Kiva:" titles are left as they are, per the brief. |

## 3. Catchphrases, images, restatement, the aftermath's shape and rhythm (priority 3)

### 3a. Jude's "I'd want it said" (13 → 5)

| Chapter | Kept | Recast |
|---|---|---|
| 27 | §3 "I'd want it said… that I was at the top." | §2 "I leaned on it once, for a loop, and I'd do it again." |
| 28 | §5 "I'd want it said I thought about it." (Kiva's "It's said" answers it at once) | §1 "This is honest as well."; §1 "I know it's luck. We didn't do anything to get it."; §5 "I don't know… I've been looking at the sea for half an hour… And I'm going out on it tomorrow anyway." |
| 31 | §3 "I'd want it said… that I've seen it come in now. Over somebody." (protected) | — |
| 32 | §5 board line "I'd want it said that I know it's honest…" (protected); §11 window speech "I'd want it said I don't know. I'll stay anyway." (protected) | §1 "I thought about it, all the way back from Mallow…" and "I don't know what I'd have said." (the variant "I'd want that said too" is cut); §2 "I'd give it all back."; §5 "I don't care about the mark. Tonight."; §11 "I know she will." |

**Location note.** The brief and the cold read both place "I've seen it come in now. Over somebody." at
ch. 32 ~l.567. It is actually ch. 31:319 (the spur, at the flood). The ch. 32:567 window speech is a different
line. Both were kept, one use each.

Anwen's own "I want it said" (3) is her locked voice and was left unchanged. Of the other "I'd want…" uses
(Aske ch. 25, Bray ch. 30, Yeo ch. 31, Anwen ch. 32), none is the formula, and none was changed.

### 3b. Other tics

- **Perrin's "I'd like it known" / "I'd like that known" (4 + 2):** all Perrin's, all kept.
- **Others' borrowed forms, varied:** Aske ch. 32:7 "I'd like that understood" → "Understand that."; Polglase
  ch. 32:197 "He'd like that noted as well" → "Put that in your N.B. as well." Aske's ch. 29 "I'd like there
  not to be" is ordinary usage and was left.
- **"expect nothing else" (4 → 3):** Kellan's ch. 25 and ch. 32 uses are kept, and so is Pettit's deliberate
  echo in ch. 30 (it carries the protected "I'm saying it about you"). Kellan's ch. 28 use → "That's Pettit."

### 3c. Repeated images: one home each

| Image | Home kept | Others |
|---|---|---|
| "frost on a window" (3 → 1) | ch. 31:171, Penhale's ward "in the shape of a fern" | ch. 30:271 → "like dust on a sill"; ch. 31:159 → "thin as a cobweb" |
| "like a sack going (up) into a loft" (2 → 1) | ch. 26:287, the Ropewalk second's haul from the top | ch. 27:195 → "the Purser went over the edge and lay on his back on the quay"; also ch. 27:343 "like a sack between two porters" → "like a chest between two porters" |
| "as though nodding were a thing that had to be done properly" (ch. 27 and ch. 32 → ch. 27 only) | ch. 27:299, Trewin's hat (ch. 24:193 also has it; ch. 24 is closed and was left) | ch. 32:41 → "Then he nodded, once." |
| "the way a referee holds up a hand" (2 → 1) | ch. 27:407, Brask's flat hand | ch. 25:307 → "It meant *that was right,* and Pru knew it." |
| "the warm low sound" (3 → 1) | ch. 25:151, where it is defined | ch. 26:291 → "The quay clapped them, not loudly."; ch. 27:265 → "the quay was pleased with them" |
| "before the water" (8 → 4) | ch. 29:289 (Pru, the gust, a different sense); ch. 31:261 Yeo to Coombe, "Before the water turned, Dinah"; ch. 32:187 **Noa's ledger, the single formal record**; ch. 32:527 Kiva to Ivey, "It turned before the water" (her development beat) | ch. 31:261 first "Before the water." cut; ch. 31:303 Yeo's slate → "at a quarter to one, in the slack"; ch. 32:183 Kiva to Noa recast as bare data (see 3d); ch. 32:531 "…before the water had" → "as if it had heard the turn coming" |

### 3d. Telegraphing (ch. 29) and restatement (ch. 31–32)

- **Ch. 29 §3–§5.** Penhale's two "never gone onto the mud" lines become one: the first is kept (ch. 29:169,
  with "my mother likes it", its only use). "I'll not, likely. I've been reserve on four Hunts, and never been
  onto the mud yet." (29:341) is cut to "I'd like to see it." Yeo's single echo (ch. 31:343, "…and his mother
  liked it") is kept.
- **Ch. 31 §1.** "The water had not turned. Only the stow." is cut. It exactly restated the last line of
  ch. 30.
- **Ch. 31 §4 (the yard).** Yeo's "From the spur. She asked. Freeing a line… I said what the book says." is cut
  to what is new: "It was lying on the mud like a hem, and it was on a post, and I didn't look at the post. I
  looked at the skin."
- **Ch. 32 §3 (Noa).** Kiva gives Noa only the data his ledger records: "The Tarn's stow turned at a quarter to
  one, or a minute before… Perrin had the watch… The water turned seven minutes after. My fingers said nothing
  till it did, and the grass stood up straight." (From about 70 words to about 40.)
- **Ch. 32 §5 (the board).** Kiva's memory of Penhale keeps the image and drops the quoted "When it's printed,
  I'll read it" (Coombe owns that payoff two scenes later).
- **Ch. 32 §10 (Ivey).** The restated timing, fingers and grass are cut to "The Tarn's stow. Seven minutes
  before, with the slack still holding, as if it had heard the turn coming." Kept, because it is new: the far
  edge is "when the thing decides to"; watch the thing, not the water; "a stow's a sleeve. It's got two ends.
  The book's for a sheet." Also cut: "He said when the Marshal's page was printed, he'd read it." Kept
  untouched: Ivey's curlew, "I'll have a second", the *Before* column.

### 3e. The aftermath's shape: breaks removed (2)

| Chapter | Break removed | Join |
|---|---|---|
| 32 | between §5 (the board) and §6 (Dray) | None needed. Same place, continuous time; Dray speaks from behind Kiva at the pole. |
| 32 | between §6 (Dray) and §7 (the *Mercury*) | One sentence added: "Kiva went back along the boards to the Long Quay." Then "…was being sold there…" |

Every line of the three sections is kept. Ch. 32 now has ten sections (was twelve), and the movement has
fifty (was 52; internal breaks 44 → 42).

### 3f. Rhythm (narration only; dialogue untouched except the formula recasts above)

- **Joins of adjacent short narrated sentences, where the thought is continuous:**
  - ch. 28 §0 ×5 ("…flat and clear, as he had said things at the marshal's box"; Pru "winding it as she had
    been since they came in"; "did not answer at once, but looked"; "There was a silence, and Jude…"; "and
    found that they were all looking at her")
  - ch. 28 §1 ×2
  - ch. 28 §2 ×3 ("He did not sit down; he was…"; "and did not look back"; "and at the top she stopped")
  - ch. 28 §5 ×6 ("Pru had gone ahead, and…"; "again and was standing"; "and he did not look round"; "Perrin
    did not answer, and Kiva did not know the answer"; "and Perrin watched him go"; "but did not lay the two
    fingers"; "It was not much: two words, once…")
  - ch. 32 §1 ×1
  - ch. 32 §2 ×6 ("not a hair but a voice, and it sang"; "did not sing; it hummed"; "and Jude opened the book";
    "and had not thought anything of it"; "saw Kiva and came over")
  - ch. 32 §3 ×2
  - ch. 32 §4 ×1
  - ch. 32 §5 ×1
  - ch. 32 §9 ×1
  - ch. 32 §11 ×3 ("…what he had said, so she stood"; "and did not cross anything out"; "She did not write that
    down; there was no column for it tonight.")
- No run-ons were added. The short call beats (*Set.* / *Nobody.* / *Fold.*), the climb (ch. 27 §0), the
  Skerry Pill fight (ch. 30) and the pass (ch. 31 §0) were not shortened.
- **"slowly" 43 → 28** (15 varied or cut): ch. 25 ×2, ch. 26 ×1, ch. 27 ×2 (one now "face by face"), ch. 28 ×2,
  ch. 29 ×1, ch. 30 ×2 ("by degrees"), ch. 31 ×1, ch. 32 ×4. The nodding-line change in ch. 32 removed one
  more.
- **Waypoint not reached.** Narration's short share moved 42.2% → 41.7%, against a waypoint of about 38%. Most
  of the remaining short narration is either deliberate (board readouts, ledger lines, Lyle's empty-hand beat,
  the calls) or speech tags left after quotes are stripped. Joining those would mean recasting dialogue or
  adding run-ons, which the brief rules out. The formula targets are unchanged.

## 4. Word counts (`wc -w`, headings included)

| Chapter | First draft | Repaired | Δ |
|---|---:|---:|---:|
| 25 | 6,320 | 6,356 | +36 |
| 26 | 5,110 | 5,104 | −6 |
| 27 | 7,295 | 7,270 | −25 |
| 28 | 5,060 | 5,023 | −37 |
| 29 | 6,195 | 6,189 | −6 |
| 30 | 6,348 | 6,357 | +9 |
| 31 | 6,684 | 6,659 | −25 |
| 32 | 9,389 | 9,245 | −144 |
| **Movement** | **52,401** | **52,203** | **−198** |

The movement is still inside the packet's 50,000–57,000.

## 5. Measures (`m4_metrics.py`, unmodified), before → after

**All text**

| Metric | Target | Before | After |
|---|---:|---:|---:|
| Body words (script tokenizer) | — | 52,311 | 52,116 |
| Sentences | — | 5,516 | 5,456 |
| Mean / median words | 14.6 / 11 | 9.48 / 6 | 9.55 / 6 |
| Population SD | ~26 | 9.18 | 9.23 |
| ≤5 words | ~27.7% | 46.1% | 45.8% |
| ≥40 words | ~3.3% | 1.6% | 1.7% |
| Longest | — | 62 | 62 |
| Paragraphs; median / mean; share over 60 | 18 / 26.8 | 1,667; 18 / 31.4; 18.8% | 1,667; 18 / 31.3; 18.5% |
| Flesch / FK grade | 72.3 / 6.8 | 96.3 / 2.2 | 96.3 / 2.2 |
| Progression per 10k (raw) | — | 29.1 | 29.4 |
| -ly filtered per 10k | — | 22.0 | 19.2 |
| Dialogue share of words | — | 29.1% | 28.9% |

**Narration only (quoted spans removed)**

| Metric | Before | After |
|---|---:|---:|
| Sentences | 3,398 | 3,361 |
| Mean / median | 10.9 / 7 | 11.0 / 7 |
| ≤5 words | 42.2% | **41.7%** |
| ≥40 words | 2.6% | 2.7% |

Dialogue only: ≤5 words 63.9% → 64.2% (median 4 → 4). Dialogue was left alone apart from the formula recasts.

**Sections and breaks**

| Metric | Before | After |
|---|---:|---:|
| Sections | 52 | 50 |
| Section mean (words) | 1,006 | 1,042 |
| Breaks per 10k, internal only | 8.41 | 8.06 |
| Breaks per 10k, with chapter openings | 9.94 | 9.59 |

**Per chapter (≤5 share / median / sections)**

| Chapter | Before | After |
|---|---|---|
| 25 | 40.0% / 7 / 7 | 39.6% / 7 / 7 |
| 26 | 45.8% / 6 / 5 | 45.8% / 6 / 5 |
| 27 | 45.8% / 6 / 5 | 45.6% / 6 / 5 |
| 28 | 50.5% / 5 / 6 | 50.6% / 5 / 6 |
| 29 | 46.4% / 6 / 8 | 46.3% / 6 / 8 |
| 30 | 44.5% / 6 / 4 | 44.7% / 6 / 4 |
| 31 | 44.4% / 6 / 5 | 44.0% / 6 / 5 |
| 32 | 49.2% / 6 / 12 | 48.6% / 6 / 10 |

Ch. 28's all-text short share did not fall. Its narration joins were offset by the shorter dialogue left where
Jude's formula was cut ("This is honest as well."; "I know it's luck.").

**Viewpoint.** The script's POV map keys ch. 32 sections by index. After the fold, the Orla and Mara sections
are §6 and §7, not §8 and §9. The unmodified script's "after" viewpoint figures are therefore misattributed
(it reads Kiva 43,747, Mara 2,249, Orla 999). The figures below come from a temporary copy of the script, kept
in the job directory and not in the repository, with only those two map keys shifted: `(32, 8)` → `(32, 6)`
Orla and `(32, 9)` → `(32, 7)` Mara. Every other line of the copy is identical.

| Lens | Before | After (remapped) |
|---|---:|---:|
| Kiva | 43,922 (84.0%) | 43,738 (83.9%) |
| Mara | 2,282 | 2,283 |
| Kellan | 2,541 | 2,541 |
| Rhea | 1,432 | 1,420 |
| Anwen | 1,159 | 1,160 |
| Orla | 975 | 974 |
| **Cutaways** | **8,389** | **8,378** |

Both totals stay inside the packet's 84–87% Kiva and 6,500–8,500 cutaway words. The script in
`provenance/tools/` was not changed. A recheck that uses it should apply the same two-key shift for ch. 32.

Reserved terms: "Unroofed" 0, "Breach" 0. Month names: none.

## 6. Phrase counts, before → after (case-insensitive, ch. 25–32)

| Phrase | Before | After |
|---|---:|---:|
| "I'd want it said" (Jude) | 13 | 5 |
| "want it said" (all, incl. Anwen's "I want it said") | 16 | 8 |
| "I'd like it known" (Perrin) | 4 | 4 |
| "I'd like that known" (Perrin) | 2 | 2 |
| "slowly" | 43 | 28 |
| "before the water" | 8 | 4 |
| "frost on a window" | 3 | 1 |
| "the warm low sound" | 3 | 1 |
| "like a sack going (up) into a loft" | 2 | 1 |
| "as though nodding were…" | 2 | 1 |
| "the way a referee holds up a hand" | 2 | 1 |
| "expect nothing else" | 4 | 3 |
| "never gone / been onto the mud" | 3 | 2 |
| "I'll read it / that" | 4 | 3 |
| "I'd want" (script lexicon, all speakers) | 18 | 9 |
| "said nothing" | 8 | 7 |

## 7. Strengths protected (checked present and unchanged after repair)

- "Don't give them yours." / "That's why they'll want it."
- the torn page caught "as if it had been a rung"; "I want it in your voice, so I've got it twice"
- the jacket exchange
- "twenty-two little pieces of the earth"
- "Say the price." / "I'm only the word."
- the eleventh rung and "You waited for my heel"
- "It's not better… the other side of the same thing."
- "There are no squares on a ladder."
- "It's horrible" / "It gets more usual. That's not the same."
- "What happens in the gap?"
- *Far edge* once, and the fold lying down where Kiva had been
- "It's a sleeve. It's got two ends. The book's for a sheet."
- "Let it come to you… Be the nearest thing."
- "He stopped at three."
- "And mine. I said it was ground."
- "He had nobody at his far edge."
- Coombe's still hands, and the type set "like somebody counting"
- Ivey's curlew
- *Before. D. Penhale…*
- the night survey that closes ch. 32

## 8. Items left unchanged, with the reason

**Recorded only, per the brief:**

- **Perrin lifting against Aske's card** (ch. 31 §1). Carried to Movement Five; no consequence is added.
- **Penhale's ward left as frost** (C18). An owner note. Its image is now the only "frost on a window" in the
  movement.
- **Monday's "It was the neap"** (ch. 26:141). Accepted as written: Hart's own word at supper, three days early
  by the review's tide estimate. "Near the neap" would also do; the owner decides.
- **Orla's "by sight for a fortnight"** (C17). Accepted as off-page.
- **"Skerry Pill" and the Halden clerk's patent line** (cold read H). This is the planned disclosure, and it is
  left as written.

**Owner items, not decided here:**

- whether sentence targets govern dialogue (64% short)
- the progression-vocabulary trend (about 29 per 10k raw, below the book average)
- Perrin's lift against the card
- the frost-shape of Penhale's ward
- the Movement Three open items (the 41-minute hold, the brown-ink line, "my best machine")

None of these was touched.

**Also left, by judgment:**

- **C19 (time words for the lodger's "evening low" and Kellan's "not moved since five"):** not in the brief, and
  each is defensible as written.
- **C20 (Perrin's "two places in a bracket"):** his estimate.
- **Kiva's guess "Forty paces off, likely"** (ch. 28) about the Tarn's stow: a guess before the draw, and the
  page later gives sixty.
- **Perrin's six "I'd like it/that known":** kept as his voice, per the brief.
- **Ch. 24:193's nodding line:** chapter 24 is closed.

## 9. Frozen edition and other files

- `editions/movement-004-first-draft/` was not modified. `shasum -a 256 -c SHA256SUMS.txt` returned OK for
  all eight files before the first edit and after the last.
- Chapters 1–24 were not edited.
- An untracked file `packets/MOVEMENT-005.md` appeared in the working tree during this session. It was not
  written, read or edited here.

**Repaired chapter hashes (SHA-256):**

| File | SHA-256 |
|---|---|
| chapter-25.md | fbd034ec2f9c353dbbb82243bd0b95a3ac0e90bc580b91a864babb998b6e365d |
| chapter-26.md | 131cf5810a7417aa9b821f2da50416a2bcdc3dafd091cacdc712323965a035bb |
| chapter-27.md | 047cbc477953f9ad483c242c830dd6ea8e2ec49af000327fe6cbcf6abc6fdb79 |
| chapter-28.md | 7f7f8031d8753b9ec72db291ef7e9e17519db855aa7f123b37566dd91d3e9cf2 |
| chapter-29.md | da733c71224bd30b96fffe8a5bc837335b2c3ee45cc88bdf5ee76ba0013dd55a |
| chapter-30.md | a4e471b5833a6a2695f171ca54f42f8b99a029383544a9c8776c746d7078357f |
| chapter-31.md | b76920e9986a1b7a2a0e3ed258d560a799d4c91f7c6e23691fff22d4614cdf7b |
| chapter-32.md | 97794571410b5772ae55f8dd182be9e4bf948d2d1a9515913f262667c9c2f299 |

## 10. Records reconciled

- `provenance/MOVEMENT-004-CONTINUITY.md`: the status line; entries marked *(repair)* in §0, §1, §2, §3, §4, §6
  and §12; and a new §14 table of every reconciliation.
- `STATE_LEDGER.md`, Movement Four block: the status line; M4.2 and M4.4 lines marked *(repair)*; new M4.8 (clocks
  and rules) and M4.9 (owner items carried).
- `AUTHORSHIP.md`: a Movement Four repair entry.

No plan or canon file was changed. This record claims no recheck, acceptance, publication or Movement Five work.
