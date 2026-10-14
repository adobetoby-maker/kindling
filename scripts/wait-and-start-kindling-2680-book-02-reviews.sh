#!/bin/zsh
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
book_root="$repo_root/books/book-2680-national-measure"
claude_bin="/Users/drive/.local/bin/claude"
editorial_prompt="$book_root/planning/OPUS-5.5-MOVEMENT-001-EDITORIAL-REVIEW.prompt.md"
cold_prompt="$book_root/planning/OPUS-5.5-MOVEMENT-001-COLD-READ.prompt.md"

while ! "$claude_bin" auth status 2>/dev/null | grep -q '"loggedIn": true'; do
  sleep 10
done

cd "$repo_root"

"$claude_bin" \
  --bg \
  --model opus \
  --effort high \
  --permission-mode acceptEdits \
  --name "National Measure Movement One Editorial Review" \
  --add-dir /Users/drive/penname \
  --append-system-prompt-file "$editorial_prompt" \
  "Execute the appended informed editorial and numerical-formula review. Read all eight chapters and supplied canon in full. Do not alter manuscript prose. Save the complete report to books/book-2680-national-measure/provenance/MOVEMENT-001-EDITORIAL-REVIEW.md. Do not commit, push, repair, or draft later chapters."

"$claude_bin" \
  --bg \
  --model opus \
  --effort high \
  --permission-mode acceptEdits \
  --name "National Measure Movement One Cold Read" \
  --append-system-prompt-file "$cold_prompt" \
  "Execute the appended fresh-context simulated cold read. Use only the supplied manuscript. Do not alter manuscript prose. Save the complete report to books/book-2680-national-measure/provenance/MOVEMENT-001-COLD-READ.md. Do not commit, push, repair, or draft later chapters."
