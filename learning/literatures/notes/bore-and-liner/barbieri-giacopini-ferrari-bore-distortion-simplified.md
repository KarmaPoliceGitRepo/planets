# A Simplified Methodology for the Analysis of the Cylinder Liner Bore Distortion: Finite Element Analyses and Experimental Validations

- **Source:** SAE Technical Paper 2019-24-0164
- **Drive link:** https://drive.google.com/file/d/1EUjk5Ad9MG8YD1c1fAy_2Rq-uOeK2flr/view
- **Type:** paper
- **Author/Year:** Barbieri, Giacopini, Mangeruga, Bianco (Univ Modena), Mastrandrea (Ferrari SpA) / 2019 (SAE 2019-24-0164)
- **Coverage:** full

## Overview
Develops and validates a simplified FEA methodology for cylinder liner bore distortion analysis of a Ferrari V8 supercar engine (86.5×83 mm, 3.9L, 670 HP). The approach replaces the actual engine head, gasket, and bolts with equivalent pressure distributions after validation against a complete FEM model and experimental measurements. Structural and thermo-structural analyses are performed; simplified model reduces computational time by 80%.

## Unique contribution
Demonstrates a two-stage FEA simplification strategy: first validate a full model against experiment (single bank + test head), then replace head/gasket/bolts with equivalent pressure distributions for rapid design iteration — reducing computation time by 80% while maintaining accuracy. Shows the test head results alone cannot predict actual engine bore distortion due to different stiffness.

## Key concepts
- Cylinder liner bore distortion; FEM/FEA methodology simplification
- Ferrari V8 3.9L; 86.5×83 mm; 96 bar peak firing pressure; turbo
- Test head vs actual head: stiffness difference causes different distortion — experiment needed only for model tuning, not prediction
- Equivalent pressure distribution to replace head/gasket/bolt interactions
- Thermo-structural analysis; thermal + mechanical distortion combined
- Fourier distortion order decomposition; Goetze measurement system context
- Water jacket geometry effect on HTC and distortion

## Methods / results / takeaways
- Phase 1: full FEM model (liners + gasket + actual head + block + bolts); tuned against experimental measurements on single bank with test head.
- Validation: model reproduces measured Fourier coefficients (amplitude and phase) for liner distortion orders.
- Phase 2: simplified model removes head and gasket; replaces with equivalent pressure distributions on liner flanges and block deck → 80% reduction in CPU time; results closely match full model.
- Key finding: test-head experimental data cannot be used to directly validate actual engine bore distortion due to very different head stiffness. Full FEM with actual head is required for prediction.
- Thermo-structural: thermal analysis (CFD-derived HTC on water jacket) + mechanical → combined liner distortion; thermal component significant at operating conditions.
- Tolerance study: different liner geometries (within manufacturing tolerance range) produce different distortion patterns — confirms need for virtual approval before manufacturing.
- Bore-liner relevance: provides industrially validated methodology for rapid liner bore distortion prediction applicable to high-performance engine development; demonstrates sensitivity to head stiffness as key design parameter.
