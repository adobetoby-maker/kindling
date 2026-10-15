# Kindling 2680, Book Two — Movement Six consolidated repair (the ending)

You are Claude Opus 5.5, returning as the prose author for *The National Measure*, public
byline Monroe Jackson, internal seat Monroe Jackson 1.3.0 / O'Connor 1.3.0. This is one bounded
same-author repair of the completed sixth movement, the book's ending (Chapters 41–48). Do not
begin another book. Do not redesign the movement. Do not launch subagents or other models; no Skill
tool is available; you repair and report yourself. Read both review reports and all eight chapters
before editing.

## Required evidence, in this order

1. `books/book-2680-national-measure/provenance/MOVEMENT-006-EDITORIAL-REVIEW.md` (informed,
   same-family; Section 3 findings C1–C15 and the ending table, Section 4 numbers, Section 6 brief)
2. `books/book-2680-national-measure/provenance/MOVEMENT-006-COLD-READ.md` (manuscript-only simulated
   read, same model family, not human feedback; Section 3 items 1–10 and its three priorities)
3. `books/book-2680-national-measure/provenance/MOVEMENT-006-CONTINUITY.md`
4. `books/book-2680-national-measure/STATE_LEDGER.md` (Movement Six block), `UNIVERSE_BIBLE.md`,
   `BOOK_MAP.md` (§3 Complete ending), `CHARACTERS.md`, `packets/MOVEMENT-006.md`
5. `books/book-2680-national-measure/manuscript/chapter-41.md` through `chapter-48.md`, completely
   and in order

The exact first draft is frozen, read-only, under
`books/book-2680-national-measure/editions/movement-006-first-draft/` with `SHA256SUMS.txt`. Never edit
it. Edit only the working files `manuscript/chapter-41.md` to `chapter-48.md` and the records named under
Deliverables. Chapters 1–40 are accepted and closed: do not touch them unless a located contradiction
forces a one-line fix, and record any such touch. (Another session has made small audio-clarity edits to
some earlier chapters; they appear as uncommitted changes. Do not touch or revert them.) Line numbers in
the reviews are first-draft numbers; find passages by their text.

Measuring script: `provenance/tools/m6_metrics.py` (`python3 -I provenance/tools/m6_metrics.py manuscript`;
its viewpoint map is keyed to first-draft section numbers, so remap in a scratch copy if you join or split
sections and say so). Run it before the first edit and after the last. It is a heuristic, not a gate.

## Three repair priorities (the whole job)

### 1. Make the climax obey its own rules (line edits; no event, outcome, time or cost changes)

- **The Master's forty paces and the sill plank (ch. 41 ~l.223; ch. 43 ~l.113–117, 147; ch. 44 ~l.407).** The
  rule is that she lays down every door within forty paces, and the sister paces forty from the sill; but from
  5.50 she stands on the stone above the dock mouth, high above the sill, while three still doors open into that
  sill beneath her and none lies down. Keep her back along the outer quay (about sixty paces from the sill) until
  the plant is called: at ch. 43 "stopped well back along the outer quay, by the gate's moorings, sixty paces from
  the sill, where she had said she would wait"; at ch. 41 Yeo adds "She'll wait back on the outer quay till the
  sill's planted"; at ch. 44 ~l.407 "came along the outer quay and down the steps". Kiva's "seventy paces off on the
  basin wall" can stay.
- **The cask's height (ch. 43 ~l.269, 301; ch. 44 ~l.25, 75, 139).** It stands four feet eleven by Hart's level,
  Polglase's call, the prediction and the box, yet is written "over her head", "over their heads", "the height of a
  man", "as tall as a man". Use eye- or chin-level phrasing ("level with her eyes", "to their chins", "taller than a
  child and as wide as a cart"); the passage that says "past the height of Anwen's shoulder" is right.
- **The Master's limit, broken without a price (ch. 45 ~l.279–293; ch. 43 ~l.119).** "She can't hold it and move"
  (ch. 41), "she did not move, because she could not" (ch. 45), then she steps back one pace; and the sister's "if
  she couldn't keep to it she'd say so first" is dropped when she overruns by fourteen minutes. Price the step ("the
  grey across the mouth shivered from wall to wall, and the flood came a hand nearer before it held") or have the sister
  lower the request ("She says she can step if it's one pace and slow"); at about 6.50 let the sister say, flatly, "She
  says she'll be late. She's saying it first."
