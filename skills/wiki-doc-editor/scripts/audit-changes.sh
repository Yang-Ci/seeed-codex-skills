#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "error: run this script inside a Git repository" >&2
  exit 2
}
cd "$repo_root"

base_ref="${1:-}"
if [[ -z "$base_ref" ]]; then
  if git show-ref --verify --quiet refs/remotes/upstream/docusaurus-version; then
    base_ref="upstream/docusaurus-version"
  elif git show-ref --verify --quiet refs/remotes/origin/docusaurus-version; then
    base_ref="origin/docusaurus-version"
  elif git rev-parse --verify HEAD^ >/dev/null 2>&1; then
    base_ref="HEAD^"
  else
    base_ref="HEAD"
  fi
fi

git rev-parse --verify "$base_ref^{commit}" >/dev/null 2>&1 || {
  echo "error: base ref '$base_ref' does not resolve to a commit" >&2
  exit 2
}

echo "Repository: $repo_root"
echo "Branch: $(git branch --show-current)"
echo "Base: $base_ref"
echo
echo "Worktree status"
git status --short
echo
echo "Committed branch diff"
git diff --stat "$base_ref"...HEAD
git diff --name-status "$base_ref"...HEAD
echo
echo "Staged changes"
git diff --cached --name-status
echo
echo "Unstaged changes"
git diff --name-status
echo
echo "Whitespace check"
git diff --check "$base_ref"...HEAD
git diff --cached --check
git diff --check
echo
echo "Generated build artifacts in worktree"
build_artifacts="$(git status --porcelain=v1 | sed -E 's/^.. //' | rg '^sites/[^/]+/build(/|$)' || true)"
if [[ -n "$build_artifacts" ]]; then
  printf '%s\n' "$build_artifacts"
else
  echo "none"
fi
echo
"$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/check-locale-sync.py" "$base_ref"
