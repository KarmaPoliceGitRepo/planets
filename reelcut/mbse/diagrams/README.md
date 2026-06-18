# ReelCut MBSE — diagram SVGs

Rendered SVGs of the model's diagrams, organised to **mirror the MagicGrid
package structure** (one folder per cell). The **Mermaid blocks inside
`../0X-*.md` remain the single source of truth** (decision Q5-c / G-2); the `.mmd`
files here are *extracted* from them and the `.svg` files are *rendered* from the
`.mmd`. Re-generate after any model edit with `./render.sh`.

## Contents (MagicGrid cell → diagram)

| Cell | Folder / file | Diagram |
|---|---|---|
| **B2** Use Cases | `B2-use-cases/use-case-diagram.svg` | actor + UC-1…UC-10 |
| **B3** System Context | `B3-system-context/system-context.svg` | ReelCut black box, actors, boundary flows |
| **W3** Structure | `W3-structure/block-definition.svg` | BDD — blocks B-1…B-13 (Built/Planned) |
| **W3** Structure | `W3-structure/internal-block.svg` | IBD — Built data-flow |
| **W2** Behaviour | `W2-behaviour/wizard-state-machine.svg` | wizard states (Media step = Planned) |
| **W2** Behaviour | `W2-behaviour/a6-export-activity.svg` | A-6 export activity (two-stage render) |
| **W2** Behaviour | `W2-behaviour/a10-replace-audio-activity.svg` | A-10 replace-audio activity |

> The **Requirements (B1/W1)** and **Parameters (B4/W4)** pillars are authored as
> SysML v2 textual notation + tables (not box-and-line diagrams), so they have no
> SVG here by design — see `../01-requirements-model.md` and `../06-parameters.md`.

## Regenerate
```bash
./render.sh        # extracts .mmd from the model, renders .svg (needs Node; fetches Chromium once)
```
