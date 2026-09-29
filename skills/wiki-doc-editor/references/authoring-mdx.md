# Seeed Wiki Authoring and MDX

Read this reference for prose, commands, front matter, headings, tabs, callouts, or component structure.

## Page structure

- Use real Markdown headings so the Docusaurus table of contents remains useful.
- Keep heading levels sequential and make headings describe a task or outcome.
- Maintain exactly one H1. If a custom JSX H1 replaces the generated title, set `hide_title: true` and preserve the front matter `title` for metadata.
- Split long installation or calibration procedures into numbered steps. Each step should state its purpose, action, and a useful verification signal.
- Use existing shared components and page classes before creating one-off markup.
- In MDX, use React-compatible attributes such as `className` unless the surrounding component intentionally uses raw HTML conventions.

## Tabs and steps

Use `Tabs` and `TabItem` for genuinely different hardware forms, operating systems, or installation paths. Tab values must be unique and stable; every tab must contain complete applicable instructions.

Typical step-flow structure:

```mdx
<div className="rebot-step-flow">
<section className="rebot-step-item">
  <span className="rebot-step-number">1</span>
  <div className="rebot-step-content">
    <h4>Step title</h4>
    <p className="rebot-step-label">Step 1</p>

    Step content

  </div>
</section>
</div>
```

Typical tab structure:

```mdx
<Tabs>
<TabItem value="unassembled" label="Unassembled Version">

Complete unassembled-version content

</TabItem>
<TabItem value="assembled" label="Assembled Version">

Complete assembled-version content

</TabItem>
</Tabs>
```

Unassembled instructions normally retain assembly media, precautions, and safety notes. Assembled instructions normally retain cabling, parameter writing, zero setup, and wiring references.

## Commands and technical facts

- Put executable commands in correctly labeled fenced blocks such as `bash`, `zsh`, `powershell`, or `text`.
- Commands must be complete and copyable. Use explicit placeholders such as `<device-ip>` and explain them.
- Preserve case, quotes, paths, environment variables, backslashes, flags, and argument order.
- Label the applicable OS, architecture, shell, hardware revision, and version when they matter.
- Present the recommended path first, followed by troubleshooting or recovery behavior.
- Verify internal consistency of dependency names, links, ports, baud rates, paths, and device names.
- Use `:::warning`, `:::tip`, and related callouts for hazards, first-run initialization, recovery, or significant limitations.

## Writing conventions

- Write concise, direct instructions with focused paragraphs.
- Use ordered lists for sequences and tables for comparisons, not for long procedures.
- Give links descriptive labels rather than unexplained raw URLs.
- Use standard Chinese punctuation and sensible spacing around English product names and numbers.
- Do not remove prerequisites, limitations, safety notes, or recovery steps to simplify presentation.
- Apply the canonical spelling rules in [terminology-style.md](terminology-style.md) to front matter, headings, prose, navigation, captions, alt text, buttons, and ARIA labels.
- Prefer the current official product or vendor spelling over accidental variants already present in the repository. Verify uncertain or potentially changed names against a primary official source rather than guessing from title case.
- Preserve exact spellings inside commands, filenames, URLs, package names, API identifiers, environment variables, configuration keys, logs, and quotations when they are literal technical values.
