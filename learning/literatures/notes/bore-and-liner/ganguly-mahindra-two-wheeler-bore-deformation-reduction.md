# Prediction and Reduction of Cylinder Liner Bore Deformation for a Two Wheeler Single Cylinder Gasoline Engine

- **Source:** SAE International Journal of Engines 8(4) (2015), SAE 2015-01-1742
- **Drive link:** https://drive.google.com/file/d/14aRi26rAn9gaYsdfnyUiCKt2yALc2ilN/view
- **Type:** paper
- **Author/Year:** Ganguly, Agarwal, Santra (Mahindra Two Wheelers Ltd.) / 2015 (SAE Int. J. Engines 8(4); SAE 2015-01-1742)
- **Coverage:** full

## Overview
Iterative FEA-driven design optimisation of cylinder liner bore deformation for a high-cubic-capacity single-cylinder gasoline two-wheeler engine that was causing piston scuffing and seizure in endurance tests. Uses ABAQUS with second-order tetrahedral elements. Four design iterations (liner thickness, block ribs, crankcase stiffness) reduce bore deformation by >17.5% at BDC zone (critical zone) and ~46% at TDC zone. Validated against test measurements.

## Unique contribution
Demonstrates a fast CAE-driven iterative design methodology to eliminate piston seizure from excessive liner bore deformation in a packaging-constrained two-wheeler engine, identifying crankcase stiffness as the key driver of BDC-zone inward deformation and achieving targets with only 364 g total weight addition.

## Key concepts
- Cylinder liner bore deformation; piston scuffing/seizure; BDC tilting marks
- Fourier harmonic orders: 0th (diameter change), 1st (eccentricity), 2nd (oval), 3rd (3-lobe), 4th (4-lobe)
- ABAQUS; second-order 10-node tetrahedral elements; contact nonlinearity; material plasticity
- Bolt pretension load case; multi-layer gasket simplification (single layer → under-prediction)
- Design iterations: window filling, liner thickness increase, block ribs/ring, crankcase stiffening
- Crankcase stiffness: increasing stiffness reverses BDC inward deformation direction
- Two-wheeler engine: packaging constraints; ADC12 aluminium block + cast iron liner

## Methods / results / takeaways
- Base engine: single-cylinder gasoline; 4 M10 studs + 2 M6 bolts; max deformation at TDC and BDC ends; BDC inward contraction ~35 µm causing piston BDC tilt marks → seizure.
- FEA: ABAQUS; second-order tet elements; sliding + tie contacts; gasket as single-layer steel (→ under-prediction of deformation magnitude vs test, but same trend).
- Design iteration 1 (window filling): counter-productive — transferred deformation from YY to XX plane; rejected.
- Design iteration 2 (liner OD +1 mm): TDC zone improves; BDC zone still excessive; carried forward.
- Design iteration 3 (block ribs + annular ring at head face + crankcase pockets): ~7% improvement at BDC.
- Design iteration 4 (crankcase ribs): >17.5% reduction at BDC zone; ~46% reduction at TDC zone — target met. Total weight addition 364 g.
- Head strengthening: additional deformation reduction + head bolt area stress below 140 MPa yield.
- Experimental validation: test shows same qualitative trend with design iteration 4 + strengthened head; seizure eliminated.
- Bore-liner relevance: practical case study showing how crankcase + liner + head stiffness changes affect bore distortion; demonstrates ABAQUS methodology for two-wheeler application.
