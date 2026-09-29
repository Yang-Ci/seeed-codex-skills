# Seeed Wiki Media and Assets

Read this reference for images, video, diagrams, remote uploads, or asset URL changes.

## Define the image presentation contract

Before changing markup or CSS, record the decisions that affect the reader's experience:

1. **Role:** inline documentation image, engineering diagram, screenshot, product card, hero, thumbnail, or zoomable evidence.
2. **Source:** intrinsic width, height, aspect ratio, transparency, focal point, file size, and stable remote URL.
3. **Frame:** intended rendered width, maximum width, aspect ratio, alignment, and surrounding background.
4. **Fit:** `cover`, `contain`, natural aspect ratio, or a dedicated art-directed asset.
5. **Corners:** which element owns the radius and clipping, and whether engineering content needs square or only subtle corners.
6. **States:** default, hover, selected, expanded, grid, lightbox, loading, and failure behavior when applicable.
7. **Responsive rule:** what changes at wide, laptop, tablet, and mobile widths.
8. **Verification:** whether Codex may visually inspect the image or must leave visual judgment to the user.

Do not apply a fixed radius, width, or 16:9 frame to every Wiki image. The contract should follow the media's job.

## Choose treatment by media role

| Media role | Priority | Typical fit and sizing | Corner guidance |
| --- | --- | --- | --- |
| Wiring or engineering diagram | Preserve every label and edge | Natural ratio or `contain`; allow zoom for small text | None or a restrained radius if it does not obscure boundaries |
| Software screenshot | Keep UI readable and uncropped | Natural ratio or `contain`; cap reading width and support zoom | Match the surrounding documentation surface |
| Product card | Strong, consistent frame | `cover` when crop is safe; otherwise `contain` over an intentional fill | Radius belongs to the card's clipping frame |
| Transparent product render | Preserve the complete subject | `contain` over a solid color or gradient; never stretch | Clip the background and subject as one visual surface |
| Hero image | Fill and hierarchy | `cover` with an explicit focal position or a dedicated crop | Match the hero container and overlays |

These are defaults to evaluate, not universal requirements.

## Size and aspect ratio

- Reuse stable Seeed-hosted assets when suitable and record their intrinsic dimensions before choosing CSS.
- Inline documentation images normally need `max-width: 100%` and automatic height so the source ratio is preserved.
- Reserve layout space with intrinsic `width` and `height` attributes or `aspect-ratio` when possible to reduce layout shift.
- Do not use `width: 100%; height: 100%` or `background-size: 100% 100%` on photographic content unless distortion is explicitly intended.
- Distinguish default and expanded geometry. A selectable card must not use its expanded dimensions before activation.
- Set a readable maximum width for screenshots and diagrams instead of allowing an extremely large source to fill the article automatically. Derive the cap from the surrounding layout rather than hard-coding one value for every page.
- For a common 16:9 product frame, sources around 1600×900 or 1920×1080 are usually sufficient. Other roles should keep their natural or designed ratio.
- Prefer source pixels near one to two times the largest rendered dimension, balancing high-density displays against download weight.
- Use focal positioning when `cover` is necessary; confirm important labels, products, hands, or faces are not cropped at any target width.

## Rounded corners and clipping

- Apply `border-radius` and `overflow: hidden` or `overflow: clip` to the stable frame that owns the image and its overlays.
- Do not round only the `<img>` while a background, shine, mask, or pseudo-element remains square.
- Keep nested radii related to the outer radius and border thickness so corners do not show gaps or colored slivers.
- Ensure focus rings remain visible outside the clipping frame.
- Recheck corners while the card is scaled, dragged, expanded, zoomed, or transitioning between layouts.
- Avoid rounding technical figures when the radius would remove meaningful pixels or imply a decorative treatment inconsistent with nearby documentation.

## Prevent empty space, tearing, and ghosting

- Decide between crop and empty space consciously. If `contain` exposes side space, provide an intentional solid or gradient fill rather than stretching the bitmap.
- Render the source bitmap once unless duplicate layers are intentional and visibly distinct.
- Do not let scan, glow, or shine pseudo-elements inherit the product image.
- Keep decorative overlays on the active or intended card only; inactive cards should not retain center-card effects.
- Use a stable keyed element and clipping surface during layout transitions so side cards, labels, and backgrounds do not split into different moving layers.
- Prefer CSS sizing and a suitable background before editing a source image solely to fit one layout.

## Click-to-zoom and interactive media

- Preserve the repository's existing global zoom behavior unless the user explicitly asks to change it. Do not modify a shared zoom plugin merely to solve one page's card size, crop, or rounded corners.
- Do not attach article image zoom automatically to images that already act as product selectors, buttons, links, drag surfaces, or carousel cards.
- For documentation images, keep zoom within a navbar-safe viewport and use a reasonable maximum scale instead of always filling the screen.
- Preserve the media's aspect ratio and rounded clipping while zoomed.
- Keyboard and touch users need an equivalent way to open and close zoomed media.
- Opening an image must not accidentally trigger the parent card, drag gesture, or navigation link.
- Prefer a page-scoped selector or wrapper exclusion when one image should opt out; change global zoom configuration only when the requested behavior is genuinely site-wide.

## Image validation

For presentation changes, verify the relevant subset:

- Final URL, HTTP success, file size, MIME type, intrinsic dimensions, and aspect ratio.
- Computed rendered width and height at wide, laptop, and mobile widths.
- `object-fit`, background sizing, and focal position.
- Radius and overflow on the actual clipping owner.
- Default and expanded sizes before, during, and after transition.
- One intended bitmap instance, with no inherited copy on pseudo-elements.
- No horizontal overflow, unexpected crop, blank bands, layout shift, or clipped focus ring.
- Zoom bounds, navbar clearance, close behavior, and nested click handling.

If the user declines image inspection, respect that instruction. Validate URLs, dimensions, DOM structure, computed styles, and state transitions mechanically, then clearly state that the final crop and visual balance remain for user review.

## Video

- Prefer Bilibili for Chinese pages and the corresponding YouTube video for English pages unless directed otherwise.
- Convert YouTube watch URLs to embed URLs and preserve useful playlist, index, start-time, or other supplied parameters.
- Reuse the target page's video wrapper and iframe attributes.
- If required media is missing, leave a clear insertion point and request the real URL; never invent or substitute one.

## Uploading new images

1. Inspect adjacent Wiki URLs to determine the correct remote product directory and filename style.
2. Ask the user to enable the remote FTP/file-server connection if it is not already confirmed.
3. Determine whether Chinese and English require separate assets. Ask only when the answer materially affects the upload.
4. Use a short descriptive filename without spaces, Chinese characters, meaningless counters, or temporary suffixes.
5. Upload through the configured remote connection. Do not place local filesystem paths in Wiki source.
6. Verify the final HTTPS URL, HTTP success, and expected file size before inserting it.
7. Keep credentials, tokens, host secrets, and private paths out of command output, commits, and PR descriptions.

If upload capability is unavailable after the connection is enabled, explain the missing capability and keep a clear local placeholder. Do not fabricate a remote URL.
