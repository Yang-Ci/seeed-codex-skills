# Motion and Visual System

Use this reference for animation, stagger, spring response, masks, glass, glow, or layout morphing.

## Translate language into parameters

Convert subjective requests into observable decisions rather than treating a phrase as a preset:

- **Energy:** calm, responsive, playful, dramatic.
- **Amplitude:** maximum translation, scale, blur, or rotation.
- **Duration:** time until the state is usable, not merely until decoration ends.
- **Damping:** number and size of overshoots.
- **Stagger:** interval, direction, and maximum total delay.
- **Continuity:** whether identity visibly persists between layouts.
- **Interruption:** whether motion reverses, snaps, or restarts.

A request for a light elastic feel usually means small displacement, at most one subtle overshoot, fast decay, and no continuing wobble. Confirm the result against the user's wording rather than preserving arbitrary numbers from another project.

## Timing guidance

Use these as starting ranges, not requirements:

- Micro feedback: roughly 120–220ms.
- Common state changes: roughly 220–480ms.
- Deliberate reveal or layout focus: roughly 450–800ms.
- Stagger: often 40–90ms, capped so the last item does not feel blocked.

The interface should become operable as soon as the meaningful state is ready. Decorative tails must not block input.

## Implementation choices

- Prefer `transform` and `opacity` for frequent animation.
- Use CSS transitions for simple reversible states and keyframes for authored sequences.
- Use measured FLIP motion when an element changes containers or grid position but must appear continuous.
- Animate height only when content geometry truly requires it; measuring with `ResizeObserver` can prevent clipping.
- Apply `will-change` narrowly and remove it when no longer needed.
- Avoid long-lived filters and large full-screen backdrop blurs on moving surfaces.
- Keep transform ownership clear. Use CSS variables or nested wrappers when drag, layout, and hover each need transforms.

## Masks and staggered reveals

- A title reveal should have an actual clipping or mask boundary, not only a fade.
- Stagger should communicate order or hierarchy. Do not delay content merely to showcase animation.
- When content opens on two sides, stagger from the center outward or according to reading order, and cap rotation so later items do not become visually unstable.
- Under reduced motion, preserve ordering and final visibility without translation, scale, parallax, or spring oscillation.

## Glass and layered effects

A convincing glass surface normally combines a restrained subset of:

- Translucent background tied to the current theme.
- A visible but quiet border.
- One inset highlight.
- One external shadow that establishes elevation.
- Backdrop blur only where content behind the surface makes it meaningful.

Do not stack several glows, borders, and highlights at equal strength. Maintain text contrast and avoid glass on large text-heavy reading surfaces when it reduces clarity.

## Prevent tearing and ghosting

- Render a product bitmap once unless duplicate layers are intentional and visibly different.
- Keep scan and shine pseudo-elements on the active visual layer only.
- Clip transforms and filters at a stable rounded container.
- Avoid switching `background-size`, filters, and transforms on several overlapping siblings in the same frame.
- Use stable keys and do not recreate animated nodes unnecessarily.
- Remove temporary inline transform variables after a completed or cancelled transition.
