# Name options for the tournament (the "Measure")

Date: 2026-10-27, ticket C2. Owner decision: "Rename (Recommended)." Nothing is renamed
yet. Every "Measure" in the seed and canon stands as written, marked once as pending in
`universe/SEED-2680.md` §5 (and the Book Two row of §9), so that a single find-and-replace
applies the owner's pick. The words *measure, count, score, tally, reckoning, assay* are
out, by the owner's ruling against counting as a motif.

What is being named: the regional tier (**the Regional Measure**, the end of the Meridian
Collegiate Circuit), the national tier (**the National Measure**, Saltmere, 2681), the
individual events ("individual Measures"), the bare noun as people say it ("the Measure,"
21 of the manuscript's 34 uses), and Book Two's working title ***The National Measure***.

## The three options

| | Regional tier | National tier | The events | Said bare | Book Two title |
|---|---|---|---|---|---|
| **1. The Gates** (recommended) | the Regional Gates | the National Gates | the singles, the lanes, the Bench, the carry, the Call (the events already have names; "individual Measures" becomes "the singles") | "the Gates" ("Seven goes to the Gates") | *The Saltmere Gates* |
| **2. The Lanes** | the Regional Lanes | the National Lanes | the singles, the lanes (the team event keeps its name), the Bench, the carry, the Call | "the Lanes" | *The Saltmere Lanes* |
| **3. The Muster** | the Regional Muster | the National Muster | the singles, the lanes, the Bench, the carry, the Call | "the Muster" | *The Saltmere Muster* |

**1. The Gates.** A gate is what a Hold stands, what the Circuit's one new rule is about
("a gate shall be left lit"), what the Order asked Kiva for twice, what the leaning post
turns out to be, and what the street below the School is named for (Stopgate). The
tournament is the gate the Circuit feeds the companies through. It reads as a place and an
act, not a tally, and *The Saltmere Gates* is a title with a harbour in it. Risk: "gate"
is already a busy word in the system vocabulary (the Hold's gate, the School's gate, the
sluice gate); the prose pass would keep "the Gates," capitalized and plural, for the
tournament only.

**2. The Lanes.** The declared-role lane is the School's method, the Old Yard is a lane,
the first Home Line laid a lane, and the climax is a lane run dark. Students already "run
the lanes"; a season that ends in "the Lanes" needs no explaining. Risk: the team event
inside the tournament is already "the lanes," so the tier and its event share a word; the
prose pass would say "the Regional Lanes" for the tier and "a lane" for the event.

**3. The Muster.** Chartered companies muster; the Home Line stands watches; a muster is
a gathering of fighters to be looked over, which is what recruiters do at the Regional.
It has the military-school flavor the series promises and no collision with any existing
term. Risk: it is not drawn from the city's own places, so it carries less of Meridian
with it, and *The Saltmere Muster* is a flatter title than the other two.

Rejected: **the Crossing** (a crossing is already the Home Line's word for a sequence;
the collision would be constant), **the Call** (already the live spawn response at the
Regional and the readout *Call*), **the Standing** (standings; a score word in disguise),
**the Floor** and **the Pit** (grounds, not the event).

## What the rename touches

Apply the pick with one case-sensitive find-and-replace of "Regional Measure," "National
Measure," "individual Measures," and then "the Measure" / "a Measure" / "Measures" by hand
where the bare noun stands. Counts are occurrences of the string `Measure` on 2026-10-27.

**Canon and seed (edit at the rename):**

| File | Lines | Hits |
|---|---|---|
| `universe/SEED-2680.md` | 226, 227, 229, 230 (§5, with the pending note), 244 (Saltmere, National Measure), 344 (§8, Movement 5 title), 367, 368 (§9 table, Book Two title) | 8 |
| `books/book-2680-opening/BOOK_MAP.md` | 65 (Movement 5 title) | 1 |
| `books/book-2680-opening/UNIVERSE_BIBLE.md` | 44 ("in Measures, brackets"), 146 ("ending in the Regional Measure") | 2 |
| `books/book-2680-opening/SERIES_MAP.md` | 53 | 1 |
| `books/book-2680-opening/STATE_LEDGER.md` | 74 (twice), 299, 349, 499, 518 (mirrors the manuscript; rewrite with the prose pass) | 6 |
| `books/book-2680-opening/packets/MOVEMENT-001.md` | 63 | 1 |
| `books/book-2680-opening/packets/MOVEMENT-004.md` | 101 | 1 |
| `books/book-2680-opening/packets/MOVEMENT-005.md` | 1 (title), 53, 91, 98 | 4 |
| `books/book-2680-opening/editor/MOTIF-BUDGET-REVISION.md` | 107 (beat 14, "the National Measure paper") | 1 |
| `universe/ARCHIVE.md` | 50 (the directory path `book-2680-national-measure`; see the folder note below) | 1 |
| `books/book-2680-national-measure/` canon docs: `BOOK_MAP.md` 10, `STATE_LEDGER.md` 13, `AUTHORSHIP.md` 8, `OWNER_BRIEF.md` 4, `SERIES_MAP.md` 3, `CHARACTERS.md` 2, `README.md` 2, `UNIVERSE_BIBLE.md` 2 | 44 |
| `books/book-2680-national-measure/packets/MOVEMENT-001..006.md` | throughout | 27 |
| `books/book-2680-national-measure/art/README.md` | 1 (the heading "The National Measure visual package") | 1 |
| `scripts/nm-breeze-audio.py` | 131 (**the published book title** `'title': 'The National Measure'` in the Breeze binding; this is what listeners see), 2 (docstring), 104 and 147 (commit messages), 310 (an error string) | 5 |
| `scripts/nm-publish-pwa.py` | 2 (docstring) | 1 |

**The folder name.** `books/book-2680-national-measure/` is referenced as a path by four
scripts: `scripts/nm-publish-pwa.py` (lines 14, 17, 38, 62, and the `--slug` help text),
`scripts/nm-breeze-audio.py` (25, 137, 192), `scripts/run-kindling-2680-book-02-movement-001.sh`
(5), and `scripts/wait-and-start-kindling-2680-book-02-reviews.sh` (5); the PWA's published
manuscript paths and the Breeze audio stems (`national-measure-chapter-NN-…`) also carry
it. **Recommendation: keep the folder path and the slugs as they are; rename only titles
and text.** Renaming the folder means editing four scripts, the PWA's content paths, and
the audio bindings for no reader-facing gain.

**Manuscript (edit at the prose pass, not before):** Book One, 34 hits in 18 chapters:
Ch. 48 (6), Ch. 40 (4), Ch. 1 (3), Ch. 8 (3), Ch. 14, 33, 35, 39 (2 each), Ch. 4, 11, 16,
24, 26, 32, 34, 37, 41, 47 (1 each). Book Two, 69 hits across its 48 chapters.

**Provenance and prompts (do not edit; they record what was written from):**
`AUTHORSHIP.md` (4), `provenance/*.md` (20), `planning/*.prompt.md` (67), `editor/*` other
than this file and `MOTIF-BUDGET-REVISION.md` (about 130), and Book Two's `planning/`,
`narration/`, and `provenance/`.

## After the pick

1. Replace in the seed first (§5, §8, §9), then the Book One canon docs and packets, then
   the Book Two canon docs, in one commit, and remove the pending note from seed §5.
2. Add the new word to seed §12 (glossary) with one line: what the tiers are called, what
   the events are called, how people say it bare.
3. The prose pass applies it to both manuscripts with its other changes.