- **Where Carrow and Dray stand (ch. 43 ~l.143):** "Further along the wall toward the Graving, above the place where the
  tear would be open" puts them at the mast's end, but the tear lies back toward the pump house: "Back along the wall
  toward the pump house, above the place where the tear would be open".
- **"Lying down" since the ward (ch. 45 ~l.145, 299):** Kiva held her still door open against the pull until the cut at
  6.16 and read the cask's count through it, so "had lain down since the ward came up" and "forty-nine minutes" are wrong:
  "had lain down since the cut" / "forty-eight minutes".
- **The second plant (ch. 44 ~l.175–213; cold-read priority 1):** Kiva tests the granite sill (ch. 43, "Second mark… It's
  good") but plants kneeling in the slurry "at the sill's foot", an untested place, which contradicts her rule from ch. 41
  ("If my fingers say a mark keeps time, it's not a mark"); and Wace is "a pace back on the dock floor" and "behind her".
  Put the second plant clearly on the tested granite (she kneels on the sill's edge; or one clause names the risk of an
  untested spot and the choice), and make Kiva's and Wace's positions picturable in one reading.
- **The deadline (ch. 45 ~l.83 and ~l.101):** Mara: "by twenty-four… there's time"; Kellan: "If you lift at twenty-four,
  there's not." Mara's sum is right (the still water is needed for the salt and the count to 6.28; the pumps may start
  after). Kellan: "If you lift after twenty-four, there's not."
- **What Mara hears (ch. 45 ~l.9):** Mara on the landing hears Aske's quiet "*one*" … "*ten*" from about 120 paces across the
  basin, though he "did not raise his voice" (ch. 44 ~l.315) and Kiva could not hear Perrin's declaration from the dock floor.
  Have Mara hear *of* the count (Polglase's call) or remove it from what she hears.
- **A section outside Kiva's view (ch. 44 ~l.215–221):** "Kiva did not see any of them" breaks the movement's rule; keep it
  in her knowledge ("She knew afterward…") or cut the sentence to what she can see.
- **The cost of the first crossing (cold read open question):** Aske forecasts that the seventh "went past the elbow" and would
  begin within the hour, but the page never shows that cost or its replacement by the second crossing's cost. Add at most two
  sentences where the cost is carried so the reader is not left unsure. Likewise Jude's and Gower's grey-wrapped fists (~l.355):
  show the aftermath in one clause if it is already implied.

### 2. Make the sums, clocks and records true (smallest edit each)

- **Saturday's lane, reversed (ch. 41 ~l.273):** "Twenty-Eight had beaten Seven in a lane on Saturday" is false (Seven won 6–5;
  Dray: "That's the fairest lane I've ever lost"); "Halden License had beaten everybody" is false (Halden was second). →
  "Twenty-Eight's blade had beaten Seven's catcher in a lane on Saturday"; "Halden License had beaten nearly everybody".
- **Clocks and counts (editorial C4 a–k):** ch. 44 ~l.305 "made it eleven minutes ago" → "at eleven minutes past"; ch. 48 ~l.57 Carrow
  "eleven minutes on that seam" → "four minutes"; ch. 44 ~l.349 "She ran forty paces" vs ~l.353 "thirty-four paces" → "She ran up the
  dock floor"; ch. 43 ~l.207 "a hundred and forty paces" → "a hundred paces" (the continuity file claims this was corrected; it was not);
  ch. 42 ~l.169 Lyle "eight days ago" → "six days ago"; ch. 48 ~l.205 "Three weeks in the shop" → "A fortnight in the shop"; ch. 46 ~l.297
  "Hers for a year and a half" → "Hers for a year"; ch. 44 ~l.203 "six times on sanctioned masts" → "a dozen times on sanctioned masts" (thirteen
  by the ledger); ch. 46 ~l.63 Aske "had combed it at the gate on the first day of the Measure" → "It had been combed at the gate the day they
  came" (a Board clerk combed it, ch. 17); ch. 47 ~l.293 Pike's hands "half closed… since the second month" → "since the gate".
- **From the cold read:** the Clerk says the paper was sealed "ten days before it came" (ch. 46 ~l.259): it was sealed on the 11th and the
  slack came on the 23rd, twelve days. Hart tells Orla "I heard. Noa Bexley told the landing at noon" (ch. 46 ~l.315) before the Chair
  struck the line at four, and at noon Hart was at the box on the timber pond, not on the landing: make the sequence true. Perrin's "first
  line under the limits" is "It can't be done by strangers" (ch. 41 ~l.275) while ch. 47 ~l.133 and ch. 48 ~l.227 name "A caller who has been
  inside both gaps" as the first line: make them agree. "four girls and Yarrow" (ch. 43 ~l.247) implies five on a plank of four: fix. The daily
  yes/no hour is "a quarter to seven" in the morning (ch. 41, ch. 46) but "Thursday evening… because it was the hour" at ch. 48 ~l.267: make the hour
  consistent or say why it moved. The Chair's two entries (ch. 46 ~l.295 and the one before) call the same mast "sanctioned" and the event "not a
  sanctioned event": make the wording read as the distinction it is.
- **The prediction's last line "wrong, twice" (ch. 46, optional):** by the paper's instrument (the hand on the grating) the line failed once (6.16–6.22,
  the pumps). Give Hart one clause ("By my hand, once. By what we did, twice. I'd want both written.") or leave it as a choice.
- **Two carried-over corrections never made (continuity §0):** ch. 45 ~l.95 "the two who held it before me" → "the man who held it before me" (canon, ch. 23:
  "when the man who kept it before me died with his hand on this glass"); and reconcile the continuity file and ledger.
- **Two small plan payoffs (one line each, only if natural):** Carrow and Kiva each use a piece of the other's method (BOOK_MAP §9): at ch. 48 ~l.57–61,
  Kiva: "Your lay's how the planks kept her count." Peverell's promised "seven columns" before the Board (ch. 41 ~l.185) may be paid in a clause at
  ch. 48 ~l.205 (Rusk's sheet). Hollis Vane's absence from the Slack is an owner item: leave it.
- **Records, not prose:** reconcile `provenance/MOVEMENT-006-CONTINUITY.md` §0 and the Movement Six block of `STATE_LEDGER.md` to every change you
  make.

### 3. Lighten the coda's repeated shape and the house voice (narration and speeches; line edits)

- **Closing restatements (editorial qualification 2; cold-read priority 2):** about a dozen after-scenes end by stating their lesson after the action
  has shown it. Cut or shorten the last line of four or five: Pike (ch. 47 ~l.339, "That's the whole of it. Two people watching the other one's far
  edge…"); Anwen (ch. 48 ~l.243–247, "In two places. Not one of us for the other."); Perrin (ch. 47 ~l.285, "I'd like it known that I was nearly wrong,
  and wasn't… That's how I know it's mine."); Jude (ch. 46 ~l.205–207, "I think that's what it's for."); and the narration or Kiva's book that writes the
  lesson after the scene has said it (ch. 41 ~l.345–347, ch. 47 ~l.129–133). Keep each action and the image that ends it.
- **"I'd want" (about 24 across eleven speakers; 21 of the "want it said/known/written" family in the cold read):** recast about two-thirds in each speaker's
  register, keeping Jude's four, Dray's "I'd want that clear", Rhea's "I'd want it on every card" and the Proprietor's "where it happened". Pru "went scarlet" four
  times in ch. 48: keep two. Give the resolution scenes of ch. 46–48 different shapes where they share one (someone offers, someone declines or accepts, someone
  says it should be written): vary the endings, do not cut the scenes.
- **Summary chains and heavy paragraphs:** split the four summary chains (ch. 47 ~l.153, ~l.291; ch. 46 ~l.139; ch. 48 ~l.77); break each speech over about 150 words
  once with a gesture or interruption; ease the heaviest paragraphs (ch. 41 ~l.243, ~l.139, ~l.75; ch. 47 ~l.179; ch. 48 ~l.165; ch. 46 ~l.263; ch. 43 ~l.95) by splitting at
  the natural pause. No *and … and* chains over about 45 words.
- **Re-reported evidence:** compress the three-accounts paragraph at the box (ch. 46 ~l.263–267) to one sentence naming the three sources; reduce the opening of the sealed
  paper (ch. 46 ~l.215 onward) where it re-reports events the reader watched an hour earlier; ease the long position map in ch. 43 (~l.131 onward) if it can be done without
  losing a bearing the climax needs. Do not shorten any pass in ch. 44 or the lift in ch. 45.
- **Chapter 43's clock (editorial C8):** §4 opens "At ten to six" but §5 opens "At a quarter to six Yeo blew one long note": "At a quarter to six Yeo had blown…", or reorder.
- Leave dialogue length alone until the owner rules.

## Strengths to protect

"One morning of somebody who won't" and "It's the first job I've ever been offered that's exactly what I'm for."; Mara's bucket with no bottom; Brask's "The water's its head. And the
head's keeping time."; Rusk: "You might have opened your eyes." / "I'd not have heard it better."; the rope drill and "That's strangers stopping."; "It's not going to the nearest thing. It's
going to the nearest thing that keeps time."; "Unless they keep its count."; "If this morning needs my three, it's not a method. It's me."; "That was a girl saying no to a rich man. This is a catcher
saying no to a method."; the quiet going out of the stone "the way warmth goes out of a cup"; "Two words, once." / "That's the easy part."; "Say you can't tell. That's a word as well."; Bannock's "It's
water" / "Tomorrow it won't be"; Lyle's "I'm saying it before"; Aske's ten-count with the price inside it; Perrin's "it's mine as well"; "the way a lamp goes when somebody turns the key the whole way
down"; Pike's "Far edge"; "It's one hold. Not two"; "Twenty-two"; the Master's "Write that you counted, and that you don't know what."; the prediction read verbatim and judged honestly; the Clerk's "That's
a better record than most sealed papers"; "I've believed one thing for seventy-seven years… I'm only no longer the man who owns it."; *Used, 1.2. Left, sealed, 0.8. Bound as before.*; the Tanyard (ch. 47 §8)
entire; "Davy never did the corners"; "It doesn't make the Bench right." "No." "Good."; "Graywater's mine. You're not."; Coombe's "That's a better first line than mine was"; Kellan's watch "four seconds behind… he
knew which four"; Mara's knock "as a joke"; Pru "I did not"; *Then we look again, and either of us may say no.*; and the last section (ch. 48 §6) **word for word**, from the ninth *no answer* to *The disk is
cold.* Retain Kiva's voice, the crew's warmth, character agency and the full length of every pass in ch. 44 and the lift in ch. 45.

## Boundaries

- No change to any event, outcome, date, ash total, power limit, injury, knowledge boundary or reserved disclosure beyond the located corrections. The Slack's course, who fails, who lets go, the
  point of light, the grid order, the commission and its two conditions, where each of the four goes, the tin (used 1.2, left 0.8, bound), Aske's card (one in fourteen days), the hand gone to the wrist for three weeks,
  the disk cold, the hull and the last section stay. No new chapter, scene, revelation, named person, power or subplot. No wholesale rewrite. Three doors remain three clean; no fourth.
- Do not modify plans or canon to excuse prose errors. Owner-protected wording stays exact.
- **Owner items — not for you to decide; record any you touched or left:** the colour "brushed twice" (ch. 45 ~l.157, ch. 48 ~l.311); the certificate precedent (the second crossing against the certificate carries no
  Board consequence); new interaction properties (reading a count through the still door; the Proprietor's "one hold"; Thrale's ward holding water and the flood; packs keeping no count after the bank came out; no
  fever after two masters touching); the revised bible §6 (the caller need not have crossed); Vane's absence from the Slack; whether the sentence targets govern dialogue; the progression shape and density.

## Deliverables

1. Repair the working files `manuscript/chapter-41.md` through `chapter-48.md`, in reading order.
2. Write `provenance/MOVEMENT-006-REPAIR.md`: runtime-reported model and session/job identifier (say plainly if unverifiable); each factual correction with its evidence; what was clarified, recast,
   split and cut, by chapter and section; before/after `wc -w` per chapter and for the movement; before/after metrics from the script (all text, narration, paragraph median and share over 60 words, chains over 45
   words, breaks per 10k); counts before and after for "I'd want", "did not say anything", "went scarlet", "on the table"; every requested item left unchanged, with the reason; confirmation that the frozen
   edition was not modified (`shasum -a 256 -c SHA256SUMS.txt`); final hashes of the eight chapters; and a quote-parity scan of ch. 41–48 (an odd count of double quotes in a paragraph that does not open a
   multi-paragraph quotation) returning zero.
3. Reconcile `provenance/MOVEMENT-006-CONTINUITY.md` and the Movement Six block of `STATE_LEDGER.md` to the surviving prose where a repair changed what they state. Add a repair entry to `AUTHORSHIP.md`. Do not
   claim recheck, acceptance or publication.

When finished, stop. Do not commit, push, publish, or draft forward.
