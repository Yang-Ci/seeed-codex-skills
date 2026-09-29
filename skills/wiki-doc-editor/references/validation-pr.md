# Seeed Wiki Validation and PR Handoff

Read this reference for builds, browser checks, commits, PR updates, or PR audits.

## Validation depth

- Always review the exact diff and run `git diff --check`.
- For prose-only edits, confirm headings, links, commands, and paired-locale consistency.
- Build every affected locale when MDX syntax, imports, components, CSS, navigation, media embeds, or page structure changed.
- Shared files under `src/` or `plugins/` can affect all locale sites; do not infer a single-site build solely from the edited page.
- Send build output to a temporary directory outside the repository when the build command supports it.
- Separate pre-existing warnings from failures introduced by the change.

Use `scripts/validate-affected-sites.sh --dry-run [base-ref]` to inspect the proposed build matrix, then run it without `--dry-run` when appropriate.

## Browser verification

Use a browser preview when the request changes interaction, layout, responsiveness, theme behavior, or client-side state. Check the relevant subset of:

- Page load and console errors.
- Requested text, links, images, and embeds.
- Desktop and narrow viewport overflow.
- Light and dark themes.
- Keyboard focus and activation.
- Pointer, drag, wheel, and scroll ownership.
- Expanded, collapsed, loading, and empty states.
- `prefers-reduced-motion` behavior.

For complex UI behavior, use `ui-interaction-engineer` and its verification matrix in addition to this Wiki validation.

## Safe Git handoff

- Commit, push, upload, or edit a PR only after explicit user authorization.
- Stage exact source paths and inspect `git diff --cached --stat` plus `git diff --cached --check`.
- Never stage `sites/*/build/`, downloaded originals, screenshots, credentials, or unrelated worktree changes.
- Use the repository's commit style and a message describing the user-visible outcome.
- Prefer the existing topic branch and open PR over creating a duplicate.

## PR auditing

For an existing PR, inspect the hosted record or an up-to-date base/head comparison:

- Base and head branches.
- Commit list and head SHA.
- Changed file count and additions/deletions.
- Full file list grouped by purpose.
- Review decision and mergeability.
- Every current check, distinguishing `queued`, `in_progress`, `success`, `failure`, and `skipped`.

Do not describe only the latest local commit as the entire PR. If checks remain pending, report them as pending and stop waiting after a reasonable observation period unless the user asked for continued monitoring.

After pushing, report the commit ID, PR URL, branch, local validation, remote CI state, and any uncommitted artifacts that were intentionally excluded.
