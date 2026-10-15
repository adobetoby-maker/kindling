#!/bin/zsh
# Launch one National Measure Opus 5.5 child as a background job.
# usage: nm-launch.sh "<job name>" <prompt path relative to repo root> "<task instruction>" [--resume <session-id>]
set -euo pipefail
repo_root="$(cd "$(dirname "$0")/.." && pwd)"
name="$1"; prompt_rel="$2"; task="$3"; shift 3
prompt_path="$repo_root/$prompt_rel"
[[ -f "$prompt_path" ]] || { echo "missing prompt $prompt_path" >&2; exit 1; }
claude auth status 2>/dev/null | grep -q '"loggedIn": true' || { echo "claude not logged in" >&2; exit 2; }
echo "prompt_sha256=$(shasum -a 256 "$prompt_path" | awk '{print $1}')"
cd "$repo_root"
exec claude --bg --model opus --effort high --permission-mode acceptEdits \
  --name "$name" --add-dir /Users/drive/penname \
  --disallowedTools EnterWorktree ExitWorktree Agent Workflow Skill \
  --allowedTools Read Edit Write Glob Grep \
    "Bash(python3:*)" "Bash(wc:*)" "Bash(grep:*)" "Bash(rg:*)" "Bash(shasum:*)" "Bash(diff:*)" \
    "Bash(cmp:*)" "Bash(ls:*)" "Bash(cat:*)" "Bash(head:*)" "Bash(tail:*)" "Bash(date:*)" \
    "Bash(mkdir:*)" "Bash(sort:*)" "Bash(uniq:*)" "Bash(tr:*)" "Bash(git diff:*)" "Bash(git status:*)" "Bash(git log:*)" \
  --append-system-prompt-file "$prompt_path" "$@" "$task"
