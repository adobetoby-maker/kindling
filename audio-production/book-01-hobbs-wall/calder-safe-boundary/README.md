# Hobb's Wall — local Calder continuation repairs

These records cover the chapter 19–28 continuation prepared on 21–22 September
2026. A chapter is published only when its directory and matching MP3 are
present; this document is not itself a claim that all chapters have landed.

## Reproducible process

1. Keep the canonical manuscript unchanged and bind its SHA-256 to the existing
   local Qwen3-TTS 1.7B Base 8-bit Calder HQ render. Preserve the original voice
   reference, performance palette, chunk ledger, and established 0.90 tempo.
2. Align the continuous recording with local Whisper large-v3-turbo. For a
   failed neighboring-word match, use a bounded source-conditioned timing pass.
   That timing pass is **not** evidence that the words were spoken correctly.
3. Apply the existing 450 ms comma / 800 ms sentence minimum-rest targets only
   where at least 20 ms of waveform-confirmed quiet permits a safe splice.
   A zero crossing in voiced speech is not a safe splice. Preserve native
   delivery wherever no safe boundary is found; record every retained boundary.
   No additional time stretch is introduced. Keep the original speech sequence.
4. Save a lossless master and 128 kbps mono MP3, target −20 LUFS / −3 dBTP.
   Audit inserted digital silence before encoding and central silence after
   MP3 decoding. Preserve natural breaths outside inserted rests.
5. Independently transcribe the **final** MP3 without a supplied source prompt.
   Check ordered source coverage, missing/added passages, excessive gaps and
   ending hold. Run technical mastering checks. Check native-take voice identity
   and sampled UTMOS naturalness against the locked reference.
6. Inspect any flagged passage with an unprompted transcription of a focused
   final-audio crop. A false-positive adjudication retains the original failing
   report, the exact flag, audio/source/crop hashes, focused transcript and
   justification. It does not erase the failure or lower the general QA gate.
7. Publish only checksum-matched, passing chapters to the regular canonical audio
   path. Pin library metadata to an immutable commit and use measured durations,
   not a 64 kbps file-size estimate. Verify full public SHA-256 and HTTP 206
   byte-range support before accepting the release.

## Transcription findings

- Chapter 19: long-form ASR timestamp drift falsely placed two “Why” utterances
  together; focused final-audio alignment and waveform confirmed the pause.
- Chapter 24: ASR wrote a spoken number as `104` and the character name as
  `Wyke`; it also invented a sentence boundary absent from the manuscript.
- Chapter 25: long-form/gap-recovery ASR falsely duplicated the spike sentence;
  focused transcription found it once. One pause flag was invented punctuation
  and another was timestamp drift with a real waveform-confirmed pause.
- Chapter 26: focused unprompted final-audio transcription recovered the complete
  flagged passage; the surrounding matched excerpt had 100% coverage after
  normalizing only the spelling of grey/gray and Toren/Torrin.
- Chapter 28: ASR invented a sentence ending after “line”; the source and focused
  final-audio transcript both have a continuous clause there.

Chapter 18's separate original-profile directory retains its own duplicate-ASR
adjudication; its MP3 was not changed during this repair pass.

## Limits and provenance

Rendering, alignment, audio post-production and quality models are local. No
ElevenLabs, remote TTS, cloud audio enhancement, or manuscript rewriting is used
in this repair pass. The assistant selected and implemented the repair/QA
procedure; this is not a claim of local-only authorship of the manuscript.

The pause pattern is intentionally **not** exact at every punctuation mark.
Every unmodified unsafe boundary is listed in the chapter record. UTMOS and voice
identity are sampled objective checks, not human listening or DMOS ratings.
Human listening approval and physical iPhone background-playback verification
remain separate from automated release checks.

The deployed library already contained separate wording edits in chapters 16–18
and 20–23 compared with this saved canonical narration source. This audio-repair
pass does not overwrite those edits. The app manifest records both manuscript
hashes and an explicit match flag. Chapters 19 and 24–28 match the narration
source exactly; these hashes distinguish edition drift from a TTS omission.

Scripts are in `/Users/drive/kindling-narrator-stage/scripts/`:
`apply-aligned-pause-score.py`, `repair-pause-alignment.py`,
`repair-and-check-hobbs.py`, `publish-repaired-hobbs.py` and
`reconcile-hobbs-release.py`. The complete local run, lossless masters and focused
audio crops are retained under
`/Volumes/Drive 2/monroe-ai/productions/kindled-calder-090-450-800-20260920/`.
