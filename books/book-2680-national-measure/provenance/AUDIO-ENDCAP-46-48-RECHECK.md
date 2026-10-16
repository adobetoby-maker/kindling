# Independent end-cap consistency recheck and preparation refresh

Checker: Codex, 2026-10-15. Read the book-narrator skill and complete 1.2.5 workflow, author `AUDIO-ENDCAP-46-48-REPAIR.md`, complete current chapters 45–48, final-unit performance bible, frozen/current sources, actual prior-knowledge and officer-tenure passages. Used local text/file tools only. No prose/canon edits, listening, rendering, publication, git operations, other agent or model.

**Source-publication: YES** for the two bounded repairs. This is a source-suitability recommendation, not publication or supervisor acceptance. The supervisor must record an explicit acceptance addendum after this actual recheck. Historical acceptance tables and author report remain byte-exact; no adoption is implied by preparation readiness.

| Chapter | Frozen accepted SHA-256 | Actual current SHA-256 | Whitespace words | Bytes |
|---|---|---|---|---|
| 46 | `8b6b8de0ac006f9c9229284f38997c5b671d9be30e536dd396725af875ae05af` | `a548da2293408fff6dcdd7d095eb7470dce7cbd474765444a342a557f40504c6` | 7,121 → 7,117 (−4) | 36,967 → 36,945 (−22) |
| 47 control | `6e3de61edfe18bdba53b0e7f25a0e4a1fc71eb667d07c94c945443172f0dc1c5` | identical | 7,175 (0) | unchanged |
| 48 | `0e8c628ef774bcf31a7acfb0b8014c9be67c86bdfb5a1ed2614c0aa33c1a0315` | `0adc917ed84018fbf4e1bc2a010b846d8edaee1de2e178379bf01541d89a18fe` | 6,429 → 6,429 (0) | 32,918 → 32,918 (0) |

The frozen hashes match the historic acceptance rows and old narration metadata. Exactly one line differs per source, with unchanged line/paragraph counts: 46:273 (paragraph 131) deletes “the sister's book, or”; 48:81 (paragraph 38) changes “twenty” to “eleven” in “She had been an officer for … years.” No other source difference. The old source copies and their SHA256SUMS remain exact. Current45 hash is `07a7859be33cce8becfbd1fabe01ea709f03ad624ea5ff97855990ae75d92ffa`; its separately repaired gate wording does not affect the knowledge anchors.

## Sister-account finding: confirmed; correction passes

At45:189 Rhea explicitly says she has written Kiva's counting, without knowing what was counted. At45:193 Kiva's focal scene shows the sister taking out a small book and writing. At45:315 Thrale tells Kiva her sister says she counted; at45:319 she explicitly says her sister has written it for her, in her words. Thus the frozen denial of knowing about the sister's book contradicts knowledge acquired before noon. Reading “book” as specifically the Order's book does not rescue it: the physical book and the account are already established. Punctuation or acted uncertainty cannot erase this knowledge.

Kellan is different. Thrale's “will have a clerk who'll say he did” is a prediction, not confirmation that a counting account exists or has been written.45:327–379 belongs to Kellan's lens; Kiva is not there. At46:129 the narrator identifies Kellan's delivered folded fault paper, but that aside does not give its contents to Kiva. At46:131 the Clerk identifies the Proprietor's witnessed relinquishment line, not a counting account or its witness by name. The noon line46:265 first confirms Mr Renn's written counting account to Kiva. Retaining “She had not known about Kellan's sheet” is therefore intelligible as the newly disclosed counting record in the immediately preceding scene. It must not be inflated into a claim that she had heard nothing about any fault paper.

“She had not known about the three accounts” means the confirmed set of three independently written records, not ignorance of every member: the next sentence already recalls Rhea's statement. The dock-floor belief that she counted alone belongs to the counting moment before Thrale's cart conversation. No new fact is needed.

Both local joins46:271→273→275 pass: Clerk locks away the records; Kiva registers the newly confirmed set and Kellan's record; Hart turns to his own honestly tested prediction. Paragraph273 retains Kiva as subject throughout. The deletion neither changes the independent records nor claims an explanation of the shared count. The author confirmed the actual defect and chose the minimal supported correction; no rejected false flag needs reinstating.

## Officer-tenure finding: confirmed; correction passes

03:217 explicitly gives eleven years as an officer of this company;07:311 says “Rhea had been an officer for eleven years” without a company restriction.07:385,14:387,20:351,31:365 and31:401 support the same span. WB-01 in the actual whole-book repair and recheck changed earlier six-year residues to eleven, and STATE_LEDGER records eleven.37:373 gives twenty years of cutting from behind a skin; that is a different measure of experience. There is no evidence for nine extra officer years elsewhere. The story's roughly five months from03 to48 cannot account for a nine-year increase. Even a possible unrecorded anniversary would not justify inventing twelve; the established eleven is the supported correction.

