# Seeed Wiki Terminology and Capitalization

Read this reference when writing or reviewing product names, platform names, company names, acronyms, navigation labels, captions, image alt text, or accessibility copy.

## Choose the authoritative spelling

Use this order of authority:

1. The current primary source published by the product or project owner: official documentation, product page, repository, or application UI.
2. An explicit terminology or style convention in the current Wiki repository.
3. A canonical spelling supplied by the user for the scoped change.

If a name is uncertain, niche, newly renamed, or likely to have changed, verify it against a current primary source before editing. Do not infer the spelling by blindly applying title case, camel case, or word spacing.

Repository frequency is evidence of existing usage, not proof that the spelling is correct. A repeated typo does not outrank an official source.

## Apply terminology across visible text

Check canonical spelling in:

- Front matter titles, descriptions, and keywords.
- Page headings, prose, tables, callouts, captions, and link labels.
- Sidebar and navigation labels, search copy, buttons, tabs, and badges.
- Image alt text, iframe titles, tooltip text, and ARIA labels.
- Shared UI strings and corresponding localized labels when they name the same product or platform.

Canonical brand and product casing normally stays unchanged across languages. Translate the surrounding sentence, not the official name.

## Protect literal technical values

Do not blindly rewrite:

- URLs, route slugs, anchors, and filenames.
- Shell commands, flags, environment variables, and paths.
- Package, module, class, function, API, configuration-key, and JSON-property names.
- Code examples, console output, logs, quoted source text, and version identifiers.

A prose name and its executable identifier can legitimately differ. For example, write `ROS 2` in prose while preserving the `ros2` command; write `GitHub` in prose while leaving a lowercase URL or package name unchanged.

## Canonical examples

These examples are a baseline, not an exhaustive or permanent glossary. A verified current official source wins if branding changes.

| Canonical form | Avoid in prose |
| --- | --- |
| `MuJoCo` | `Mujoco`, `mujoco`, `MuJoco` |
| `Isaac Sim` | `IsaacSim`, `Isaacsim`, `isaac sim` |
| `Isaac Lab` | `IsaacLab`, `Isaac lab` |
| `Isaac ROS` | `IsaacROS`, `Isaac Ros` |
| `NVIDIA` | `Nvidia`, `nVIDIA` |
| `ROS 2` | `ROS2`, `Ros 2` |
| `GitHub` | `Github`, `github` |
| `JavaScript` | `Javascript`, `javascript` |
| `TypeScript` | `Typescript`, `typescript` |
| `PyTorch` | `Pytorch`, `pytorch` |
| `TensorFlow` | `Tensorflow`, `tensorflow` |
| `OpenAI` | `OpenAi`, `Openai` |
| `LeRobot` | `Lerobot`, `lerobot` |
| `Hugging Face` | `HuggingFace`, `Hugging face` |
| `macOS` | `MacOS`, `Mac OS` |
| `Raspberry Pi` | `Raspberry PI`, `raspberry pi` |
| `JetPack SDK` | `Jetpack SDK`, `JetPack sdk` |
| `Atom-S` | `Atom S`, `AtomS` |
| `StackForce` | `Stackforce`, `stackforce` |
| `Seeed Studio` | `Seeed studio`, `seeed studio` |

## Review workflow

1. Identify every affected human-readable surface, including metadata, navigation, media descriptions, and accessibility text.
2. Search case-insensitively for the canonical term and likely joined, spaced, or differently cased variants.
3. Verify uncertain spellings against a primary official source and record the source when the correction may be disputed.
4. Correct visible prose and labels while preserving literal technical values.
5. Compare corresponding localized surfaces when the name is shared across languages.
6. Run `scripts/check-terminology.py <affected-paths...>`, inspect every finding in context, and review the exact diff.

The checker is deliberately conservative and does not modify files. Its findings are review prompts, not permission for a global replacement.
