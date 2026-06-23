# Traceability

> The MagicGrid closes the loop across layers with SysML relationships
> (your #5 rules). Direction: **SN —«deriveReqt»→ SR —«deriveReqt»→ CR/HC**;
> functions **«refine»** SR & SN; logical subsystems **«satisfy»** SR; behaviour
> **«allocate»** to structure; requirements **«verify»** by behaviour/structure/tests;
> MoP **value-bind** to structure and roll up to MoE.

## Mission thread (Enterprise/SoS: Vignette → Mission UC → Capability → Need)
```mermaid
flowchart LR
  MV1["MV-1 raw→watchable"] --> CAP1["CAP-1 Ingest"] & CAP3["CAP-3 Curate"] & CAP7["CAP-7 Render"]
  MV2["MV-2 tighten/order"] --> CAP2["CAP-2 Comprehend"] & CAP4["CAP-4 Bridge"] & CAP9["CAP-9 Caption"]
  MV3["MV-3 re-media"] --> CAP5["CAP-5 Re-media"] & CAP6["CAP-6 Balance"]
  MV4["MV-4 private"] --> CAP10["CAP-10 Keep-local/Port"]
  MV5["MV-5 on-the-go"] --> CAP10
  CAP1 --> SN1["SN-1"]; CAP2 --> SN2["SN-2"]; CAP3 --> SN1
  CAP4 --> SN2; CAP5 --> SN5["SN-5"]; CAP6 --> SN6["SN-6"]
  CAP7 --> SN1; CAP8["CAP-8 Normalize"] --> SN2; CAP9 --> SN2
  CAP10 --> SN3["SN-3"] & SN4["SN-4"] & SN7["SN-7"]
  MV6["MV-6 never lose work"] --> CAP11["CAP-11 Sustain"] --> SN8["SN-8"]
  MV7["MV-7 grow/repurpose"] --> CAP12["CAP-12 Tighten"] & CAP13["CAP-13 Repurpose"] & CAP15["CAP-15 Present"] & CAP16["CAP-16 Localise"]
  MV8["MV-8 polish/brand"] --> CAP17["CAP-17 Enhance-audio"] & CAP18["CAP-18 Brand"] & CAP20["CAP-20 Protect"] & CAP21["CAP-21 Trust"]
  CAP12 --> SN13["SN-13"]; CAP13 --> SN14["SN-14"]; CAP15 --> SN10["SN-10/17"]; CAP16 --> SN11["SN-11"]
  CAP17 --> SN16["SN-16"]; CAP18 --> SN18["SN-18"]; CAP20 --> SN9["SN-9"]; CAP21 --> SN12["SN-12"]
```
> Bottom-up validation: every capability is owned by ≥1 need; every need traces to
> ≥1 capability (see `0-enterprise-sos/3`). SN baseline therefore complete & justified.

## Vertical thread (p.27 style: Need → System Req → Component Req)
```mermaid
flowchart LR
  SN5["SN-5 add/replace media"] -->|deriveReqt| SR23["SR-2.3 replace audio"]
  SN5 -->|deriveReqt| SR24["SR-2.4 add audio"]
  SN5 -->|deriveReqt| SR25["SR-2.5 image clips"]
  SN6["SN-6 independent A/V"] -->|deriveReqt| SR21["SR-2.1 demux"] --> SR22["SR-2.2 portable model"]
  SR23 -->|deriveReqt| CR6["CR-6"]; SR24 -->|deriveReqt| CR7["CR-7"]
  SR25 -->|deriveReqt| CR8["CR-8"]; SR21 -->|deriveReqt| CR5["CR-5"]; SR22 -->|deriveReqt| CR4["CR-4"]
  SN7["SN-7 mobile"] -->|deriveReqt| HC1["HC-1 (constraint)"]
  SN8["SN-8 preserve work"] -->|deriveReqt| SR32["SR-3.2 autosave/restore"]
  SN8 -->|deriveReqt| SR33["SR-3.3 undo/redo"] --> F17["F-17"]
  SN8 -->|deriveReqt| SR34["SR-3.4 cancel/progress"]
  SR32 --> F16["F-16"]
```

## Cross-pillar matrix (per system requirement)
| SR | refinedBy (F, behavior) | satisfiedBy (LS, structure) | verifiedBy (test) | param (MoP) |
|---|---|---|---|---|
| SR-1.1 segment | F-4 | LS-Segment | T-5 | — |
| SR-1.2 keep/order | F-5,F-6 | LS-EditModel | T-1,T-2 | — |
| SR-1.3 render | F-8 | LS-Render | T-3,T-4 | MOP-2,MOP-7 |
| SR-1.4 captions | F-9 | LS-Caption | T-6 | MOP-6 |
| SR-1.5 loudness | F-10 | LS-Master | T-7 | MOP-1 |
| SR-1.6 A/V sync | F-8 | LS-Render | T-3,T-4 | MOP-2 |
| SR-1.7 local-only | — (context) | LS-HMI | T-7 | MOP-8 |
| SR-2.1 demux | F-2 | LS-Ingest | T-8 | — |
| SR-2.2 portable model | F-2 | LS-EditModel | T-8 | — |
| SR-2.3 replace audio | F-11 | LS-Caption/EditModel | T-9 | MOP-6 |
| SR-2.4 add audio | F-12 | LS-AudioMix | T-10 | MOP-1,MOP-5 |
| SR-2.5 image clips | F-13 | LS-Render | T-11 | MOP-4 |
| SR-2.6 mix loudness | F-10,F-12 | LS-Master | T-9,T-10 | MOP-1 |
| SR-2.8 MoP threshold | F-6,F-14 | LS-EditModel | T-8..T-11 | MOP-3 |
| SR-3.1 validate input | F-15 | LS-Ingest | T-12 | — |
| SR-3.2 autosave/restore | F-16 | LS-HMI | T-13 | — |
| SR-3.3 undo/redo | F-17 | LS-EditModel | T-14 | — |
| SR-3.4 cancel/progress | F-18,F-19 | LS-HMI | T-15 | — |
| SR-3.5 invalidate-on-source-change | F-4,F-11 | LS-Caption | T-9 | MOP-6 |
| SR-3.6 incremental re-render | F-20 | LS-Render | T-16 | MOP-7 |
| SR-4.1 non-destructive | F-30 | LS-Ingest | T-17 | — |
| SR-4.2 platform aspect/preset | F-25 | LS-Render | T-18 | MOP-10 |
| SR-4.3 multilingual captions | F-26 | LS-Caption | T-19 | MOP-10 |
| SR-4.4 WYSIWYG preview | F-31 | LS-Render | T-20 | — |
| SR-4.5 auto-tighten | F-21 | LS-Segment | T-21 | MOP-11 |
| SR-4.6 highlight clips + cover | F-22 | LS-Render | T-22 | — |
| SR-4.7 chapters | F-23 | LS-Segment | T-23 | MOP-11 |
| SR-4.8 clean audio | F-24 | LS-AudioMix | T-24 | MOP-12 |
| SR-4.9 burned-in captions | F-27 | LS-Render | T-25 | MOP-10 |
| SR-4.10 branding | F-28 | LS-Render | T-26 | — |
| SR-4.11 style presets | F-29 | LS-EditModel | T-27 | — |
| SR-5.1 transcript export | F-32 | LS-Caption | T-28 | — |
| SR-5.2 batch export | F-33 | LS-Render | T-29 | MOP-7 |
| SR-5.3 license flag | F-34 | LS-Ingest | T-30 | — |
| SR-5.4 embed metadata | F-35 | LS-Render | T-31 | — |

## MoE roll-up
MOE-2←MOP-8 · MOE-3←MOP-1,MOP-2,MOP-5 · MOE-6←MOP-6 · MOE-5←MOP-3 · MOE-1←MOP-4,MOP-7 · MOE-4←MOP-9 ·
MOE-7←MOP-10 · MOE-8←MOP-11 · MOE-9←MOP-12.

## Test catalogue (`../tests/`)
T-1 reorder · T-2 keep/renumber · T-3 timing math · T-4 ffmpeg render · T-5 segment ·
T-6 caption remap · T-7 e2e/loudness · **T-8** demux/portable-model · **T-9** replace-audio ·
**T-10** add-audio · **T-11** image-clip · **T-12** validate-input · **T-13** autosave/restore ·
**T-14** undo/redo · **T-15** cancel/progress · **T-16** incremental-render ·
**T-17** non-destructive · **T-18** aspect/preset · **T-19** multilingual-captions ·
**T-20** WYSIWYG-preview · **T-21** auto-tighten · **T-22** highlight-clip ·
**T-23** chapters · **T-24** clean-audio · **T-25** burned-captions · **T-26** branding ·
**T-27** style-preset · **T-28** transcript-export · **T-29** batch-export ·
**T-30** license-flag · **T-31** embed-metadata. (T-1…T-7 Built; T-8…T-31 Planned.)

## Conformance
Model now rooted at the **Enterprise/SoS** layer: SoI black-box node inside the
System-of-Systems context block, external + environment nodes (incl. iPhone &
Android), SoS BDD + IBD with exchanged items, mission vignettes → mission use cases
→ capabilities → **derived** stakeholder needs (bottom-up validation). Below it, all
four pillars populated across **Conceptual / Logical / Physical** layers (NTRS p.7),
package tree mirrors p.10, relationships per your #5, requirement attributes per p.15,
requirement stereotypes per p.16. Mobile (SN-7) is a hardware **constraint** (HC-1),
detailed design deferred.
