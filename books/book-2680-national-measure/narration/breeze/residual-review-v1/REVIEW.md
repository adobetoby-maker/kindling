# Exact-edition residual review packet

21 selected unresolved hypotheses now have lossless local context clips on Drive2,
bound in `record.json` to exact canonical source, chapter MP3, assembled WAV,
ordered take hashes and sample offsets. They include full previous/center/next
checkpoints and the existing authored rests, cut only at complete checkpoint
boundaries. No speech trimming, new fades, stretching, direction, canon or
production audio changes. Frozen editions v1 and v2 remain preserved.

Chapters32/33/48 use v2, the others their selected v1 editions. This specifically
fixes the evidence mismatch where an older original-neighbor context was used
around a center now adjoining replacement audio:33 s215 now has v2's new216,
and37 s038/059 now use their actual selected candidate centers and neighbors.
These clips are not themselves approved pickups or new published audio.

The21 clips total1,014.26seconds, including overlapping contexts; this is neither
unique coverage nor final book duration. They are a focused review aid, not a
complete owner listen or an exhaustive queue of every possible audio problem.
The reason strings are ASR/identity hypotheses, not proven audible defects.
All short-clip identity and naturalness flags remain in their separate raw reports.

One serialized, cached Whisper view is running through
`scripts/nm-residual-packet-asr.py` (offline-qa.lock). It uses the actual review
clip hashes, retains all decoder differences and cannot replace or accept audio.
Inspect `asr-review.json` when it completes. Do not repeat a bounded attempt or
rerender automatically to chase recognition spellings. A complete owner listen
and the pending delivery preference remain separate requirements.
