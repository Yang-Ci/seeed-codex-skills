# Seeed Wiki Authoring and MDX

Read this reference for prose, commands, front matter, headings, tabs, callouts, or component structure.

## Page structure

- Use real Markdown headings so the Docusaurus table of contents remains useful.
- Keep heading levels sequential and make headings describe a task or outcome.
- Maintain exactly one H1. If a custom JSX H1 replaces the generated title, set `hide_title: true` and preserve the front matter `title` for metadata.
- Split long installation or calibration procedures into numbered steps. Each step should state its purpose, action, and a useful verification signal.
- Use existing shared components and page classes before creating one-off markup.
- For a page-wide visual refresh, follow the established design of nearby related Wiki pages throughout the article, including purchase buttons, procedure steps, cards, and alignment. Preserve introductory platform sections explicitly requested by the user.
- Give interactive cards and collapsible section headers a restrained hover response consistent with the page's existing interaction style. Keep keyboard focus visible, make hover and focus work in light and dark themes, respect reduced-motion preferences, and preserve native disclosure and link behavior.
- In robotics Wiki pages using `rebot-wiki-style.css`, prefer the existing `rebot-buy-button-group` / `rebot-buy-button` pattern for purchase links when it matches nearby pages. Preserve each destination and localize the visible label; do not substitute it for platform, navigation, or other non-purchase links.
- Check whether product images and purchase links repeat unnecessarily within the page. Remove redundant presentation when it serves no distinct context, while retaining images and links needed for separate platform tabs, steps, troubleshooting cases, or products.
- In MDX, use React-compatible attributes such as `className` unless the surrounding component intentionally uses raw HTML conventions.

## Robotics quick-start references

Use these two page pairs as the primary UI and layout references for robotics quick starts. Paths are relative to the Wiki repository root. Open the sections relevant to the requested changes and compare the corresponding locale when editing both.

| Reference | English source | Chinese source |
| --- | --- | --- |
| SO-ARM100 / SO-ARM101 with LeRobot | `sites/en/docs/Robotics/Robot_Kits/Lerobot/Lerobot_SO100Arm_New.md` | `sites/zh-CN/docs/Robotics/Robot_Kits/Lerobot/cn_Lerobot_SO100Arm_New.md` |
| reBot Arm B601-RS Quick Start | `sites/en/docs/Robotics/Robot_Kits/reBot_Arm/B601_RS/reBot_Arm_B601_RS_Getting_Started.md` | `sites/zh-CN/docs/Robotics/Robot_Kits/reBot_Arm/B601_RS/cn_reBot_Arm_B601_RS_Getting_Started.md` |

- **Product introduction.** On a full refresh to match these pages, compare the title, visible product image, centered purchase action, and any platform or tool information relevant to the reader. Reuse the matching product image in the page body and replace legacy purchase markup with `rebot-buy-button-group` / `rebot-buy-button` in each affected locale. Keep existing purchase destinations, source any missing locale destination from the same product's reference page, and localize the labels. The SO-ARM `sensecraft-banner` is an example for a relevant software entry and guide. Preserve separate purchase and tool actions when both belong on the target page.
- **Learning path and platform installs.** Use SO-ARM's **Recommended Learning Path** for numbered navigation cards that link to later sections. Its `soarm-learning-path` layout is defined in `src/css/soarm101-pinocchio-style.css`. Use the **Install LeRobot** section as the example for peer Jetson and Ubuntu x86 tabs, each with its own vertical circular step flow.
- **Hardware, setup, and calibration.** Use B601-RS's **Assembly Guide** for assembled and unassembled variants inside one step, and **Connect the Arms** and **Software Setup and Calibration Workflow** for vertical numbered procedures. Use the latter section's OS tabs and `rebot-demo-details` disclosure for platform-specific setup and longer supporting instructions. Keep safety notices visible where readers need them.
- Reuse the applicable patterns from `src/css/rebot-wiki-style.css`. Use the SO-ARM-specific learning path style for section navigation where it fits. Apply the [layout rules below](#choose-a-layout-for-the-content) to the target's own sequence and options.

## Choose a layout for the content

Inspect the target page and the relevant section of a [quick-start reference](#robotics-quick-start-references) or a related tutorial. For a page-wide tutorial rewrite, classify groups across the whole page, including inside existing tabs and disclosures.

| What the reader needs to do | Layout |
| --- | --- |
| Complete several actions in order, such as connect → configure → verify | On a tutorial that uses the reBot design, reuse `rebot-step-flow`. On other pages, use the established step component or a numbered list. |
| Choose one applicable version, platform, or method for the same task, such as Ubuntu x86 / Jetson Orin or prebuilt package / source build | Put the alternatives in one `Tabs` group with a peer `TabItem` for each choice. |
| Choose a path, then complete several actions | Put the step flow inside each applicable tab. If only one step differs, keep the overall flow and put the tabs inside that step. |
| Look up labels such as `Pos`, `V`, and `Status`, compare specs, or scan a set of tools and their uses | Use a compact Markdown table with descriptive columns such as **Field / Meaning** or **Tool / Purpose**. |
| See prerequisites or shared information | Keep it visible in a list or section. |

- Use a real ordered list for short action sequences. Give a lookup table its own descriptive heading and keep exact UI labels in the first column. Put operational cautions next to the relevant action.
- Reuse `/src/css/rebot-wiki-style.css` and the existing `rebot-step-flow`, `rebot-step-item`, `rebot-step-number`, and `rebot-step-content` markup. Follow the nearest tutorial's numbering and label convention. Apply it to comparable procedures throughout the requested scope, including non-default tabs. Keep short substeps as lists inside a step.
- Reuse the page's existing Tabs component or import `Tabs` from `@theme/Tabs` and `TabItem` from `@theme/TabItem`. Give peer tabs unique, stable values and localize the labels. Each tab must contain the commands, warnings, media, and verification that apply to that choice. Keep truly shared prerequisites and steps visible outside the group.
- In paired edits, keep the tab order, values, and step structure aligned. Preserve existing explicit heading IDs and incoming links when moving content into tabs.
- For additional examples of a specific pattern, see the **Install Isaac Sim** section of `reBot_Arm_B601_RS_isaacsim.md` for alternative installation methods and **Initial System Environment** in `reBot_Arm_B601_DM_Lerobot.md` for sibling platform tabs.

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
- Use lists, tables, and procedure components according to the [layout rules above](#choose-a-layout-for-the-content).
- Give links descriptive labels rather than unexplained raw URLs.
- Use standard Chinese punctuation and sensible spacing around English product names and numbers.
- Do not remove prerequisites, limitations, safety notes, or recovery steps to simplify presentation.
- Apply the canonical spelling rules in [terminology-style.md](terminology-style.md) to front matter, headings, prose, navigation, captions, alt text, buttons, and ARIA labels.
- Prefer the current official product or vendor spelling over accidental variants already present in the repository. Verify uncertain or potentially changed names against a primary official source rather than guessing from title case.
- Preserve exact spellings inside commands, filenames, URLs, package names, API identifiers, environment variables, configuration keys, logs, and quotations when they are literal technical values.
