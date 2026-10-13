#!/usr/bin/env bash
set -euo pipefail

dry_run=false
build_all_locales=false
base_ref=""
for argument in "$@"; do
  case "$argument" in
    --dry-run) dry_run=true ;;
    --all-locales) build_all_locales=true ;;
    -h|--help)
      echo "usage: $0 [--dry-run] [--all-locales] [base-ref]"
      exit 0
      ;;
    *)
      if [[ -n "$base_ref" ]]; then
        echo "error: provide at most one base ref" >&2
        exit 2
      fi
      base_ref="$argument"
      ;;
  esac
done

repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "error: run this script inside a Git repository" >&2
  exit 2
}
cd "$repo_root"

if [[ -z "$base_ref" ]]; then
  if git show-ref --verify --quiet refs/remotes/upstream/docusaurus-version; then
    base_ref="upstream/docusaurus-version"
  elif git show-ref --verify --quiet refs/remotes/origin/docusaurus-version; then
    base_ref="origin/docusaurus-version"
  else
    base_ref="HEAD"
  fi
fi

git rev-parse --verify "$base_ref^{commit}" >/dev/null 2>&1 || {
  echo "error: base ref '$base_ref' does not resolve to a commit" >&2
  exit 2
}

changed_files="$({
  git diff --name-only "$base_ref"...HEAD
  git diff --cached --name-only
  git diff --name-only
  git ls-files --others --exclude-standard
} | sed '/^$/d' | sort -u)"

changed_files="$(printf '%s\n' "$changed_files" | rg -v '^sites/[^/]+/build(/|$)' || true)"
if [[ -z "$changed_files" ]]; then
  echo "No source changes detected."
  exit 0
fi

declare -A selected=()
if $build_all_locales; then
  while IFS= read -r locale; do
    selected["$locale"]=1
  done < <(
    find sites -mindepth 2 -maxdepth 2 -name package.json -printf '%h\n' \
      | sed 's#^sites/##' \
      | sort -u
  )
else
  for locale in en zh-CN; do
    [[ -f "sites/$locale/package.json" ]] && selected["$locale"]=1
  done
fi

if [[ ${#selected[@]} -eq 0 ]]; then
  echo "No affected locale site detected."
  exit 0
fi

mapfile -t locales < <(printf '%s\n' "${!selected[@]}" | sort)
echo "Base: $base_ref"
echo "Build locales: ${locales[*]}"

if $dry_run; then
  exit 0
fi

command -v yarn >/dev/null 2>&1 || {
  echo "error: yarn is required for this repository" >&2
  exit 2
}

wiki_build_root="$(mktemp -d -t seeed-wiki-build.XXXXXX)"
trap 'rm -rf -- "$wiki_build_root"' EXIT

for locale in "${locales[@]}"; do
  output_dir="$wiki_build_root/$locale"
  echo "Building sites/$locale -> $output_dir"
  yarn --cwd "sites/$locale" build --out-dir "$output_dir"
done

echo "Selected locale builds passed. Temporary output removed on exit."
