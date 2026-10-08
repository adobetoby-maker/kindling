# Kindling 2680, Book One (title unset) — authorship record

Public byline: **Monroe Jackson**

## Prologue and Movement One — Three Doors

- Status: **drafted (prologue plus chapters 1–8); first draft frozen (2026-10-08).**
  Stopped for movement review. No editorial pass, scoring, or repair has been run.
- Seat: Monroe Jackson 1.3.0, O'Connor seat 1.3.0 (progression-adventure)
- Selected author: Opus
- Requested model alias: `claude-opus-5-5`
- Actual model that wrote the prose: **Claude Opus 5.5 (`claude-opus-5-5`)**, as reported
  by the runtime environment. Every manuscript sentence was written by this model in one
  authoring session, in order: prologue, then chapters 1–8. No other model wrote or revised
  prose. No subagents were used, for prose or for research. Canon was read directly from the
  project files (universe and Book One bibles, *Meridian* ch. 48 and its Movement Six
  checkpoint, the *Wellspring* postscript plan and state ledger, the name registry).
- In-run corrections, all by the same author before the edition was frozen. These were blocking
  continuity and canon fixes, not editorial passes:
  - A one-scene prologue name collided with *Meridian*'s Pell; renamed Hedda.
  - Kindling Day row and line-order counts made consistent across chs. 1–2.
  - The weighbridge was dated "six hundred years ago"; corrected to the founders' era.
  - The ch. 5 fingertip precursor was moved to the canon "first two fingers" (index and
    middle).
  - In ch. 7, Orla no longer says *mine* for a Ward she cannot take.
  - In ch. 7, a false claim that Kiva's readings were "the lowest" was replaced.
  - A ch. 8 viewpoint breach (Kiva naming the 2431 registrar) was removed.
  - Orla's drawer chronology in ch. 8 was made consistent.
- Provider: Anthropic, via Claude Code (background job, git worktree
  `worktree-kindling-2680-movement-001`)
- Movement packet: `packets/MOVEMENT-001.md`
  (SHA-256 `e0a4ae06c77e5ff2d98aeda3d13ec0bdcb3ccae88633ec486ffaf265ccf9d580`)
- Compiled prompt: `planning/OPUS-5.5-PROLOGUE-MOVEMENT-001.prompt.md`
  (SHA-256 `706050e56678447c36c2bdcfc7dab60c784019e0a7c7b447a31d420889876a7b`)
- Prologue plan: `PROLOGUE_PLAN.md`
  (SHA-256 `8e2fd262203c834b1257430f794c91bf3b2127048078028fc41734b81715699d`)
- Numerical formula: `/Users/drive/penname/research/ironprince-craft-formula.md`,
  SHA-256 `9f97e2f225c0bcf61d2e922719153fcf00e3b029f7b1552f213888d33130c0b8`. This matches
  the hash recorded in the compiled prompt. It was verified before drafting and again at the end
  of the run.
- Edition: Book One, Prologue and Movement One, first draft (2026-10-08), frozen at
  `editions/movement-001-first-draft/`
- Manuscript: `manuscript/prologue.md`, `manuscript/chapter-01.md` … `chapter-08.md`
- Continuity checkpoint: `provenance/MOVEMENT-001-CONTINUITY.md`

### Viewpoints and length

| Ch | Heading | POV | Days | Words (`wc -w`) |
|---|---|---|---|---:|
| P | What Somebody Wrote Down | Six dated historical snapshots (2080–2680) | — | 4,871 |
| 1 | Renn, Then Rowan | Kiva | D+0 | 5,110 |
| 2 | What the Needle Wrote | Kiva; Mara cutaway | D+0–1 | 4,551 |
| 3 | One at a Time | Kiva | D+2–3 | 5,184 |
| 4 | Nobody Can Sign It | Kiva; Ysra cutaway | D+5–7 | 4,545 |
| 5 | Holding | Kiva | D+8 | 5,367 |
| 6 | The Account | Kiva; Kellan and Anwen cutaways | D+8–12 | 5,626 |
| 7 | Letting Go | Kiva | D+13–15 | 5,570 |
| 8 | The Lowest Line | Kiva; Ysra and Orla cutaways | D+16–19 | 4,894 |
| **Movement (chs 1–8)** | | | | **40,847** |
| **With prologue** | | | | **45,718** |

First-draft SHA-256 (identical in `manuscript/` and `editions/movement-001-first-draft/` at freeze):

```
99e0ce1e3db21bbf97ee06ffc9238b98b7814fd75cef636683dacf669c82a103  prologue.md
5f0e03678801089b74a6fd2a0b3fc0bacbd053ae8a3a9574228a67e2dc6c1ea2  chapter-01.md
dffbedff3dd03a490a02c84834133a7fd2007de83001eeaee2823787f4da42f7  chapter-02.md
d321b1e33060d61288100c0934101a8a0b7e67e41892d243891524c63e57c482  chapter-03.md
25f796943996b2652f9a09917ff6fd3e6967c825fdeefa711350def136d69288  chapter-04.md
39d58fc5dbff2060fd5f7ad7906bee809c4ab6e0211ee6ed7e846ce0a12837eb  chapter-05.md
283ad75fb4ddc7f0b6646aee6c7280290b92866c58e1a60f826075373ca07201  chapter-06.md
dadf2c592c3cc7c4d23874206c56bd397cb5382b3f3e037e6a393cfb12243ab6  chapter-07.md
27418de7372c7d071ab90dc31fe0a40f2c8191876067164aa819b724abb88fcd  chapter-08.md
```

- **Single lead.** Kiva holds about 84.8% of the movement's words. Five brief cutaways total
  6,196 words (about 15.2%): Mara 1,294; Ysra 1,420 + 750; Kellan 866; Anwen 685; Orla 1,181.
  That is above the formula's ~13%, and Ysra exceeds the 2.5–3.7% per-person band. **Reported,
  not repaired.**
- **Length is below the book map's implied ~45,000–52,500 words per movement.** No chapter was
  compressed for output limits, and no scene was padded. Whether to expand belongs to the
  movement review.
- Noa Bexley and Hollis Vane were not introduced; the run did not earn them. Rhea Sorn appears
  once, at the anniversary walk.
- No per-chapter editing, scoring, or approval gates were run. The target-versus-observed
  comparison against the O'Connor numerical formula (sentence distribution, paragraph rhythm,
  readability, progression density, development cadence) belongs to the movement editorial pass.

Codex orchestrates the run and repository work. Codex did not substitute itself as the prose
author.
