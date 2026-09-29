# Seeed Wiki Repository Map

Read this reference before editing or auditing a Seeed Wiki repository.

## Resolve the active repository

- Use `git rev-parse --show-toplevel` rather than assuming the current directory is the root.
- Inspect `git status --short`, the current branch, and configured remotes.
- Treat an existing root-level `wiki.md` as newer authority than these bundled defaults.
- Preserve dirty files unless they are explicitly in scope. Shared worktrees may contain user changes.

## Source locations

Common locations in `wiki-documents` are:

- `sites/<locale>/docs/`: localized Markdown and MDX source.
- `sites/<locale>/*sidebar*.js`: locale navigation and learning-path labels.
- `src/components/`: shared React components used from MDX.
- `src/css/`: shared styling and design tokens.
- `src/theme/`: Docusaurus theme overrides.
- `plugins/`: client modules and Docusaurus plugins.
- `sites/<locale>/build/`: generated output; never edit or stage it.

Use `rg` and nearby files to confirm the actual convention before introducing a new path or abstraction.

## Scope decisions

- A page-only prose correction should normally remain in that page and its requested locale pair.
- A shared component or stylesheet can affect every locale even when only one page imports it. Inspect all imports before deciding the build matrix.
- Navigation label changes may require synchronized sidebar updates without translating full page bodies.
- Preserve stable front matter such as `slug`, `url`, `createdAt`, and document IDs unless the task explicitly changes routing.
- When replacing a Markdown title with a custom H1, keep exactly one accessible H1 and set the appropriate front matter to prevent a duplicate generated title.

## Review sources of truth

- For uncommitted work, review staged and unstaged diffs separately.
- For a branch handoff, compare against the intended base with a three-dot diff.
- For an existing GitHub PR, its hosted base/head comparison is authoritative for the PR's complete file and commit list.
- Generated build directories, downloaded source images, and local preview artifacts are not part of a PR unless the repository explicitly tracks them.

Run `scripts/audit-changes.sh [base-ref]` when a full branch or PR-scope inventory is useful.
