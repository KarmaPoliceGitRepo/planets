# Note-taking conventions (used by reading agents)

One note file per document: `notes/<subfolder-slug>/<doc-slug>.md`.
`<doc-slug>` = lowercase, hyphenated, shortened from the file title (drop extensions, noise like "libgen", "(1)").

## Per-document note template

```markdown
# <Human-readable title>

- **Source:** <original Drive file title>
- **Drive link:** <viewUrl>
- **Type:** book | paper | thesis | datasheet | notes | slides | spreadsheet
- **Author/Year:** <if identifiable>
- **Coverage:** full | partial (large file, truncated extraction) | unreadable (image-only/unsupported)

## Overview
1 short paragraph: what this document is and what it is about.

## Unique contribution
What THIS document adds that others may not (specific method, experiment, result, data, design).

## Key concepts
Bullet list of concept terms touched by this doc (just terms — definitions live in concept pages later).

## Methods / results / takeaways
The substantive learnings: methods used, key equations (only if central to this doc), results, numbers,
practical gotchas. Original summary wording — never reproduce long passages from the source.
```

## Sidecar files per folder

`notes/<subfolder-slug>/_concepts.tsv` — one row per (concept, doc):
```
concept_term	aliases_seen	one_line_definition	doc_slug
```

`notes/<subfolder-slug>/_manifest.tsv` — one row per Drive file found in the folder (recursively):
```
drive_file_id	title	mime_type	size_bytes	status	doc_slug_or_dash
```
status ∈ read | partial | unreadable | skipped-duplicate

## Conflict rule (added 2026-06-09)
When sources disagree, prioritize the better-quality source:
peer-reviewed journal / published standard > textbook > PhD thesis > conference paper > slides/datasheet > personal notes.
Prefer newer reviews over older primaries for settled topics. Record the disagreement explicitly:
"X (per <better source>); <other source> claims Y" — never silently average.
