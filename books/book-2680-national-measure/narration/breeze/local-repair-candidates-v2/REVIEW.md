# Provisional repair update — changed chapters32/33/48 only

These are separate local QA editions, not approved masters or published files.
Frozen v1 and every production take/score remain unchanged. The other eight
provisional v1 chapter editions are retained in their existing location.

Nine total candidate centers are selected in the three updated chapters. Existing
v1 replacements are carried forward, adding batch4's32 s035, batch5's33 s118,
s147/s216, and batch6's48 s112. Each selection binds canonical source, production
direction, original take and candidate WAV hashes. The only prepared-text change
is33 s118/s216 rank parentheses removal; an exact transformation check plus
normalized word/digit/order equality guards it. No manuscript word changes.

The builder streams original/replacement checkpoints in score order, applies
five-ms edge fades and authored silent joins, then encodes/decodes and screens
each changed chapter. No time stretching, production copy, release markers,
publishing, LFS retry, billing or hosting change. The first launch used a system
Python lacking NumPy and exited before importing the worker or writing artifacts;
the existing Breeze runtime now runs the same bounded job. No duplicate model job.

Whole-chapter ASR is in progress. After it exits, run the CPU ordered-waveform
audit with `scripts/nm-candidate-integrity.py --edition 2` using the existing
Breeze Python. Do not inherit v1 integrity reports for these changed audio hashes.
Further isolated corroboration can use `nm-candidate-triage.py --edition 2`;
nm-breeze-triage.py now narrowly permits only the exact v1/v2 roots, using each
edition's bound take manifest. Context mode still rejects candidate roots.
Do not silently fall back to production WAVs or mutate frozen v1.

ASR ambiguity remains (32 Clerk/clique;33 s216 isolated number homophones), as do
previously logged unchanged word residuals, mastering/headroom, approved-master
pace, identity/naturalness limits and complete owner listen.48 s112's improved
identity windows do not approve the full chapter. Publication budget holds stay.
