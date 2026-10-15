# National Measure completion loop

Owner instruction: continue until book and complete local Breeze audio are published.

- Canonical prose: chapters 1–16, 107,866 words.
- Movement One: accepted after repair/recheck, 48,243 words.
- Movement Two: first draft, 59,623 words; editorial review `d012916b`, simulated
  manuscript-only cold read `e9132b0f` actively running.
- Next: consolidate reviews, freeze pre-repair edition, Opus repair/recheck, then
  Sonnet briefs and Opus drafts for movements 3–6.
- Published: source main `9a50b97`; PWA `2ccffda`, version 1.18.36, all 16 chapters
  verified byte-identical on deployed site.
- Audio: rolling chapters 1–3 run initialized under
  `narration/monroe-1.2.5/calder/chapters-01-03`. Owner selects Breeze with Original
  Calder; generated run's Fish renderer fields are defaults, not this run's choice.
  Codex performance bible, clarity review and direction are still pending. No Book
  Two audio has been rendered or published.
- Shared audio: Book One preparation directories exist at
  `/Users/drive/.local/share/monroe-tts/fractured-directors-run/kindling-2680-book-01-ch00`
  through `ch48`. The other session was interrupted. Do not overwrite its work or
  launch competing MLX workers. No Path Given remains intentionally stopped.
- Hourly supervisor: `finish-national-measure-text-and-breeze-audio`, ACTIVE.

## Update 2026-10-14 22:45 MDT — Sonnet 5.5 showrunner `8491a39c`

- Phase: Movement Two review. Cold read `e9132b0f` COMPLETE:
  `provenance/MOVEMENT-002-COLD-READ.md` (15,137 bytes; simulated, same model family,
  memory hook leaked series summaries; NOT human feedback). Verdict: continue; priorities:
  (1) thin tics/rituals (tied a knot x23, "I'd like it known" x11, van-slate x3, ch16 ledger read-out),
  (2) one-pass clarity (ward/plank/still-door vocabulary, ch10 slope chain, ch14 rung rule, Coombe lodger
  reversal, unsignalled POV under "Kiva:" titles), (3) ten small continuity slips + ch14 l.143 stray quote.
- Editorial review `d012916b` still working; output
  `provenance/MOVEMENT-002-EDITORIAL-REVIEW.md` not yet written.
- Next: consolidate (max 3 priorities), freeze `editions/movement-002-first-draft/`, same-author Opus repair,
  fresh Opus recheck, reconcile, commit/publish, then Movement 3 brief.

## Update 2026-10-14 22:58 MDT — Movement Two repair launched

- Editorial review `d012916b` DONE: `provenance/MOVEMENT-002-EDITORIAL-REVIEW.md`
  (sha256 35b1b39c…). Cold read sha256 9cf7724b…. Both simulated/same-family, not human.
- Consolidated three priorities: (1) continuity/physical-state line fixes; (2) one-pass clarity
  (door vocabulary, slope chain, rung rule, POV anchoring) plus narration sentence reshaping toward
  the mid band, dialogue untouched; (3) thin tics (knots, "I'd like it known", van-slate, ch16 ledger,
  duplicate share explanation).
- Frozen read-only edition `editions/movement-002-first-draft/` (SHA256SUMS.txt; matches commit 9a50b97).
- Repair prompt `planning/OPUS-5.5-MOVEMENT-002-REPAIR.prompt.md` sha256
  fbd07ebfebb72d9e9e73a58eac3a22195ca128266fb69f955a72a9b4793c73b1.
- ACTIVE CHILD: Opus 5.5 repair job `80479656` (launcher `scripts/nm-launch.sh`; EnterWorktree/Agent/Workflow disabled).
  Output: manuscript/chapter-09..16.md, `provenance/MOVEMENT-002-REPAIR.md`.
- Next: on completion, fresh-context Opus recheck of defects + changed joins only; then reconcile,
  commit, publish M2 to PWA, then Movement 3 brief (entry state from repaired M2 + ledger).
- Owner-decision items recorded (not blocking): dialogue vs sentence targets; front-load arithmetic;
  plan six-crossing calendar (prose says four); Order binding of plain ash; lodger on two unlike doors.

## Update 2026-10-14 23:15 MDT — Movement Two repaired; recheck running

- Repair job `80479656` DONE (runtime-reported claude-opus-5-5). Record `provenance/MOVEMENT-002-REPAIR.md`
  (17 factual fixes F1–F17; clarity edits; ~100 narration splits, ~15 joins; knots 21→7; "I'd like it known"
  all Perrin; ch14/16 readouts thinned). Words 59,623 → 59,234. Formula measures NOT reached (narration median 7,
  short share 41.4%); recorded honestly; long tail 4.6%→3.6%. Frozen edition verified OK (SHA256SUMS).
- Left for owner/M3: whether a sanctioned mast read Perrin+Anwen's unlike-door pair at the ch13 license floor.
- ACTIVE CHILD: fresh-context recheck `7508774e` (prompt sha256 31b54076…); output
  `provenance/MOVEMENT-002-RECHECK.md`. Pre-recheck manuscript hashes saved in job tmp.
- Next: on recheck PASS (or one bounded defect fix), commit M2 repaired (stage only my paths), push source,
  publish ch 9–16 repaired to PWA, write Movement 3 packet and compile prompt.
