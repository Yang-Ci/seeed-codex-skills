# Seeed Wiki Localization

Read this reference when editing paired pages, translating content, or changing labels shared by multiple locales.

## Choose the synchronization level

Use the narrowest level that matches the request:

1. **Complete paired-page synchronization:** Keep Chinese and English headings, step order, tabs, images, tables, callouts, and video positions structurally aligned.
2. **Shared-label synchronization:** Update a product name, navigation label, platform spelling, or accessibility label across every locale where that exact shared concept appears, without rewriting unrelated prose.
3. **Single-locale correction:** Keep the change local when it is language-specific and does not alter shared structure or navigation.

Do not translate full pages in secondary locales merely because a shared label changed. Modify additional locales only when the request or shared navigation contract requires it.

## Decide whether English must follow Chinese

When a Chinese source file changes without its English counterpart, inspect the actual diff and record one of these outcomes before PR handoff:

- **Synchronization required:** The change affects shared facts, product specifications, prerequisites, commands, code behavior, step order, headings, tables, warnings, media, links, product terminology, navigation, accessibility labels, or interaction behavior. Update the English counterpart in the same PR unless the user explicitly scopes it otherwise.
- **Chinese-only is intentional:** The change is a Chinese-language grammar or punctuation correction, a translation-quality improvement with no meaning change, or a China-specific resource such as Bilibili. Keep it local and state the reason in the handoff.
- **Counterpart unresolved:** No reliable English page can be mapped. Do not invent a translation target; report the Chinese path and ask for review when synchronization may be material.

Run `scripts/check-locale-sync.py [base-ref]` before commit or PR handoff. Its path matching is a reminder mechanism, not semantic proof: the agent must inspect each listed diff and make the decision above.

## Preserve technical meaning

- Translate prose naturally rather than word-for-word.
- Preserve commands, filenames, code identifiers, URLs, parameters, units, and product names unless the task explicitly standardizes them.
- Do not add a translated tab label without translating its complete tab contents.
- Keep the same warning severity, prerequisites, limitations, and recovery instructions across paired pages.
- Localize image alt text, iframe titles, button labels, and ARIA labels when users encounter them.
- Keep canonical product, platform, project, and company capitalization identical across languages. For example, use `MuJoCo` and `Isaac Sim` in both English and Chinese prose.
- When a shared canonical name changes, scan corresponding navigation, headings, captions, alt text, and accessibility labels in affected locales without rewriting unrelated translated content.
- Do not normalize protected literals such as commands, paths, URLs, package names, or code identifiers merely to make them resemble prose terminology.

## Structural comparison

Before finishing a paired-page change, compare:

- Front matter fields that should correspond.
- Heading sequence and level.
- Tabs and tab values.
- Ordered steps and callouts.
- Image and video positions.
- Internal routes and locale prefixes.
- Imported shared components and their locale props.

For PR handoff, list any changed Chinese page that was intentionally not synchronized and the reason. Do not silently omit a likely English counterpart.

Do not force textual parity when one locale has an intentionally different regional resource, such as Bilibili for Chinese and YouTube for English.
