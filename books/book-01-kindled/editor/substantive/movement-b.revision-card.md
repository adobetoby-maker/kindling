# Monroe 1.3 substantive revision card — Movement B

Compiled chapters 26–33; Hobb's Wall source chapters 07–14.

Review mode: substantive editorial self-review, not an independent cold read. I read the Monroe editor instructions, substantive-pass README, universe bible, state ledger, all eight performance summaries, the frozen source chapters, the punctuation baseline, and the current revised movement before editing. I edited the revised files in reading order, then reread chapters 26–33 continuously and checked the chapter 25/26 and 33/34 joins. The immutable comparison point for counts and change accounting is commit `2f42770`.

## Chapter dispositions

| Chapter | Disposition | Before | After | Added | Removed | Net |
|---|---|---:|---:|---:|---:|---:|
| 26 | `KEEP` | 3,036 | 3,036 | 0 | 0 | 0 |
| 27 | `KEEP` | 3,184 | 3,184 | 0 | 0 | 0 |
| 28 | `KEEP` | 2,660 | 2,660 | 0 | 0 | 0 |
| 29 | `REPAIR` | 6,191 | 6,210 | 46 | 27 | +19 |
| 30 | `KEEP` | 3,220 | 3,220 | 0 | 0 | 0 |
| 31 | `REPAIR` | 2,456 | 2,457 | 12 | 11 | +1 |
| 32 | `REPAIR` | 3,409 | 3,405 | 3 | 7 | -4 |
| 33 | `REPAIR` | 3,263 | 3,265 | 2 | 0 | +2 |
| **Movement** |  | **27,419** | **27,437** | **63** | **45** | **+18** |

Before/after totals use `wc -w` per file. Added and removed totals use Git's porcelain word diff against `2f42770`; replacements therefore count once on each side.

## Located problems, material fixes, and protected strengths

### Chapter 26 — `KEEP`

- Located problem: none requiring prose intervention. The chapter's long coordinations remain hierarchical on a single read, and the shifts from autonomous line work to Milo's night role, rank language, Toren's stillness drill, and Dessa's fear of being left behind are cleanly staged.
- Material fix: none.
- Edit classes: unchanged.
- Protected strengths: the cold-fire opening; Senna and Dessa in the cart; `The bridge went great`; Milo learning to call first and hold the light high; the rank conversation; Garrick's Torch status set against his two-minute stand; Toren's quarter-hour hold; Dessa's arithmetic of injury; Rook meeting her at eye level; the closing instruction to do nothing.

### Chapter 27 — `KEEP`

- Located problem: none requiring prose intervention. The steading fight clearly motivates Toren's false `hold it harder` model, the test disproves it, and Dessa's quiet four-second breakthrough remains physically and emotionally legible without explanatory expansion.
- Material fix: none.
- Edit classes: unchanged.
- Protected strengths: Dessa's nine-minute opening; Toren's brief competence before the light-targeting reversal; Milo keeping his light; Rook testing rather than lecturing; the exchange of stones; the domestic scale of Dessa's light; Rook's hand over his mouth; the next-morning shift into specific instruction for Wyck.

### Chapter 28 — `KEEP`

- Located problem: none requiring prose intervention. The tally, the redistribution of group roles, Wyck's inventory lesson, Toren's Ember threshold, and the orchard briefing advance in a clear causal sequence.
- Material fix: none.
- Edit classes: unchanged.
- Protected strengths: Garrick's paper; the five-bar gate; Dessa becoming part of the drill rather than an obstacle around it; Wyck's water-end question; `It's an inventory. I do it with the mule`; the sack carry and surprise fall; the warm-stone realization; Wyck's quiet response to remaining Kindled; the final promise that Rook will explain the orchard while everyone is warm and unhurt.

### Chapter 29 — `REPAIR`

