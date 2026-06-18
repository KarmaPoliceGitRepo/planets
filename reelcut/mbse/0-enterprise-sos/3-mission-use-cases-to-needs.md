# Enterprise / SoS · Step 2 (cont.) — Mission Use Cases → Capabilities → Stakeholder Needs

> Each mission vignette is decomposed into **mission use cases (MUC)**. The MUC set
> is **consolidated** (dedup + group by purpose) by decomposing each into the
> **capabilities (CAP)** it requires, then **regrouping** by capability. The
> consolidated capability set is what the **stakeholder needs (SN)** must cover —
> so the SN baseline in `1-problem-domain/black-box/1` is *derived from*, and
> justified by, this analysis (bottom-up), closing «deriveReqt» upward.

## 1 · Decompose vignettes → mission use cases

| Vignette | Mission use cases (raw) |
|---|---|
| MV-1 | MUC-a import recording · MUC-b understand content · MUC-c assemble a watchable cut · MUC-d produce output file |
| MV-2 | MUC-e remove dead air · MUC-f reorder topics · MUC-g bridge gaps with transitions · MUC-h caption speech |
| MV-3 | MUC-i replace audio · MUC-j add & duck a track · MUC-k insert photos · MUC-l balance/mute tracks |
| MV-4 | MUC-m keep all media local · MUC-n publish only on explicit action |
| MV-5 | MUC-o carry edit as portable doc · MUC-p resume edit on phone |
| MV-6 | MUC-q autosave & restore (incl. crash recovery) · MUC-r undo/redo edits · MUC-s cancel/abort a long operation |
| MV-7 | MUC-t tighten (filler/silence) · MUC-u extract highlight clips + cover · MUC-v add chapters · MUC-w platform-fit aspect + burned captions · MUC-x translate captions |
| MV-8 | MUC-y clean audio · MUC-z add branding (intro/outro/overlays) · MUC-aa reuse style preset · MUC-ab protect original (non-destructive) · MUC-ac trust preview (WYSIWYG) |

## 2 · Decompose each MUC → capabilities, then regroup (consolidation)

De-duplicating by purpose, the 16 mission use cases collapse onto **10 capabilities**:

| CAP | Capability | Consolidated from MUC | Mission coverage |
|---|---|---|---|
| **CAP-1 Ingest** | bring media into the system | a, (o/p import) | MV-1,3,5 |
| **CAP-2 Comprehend** | segment & tag by topic / speech | b, h | MV-1,2 |
| **CAP-3 Curate** | keep/drop & re-order content | c, e, f | MV-1,2 |
| **CAP-4 Bridge** | gap-aware transitions | g | MV-2 |
| **CAP-5 Re-media** | replace/add audio, add images | i, j, k | MV-3 |
| **CAP-6 Balance** | level/mute/duck tracks (A/V independence) | j, l | MV-3 |
| **CAP-7 Render** | compose final video deterministically | c, d, g, k | MV-1,2,3 |
| **CAP-8 Normalize** | loudness + A/V-sync to spec | d, j | MV-1,2,3 |
| **CAP-9 Caption** | produce correct, re-timed captions | h | MV-2 |
| **CAP-10 Keep-local / Port** | stay on device; portable doc; mobile | m, n, o, p | MV-4,5 |
| **CAP-11 Sustain** | preserve work: autosave/restore, undo/redo, cancel/abort, error recovery | q, r, s | MV-6 |
| **CAP-12 Tighten** | auto-remove filler words + long silences | t | MV-7 |
| **CAP-13 Repurpose** | highlight clips + cover frame | u | MV-7 |
| **CAP-14 Structure** | chapters / timestamps from segments | v | MV-7 |
| **CAP-15 Present** | platform-fit aspect/resolution + burned (open) captions | w | MV-7 |
| **CAP-16 Localise** | spoken-language captions + translation | x | MV-7 |
| **CAP-17 Enhance-audio** | denoise/dehum + speech leveling | y | MV-8 |
| **CAP-18 Brand** | intro/outro, title, lower-thirds, logo/watermark | z | MV-8 |
| **CAP-19 Reuse** | save/apply style presets across episodes | aa | MV-8 |
| **CAP-20 Protect** | non-destructive original | ab | MV-8 |
| **CAP-21 Trust** | WYSIWYG preview = export | ac | MV-8 |

## 3 · Derive stakeholder needs — capability coverage matrix

The stakeholder needs must **cover the full scope demanded by all capabilities**.
Mapping CAP → SN shows the SN baseline is complete (every CAP is owned by ≥1 SN)
and justified (every SN traces to ≥1 CAP):

| Capability | Covered by need(s) |
|---|---|
| CAP-1 Ingest | SN-1 |
| CAP-2 Comprehend | SN-1, SN-2 |
| CAP-3 Curate | SN-1 |
| CAP-4 Bridge | SN-2 |
| CAP-5 Re-media | **SN-5** |
| CAP-6 Balance | **SN-6** |
| CAP-7 Render | SN-1, SN-2 |
| CAP-8 Normalize | SN-2 |
| CAP-9 Caption | SN-2 |
| CAP-10 Keep-local / Port | SN-3, SN-4, **SN-7** |
| CAP-11 Sustain | **SN-8** |
| CAP-12 Tighten | **SN-13** |
| CAP-13 Repurpose | **SN-14** |
| CAP-14 Structure | **SN-15** |
| CAP-15 Present | **SN-10, SN-17** |
| CAP-16 Localise | **SN-11** |
| CAP-17 Enhance-audio | **SN-16** |
| CAP-18 Brand | **SN-18** |
| CAP-19 Reuse | **SN-19** |
| CAP-20 Protect | **SN-9** |
| CAP-21 Trust | **SN-12** |

**Result:** the consolidated capability set is fully covered by **SN-1…SN-19**
(`1-problem-domain/black-box/1-stakeholder-needs.md`) — no capability is orphaned,
no need is unjustified. This is the bottom-up validation of the SN baseline that
the system-level black box then refines into use cases UC-1…UC-10.

```sysml
// capabilities are the bridge; needs derive from the capability scope (req→req)
requirement def CAP_5_ReMedia { doc /* replace/add audio, add images */ }
deriveReqt SN_5_AddOrReplaceMedia    from CAP_5_ReMedia;
deriveReqt SN_6_IndependentManipulation from CAP_6_Balance;
deriveReqt SN_7_Mobile               from CAP_10_KeepLocalPort;
deriveReqt SN_8_PreserveWork         from CAP_11_Sustain;
deriveReqt SN_13_Tighten             from CAP_12_Tighten;
deriveReqt SN_14_Repurpose           from CAP_13_Repurpose;
deriveReqt SN_16_CleanAudio          from CAP_17_EnhanceAudio;
deriveReqt SN_9_NonDestructive       from CAP_20_Protect;
```

> Trace recorded in `5-traceability.md` (mission thread: MV → MUC → CAP → SN → SR).
</content>
</invoke>
