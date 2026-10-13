#!/bin/zsh
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
prompt_rel="books/book-2680-national-measure/planning/OPUS-5.5-MOVEMENT-001.v2.prompt.md"
prompt_path="$repo_root/$prompt_rel"
expected_hash="13a2e2da3a5ad945308256278c027ec42b618929fa7215c202f5c7d6f1e821e2"

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code is not installed." >&2
  exit 1
fi

if ! claude auth status 2>/dev/null | grep -q '"loggedIn": true'; then
  echo "Claude Code is not logged in. Run: claude auth login" >&2
  exit 2
fi

actual_hash="$(shasum -a 256 "$prompt_path" | awk '{print $1}')"
if [[ "$actual_hash" != "$expected_hash" ]]; then
  echo "Refusing to launch: compiled prompt hash changed." >&2
  echo "Expected: $expected_hash" >&2
  echo "Actual:   $actual_hash" >&2
  exit 3
fi

cd "$repo_root"

exec claude \
  --bg \
  --model opus \
  --effort high \
  --permission-mode acceptEdits \
  --name "Kindling 2680 Book Two Movement One" \
  --add-dir /Users/drive/penname \
  --append-system-prompt-file "$prompt_path" \
  "Execute the compiled Movement One authoring assignment now. Read the appended prompt in full, write complete chapters 1 through 8 and the required continuity/provenance records, and stop at the packet's stop condition. Do not commit, push, publish, review, score, or repair."