- Located problem: four action descriptions treated the Ember's visible light as if it were the blade or forearm structure itself. That conflicts with the locked two-part Edge canon: moving metal supplies the weapon form, while a narrow local edge-light supplies the working edge and is distinct from Blaze-rank body light.
- Material fix: rebuilt those four descriptions so Rook's and Toren's metal forms arrive first and thin light kindles only along the working edge. Toren's crisis surge still changes the spike, braces his forearm, empties his reserve, and ends on exactly the same tactical and emotional result.
- Edit classes: 4 replacements; 4 sentence rebuilds; no paragraph rebuild.
- Protected strengths: the fire-side Stilts lesson; the line drawing and tapped ditch; Toren's correct hedge call turning into dangerous confidence; orchard geography; Stilt foot mechanics; the concealed-ditch reversal; Milo's and Dessa's calls; Toren's error and two-kill overdraw; Wyck holding the gap; the three-door explanation; injury and recovery costs; the debrief's distinction between knowing and doing while afraid; the unfinished `What I had wrong` close.

### Chapter 30 — `KEEP`

- Located problem: none requiring prose intervention. The recovery summary is economical, the Drum's burn pattern is clear, and Cinder Company's name alters Rook's behavior through observable restraint rather than explanatory narration.
- Material fix: none.
- Edit classes: unchanged.
- Protected strengths: Toren's gradual refill; Wyck being made to report his hand; Dessa's quarter-mile return to the mule's head; Ott's voice and trade knowledge; the difference between flat and level; the exact Flask-and-a-half payment; Wyck's reading of the purchase; Senna's warning not to force the name that week; Rook facing south with the chit.

### Chapter 31 — `REPAIR`

- Located problems: Toren's internal inventory reduced the exact price of the company chit from a Flask and a half to half a flask, and the same sentence ended with a broken attachment (`a lesson ... that Toren had not been able to sleep properly since`).
- Material fix: restored the amount as something the brass `had cost`, rather than what it was worth, and completed the final causal clause as a lesson that had kept Toren from sleeping.
- Edit classes: 1 sentence rebuild containing 2 factual/syntactic replacements; no paragraph rebuild.
- Protected strengths: the three uneventful days; the tally becoming weather; Wyck's refusal to forget Rook's earlier trade; Toren reaching the one-house/three-doors inference himself; the 110-mile arithmetic; Dessa's uncertainty about her breakthrough; Toren and Wyck's almost-comfortable fire talk; `what am I standing in a line for`; the third-watch close.

### Chapter 32 — `REPAIR`

- Located problem: the Toren/Wyck drill was called ninety seconds, its first two stated stages already consumed fifty seconds, the takedown took another second and a half, and Rook then called the whole event nine seconds. The three clocks could not describe the same action.
- Material fix: made the drill one coherent thirty-second sequence: twenty seconds of nothing, about eight seconds of play, then the second-and-a-half takedown. Rook now names the same thirty-second interval in the debrief.
- Edit classes: 2 exact duration replacements; 1 clause compression; no sentence or paragraph rebuild.
- Protected strengths: the delayed confrontation; the disciplined camp read; Dessa isolating the one claim Rook cares about; the targeted straw coat; the honest-monster/deceptive-person distinction; Wyck's weaponized apology and immediate remorse; Milo learning to place his light away from his body; the group unconsciously facing outward; Rook turning north.

### Chapter 33 — `REPAIR`

- Located problem: Wyck said Rook had finished the eight-day survival phase `before Hobb's Wall`, but those eight days of shoving-and-shouting instruction occurred at Hobb's Wall and were complete before the group left it.
- Material fix: inserted `we left`, preserving Wyck's cadence while making the chronology exact.
- Edit classes: 1 bounded insertion; no sentence or paragraph rebuild.
- Protected strengths: the man-drill opening; Wyck's controlled public challenge; Rook admitting the course, its personal purpose, and his unreadiness; the three promises; Dessa identifying departure as evasion; Senna's accounting of twenty-two watches; Wyck's `all five at once` condition and dropped bar; the easier camp after acknowledgment; Dessa's distinction between a secret and imposed doubt; Toren's disk pressure; Rook holding the chit still.

## Change-class summary

