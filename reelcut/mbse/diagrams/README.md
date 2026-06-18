# ReelCut MBSE — diagram SVGs

Rendered SVGs of the model's diagrams, organised by **MagicGrid layer** (mirroring
the package structure of NTRS 20190032390). The **Mermaid blocks in the model
files are the single source of truth**; `render.sh` *extracts* `.mmd` and *renders*
`.svg`. Re-run after any model edit.

| Layer | File | Diagram |
|---|---|---|
| Conceptual | `conceptual/use-cases.svg` | use cases (UC-1…10) inside the SoI context block |
| Conceptual | `conceptual/system-context-ibd.svg` | **IBD** system context (ports/interface blocks/flows) |
| Logical | `logical/functional-analysis-activity.svg` | UC-6 export activity (functions) |
| Logical | `logical/logical-subsystems-bdd.svg` | logical subsystem breakdown |
| Logical | `logical/logical-subsystems-ibd.svg` | logical interconnections (item flows) |
| Physical | `physical/component-structure-bdd.svg` | physical components (scripts) |
| Physical | `physical/component-behavior-sequence.svg` | export sequence |
| Traceability | `traceability/vertical-thread.svg` | SN → SR → CR/HC thread |

```bash
./render.sh        # regenerate (needs Node; fetches Chromium once)
```

> Requirements/Parameters cells are authored as SysML v2 textual + tables (no
> box-and-line diagram), so they have no SVG by design.
