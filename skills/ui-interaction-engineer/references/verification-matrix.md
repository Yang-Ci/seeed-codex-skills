# UI Verification Matrix

Use this reference before handing off a changed interaction. Select the relevant checks rather than performing unrelated testing.

## State coverage

- Initial/default state.
- Hover and focus-visible state.
- Active/pressed state.
- Transition in progress.
- Expanded and collapsed state.
- Default versus selected media geometry.
- Overview, grid, or alternate layout.
- Disabled, empty, loading, or error state when applicable.
- State after rapid repeated input and after returning to the initial state.

## Input coverage

- Pointer click on the primary item and adjacent items.
- Drag below and above the activation threshold.
- Touch or pointer cancellation.
- Wheel in both directions and trackpad-like small deltas.
- Page scrolling while the component is inactive, active, expanded, and in overview mode.
- Keyboard traversal, activation, directional keys, Space, Enter, and Escape as applicable.
- Links and buttons nested inside interactive layouts.

## Viewport and environment

- Wide desktop, common laptop width, and narrow mobile width.
- Resize while a non-default state is active.
- Light and dark themes.
- `prefers-reduced-motion: reduce`.
- Slow or missing image behavior when relevant.
- Browser console errors and React warnings.

## Visual and layout integrity

- No unintended horizontal overflow.
- No clipped focus rings or interactive content.
- No duplicate image layers, stale pseudo-elements, seams, or tearing.
- Stable rounded corners throughout transforms.
- Intrinsic aspect ratio remains correct; photographic media is not stretched.
- `cover` crops only approved areas, while `contain` side space has an intentional fill.
- Default cards do not begin at their expanded dimensions.
- Zoomed media fits below persistent navigation and closes without activating its parent card.
- Text remains readable over imagery and glass surfaces.
- Side content remains attached to its intended item and does not overlap unrelated sections.
- Final geometry is stable after animations and observers settle.

## Performance and cleanup

- Frequent motion primarily uses transforms and opacity.
- Large blur and filter regions remain bounded.
- Global listeners, observers, timers, frames, pointer capture, and inline motion variables are cleaned up.
- Rapid input does not queue stale openings or move to an outdated item.
- Reduced motion does not wait through decorative delays.

## Handoff report

Report:

1. The visible behavior implemented.
2. States and inputs actually verified.
3. Viewports and motion/theme variants checked.
4. Any portion intentionally left for the user's visual review.
5. Known limitations or follow-up work.

Do not claim visual verification when only source or DOM checks were performed.
