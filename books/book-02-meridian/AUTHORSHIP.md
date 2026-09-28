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

## Movement Four — The Rip Road

- Status: **drafted, reviewed, repaired, and accepted (chapters 25–32; 2026-09-27/28).**
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as
  reported by the runtime environment.
  - It was one continuous session, and every manuscript sentence was written in it.
  - No subagents and no Agent tool were used, for research or for prose.
  - No other model wrote or revised prose.
- Session architecture:
  - The author read the compiled prompt in full, then Chapters 17–24 in full.
  - It consulted `provenance/MOVEMENT-003-CONTINUITY.md` (binding ledger),
    `provenance/MOVEMENT-002-CONTINUITY.md` and
    `planning/OWNER_REVISION_2026-09-27.md` to verify facts.
  - It grepped earlier chapters for a handful of physical details (the hook's long
    reach, ground-reading vocabulary, Pell's manner).
  - It drafted chapters 25–32 in order with the file-writing tool.
  - It then read the whole run in order and corrected only blocking contradictions
    with exact-string edits.
- Provider: Anthropic, via Claude Code (Agent SDK harness)
- Movement packet: `packets/MOVEMENT-004.md`
  (SHA-256 `7687b3c2716e6322bb04ab3ac3991aaec34aec386399b6028269941887de79dc`)
- Compiled prompt: `editor/MOVEMENT-004-OPUS-5-5.prompt.md`
  (SHA-256 `be133235ab310af3d19dd3fd080a37c2a6df598d03d877c1a2f0db3686dbca0b`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`,
  verified before drafting and again at the end of the run.
- Edition: Book Two, Movement Four, first draft (2026-09-27)
- Manuscript: `manuscript/chapter-25.md` through `manuscript/chapter-32.md`
- Viewpoints:

  | Chapters | POV |
  |---|---|
  | 25, 28, 31 | Callie |
  | 26, 29 | Toren |
  | 27, 30, 32 | Jab |

  Each chapter has a single viewpoint.
- Drafted length: **53,750 words** (`wc -w`), about 7.5% above the packet's approximate
  42,000–50,000. No scene was padded, and none was compressed to fit.
- Viewpoint share by words: Jab 37.0%, Callie 33.9%, Toren 29.1%.
  - **This does not meet the packet's "Callie-leaning, Jab and Toren co-equal
    behind her."** Callie has three chapters, including the fight's finish, but
    Jab's three chapters are longer.
  - It is recorded, not silently rebalanced, and left for the editorial pass.
  - Cumulative through Movement Four: Callie 34.0%, Toren 33.1%, Jab 33.0%.
- Continuity checkpoint: `provenance/MOVEMENT-004-CONTINUITY.md`
  (SHA-256 `12f81d046690425311f5fa008551685377270a4f97a52132c675142e75307c7e`).
  It records:
  - the conflicts resolved before drafting (Ward vs radiation; the contingency;
    the red-call rule as the mechanism that names the three leads);
  - author choices that are now canon;
  - the day map and viewpoint map;
  - the ash ledger: road 8→0; inside 64→40 after the night's settling (one Flask
    spent on the road, one broken on Tonk's rail, one spent in the cut); the line
    16; working 24 against 48 priced; home 24 untouched;
  - bodies and injuries (Pell's broken right ankle; Rook's reopened, contaminated
    back, off; Callie's ribs; Toren's jarred forearm);
  - object state and knowledge boundaries (the ten-and-three recall of loose ash,
    stated as Jab's inference);
  - the wash fight's staging;
  - open clocks (earliest return D+55 against the ~D+54 cycle; the road east cut);
  - the exact exit pressure for Movement Five.
- Frozen first draft: `editions/movement-004-first-draft/`, hash-checked against the
  manuscript at the end of the run.

No per-chapter editing, scoring, or approval gates were run. During the whole-run
read the author corrected only blocking contradictions:
- road-jar attribution on the drift day;
- the vent-jar count;
- the husk-smear count and the horse's recall in the ledger;
- the siding and road-day references;
- the D+41 ward reference;
- Dessa's distance and the D+41 chair time;
- counter readings kept below the red until the red call;
- which side of the culvert was undermined;
- one knowledge slip (Jab "hearing" advice given when he was absent).

Target-versus-observed comparison against the formula was **not** run; it belongs to
the movement editorial pass. The scene-break proxy is known to be short (about 467
words per section against ~950). No human cold read has been run.

The connected first draft was followed by one simulated cold read, one canon/formula
editorial review, one consolidated same-author repair, and one fresh-context targeted
recheck. The recheck accepted all manuscript questions and found only three mistyped
hash suffixes in the repair report; those were replaced with the full verified hashes.
No manuscript line changed after acceptance.

## Movement Four — consolidated same-author repair

- Status: **complete; targeted recheck verdict `repair accepted`**
- Cold read: `editor/MOVEMENT-004-COLD-READ.md`
- Editorial review: `editor/MOVEMENT-004-EDITORIAL-REVIEW.md`
- Repair prompt: `editor/MOVEMENT-004-REPAIR.prompt.md`
- Repair report: `editor/MOVEMENT-004-REPAIR-REPORT.md`
- Recheck: `editor/MOVEMENT-004-RECHECK.md`
- Model that actually made the repair: **Claude Opus 5.5 (`claude-opus-5-5`)**,
  the same selected author, in one continuous session with no subagents or Agent
  tool.
- Review disclosure: both reviews and the recheck used Claude Opus 5.5 in fresh
  contexts. They are same-model simulated reads, not independent human reads.
- Repaired length: **54,991 words** (`wc -w`), net +1,241 words from the frozen
  first draft and 9 words below the book map's 55,000-word movement allowance.
- Repair scope:
  - priced Callie's gust/lull lee and Toren's long cart hold through settled ash,
    personal reserve and explicit floor checks;
  - repaired the Chapter 26 camp compass and protected the lent ash during the
    empty-cart second crossing;
  - reconciled road/inside/home ledgers and small wash geometry/object seams;
  - named `Guard` once after demonstration;
  - lightly thinned repeated surface phrases while preserving the complete fight,
    count motif, viewpoint voices and ten-and-three ending.
- Frozen first draft: untouched and recorded with full SHA-256 hashes in the repair
  report.

Codex orchestrates the run and repository work. Codex does not substitute
itself as the prose author.

## Movement Five — Caul Hill

- Status: **drafted, reviewed, repaired, and accepted (chapters 33–40; 2026-09-28)**
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as
  reported by the runtime environment.
  - It was one continuous session, and every manuscript sentence was written in it.
  - No subagents and no Agent tool were used, for research or for prose.
  - No other model wrote or revised prose.
- Session architecture:
  - The author read the compiled prompt in full, including the embedded Chapter 32,
    book map, M4 checkpoint, canon and name registries.
  - It then read Chapters 25–31 in full (Chapter 32 was read in the prompt).
  - To verify facts it grepped and read excerpts of earlier chapters: Senna's Caul Hill
    accounts (chs 14, 18, 24), the lifting technique (ch 7), the carrier, boxes, tongs,
    door and permission (chs 17, 19–24), and the M3 checkpoint's settling capacities.
  - It drafted chapters 33–40 in order with the file-writing tool, one connected run,
    with no per-chapter scoring, approval or editing gate.
  - It then checked the run for blocking contradictions and corrected them with
    exact-string edits (listed below), wrote the continuity checkpoint, and froze a copy
    of the first draft.
- Provider: Anthropic, via Claude Code (Agent SDK harness)
- Movement packet: `packets/MOVEMENT-005.md`
  (SHA-256 `f29be1b269c3ff5f8c760f5a2d7a49467cc0672421978ba92d9cb7204140556e`)
- Compiled prompt: `editor/MOVEMENT-005-OPUS-5-5.prompt.md`
  (SHA-256 `b907799f038cbbc679576a784ab6599160f8524cd934690d09f5048096e0f877`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`,
  matching the prompt's recorded hash; re-verified at the end of the run.
- Edition: Book Two, Movement Five, first draft (2026-09-28)
- Manuscript and SHA-256 at the end of the run:

  | File | POV | Words (`wc -w`) | SHA-256 |
  |---|---|---:|---|
  | `manuscript/chapter-33.md` | Toren | 6,637 | `dd6e4caee42e98f5253fbf12befa2359a69db4311b7b75b5f06828b5e288a8cd` |
  | `manuscript/chapter-34.md` | Callie | 6,483 | `f12c40c537979995d3cd2096dab7d857e5b8b3be24660abe418bdbcee0e88ce9` |
  | `manuscript/chapter-35.md` | Jab | 6,442 | `419a87801e9d35c0cfa7a36301a84c74ca2f3ac33cc8acf15e479b08aa0da72c` |
  | `manuscript/chapter-36.md` | Toren | 5,059 | `39d17f9e95fd48a3ee3944adf311237628344755b41b3652b6412258faba052d` |
  | `manuscript/chapter-37.md` | Callie | 5,681 | `9f7cab7e7b172b2a4d36f0332797311ae283aea5c0f04e5efb8806593ab08acc` |
  | `manuscript/chapter-38.md` | Jab | 6,336 | `90a8e4590c1889ca270f833ffed1c7371951c6ea0dcab30ccc7460036701558d` |
  | `manuscript/chapter-39.md` | Toren | 4,662 | `d6523cb6a2815c1d539d4acd8b7552af335e1c6f84cc78e2711171a4a87c8731` |
  | `manuscript/chapter-40.md` | Callie | 4,893 | `695d7efe6c7b96e999b7f1e01817c331b2003de4c1da32351cb7d88c564a80f2` |

  Each chapter has a single viewpoint.
- Drafted length: **46,193 words** (`wc -w`), inside the packet's approximate
  42,000–48,000. No scene was padded, and none was compressed to fit.
- Frozen first draft: `editions/movement-005-first-draft/`, byte-identical to the
  manuscript files above at the end of the run (`cmp`).
- Continuity checkpoint: `provenance/MOVEMENT-005-CONTINUITY.md`
  (SHA-256 `38f55387c647dbde438017083e9a565ed0503a673aed80492686243ff9a660f5`). It
  records the conflicts resolved before drafting, author choices now canon (the bridge,
  gate, yard, road, long building, stair and ramp, the steel door that pushes from the
  corridor side, room 1, the drum, the sky count), the lifter's mechanic and anatomy,
  the day and viewpoint maps, the full ash ledger (40 in; day line 28; the line crossed
  on purpose for two turns; 32 lifted after the kill; 20½ clean + 4 dirty of the
  lifter's, 13 fence, 24 home untouched at exit), the fight's staging, recovered boxes
  (two; the half-open third left), bodies, objects, knowledge boundaries, the route
  decision (the wash, the cart in pieces, D+50 if the wind is down; home D+55 at best),
  and Movement Six's entry pressure.

**Deviations and disclosures**

- **Viewpoint balance is not even.** The packet asked for a true three-way movement
  finishing approximately even by words. Observed: Callie 36.9%, Toren 35.4%, Jab 27.7%
  (Jab has the two chapters and they are not long enough). Cumulative through Movement
  Five: Callie 34.5%, Toren 33.4%, Jab 32.0%. Recorded, not rebalanced; for the
  editorial pass.
- **Scene-break proxy is short:** about 436 words per section against the formula's
  ~950 (same direction as Movements Two to Four).
- **"The way …"** occurs about 139 times across the movement (including literal uses),
  the surface tic flagged in M4. Not thinned in the drafting run.
- **Formula comparison was not run**; it belongs to the editorial pass.
- **The single disk clue was held** for Movement Six; Toren's stone is not mentioned.
- **Author inventions not previously on the page** (now recorded as canon in the
  checkpoint): the barrow ramp and rope rings on the yellow stair; the shed's tongs
  packed inside the carrier with a label; the drum; the pump's lift/flap/push; the
  gatehouse chalk strokes; the copper-wire twist on the gate chain; Sowerby's four fever
  papers in Dee's bag; the name "the lifter".
- **Blocking contradictions corrected during the whole-run check** (exact-string edits):
  - ch 34: Dee's running total of ash spent after forty turns (2¼ → 3¼) to match the
    two halts;
  - ch 35: the red call now reads 150 (the red) rather than 140; an invented quotation
    attributed to Rook from Book One was replaced with a memory that asserts no quote;
  - ch 36: one possessive slip ("Dee's own stone");
  - ch 37: the ceiling rope is now cut in the corridor before the hole (so the lee can
    cover the hole), Dee and Jab enter before Callie sets the lee, and Dee's call at the
    end of the first three is worded as a three, not a count;
  - ch 39: the tongs lie where Callie dropped them on D+47; the gate wire is re-twisted
    on the way out rather than untwisted; the lifter's collapse is measured from where it
    lay, not the carrier; the five recovered jars are "three full and two not";
  - ch 40: a mis-attributed line of Pell's; the lifter's clean count after Dee's night
    draw (20½, not 22) and the downstream sum; "eight days" away from home, not nine.
- No human cold read has been run. The completed reviews are disclosed same-model
  simulated reads, not independent human reads.

Codex orchestrates the run and repository work. Codex does not substitute
itself as the prose author.

## Movement Five — consolidated same-author repair

- Status: **complete; targeted recheck verdict `repair accepted`**
- Cold read: `editor/MOVEMENT-005-COLD-READ.md`
- Editorial review: `editor/MOVEMENT-005-EDITORIAL-REVIEW.md`
- Repair prompt: `editor/MOVEMENT-005-REPAIR.prompt.md`
- Repair report: `editor/MOVEMENT-005-REPAIR-REPORT.md`
- Recheck: `editor/MOVEMENT-005-RECHECK.md`
- Model that actually made the repair: **Claude Opus 5.5 (`claude-opus-5-5`)**,
  the same selected author, in one continuous session with no subagents or Agent
  tool.
- Review disclosure: both reviews and the recheck used Claude Opus 5.5 in fresh
  contexts. They are same-model simulated reads, not independent human reads.
- Repaired length: **47,586 words** (`wc -w`), net +1,393 words from the frozen
  first draft and inside the movement's 42,000–48,000 target.
- Repair scope:
  - enforced Toren's one-configuration limit through explicit Guard/Edge handoffs;
  - repriced the D+48 catch sequence, reserve floors and deliberate line crossing;
  - repaired yard, door, stair, threshold, fall and sledge-belay staging;
  - reconciled jar, sky, day, medicine, naming and read-aloud continuity;
  - preserved the full fight, two recovered wheel boxes, three untouched home
    Flasks, uncertain lifter Yield and unresolved change in the sky count.
- The targeted recheck found one reversed stair count. It was corrected exactly
  (twenty steps to the landing, then thirty), after which the repair was accepted.
- Frozen first draft: untouched and hash-verified in the repair report.

Codex orchestrates the run and repository work. Codex does not substitute
itself as the prose author.
