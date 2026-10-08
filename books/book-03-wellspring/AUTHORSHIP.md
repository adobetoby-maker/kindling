# Wellspring (Kindled Book Three) — authorship record

Public byline: **Monroe Jackson**

## Movement One — Winter Line

- Status: **drafted (chapters 1–8); editorial review and simulated cold read done;
  one consolidated same-author repair complete; targeted recheck passed (2026-10-08).**
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment. Every manuscript sentence was written by this model in
  one authoring session. The session was resumed once after the harness process
  restarted, with the same model and context carried forward. No other model wrote or
  revised prose.
- Research assistance, disclosed: one read-only subagent (general-purpose type)
  compiled a canon digest of *Meridian* chapters 1–48 and continuity notes M1–M5
  (`/tmp/meridian-canon-digest.md`, outside the repo). It wrote no manuscript prose and
  edited no project files. Its model was the harness default and was not separately
  verified.
- Provider: Anthropic, via Claude Code (Agent SDK harness)
- Movement packet: `packets/MOVEMENT-001.md`
  (SHA-256 `8650096ce94d4f82cb6c258276b16d026ca90fc3a54c2a9497c15334225e1b33`)
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-001.prompt.md`
  (SHA-256 `dbc991300fbef92e0e901ce3ec5e6b0af346c1ad55f4b505a1b4c58c062e776f`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`,
  verified before drafting and again at the end of the run.
- Edition: Book Three, Movement One, first draft (2026-10-08)
- Manuscript: `manuscript/chapter-01.md` through `manuscript/chapter-08.md`
- Continuity checkpoint: `provenance/MOVEMENT-001-CONTINUITY.md`

### Viewpoints and length

| Ch | Heading | POV | Days | Words (`wc -w`) |
|---|---|---|---|---:|
| 1 | Somebody Else's Number | Callie | D+61–62 | 5,915 |
| 2 | Where Before How | Jab | D+62–65 | 7,343 |
| 3 | Whoever Can See Both | Toren | D+65–67 | 6,586 |
| 4 | What Katori Held | Callie | D+66–68 | 7,369 |
| 5 | Finite | Jab | D+70–77 | 7,240 |
| 6 | Summer Oil | Toren | D+78–79 | 5,809 |
| 7 | The Wrong Dark | Ensemble (company camera) | D+79 night | 10,198 |
| 8 | What One Night Costs | Ensemble (Toren / Callie / Jab settles) | D+80–85 | 6,482 |
| **Total** | | | | **56,942** |

- Co-protagonists are near-even by design. Each lead has two single-POV chapters,
  and the two ensemble chapters give each a sustained section. This follows the
  project's owner-approved override of the seat's default 87/13 single-lead allocation.
- **Length is above the book map's implied ~47,500–53,300 words per movement.** No
  scene was padded and none was compressed to fit. The set piece (ch 7) is the longest
  chapter by choice.
- No per-chapter editing, scoring or approval gates were run. Target-versus-observed
  comparison against the formula belongs to the movement editorial pass.

Codex orchestrates the run and repository work. Codex does not substitute itself as
the prose author.

## Movement One — consolidated same-author repair

- Status: **complete; targeted recheck passed.** Movement Two not begun.
- Targeted recheck: `editor/MOVEMENT-001-TARGETED-RECHECK.md`
- Prompt: `editor/MOVEMENT-001-REPAIR.prompt.md`
- Report: `editor/MOVEMENT-001-REPAIR-REPORT.md`
- Reviews acted on: `editor/MOVEMENT-001-EDITORIAL.md` (fresh-session, same-model
  editorial and formula review) and `editor/MOVEMENT-001-COLD-READ.md` (simulated cold
  read by a model). **No human reader or human test has been run.**
- Model that actually made the repair: **Claude Opus 5.5 (`claude-opus-5-5`)**, the same
  selected author and seat, continuing the drafting session. No subagents and no other
  model were used in the repair.
- Pre-repair edition (frozen, untouched): `editions/movement-001-pre-repair/manuscript/`
  (checksums in `editions/movement-001-pre-repair/SHA256SUMS.txt`).
- Scope: the three repair priorities only.
  1. Hard canon and arithmetic: the one-configuration rule at the far gap, the lantern
     beat, the ash ledger, the roster, and dates and clocks.
  2. Read-aloud orientation in Chapter 7, plus local thinning of clustered tics and
     restated lessons.
  3. Records.
  No scene was added or cut, and the set piece was not shortened.
