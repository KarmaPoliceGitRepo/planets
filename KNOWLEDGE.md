# Project Knowledge (graphify store)

> Durable project memory maintained by the `graphify` skill. Agents read this for
> context and append durable facts here. Keep entries terse; date decisions.
> Never write secrets, tokens, or personal data here — this file is committed and shared.

## Overview
`planets` (GitHub: `KarmaPoliceGitRepo/planets`) hosts reusable **Claude Code skills**
under `.claude/skills/` and, since 2026-06-09, a large **literature knowledge base** under
`learning/literatures/` distilled from the user's Google Drive research library
("0000 -03- LITERATURES", ~645 files / 40 folders: ultrasonics, acoustics, tribology,
transducers, signal processing, engineering).

## Literature knowledge base (learning/literatures/)
- **Entry points:** `GLOSSARY.md` (203 canonical concepts), `INDEX.md` (~700 per-document notes), `MANIFEST.md` (645-file inventory with read status).
- **Structure:** `concepts/<slug>.md` — ONE canonical page per concept (aliases, definition, key relations, "Discussed in" backlinks); `notes/<folder>/<doc-slug>.md` — per-document notes (overview, unique contribution, methods/results); `_graphify/` — domain digests; `_deep_read_queue.tsv` — PyMuPDF+vision deep-read pipeline state.
- **Dedup rule:** a concept is defined once; notes link to `concepts/` instead of re-defining. Duplicates are semantic (same scientific meaning), not string matches.
- **Conflict rule (2026-06-09):** on disagreement prefer journal/standard > textbook > thesis > conference > slides/datasheet > personal notes; newer reviews for settled topics; record disagreements explicitly, never average silently.
- **Key cross-cutting findings:** acoustoelasticity (velocity–stress, Hughes–Kelly; diffuse scattering ~10–50× more stress-sensitive than velocity per Kube & Turner 2016); temperature dependence of sound speed (steel shear ≈ linear, e.g. V = −0.4521·T + 3259.9 m/s, Wei 2020) — temperature is the dominant confounder in ultrasonic stress/film measurement; grain-scattering attenuation regimes (Rayleigh ∝D³f⁴ → stochastic ∝Df² → geometric, unified by Stanke–Kino 1984); ultrasonic reflection-coefficient method (Dwyer-Joyce/Sheffield lab) for oil-film thickness & contact stiffness via spring model R = 1/(1+(2K/ωZ)²)^½ analogues.

## Architecture
- Skills live in `.claude/skills/<name>/SKILL.md`, each with YAML frontmatter (`name`, `description`) plus a Markdown body of instructions.
- Project-scoped skills (committed here) are auto-discovered by any Claude Code session working in this repo; user-scoped copies can also live in `~/.claude/skills/`.
- This `KNOWLEDGE.md` at the repo root is the project's persistent memory, written/read by the `graphify` skill.

## Decisions
- 2026-06-06 — Added first two skills (`image-to-pptx`, `task-history-review`) via PR #1, which was merged to `main`.
- 2026-06-06 — Skills are versioned in-repo (project scope) so all agents share them, rather than relying on ephemeral user-scope installs in the remote container.
- 2026-06-07 — Added `graphify` skill: durable project memory stored in root `KNOWLEDGE.md`, organized as light entity/relationship graph + notes.
- 2026-06-07 — Every session auto-loads this store: a `SessionStart` hook in `.claude/settings.json` cats `KNOWLEDGE.md` into context, and `CLAUDE.md` points agents here. No need to ask agents to read it.
- 2026-06-09 — Built the literature knowledge base on branch `claude/folder-branch-books-learning-10r2i4` (PR #3): ~40 parallel reader agents (1/folder), per-doc notes + `_concepts.tsv` sidecars, 4 domain merge agents clustering 1556 raw concept rows into 203 canonical pages, deep-read pipeline (PyMuPDF text + rendered-figure visual reading) for priority papers, adversarial verification pass cross-checking concept claims against source notes.
- 2026-06-09 — Source PDFs/PNGs are NEVER committed (copyright + size); only original summary notes. /tmp/deepread is scratch.

## Conventions
- One skill per directory under `.claude/skills/`; keep `description` trigger-rich so the skill is matched on the right requests.
- Keep shell snippets in skill docs copy-pasteable (use `python3 -m pip`, give concrete examples instead of `<placeholder>`s).
- Commit knowledge updates with messages prefixed `graphify:`.

## Entities & Relationships
- **planets repo** —contains→ **.claude/skills/** : project-scoped skills.
- **graphify skill** —writes/reads→ **KNOWLEDGE.md** : the persistent memory store.
- **image-to-pptx skill** —depends on→ **python-pptx** : builds editable .pptx from images.
- **task-history-review skill** —reads→ **git + GitHub artifacts** : reconstructs recent activity.
- **agents** —read→ **KNOWLEDGE.md** : for context before non-trivial tasks.
- **learning/literatures/** —distills→ **Drive "0000 -03- LITERATURES"** : 645-file research library.
- **notes/** —link to→ **concepts/** : definitions live once in concept pages; notes carry each doc's unique contribution.
- **GLOSSARY.md / INDEX.md / MANIFEST.md** —index→ **concepts/ and notes/** : generated entry points (regenerable by script).
- **_deep_read_queue.tsv** —drives→ **deep-read pipeline** : PyMuPDF + figure-vision upgrades of partial/unreadable notes.

## Glossary
- **Skill** — a `SKILL.md` under `.claude/skills/` that Claude Code can invoke (e.g. `/graphify`).
- **graphify store** — this `KNOWLEDGE.md` file; the project's durable memory.

## Gotchas
- The remote execution environment is an ephemeral container, NOT the user's machine: anything not committed/pushed is lost, and `~/.claude/skills/` here does not sync to the user's real setup.
- No CI workflows are configured in this repo, so PR checks are limited to the Copilot reviewer.
- Drive MCP `download_file_content` works only in the MAIN session (denied to subagents) and intermittently fails with "session expired" on large PDFs — retry later; small files usually succeed.
- Background Agent calls must set `model: "sonnet"` in this environment (default model 400s with `thinking.type.disabled`).
- Some Drive files remain `partial`/`unreadable` (huge scans, djvu, epub) — see MANIFEST.md statuses; deep-read queue holds remaining upgrade candidates.

## Open Questions
- What is the intended longer-term purpose of `planets` beyond hosting skills?
