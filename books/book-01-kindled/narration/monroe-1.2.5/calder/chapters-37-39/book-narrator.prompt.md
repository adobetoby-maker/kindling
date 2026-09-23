Activate Monroe Book Narrator 1.2.5 for **Kindled**, chapters
37, 38, 39, using **Calder**.

Read `/Users/drive/penname/pennamecodexv3/workflows/book-narrator-1.2.5.md` first, then read `/Users/drive/git-backups/kindling/books/book-01-kindled/narration/monroe-1.2.5/calder/chapters-37-39/RUN.md` and every selected
source chapter before acting. If a book performance bible does not exist, build it from
the complete available manuscript before chapter direction.

For each selected chapter, perform the clarity loop first. Write one JSON object per
prose paragraph to its `clarity-review.jsonl`, following `/Users/drive/penname/pennamecodexv3/schemas/narration-clarity-item.v1.schema.json`. The
prepared narration copy must preserve the exact word sequence. Put any wording-level
repair in `writing-monroe-feedback.md`; do not hide it in the narration copy.

Punctuation is part of the performance score. Recover the intended hierarchy from the
paragraph, scene, three-chapter movement, and book arc. If misplaced run-on commas flatten
distinct actions or direct the wrong oral meaning, classify the word-locked repair as
`punctuation-correction` and adopt it even when the sound changes materially. Use
`performance-choice` only when context leaves two readings genuinely viable; then keep
the source score in `preparedText`, put the alternative in `alternatePreparedText`, render
both with identical settings and context, and wait for owner selection.

Only when blocking clarity feedback is resolved, create sparse performance direction
using the chapter's rolling context and `/Users/drive/kindling-narrator-stage/docs/audio-coaching/calder-delivery-coach.v1.json`. Render through
Local Qwen voice ID `calder-original-fifteen-anchor-v1` with native speed
1.0. Treat that speed as a hint: measured delivery against the
approved master is the authority. Never time-stretch the finished audio.

Run objective audio checks, then listen in full. Log exact pickups in
`listening-review.md`, redo only failed passages, recheck joins, and loop until clean.
Report the output paths and any still-open Writing Monroe feedback.
