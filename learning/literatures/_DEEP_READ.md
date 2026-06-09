# Deep-read workflow (PyMuPDF + vision)

Goal: upgrade notes whose Coverage is `partial` or `unreadable` to full understanding, so the
knowledge base can answer any ultrasound/acoustics question. Queue: `_deep_read_queue.tsv`
(work top-down; rows are priority-ordered with ultrasound/acoustics folders first).

## Per-document procedure

1. **Pick** the first `pending` row; set it to `working` (edit the TSV) so parallel agents don't collide.
2. **Download the real PDF** (not the lossy text extraction): load the Drive tool
   `mcp__8094c1a2-e886-4498-81aa-c6e73e702b63__download_file_content` via ToolSearch, call it with the
   fileId, decode base64 to `/tmp/deepread/<doc_slug>.pdf` (use python, never paste base64 into context).
3. **Extract text with PyMuPDF** (`import fitz`): full text page by page. For big books, extract the ToC
   (`doc.get_toc()`) and read chapter-by-chapter, summarizing as you go instead of loading everything at once.
4. **Use your eyes on figures**: detect pages with images/drawings (`page.get_images()`, or key figures
   referenced in the text), render them: `pix = page.get_pixmap(dpi=120); pix.save(png_path)` — then use the
   **Read tool on the PNG** to visually inspect the figure. Capture what the figure actually shows (curve
   shapes, axes, trends, schematics) in the note. For scanned/image-only PDFs (`unreadable` rows), render
   pages and read them visually — that is the only way in.
5. **Upgrade the note** at `notes/<folder>/<doc_slug>.md`: set Coverage to `full (deep read)` (or
   `visual read (scanned)`), enrich Methods/results/takeaways with the previously-missing chapters, and add a
   `## Figures` section describing the informative figures. Keep summaries original — no long verbatim passages.
6. **Update sidecars**: append new concept rows to the folder's `_concepts.tsv` and fix the status in the
   folder's `_manifest.tsv` (partial → read, unreadable → read-visual when successful).
7. **Mark the queue row** `done` (or `failed: <reason>` — e.g. encrypted, file too corrupt) and delete the temp PDF.
8. **Commit**: `git add learning && git commit -m "learning: deep-read <doc_slug> (<folder>)" && git push`.

## Rules
- /tmp/deepread/ is scratch — never commit PDFs or PNGs to the repo (copyright + size).
- If a figure is unreadable at 120 dpi, retry at 200 dpi; give up after that and note it.
- Respect other agents: only touch the queue row you claimed and your own note/sidecar edits.
