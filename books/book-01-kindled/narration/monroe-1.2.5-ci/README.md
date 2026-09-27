# Kindled — Monroe Book Narrator 1.2.5-CI

Production label:

`Monroe 1.2.5-CI · Directed-Paced · Fish S2 Pro · Original Calder`

Codex reads each canonical chapter with its rolling book context and authors the
performance direction. The pacing compiler then makes the chapter clock explicit:

- 1,550 ms sentence and complete-thought landings;
- 2,100 ms paragraph, speaker, and subject resets;
- 2,700 ms written scene breaks;
- selective 320–340 ms pre-word preparations.

Fish Audio S2 Pro 8-bit performs the prepared takes locally at native speed with
the locked Original Calder source and local Calder performance anchors. Finished
speech is never time-stretched. Qwen is not part of this production lane.

The production queue is resumable and hash-bound. `QA-cleared` still requires the
owner's complete listen before the exact audio hash may be labeled `Finished`.

Only one Fish model download is used. Multiple worker processes share the Hugging
Face cache and load separate in-memory model instances; duplicate downloads do not
increase throughput.

Initialize or inspect the queue:

```bash
python3 run-kindled-monroe-1.2.5-ci.py --status
```

Launch a bounded two-worker test:

```bash
python3 run-kindled-monroe-1.2.5-ci.py --launch-workers 2 --limit-per-worker 1
```

Continue the complete book after checking aggregate throughput:

```bash
python3 run-kindled-monroe-1.2.5-ci.py --launch-workers 2
```

After a bounded benchmark is already rendering, schedule the full two-worker
queue to begin as soon as those current renders finish:

```bash
python3 run-kindled-monroe-1.2.5-ci.py --defer-workers 2
```
