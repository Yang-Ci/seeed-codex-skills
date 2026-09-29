# Seeed Codex Skills

Reusable Codex skills for Seeed Studio Wiki work and polished web UI interactions.

## Included skills

### `wiki-doc-editor`

Creates, edits, localizes, validates, and prepares pull requests for Seeed Studio Wiki Markdown/MDX documentation. It includes guidance for repository scope, bilingual structure, media uploads, builds, and PR audits.

### `ui-interaction-engineer`

Designs, implements, reviews, and verifies web UI styling and interaction behavior, including carousels, drag gestures, scroll ownership, layout transitions, motion accessibility, responsive layouts, and media presentation.

## Install

Clone or download this repository, then copy each complete skill directory into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/wiki-doc-editor ~/.codex/skills/
cp -R skills/ui-interaction-engineer ~/.codex/skills/
chmod +x ~/.codex/skills/wiki-doc-editor/scripts/*.sh
```

Start a new Codex session if the skills are not discovered immediately.

## Use

Invoke a skill explicitly when desired:

```text
$wiki-doc-editor
$ui-interaction-engineer
```

Codex may also select either skill automatically when the request matches its description.

## Repository layout

```text
skills/
├── wiki-doc-editor/
│   ├── SKILL.md
│   ├── agents/
│   ├── references/
│   └── scripts/
└── ui-interaction-engineer/
    ├── SKILL.md
    ├── agents/
    └── references/
```

Review skill instructions and executable scripts before installing updates from any external repository.
