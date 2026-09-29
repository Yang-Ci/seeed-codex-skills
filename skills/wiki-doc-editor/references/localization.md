# Seeed Wiki Localization

Read this reference when editing paired pages, translating content, or changing labels shared by multiple locales.

## Choose the synchronization level

Use the narrowest level that matches the request:

1. **Complete paired-page synchronization:** Keep Chinese and English headings, step order, tabs, images, tables, callouts, and video positions structurally aligned.
2. **Shared-label synchronization:** Update a product name, navigation label, platform spelling, or accessibility label across every locale where that exact shared concept appears, without rewriting unrelated prose.
3. **Single-locale correction:** Keep the change local when it is language-specific and does not alter shared structure or navigation.

Do not translate full pages in secondary locales merely because a shared label changed. Modify additional locales only when the request or shared navigation contract requires it.

## Preserve technical meaning

- Translate prose naturally rather than word-for-word.
- Preserve commands, filenames, code identifiers, URLs, parameters, units, and product names unless the task explicitly standardizes them.
- Do not add a translated tab label without translating its complete tab contents.
- Keep the same warning severity, prerequisites, limitations, and recovery instructions across paired pages.
- Localize image alt text, iframe titles, button labels, and ARIA labels when users encounter them.

## Structural comparison

Before finishing a paired-page change, compare:

- Front matter fields that should correspond.
- Heading sequence and level.
- Tabs and tab values.
- Ordered steps and callouts.
- Image and video positions.
- Internal routes and locale prefixes.
- Imported shared components and their locale props.

Do not force textual parity when one locale has an intentionally different regional resource, such as Bilibili for Chinese and YouTube for English.
