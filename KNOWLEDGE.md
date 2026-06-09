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
- 2026-06-09 — Read the full *UML for Java Programmers* PDF (supplied via Google Drive MCP; 247pp extracted with PyMuPDF) and built a **consolidated object catalog + knowledge graph** at `coding/uml-for-java-programmers/docs/book-object-graph.md`. ~140 objects extracted across ch.1-6/10/11/12, deduped & merged (same-named objects consolidated, aliases noted), sorted alphanumerically; plus Mermaid **direct-link** classDiagrams per worked example and an **inferred-link** graph (principle exemplars, GoF/PoEAA pattern families, SMC generating its own `ServerController`, the three reusable layers). Gotcha surfaced: the book's `SocketServer`(interface)/`SocketService`(class) names are **inverted** vs our case-study reconstruction.
- 2026-06-09 — Extended that doc (§5/§6) to **link the graph to the OMG UML 2.0 specs** in the shared Drive folder (`formal/05-07-04` Superstructure, `formal/05-07-05` Infrastructure). Used **3 parallel sub-agents** to mine both specs (710+218pp) for the defining clause+page of every UML construct the graph uses; added a graph-edge→metaconstruct bridge, diagram-type→clause map, structural/behavioral/core construct tables (each deep-linked via Drive `#page=` anchors), and a **90-figure index** linking each captioned book figure to its page. Page offset cross-checked: Superstructure PDF page = printed + 16.
- 2026-06-09 — Added a companion doc **`coding/uml-for-java-programmers/docs/sysml-to-java.md`** that **links SysML to the Java case study**, sourced from **Holt & Perry, *SysML for Systems Engineering*, 3rd ed.** (Drive id `1I7UxaGSfYIBS4_dTzu3GiWrZhi6LGImj`; 40 MB PDF — the binary download exceeded the MCP transport, so `read_file_content`'s natural-language extract was used: front matter + Part I MBSE + ch.4 SysML intro + into ch.5 notation). Built with a **parallel sub-agent fleet** (≈20: one per SysML diagram type + per construct family + traceability/allocation/profiles + Holt's MBSE method + a worked example + a master cross-walk). Key finding: **structural + state-machine constructs map directly to Java** (the SMC compiler makes the state-machine mapping *executable*), while SysML's two *new* diagrams — **requirement & parametric** — plus **allocation/viewpoints** map only to tests, traceability and design intent, never to runtime code. SysML 1.x grounded as a **UML 2 profile** (reuses the existing OMG-spec links). Gotchas: `drive.google.com` direct-download and `docs.nomagic.com` are both outside the container's network allowlist (only the Drive MCP works); Holt's extract has an unreliable page-marker→printed-page mapping, so Holt is cited by **section + printed page**, not fabricated PDF `#page=` anchors.

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
- **book-object-graph.md** (in coding repo) —catalogs→ **~140 objects from the UML-for-Java-Programmers book** : alphanumeric, consolidated, with direct + inferred Mermaid link graphs.
- **Google Drive MCP** —supplied→ **the book PDF + OMG UML 2.0 specs** : oversized tool results auto-save to disk; decode base64 → PDF, extract text with PyMuPDF (pypdf's `cryptography` rust binding is broken in this container).
- **book-object-graph.md** —grounded in→ **OMG UML 2.0 Superstructure + Infrastructure** : each construct/edge deep-links to the defining clause+page in the Drive spec PDFs.
- **sysml-to-java.md** (in coding repo) —links→ **SysML constructs → Java realizations** in the SMC case study : grades each construct direct/partial/intent-only; sourced from Holt & Perry 3rd ed. + canonical OMG SysML, reusing the UML-2 spec links (SysML = a UML 2 profile).
- **SMC compiler** —realizes→ **a SysML state machine as executable Java** : `.sm` ⇄ `smc.fsm` model ⇄ generated class; the headline SysML→Java link (the model is the compiled source artifact, the MBSE promise made concrete).

## Glossary
- **Skill** — a `SKILL.md` under `.claude/skills/` that Claude Code can invoke (e.g. `/graphify`).
- **graphify store** — this `KNOWLEDGE.md` file; the project's durable memory.

## Gotchas
- The remote execution environment is an ephemeral container, NOT the user's machine: anything not committed/pushed is lost, and `~/.claude/skills/` here does not sync to the user's real setup.
- No CI workflows are configured in this repo, so PR checks are limited to the Copilot reviewer.
- The **Google Drive MCP is the only way to reach the shared Drive files**: `drive.google.com` direct-download URLs and `docs.nomagic.com` are both **outside the remote container's network allowlist**, and the user's local `/Users/...` paths do not exist in the container. Large PDFs (e.g. the 40 MB *SysML for Systems Engineering* book) **exceed `download_file_content`'s transport** (session-expires); fall back to `read_file_content` (a lossy natural-language extract with `[**Page N**]` markers). That extract's page-marker→printed-page mapping is unreliable, so cite such books by **section + printed page**, not fabricated PDF `#page=` anchors.

## Open Questions
- What is the intended longer-term purpose of `planets` beyond hosting skills?
