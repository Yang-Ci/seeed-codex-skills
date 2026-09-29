---
name: ui-interaction-engineer
description: Design, implement, review, and tune web interface styling and interaction behavior. Use for carousels, cards, hover states, scroll ownership, drag gestures, layout transitions, glass treatments, responsive behavior, motion accessibility, and browser UI verification. Do not use for content-only edits, native mobile UI, or bitmap image generation.
---

# UI Interaction Engineer

Turn a visual or behavioral direction into a coherent, responsive, accessible web interaction that fits the existing product rather than imposing a generic style.

## Route the task

- Read [references/interaction-contract.md](references/interaction-contract.md) when behavior has multiple states, inputs, transitions, or scroll rules.
- Read [references/motion-system.md](references/motion-system.md) when adding animation, stagger, spring response, masks, glass effects, or layout morphing.
- Read [references/media-layout.md](references/media-layout.md) when image sizing, crop, aspect ratio, backgrounds, rounding, or ghosting matters.
- Read [references/verification-matrix.md](references/verification-matrix.md) before verifying or handing off an implemented interaction.

If the user asks only for ideas or a motion proposal, provide the interaction contract and stop before editing. If the task is inside a documentation repository, combine this skill with the repository's documentation skill; that skill controls content, localization, builds, and Git handoff.

## Understand before styling

- Inspect the current component, styles, design tokens, surrounding layout, and responsive conventions.
- When the user provides an inspiration URL, inspect the current site and extract reusable principles such as hierarchy, rhythm, type treatment, and motion. Do not copy proprietary fonts, assets, or distinctive artwork without permission.
- Translate subjective directions into observable parameters: state, duration, easing, displacement, damping, stagger, crop, layering, and stop conditions.
- Make reasonable defaults when details are not material. Ask only when a missing choice would substantially change the result.
- Preserve the user's explicit verification boundary. If they say not to inspect images, validate mechanically and leave visual judgment to them.

## Implement a stateful interaction

- Define one source of truth for the active, expanded, dragging, grid, transitioning, disabled, or loading state.
- Assign ownership for click, pointer, keyboard, wheel, and page scroll before attaching handlers.
- Specify what happens when an action interrupts another action: cancel, reverse, queue, collapse first, or ignore.
- Clean up timers, observers, animation frames, global listeners, pointer capture, and temporary inline variables.
- Suppress the click that follows a meaningful drag, but preserve normal clicks and links.
- Prevent page scrolling only while the component intentionally consumes the wheel gesture. Restore normal scrolling in expanded, reading, or overview states unless the product requires otherwise.
- Keep inactive content out of the keyboard path with suitable focus management, `inert`, or equivalent semantics.

## Preserve visual coherence

- Reuse existing spacing, color, radius, typography, shadow, and motion tokens before inventing new ones.
- Treat glass, gradients, glow, and scan effects as hierarchy tools, not default decoration.
- Give every pseudo-element and image layer a single purpose. Avoid duplicate bitmap layers or effects that remain active on off-center cards.
- Prefer `transform` and `opacity` for motion. Measure and animate layout changes deliberately when geometry must move.
- Keep motion interruptible and short enough to preserve control. Reduced-motion behavior must remain complete and understandable.
- Make desktop, narrow viewport, touch, light theme, and dark theme intentional rather than accidental fallbacks.

## Validate the behavior

- Verify the requested path end to end, not only the default screenshot.
- Check keyboard, pointer, drag, wheel, page scroll, rapid repeated input, resize, theme, and reduced-motion states as relevant.
- Check the console, focus order, overflow, clipping, image layering, and cleanup after state changes.
- When a dev server is available, use browser automation for observable interaction checks. Do not claim visual approval for aspects the user reserved for their own review.
- Report what changed, the interaction states verified, and any remaining visual judgment or known limitation.

Do not commit, push, deploy, upload assets, or mutate external systems unless the user separately authorizes those actions.
