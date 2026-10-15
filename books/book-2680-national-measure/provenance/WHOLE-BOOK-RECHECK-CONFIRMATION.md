# Whole-book recheck — confirmation and acceptance

Date: 2026-10-15 (morning, MDT). Showrunner: Sonnet 5.5 (records only; no prose written).

**Chain.** Three fresh-context whole-book reviews (continuity `6f04bed8`, promises `26886465`, seams `ffc1e86f`; all Claude Opus 5.5, runtime-reported, same-family simulated, read-only) produced located findings that
cross movements. One same-author Opus 5.5 repair (job `32af798e`, `provenance/WHOLE-BOOK-REPAIR.md`) applied them (with the showrunner's owner-level decisions recorded in the repair brief §B) to 35 chapters; a fresh-context
recheck (job `59421479`, `provenance/WHOLE-BOOK-RECHECK.md`) re-read every changed passage against the frozen pre-repair book and found the repair accurate and bounded, with four surviving items (D1 Kiva's knowledge of Mara's
thirty-six hands at 33:71; D2 a surviving "she never went red" at 42:207; D3 a 77/76 split in the age of the Proprietor's reading at 39:189, authorised by the showrunner; D4 three stale "Sedge" record lines). The same repair author
(Opus 5.5, resumed, job `0176bac3`, `OPUS-5.5-WHOLE-BOOK-SECOND-REPAIR.prompt.md`) applied exactly those four items. Showrunner verification: only chapters 33, 39 and 42 differ from the state the recheck inspected; each of the four
sites is as specified; the quote-parity scan finds no odd-quote paragraph that is new against the frozen book; the frozen edition `editions/whole-book-pre-repair/` verifies OK for all 48 files; the rename to *Shapter* has no old-name residue in
chapters 37 and 41–44.

**The book is accepted as editorial context and as the text for publication** at 325,933 words (`wc -w` semantics over the 48 chapter files; committed text changes to 35 chapters since the PWA's 1.18.45). This is a same-model-family
editorial acceptance. It is not human reader feedback, independent testing, or narration approval. The final four bounded edits were verified by the showrunner by site check, scan and hash, not by another fresh-context model pass.

## Accepted text: final SHA-256 per chapter

| Ch | Words | vs pre-whole-book-repair | SHA-256 |
|---:|---:|---|---|
| 1 | 5,889 | changed | `436fb3329cb8739768f35d6c449a5e4f31eebb60178b5a891e06921e7e2de410` |
| 2 | 5,709 | unchanged | `12c3e7923ab40929de5134701949343a90a45cf28f83dbabdd0046244778fe19` |
| 3 | 5,599 | changed | `c4120ba3ac84beeb780a5c4e5faecb3f965a1667d8de8d750e3195526e8ff632` |
| 4 | 5,451 | unchanged | `ed44c7986609a28e7eb858f2fa9796628e1231f51661594988cd469233265144` |
| 5 | 5,654 | unchanged | `e47d8af8d8b02feeda606b9544dbd62ee12e8d8d419aeefc59a8facd4f14063f` |
| 6 | 5,587 | unchanged | `04db4dadc301d9aa88bde0959e2a7370542a7f4c8d12fd744b7e07a765fbb85d` |
| 7 | 7,389 | unchanged | `110b7906434f71f0752cf944a7eae91d3a092052d4444622ba7a471d656ec3cc` |
| 8 | 6,973 | changed | `d3523cb5f4cb50ce700b0aff8fc80e6220f911362924932a681e341f137dbb96` |
| 9 | 8,917 | changed | `4f951492d37d8f80f178789db2d5dd1a42b7ca120701da45b735a6d2a186788d` |
| 10 | 6,225 | unchanged | `c1a2d19ca47b486dea958e288e095b10a5a038aa7d5c86ddf8d81544ee7c19eb` |
| 11 | 7,891 | unchanged | `0e1e288bbdddf474ca8ac3afce7eee14c4fa53db4989251abb44a150e21f3a91` |
| 12 | 7,350 | unchanged | `bcb42ba039791ff377f361eed96c4b1f57e98b7b22aefba11d3555e671e8b5da` |
| 13 | 7,309 | changed | `c3834e03c8298e4ac8cc5552c0abc3022eba896d60c50e868c1ccd19f930ca31` |
| 14 | 6,128 | changed | `a879cca493717a47eabc862564c00290a5c1a7a555c0252f7067afc03268eb30` |
| 15 | 8,414 | changed | `ae7960eb39d25f80027d54809f85c915bb9f50d2d163a3171f54f6f378010892` |
| 16 | 7,024 | changed | `712bf52cd168daf4629841dfa7a6c63340ca01d1e62e7d858b1e17edc0498685` |
| 17 | 7,161 | changed | `dbbb78fa53a5878c4c46a9facaf1c2bcfa6707639a85891c3873464c177a427a` |
| 18 | 8,132 | unchanged | `4a4aba68311d38d78c443740d506c1a6303f9144a098da4bf1130d24460aadf9` |
| 19 | 7,610 | changed | `2946d2594d6c4f2aab58d8f358874967b8ac986fe04243426dac100108a2fb6f` |
| 20 | 7,094 | changed | `21bd8a0aae6381b5636b197f76857c9ea81c473b6dd4382f9690d61b831d30bd` |
| 21 | 6,558 | changed | `2c61f1905c47ad7c39bf397642e800bc63b0f3d419fbed440443158eb0bd81f4` |
| 22 | 5,779 | changed | `698872859d82a4f6fb30becc84783fb99e3ab9201622449dc7bc9d28c9d2cd0d` |
| 23 | 6,512 | unchanged | `71245a038c63cc2a06efe176402c6e56c41aad36e556ac56b70d448c9ae2b712` |
| 24 | 5,761 | unchanged | `bf68b73a52ff1e62f35e523c2da1977bd6463d4529c33953740fde4d8e17f547` |
| 25 | 6,364 | changed | `59653f7f481162d4e88739b1c573adc748267062050a5a6c21681542159473d1` |
| 26 | 5,106 | changed | `e51f0c51773bb1447c3cd4ab7201dd1e727fd600ed0ff593697e21830f327da7` |
| 27 | 7,270 | unchanged | `047cbc477953f9ad483c242c830dd6ea8e2ec49af000327fe6cbcf6abc6fdb79` |
| 28 | 5,021 | changed | `a3d147679948502b05ee1879e37f7d347de0228acb8fab2b75121edc0b86e5dd` |
| 29 | 6,186 | changed | `9fc46737f1933c505a25774e156b43e32d422712aa4543094b8fd635b17318fe` |
| 30 | 6,356 | changed | `4684b0bad35aa1062c1255a93ffda1844a5bb9ec6a2be02768ec0b387a106a87` |
| 31 | 6,646 | changed | `c2fad74e257925f8d194a1967f35d34a0e9577083d453fecb7958ede136f9a7e` |
| 32 | 9,199 | changed | `835eb0caf7137d74ee6c7e164707026b796e9484920b0f203d45ee72c29376fa` |
| 33 | 8,529 | changed | `f584ff623f871dfe4108aae61816e35f729d0d3af6f5f82344d62a9fd7099da6` |
| 34 | 6,365 | changed | `6b24e7abe844e79643e77c8f20c6e956e51f0bd40b98443ddeebe0f05aaf5f35` |
| 35 | 6,006 | changed | `1dee7ed8caabd3adee8a78fc67dd3e259b516d8a0e8888e052bad5cb043362e1` |
| 36 | 8,131 | changed | `6a61fd68ff8acdc00884382e11b23a6ca03dcf802db5a7ccfe939b3dbc524457` |
| 37 | 6,629 | changed | `59097370d58d817dc2ee871f50ec004d5189dcbe4cc1e38ec8ff4a0e3fc7f7be` |
| 38 | 6,126 | changed | `3f67d10d46a1186bf0b3d912ba19f3298f391753b1172f1aa913c05cba59e24a` |
| 39 | 5,585 | changed | `6eec65de0644f1a92aa58b2c05aa0592d4a528f022aa5dddd3bb4035f8357356` |
| 40 | 7,972 | changed | `4c32f991450a9104fe9cc37615346469383cc72753fb715dc7d451530fc11aee` |
| 41 | 7,231 | changed | `a67ed23f4ac8db2330dce78c4f0521211f32435e5bb662484dde23bc32efd104` |
| 42 | 6,896 | changed | `6d9e7dca70bead9dae377f17c457607434da5e0e690bce5ebb5a286a8e179506` |
| 43 | 5,715 | changed | `18aeddbbc35392f2fb20c6d66738b361d4a4ce138ec79c07b9b9e81c0fbd38b1` |
| 44 | 8,432 | changed | `c81c856671d9d99886dbdb6f7277b5111fe0beb3f18c201d46abd97a2f441ace` |
| 45 | 7,327 | unchanged | `f8467d4d06ab05d22f75c7efea3c034e8b4604f7f32700a22712dfa0410e1edd` |
| 46 | 7,121 | changed | `8b6b8de0ac006f9c9229284f38997c5b671d9be30e536dd396725af875ae05af` |
| 47 | 7,175 | changed | `6e3de61edfe18bdba53b0e7f25a0e4a1fc71eb667d07c94c945443172f0dc1c5` |
| 48 | 6,429 | changed | `0e8c628ef774bcf31a7acfb0b8014c9be67c86bdfb5a1ed2614c0aa33c1a0315` |

## For the audio queue (stable checkpoint)

Chapters unchanged by the whole-book repair keep the hashes recorded in their movement confirmation files (and the audio-clarity reports for chapters 8, 9, 11, 14, 15, 19, 24). Chapters **changed** by the whole-book repair are marked above; any audio rendered from
the earlier text of a changed chapter no longer matches the accepted text. Already-published Breeze candidates affected: **chapter 1** (two lines: "three of them besides"; "eleven weeks and four days") and **chapter 3** (the Pit added to the occasions of the dream);
chapters 2, 4, 5, 6, 7, 10, 11, 12, 18, 23, 24, 27 and 45 are unchanged by the whole-book repair (chapters 8, 9, 13, 14, 15 and 19, among those near the audio queue's current units, did change). Writing-level narration clarity repairs must still go to Opus before a passage renders; none is pending from this loop.

## Open owner items (recorded, not decided)

The deferred W4 (Pettit as a still door and Yarrow as a hand door against Book One's Kill and still door); the colour "brushed twice" (45:157, 48:311); the certificate precedent (a crossing against the certificate carries no Board consequence); new interaction properties
(reading a count through the still door; "one hold"; Thrale's ward holding water and the flood; packs keeping no count after the bank came out; no fever after two masters touch); the revised bible §6 (the caller need not have crossed); Hollis Vane's absence from the Slack and the
dropped Home Line roll turn; whether the sentence targets govern dialogue (about 60% of dialogue sentences are five words or fewer); the progression density against the book-level 58 (mid-book movements run lower, the opening and the ending higher); the tide clock;
the 41-minute hold; the brown-ink line; "my best machine"; Penhale's ward as frost; the Order's four unanswered questions; the Barrel's yield figure (686.4, chosen above the Flask scale); the new name *Shapter*; the 76/77 age of the Proprietor's reading as written; whether the
last page should lean outward (the hull). The formula's sentence-length targets were never reached in any movement and were not changed.

## Narration clarity acceptance addendum — 2026-10-15 19:55 UTC

The historical table above records the whole-book acceptance edition. These three
rows explicitly supersede it after bounded Opus5.5 prose repairs and independent
Codex textual/continuity rechecks. All other accepted chapter hashes are unchanged.

| Chapter | Current words | Current accepted SHA-256 |
|---:|---:|---|
| 26 | 5,106 | `1ecc21951e2bd781d1e38843691b2564dc564ee0de0e1ab13b6d0707b444d6d3` |
| 27 | 7,280 | `e18bed0e5fa3cf86a3f197953c6b914ce7de0c53080f4cb81dd4945298a9af83` |
| 33 | 8,529 | `67137ebaa52d5fc114fdabeb822e0478b23e83baf4daf22f56289ce3c06965eb` |

The book is now 325,943 words (+10, all in chapter27). Chapter26 corrects the
number of predecessors in a thirteenth run and Tolver's declared stance wording;
chapter27 explicitly places the head handoff/climb before hauling and preserves
declared stance; chapter33 corrects one catcher's She→He pronoun. No plot outcome,
injury, new power or reserved disclosure was changed. Frozen prior editions and
actual Opus sessions/hashes are recorded in AUDIO-CLARITY-26-27-REPAIR.md,
TOLVER-STANCE-26-27-REPAIR.md and AUDIO-PRONOUN-33-REPAIR.md.

Acceptance evidence: narration/AUDIO-STANCE-26-27-RECHECK.md and
provenance/AUDIO-PRONOUN-33-RECHECK.md. Both inspect exact cumulative differences,
changed paragraphs and joins; ready-source recommendations pass. Narration was
separately refreshed and word-locked. This acceptance is for source publication,
not human audience feedback or audio listening approval. Codex orchestrated and
checked; Opus5.5 authored all changed manuscript words.

### Placement addendum — 2026-10-15 22:02 UTC

Chapter37's called head/foot names now agree with executed positions and later
action. Opus5.5 job7c9c2be6 authored only the two-name swap; independent Codex
source/joins recheck passes (AUDIO-PLACEMENT-37-RECHECK.md). Frozen prior source
is retained in editions/audio-placement-37-pre-repair/; exact repair provenance
is AUDIO-PLACEMENT-37-REPAIR.md. This supersedes only37's historical hash:
`c39b066241dc7c1027d462ee855c59303805f5fd14eb0062ead5ee0f738afc21`.
Chapter37 remains6629 words, delta0; total325943. No plot/power/injury/outcome
changes, owner decisions, human feedback or listening approval are implied.
