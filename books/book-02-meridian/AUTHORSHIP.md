# Meridian — authorship record

Public byline: **Monroe Jackson**

## Movement One — Three Roads, One Wall

- Status: **drafted (chapters 1–8); cold read and editorial review done; consolidated same-author repair complete (2026-09-27)**
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**,
  one continuous run, no subagents, no other model substituted
- Provider: Anthropic subscription CLI (`claude.ai`, Max plan)
- Movement packet: `packets/MOVEMENT-001.md`
- Compiled prompt: `editor/MOVEMENT-001-OPUS-5-5.prompt.md`
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`
  (hash re-verified at the end of the run)
- Edition: Book Two, Movement One, first draft (2026-09-27)
- Manuscript: `manuscript/chapter-01.md` through `manuscript/chapter-08.md`
- Drafted length: 39,700 words (above the packet's approximate
  28,000–36,000 range; no scene was compressed to fit)
- Source manifest: `SOURCE_POOL.md`
- Continuity checkpoint: `provenance/MOVEMENT-001-CONTINUITY.md`

No per-chapter editing, scoring, or approval gates were run. Target-versus-observed
comparison against the formula belongs to the movement editorial pass.

Codex orchestrates the run and repository work. Codex does not substitute
itself as the prose author.

## Movement One — consolidated same-author repair

- Status: **complete**
- Prompt: `editor/MOVEMENT-001-REPAIR.prompt.md`
- Report: `editor/MOVEMENT-001-REPAIR-REPORT.md`
- Model that actually made the repair: **Claude Opus 5.5 (`claude-opus-5-5`)**, the same selected author and seat. One session, no subagents, no substitute model.
- Scope:
  - line-level continuity and object-state fixes
  - narration cadence widening
  - adult-register separation
- No scenes were added or cut.
- The frozen first draft is at `editions/movement-001-first-draft/`.
- No human cold read has been run.

## Movement Two — The North Yard

- Status: **drafted, reviewed, repaired, and accepted (chapters 9–16; 2026-09-27)**
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment. It was one continuous session, and every manuscript
  sentence was written in it. No other model wrote or revised prose.
- Research assistance, disclosed: three read-only subagents (general-purpose type)
  extracted Book One facts with quotations. They covered the Callie, Jab and Toren
  strands of `book-01-kindled/revised/` and the Callie source pool. They wrote no
  manuscript prose and edited no files. Their model was the harness default and was
  not separately verified.
- Provider: Anthropic, via Claude Code (Agent SDK harness)
- Movement packet: `packets/MOVEMENT-002.md`
  (SHA-256 `889741435405b24b682c8a5bafe3721db5ead08bef23ee15eadf786e454c5e01`)
- Compiled prompt: `editor/MOVEMENT-002-OPUS-5-5.prompt.md`
  (SHA-256 `8dcf7d0cc3ffe9b851cd249df83a0955e5531acbbf64deaf36171091408ea261`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`,
  verified before drafting and again at the end of the run.
- Edition: Book Two, Movement Two, first draft (2026-09-27)
- Manuscript: `manuscript/chapter-09.md` through `manuscript/chapter-16.md`
- Viewpoints:

  | Chapters | POV |
  |---|---|
  | 9, 12, 14 | Toren |
  | 10, 13, 16 | Callie |
  | 11, 15 | Jab |

  Each chapter has a single viewpoint.
- Drafted length: 62,793 words (wc). That is above the packet's approximate
  48,000–55,000. No scene was padded, and none was compressed to fit.
- Continuity checkpoint: `provenance/MOVEMENT-002-CONTINUITY.md`. It holds:
  - the conflicts resolved
  - the day map
  - how the Sag-line failure was staged
  - object state, open clocks, and bodies at exit
  - withheld material
  - facts on viewpoint share

No per-chapter editing, scoring, or approval gates were run. The connected first
draft was followed by one cold read, one canon/formula editorial read, and one
consolidated same-author repair. The post-repair targeted recheck accepted all eight
questions without requesting another manuscript change. No human cold read has
been run.

The frozen pre-review edition is at `editions/movement-002-first-draft/`.

## Movement Two — consolidated same-author repair

- Status: **complete; targeted recheck verdict `repair accepted`**
- Prompt: `editor/MOVEMENT-002-REPAIR.prompt.md`
- Report: `editor/MOVEMENT-002-REPAIR-REPORT.md`
- Recheck: `editor/MOVEMENT-002-RECHECK.md`
- Model that actually made the repair: **Claude Opus 5.5
  (`claude-opus-5-5`)**, the same selected author and seat, in one session with
  prose subagents disabled.
- Recheck model: **Claude Opus 5.5 (`claude-opus-5-5`)**, fresh context,
  read-only against the manuscript. This is a same-model simulated editorial
  check, not an independent human read.
