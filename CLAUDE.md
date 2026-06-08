# CLAUDE.md

## Project memory (graphify)

This repo keeps durable project memory in **`KNOWLEDGE.md` at the repo root**, maintained by the `graphify` skill.

- **Read it first.** At the start of any non-trivial task, read `KNOWLEDGE.md` for established architecture, decisions, conventions, and gotchas. A `SessionStart` hook (`.claude/settings.json`) also auto-injects it into context each session.
- **Keep it current.** When you learn or decide something durable, record it with the `graphify` skill (`/graphify`) and commit the update.

## Skills

Reusable skills live in `.claude/skills/`: `graphify` (project memory), `image-to-pptx` (images → editable PowerPoint), `task-history-review` (recap recent repo activity).
