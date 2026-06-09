# Bore Analysis Tool (BAT) — Cylinder Bore Shape Analysis and Ring Conformability

- **Source:** Lotus Engineering Internal Report, 16 May 2001
- **Drive link:** https://drive.google.com/file/d/1DJxGJRPt4-2_ZKLTMR0GxeawNMgIWlCj/view
- **Type:** report
- **Author/Year:** Gibbs, Paul (Lotus Engineering) / 2001
- **Coverage:** full

## Overview
Internal Lotus Engineering report describing the Bore Analysis Tool (BAT), an Excel-based software tool for analysing cylinder bore shape data from Taylor-Hobson Talyrond instruments (2000-point text file input per measurement plane). BAT applies Gaussian filtering (ISO 11562) to remove high-frequency noise, then performs FFT-based harmonic decomposition (up to order 50) to extract Fourier coefficients at multiple axial depths. Tool implements Tomanik's ring conformability criterion to determine whether a piston ring can conform to each measured bore shape, and iterates on predicted ring shape to find equilibrium. Calculates gap areas (open-ring sealing gaps) and percentage sealing. Outputs: polar cross-section plots per plane, 3D bore shape visualisation, magnitude vs depth plots per harmonic order, % sealing vs depth, ring gap area distributions.

## Unique contribution
Complete description of an industrial software pipeline from raw Talyrond data to actionable ring conformability and sealing percentage outputs; documents Tomanik conformability formula and threshold implementation in production use; iterative ring shape prediction is a rare explicit documentation of how ring equilibrium shape is computed from bore input; gap area and % sealing outputs provide direct ring-pack performance metrics not available from distortion magnitudes alone.

## Key concepts
- Taylor-Hobson Talyrond text file: 2000 circumferential data points per axial plane; radius vs angle
- Gaussian filter (ISO 11562): low-pass filter applied to remove measurement noise while preserving form harmonics
- FFT harmonic decomposition: up to order 50; magnitudes and phases extracted per plane; lower orders (1–8) most relevant to ring conformability
- Tomanik conformability formula: Umax = 10(i·k·r² − 1); where i = ring free shape parameter, k = bore harmonic amplitude, r = bore radius; % sealing = 113 − ub/Umax where ub = bore harmonic amplitude
- GOETZE / Dunaevsky conformability bounds also referenced for comparison
- Iterative ring shape prediction: ring free-shape adjusted iteratively until equilibrium with bore shape achieved; accounts for ring tension redistribution
- Gap area calculation: integrates radial gap between ring and bore where ring cannot conform; total gap area is indicator of blow-by and oil consumption risk
- % sealing vs depth: fraction of circumference in contact at each axial measurement plane; key design quality metric
- Bore twist: axial variation of harmonic phase angle; BAT calculates twist per order from phase vs depth data
- Outputs: radial cross-section polar plots, 3D bore shape, magnitude vs depth (per order), % sealing vs depth, ring gap areas
- Fourier order interpretation: 0 = diameter; 1 = eccentricity; 2 = oval; 3 = three-lobe; 4 = cloverleaf; consistent with Maassen/GOETZE conventions

## Methods / results / takeaways
- Input pipeline: Talyrond text → Gaussian filter → FFT → harmonic coefficients at multiple axial depths.
- Conformability check: each harmonic order tested individually against Tomanik bound; orders exceeding Umax indicate non-conformance at that depth.
- Iterative ring equilibrium: free ring shape (elliptical profile parameters) adjusted until ring contact pressure distribution with the bore shape is self-consistent; converges typically within a few iterations.
- Gap area metric: total open gap per plane integrated over circumference; correlated to blow-by and LOC.
- % sealing: primary output for go/no-go bore quality assessment; values below ~90% typically indicate ring conformability concern.
- Bore twist: extracted from phase vs axial position; non-zero twist indicates systematic machining bias or asymmetric thermal distortion; BAT documents twist magnitude and direction.
- Bore-liner relevance: provides the complete data-processing and ring-conformability chain for bore shape analysis, from raw measurement to engineering decision; Tomanik criterion is the adopted conformability metric; iterative ring shape prediction enables more accurate sealing % than direct analytical formulae alone.
