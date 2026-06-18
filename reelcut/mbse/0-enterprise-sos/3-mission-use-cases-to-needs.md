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

**Result:** the consolidated capability set is fully covered by **SN-1…SN-8**
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
```

> Trace recorded in `5-traceability.md` (mission thread: MV → MUC → CAP → SN → SR).
</content>
</invoke>
