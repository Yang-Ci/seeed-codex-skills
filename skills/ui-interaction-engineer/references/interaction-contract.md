# Interaction Contract

Use this reference to make multi-state behavior explicit before implementation.

## Contract template

Write a compact contract containing only the fields relevant to the request:

| Field | Decision |
| --- | --- |
| States | Stable states the user can perceive |
| Entry | Initial state and restoration behavior |
| Inputs | Click, pointer, wheel, keyboard, scroll, resize |
| Transitions | Source state, destination state, timing, and ordering |
| Interruption | Cancel, reverse, queue, collapse first, or ignore |
| Scroll owner | Component or page for each state |
| Focus owner | Where keyboard focus moves or remains |
| Responsive rule | What changes structurally at narrow widths |
| Reduced motion | Equivalent state change without decorative movement |

Do not force every UI into a formal state machine, but use state-machine thinking when independent booleans could create impossible combinations.

## Input ownership

- A click activates the element under the pointer unless a preceding drag crossed the movement threshold.
- Pointer capture belongs to the active drag and must be released on pointer up, cancellation, or unmount.
- Wheel handling should accumulate deliberate movement, use a direction-aware threshold, and include a cooldown so one physical gesture does not skip several items.
- Call `preventDefault()` only when the component actually consumes the gesture. Passive listeners cannot cancel page scrolling.
- Keyboard behavior should use familiar keys, visible focus, and native buttons or links where possible.
- Links inside draggable or clickable containers must remain independently operable.

## Transition ordering

For transitions that cannot safely overlap, define an explicit sequence such as:

1. Close the current detail state.
2. Wait for the structural close transition, or complete immediately under reduced motion.
3. Change the active item.
4. Open the destination only when the request implies opening it.

Store scheduled work so a new action can cancel stale timers. State refs may be needed when event listeners outlive a render, but visible UI state should remain declarative.

## Layout modes

When a component has both a focused view and an overview:

- Overview items must all be available to pointer and keyboard users.
- Selecting an overview item should preserve identity while it moves or switches to focus.
- A FLIP-style measurement is appropriate when the same visual object must travel between layouts.
- If motion is reduced, switch states directly without leaving stale transforms or hidden siblings.
- Disable carousel-only controls while overview mode owns selection.

## Accessibility invariants

- Use native interactive elements and meaningful accessible names.
- Keep `aria-expanded`, `aria-pressed`, current position, and live status synchronized with visible state.
- Hidden or offstage items must not remain tab stops.
- Escape should close transient detail or overlay states when that matches platform expectations.
- Never make animation the only way to understand that state changed.
