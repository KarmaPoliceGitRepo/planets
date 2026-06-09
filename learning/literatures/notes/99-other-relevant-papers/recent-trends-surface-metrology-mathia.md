# Recent Trends in Surface Metrology

- **Source:** Recent trends in surface metrology - (2011) TG Mathia.pdf
- **Drive link:** https://drive.google.com/file/d/1epGDlASqwpq6XCP0dMLWkVQYeg-Y4qFz/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** T.G. Mathia, P. Pawlus, M. Wieczorowski / 2011 (published in Wear 271, 494–508)
- **Coverage:** full

## Overview
A comprehensive review article in the journal Wear surveying the state of the art and emerging directions in surface metrology as of 2010–2011. It covers measurement hardware (tactile profilometers, optical interferometers, confocal microscopes, AFM/STM), signal processing (sampling interval selection, Gaussian and robust filtering, wavelet methods), characterisation of structured and multi-process surfaces, and the functional impact of surface texture—especially the role of surface texturing in improving tribological performance of sliding assemblies.

## Unique contribution
This review synthesises contributions from British, German, US, Russian, French, and Polish metrology schools into a single coherent overview, with particular depth on multi-process (plateau-honed) surface characterisation and the emerging application of surface texturing (laser-ablated dimples, oil pockets) to friction and wear control. It also flags non-traditional application domains (bio-engineering, forensics, food science, road/rail, textiles) that rarely appear in focused tribology papers.

## Key concepts
- Surface topography / surface metrology
- Tactile profilometer / stylus profilometer
- Optical profilometry (PSI, VSI, EVSI, white-light interferometry)
- Confocal microscopy
- AFM / STM / SPM
- Sampling interval / Nyquist frequency / aliasing
- Gaussian filter / robust Gaussian filter / spline filter
- Wavelet transform / multi-scale analysis
- Structured surfaces / engineered surfaces
- Multi-process texture / plateau-honed surfaces
- Abbott-Firestone curve / material ratio curve
- Rk / Rpk / Rvk / Mr1 / Mr2 parameters (ISO 13565-2)
- Rpq / Rvq / Rmq parameters (ISO 13565-3)
- Surface texturing / laser surface texturing
- Dimples / oil pockets / micro-hydrodynamic bearings
- Tribology / friction / wear / lubrication
- Cylinder liner honing

## Methods / results / takeaways
**Measurement techniques:**
- Contact (stylus) remains dominant in industry; intelligent probes with AM communication and memory chips reduce operator error.
- White-light interferometry (VSI) offers nm-range vertical resolution over >1 mm range; combined with microscopy objectives it becomes an "optical profilometer."
- Confocal microscopes achieve excellent lateral resolution but struggle with steep slopes (>90°) and transparent/semitransparent layers.
- AFM resolves sub-nm features on any material; STM is limited to conductors.

**Sampling and filtering:**
- Optimal sampling interval: 80% of cumulative spectral power should fall below 1/3 of Nyquist frequency (Mainsah criterion), with minimum spacing set by probe tip radius.
- Standard Gaussian filter (ISO 11562) introduces edge artefacts (running-in/out lengths); Gaussian regression filters and spline filters eliminate these but add computation cost.
- Robust Gaussian filters (Tukey, Hampel, Andrews weight functions) prevent freak values (scratches, deep grooves) from distorting the mean line—essential for multi-process textures.
- Wavelet transforms enable multi-scale decomposition, separating manufacturing signatures at different length scales.

**Multi-process surfaces:**
- Plateau-honed cylinder liners are the canonical example: smooth plateaux (load-bearing) plus deep valleys (oil reservoir/debris trap).
- ISO 13565-2 (Rk family: Rk, Rpk, Rvk, Mr1, Mr2) is standard in European industry; ISO 13565-3 (Rq family: Rpq, Rvq, Rmq) is more tightly correlated with honing process variables (stone grit, pressure, time).
- Key practical finding: Rk and Rvk decrease with increasing plateau honing time t and decrease with increasing coarse honing pressure p_v; Mr2 and Rmq increase.

**Surface texturing:**
- Dimple/pocket textures (machined, laser-ablated, etched) serve as micro-hydrodynamic bearings, lubricant reservoirs, and debris traps.
- Laser surface texturing (LST) enables precise dimple geometry control; partial texturing of piston rings (Etsion group) reduces friction and improves fuel efficiency.
- Dimple density, shape, and distribution all affect the Stribeck curve—optimum parameters are application-specific and not yet fully defined.

**Other applications noted:** biomedical implants (titanium surface roughness affects osseointegration), forensic ballistics (3D topography for firearm identification), food science (chocolate colour/gloss vs. topography), road texture.
