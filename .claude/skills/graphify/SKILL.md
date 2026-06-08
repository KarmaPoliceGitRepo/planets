---
name: graphify
description: Store and recall durable project knowledge in a persistent memory file at the repository root (KNOWLEDGE.md). Use when the user says "graphify", "store knowledge", "remember this for the project", "save this decision/context to root", or whenever an agent should record OR look up durable facts — architecture, decisions, conventions, entities/relationships, glossary — that future sessions need. Invoked via /graphify; agents should also READ the store at the start of non-trivial tasks for context.
---

# graphify — persistent project memory

`graphify` maintains a single durable knowledge store, **`KNOWLEDGE.md` at the repository root**, that survives across sessions (it's committed to git). It is the project's long-term memory: the place agents write hard-won facts and read them back so each new session doesn't start from zero. Knowledge is organized lightly as a graph — entities and the relationships between them — alongside human-readable notes.

There are two modes: **recall** (read) and **store** (write). Most invocations are store; recall should happen automatically at the start of substantive work.

## Recall (read) — do this first on non-trivial tasks

Before starting real work in this repo, read the store for context:

```bash
test -f KNOWLEDGE.md && sed -n '1,400p' KNOWLEDGE.md || echo "No KNOWLEDGE.md yet"
```

Use what you find — established decisions, conventions, gotchas — instead of re-deriving or contradicting it. If something in the store is now wrong, update it (see below) rather than silently working around it.

## Store (write) — when asked to graphify / remember

When the user says "graphify X", "store this", "remember this for the project", etc.:

1. **Read the current store first** so you update in place rather than duplicating.
2. **Decide what's durable.** Capture facts that future sessions will need: architecture, design decisions and their rationale, naming/style conventions, key entities and how they relate, glossary terms, recurring gotchas, and open questions. Do **not** store transient state (current task status, ephemeral TODOs) or secrets/credentials.
3. **Place each item in the right section** (see format). Keep entries terse — one or two lines.
4. **Update, don't blindly append.** If an entry already covers the topic, edit it (and note the change) instead of adding a duplicate. Remove entries that are now false.
5. **Date entries** that are decisions or events: prefix with `YYYY-MM-DD`.
6. **Commit the change** so the memory persists for other agents: stage `KNOWLEDGE.md`, commit with a message like `graphify: record <topic>`, and push to the working branch.

## Store format

`KNOWLEDGE.md` uses these sections (create any that are missing, omit ones with nothing in them):

```markdown
# Project Knowledge (graphify store)

> Durable project memory maintained by the `graphify` skill. Agents read this for
> context and append durable facts here. Keep entries terse; date decisions.

## Overview
One-paragraph description of what this project is.

## Architecture
- Bullet facts about structure, components, data flow.

## Decisions
- YYYY-MM-DD — Decision and its rationale.

## Conventions
- Coding/style/process conventions to follow.

## Entities & Relationships
<!-- the lightweight graph: Entity —relation→ Entity : note -->
- **EntityA** —depends on→ **EntityB** : why.

## Glossary
- **Term** — definition.

## Gotchas
- Non-obvious traps and how to avoid them.

## Open Questions
- Unresolved questions worth revisiting.
```

The **Entities & Relationships** section is the "graph": each line is an edge `Subject —relation→ Object`. Optionally regenerate a Mermaid view from these edges when asked:

```mermaid
graph LD
  EntityA -->|depends on| EntityB
```

## Notes & limits

- One store per repo, at the root, committed to git — that's what makes it shared, persistent memory for every agent working on the repo.
- This skill is invoked on demand. To make every session *automatically* aware of the store, a repo can add a pointer in `CLAUDE.md` ("Read `KNOWLEDGE.md` for project memory; use the graphify skill to update it") and/or a `SessionStart` hook that injects the store. This repo already ships both; in a repo that doesn't, offer to add them rather than assuming.
- Never write secrets, tokens, or personal data into the store; it's committed and shared.
