# Analysis of Cylinder Bore Distortion During Engine Operation

- **Source:** SAE Technical Paper 950541, International Congress and Exposition, Detroit, February–March 1995
- **Drive link:** https://drive.google.com/file/d/1RC_kqrRdshCjt0ToaOEdPaNV_HWcGV1D/view
- **Type:** paper
- **Author/Year:** Abe, Shizuo; Suzuki, Makoto (Toyota Motor Corp.) / 1995 (SAE 950541)
- **Coverage:** full

## Overview
Develops an ABAQUS FEM method for cylinder bore distortion during engine operation that accounts for the frictional sliding between the cylinder head and the block top deck via the gasket. Models thermal, combustion pressure, and assembly loads for a Toyota 4-cylinder 1.5L cast iron block / aluminium head closed-deck Siamese engine. Key finding: thermal distortion is the dominant effect on operating bore distortion, much larger than bolt-clamping distortion. Head–block friction coefficient (µ = 0.1) calibrated from a thermal cycle test. Results compare better with Fujimoto's fired measurements than conventional (full-slide) methods.

## Unique contribution
First explicit inclusion of head–block deck friction hysteresis in FEM bore distortion simulation, demonstrating that this frictional sliding mechanism causes characteristic post-run 2nd-order distortion increase; also shows thermal operating distortion dominates bolt-clamping distortion and requires thermo-structural FEM (not just mechanical assembly analysis).

## Key concepts
- ABAQUS non-linear FEM; thermo-structural; Siamese cast iron block + aluminium head; closed deck
- Head–block friction: non-linear gasket interface (gap + nonlinear spring + plastic slip model); bolt = beam element
- Coefficient of friction µ = 0.1 between head and block (calibrated from thermal cycle test vs Loenne)
- Thermal cycle hysteresis: head expands → slides outward during heating; contracts → slides inward during cooling; friction direction reversal → net distortion after cooling
- Fourier order decomposition: 2nd and 3rd order dominant in thermal operating distortion
- Thermal distortion >> clamping distortion; combustion gas pressure effect is small (slight 2nd order increase, slight 4th order decrease)
- Dunaevsky ring conformability criterion used to evaluate piston ring conformability to calculated bore distortion
- Validation against Fujimoto SAE 910042 fired measurements

## Methods / results / takeaways
- FEM model: half of cylinders 1 and 2; dummy head (thickness calibrated to match real-head bolt-down distortion); gasket as interface element with gap + nonlinear spring (normal) + plastic slip (tangential).
- Temperature distribution: measured at multiple block points; heat transfer BCs adjusted until calculated wall temperatures match (within 10°C); wall between Siamese bores ~80°C hotter than thrust/anti-thrust side walls at 5200 rpm full load.
- Bore distortion during operation: thermal load >> combustion gas pressure; Siamese bore hot inter-bore wall → expansion perpendicular to crankshaft → 2nd order distortion increase (2nd and 3rd cylinders most affected).
- Combustion pressure effect: small; slightly increases 2nd order (Siamese inter-bore wall thicker), slightly decreases 4th order (head seating force reduced at TDC → bolt-induced distortion partially relaxed).
- Post-engine-run (cooled) distortion: 2nd order increases (especially cylinders 2 and 3) — explained by head friction hysteresis: during cooling, aluminium head slides inward, dragging Siamese inter-bore wall inward.
- Friction coefficient determination: sensitivity study of µ on post-run 2nd order; µ = 0.1 matches Loenne's measurements.
- Piston ring conformability (Dunaevsky formula): 2nd and 3rd order thermal operating distortions significantly exceed ring conformability limits → increased oil consumption risk.
- Comparison with Fujimoto: new method (with head friction) agrees better with fired measurements than conventional (perfect slip) method.
- Bore-liner relevance: thermo-structural FEM methodology for predicting fired bore distortion; demonstrates thermal distortion is the primary operating distortion driver; quantifies head–block friction contribution to post-run distortion; applies Dunaevsky conformability criterion.
