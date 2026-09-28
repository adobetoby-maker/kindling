# Meridian — final whole-book copy corrections

Date: 2026-09-28

The final whole-book audit accepted the novel for the owner/listening edition and
identified three copy-level continuity errors. Codex applied only the exact fixes; no
scene, plot, capability, ledger, viewpoint or outcome changed.

1. `manuscript/chapter-10.md`
   - Meridian's horse count now reads **nine**, matching the later departure scene in
     chapter 24 and preserving the earlier Movement Three repair's selected count.
   - Final words: 8,376.
   - SHA-256: `782d11b1a8e1bb6815681a2ca8e987b75dbbefc68396bca62a19f0a7856eeb88`.

2. `manuscript/chapter-46.md`
   - Doctor Keel's examination uses `she/her` consistently.
   - Sowerby's comparison uses Tilda's actual first head picture on D+1, not the D+13
     review day.
   - Two adjacent listening clarifications: `fourth bed on the left`; `did not sleep at
     first` before Callie later falls asleep.
   - Final words: 5,377.
   - SHA-256: `ff335814549a8dcaffd52d51be4c74e5c93f927d5ebfba2c572f4935b58ab6f2`.

3. `manuscript/chapter-24.md`
   - Verified unchanged from its accepted post-Movement-Three count: **nine** horses.
   - Final words: 8,135.
   - SHA-256: `8e4dc59814c207f389ef9cf915be17de7bfc9eb3ef4c4346be6b6ed6bc2c7abe`.

Validation:

- Full manuscript: **317,695 words**.
- `git diff --check`: clean.
- The frozen movement editions remain untouched; they preserve pre-repair/pre-copy
  snapshots by design.
