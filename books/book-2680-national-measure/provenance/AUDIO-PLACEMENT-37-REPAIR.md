# Placement repair — Pru's head/foot call in the second carry (chapter 37)

> Built by TAC

| Field | Value |
|---|---|
| Author of record | Claude Opus 5.5, prose author (`claude-opus-5-5`, as reported by the runtime; not verifiable from inside the session) |
| Session | `https://claude.ai/code/session_01Et3vThEPM4NPXb5Fctm4de` (background job `7c9c2be6`) |
| Date | 2026-10-15, about 14:55–15:00 MDT |
| Instruction | Owner: "Verify and minimally resolve only Pru call versus executed head-foot positions; freeze and report." The owner authorised this bounded narration-to-author loop. |
| Finding answered | `narration/monroe-1.2.5/calder/chapters-37-39/chapter-37/writing-monroe-feedback.md` (SHA-256 `795cffd4d7aea91da1e61e9fa0533b2205a194cda98d438d60162dadaed367bb`), BLOCKED on 37:229 and 37:231 (prose paragraphs 111–112, second carry) |
| State at start | `manuscript/chapter-37.md` = the accepted text in `WHOLE-BOOK-RECHECK-CONFIRMATION.md` row 37 (`59097370…`, 6,629 words) = the narration source (`chapter-37.performance.json` `sourceSha256`) |
| Files edited | `manuscript/chapter-37.md` (two names exchanged in one line) and this report. A new frozen edition was added at `editions/audio-placement-37-pre-repair/` |
| Not touched | Every other chapter, every earlier report and frozen edition, the planning prompts that quote the old line, maps, ledger, continuity files, the acceptance table, `AUTHORSHIP.md`, every narration artifact (feedback, direction, performance JSON, clarity review, contexts), scripts and git state. No commit, push, publish or render. No Skill, Agent, subagent, other model or paid API. |

**Scope of claim.** This repair changes the text only. Nobody has listened to it, re-narrated it or rendered it, and the
narration validators have not been rerun. The narration source hash is now stale (see §5).

## 1. Freeze (before any edit)

`editions/audio-placement-37-pre-repair/` did not exist. I created it and copied the working file into it with `cp -p`.
The copy is read-only (444) and has a `SHA256SUMS.txt`. It verified `OK` before the edit and again after.

| File | Frozen (= accepted) | After this repair | Words (`wc -w`) | Bytes |
|---|---|---|---|---|
| `chapter-37.md` | `59097370d58d817dc2ee871f50ec004d5189dcbe4cc1e38ec8ff4a0e3fc7f7be` | `c39b066241dc7c1027d462ee855c59303805f5fd14eb0062ead5ee0f738afc21` | 6,629 → 6,629 (0) | 34,260 → 34,260 (0) |

Chain: accepted → `editions/audio-placement-37-pre-repair/` → current.

## 2. Change (exact)

There is one change: the two names in Pru's call exchanged places. Every other word, the italics, the attribution
(none; the call stands alone after the down) and the punctuation are unchanged.

| # | Ch:line (para) | Before | After |
|---|---|---|---|
| 1 | 37:229 (prose para 111, the second carry) | "\*Talley, head. Pryce, foot. Walk. North.\*" | "\*Pryce, head. Talley, foot. Walk. North.\*" |

`diff editions/audio-placement-37-pre-repair/chapter-37.md manuscript/chapter-37.md` shows only line 229.

## 3. Why the executed positions govern

Identities: Pryce is Anwen and Talley is Jude (`CHARACTERS.md` rows "Anwen Pryce", "Jude Talley"). The chapter agrees
at 37:149 ("*Pryce, ward. Talley, edge.*") and at 37:169–171, where "*Pryce, south. Talley, north*" is executed as
"Anwen's wall came up south. Jude went north".

The call was the only element in the chapter that put Jude on the head and Anwen on the foot. Four other passages put
them the other way round, and they agree with each other:

- **Pru's plan, 37:207.** "We carry on Pryce's hands and Talley's hand, the head and the foot". That is a respectively
  pairing: Pryce takes the head and Talley takes the foot. The call at 229 contradicted the caller's own plan.
- **The take, 37:231.** "Anwen had the head in her two good hands; Jude had the foot in his one."
- **Dray's approach, 37:235.** "He stood with the foot poles in his right hand and his left arm against his chest
  … in a count and a half Jude had walked the foot three paces."
- **The injury logic, 37:177 and 37:203.** Jude fights one-handed with his left arm held to his chest. Pru's counter
  is that he does not turn and Dray must go round to his right. That works because Jude holds one pair of poles in his
  one hand, on the foot, while Anwen's two hands take the head.

The positions also carry Dray's approach, the long way round, the count and a half and the hurdle transfer. Changing
any of them would redesign the action. Changing the call costs two words in place.

**Origin.** The slip is original. It is already in `editions/movement-005-first-draft/chapter-37.md:225` and
`editions/whole-book-pre-repair/chapter-37.md:229`, each time beside the same "Anwen had the head" sentence. No later
repair introduced it.

## 4. Preserved, and the joins

- **Preserved:**
  - Pru as the caller, and the call as an unattributed italic line with the same four sentences;
  - Anwen carrying the head in two hands, and Jude carrying the foot in one;
  - Jude's injury, with his left arm against his chest;
  - the north route along the posts, and *hands, south* with Anwen's wall;
  - Dray's approach to Jude's left, his not turning, her long way round to his right, the count and a half and the
    three paces;
  - the hurdle transfer onto Kiva's and Pru's crossed forearms;
  - the score ("*Three to Seven. A down. Four to four.*"), the roles, and everything after.
- **Join before (37:227 → 37:229).** 37:225 ends "Jude was there." and 37:227 is the marshal's "*Down.* Twenty-Eight.".
  The call follows with "*Pryce, head*" first. Anwen has just walked her wall round the still door, which had come for
  the head, so she is already at the head when she is named to it.
- **Join after (37:229 → 37:231).** 37:231 opens "Anwen and Jude had the Commodore. Anwen had the head …; Jude had the
  foot …". The names now come in the same order as the call (Pryce/Anwen, then Talley/Jude) and the assignments
  match, so a listener confirms the call instead of revising it.
- **Checks.** A quote-parity scan of the chapter finds no non-blank line with an odd number of `"` marks. The edit
  was applied as an exact-once replacement. The new line occurs exactly once. The frozen copy still verifies `OK`.

## 5. Next (not done here; not mine to do)

- **Acceptance.** Whoever holds the acceptance table should take the new chapter-37 hash
  (`c39b0662…`, 6,629 words, unchanged count) in place of `59097370…`.
- **Narration.** `chapter-37.performance.json` still names `sourceSha256` `59097370…`. The narration side must:
  - re-review paragraph 111 and both joins;
  - refresh the context, clarity review and direction against the new hash;
  - rerun both word-lock checks and the initialized-run validation before any ready marker.

  `narration/RECHECK-PLACEMENT-37.prompt.md` is already staged for that independent recheck. The word count and
  token order are unchanged; only the two names swap position.
- **Records.** No ledger, continuity file or map records this call. The planning prompts that quote the old line
  are historical prompt snapshots, so they were left as they are.
