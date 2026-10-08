# New Product Wiki Homepage Links

Use this workflow when creating or discovering a new product Wiki, including during change reviews and PR audits.

## Detect and map

- Inspect added Markdown/MDX pages, including untracked files for local work and added files in the intended base/head comparison for branch or PR work. Read front matter and content to identify robotics relevance. Include robotics compute, robot kits, sensors, and related products represented on the homepage, even when their Wiki pages live elsewhere. An added translation or renamed file does not by itself mean a new product.
- Locate the actual robotics homepage and product-link owner. Common sources are `sites/en/docs/Edge_Robotics.md` and localized counterparts such as `sites/cn/docs/cn_Edge_Robotics.md`; verify paths with `rg --files`. If a shared component or data file owns the links, edit that source.
- Compare existing product cards and resolved Wiki routes. Add missing links within an existing product card; create a card only for a new product, following adjacent conventions. Avoid duplicate links or cards and do not treat every tutorial as a new product.

## Notify and automatically assist

Tell the user, in their language, which new product Wiki was found and that it needs synchronization to the robotics homepage product links. For example: “发现新增的 X 产品 Wiki，需要同步到机器人首页的产品链接中；我会补齐对应入口并检查链接。”

Automatically make the minimal local source edits when relevance, placement, and target are clear, without asking the user to repeat the synchronization request. Preserve existing layout and unrelated changes. For a read-only audit or explicit no-edit request, identify the missing entry and provide a concrete patch suggestion instead.

Resolve the URL from front matter (`slug` or configured document route) and locale routing configuration, rather than guessing from the filename. Use the official product name and actual page purpose as the label. Never invent product specifications, images, purchase URLs, or Wiki routes to fill a card.

Synchronize corresponding Chinese and English homepage links when applicable and valid destination pages exist, following [localization.md](localization.md). Do not invent localized routes or translate every locale automatically. Report missing localized Wikis; use cross-language links only when an existing repository convention supports them.

If product relevance, destination, or placement is ambiguous, complete clear entries first and ask only for the missing decision. If the Wiki repository is unavailable, report the needed source location and proposed product/link mapping. Local synchronization does not authorize uploads, commits, pushes, or PR mutations; retain the existing Git handoff rules.

## Verify and report

- Confirm every added link targets an existing page and matches its configured route and locale.
- Review the diff for duplicate cards or links and unintended changes. Run `git diff --check` and affected-locale validation as required by [validation-pr.md](validation-pr.md).
- Report the product Wiki, affected homepage source, link target, and status: completed, already present, intentionally unnecessary with reason, or unresolved with a specific missing fact. Include unresolved homepage synchronization in PR review findings and summaries.
