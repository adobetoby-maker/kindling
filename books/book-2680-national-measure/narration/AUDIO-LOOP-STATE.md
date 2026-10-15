# National Measure — local Breeze audio loop

## Current phase

Book context preparation for the sixteen accepted chapters. The book remains in
progress; refresh context when later accepted movements land.

- Started the existing `build-book-performance-bible.py` with the complete
  currently available chapters 1–16 and local `qwen3.5:35b-a3b-q4_K_M`.
- This local model creates context summaries and a provisional bible. It is not
  the final performance director. Codex must inspect the bible, read the selected
  three-chapter window, complete the paragraph clarity pass, and direct the score.
- Running command: `python3 -u /Users/drive/kindling-narrator-stage/scripts/build-book-performance-bible.py books/book-2680-national-measure/manuscript books/book-2680-national-measure/narration/performance-bible --model qwen3.5:35b-a3b-q4_K_M --title 'The National Measure' --audience adult`.
- Shell session at launch: `29401`; inspect the actual process and summary files
  before resuming. Summaries are checkpointed by chapter source hash.
- Output directory: `narration/performance-bible/`.
- Follow with `write-book-performance-contexts.py` to create the rolling chapter
  context files. Read and verify their contents against accepted prose before use.
- First narration unit: `monroe-1.2.5/calder/chapters-01-03/run.json`.
- Renderer override: `monroe-1.2.5/calder/chapters-01-03/BREEZE-OVERRIDE.md`.
- Model: local `mlx-community/Breeze-TTS-2-mlx-8bit`; Original Calder clone.
- No Book Two audio rendered yet. No performance-ready marker is authorized until
  Codex's clarity and direction artifacts exist and pass source word-lock checks.

## Shared resources

No Breeze/Fish renderer was running at context-preparation launch. Book One has
preparation directories and four saved prologue segment WAVs. Preserve them.
No Path Given remains deliberately stopped. Do not run a competing MLX renderer.
The local context model is using Metal; unload it after context preparation before
loading the Breeze renderer, so the two jobs do not contend for shared memory.

## Next action

Finish and validate the provisional bible; create contexts; Codex-read and direct
chapters 1–3; compile Breeze segment tracks with silent thought boundaries and
brief edge fades; render checkpointed audio and run technical/coverage checks;
publish each listening candidate to kindling and the PWA. Continue through the
accepted manuscript in rolling three-chapter units as writing progresses.

## Immediate publication loop — 2026-10-15

- Owner reiterated: publish audio immediately after each chapter is ready.
- Context builder completed successfully. The provisional sixteen-chapter bible
  and `narration/contexts/chapter-01.context.md` through chapter 16 are present.
- Codex full-unit clarity/direction task active: prompt
  `narration/DIRECT-OPENING-UNIT.prompt.md`, result
  `narration/DIRECT-OPENING-UNIT.result.md`; shell session `53043`, runtime reported
  `gpt-6.1-sol`, CLI PID 91827 at launch. Rediscover actual process before resuming.
- Render/publish worker active: `scripts/nm-breeze-audio.py`, shell session
  `78406`, PID 12344 at launch. It waits for Codex's word-locked direction.ready
  markers; synthesizes one chapter at a time; adds 5ms zero-edge fades to the
  assembled joins; encodes/decodes; uploads proper Git LFS media to kindling;
  updates the PWA kindling manifest immediately, with no full-book wait.
- Source/PWA publication uses per-file GitHub SHA checks and retry, leaving
  authoring worktrees and other voices untouched. No force updates.
- Each `published.json` records hashes, duration, technical checks and the PWA
  commit. Initial state is pushed-awaiting-live-verification. The supervising
  heartbeat must verify live manifest/audio and record that result.
- No ready audio existed at this update. First three-chapter direction is still
  in progress. Later accepted units remain queued for Codex preparation.

## Heartbeat — opening unit rendering

