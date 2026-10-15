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

## Update 2026-10-14 23:45 MDT — Movement Two CLOSED and published; Movement Three drafting

- M2 recheck `7508774e` found one defect (ch16 l.135); fixed by resumed repair author `fdbd4fb4` (3 edits).
  Accepted as editorial context: `provenance/MOVEMENT-002-RECHECK-CONFIRMATION.md` (final hashes). 59,234 words.
- Source: kindling main `1a2dc08` (ff from 9a50b97, includes Codex's cfddb02). Frozen
  `editions/movement-002-first-draft/` committed.
- PWA: boundary-universe main `96c9162`, version 1.18.37, sw-v1213; all 16 chapters verified
  byte-identical on books.worker-bee.app (repaired ch 9–16 live).
- Reusable tools: `scripts/nm-launch.sh`, `scripts/nm-publish-pwa.py` (not yet committed).
- ACTIVE CHILD: Movement Three author `21a609b3` (Opus 5.5), prompt
  `planning/OPUS-5.5-MOVEMENT-003.prompt.md` sha256 902d5abb…d3d6b8, packet `packets/MOVEMENT-003.md`.
  Writes ch 17–24 + `provenance/MOVEMENT-003-CONTINUITY.md`; checkpoint file if output-limited:
  `provenance/MOVEMENT-003-CHECKPOINT.md`.
- Audio: untouched by this loop; accepted stable text/hash for ch 1–16 is the table in the
  confirmation file (ch 1–8 per MOVEMENT-001-RECHECK-CONFIRMATION). Breeze/Calder work belongs to Codex.
- Blockers: none.
- Next: when M3 lands: parallel informed editorial+formula review and fresh cold read; consolidate; freeze;
  same-author repair; fresh recheck; publish; then Movement 4 brief from surviving prose.

## Update 2026-10-15 00:25 MDT — Movement Three drafted; reviews running

- M3 author job `21a609b3` DONE (runtime-reported claude-opus-5-5): ch 17–24, 54,482 words, no output-limit
  interruption. Kiva 82.5%, cutaways 17.5% (Anwen, Orla, Rhea, Mara, Kellan). Frozen read-only
  `editions/movement-003-first-draft/` (hashes match author's record).
- ACTIVE CHILDREN: informed editorial+formula review `b4e11087` (-> `provenance/MOVEMENT-003-EDITORIAL-REVIEW.md`,
  script `provenance/tools/m3_metrics.py`); manuscript-only cold read `884bf82e`
  (-> `provenance/MOVEMENT-003-COLD-READ.md`). Prompts: planning/OPUS-5.5-MOVEMENT-003-{EDITORIAL-REVIEW,COLD-READ}.prompt.md.
- Publishing M3 first draft to PWA labeled draft (chapters 1–24), then supervising reviews.
- Next: consolidate (max 3), repair prompt, same-author repair, fresh recheck, publish repaired, then Movement 4 brief.

## Update 2026-10-15 00:50 MDT — Movement Three reviewed; repair running

- Published to PWA: ch 1–24, version 1.18.38, sw-v1214, PWA main f660d7d; ch 17–24 labeled "first draft awaiting review";
  all 24 chapters byte-identical to source on books.worker-bee.app. Source main f529390 (+ local 5d8f25d review artifacts).
- Reviews DONE: editorial `b4e11087` (`provenance/MOVEMENT-003-EDITORIAL-REVIEW.md`), cold read `884bf82e`
  (`provenance/MOVEMENT-003-COLD-READ.md`). Both simulated/same-family.
- Consolidated: P1 numbers/clock/logic line fixes (lane-2 tally, litter rule, nights, bag count 7, timestamps, Bench);
  P2 scene-structure (remove 15–20 intra-scene breaks), sentence contrast (over-corrected: >=40 share 0.4%), footholds;
  P3 distinct voices ("I'd want" 28 -> Jude/Anwen only; said nothing; scarlet; since).
- ACTIVE CHILD: M3 repair `8e3ee375` (prompt planning/OPUS-5.5-MOVEMENT-003-REPAIR.prompt.md sha256 c0ca2755…80fb).
  Output `provenance/MOVEMENT-003-REPAIR.md`. Pre-repair manuscript hashes in job tmp.
- Owner items logged: dialogue vs sentence targets; front-load arithmetic; harbour tide clock (slack moves 1 min/day);
  Graving seeding floor and slate template accepted as departures; BOOK_MAP s12 Rhea-short moved to M3.
- Next: fresh recheck -> publish repaired -> Movement 4 brief.

## Update 2026-10-15 01:35 MDT — Movement Three CLOSED and published; Movement Four drafting

- M3 repair `8e3ee375` (20 factual fixes F1–F20; 20 intra-scene breaks removed: internal breaks 14.5→10.8/10k;
  voice tics halved) → recheck `a495af2f` found one defect (ch23:195 referent) → second repair `ca51c377`
  (one sentence). Accepted as editorial context: `provenance/MOVEMENT-003-RECHECK-CONFIRMATION.md`
  (final hashes). 54,611 words. Sentence-rhythm waypoint NOT reached (recorded; owner item).
- Source: kindling main `6c8b684`. PWA: boundary-universe main `521e59a`, version 1.18.39, sw-v1215;
  chapters 1–24 verified byte-identical on books.worker-bee.app.
- ACTIVE CHILD: Movement Four author `9f1bbf7e` (Opus 5.5), prompt `planning/OPUS-5.5-MOVEMENT-004.prompt.md`
  sha256 24f6ecfe…6224, packet `packets/MOVEMENT-004.md` (chapters 25–32: Bench w/o Kiva, Perrin's Carry,
  the Longshore Hunt, a Company catcher's death, handed crossing live, Seven ninth). Checkpoint if limited:
  `provenance/MOVEMENT-004-CHECKPOINT.md`.
- Audio: accepted stable text for ch 1–24 listed in the confirmation files (ch 1–8 per
  MOVEMENT-001-RECHECK-CONFIRMATION). Codex/Breeze work untouched by this loop.
- Blockers: none.
- Next: M4 informed editorial + cold read in parallel -> consolidate -> repair -> recheck -> publish -> M5 brief.

## Update 2026-10-15 03:05 MDT — Movement Four CLOSED and published; Movement Five drafting

- M4: draft `9f1bbf7e` (52,401) -> editorial `28d8a21c` + cold read `b4360b6b` -> repair `647704f1` (18 factual
  fixes incl. Bench re-ranking so Seven stays 9th; clarity; catchphrase thinning; ch32 fold; 52,203 words) -> fresh
  recheck `e6a7d3ad` PASS, no prose defect (4 stale record lines fixed by showrunner). Accepted as context:
  `provenance/MOVEMENT-004-RECHECK-CONFIRMATION.md` (final hashes).
- Source: kindling main `2ce5e33`. PWA: boundary-universe main `eefb645`, version 1.18.41, sw-v1217;
  chapters 1–32 repaired, byte-identical on books.worker-bee.app.
- ACTIVE CHILD: Movement Five author `dd002b97` (Opus 5.5), prompt `planning/OPUS-5.5-MOVEMENT-005.prompt.md`
  sha256 51978fba…e905, packet `packets/MOVEMENT-005.md` (chapters 33–40: the Lane, Charter Board hearing,
  Kiva puts the dream on a table, two Glory masters, "Unroofed Sky" coined, Seven seventh by one mark).
  Checkpoint if limited: `provenance/MOVEMENT-005-CHECKPOINT.md`.
- Blockers: none. Owner items accumulating (dialogue vs sentence targets; front-load arithmetic; Penhale's ward
  frost-shape; M3 open items) -- recorded in confirmation files, not blocking.
- Next: M5 reviews -> repair -> recheck -> publish -> M6 brief (the Slack) -> whole-book review.

## Update 2026-10-15 04:10 MDT — Movement Five drafted & published as draft; reviews running; concurrent audio activity

- M5 draft `dd002b97` DONE (55,218 words, chapters 33–40; Kiva 87.0%; frozen `editions/movement-005-first-draft/`).
  Source kindling main `f23455c`. PWA boundary-universe main `4c3fc60`, version 1.18.42, sw-v1218; chapters 1–40
  live and byte-identical to committed source; 33–40 labeled "first draft awaiting review".
- ACTIVE CHILDREN: M5 informed editorial+formula review `887082aa` (-> `provenance/MOVEMENT-005-EDITORIAL-REVIEW.md`);
  M5 manuscript-only cold read `165093a7` (-> `provenance/MOVEMENT-005-COLD-READ.md`).
- COMPETING/CONCURRENT RUN (recorded, not interfered with): the audio supervisor (Codex) commissioned Opus 5.5 job
  `9ab8514b` "Audio Clarity 8–9" (`planning/OPUS-AUDIO-CLARITY-08-09.prompt.md`), which made eight word-level fixes in
  chapters 8 and 9 (record `provenance/AUDIO-CLARITY-08-09-REPAIR.md`, frozen `editions/audio-clarity-08-09-pre-repair/`).
  Showrunner verified hashes, committed exactly those files, and published them. NEW STABLE HASHES: ch 8
  `2cf6a109…`, ch 9 `3a2316f2…` (supersede the Movement One/Two confirmation tables for these files). Audio worktree
  commits (`a300d0e`, `2c0c73b`) and audio-candidate pushes (`6782bb0`, `7adae03`; PWA `3453a07`, `ac78391`) are the audio
  session's; main was merged, never forced.
- Publish helper now reads committed bytes (git show HEAD:) so another session's uncommitted edits never publish.
- Blockers: none.
- Next: consolidate M5 reviews -> repair -> recheck -> publish -> M6 brief (the Slack) -> M6 -> whole-book review.
