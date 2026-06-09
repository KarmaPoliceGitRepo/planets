# Module 10 – Physical Origin of Electrical Noise

- **Source:** module10 - Physical Origin of Electrical Noise.pdf
- **Drive link:** https://drive.google.com/file/d/1O3p0Zie-ekU3Q6trjS54XAt2vw8IqSB9/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (25 pages) covering the fundamental physical origins of noise in resistors, BJTs, and FETs — including thermal (Johnson-Nyquist) noise, shot noise, and flicker (1/f) noise — with derivations grounded in statistical mechanics and equipartition theory.

## Unique contribution
Derives Johnson-Nyquist thermal noise from first principles via the equipartition theorem and transmission line model, then extends systematically to shot noise in BJTs and channel noise in MOSFETs, providing the physical underpinning for the equivalent noise source models used in Modules 11–12.

## Key concepts
- Thermal noise (Johnson-Nyquist noise)
- Shot noise
- Flicker noise (1/f noise)
- Equipartition theorem
- Noise spectral density
- BJT noise sources (base and collector shot noise)
- FET channel thermal noise
- Gate-induced noise
- White noise
- Noise power spectral density

## Methods / results / takeaways
- Thermal noise in resistor R: vn² = 4kTRΔf (voltage source) or in² = 4kT/R·Δf (current source); derivation from equipartition (½kT energy per mode).
- Shot noise from DC current IDC: id² = 2qIDC·Δf; arises from discrete, independent carrier crossings of a potential barrier.
- BJT: collector shot noise ic² = 2qIC·Δf; base shot noise ib² = 2qIB·Δf; at low frequency base current noise dominates input NF.
- FET channel thermal noise: id² = 4kTγgds0·Δf where γ = 2/3 for long-channel MOSFET in saturation, gds0 = drain-source conductance at VDS=0.
- Gate-induced noise (correlated): ig² = 4kTδgg·Δf; partially correlated with channel noise via coefficient c ≈ j0.395.
- Flicker (1/f) noise: id² = KF·ID^AF/f·Δf; dominant below the 1/f corner frequency (kHz to MHz range for MOSFETs).
- Noise temperature Tn = T(F−1) provides an equivalent physical temperature interpretation of noise figure.
