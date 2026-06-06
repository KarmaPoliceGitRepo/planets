---
name: image-to-pptx
description: Read one or more images (slide mockups, screenshots, design comps, whiteboard photos) and produce a PowerPoint (.pptx) file that matches them — recreating the layout, text, colors, and structure as editable native slides. Use when the user wants to turn an image/picture/screenshot/mockup of a slide or deck into an actual editable PowerPoint, "make a pptx that looks like this", "recreate this slide", or "convert these images into a presentation".
---

# Image → PowerPoint

Turn reference image(s) into an editable `.pptx` whose slides visually match them. The goal is **native, editable objects** (text boxes, shapes, tables) that recreate the source — not images pasted onto slides.

## 1. Look at the image(s) first

Use the Read tool to view every provided image. For each one, take note of:

- **Slide intent**: title slide, agenda, content/bullets, two-column, chart, quote, section divider, closing.
- **Layout & geometry**: where each element sits (top/center/left), relative sizes, alignment, columns.
- **Text**: exact wording, hierarchy (title vs subtitle vs body vs caption), bullet nesting, emphasis.
- **Style**: background color, accent/brand colors (estimate hex), font family/size feel (sans vs serif), bold/weight.
- **Non-text elements**: logos, icons, rectangles/dividers, tables, charts, image placeholders.

If anything is illegible or ambiguous (a cropped word, an unreadable hex), note it and either make a reasonable choice or ask the user — don't silently invent core content.

## 2. Set up tooling

The deck is built with [`python-pptx`](https://python-pptx.readthedocs.io/). It is often **not installed** — install into the active environment before building:

```bash
python3 -c "import pptx" 2>/dev/null || pip install python-pptx
```

## 3. Build the deck

Write a Python script that constructs the presentation. Guidelines that make output match the source:

- **Slide size**: default to 16:9 (`prs.slide_width = Inches(13.333)`, `prs.slide_height = Inches(7.5)`). Use 4:3 only if the image is clearly that ratio.
- **Start from a blank layout** (`prs.slide_layouts[6]`) and place your own text boxes/shapes so positions match the image, rather than fighting the built-in placeholders.
- **Positioning**: convert the image's relative layout into `Inches(...)` for `left/top/width/height`. Eyeball proportions from the image (e.g. title in top ~20%, body below).
- **Colors**: set fills and font colors with `RGBColor(0xRR, 0xGG, 0xBB)` using the hex values you estimated. Match the background fill of the slide.
- **Fonts**: set `font.name`, `font.size` (`Pt(...)`), `font.bold`, and `font.color`. Mirror the hierarchy you observed (large title, smaller body).
- **Bullets / nesting**: use paragraphs with `paragraph.level` for indentation.
- **Tables/charts**: recreate tables with `add_table`; for charts, recreate as a native chart if data is readable, otherwise approximate with shapes and label it.
- **One slide per source image**, in order.

Keep a tight reusable helper for "add a text box with these style attrs" to stay consistent across slides.

## 4. Save and deliver

- Save to a clearly named file, e.g. `output.pptx` (or a name the user requested) in the working directory.
- After saving, use the `SendUserFile` tool to surface the `.pptx` to the user so they can download it.
- Briefly summarize what you recreated and call out any assumptions (estimated colors/fonts, illegible text you guessed at) so the user can correct them.

## Notes & limits

- python-pptx renders true PowerPoint XML — colors/fonts/positions are exact to what you set, but it cannot *see* the image for you. Accuracy depends on how carefully you read the source in step 1.
- Exotic fonts not installed on the user's machine will fall back to a default in PowerPoint; pick widely available fonts (Calibri, Arial, Georgia) unless the user has the brand font.
- If asked to also produce a rendered preview (PNG) of the slides, that requires LibreOffice (`soffice --headless --convert-to png`) and may not be installed — offer it rather than assuming.
