# Engine Cambore Distortion Analysis From Design to Manufacturing

- **Source:** SAE Technical Paper 2004-01-1449
- **Drive link:** https://drive.google.com/file/d/1YXYnifsr5WuK0vtyyvM_jr7Se69pLTQK/view
- **Type:** paper
- **Author/Year:** Liu, Winship (Ricardo), Ho, Hsia, Wehrly, Resh (DaimlerChrysler) / 2004 (SAE 2004-01-1449)
- **Coverage:** full

## Overview
Presents a methodology for cambore (camshaft bore) distortion analysis linking FEA of assembly bolt loads to manufacturing "head crushing" process optimisation. Fourier harmonic decomposition (orders 0–4) is used to quantify distortion. A custom MatLab post-processing code extracts bore surface displacements from ABAQUS results to compute roundness, eccentricity, cylindricity, and harmonic orders. Validated against test data; two crushing load cases compared.

## Unique contribution
Demonstrates a complete design-to-manufacturing feedback loop for cambore: FEA predicts distortion from cold clamping (57 kN/bolt, 8 bolts) → manufacturing crushing loads selected to pre-distort the bore such that post-bolt assembly distortion is minimised. Finds that a 50 kN crushing load (Crushing Case 2) matches cold-clamping distortion to within tolerances.

## Key concepts
- Cambore distortion; camshaft seizure risk; cylinder head boring
- Fourier harmonic decomposition (orders 0–4): eccentricity, ovality, three-lobe, four-lobe
- Roundness; cylindricity; least-square circle; Fourier coefficients via FFT
- Head crushing (pre-distortion machining); manufacturing process planning
- ABAQUS/Standard; custom MatLab bore distortion code
- Head bolt clamping load; gasket nonlinearity (excluded from this study)
- Computer integrated manufacturing (CIM)

## Methods / results / takeaways
- Mathematical model: dR = Σ(Ai cos(iθ) + Bi sin(iθ)) for i = 0–4; magnitude = √(Ai² + Bi²); angle = atan(Bi/Ai).
- FEA: quarter model (2 half-cylinders + 1 full cylinder); linear analysis (no gasket); ABAQUS/Standard; 57 kN/bolt cold clamping.
- Cold clamping distortion: cylindricity 120–150 µm; roundness 60–80 µm (across 4 cambores).
- FEA model validated against modal test: mass ±1.3%, torsion frequency +1%, vertical bending −0.6%.
- Crushing Case 1 (10 kN/bolt, head upside down): cylindricity 50–60 µm; roundness 20–30 µm — insufficient to compensate assembly distortion.
- Crushing Case 2 (45–50 kN/bolt, head bolted to block, crushing from top): cylindricity 110–145 µm; roundness 50–75 µm at 50 kN — matches cold clamping case closely.
- Conclusion: 50 kN head crushing load (matching bolt assembly load) is required to pre-compensate assembly distortion in manufacturing.
- Relevance: bore distortion analysis methodology (Fourier decomposition + MatLab post-processing of ABAQUS results) is the same framework used for cylinder bore distortion in piston ring conformability studies.
