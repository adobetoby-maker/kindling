# Instruction repair trials — Codex disposition, 2026-10-19

These are local, exact-source-word auditions. No canonical wording, production
score, original take, publication record or live media was changed. Breeze and
Whisper ran sequentially using existing caches. Owner listening remains pending.

## First bounded trial

Three short, non-numeric delivery instructions replaced long operational/scene
instructions in a separate diagnostic folder, not the production score.

- 35 s043: 4.32 sec, peak .5572, ASR exact ordered words. Spoken long direction
  from the old take is absent from the candidate transcript.
- 38 s068: 33.76 sec, peak .7333, no omissions/additions; Halden/Haldan and
  harbour/harbor orthographic differences. Original spatial paragraph restored.
- 41 s056: 23.76 sec, peak .7531, no omissions/additions; brake/break and names
  Talley/Tally, Aske/Ask, Pru/Prue differ orthographically. The opening clause
  replaced by pacing numbers in the old take is now present.

All candidate samples finite. No time stretching. Exact candidate hashes and
input bindings are in diagnostic-instruction-leak-v1/review.json and inputs.json.
Native take pace is approximately 222, 174 and 172 WPM respectively, before
authored chapter rests; these isolated measures do not establish whole-chapter
delivery acceptance against the locked master.

Fresh neighboring contexts used original adjacent takes, diagnostic center take,
the production five-ms edge fades and internal authored pauses, omitting only the
final trailing authored pause from the diagnostic window. Completed 04:58:05Z.
All candidate middle passages are retained in context without instruction text.
41's context has no additions/omissions, only the same homophones/names plus
clerk/clock. 35's preceding I'd/I differs, and both 35/38 contexts include garbled
tail additions after the final expected neighbor. These are unresolved: isolate
the neighboring take/tail and distinguish actual speech from decoder hallucination
before calling the joins passed. Do not silently discard the evidence or promote
these auditions automatically.

## Second bounded trial — active

One candidate each for 14 corroborated failure passages: 30 s115; 33 s025/s193;
34 s008/s122/s127; 35 s002; 37 s059; 38 s139; 39 s079/s098/s099; 47 s096;
48 s039. Short Codex instructions preserve the passage's factual restraint,
repetition, formal-message or reply intention without quoting scene prose or
numeric timing inside instruct. Every source word, voice reference and authored
rest remains unchanged. This is not a bulk acceptance or a pronunciation rewrite.

Job shell 80443, parent 98201 / renderer 98219 at launch, output
diagnostic-instruction-leak-v2. scripts/nm-offline-leak-trial.py --batch 2 performs
one render per passage then isolated ASR; only after it exits successfully,
scripts/nm-trial-context.py --batch 2 checks neighboring windows. The shared
offline-qa lock and busy checks prevent duplicate model work. Inspect actual
processes before launching anything else. No automatic retry, production-copy,
take displacement, assembly or publication. Existing 30/33 repair requests remain
publication-held and are not consumed by this diagnostic run.

Unmapped 32 s163/s164 and 37 s038-window numeric leakage still need take-level
localization. Other lexical/numeric/short-input residuals, mastering, measured
pace, identity/naturalness and owner listen remain open. GitHub LFS budget hold
still blocks 47/48 and replacement publication; no retry/billing change attempted.