- Codex opening-unit task completed. All 697 prose paragraphs across chapters
  1–3 were reviewed; per-chapter word-lock, clarity coverage and harness validation
  passed. Inspect `DIRECT-OPENING-UNIT.result.md` and each chapter's
  `preparation-review.json` for exact evidence. One nonblocking headcount query is
  recorded for Writing Monroe; it did not require a spoken-text change.
- The one Breeze worker is actively synthesizing chapter 1. Last checked checkpoint
  was `chapter-01/breeze-directed/s012.wav`; render process PID 25944, supervising
  worker PID 12344. Rediscover rather than trusting those PIDs indefinitely.
- Chapters 2 and 3 have validated direction.ready markers and will follow without
  another owner instruction. No complete chapter recording is published yet.
- The next Codex unit, chapters 4–6, was initialized and launched as shell session
  `97456`; prompt `DIRECT-UNIT-04-06.prompt.md`, result
  `DIRECT-UNIT-04-06.result.md`. It prepares text/direction only and preserves the
  first unit and active render. Check it before launching more preparation.
- Writing showrunner and Movement Three repair are healthy. No intervention or
  duplicate writing/audio worker is required.

## Heartbeat — chapter 1 progressing; next units prepared

- The chapter 1 renderer remains healthy: 181/241 segment WAV checkpoints were
  present at inspection. One worker and one renderer; no complete MP3 yet.
- Chapters 4–6 finished Codex preparation. Independent harness validation passed
  for all 746 paragraph reviews, complete source word locks, and zero blockers.
  They are queued behind chapters 1–3 without a separate owner instruction.
- Chapters 7–9 are now being read/directed: prompt
  `DIRECT-UNIT-07-09.prompt.md`, result `DIRECT-UNIT-07-09.result.md`, shell session
  `66924`. Check this process before launching the next preparation unit.
- Writing: Movement Three is repaired/rechecked and published, bringing accepted
  text to chapters 1–24. Opus Movement Four drafting job `9f1bbf7e` is active under
  Sonnet showrunner `8491a39c`; no duplication or intervention is needed.

## Heartbeat — first chapter uploaded; publication repair

- Chapter 1 rendered: 241 segments, 2,518.7 seconds (41m 58.7s), approximately
  140.57 spoken words/minute. Input word-lock and full MP3 decode passed; peak
  0.98859; 5ms edge fades. Owner/perceptual listen remains pending.
- Upload initially failed because `git lfs clean` accepts a positional path,
  not `--filename`. Fixed the worker and uploaded the existing MP3 without
  regenerating it. Source/audio hashes match the review. The 30,225,357-byte
  public GitHub LFS media download was verified in full against SHA-256
  `1e2564541848a7bfbab01a6bb1cb3a502c34084808e05778e74c3171616dba27`.
- PWA manifest publication commit `3453a07663d160d1fb675dedb37620b619755d7c` is
  deploying. Verify live manifest before notifying first audio availability.
- Preserved the active chapter 2 renderer when replacing only its supervisor.
  New worker PID 29640, shell session 46110; chapter 2 renderer PID 97270.
- Chapter 7 is prepared. Chapters 8–9 are held for located wording issues;
  surgical Opus repair `9ab8514b` is active, prompt
  `planning/OPUS-AUDIO-CLARITY-08-09.prompt.md`. Report expected at
  `provenance/AUDIO-CLARITY-08-09-REPAIR.md`. Verify report/joins, publish exact
  repaired source, refresh prepared hashes and Codex recheck before readiness.
- Chapters 10–12 Codex preparation is active, shell session 53555, prompt
  `DIRECT-UNIT-10-12.prompt.md`, result `DIRECT-UNIT-10-12.result.md`.

### First chapter live

PWA deployments for `3453a07` succeeded. The live kindling manifest now lists
Book Two chapter 1 with exact source/audio hashes. Full LFS audio HTTP 200 and
SHA-256 passed, and byte-range playback returned HTTP 206. Duration: 41m 58.7s.
`published.json` now records live verification. Notify first availability once;
subsequent healthy render progress should remain quiet. Owner listening pending.

