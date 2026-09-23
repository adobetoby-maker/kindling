# Initial assembly audit — 2026-09-23

## Size

| Measure | Count |
|---|---:|
| Compiled chapter files | 53 |
| Compiled `wc -w` total, including Markdown headings | 212,412 |
| Retained source total before heading renumbering | 212,306 |
| Prose-token count from the Monroe punctuation scanner | 211,484 |
| Hobb's Wall / Toren source 1–26 | 97,489 |
| Callie source 1–17 | 76,598 |
| Jab source 1–10 | 38,219 |
| Reserved Book Two source pool | 41,475 |

The 106-word difference between the retained-source sum and the compiled
`wc -w` count comes from replacing short source headings with numbered,
viewpoint-labeled Kindled headings.

## Listening-risk baseline

The deterministic Monroe scan found 781 sentences above 45 words and 252
paragraphs above 100 words across the initial assembly. That is a locator, not
an automatic defect count.

| Viewpoint | Chapters | Scanner words | Sentences >45 words | Paragraphs >100 words | Longest detected sentence |
|---|---:|---:|---:|---:|---:|
| Toren / Hobb's Wall | 26 | 97,044 | 507 | 116 | 160 words |
| Callie | 17 | 76,400 | 78 | 83 | 90 words |
| Jab | 10 | 38,040 | 196 | 53 | 115 words |

This supports the owner's listening diagnosis: Hobb's Wall carries most of the
book's sentence-load risk. The Monroe 1.3 pass should examine those locations in
context, correcting genuine oral ambiguity while preserving purposeful long
cadence.

## Highest-priority compiled chapters

By number of detected sentences over 45 words, the first Hobb's Wall chapters
to receive concentrated listening attention are Kindled 41, 50, 49, 45, 44,
48, 11, 43, 46, and 40. They correspond to the later Homura/Cinder/Milo and
Meridian-approach movements plus one early-road chapter. The scanner does not
authorize shortening them; it tells the editor where a listener is most likely
to lose the sentence hierarchy.

