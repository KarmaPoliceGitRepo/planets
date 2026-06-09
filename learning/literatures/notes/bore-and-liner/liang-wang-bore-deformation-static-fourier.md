# Investigation on Cylinder Bore Deformation under Static Condition Based on Fourier Decomposition

- **Source:** SAE Technical Paper 2017-01-0366
- **Drive link:** https://drive.google.com/file/d/1Ez_N_yrJ-2w0tu7j2ru6xNjcRM8878u9/view
- **Type:** paper
- **Author/Year:** Liang, Wang (State Key Lab of Engines Tianjin), Huang, Yang (China North Engine Research Institute), Tang, Cui (Tianjin University) / 2017 (SAE 2017-01-0366)
- **Coverage:** full

## Overview
FEA study (Hypermesh + FEA solver) of static cylinder bore deformation under head bolt preload for a V6 engine (132 mm bore) with Matlab Fourier decomposition. Investigates effects of preload magnitude (80–160 kN), bolt distribution (spacing and number), bolt length (40–80 mm), and first-thread location. Validates against V-INCOMETER measurements. Finds that 2nd and 4th order Fourier terms dominate; orders above 8th are negligible.

## Unique contribution
Systematic Fourier decomposition analysis of static bore distortion demonstrating that: (1) 2nd and 4th orders dominate static bolt-induced distortion; (2) longer bolts and lower first-thread position reduce distortion by distributing load over greater depth; (3) more uniform symmetric bolt distribution consistently reduces distortion; (4) static distortion (up to 30 µm) is large enough to significantly affect dynamic distortion and cannot be neglected.

## Key concepts
- Static cylinder bore deformation; head bolt preload; V6 engine (132 mm bore)
- Fourier decomposition orders 0–8; 2nd and 4th order dominant; orders >8 negligible
- Bolt preload magnitude (80–160 kN); bolt length effect; first-thread depth effect
- Bolt distribution symmetry; number of bolts; bearing load concentration
- FEA: Hypermesh mesh, ~3M tetrahedral elements, 4mm max / 1mm at contact; FE solver
- V-INCOMETER experimental validation
- Matlab program for Fourier decomposition of nodal radial displacements

## Methods / results / takeaways
- FEA model: V6 engine block + head + liner + gasket; tetrahedral elements; contact pairs between all mating surfaces; fixed at 4 corner nodes of block bottom; bolt preload as 1D element force.
- Validation: displacement patterns match V-INCOMETER measurements qualitatively and quantitatively for baseline case.
- Fourier decomposition: radial deviation around circumference decomposed into orders 0–8; 2nd and 4th orders dominate for all bolt configurations studied.
- Preload magnitude: increasing preload (80→160 kN) increases distortion nearly proportionally; largest single increment at lower preloads; 200% preload gives 48% more distortion.
- Bolt distribution: symmetric, uniform distribution (a1=b1) gives lower distortion than asymmetric (a≠b); 8-bolt uniform produces less fluctuation than 4-bolt uniform at same total load.
- Bolt length: longer bolts (40→80 mm) reduce bore deformation by distributing load over greater thread engagement depth, avoiding force concentration at top of block.
- First-thread location: lower position (40 mm from deck) → less distortion than flush (0 mm); deformation mainly in upper half of liner.
- Maximum static distortion ~30 µm; considered significant input to total dynamic distortion.
- Bore-liner relevance: establishes that bolt-induced static distortion is primarily 2nd and 4th order and provides bolt design guidelines to minimise it; foundation for dynamic distortion analysis.
