# Name options for the tournament (the "Measure")

**Owner picked The Gates on 2026-10-28** (ticket N1, "Go"; the editor's recommended option 1).
The rename is applied in the canon and seed (see "Applied" below). The text from "The three
options" down is kept as the record of what was considered, and so still says "Measure."

Date: 2026-10-27, ticket C2. Owner decision: "Rename (Recommended)." The words *measure,
count, score, tally, reckoning, assay* are out, by the owner's ruling against counting as a
motif.

What was named: the regional tier (**the Regional Measure**, the end of the Meridian
Collegiate Circuit), the national tier (**the National Measure**, Saltmere, 2681), the
individual events ("individual Measures"), the bare noun as people say it ("the Measure,"
21 of the manuscript's 34 uses), and Book Two's working title ***The National Measure***.

## Applied (ticket N1, 2026-10-28)

Done on branch `feature/2680-gates`: `universe/SEED-2680.md` (§5, §8, §9, §12 glossary entry
for the Gates tiers), `books/book-2680-opening/` `BOOK_MAP.md`, `SERIES_MAP.md`,
`UNIVERSE_BIBLE.md`, `STATE_LEDGER.md`, `packets/MOVEMENT-001.md`, `-004.md`, `-005.md`, and
`editor/MOTIF-BUDGET-REVISION.md`. The "pending owner pick" note is gone from seed §5.

Wording chosen:

| Was | Now |
|---|---|
| the Regional Measure | the Regional Gates |
| the National Measure | the National Gates |
| the Measure (bare, the tournament) | the Gates; in packets and canon docs the full tier name is used wherever a literal gate could be read (the School's gate, the Hold's gate, the sluice gate, a ward gate, Stopgate) |
| individual Measures | the singles |
| Book Two title *The National Measure* | *The Saltmere Gates* |

Grammar: the Gates is a plural proper noun ("the Regional Gates were Friday and Saturday,"
"the Regional Gates fall in the autumn"). Only the tournament is capitalised; an event is
never "a Gates"; a literal gate stays lowercase and singular.

**Not applied here, still to do as a separate ticket in the `kindling-2680-book-02` repo:**
Book Two's canon docs (`books/book-2680-national-measure/` `BOOK_MAP.md`, `STATE_LEDGER.md`,
`AUTHORSHIP.md`, `OWNER_BRIEF.md`, `SERIES_MAP.md`, `CHARACTERS.md`, `README.md`,
`UNIVERSE_BIBLE.md`, `art/README.md`), its packets `MOVEMENT-001..006.md`, and the
published title in `scripts/nm-breeze-audio.py` (`'title': 'The National Measure'`, plus its
docstring, two commit messages and an error string) and the docstring of
`scripts/nm-publish-pwa.py`. The folder name `book-2680-national-measure`, the slugs and the
audio stems stay as they are (and `universe/ARCHIVE.md` line 50 still names the folder path).
The manuscripts (Book One's 34 hits, Book Two's 69) are renamed at the prose pass.

### Applied (ticket R4, 2026-10-28): three more renames, owner ruled

Done on branch `feature/2680-rulings`. Unlike the Gates rename these were not options
lists; the owner ruled the names directly. The canon docs carry the new names (the seed
glossary, §12), and the prose pass applies them from the table in
`MOTIF-BUDGET-REVISION.md` §8.7.

| Was | Now | Manuscript uses (Book One) |
|---|---|---|
| Measure Hall (Ysra's building as Placement Chair) | the Placement Hall | 20 in 14 chapters |
| Rule Nine (the Circuit's home rule; title of Ch. 19) | Rule Six, "A change called aloud is declared when it is called." | 10 in 7 chapters |
| Team Eleven | Team Twenty-Two | 5 in Ch. 10, 12, 13 |

Rule Six keeps the numbered-rule convention (Rule Fourteen and Rule Nineteen exist). Team
Twenty-Two does not collide with Team Twenty-Eight. Book Two's manuscript and canon
(`books/book-2680-national-measure/`) also say "Measure Hall"; that is the parallel Book
Two ticket's, not this one.

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
