# CAE Simulations for Engine Block Bore Distortion

- **Source:** SAE Technical Paper 2012-01-1320 (April 2012), DOI: 10.4271/2012-01-1320
- **Drive link:** https://drive.google.com/file/d/1y2n1pHxymvQa02JzMQngYcK9a_4H5eCL/view
- **Type:** paper
- **Author/Year:** Ghasemi, Amir / 2012 (SAE 2012-01-1320)
- **Coverage:** full

## Overview
Methodology paper presenting a complete CFD → thermal FEA → structural FEA bore distortion workflow for engine block bore distortion analysis. MATLAB post-processor computes roundness, eccentricity, cylindricity, solid-rod parameter, and Fourier harmonic orders (0–4) from FEA nodal displacements. Includes correction for manufacturing (machining/honing) via subtraction of assembly-step distortion. Validated against PAT Incometer (Goetze measurement system) with 5–10% agreement. Confirms that 2nd and 4th orders dominate for 4-bolt gasoline engines; 6th order would be primary for 6-bolt heavy-duty diesel engines.

## Unique contribution
Complete practical CAE workflow including the manufacturing correction step (Umachining subtracted from thermal and firing distortions); defines and calculates roundness, eccentricity, cylindricity, AND solid-rod parameter from the same FEA displacement dataset; explains physical connection between bolt pattern and dominant Fourier order.

## Key concepts
- Bore distortion sources: assembly bolt clamping, thermal operating loads, combustion firing pressure, manufacturing tolerances
- Piston-liner friction: ~23% of total engine friction; bore distortion creates non-conformity → higher oil consumption, blow-by, wear
- Fourier decomposition: 0th = diameter change; 1st = eccentricity; 2nd = oval; 3rd = 3-lobe; 4th = cloverleaf (4-bolt engines)
- 4-bolt pattern → 4th order dominant; 6-bolt heavy diesel → 6th order; symmetric placement key
- Cylindricity calculation: interpolated center line between top and bottom LSC; max Rmax − min Rmin over all levels
- Solid rod: maximum diameter of circular rod fitting inside distorted bore (prevents bearing seizure)
- Manufacturing correction: honing/boring removes assembly-step distortion; corrected thermal distortion = FEA(thermal) − FEA(assembly)
- CFD provides heat transfer coefficients; boiling correction applied above 125°C wall temperature
- MLS gasket design: non-stopper for stiff head / lower combustion pressure; stopper MLS for higher combustion pressure (but increases bore distortion through stopper)
- FEA loading sequence: room temperature assembly → thermal (max operating) → combustion pressure → cold soak (−20°F) → return to room temperature
- PAT Incometer used for experimental validation; 5–10% discrepancy between FEA and test

## Methods / results / takeaways
- MATLAB code extracts FEA nodal displacements, calculates least-squares circle per level, applies Fourier analysis to give harmonic coefficients.
- Dominant orders in 4-bolt gasoline engine: 2nd and 4th; 0th and 1st have little conformability significance (just diameter change and eccentricity).
- Bore distortion shown for hot clamping condition at multiple axial levels; bore 2 results provided for 2nd, 3rd, 4th order Fourier harmonics.
- Table 1: FEA vs Incometer comparison for assembly condition; 5–10% agreement.
- Four-bolt pattern creates 4-lobe (cloverleaf) distortion; bolt-boss depth and bolt length are key design levers.
- Loading sequence includes cold soak (min bolt load from thermal contraction) to verify sealing pressure retained throughout life.
- Gasket choice: stopper MLS → higher combustion sealing but increases bore distortion; active MLS → lower bore distortion but harder to generate high sealing stress.
- Bore-liner relevance: provides practical methodology for bore distortion prediction including manufacturing correction; explains bolt-pattern → Fourier order relationship; PAT Incometer validation confirms FEA accuracy suitable for design guidance.
