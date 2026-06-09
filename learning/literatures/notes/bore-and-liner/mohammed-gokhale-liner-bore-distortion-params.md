# Analysis of Parameters Affecting Liner Bore Distortion in DI Diesel Engines

- **Source:** SAE Technical Paper 2015-26-0178
- **Drive link:** https://drive.google.com/file/d/1Jc0G7xPds1RmYFlpZ-bq4hxhBbQy7XsY/view
- **Type:** paper
- **Author/Year:** Mohammed, Gokhale, Pardeshi, Gokhale, Kumar (Kirloskar Oil Engines / College of Engineering Pune) / 2015 (SAE 2015-26-0178)
- **Coverage:** full

## Overview
Parametric FEA study of four design parameters affecting cylinder liner bore distortion in a heavy-duty off-highway direct-injection diesel engine with a top-hung liner: gasket thickness (0.85–1.3 mm), liner wall thickness (four variants A–D), number of head bolts (4 vs 6), and bolt preload level (75–90% proof strength). Uses ANSYS mechanical APDL. Validated experimentally by measuring bore distortion at 10 axial planes using a custom dial gauge on four machined liners.

## Unique contribution
Quantifies the relative importance of four assembly/geometry parameters on liner bore distortion, finding that liner wall thickness and bolt preload are the most influential parameters while MLS gasket thickness (in the 0.85–1.3 mm range) has negligible effect; validates FEA trends against physical measurements to within 10–15%.

## Key concepts
- Liner bore distortion (LBD); harmonic orders 0–5; Fourier decomposition
- FEA of crankcase–liner–cylinder head assembly; ANSYS APDL; ANSYS Mechanical
- MLS (multi-layer steel) gasket; top-hung liner; O-ring sealing below liner
- Bolt preload calculation: torque coefficient K; proof strength; M14/M16/M18 bolts
- Gasket thickness effect; liner thickness (4 variants A–D); 4-bolt vs 6-bolt configuration
- Bore distortion measurement: custom dial gauge; 10 axial planes; 10° circumferential intervals
- Siamese bore / closed deck relevance

## Methods / results / takeaways
- FEA model: crankcase + liner + cylinder head assembly; fixed support at crankcase bottom; cylindrical support at liner O-ring grooves; bolt preload as per specification.
- Material properties assigned to each component; frictional contacts defined between mating surfaces.
- Gasket thickness (0.85–1.3 mm MLS): bore distortion shape and magnitude essentially unchanged across all five configurations — MLS gasket stiffness dominates over thickness variation in this range.
- Liner thickness: thinnest liner (A) produces highest distortion; distortion decreases nearly linearly with increasing thickness. Liner thickness is the most influential parameter among the four studied.
- Number of head bolts: 4-bolt configuration produces higher distortion than 6-bolt; distortion shape changes from 2-lobe (6-bolt) to 4-lobe (4-bolt), matching the bolt spacing symmetry.
- Bolt preload: bore distortion increases nearly linearly with preload from 75% to 90% of proof strength; shape unchanged, magnitude scales with preload.
- Experimental validation (liner thickness only): four machined liners measured on engine; FEA trend confirmed within 10–15%; thin liner (A) somewhat under-predicted.
- Bore-liner relevance: demonstrates design parameters for minimising liner bore distortion; establishes that liner thickness is critical and that FEA methodology with ANSYS is adequate for production design guidance.
