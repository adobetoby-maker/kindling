# Delivery targets remain unresolved

## Decoded pause benchmark — 2026-10-19T13:15Z

`pause-benchmark-v1/review.json` binds the hash-locked approved Calder master and
separate39 v1/32,33,48 v2 candidates. CPU ffmpeg silencedetect used both -40 and
-50dB thresholds, minimum150ms, excluding file-edge intervals from internal pause
quantiles. This is thresholded quiet, not linguistic alignment, breath judgment,
VAD or perceived pace approval. Different content and threshold choices matter.

At -50dB, the approved master has median288ms /P90 653ms internal detected quiet,
9.5% total quiet. The four candidates have median550–686ms /P90 2229–2268ms,
32.6–38.3% total quiet; the -40dB comparison shows the same directional difference.
Candidate overall whitespace-word rates are132.0–138.2WPM, below195–215. Their
non-quiet word-rate proxies are202.7–213.8 at -50dB, but these are **not** measured
articulation rates: quiet breaths/low speech and different source content confound
the calculation. Do not replace an overall-WPM target with this proxy.

Inserted authored rests total333.5/613.85/500.25/354.75seconds respectively. They
are only part of detected quiet; native waveform silence contributes too. Do not
blame every pacing difference on joins, trim speech/meaningful rests, time-stretch
or call the inherited target waived. A native-delivery comparison and any needed
owner preference remain open. Approved-master source word count was intentionally
not inferred from a historical path with changed-source evidence; only its exact
approved audio hash is asserted here. No audio was edited by this benchmark.

## Bounded mastering test — 2026-10-19T09:14Z

Separate Chapter 39 provisional repair edition, no original/publication changes.
scripts/nm-master-audition.py verified the profile and approved-master hash, then
measured the approved MP3 at -20.51 LUFS / -3.26 dBTP. A two-pass loudnorm experiment
on the separate candidate WAV used -20 LUFS / -3.5 dB pre-encode peak ceiling /
LRA7, dynamic amplitude processing where linear gain could not meet both targets.
Encoded 128-kbps mono MP3 measured -20.47 LUFS / -3.83 dBTP, LRA5.8; the existing
technical master verifier passed mono/bitrate/loudness/true peak/no clipping/DC/
ending-hold checks. Exact WAV frames/rate equal input: no time stretching or cut.

Evidence: master-audition-v1/record.json, measurements-before/after.json and
technical-master.json; media separately on Drive 2. This is a one-file technical
mastering method test, not approval of perceived dynamics, full speech coverage,
pace, voice/naturalness, human listening, every chapter or publication readiness.
All other inherited target conflicts below remain open. Preserve the originals.

Checked 2026-10-18. Measurement only; no audio or canon changes.

The selected Original Calder profile at
`/Users/drive/kindling-repo-stage/books/book-01-kindled/narration/kokoro-guided-calder/profile.production-default.json`
specifies overall 195–215 WPM (preferred 208.8), target -20 LUFS, -3 dB
true peak and voice similarity >=0.84. Its approved master hash is
`2f97e38dd47a1e1f29a85d67c2075ee80bcfb5ea833dec1a2c34aed6fd360bf1`.
That profile's renderer is Fish; the owner explicitly selects Breeze for this
book. This engine override is not evidence that the owner listened to and
accepted a slower Breeze delivery, or that every inherited target has passed.

Current 39 chapter publication records measure 127.83–143.07 WPM overall.
This does not meet the inherited numerical pacing range. Meaning-based rests
and native Breeze delivery contribute; do not attribute the entire difference
to joins without measuring speech versus silence. No post-render time stretching.

Full decoded MP3 loudness measurements now include chapters 38 (-21.1 LUFS,
-0.6 dBFS true peak) and 39 (-21.3 LUFS, -0.5 dBFS true peak). The earlier
37-chapter survey remains valid for its exact files. These candidates do not
meet the profile's -3 dB true-peak target. A segment sample-peak/decode pass
does not prove a decoded delivery-master pass.

Before technical closure: measure pacing and pause distribution against the
approved master; test a bounded native-delivery alternative if warranted,
without changing words, voice identity or the owner's intentional landings.
Resolve any required owner preference explicitly rather than calling a pacing
mismatch approved. Test mastering against -20 LUFS / -3 dB true peak without
concealing railed source takes, preserve originals, and hash/verify/publish any
new master. Voice stability, coverage residuals and owner listening also remain
open. No Finished designation is justified by upload completion alone.