Both local joins48:79→81→83 pass: the hidden slate line “Not mine to keep” becomes Rhea's recognition of possessive kindness, then recalls that she herself had once been the second. Eleven years supports her professional knowledge without reclassifying her earlier second service. The hypothetical “At the end of five years” remains hypothetical. Neither no, the two conditions, Coombe's commission, Mara's guardianship, Anwen's departure, nor the outward hull ending changes.

Movement joins45→46,46→47 and47→48 also pass: witnessed counting precedes the noon records; Wednesday's hand loss and forecast precede Thursday's fourteen-day card; Rhea's unshown slate line at47's cellar becomes visible only in her own focal scene at48. No knowledge is lent to Kiva by direction.

## Freeze and bounded preparation refresh

Old46/48 evidence is preserved read-only under `narration/editions/source46-48-pre-endcap-refresh-20261015/frozen/`: prepared prose, complete paragraph reviews/feedback/choices, performance tracks, contexts, Breeze directions/preparation reviews, shared run/unit bible and historic unit result. `frozen-hashes.json` verifies every copy. `preserved-files.json` protects all manuscript files, historical acceptance, author report, and all47 chapter/context/Breeze artifacts. All pass byte-for-byte. The prior unit result remains historic rather than being silently rewritten.

Refreshed only46/48 preparation and shared run/unit dependencies. Full review coverage:182 paragraphs in46 and164 in48; all clean, no writing or A/B blocker. Each repaired paragraph and its scene review reasons now state the supported distinction. Prepared46/48 are byte-exact current prose, with headings; no punctuation repair was needed. Contexts retain all owner-deferred items and ending constraints. Sparse scene-specific instructions, Original Calder identity and explicit return to base remain, with1550/2100/2700ms boundary policy and one selective320ms preparation per chapter. Local Breeze override governs the initialized Fish defaults.

Changed ID/text/instruct tuples:46:s100 instruction and s132 text;48:s033 instruction and s040 text. Exact before/after records are in `changed-tuples.json`.48's repaired paragraph spans more than one segment; all mapped segments were checked, with only the one containing the tenure word changed. An initial refresh assumption that it fit one segment failed; the frozen evidence was restored, the update was corrected to cover the whole mapping, and validation was rerun. No source was changed by this tooling correction.

Actual recursive WAV inventory across both46/48 Breeze trees and both prepared chapter trees found **0 WAVs:0 retained,0 archived**. Paths and absence are recorded in `wav-inventory.json`. No filename/ID alone was treated as take provenance. There is no waveform to measure or listen to, and no audio quality or identity approval is claimed.

## Independent validation and current-source readiness

Harness and independent validator pass46/47/48:7,149/7,188/6,442 normalized heading-inclusive words;182/170/164 prose paragraphs; zero blockers. Whitespace counts above deliberately use a different convention. The independent validator checks the supplied clarity schema, source/frozen acceptance chain, prepared and spoken order, paragraph mapping, headings, voice resets and written scene landings. The separate character scanner checks word order, exact heading text and exhaustive segment coverage without importing the preparation implementation.47 is validated read-only.

`endcap-dependencies.json` records actual source, evidence, preparation, workflow, schema-related validation and unit dependency hashes. Its unit SHA-256 is `8a7ac4c568ae3ee1fcd84269ad30cc7240b9a3b8916393caf136ecaf85f82679`, calculated from sorted compact JSON of the dependency mapping.46/48 preparation reviews reference that manifest. Their current-source `direction.ready` markers were written only after validation and contain the current source hashes above. These mark text readiness; supervisor acceptance, audio generation, acoustic checks and complete owner listening remain pending. No Finished claim.

Commands actually used (all local, no render/listen):

```sh
cat /Users/drive/.codex/skills/book-narrator/SKILL.md
cat /Users/drive/penname/pennamecodexv3/workflows/book-narrator-1.2.5.md
cat provenance/AUDIO-ENDCAP-46-48-REPAIR.md
cat manuscript/chapter-{45,46,47,48}.md
# Additional sed ranges read source sections without tool-output truncation.
rg -n 'officer.*(eleven|twenty|six)|twenty years of cutting' manuscript/chapter-{03,07,14,20,31,37}.md
python3 narration/monroe-1.2.5/calder/chapters-46-48/refresh_endcap.py
python3 narration/monroe-1.2.5/calder/chapters-46-48/validate_endcap.py
/Users/drive/penname/harness/book-narrator.sh validate "$PWD/narration/monroe-1.2.5/calder/chapters-46-48/run.json"
python3 narration/monroe-1.2.5/calder/chapters-46-48/verify_endcap_final.py
```

Exact one-line differences, byte/word counts and frozen/current digests were checked with local Python `hashlib`, `difflib` and whitespace splitting; both independent validators are saved beside the run. The refresh script is deliberately one-shot and refuses an existing freeze directory. Final preparation/ready/manifest hashes are captured separately in `endcap-final-hashes.json` without a circular self-hash.

Supervisor handoff: adopt the explicit current46 and48 hashes with a new acceptance addendum after this check. The author report, historical acceptance tables and open owner mysteries have not been edited.
