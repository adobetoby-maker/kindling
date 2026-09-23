# Monroe 1.3 substantive revision card — Movement C

Compiled chapters 39–44; Hobb's Wall source chapters 15–20.

Review mode: substantive editorial self-review, not an independent cold read. The immutable comparison point is commit `2f42770`. The repository-level `universe/UNIVERSE_BIBLE.md` is authoritative where the compiled-book context differs.

## Chapter dispositions

| Chapter | Disposition | Before | After | Added | Removed | Net |
|---|---|---:|---:|---:|---:|---:|
| 39 | `TIGHTEN` | 3,462 | 3,442 | 19 | 39 | -20 |
| 40 | `REPAIR` | 3,157 | 3,151 | 25 | 31 | -6 |
| 41 | `REPAIR` | 6,690 | 6,711 | 88 | 67 | +21 |
| 42 | `REPAIR` | 4,328 | 4,339 | 16 | 5 | +11 |
| 43 | `REPAIR` | 4,923 | 4,915 | 24 | 32 | -8 |
| 44 | `TIGHTEN` | 4,234 | 4,198 | 36 | 72 | -36 |
| **Movement** |  | **26,794** | **26,756** | **208** | **246** | **-38** |

Before/after totals use `wc -w`. Added and removed totals use Git's porcelain word diff against `2f42770`; replacements count on both sides.

## Material repairs

- **Chapter 39:** separated four overloaded coordination chains in the gate drill, Senna's breathing crisis, and Rook's exhausted sleep. The facts and emotional beats remain unchanged, but the listener no longer has to retain several simultaneous subjects and actions before reaching a stop.
- **Chapter 40:** made Wyck's position at the fire immediately visible; corrected Rook's Satori count so Dessa plus two dead cases equals three people besides Rook; rebuilt the fire-making sequence with explicit agents and verbs.
- **Chapter 41:** repaired Rook's family chronology; distinguished Satori from the later work of opening additional doors; kept him explicitly a demonstrated two-door Blaze without claiming the third; changed Homura's destruction from the internally contradictory `everyone` to `nearly everyone`; reconciled the six-year/four-year grief chronology; repaired the Satori-case recap; and clarified that Cinder destroyed both people and the research proof.
- **Chapter 42:** corrected Dessa's Satori-case recap and repaired the east-facing dawn geography so the light rises in front of Rook and Toren while their chosen road lies behind them.
- **Chapter 43:** corrected the elapsed-night reference and rebuilt the engine-house/sluice description into a spatial sequence that can be understood on one hearing.
- **Chapter 44:** corrected the elapsed-night reference; rebuilt Rook's takedown, Milo's setup, and the first two attacks at the arch into trackable cause-and-effect units; added paragraph landings where the combat geometry changes.

## Protected strengths

The pass preserves the movement's long-breath voice where conjunctions build pressure rather than obscure hierarchy. It leaves Rook's confession, Toren and Dessa's reactions, the Homura history, the group's changing division of labor, Milo's light trap, the sluice defense, all outcomes, and every final narrative beat intact. No scene, power, motive, death, or relationship was invented or removed.

## Unresolved canon questions

1. `books/book-01-kindled/UNIVERSE_BIBLE.md` calls Rook's dead partner Satori Kess, while the authoritative repository bible and the manuscript call her Vera Kess and use *Satori* for the state/object. This pass followed `universe/UNIVERSE_BIBLE.md`; the compiled context should be synchronized before future automated edits.
2. The ordinary Ember ownership rule still needs its planned explanation for why Rook can use Vera's disk and Dessa can briefly activate it.
3. `STATE_LEDGER.md` remains a pre-book ledger and should be rebuilt from the accepted revised edition before Book Two continuity work.

## Continuous-read verdict

Movement C now reads more cleanly without flattening its voice. The major improvement is hierarchy: the reader can tell what happens first, who acts, what changes, and what the result costs. The Homura explanation is internally consistent with the authoritative bible, and the sluice fight can be staged mentally on one pass. The revisions are suitable for owner review; narration markup should wait until the prose edition is accepted.

## Completion checks

- Changed manuscript files: `revised/chapter-39.md` through `revised/chapter-44.md`.
- Frozen `chapters/chapter-39.md` through `chapters/chapter-44.md`: unchanged.
- Chapter headings, scene-break structure, and final narrative beats: preserved.
- Narration markup or timing controls added: none.
- `git diff --check`: clean at movement completion.