- Additions: 63 words, limited to the Edge metal/light distinction, the exact ash price, completed syntax, and the Hobb's Wall chronology marker.
- Cuts: 45 words, chiefly the contradictory all-light Edge wording and incompatible drill-duration phrases.
- Replacements: 4 Edge descriptions in chapter 29; price and syntax inside 1 chapter-31 sentence; 2 duration values and 1 timing clause in chapter 32; 1 chronology phrase in chapter 33.
- Sentence rebuilds: 4 in chapter 29 and 1 in chapter 31.
- Paragraph rebuilds: none.
- Unchanged protected passages: all of chapters 26–28 and 30; every training plant and payoff; Dessa's Satori touch; both Ember-rank recognitions; the complete orchard action and aftermath; the Cinder Company reveal; the three-door teaching; the cold-camp lesson; Wyck's confrontation; all chapter-ending narrative beats.

## Unresolved canon questions

1. Nell's ordinary ownership rule says Toren's Ember is a grey stone in another person's hand, yet Rook uses Satori Kess's Ember and Dessa briefly activates that same Ember. The scene strongly suggests the exception is purposeful, but the exact mechanism remains unstated. Future canon should decide whether the exception comes from Satori's state/object relationship, Rook and Satori's Heartfire, Rook's Blaze breadth, or another already-planned rule; this pass did not invent an answer.
2. Toren's orchard overdraw temporarily produces a thinner, longer, non-ugly Edge form with metal running back over his forearm while he is still named Ember rank. The current rank bible reserves a deliberately chosen, reliable refined shape for Flame/Fire. The prose is compatible with an involuntary crisis reshaping that Toren cannot sustain or repeat, but future canon should confirm whether this is a transient overdraw, the onset of his next rank change, or an allowed variation of his single unrefined form.
3. `STATE_LEDGER.md` still contains only the pre-Chapter-1 opening state and says no chapters have been drafted. It supplies no post-Movement-B continuity record for Dessa's leg, Wyck's arm, Toren's depletion and recovery, the group's ranks, the changed route, or the Cinder Company trail. This pass did not alter the append-only ledger because the assignment limits edits to the eight revised chapters and this revision card.

## Continuous-read verdict

The movement works as one escalating training-and-consent unit. Chapter 26 transfers tactical authority from Rook to the four young people and makes competence a distributed group property. Chapters 27–28 turn stillness into Dessa's breakthrough and Toren's Ember threshold while letting Wyck's lack of a visible job accumulate pressure. Chapter 29 converts every training plant into a readable orchard fight, then proves that instruction shortens failure rather than abolishing it; Toren and Wyck advance through different doors at real physical cost. Chapter 30 reintroduces Cinder Company through a trade scene and changes the direction of Rook's attention. Chapters 31–32 widen the Path, expose the route deception, and turn training from honest Riftspawn toward deceptive people. Chapter 33 makes the withheld course an explicit consent problem and resolves only the denial, not the secret.

The post-edit read retains Toren's road arithmetic, Rook's restraint, Dessa's exactness, Wyck's flat pressure, Milo's vulnerable utility, Senna's dry authority, spacious action, and the intentional repeated-conjunction cadence. The four repaired Edge passages now agree with the metal-plus-edge-light canon without changing the orchard choreography. The chapter-to-chapter residue is continuous: Dessa's assigned stillness becomes the four-second light; Toren's warmth leads into the orchard overdraw; the injury costs lead into the Drum; the chit turns the watch from south to north; and the north-facing watch forces Wyck's public challenge. The alternating-protagonist joins at 25/26 and 33/34 remain clean, and no final beat changed.

Verdict: **movement ready for owner review**, with the two reserved Ember/Satori and rank-transition mechanism questions carried forward rather than solved in prose.

## Completion checks

- Changed manuscript files: `revised/chapter-29.md`, `revised/chapter-31.md`, `revised/chapter-32.md`, and `revised/chapter-33.md`.
- Reviewed and deliberately unchanged manuscript files: `revised/chapter-26.md`, `revised/chapter-27.md`, `revised/chapter-28.md`, and `revised/chapter-30.md`.
- Frozen `chapters/chapter-26.md` through `chapters/chapter-33.md`: unchanged.
- Chapter headings, scene-break counts, and final narrative beats: unchanged.
- Removed scenes: none.
- New lore, power, motive, outcome, or major event: none.
- Narration markup or timing controls added: none.
- `git diff --check`: clean.
