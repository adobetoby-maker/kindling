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