## Heartbeat — chapter 2 live; targeted clarity rechecks

- Chapter 2 uploaded automatically and is live: 2,464.4 seconds (41m 4.4s),
  29,573,901 bytes. Live manifest and full media download SHA-256 verified as
  `b26e0387a6aba44143a73157da0d9c7f6dd59d161212f79ab81f5bbc0bbef713`.
  Chapter 3 is rendering under the single worker.
- Chapters 10–12 completed preparation: 717 paragraphs, word locks and harness
  validation passed. Later Opus anatomical fixes can invalidate chapter 11's
  preparation: source-hash guard prevents stale audio. Recheck chapter 11 once
  the pending hand-count repair report lands.
- Chapters 8–9 were surgically repaired by Opus with eight word-level fixes;
  Sonnet has already committed those changes (`05eb1ea`) and recorded new hashes.
  Fresh Codex narration recheck active: shell session 73005, prompt
  `RECHECK-08-09.prompt.md`, result `RECHECK-08-09.result.md`. It refreshes hashes,
  prepared wording, reviews, direction and readiness only after verification.
- Opus hand-count repair `98c8ed9c` is active for exact single-left-hand arithmetic
  in chapters 11,14,15,19,24. Report
  `provenance/AUDIO-HAND-COUNTS-REPAIR.md`. Do not overlap its source edits.
- Chapters 13–15 preparation is queued behind that report (shell 81321), then
  initializes a fresh run and Codex direction from repaired source. Prompt/result
  `DIRECT-UNIT-13-15.{prompt,result}.md`. Source and hashes govern provisional
  summaries. Continue chapter 11's targeted recheck before it can render.
- The M5 editorial session `887082aa` was blocked on a penname-editor skill that
  would switch review execution to Codex. Declined that tool and resumed the SAME
  Opus session using the supplied O'Connor rubric/formula without substitution.
  It is now working. Master showrunner and cold read remain active; no duplicate
  review session was launched.

## Heartbeat — refreshed opening fixes; spatial clarity repair queued

- Fresh Codex recheck accepted all eight Opus corrections to chapters 8–9 and
  refreshed narration, source hashes, reviews and readiness. Both are ready;
  chapter 7 remains unchanged. Result: `RECHECK-08-09.result.md`.
- Chapters 13–14 are prepared and ready. Chapter 15 is held on two concrete
  issues: third/fourth stamp interval, and west/uphill catching position versus an
  east/downhill cloth. All 713 paragraphs were reviewed, but no false ready
  marker was created for chapter 15. Result `DIRECT-UNIT-13-15.result.md`.
- Opus completed the ten one-hand number fixes in chapters 11,14,15,19,24,
  including two additional chapter 14 occurrences. Full report at
  `provenance/AUDIO-HAND-COUNTS-REPAIR.md`; frozen edition preserved.
- Opus surgical spatial/cadence/Hart-hand repair `f842bac9` is active for ONLY
  chapters 15 and 19. Prompt `planning/OPUS-AUDIO-SPATIAL-15-19.prompt.md`, report
  expected `provenance/AUDIO-SPATIAL-15-19-REPAIR.md`. This preserves prior hand
  corrections; other source changes are outside its scope.
- Fresh Codex recheck is queued behind that report in shell session 36093:
  `RECHECK-HAND-AND-SPATIAL.prompt.md` -> `RECHECK-HAND-AND-SPATIAL.result.md` and
  `HAND-AND-SPATIAL-RECHECK.md`. It verifies all cumulative source corrections
  against the two frozen editions and refreshes ONLY chapter 11/15 narration.
  Wait for its acceptance before committing/publishing those five source files.
- M5 second repair `f517a39f` had a permission prompt for its own temporary quote-
  parity script. Approved that exact harmless script; same author resumed, with
  no model substitution or competing writer. Master showrunner remains healthy.
