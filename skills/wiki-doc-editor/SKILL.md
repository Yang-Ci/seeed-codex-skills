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
- For official product names, capitalization, spacing, acronyms, navigation labels, alt text, or ARIA terminology, read [references/terminology-style.md](references/terminology-style.md).
- For paired pages, translated content, or shared labels across locales, read [references/localization.md](references/localization.md).
- For images, video, remote uploads, asset URLs, image sizing, rounded corners, crop, or zoom behavior, read [references/media-assets.md](references/media-assets.md).
- For builds, browser checks, commits, PRs, or full PR summaries, read [references/validation-pr.md](references/validation-pr.md).
- For substantial web styling, image presentation, motion, gestures, scrolling, or layout transitions, also use `ui-interaction-engineer` when it is available. Image framing and rounded-corner work should load its media-layout guidance; interactive media should also load its verification matrix. This skill remains authoritative for Wiki scope, localization, remote media, builds, and Git handoff.

## Preserve scope and source

- Inspect the target section, nearby conventions, shared components, and corresponding localized page before editing.
- Preserve unrelated or pre-existing changes. Do not revert or reformat them for convenience.
- Make the smallest coherent change that achieves the requested outcome.
- Edit source files, never generated `sites/<locale>/build/` output.
- Reuse established imports, components, CSS tokens, media patterns, and navigation structures.
- Do not modify additional locales merely because they exist. Synchronize them only when the requested content or a shared label genuinely applies.
- Before PR handoff, classify every changed localized page as shared-content, shared-label, or locale-only. If a Chinese source page changed without its English counterpart, explicitly report whether English synchronization is required, intentionally unnecessary, or cannot be resolved.
- Before changing image presentation, define its role, frame, fit mode, radius owner, default and expanded sizes, zoom behavior, responsive rule, and visual verification boundary. Do not begin with a universal radius or aspect ratio.

## Sync new product Wiki links to the robotics homepage

When creating a product Wiki or discovering newly added product pages during change reviews or PR audits, check whether they belong in the robotics homepage product links. Review staged, unstaged, and untracked pages for local work, or the intended base/head diff for a branch or PR. Product pages may live outside `docs/Robotics/`.

Follow [references/robotics-product-links.md](references/robotics-product-links.md). Tell the user that the new product Wiki needs homepage link synchronization, then automatically complete the applicable local source edits when the product and destination are clear. A reminder alone does not complete this workflow. Report completed synchronization or the concrete missing information.

## Validate proportionally

- Review the exact diff and run `git diff --check`.
- Build every affected locale when MDX syntax, imports, shared components, CSS, media embeds, navigation, or page structure changed.
- Prefer temporary build destinations outside the repository so validation does not leave generated files in the worktree.
- Inspect generated output for requested headings, links, tabs, images, and embeds. Use browser verification when interaction, responsive layout, or visual state materially matters.
- Run the terminology checker on affected human-readable source files, review every finding in context, and preserve protected literals such as URLs, commands, filenames, and code identifiers.
- Run the locale synchronization checker before commit or PR handoff. Treat its output as a required review decision, not an automatic instruction to translate every page.
- For image presentation changes, verify intrinsic and rendered dimensions, aspect ratio, clipping layer, breakpoint behavior, duplicate layers, and default versus expanded geometry.
- Distinguish local validation, remote CI, pre-existing warnings, and new failures. Never report a pending check as passed.

The helper scripts are optional deterministic aids:

- `scripts/audit-changes.sh [base-ref]` reports committed PR scope, worktree changes, whitespace errors, and generated build artifacts.
- `scripts/check-terminology.py [--warn-only] <path>...` reports non-canonical product names, capitalization, and spacing without modifying files.
- `scripts/check-locale-sync.py [base-ref]` reports changed Chinese source files whose likely English counterpart is absent from the proposed PR diff.
- `scripts/validate-affected-sites.sh [--dry-run] [base-ref]` detects affected locale sites and builds them into a temporary directory.

## Guard external changes

- Do not upload media, commit, push, edit a PR, or create a PR unless the user authorizes that action.
- Stage exact source paths instead of using `git add .`.
- Exclude generated builds, credentials, temporary files, and unrelated changes.
- If the same topic already has an open PR, update its branch instead of opening a duplicate.
- For an existing PR, audit the hosted base/head diff rather than inferring its full contents from the local working tree.
- After pushing, report the commit ID, PR URL, review state, and current CI state.
