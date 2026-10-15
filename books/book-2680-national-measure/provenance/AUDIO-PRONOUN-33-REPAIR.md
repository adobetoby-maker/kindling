# Pronoun repair — the Tarn's second-four catcher (chapter 33)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime; not verifiable from inside the session) |
| Session | `https://claude.ai/code/session_01K67v6aQns7pcR684foswqw` (background job `95089cc9`) |
| Date | 2026-10-15, about 12:56–13:00 MDT |
| Instruction | Owner: "Verify and repair only the chapter33 Tarn catcher pronoun inconsistency; freeze and report." The owner authorised this bounded narration-to-author loop. |
| Finding answered | `narration/monroe-1.2.5/calder/chapters-31-33/chapter-33/writing-monroe-feedback.md` (SHA-256 `fb0ed210c4c411549f9fc155bfb38591a0ff0e0ac3a50ac7972f223418bdb70e`), blocking prose paragraph 178, 33:367 |
| State at start | HEAD `d3e231e`. `manuscript/chapter-33.md` = HEAD = the accepted text in `WHOLE-BOOK-RECHECK-CONFIRMATION.md` (`f584ff62…`, 8,529 words) = the narration source (`chapter-33.performance.json` `sourceSha256`) |
| Files edited | `manuscript/chapter-33.md` (one word) and this report. A new frozen edition was added at `editions/audio-pronoun-33-pre-repair/` |
| Not touched | Every other chapter, every earlier report and frozen edition, maps, ledger, continuity files, the acceptance table, `AUTHORSHIP.md`, every narration artifact (feedback, direction, performance JSON, clarity review), scripts and git state. No commit, push, publish or render. No Skill, Agent, subagent or other model. |

**Scope of claim.** This repair changes the text only. Nobody has listened to it, re-narrated it or rendered it, and the
narration validators have not been rerun. The narration source hash is now stale (see §5).

## 1. Freeze (before any edit)

`editions/audio-pronoun-33-pre-repair/` did not exist. I created it and copied the working file into it with `cp -p`.
The copy is read-only (444) and has a `SHA256SUMS.txt`. It verified `OK` before the edit and again after.

| File | Frozen (= accepted = HEAD) | After this repair | Words (`wc -w`) | Bytes |
|---|---|---|---|---|
| `chapter-33.md` | `f584ff623f871dfe4108aae61816e35f729d0d3af6f5f82344d62a9fd7099da6` | `67137ebaa52d5fc114fdabeb822e0478b23e83baf4daf22f56289ce3c06965eb` | 8,529 → 8,529 (0) | 44,405 → 44,404 (−1) |

Chain: accepted → `editions/audio-pronoun-33-pre-repair/` → current.

## 2. Change (exact)

There is one change: one word, "She" became "He". The punctuation is unchanged and no sentence was recast.

| # | Ch:line (para) | Before | After |
|---|---|---|---|
| 1 | 33:367 (prose para 178, the Lane's second carry) | "The third thing the Tarn tried was their catcher. **She** was a small fair boy with a fresh bandage on his wrist, …" | "The third thing the Tarn tried was their catcher. **He** was a small fair boy with a fresh bandage on his wrist, …" |

`diff editions/audio-pronoun-33-pre-repair/chapter-33.md manuscript/chapter-33.md` shows only line 367, and only this word.

## 3. The referent, verified

- **One person.** The same catcher appears three times in the chapter:
  - 33:277 introduces him without a gender: "a catcher with a fresh bandage on one wrist".
  - 33:363 has "their Hold and their catcher on the foot poles", with no pronoun.
  - 33:367–377 is the paragraph under repair and the two that follow it.
- **Every other gendered word for him is male.** At 33:367 he is "boy", "his wrist", "he came in low", "his ward",
  "his hip", "He meant", "his tray". Pru's call at 33:371 is "*His. North.*". At 33:373 there is "touched the boy",
  "The boy kept his tray" and "touched him again". At 33:377 there is "The boy let go and knelt". "She" is the only
  exception, and it contradicts the noun "boy" in its own sentence.
- **Canon.** No other record gives this catcher a gender:
  - `CHARACTERS.md` and `BOOK_MAP.md` do not mention him.
  - `STATE_LEDGER.md` §M4.3 lists "The Tarn's catcher (unnamed): ankle, Tue". That is the first four's catcher at
    the Hunt, a different person.
  - The text before any repair (`editions/whole-book-pre-repair/chapter-33.md:367`) already had "She … boy". The
    slip is original and was not introduced by a later repair.
- **Likely origin.** The paragraph before (33:365) runs on "her": the Tarn captain "folded her arms", and Kiva leans
  "with her knees bent". The "She" probably carried over from there.

## 4. Preserved, and the joins

- **Preserved:**
  - the same single catcher;
  - the fresh bandage on the wrist (33:367, with 33:277);
  - the low approach on the north side;
  - the ward used as a tray, "the width of a doormat", set under the litter's middle;
  - the lift tactic ("lift the litter's middle on his tray and walk it back east over the line");
  - Pru's call, Jude's two halves, the down, and the litter ending a hand's breadth west;
  - the score (7–2) and all plot.
- **Join before (33:365 → 33:367).** 33:365 ends on Kiva leaning the Commodore's head west. 33:367 opens with "their
  catcher" as the subject, so "He" has that antecedent within two words. The listener no longer revises from "she"
  to "boy".
- **Join after (33:367 → 33:369).** 33:369 opens with "Kiva felt it come up under the canvas. She could not…". That
  "She" is Kiva, and it now stands out more clearly against the male catcher.
- **Checks.** No line in the chapter has an odd number of `"` marks. The edit was applied by an exact-once
  replacement. The frozen copy still verifies `OK`.

## 5. Next (not done here; not mine to do)

- **Acceptance.** Whoever holds the acceptance table should take the new chapter-33 hash
  (`67137eba…`, 8,529 words, unchanged count) in place of `f584ff62…`.
- **Narration.** `chapter-33.performance.json` still names `sourceSha256` `f584ff62…`. The narration side must:
  - re-review paragraph 178 and both joins;
  - rebuild the direction against the new hash;
  - rerun both validators before any ready marker.
- **Records.** No ledger, continuity file or map records the pronoun, so none needs changing.
