# Media and Layout

Use this reference when imagery, crop, aspect ratio, rounded corners, empty side space, or ghosting affects the interface.

## Choose the frame before the image rule

1. Identify the intended card or hero aspect ratio.
2. Determine whether the complete subject or a filled frame has priority.
3. Inspect the image's intrinsic dimensions and subject position when visual inspection is allowed.
4. Choose `cover`, `contain`, a focal `object-position`, or a dedicated art-directed asset.
5. Test the same rule at wide, standard, and narrow widths.

For common 16:9 product cards, source assets around 1600×900 or 1920×1080 usually provide enough detail without excessive weight. This is guidance, not a requirement; match the actual rendered size and device density.

## Cover versus contain

- Use `cover` when edge-to-edge fill is more important than preserving every pixel.
- Use `contain` when cutting off the product or embedded title is unacceptable.
- When `contain` exposes side space, use a deliberate solid color or gradient derived from the image rather than stretching the bitmap.
- Do not use `background-size: 100% 100%` for photographic content unless distortion is explicitly desired.
- Prefer `object-position` or background positioning before editing the source file.

## Rounded media

- Apply the radius and `overflow: hidden` to the same stable frame that clips the image and animated overlays.
- Keep nested radii mathematically related so borders do not show uneven corners.
- Verify focus rings are not clipped by the media mask.
- When a card scales, keep border, shadow, and clipping on a single composited wrapper where practical.

## Avoid ghost images

Common causes include:

- The same URL in both a background and a pseudo-element.
- An old image layer left behind during a crossfade.
- A transparent PNG placed over a blurred copy without an intentional separation.
- Duplicate keyed components rendered in two layout modes.
- A shine layer accidentally inheriting the product background.

Confirm the DOM and computed backgrounds contain only the intended image instances. Use a separate gradient layer for fill rather than a second copy of the photo.

## Respect asset boundaries

- Do not edit or regenerate source imagery when CSS layout can satisfy the request.
- Use image generation or editing only when the user asks for an asset change or layout cannot preserve the subject.
- If the user reserves image review for themselves, report the selected sizing rule and mechanical checks without claiming the crop looks correct.
