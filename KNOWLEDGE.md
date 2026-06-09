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
- 2026-06-06 — Added first two skills (`image-to-pptx`, `task-history-review`) via PR #1, which was merged to `main`.
- 2026-06-06 — Skills are versioned in-repo (project scope) so all agents share them, rather than relying on ephemeral user-scope installs in the remote container.
- 2026-06-07 — Added `graphify` skill: durable project memory stored in root `KNOWLEDGE.md`, organized as light entity/relationship graph + notes.
- 2026-06-07 — Every session auto-loads this store: a `SessionStart` hook in `.claude/settings.json` cats `KNOWLEDGE.md` into context, and `CLAUDE.md` points agents here. No need to ask agents to read it.
- 2026-06-09 — Implemented the *UML for Java Programmers* (R. C. Martin) end-to-end **SMC remote-service case study** as a learning artifact. It lives in the sibling repo **`KarmaPoliceGitRepo/coding`** at `uml-for-java-programmers/` (not in this repo), branch `claude/uml-java-programmers-eqyyq1`. JDK 21 + Maven + JUnit 5; 15 tests pass incl. a real-socket end-to-end client/server compile. Reconstruction (book PDF + O'Reilly TOC are network-blocked from the remote container), faithful to the book's described architecture.

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
- **coding repo** —hosts→ **SMC remote-service case study** (`uml-for-java-programmers/`) : UML-for-Java-Programmers learning project.
- **SMC case study** —layered as→ **socketserver** (reusable `SocketServer`/`SocketService`) + **smc compiler** (`fsm` model, `SmcParser`, `JavaCodeGenerator`, `Compiler`) + **smc.remote** (serializable message protocol, `SMCRemoteServer`/`SMCRemoteService`/`SMCRemoteClient`).

## Glossary
- **Skill** — a `SKILL.md` under `.claude/skills/` that Claude Code can invoke (e.g. `/graphify`).
- **graphify store** — this `KNOWLEDGE.md` file; the project's durable memory.

## Gotchas
- The remote execution environment is an ephemeral container, NOT the user's machine: anything not committed/pushed is lost, and `~/.claude/skills/` here does not sync to the user's real setup.
- No CI workflows are configured in this repo, so PR checks are limited to the Copilot reviewer.

## Open Questions
- What is the intended longer-term purpose of `planets` beyond hosting skills?
