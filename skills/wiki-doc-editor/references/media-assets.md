# Seeed Wiki Media and Assets

Read this reference for images, video, diagrams, remote uploads, or asset URL changes.

## Images

- Reuse stable Seeed-hosted assets when suitable.
- Follow nearby conventions for dimensions, captions, alignment, galleries, and localized `alt` text.
- Decide deliberately between `cover` and `contain`: `cover` fills a frame but may crop; `contain` preserves the whole subject but may expose background space.
- Prefer CSS sizing and a suitable background before editing a source image solely to fit one layout.
- Avoid rendering the same bitmap in multiple overlapping layers, which can create visible ghosting.
- Preserve rounded corners on the actual clipping layer and verify overflow behavior.

If the user declines image inspection, respect that instruction. Validate URLs, dimensions, DOM structure, and CSS mechanically, and clearly report that visual inspection was left to the user.

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
