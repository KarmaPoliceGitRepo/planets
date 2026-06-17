# Project Knowledge (graphify store)

> Durable project memory maintained by the `graphify` skill. Agents read this for
> context and append durable facts here. Keep entries terse; date decisions.
> Never write secrets, tokens, or personal data here — this file is committed and shared.

## Overview
`planets` (GitHub: `KarmaPoliceGitRepo/planets`) is a small repository currently used
primarily as a home for reusable **Claude Code skills** under `.claude/skills/`. Beyond
`README.md` and `SECURITY.md`, the substantive content is the skills themselves.

## Architecture
- Skills live in `.claude/skills/<name>/SKILL.md`, each with YAML frontmatter (`name`, `description`) plus a Markdown body of instructions.
- Project-scoped skills (committed here) are auto-discovered by any Claude Code session working in this repo; user-scoped copies can also live in `~/.claude/skills/`.
- This `KNOWLEDGE.md` at the repo root is the project's persistent memory, written/read by the `graphify` skill.

## Decisions
- 2026-06-17 — Extended `podcast-the-missing-link/` to full end-to-end tooling + a UI. Added: `scripts/clean_audio.sh` (FFmpeg DSP chain highpass→afftdn denoise→adeclick→deesser→acompressor→lowpass; strengths light/medium/strong; writes `working/episode_clean.wav`; does NOT set loudness so −16 LUFS stays solely in `process_episode.sh`); `scripts/segment_episode.py` (Whisper → context-based **segments** + **sub-sections** with keyword **tags**, grouped by silence gaps + lexical-cohesion Jaccard test; caches `working/whisper.json`; writes editable `working/segments.json`); `scripts/render_selection.py` (FFmpeg trim+concat rebuild of audio+video from kept items; backs up original premaster); `scripts/studio.py` + `studio/studio.html` (zero-dependency local web UI on 127.0.0.1:8765 via stdlib `http.server`; drives clean→segment→tick-keep→render→master→subtitles with a background-job log + path-traversal guard); `slides/make_slides.py` → `slides/how-to-use-the-missing-link.pptx` + `.pdf` (python-pptx deck; LibreOffice→PDF with reportlab fallback). `process_episode.sh` now also prefers `episode_clean.wav` (when no premaster) and `episode_cut.mp4` (selection render). New guide `02-implementation/06-studio-and-segments.md`; SE doc 06 §6.6 logs C4b/C5b/C10 + F4b/F4c. All additive/backward-compatible; verified end-to-end (clean→segment(reuse)→render 30s→18s→master PASS −16 LUFS; studio endpoints + traversal guard tested). GOTCHA: LibreOffice is broken in the remote container (can't load any source file) so the committed PDF is the reportlab fallback; on a normal machine the script makes a pixel-perfect PDF from the pptx. Slide deps (python-pptx, reportlab) are intentionally NOT in `scripts/requirements.txt` (kept lean for the Whisper path); `make_slides.py` imports them lazily with install hints.
- 2026-06-14 — Added `podcast-the-missing-link/`: a full end-to-end, free, beginner-friendly podcast production system for the show "The Missing Link" (Nepal migration/villages/energy/tourism). Built with a systems-engineering methodology (stakeholders → needs → requirements → ConOps → functional → physical architecture → V&V → traceability) plus implementation guides, episode content, and working automation scripts (FFmpeg mastering to -16 LUFS, Whisper transcription, episode scaffolding). Tooling chosen for $0 cost + 12-year-old usability (OBS, Audacity, FFmpeg, Whisper, Canva, Spotify for Creators, YouTube). The "Uber-for-guides" app is scoped as the show's subject/future system, not built here. Scripts verified end-to-end with FFmpeg (`process_episode.sh` prints PASS; outputs meet MP3 44.1k/128k and MP4 H.264/AAC specs).
- 2026-06-06 — Added first two skills (`image-to-pptx`, `task-history-review`) via PR #1, which was merged to `main`.
- 2026-06-06 — Skills are versioned in-repo (project scope) so all agents share them, rather than relying on ephemeral user-scope installs in the remote container.
- 2026-06-07 — Added `graphify` skill: durable project memory stored in root `KNOWLEDGE.md`, organized as light entity/relationship graph + notes.
- 2026-06-07 — Every session auto-loads this store: a `SessionStart` hook in `.claude/settings.json` cats `KNOWLEDGE.md` into context, and `CLAUDE.md` points agents here. No need to ask agents to read it.

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

## Glossary
- **Skill** — a `SKILL.md` under `.claude/skills/` that Claude Code can invoke (e.g. `/graphify`).
- **graphify store** — this `KNOWLEDGE.md` file; the project's durable memory.

## Gotchas
- The remote execution environment is an ephemeral container, NOT the user's machine: anything not committed/pushed is lost, and `~/.claude/skills/` here does not sync to the user's real setup.
- No CI workflows are configured in this repo, so PR checks are limited to the Copilot reviewer.

## Open Questions
- What is the intended longer-term purpose of `planets` beyond hosting skills?
