# Monroe narration methods

This document gives the production pieces stable names. An engine is not a
method, a voice is not a method, and a generated MP3 is not automatically a
finished chapter.

## Naming format

Use this order everywhere the reader, manifests, review notes, and release
records display a narration version:

`Process · Performance method · Engine · Voice · Finish state`

The five layers mean:

1. **Process** — how the book is understood, prepared, directed, rendered,
   checked, and reviewed.
2. **Performance method** — how the prose is divided into prepared thoughts and
   how pace is controlled.
3. **Engine** — the local speech model that produces the waveform.
4. **Voice** — the locked speaker identity supplied to the engine.
5. **Finish state** — whether the file is an experiment, has passed objective
   checks, or has also passed the owner's complete listen.

The active production process is **Monroe Book Narrator 1.2.5-CI (Codex
Integrated)**. CI means Codex reads the book context and authors the structured
performance direction before the local voice model renders it.

## Method A — Directed-Paced

### Official label

**Monroe 1.2.5-CI · Directed-Paced · Fish S2 Pro · Original Calder · Finished**

Short UI label: **Calder Directed-Paced — Fish S2 Pro**

Stable method ID: `monroe-1.2.5-ci-directed-paced`

Reference master:

`/Users/drive/kindling/books/book-01/narration/monroe-1.2.5/calder/chapters-01-03/chapter-02/chapter-02.calder.mp3`

### What “Directed-Paced” means

Fish reads the words, but it does not decide the whole performance or the
chapter clock. Codex prepares the book context, selects
performance spans, divides the chapter into complete speakable thoughts, and
writes an explicit pause score. The engine performs each prepared take at
native speed. The final pace comes from the performed takes plus authored quiet,
not from stretching the completed waveform.

The Ember Chapter 2 reference used:

- 2,527 canonical words with no wording changes;
- 130 sentence-prepared takes;
- 1,550 ms sentence landings;
- 2,100 ms paragraph, speaker, and subject resets;
- 2,700 ms written scene breaks;
- four selective 300–340 ms pre-word preparation holds;
- two 1,100 ms thought breaths in the final revelation;
- sparse performance colors: suspense, fear, urgent action, reflection, and a
  restrained final-revelation take;
- measured pace of 149.92 WPM;
- Fish Audio S2 Pro 8-bit at native speed 1.0 and temperature 0.62;
- Original Calder cloned from the locked approved source recording;
- 128 kbps MP3 mastering at the audiobook loudness target, with no waveform
  time-stretch.

### Directed-Paced production sequence

1. **Read the book.** Read the performance bible and the rolling three-chapter
   context so the chapter is performed as part of an arc rather than as an
   isolated clip.
2. **Prepare a word-locked narration copy.** Check every paragraph for one-pass
   listening clarity. Punctuation and paragraphing may expose the intended
   hierarchy; words may not be added, removed, replaced, or reordered.
3. **Direct the chapter.** Mark only meaningful changes in intention, status,
   danger, humor, reflection, intimacy, or tactical pressure. Every temporary
   color must return to the base Calder narrator.
4. **Prepare the takes.** Keep complete sentences and dialogue-attribution units
   together. Avoid unstable one-word takes. Split long material only at a real
   syntactic or dramatic boundary.
5. **Write the pause score.** Assign sentence landings, paragraph/speaker resets,
   scene breaks, and a very small number of pre-word or internal thought holds.
   Pauses serve comprehension or dramatic preparation; they are not decoration.
6. **Render locally.** Fish S2 Pro performs each take from a locked Original
   Calder reference. The engine is asked for an unhurried, intimate,
   conversational read, but measured output—not the prompt—determines the real
   pace.
7. **Assemble natively.** Join take edges with short click-safe fades and the
   authored silence. Do not speed up or slow down the finished speech.
8. **Check the file.** Verify word order and coverage, joins and silence,
   mastering, measured WPM, Calder identity, and synthetic-naturalness outliers.
