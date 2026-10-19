# Sampled naturalness diagnostic — 2026-10-19

Book Narrator objective-QA workflow; owner-selected Breeze overrides the workflow's
Fish default. No production audio changes, automatic pickup decisions, human
listening claim or delivery acceptance follow from this screen.

## Raw result retained

`naturalness-screen-v1/naturalness.json` scored1,152 takes from the frozen
`voice-screen-v1/record.json`: median3.81785, range2.7328–5.0737. These are model
estimates, not human MOS. Its55 flags include30 below the absolute3.15 diagnostic
floor and25 flagged only against the chapter's reference-relative floor.22 flags
are shorter than3 seconds. Only one overlaps the identity screen's50 failures.
Different diagnostic models do not establish an audible defect by agreement or
clear a take by disagreement. Full coverage, naturalness and owner listen remain
unapproved. Raw report SHA256:
`1db79de5d2e88587d537fd5b99c3445bd0b1ba389f4ea7261e1f03b7680c2c2f`.

The ledger predates batches4–6: later candidates must not inherit these results.
All ledger WAV hashes were checked unchanged at completion by the parent process.

## Reference-score confound found

All48 palette roles point to exactly the same locked Calder reference WAV. Yet
the existing checker reports reference estimates2.6827–3.9829 across those roles.
Inspection shows it seeds random generators once, then predicts the same reference
48 times while the crop-selection random state advances. A fixed seed for the
whole run provides repeatable order, not a consistent same-input reference score.
Therefore the varying chapter-relative floors are not evidence of chapter quality.
Do not clear failures or order rerecords from this comparison alone.

`scripts/nm-naturalness-controls.py` runs one bounded follow-up, resetting Python,
NumPy and Torch seeds to42 immediately before every prediction. It repeats the
identical reference3 times, retains all55 original flags, checks10 known-reference
duration crops, and compares original48 s112 with its separate batch6 candidate.
Results are a separate diagnostic; they do not overwrite the raw screen or lower
its threshold. First3 reference repeats are identical3.4474332332611084. Remaining
controls completed; see `naturalness-controls-v1/review.json`.

### Controlled result

All70 predictions completed with input WAV hashes unchanged. The common reference
score gives a3.15 diagnostic floor. Nine of the original55 flagged takes remain
below that floor with this fixed crop selection:01 s032,11 s056,21 s185,29 s049,
31 s035,34 s001,37 s102,38 s001 and38 s028. The original55 flags are not deleted;
changing a crop can change a score and is not a repair or perceptual clearance.
Six of the10 known-positive reference crops also score below3.15, showing the
duration/content confound. Three34/38 heading/short-clip items remain subject to
the same caution.37 s102 is a6.16-second short dialogue/attribution exchange;
it merits focused review, not automatic rerecording based on predicted MOS.

Original48 s112 scores4.1177 and its batch6 candidate4.2101 under the controlled
naturalness check, even though the original's temporal identity windows fail.
This is direct evidence that a naturalness estimate cannot stand in for narrator
identity, correct words, or listening. No take was promoted from these scores.

## Runtime provenance and limits

Existing Drive2 `voice-quality-venv`, UTMOSv2 version1.3.1.dev0 (installation commit
cc2700db57bb83ee13dc31ebe1b868c254e15d09), local CPU predictions, no hosted inference.
Cached fusion_stage3/fold0_s42_best_model.pth SHA256:
`c8149d988e4bbf3f347e6966b5d769de347a5f8c59ffca1dc4bd4bf5b8585e57`.
The checkpoint downloaded once during the initial screen; no package installation
or duplicate rendering environment was required. Very short clips, different
phonetic content and model evaluation crops limit comparisons even after seeding
is controlled. Exact spoken words, joins, delivery pace and perceptual performance
require their own evidence. Existing publication budget holds remain unchanged.
