---
name: wiki-doc-editor
description: Create, edit, translate, review, validate, and prepare pull requests for Seeed Studio Wiki Markdown/MDX documentation. Use for localized Wiki pages, Docusaurus components, navigation, media uploads, shared documentation UI, builds, and Wiki PR audits. Do not use for unrelated generic Markdown or application UI work outside the Wiki.
---

# Seeed Wiki Editor

Produce accurate, localized, buildable Seeed Wiki changes while preserving the user's scope, existing work, and repository conventions.

## Establish authority

1. Find the repository root and inspect `git status` before acting.
2. If `<repo-root>/wiki.md` exists, read it completely and treat it as the current project guide.
3. Otherwise, use the bundled references below as the project defaults, loading only those relevant to the task.
4. The user's latest explicit instruction overrides a bundled convention.

## Route the task

Always read [references/repository-map.md](references/repository-map.md) before editing or auditing a Seeed Wiki repository.

- For prose, MDX structure, commands, tabs, headings, or front matter, read [references/authoring-mdx.md](references/authoring-mdx.md).
- For paired pages, translated content, or shared labels across locales, read [references/localization.md](references/localization.md).
- For images, video, remote uploads, or asset URLs, read [references/media-assets.md](references/media-assets.md).
- For builds, browser checks, commits, PRs, or full PR summaries, read [references/validation-pr.md](references/validation-pr.md).
- For substantial web styling, motion, gestures, scrolling, or layout transitions, also use `ui-interaction-engineer` when it is available. This skill remains authoritative for Wiki scope, localization, media, builds, and Git handoff.

## Preserve scope and source

- Inspect the target section, nearby conventions, shared components, and corresponding localized page before editing.
- Preserve unrelated or pre-existing changes. Do not revert or reformat them for convenience.
- Make the smallest coherent change that achieves the requested outcome.
- Edit source files, never generated `sites/<locale>/build/` output.
- Reuse established imports, components, CSS tokens, media patterns, and navigation structures.
- Do not modify additional locales merely because they exist. Synchronize them only when the requested content or a shared label genuinely applies.

## Validate proportionally

- Review the exact diff and run `git diff --check`.
- Build every affected locale when MDX syntax, imports, shared components, CSS, media embeds, navigation, or page structure changed.
- Prefer temporary build destinations outside the repository so validation does not leave generated files in the worktree.
- Inspect generated output for requested headings, links, tabs, images, and embeds. Use browser verification when interaction, responsive layout, or visual state materially matters.
- Distinguish local validation, remote CI, pre-existing warnings, and new failures. Never report a pending check as passed.

The helper scripts are optional deterministic aids:

- `scripts/audit-changes.sh [base-ref]` reports committed PR scope, worktree changes, whitespace errors, and generated build artifacts.
- `scripts/validate-affected-sites.sh [--dry-run] [base-ref]` detects affected locale sites and builds them into a temporary directory.

## Guard external changes

- Do not upload media, commit, push, edit a PR, or create a PR unless the user authorizes that action.
- Stage exact source paths instead of using `git add .`.
- Exclude generated builds, credentials, temporary files, and unrelated changes.
- If the same topic already has an open PR, update its branch instead of opening a duplicate.
- For an existing PR, audit the hosted base/head diff rather than inferring its full contents from the local working tree.
- After pushing, report the commit ID, PR URL, review state, and current CI state.
