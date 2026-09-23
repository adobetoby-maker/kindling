# Monroe 1.3 substantive revision card — Movement D

Compiled chapters 45–50; Hobb's Wall source chapters 21–26.

Review mode: substantive editorial self-review, not an independent cold read. The immutable comparison point is commit `2f42770`. The repository-level `universe/UNIVERSE_BIBLE.md` is authoritative where the compiled-book context differs.

## Chapter dispositions

| Chapter | Disposition | Before | After | Added | Removed | Net |
|---|---|---:|---:|---:|---:|---:|
| 45 | `REPAIR` | 4,176 | 4,165 | 35 | 46 | -11 |
| 46 | `TIGHTEN` | 3,481 | 3,468 | 15 | 28 | -13 |
| 47 | `REPAIR` | 3,589 | 3,597 | 9 | 1 | +8 |
| 48 | `REPAIR` | 3,993 | 3,992 | 33 | 34 | -1 |
| 49 | `REPAIR` | 4,433 | 4,440 | 18 | 11 | +7 |
| 50 | `REPAIR` | 4,669 | 4,674 | 7 | 2 | +5 |
| **Movement** |  | **24,341** | **24,336** | **117** | **122** | **-5** |

Before/after totals use `wc -w`. Added and removed totals use Git's porcelain word diff against `2f42770`; replacements count on both sides.

## Located problems and material fixes

- **Chapter 45:** the fire tableau counted five people although six were present; the bread-order correction said both that Toren and Milo were last; and several crucial physical sequences buried their order inside long coordination chains. The pass corrected the party count, changed Milo's correction to “next to last,” and rebuilt the bar recovery, Senna's removal from the cart, and Milo's placement and breathing assessment into consecutive actions. The assault geography, Milo's choice, the unheard farewell, his death, Vera's stone, and the Tull confrontation remain unchanged.
- **Chapter 46:** the knife reversal and Toren's run back to the north side required a listener to retain multiple subjects and changes before reaching a stop. Both were rebuilt into short causal units without changing hesitation, timing, casualties, Rook's choice, or the spear strike. Tull's testimony and Rook's two distinct accounts—the public bill and the private truth—were protected.
- **Chapter 47:** seven reachable bodies and the eighth body in the reeds shared an ambiguous pronoun chain, making it briefly possible to read the burial labor as handling eight bodies before Toren later says seven. The unreachable eighth body is now explicitly located outside safe reach. Milo's cairn, the bread ritual, Marta's flask, Toren's physical grief, Wyck receiving Elias's name first, and the departure remain intact.
- **Chapter 48:** the culvert paragraph said Toren's Edge had never emitted light and never would, while Chapter 50 depends on him deliberately lighting the same spike. The paragraph now distinguishes the dark metal shape from its narrow optional edge-light: useful as a weapon, inadequate as a lamp, and dangerous to kindle in the Sag. This reconciles the existing climax without giving Toren a new power. The Sag signs, strut training, one-and-a-half-second changeover, grief scene, and ninety-one-pace reveal were protected.
- **Chapter 49:** “broke off” could momentarily read as the damaged limb detaching rather than the creature abandoning its attack. More importantly, the text used `Barrel` as the creature name, contrary to the authoritative bible's separate terms: a **Breach** is the creature and **Barrel** is its yield grade. Both meanings are now explicit. The revetment geometry, Wyck's failed plant, Dessa's reversed-rule discovery, Toren's successful read, injuries, and first-light arithmetic are unchanged.
- **Chapter 50:** “Thirteen days old, with a bowl in your hands” attached grammatically to Toren and could momentarily make him sound thirteen days old. It now explicitly refers to the age of his Ember. Rook's four-part instruction, Pitch's death, Toren's simultaneous Edge/Stride breakthrough, his decision to protect the group rather than take the easy strike, the Ember's extinguishing, the ash arithmetic, and the closed Meridian gate were protected.

## Change anatomy

- **Additions:** 117 words, all local clarifiers or connective language inside existing scenes; no new scene, outcome, motive, or lore event.
- **Cuts:** 122 words, chiefly coordination scaffolding and repeated subject setup in action passages.
- **Replacements:** fifteen bounded locations across the six chapters, including two continuity corrections, one power-description reconciliation, and one canon-vocabulary correction.
- **Sentence rebuilds:** the Chapter 45 spur fight and medical aftermath, Chapter 46 knife reversal and north-bank run, Chapter 47 body count, Chapter 49 withdrawal and threat naming, and Chapter 50 opening reference.
- **Paragraph rebuilds:** one—the Chapter 48 culvert paragraph, rebuilt to distinguish Edge-light from useful illumination while keeping Milo's absence as the landing.
- **Unchanged protected passages:** Milo and Rook's brothers conversation; Milo's decoy argument and death speech; Rook's confrontation with Tull and refusal to arrange it into virtue; the bread and name rituals; Toren and Wyck on the rail; the Sag's three signs; the Hallam Cross combat rule; Toren's changeover breakthrough; the ash recovery; and the Meridian handoff.

## Unresolved canon questions

1. `books/book-01-kindled/UNIVERSE_BIBLE.md` calls Rook's dead partner Satori Kess, while the authoritative repository bible and the manuscript call her Vera Kess and reserve *Satori* for the state/object. This pass followed `universe/UNIVERSE_BIBLE.md`; the compiled context still needs synchronization.
2. The book-specific bible records the owner-ratified metal-form/edge-light distinction, but the repository-level bible has not yet absorbed that detail. Movement D already required the distinction because Chapters 48 and 50 otherwise contradicted each other. The canon files should be synchronized before later books rely on edge-light behavior.
3. `STATE_LEDGER.md` remains a pre-book ledger. It does not yet track Milo's death, Rook's injuries and revealed name, Wyck's injuries, Pitch's death, Toren's spent Ember, or the party's arrival at Meridian; it should be rebuilt from the accepted revised edition before Book Two continuity work.

Toren's missing door at the end of Chapter 50 is intentionally unanswered on the page, not treated here as a continuity error.

## Continuous-read verdict

Movement D now carries one uninterrupted line of consequence: Milo's chosen light buys the arch; the cost forces Rook's embodied choice; burial and ritual keep that cost present on the road; grief exposes the missing light; training names the one-and-a-half-second limit; the Breach exploits that limit; and Toren's refusal to choose between Edge and Stride pays off the movement's instruction under pressure. The entry pressure, escalation, turn, climax, and closed-gate handoff all survive. The revised action is easier to stage on one reading, the protected emotional passages remain restrained, and the power and threat vocabulary is internally coherent. The movement is suitable for owner review; narration preparation should remain word-locked to the accepted substantive edition afterward.

## Completion checks

- Changed manuscript files: `revised/chapter-45.md` through `revised/chapter-50.md`.
- Audit file: `editor/substantive/movement-d.revision-card.md`.
- Frozen `chapters/chapter-45.md` through `chapters/chapter-50.md`: unchanged.
- Compared against frozen sources, punctuation candidates/reports, performance summaries, and baseline commit `2f42770`.
- Chapter headings, scene-break structure, chronology, and final narrative beats: preserved.
- Scenes silently removed: none.
- Narration markup or timing controls added: none.
- `git diff --check`: clean at movement completion.
