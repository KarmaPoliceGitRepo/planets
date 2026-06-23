# CLAUDE.md

## Project memory (graphify)

This repo keeps durable project memory in **`KNOWLEDGE.md` at the repo root**, maintained by the `graphify` skill.

- **Read it first.** At the start of any non-trivial task, read `KNOWLEDGE.md` for established architecture, decisions, conventions, and gotchas. A `SessionStart` hook (`.claude/settings.json`) also auto-injects it into context each session.
- **Keep it current.** When you learn or decide something durable, record it with the `graphify` skill (`/graphify`) and commit the update.

## MBSE behaviour rule (persistent)

For any **MBSE task**, you **MUST** use the `brainstorming` skill (`/brainstorming`)
whenever you **enrich** or need to **complete the scope of behaviour models**
(use cases, activities, sequences, state machines, interactions, functions).
Behaviour-model completeness is the case where brainstorming is mandatory, not
optional — enumerate all possible behaviours (happy, alternate, exception, edge)
before writing them into the model.

## Communication rule — caveman in chat, full prose in artifacts (persistent)

Default chat register for this repo is **caveman mode** (the `caveman` skill): compress
replies to the user. **Convert to non-caveman (normal, full English) when ANY of these
holds:**

- The user explicitly asks for normal/expanded prose (or turns caveman off).
- The output is a **durable artifact**, not chat — i.e. anything written to disk or
  shared: MBSE model files, code, commit and PR messages, `KNOWLEDGE.md`, specs/design
  docs, file captions. Artifacts are **always** full, precise English — never caveman.
- Precision matters more than brevity: definitions, requirement statements, rationale.

Rule of thumb: **talk caveman, write proper.** Caveman is a chat-only compression; it
must never leak into committed content.

## MBSE drift-check rule (persistent)

After editing the ReelCut MBSE model and **before committing**, run the drift checker and
keep it green:

```
.claude/hooks/drift-check.sh
```

It verifies, fast and deterministically: **code-fence parity** in every model `.md`, and
that every system requirement's `derivedFrom` need and `refinedBy` function **resolves to
a defined ID** (no dangling traceability). A `Stop` hook (`.claude/settings.json`) runs it
automatically and surfaces any findings as a warning — that is a backstop, not a
substitute for running it yourself. **Whenever you change mermaid diagrams, also run
`reelcut/mbse/diagrams/render.sh` and confirm all diagrams render** (the drift checker does
not render — it only checks fence balance).

## Skills

Reusable skills live in `.claude/skills/`: `graphify` (project memory), `image-to-pptx` (images → editable PowerPoint), `task-history-review` (recap recent repo activity).