- Repaired length: **63,115 words** (`wc -w`), net +322 words.
- Repair scope:
  - made the minute-20 Sag handover decision explicit;
  - made Toren's uncalled sighting an owned failure and corrected the ledger;
  - repaired day counts and Dee's Homura training age;
  - reduced repeated Dee epithets and surface tics while preserving the fight;
  - modestly widened narration cadence without flattening impact beats.
- Owner-level historical conflicts left explicit: Wyck's injured side/finger
  count, the single-account wording for Toren's original arm break, and Tonk's
  six-versus-ten-week estimate.

Codex orchestrates the run and repository work. Codex does not substitute
itself as the prose author.

## Movement Three — Working Depth

- Status: **drafted, reviewed, repaired, and accepted (chapters 17–24; 2026-09-27)**
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment. It was one continuous session, and every manuscript
  sentence was written in it. No subagents were used for research or prose. No other
  model wrote or revised prose.
- Provider: Anthropic, via Claude Code (Agent SDK harness)
- Movement packet: `packets/MOVEMENT-003.md`
  (SHA-256 `8d11635023e3fe82e6beb04316f87826bc7e84219c8295108548733a9fd851d5`)
- Compiled prompt: `editor/MOVEMENT-003-OPUS-5-5.prompt.md`
  (SHA-256 `c524ee50407666b3eb69dce0fac713859342b67536d6c6e50ee03d4a108a41c9`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`,
  verified before drafting and again at the end of the run.
- Edition: Book Two, Movement Three, first draft (2026-09-27)
- Manuscript: `manuscript/chapter-17.md` through `manuscript/chapter-24.md`
- Viewpoints:

  | Chapters | POV |
  |---|---|
  | 17, 20, 22 | Jab |
  | 18, 21, 24 | Toren |
  | 19, 23 | Callie |

  Each chapter has a single viewpoint.
- Drafted length: **64,254 words** (`wc -w`). That is above the packet's approximate
  46,000–52,000, by about 24% over the upper bound. No scene was padded, and none
  was compressed to fit.
- Continuity checkpoint: `provenance/MOVEMENT-003-CONTINUITY.md`. It records:
  - the author choices that are now canon, including the ash ratio, the recall
    mechanics and the Director's conditions;
  - the day map and the pen emergency as staged;
  - the ledger, Jab's terms, object state, open clocks and bodies at exit;
  - withheld material and facts on length and viewpoint.
- Pre-drafting plan (superseded by the checkpoint):
  `provenance/MOVEMENT-003-WORKING-PLAN.md`.
- Frozen first draft: `editions/movement-003-first-draft/`, hash-checked against the
  manuscript at the end of the run.

No per-chapter editing, scoring, or approval gates were run. During the run the author
corrected only blocking internal contradictions: the calendar, the store arithmetic,
Dee's Homura duration, settling times, and one week-count that would have touched an
owner-level conflict. Target-versus-observed comparison against the formula belongs to
the movement editorial pass. No human cold read has been run.

The connected draft was followed by one simulated cold read, one canon/formula
editorial review, and one consolidated same-author repair. A fresh-context targeted
recheck passed seven questions and found one remaining departure-knowledge clause;
that clause alone was removed, after which the verdict was recorded as
`repair accepted`. The final repaired length is **64,988 words** (`wc -w`), net +734
words from the frozen first draft.

## Movement Three — consolidated same-author repair

- Status: **complete; targeted recheck verdict `repair accepted`**
- Cold read: `editor/MOVEMENT-003-COLD-READ.md`
- Editorial review: `editor/MOVEMENT-003-EDITORIAL-REVIEW.md`
- Repair prompt: `editor/MOVEMENT-003-REPAIR.prompt.md`
- Repair report: `editor/MOVEMENT-003-REPAIR-REPORT.md`
- Recheck: `editor/MOVEMENT-003-RECHECK.md`
- Model that actually made the substantive repair: **Claude Opus 5.5
  (`claude-opus-5-5`)**, the selected author, in one session with prose subagents
  disabled.
- Review disclosure: both reviews and the targeted recheck used Claude Opus 5.5 in
  fresh contexts. They are same-model simulated editorial reads, not independent
  human cold reads.
- Repair scope: pen geometry, red-call accountability, ash accounting and abort
  arithmetic, day/count corrections, departure staging, and a restrained read-aloud
  repetition pass. Narration cadence already matched the selected distribution and
  was not broadly rewritten.
- Final targeted correction: removed Dessa's unsupported claim that the Sag had been
  quiet since the fifth hour; no replacement prose or other manuscript change was
  introduced at recheck.

Codex orchestrates the run and repository work. Codex does not substitute
itself as the prose author.
