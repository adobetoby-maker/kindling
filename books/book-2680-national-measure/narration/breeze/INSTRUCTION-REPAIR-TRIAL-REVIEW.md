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

## Second-trial disposition — 2026-10-19T06:04Z

All 14 diagnostic takes and fresh contexts finished, no active process remained.
No candidate has a suspicious isolated omission/addition. The following centers
are restored with exact words or name/homophone/numeric-notation differences:
30 s115 (including repeated shut clause); 33 s025/s193; 34 s008/s122/s127;
35 s002; 38 s139; 39 s079/s098/s099; 47 s096; 48 s039. Chapter 37 s059 still
transcribes who'd for who, so its tense/word boundary is unresolved, not accepted.
The maximum candidate sample peak is .98337 at 39 s098; all samples finite,
but mastering headroom remains unresolved. No production score/take was replaced.

Context 30 and 33 have no additions/omissions. Contexts 34, 37, 47 and 48 include
extra tail material; 39's individual-center windows still include the adjacent
old failed take. Combined-candidate context checks for 39 s098/s099 are now
queued so neither known failed neighbor contaminates the other's check.

## Take localization 003 — completed 06:03:09Z

Seventeen exact original takes were screened separately using named chapter-local
requests/reports, preserving old screening evidence. Results:

- 32 s163, the brief attributed answer, contains the pacing-number-like addition;
  s162 has only Aske/ask and s164 only eighth/eights. Failure now localized.
- 37 s037, the brief reply, contains the numeric direction-like addition. s038
  has a separate rearranged/missing clause; s060 only Carrow/Karo.
- 35 s042 retains I'd/I discrepancy. s044 transcribes exactly in isolation.
- 38 s138 retains I wrote/I'll write and I/I'll discrepancies; s069 has names only.
- 34 s009 has Polglase spelling only; s123 and s128 transcribe exactly.
- Original 39 s098 repeats its sentence in isolated ASR; s099 changes You're/I.
  Both already have clean isolated diagnostic replacements, awaiting combined join.
- 47 s097 and 48 s040 transcribe exactly in isolation. Their long gibberish tail
  additions in larger context are not corroborated; retain evidence and do not
  automatically rerecord these takes or claim human listening established cause.

Measured native below--50-dB tails of these originals are only .03–.54 sec; no
long silent pad was found that alone explains the contextual decoder additions.
The additions cannot be dismissed solely as excessive authored end silence.

## Active third bounded trial

Shell 3739 first runs combined adjacent-candidate checks for batch 2 (39 s098/099),
then one diagnostic take each for 32 s163, 35 s042, 37 s037/s038, 38 s138 in
diagnostic-instruction-leak-v3, followed by isolated ASR, individual neighboring
contexts and combined 37 s037/s038 contexts. Scripts accept --batch 3 and
nm-trial-context.py --combine-adjacent. All operations serialized with offline-qa
lock; no automatic retries, production mutations or publication. Check actual
processes/results before new shared-model work. Existing originals/holds preserved.

Combined batch-2 Chapter 39 windows completed 06:03:46Z. Both s098-centered and
s099-centered windows now use both candidate replacements together and transcribe
with exact ordered words, no additions/omissions/substitutions. This resolves the
known old-neighbor contamination for those windows only; the candidate master,
voice and owner listen remain unapproved. Batch 3 renderer 25989 / parent 25965
is now active in shell 3739; first s163 candidate checkpoint written.

## Third-trial disposition and consolidated local editions — 07:04Z

Batch 3 completed 06:06:07Z, all five neighboring windows at 06:06:44Z, and the
two combined Chapter 37 windows at 06:06:55Z. No model job remained at inspection.
32 s163, 35 s042, 37 s037 and 38 s138 isolated candidates have exact ordered ASR;
the numeric leakage in the two brief replies is absent. 37 s038 still varies
I'd/I'm and want it/one of in isolation; combined context changes it/a in one
window. It is not accepted as exact speech coverage. Batch-3 35/38 context checks
include the old failed neighbor from another diagnostic batch; this is not a new
failure in the replacement center. Cross-batch composition must use all relevant
candidate neighbors together. No blind second render was launched.

To check the repaired passages at chapter scale, scripts/nm-build-repaired-candidates.py
now streams separate provisional editions from existing checkpoints plus all 22
diagnostic center takes across 11 chapters (30,32,33,34,35,37,38,39,41,47,48).
No new TTS, canonical wording changes, time stretching, normalization, production
score edits, original displacement or publishing. The known Chapter 37 discrepancies
remain explicit; inclusion in this experiment is not acceptance or readiness.

Media destination: /Volumes/Drive 2/monroe-ai/national-measure/local-repair-candidates-v1.
Repository metadata: narration/breeze/local-repair-candidates-v1, selection.json
and per-chapter take-manifest/technical-review/asr files. Every original or
replacement take is bound to its hash and source score; assembly preserves order,
five-ms zeroed edge fades and all authored rests, then encodes/decodes MP3.
Full-chapter Whisper screens run sequentially afterward per chapter; all results
remain supervisor-review pending. The evidence is deliberately separate from
published.json and the publication worker queue.

Active shell 76188, parent 32406 at launch; Chapter 30 assembled and began full
ASR at 07:03:13Z. Inspect actual job/checkpoints before additional model work.
The LFS budget hold, existing 47/48 readiness holds, 30/33 held repair requests,
old public candidates, Book One checkpoints and stopped No Path Given are intact.
