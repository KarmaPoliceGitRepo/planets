# Investigation on Cylinder Bore Deformation under Static Condition Based on Fourier Decomposition

- **Source:** SAE Technical Paper 2017-01-0366 (March 2017), DOI: 10.4271/2017-01-0366
- **Drive link:** https://drive.google.com/file/d/1e3EJ8e0B2Y-oStLpZb2ruIlrUjR2r2RL/view
- **Type:** paper
- **Author/Year:** Liang, Xingyu; Wang, Yuesen; Huang, Shuhe; Yang, Guichun; Tang, Lin; Cui, Guoqi (State Key Lab of Engines, Tianjin University / China North Engine Research Institute) / 2017 (SAE 2017-01-0366)
- **Coverage:** full

## Overview
FEA study of cylinder bore distortion under static (bolt pretightening only) conditions for a V6 engine (132 mm bore diameter). Hypermesh model (~3 million tetrahedral elements); MATLAB Fourier decomposition. Parametric study of bolt preload magnitude (baseline 80,000 N ± 50–100%), bolt distribution pattern (a1/b1 vs a/b; 4 vs 8 bolts), bolt length (40/60/80 mm), and first-thread location (0/20/40 mm from deck). Validated against V-INCOMETER experimental measurements. Maximum static distortion ~30 µm. Dominant Fourier orders: 2nd (oval) and 4th (cloverleaf); orders above 8th negligible. More uniform bolt distribution and longer bolts both reduce distortion.

## Unique contribution
Parametric investigation isolating the effect of bolt preload level, distribution pattern, bolt length, and first-thread location on static bore distortion magnitude and Fourier order content; validates that 2nd and 4th orders dominate static distortion; demonstrates that 8-bolt uniform distribution reduces both amplitude and higher-order content vs 4-bolt arrangement.

## Key concepts
- V6 engine, bore diameter 132 mm; V-INCOMETER for validation; ~3 million tetrahedral elements (max 4 mm, contact surfaces 1 mm)
- Bolt pretension formula: tightening torque T = T1 + T2; F0 = 80,000 N per bolt at 130 Nm torque, d=8 mm
- 24 cylinder head bolts total (V6); 4 bolts per cylinder average
- Maximum static distortion: ~30 µm (comparable to dynamic thermal distortion → must not be neglected)
- Dominant orders: 2nd (oval) and 4th (cloverleaf); orders > 8 contribute negligibly
- Preload effect: 48% increase in distortion when preload increases by 100% (diminishing returns)
- Bolt distribution: symmetric a1/b1 (equal spacing) → lower distortion; 8-bolt → lower amplitude + less fluctuation vs 4-bolt
- Bolt length: longer bolt (80 mm) → smaller distortion (load spreads over longer thread engagement); 40 → 60 → 80 mm progressively reduces distortion
- First-thread location: lower first thread position (closer to deck = 0 mm) → smaller deformation in upper half
- Geometry: end cylinders worse than middle in cast iron V-config (asymmetric thermal not in scope here); but V6 geometry affects results per cylinder
- Compares favourably with Bird & Gartside, Maassen et al. SAE 2001-01-0569, and Koch et al. 1998

## Methods / results / takeaways
- Validation: FEA vs V-INCOMETER at same cross-section; match in both magnitude and trend across multiple sections.
- 32 mm cross-section (location of first ring) used as primary analysis plane.
- Radial deformation contour: maximum expansion on exhaust side; maximum shrinkage on intake side — asymmetric even under static bolt loads.
- Upper half deforms more than lower half under pretightening; first-thread location controls how far down this asymmetry penetrates.
- Key insight: static distortion up to 30 µm not negligible; it adds to dynamic thermal distortion and is under design control via bolt geometry.
- Bore-liner relevance: establishes static baseline distortion levels, dominant Fourier orders, and design levers (bolt count, length, distribution) for reducing static bore distortion before thermal effects occur; confirms 2nd and 4th orders as primary concerns consistent with other literature.
