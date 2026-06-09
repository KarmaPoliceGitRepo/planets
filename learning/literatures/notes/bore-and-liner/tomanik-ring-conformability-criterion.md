# Piston Ring Conformability Needs Considering the Bore Distortion Harmonic Analysis

- **Source:** SAE 2009-01-0190 (Tomanik 2009)
- **Drive link:** https://drive.google.com/file/d/1vLYGT5qQ6yRJQSg-MMIlmVz2mYztH6gO/view
- **Type:** paper
- **Author/Year:** Tomanik / 2009 (SAE Technical Paper 2009-01-0190; Mahle)
- **Coverage:** full

## Overview
Develops an improved ring conformability criterion based on bore distortion harmonic decomposition. Previous Muller criterion gives a single global pass/fail; this work (extending the "RDT" criterion from MIT) defines per-order conformability limits and a composite ΣU% metric. ~105,000 parametric simulation cases run to map conformability across ring stiffness, bore distortion amplitude, and harmonic order combinations.

## Unique contribution
First practical industry implementation of per-harmonic conformability assessment (ΣU% = Σ(Ui/Uimax_T) ≤ 100%) that combines all harmonic orders into a single compliance budget, replacing the single-order Muller criterion. Demonstrates that 2nd-order (ovality) and 0th-order (diameter mismatch) dominate under actual operating conditions where thermal and mechanical bore distortions act simultaneously.

## Key concepts
- Ring conformability; Muller criterion; RDT criterion (MIT)
- Bore distortion harmonic analysis; Fourier decomposition (orders 0–8+)
- Per-harmonic conformability limit Uimax_T; composite ΣU% metric
- Ring radial stiffness EI; ring free gap; ring tension
- 2nd-order (oval) distortion; 0th-order (diameter); higher-order distortion
- Parametric simulation; ~105,000 cases
- Thermal bore distortion vs head-bolt mechanical distortion
- Blowby and oil consumption consequences of poor conformability

## Methods / results / takeaways
- Bore distortion represented as Fourier series: r(θ) = Σ Ai cos(i·θ + φi), orders i = 0, 2, 3, 4, …
- Ring modelled as curved beam with radial flexibility; conformability condition: ring follows bore without gaps > critical leakage threshold.
- Per-order conformability limit Uimax_T derived from simulations; combined metric: ΣU% = Σ(Ui/Uimax_T) × 100% ≤ 100%.
- ~105,000 parametric cases: varied ring EI, bore distortion amplitudes per order, ring free shape.
- Under engine operating conditions: thermal oval (2nd order) and total diameter change (0th order) are dominant contributors to ΣU%; higher orders (3–8) matter mainly in cold assembly or with severe head-bolt patterns.
- Comparison with Muller criterion: Muller (single order, single amplitude) is overly conservative for some orders and insufficient for others; ΣU% gives more accurate pass/fail with physical basis.
- Practical guidance: for a typical passenger car gasoline engine bore, ring EI optimisation against 2nd and 0th order distortion captures >80% of conformability risk.
- Poor conformability consequences: blowby increase, oil consumption increase, uneven ring wear.
- Note: Tomanik criterion has become industry standard at Mahle and referenced in subsequent literature (e.g., Gode 2018 thesis uses this approach for ring conformability assessment).
