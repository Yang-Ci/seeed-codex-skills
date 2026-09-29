# Seeed Wiki Validation and PR Handoff

Read this reference for builds, browser checks, commits, PR updates, or PR audits.

## Validation depth

- Always review the exact diff and run `git diff --check`.
- For prose-only edits, confirm headings, links, commands, and paired-locale consistency.
- Build every affected locale when MDX syntax, imports, components, CSS, navigation, media embeds, or page structure changed.
- Shared files under `src/` or `plugins/` can affect all locale sites; do not infer a single-site build solely from the edited page.
- Send build output to a temporary directory outside the repository when the build command supports it.
- Separate pre-existing warnings from failures introduced by the change.
- Run `scripts/check-terminology.py <affected-paths...>` for human-readable Wiki source. Review warnings in context instead of applying blind replacements.
- When a canonical product or platform name is shared across locales, search likely variants in the corresponding pages and shared navigation or accessibility labels. Separate pre-existing terminology debt from inconsistencies introduced by the current change.
- Never auto-fix URLs, anchors, filenames, commands, package names, API identifiers, environment variables, configuration keys, logs, or quotations based only on a prose capitalization rule.

Use `scripts/validate-affected-sites.sh --dry-run [base-ref]` to inspect the proposed build matrix, then run it without `--dry-run` when appropriate.

## Locale synchronization review

Before committing, pushing, or preparing a PR summary:

1. Run `scripts/check-locale-sync.py [base-ref]` against the intended PR base.
2. Inspect the substantive diff for every changed Chinese page whose English counterpart is not changed.
3. Classify it as `sync required`, `Chinese-only justified`, or `counterpart unresolved` using the criteria in [localization.md](localization.md).
4. Add the missing English change when synchronization is required and within scope. Otherwise, state the reason or unresolved mapping in the handoff instead of silently proceeding.

The path checker is intentionally advisory. Do not block a valid language-only correction, and do not claim two pages are synchronized merely because both filenames appear in the diff; compare their affected facts, structure, media, links, and user-facing behavior.

## Browser verification

Use a browser preview when the request changes interaction, layout, responsiveness, theme behavior, or client-side state. Check the relevant subset of:

- Page load and console errors.
- Requested text, links, images, and embeds.
- Desktop and narrow viewport overflow.
- Intrinsic versus rendered media dimensions, aspect ratio, crop, and focal position.
- Rounded-corner continuity across images, backgrounds, overlays, hover, expansion, and zoom.
- Distinct default and expanded media geometry; inactive content must not start at expanded size.
- Intentional treatment of `contain` side space and confirmation that photographic media is not stretched.
- A single intended bitmap layer with no stale background or pseudo-element copy.
- Light and dark themes.
- Keyboard focus and activation.
- Pointer, drag, wheel, and scroll ownership.
- Expanded, collapsed, loading, and empty states.
- `prefers-reduced-motion` behavior.

For image or card presentation changes, test at least one wide, one common laptop, and one narrow viewport. Record mechanical measurements when visual inspection is unavailable, and do not claim that crop or composition looks correct unless it was actually inspected.

For complex UI behavior, use `ui-interaction-engineer` and its verification matrix in addition to this Wiki validation.

## Safe Git handoff

- Commit, push, upload, or edit a PR only after explicit user authorization.
- Stage exact source paths and inspect `git diff --cached --stat` plus `git diff --cached --check`.
- Review the locale synchronization report and resolve or disclose every Chinese-only page reminder before the external PR action.
- Never stage `sites/*/build/`, downloaded originals, screenshots, credentials, or unrelated worktree changes.
- Use the repository's commit style and a message describing the user-visible outcome.
- Prefer the existing topic branch and open PR over creating a duplicate.

## PR auditing

For an existing PR, inspect the hosted record or an up-to-date base/head comparison:

- Base and head branches.
- Commit list and head SHA.
- Changed file count and additions/deletions.
- Full file list grouped by purpose.
- Chinese-only source changes and, for each, whether English synchronization was completed, intentionally unnecessary, or unresolved.
- Review decision and mergeability.
- Every current check, distinguishing `queued`, `in_progress`, `success`, `failure`, and `skipped`.

Do not describe only the latest local commit as the entire PR. If checks remain pending, report them as pending and stop waiting after a reasonable observation period unless the user asked for continued monitoring.

After pushing, report the commit ID, PR URL, branch, local validation, remote CI state, and any uncommitted artifacts that were intentionally excluded.
