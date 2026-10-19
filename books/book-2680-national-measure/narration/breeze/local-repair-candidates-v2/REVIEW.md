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

Whole-chapter ASR, CPU ordered-waveform audits and isolated corroboration completed
2026-10-19T13:13:24Z. All three structural checks pass exact ordered checkpoints,
five-ms fades, authored silent joins and total frames within one PCM16 quantization
step. This is not a spoken-word or perceptual acceptance. Combined duration of the
three changed candidate chapters is10,751.65seconds, not whole-book duration.
Whole ASR ordered-coverage ratios:32 .9744,33 .9605,48 .9736. These are decoder
screens, not literal missing-word counts. Of37 isolated selected takes,17 match
after normalization and20 retain differences. Original words and reports remain.
Further isolated corroboration can use `nm-candidate-triage.py --edition 2`;
nm-breeze-triage.py now narrowly permits only the exact v1/v2 roots, using each
edition's bound take manifest. Context mode still rejects candidate roots.
Do not silently fall back to production WAVs or mutate frozen v1.

ASR ambiguity remains (32 Clerk/clique;33 s216 isolated number homophones), as do
previously logged unchanged word residuals, mastering/headroom, approved-master
pace, identity/naturalness limits and complete owner listen.48 s112's improved
identity windows do not approve the full chapter. Publication budget holds stay.

Newly selected isolated flags include33 s165 no/now, s212 seeding/seating and
s215 and/than; do not hide these among proper-name spelling differences.
32 s091 still lacks K and s046 drams/drums remains uncertain. A bounded original-
neighbor context check completed13:15:03Z and retains those five differences.
33 s212's context also decodes I/or in unchanged neighbor211; do not attribute
that to212.32 s046 has an uncorroborated context-only gibberish tail, absent from
its isolated take; this is not automatically an audible instruction leak. It is not
a v2 join audit:33 s215's original following216 differs from v2's replacement216.
48 crooked/crook and zero/note-point residuals remain explicitly unresolved.