9. **Listen to the whole chapter.** Make pickups only at exact failed takes,
   preserve accepted takes, and recheck both joins.
10. **Finish.** Use `Finished` only after the owner has listened and no pickup is
    open.

### Why it sounds different

This method makes the chapter feel intentionally performed because every new
thought has a prepared start and a complete landing. Fish still supplies the
voice and micro-prosody, but the director—not the model's default streaming
rhythm—controls the larger musical structure and clock.

## Archived comparison — Directed-Native

### Official label

**Monroe 1.2.5 · Directed-Native · Qwen3-TTS 1.7B · Clear Calder · Archived Audition**

Short UI label: **Clear Calder Directed-Native — Qwen3**

Stable method ID: `monroe-1.2.5-directed-native`

Historical Kindled comparison candidate:

`/Volumes/Drive 2/monroe-ai/auditions/kindled-book-one-kokoro-guided-calder-qwen/chapter-01.mp3`

### What “Directed-Native” means

The same book understanding and scene direction are present, but the pace score
is sparse. The chapter is divided into larger thought or paragraph-sized takes,
and the TTS model controls most sentence-level timing inside each take. Authored
silence is reserved for scene changes, selected tactical landings, and rare
pre-word emphasis.

The current Kindled Chapter 1 Qwen candidate used:

- 3,837 canonical words;
- 43 thought-sized takes;
- eight directed scene or emotional spans;
- a 530 ms ordinary take landing;
- selected 670 ms tactical landings;
- 1,200 ms written scene breaks;
- one 350 ms pre-word preparation hold on “down and back”;
- Qwen3-TTS 1.7B Base 8-bit at native speed 1.0 and temperature 0.72;
- Clear Calder cloned from the same locked Original Calder source and an
  approved performance-reference palette;
- measured pace around 216 WPM;
- no waveform time-stretch.

### Directed-Native production sequence

1. Read the book performance bible and rolling chapter context.
2. Produce the same word-locked, one-pass-clear narration copy.
3. Direct a small number of full scene spans: humor, reflection, investigation,
   suspense, urgent action, and intimate care.
4. Keep larger complete thoughts together. Let Qwen decide ordinary sentence
   breaths and internal cadence within each take.
5. Add only structural pauses: scene breaks, a few tactical landings, and rare
   pre-word preparation.
6. Render locally with the locked Calder reference and performance palette.
7. Assemble at native duration; never time-stretch the speech.
8. Run the same coverage, mastering, identity, naturalness, and pacing checks.
9. Listen to the complete chapter and repair only failed takes.
10. Keep the result labeled `Audition` until it passes the full listen and the
    owner promotes that exact audio hash.

### Current status

This lane is not eligible for new production. The Qwen candidate passes
technical mastering and Calder identity. Its text check found no suspicious
omission or added passage on adjudicated review. It is not `Finished`: two
curiosity takes remain below the current automated naturalness reference floor,
and its measured pace is just above the current Directed-Native target ceiling.
Human comparison is still useful, but the evidence must remain attached to the
audition.

## The practical distinction

| Layer | Directed-Paced | Directed-Native |
| --- | --- | --- |
| Who controls the large clock? | Authored pause score | Mostly the TTS engine |
| Typical take size | Sentence or complete dialogue unit | Thought or paragraph group |
| Ordinary sentence landing | Explicit | Model-native |
| Structural pauses | Dense and measured | Sparse and selective |
| Reference pace | About 150 WPM | About 210–216 WPM |
| Best use | Final audiobook performance | Fast audition and voice comparison |
| Current reference engine | Fish S2 Pro | Qwen3-TTS 1.7B |
| Current reference voice | Original Calder | Clear Calder |
| Current state | Finished reference | Audition |

## Finish-state vocabulary

- **Audition** — listenable comparison; objective or human review remains open.
- **QA-cleared** — all applicable automated gates pass; owner listening remains.
- **Finished** — exact audio hash has passed objective review and the owner's
  complete listen; no pickup remains.

Never use `Finished` to mean only “the render command ended.”