- Chapter 3 continues synthesis (last inspected s185); chapters 1–2 remain live.
  No new upload or owner action is required at this check.

## 2026-10-15 11:52 UTC — bounded recovery and next narration unit

- M5 is repaired/rechecked and published (55,497 words). M6 draft 41–48 has
  landed; master Sonnet 8491a39c owns reviews and whole-book closure. M6 editorial
  c89e8156 attempted the wrong Codex-backed penname-editor skill; declined that
  skill and instructed the same Opus session to perform its supplied review.
  It is working again; cold read 2dcf4399 also runs. No substitute author.
- Chapter 3 completed synthesis but technical gate held it: only s129.wav has
  one sample at PCM rail (0.999969, sample 96170, 4.00708s). Preserved that exact
  take as held-takes/s129.possible-clipping.wav; all other takes untouched.
  No attenuation is being passed off as repair of potentially clipped audio.
  Restarted only supervisor 29640 as 55205 (shell74336); active chapter4 renderer
  4584 was preserved. The single worker waits for it, then retries chapter3's
  one missing segment and rechecks its complete assembly before publication.
- Hand/spatial fresh recheck passed11/19/24 but found two concrete residual
  defects in14/15. Chapter14 old ready marker is preserved under
  direction.blocked-clarity; chapter15 remains blocked. No affected source was
  committed or published. Opus6754e4fb continues f842bac9's context to fix only
  those two defects. Report AUDIO-FINAL-14-15-REPAIR.md.
- Fresh Codex recheck queued shell71795 behind that report: prompt
  narration/RECHECK-FINAL-14-15.prompt.md. It must verify cumulative five source
  chapters and refresh14/15 before ready markers/publication. Wait for actual
  acceptance before source commit; do not publish those uncommitted five files.
- Initialized16–18 and launched Codex director shell85936 with
  DIRECT-UNIT-16-18.prompt.md. It reads all three chapters and extends17/18
  contexts honestly beyond the provisional16-chapter bible, with explicit Breeze
  override. No local GPU context model or duplicate audio renderer launched.
- Live PWA audio remains chapters1–2. Per-chapter publication continues as soon
  as each technical candidate passes; no owner listening certification implied.

## 2026-10-15 12:53 UTC — audio 3 live; targeted clarity accepted

- Chapter3 pickup succeeded; all other takes preserved. Full live media download
  SHA256 matches 77aac9800f8c30df8d30108a75f3a00aaab047ba3853f8c191adbab4f298737b;
  live manifest matches and range request returns206. Duration2372.66s (39m33s),
  max segment peak0.994232, decode/wordlock pass. Owner listening still pending.
- Chapter4 completed but s190.wav has two PCM-rail samples, so held from publish.
  Added bounded pickup handling to worker: preserves peak-flagged takes under
  held-takes and rerenders only them once per attempt; still blocks publication
  if rail remains. No masking by attenuation or time stretching. Syntax checked.
  Restarted only parent55205 as83718 (shell85592), preserved active chapter5
  renderer4346. Worker waits for5 before recovering4; no competing MLX model.
- Opus6754e4fb and fresh Codex final recheck completed. FINAL-14-15-RECHECK.md
  passes exact cumulative source11/14/15/19/24 and narration14/15. Ready markers
  are current, all earlier ten hand fixes/cast preserved. Notified master8491a39c
  to commit/publish exact five source files, three repair reports/frozen editions
  and acceptance evidence with authorship at next safe publication step.
- Codex16–18 complete:692 paragraph reviews, wordlock100%, no open blockers,
  all3 ready. Initialized19–21, Codex director shell69872 now reading/directing
  from repaired19 and rolling context, prompt DIRECT-UNIT-19-21.prompt.md.
- M6 reviews both complete; master Sonnet consolidating max3 priorities for
  same-author repair, then whole-book review. No duplicate writing job launched.
