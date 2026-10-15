# Direct National Measure chapters 4–6 for local Breeze

Owner authorizes complete local audio and publication of every ready chapter.
You are the Codex performance director. Work only in this book's narration tree,
not its manuscript, planning, provenance, or git state. Use apply_patch for edits.
Do not delegate to agents, invoke another model, render, publish, commit or push.

Read fully:
- /Users/drive/.codex/skills/book-narrator/SKILL.md and its linked workflow.
- narration/performance-bible/book-performance-bible.md (provisional local-model
  context; verify key facts against prose and never treat it as canon).
- manuscript/chapter-04.md, chapter-05.md, chapter-06.md in reading order.
- narration/contexts/chapter-04.context.md through chapter-06.context.md.
- narration/monroe-1.2.5/calder/chapters-04-06/run.json and BREEZE-OVERRIDE.md.
- /Users/drive/penname/pennamecodexv3/schemas/narration-clarity-item.v1.schema.json.

Read all three chapters BEFORE directing any. Complete paragraph-level clarity
reviews in the initialized run, one entry per prose paragraph, with honest exact
locations, explanation and word-locked prepared text. Adopt clear punctuation
corrections from context; preserve words and sequence. Send any wording repair to
writing-monroe-feedback.md rather than changing canon. If clarity cannot resolve,
save the concrete blocker and do not mark that chapter ready. Do not invent A/B
choices merely because punctuation changes sound.

Prepare the narration copies, sparse chapter performance tracks and a brief
unit-level performance bible with source hashes and characterization derived from
actual reading. Deliberate, clear Calder narration; character color is restrained
and every return resets to base narrator. Use complete thought units and retain
dialogue-attribution clauses together. Do not break sentences mid-clause just to
hit a token count. Do not direct a caricature or change narrator identity.

Also produce a ready-to-render Breeze direction track for each clear chapter:
`narration/breeze/chapter-04/direction.json`, and similarly chapters 02, 03.
Schema: top-level schemaVersion=1, bookId="kindling-2680-book-02", chapterNumber,
source (absolute canonical path), sourceSha256, director="Codex", directionPolicy,
segments. Each segment contains id="s001" etc, speaker, text, instruct,
pauseAfterMs. Metadata directions never enter spoken text. Plain text removes
Markdown presentation only; preserve canonical spoken word sequence, including
heading. No added dialogue or plot. Prepared punctuation may differ while keeping
the same word sequence. Base identity: Original Calder, warm restrained
Australian-English; native synthesis, no waveform time stretching.

Start with 1550 ms completed-sentence/thought landings, 2100 ms paragraph/speaker/
subject restart and 2700 ms written scene breaks, larger boundary wins. Mark only
real selective pre-word preparations of 300–340 ms; avoid separating an attribution
from dialogue. Keep enough context per segment for natural performance, and keep
text under about 700 characters at a meaningful boundary wherever possible.
Reset instruction to base narrator after temporary dialogue/emotion. Match scene
meaning rather than inserting commas on a quota.

Validate normalized spoken words against canonical source independently for every
chapter and record word-lock hash/coverage and all actual validation commands in
`narration/breeze/chapter-NN/preparation-review.json`. Validate the initialized run
with /Users/drive/penname/harness/book-narrator.sh validate when applicable.
Only after actual reading, clarity and direction are complete and word lock passes,
write `direction.ready` inside that chapter directory, containing sourceSha256.
If any step is incomplete, leave no ready marker and state the exact next action.
Do not call audio complete or claim a human listen. Finish with exact paths and
the ready/blocked state of each chapter. Write no novel prose.

Preserve every other unit, script, worker and ready/rendered artifact. The previous unit is actively rendering. Use distinct validation/preparation helper filenames for this unit. Read its new run.json and use only its paths; do not edit chapters 1–3 or mark unseen prose reviewed. Current book bible covers accepted chapters 1–16; chapters 17–24 are drafts and remain outside this audio task.
