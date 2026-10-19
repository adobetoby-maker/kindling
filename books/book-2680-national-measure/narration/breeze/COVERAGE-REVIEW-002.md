# Offline coverage review 002 — 2026-10-19

All 48 current local recordings now have whole-chapter and isolated-flag ASR
screens, bound to their current source/audio hashes. All are review-pending,
not coverage approvals. Local duration totals 142,598.38 seconds (39:36:38.38).
Only chapters 1–46 were previously live verified; 47–48 remain unpublished.

The offline drain completed at 03:01:41Z. No synthesis or publication ran.
Chapter 38's repaired s123 contextual screen differs only in Aske/ask spelling;
this supports the bounded peak repair, not whole-chapter approval.

Codex reviewed isolated transcripts against the exact corresponding score text.
The following are material flags, distinct from names, possessives, homophones,
and numeric notation. A second contextual pass is running in shell 38392,
PID 35079 at launch, using named `coverage-002` request/review files so earlier
context evidence is preserved. Do not duplicate that model job.

- 32 s163/s164: contextual decoder includes numeric pacing-like words absent
  from the source; determine whether this belongs to the neighboring short take.
- 34 s008/s122/s127: ledger repetitions, major corruption in repeated
  "She could have" passage, and repeated signature; check neighboring audio.
- 35 s002/s043: isolated speech includes core direction and long scene intention
  instead of canonical opening prose. Clear instruction-channel leakage candidate.
- 37 s038/s059: missing/rearranged clause and extensive spoken scene/delivery
  direction instead of canonical prose.
- 38 s068/s139: extensive spoken delivery/scene intention; s123's earlier peak
  repair did not address these different takes.
- 39 s079/s098/s099: year expansion, possible repeated short narrative, and
  You're/I discrepancy need context; not yet pickup decisions.
- 41 s056: source opening replaced by numeric pacing-like text.
- 47 s096: long appended scene intention absent from canonical words.
- 48 s039: repeated "Not mine to keep" in isolated transcript.

Other residuals remain in the individual isolated reports, including 40 s077
missing "both", 43 s088 missing ledger initial K, 45 s017 added "and", 46
s016 a/her and s157 who'd/who, liked/like. Do not silently accept these or infer
all unchecked takes passed because the full screen did not flag them.

Publication readiness for 47/48 and replacement requests for 30/33 remain held.
Worker 70030 is no longer present at this checkpoint; do not restart publishing
under blocked LFS access. Reconcile processes before eventual recovery. No Path
Given remains stopped. Further repair should preserve old takes and score/hash
history, use short non-spoken instruction only, and recheck replacement plus
joins. No new pickup or audio mutation was authorized by this ASR pass itself.

Mastering, measured pace versus approved master, identity/stability/naturalness,
full spoken-word resolution and owner listening remain open. No Finished claim.

## Context pass outcome and bounded trial

The named context pass completed 03:55:39Z, all nine chapters. Extensive direction
leakage in 35 s002/s043, 37 s059, 38 s068/s139 and 47 s096 is corroborated;
41 s056's numeric replacement and 48 s039's repeated final sentence also recur.
34 s008 repeats a ledger clause, s122 remains corrupt, and s127 has additional
garbled material in context. 32's pacing-like material repeats in overlapping
windows; isolate neighboring takes before attributing it to s163 or s164.
37 s038's window likewise includes numeric instruction-like material from a
potential neighbor. 39 s079's year expansion and s098/s099's repeated narrative
plus changed reply recur. These remain exact-source/audio-bound findings, not
proof every decoder-only tail addition is spoken.

A non-publishing trial of three short, non-numeric instructions is now running
via scripts/nm-offline-leak-trial.py, shell 63288. Targets: 35 s043 (short opening),
38 s068 (long spatial paragraph), 41 s056 (numeric-instruction leak). Exact
source words, pauses and voice reference retained; original scores/takes never
modified. One diagnostic take per target, then serialized ASR. Outputs live in
diagnostic-instruction-leak-v1. Initial loader failed before any take because it
was pointed at the Whisper cache; the same trial resumed once with the existing
/Users/drive/.cache/huggingface Breeze cache offline. Failure log and explicit
cache-recovery record preserved; no download and no blind audio retry loop.
Inspect this process/results before loading another model. Results require Codex
review and cannot replace production takes or bypass the publication hold.