- Style exception recorded, per the repair decision: the movement keeps the house's plain,
  short-sentence audiobook voice. The measured sentence-length and readability deviation
  from the numerical formula (editorial §5, F1) is accepted for this movement. It was not
  forced toward the targets.

| Ch | Words before | Words after |
|---|---:|---:|
| 1 | 5,915 | 5,912 |
| 2 | 7,343 | 7,361 |
| 3 | 6,586 | 6,579 |
| 4 | 7,369 | 7,362 |
| 5 | 7,240 | 7,246 |
| 6 | 5,809 | 5,815 |
| 7 | 10,198 | 10,720 |
| 8 | 6,482 | 6,466 |
| **Total** | **56,942** | **57,461** |

## Movement Two — The Spring Review

- Status: **drafted (chapters 9–16), first draft, 2026-10-08.** Stopped for movement
  review. No editorial pass, cold read, recheck or repair has been run on this movement.
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment. Every manuscript sentence in chapters 9–16 was written by
  this model in one authoring session, in chapter order, with no per-chapter editing,
  scoring or approval gates. During and after the run the same model made a small set
  of blocking continuity corrections (dates, who said a rule, two invented proper
  names replaced with role descriptions, italics removed from post-action dialogue in
  ch 15). No subagents were used. No other model wrote or revised prose.
- Research inputs, disclosed: Movement One manuscript (chs 1–8, repaired edition), its
  continuity checkpoint, `BOOK_MAP.md`, `CHARACTERS.md`, `STATE_LEDGER.md`,
  `universe/UNIVERSE_BIBLE.md` and `universe/NAME_REGISTRY.md`, and the read-only
  *Meridian* canon digest compiled for Movement One (`/tmp/meridian-canon-digest.md`,
  outside the repo).
- Provider: Anthropic, via Claude Code (background session)
- Movement packet: `packets/MOVEMENT-002.md`
  (SHA-256 `e5a2290b9accad8082b47878e1ccbfc08955b3370baec032145546bf68c44824`)
- Compiled prompt: `planning/OPUS-5.5-MOVEMENT-002.prompt.md`
  (SHA-256 `fa0e6cbe1739d0667182d3f5cd5a8a6dced8aa2295843c30da054ee1cb5a4251`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`,
  verified before drafting.
- Edition: Book Three, Movement Two, first draft (2026-10-08)
- Manuscript: `manuscript/chapter-09.md` through `manuscript/chapter-16.md`
- Continuity checkpoint: `provenance/MOVEMENT-002-CONTINUITY.md`
- Workspace note: drafted in the git worktree branch `worktree-wellspring-m2` because the
  background session required isolation; `books/book-03-wellspring/` is untracked on
  `main`, so these files must be copied into the main checkout to sit beside Movement One.

### Viewpoints and length

| Ch | Heading | POV | Days | Words (`wc -w`) |
|---|---|---|---|---:|
| 9 | Names on the Card | Toren | D+93–101 | 7,393 |
| 10 | The Line She Reads | Callie | D+97–104 | 7,318 |
| 11 | Not Both | Jab | D+102–106 | 7,742 |
| 12 | The Assumed Line | Toren | D+106–114 | 6,976 |
| 13 | Households | Callie | D+111–114 | 5,622 |
| 14 | The Shadow Side | Ensemble (company camera) | D+115 | 6,504 |
| 15 | Lit Before Dark | Ensemble, Jab-led (rescue cuts to Callie/Toren; aftermath Jab) | D+115 | 7,728 |
| 16 | The Spring Review | Ensemble (Callie / Toren / Jab settles) | D+117–118 | 6,359 |
| **Total** | | | | **55,642** |

- Co-protagonists are near-even by design (owner-approved override of the seat's
  default 87/13). Jab's single-POV chapter share is lower this movement; ch 15 carries
  him. See the continuity checkpoint's flags.
- **Length is above the book map's implied ~47,500–53,300 words per movement.** No scene
  was padded and none was compressed to fit. The set piece spans chs 14–15.
- Packet interpretation recorded: the brief's "Mara's equivalent adult stakeholders" was
  read as the learners' guardians and reviewed households (the registry's Mara Rowan is a
  2680 character). The girl in mittens remains unnamed; no other new character is named.
- Target-versus-observed comparison against the formula belongs to the movement
  editorial pass. A heuristic observation is recorded in the checkpoint (flag 6) only so
  the review starts from numbers, not as a score.

Codex orchestrates the run and repository work. Codex does not substitute itself as
the prose author.
