# An Easily Constructed, Broad Bandwidth Ultrasonic Probe for Research Purposes

- **Source:** Bainton Hillier Silk PVDF probe 1981
- **Drive link:** https://drive.google.com/file/d/1RNU7AE-pXfQ6OxsqieQ2TuXkfjoHwq_x/view
- **Type:** paper (Journal of Physics E: Scientific Instruments 14, 1313–1319, 1981)
- **Author/Year:** K. F. Bainton, M. J. Hillier, M. G. Silk / 1981
- **Coverage:** full

## Overview
Describes construction and KLM-based design of a simple PVDF pulse-echo probe: PVDF film (30 μm) sandwiched between a Perspex absorbing backing and a polystyrene probe shoe (stand-off delay line). Uses KLM model to predict insertion loss, pulse shape, and frequency spectrum as functions of PVDF acoustic impedance (two published values: 2.88 vs 4.14 MRayl) and bond line thickness (1.5–24 μm). Builds ~20 probes and shows ±1 dB reproducibility; bandwidth 2–15 MHz.

## Unique contribution
Demonstrates that a simple PVDF film probe with polystyrene shoe has highly reproducible pulse shape (±1 dB over 20 probes) because pulse characteristics are governed primarily by absorption in the polystyrene shoe rather than by bond line variability — provided bond lines remain below ~10 μm. Shows that replacing aluminum electrode films with evaporated gold allows 400 V drive without damage. PVDF probe is 15 dB less sensitive than PZT probe but generates compact pulse; discrepancy from theory (~4 dB predicted) attributed to overestimated PVDF coupling coefficient.

## Key concepts
- PVDF acoustic impedance: 2.88 MRayl (c = 1600 m/s) vs 4.14 MRayl (c = 2300 m/s) — two published values
- Probe design: Perspex backing (3.16 MRayl) | PVDF (30 μm) | polystyrene shoe (2.48 MRayl) | water/target
- Bond line: Araclor 1260, Z ≈ 1.65 MRayl; thickness <10 μm for minimal effect on pulse shape
- Bond line effect: >12 μm → frequency shift; 24 μm → split frequency bands; <6 μm → negligible change
- KLM model: used to predict all parameters; probe shoe absorption is dominant shaping mechanism
- Sensitivity loss: PVDF probe 15 dB below PZT; theory predicts only 4 dB below (remainder: coupling coefficient overestimate + polystyrene absorption)
- Al electrode damage: aluminum films damaged at >100 V drive; gold film replacement allows 400 V
- Al/Araldite backing: could be used for impedance matching to PVDF; Al/Araldite reaches PVDF match at low Al concentration

## Methods / results / takeaways
- PVDF films: 9 μm and 30 μm commercial pre-polarised; both produce identical pulse shape
- Araclor 1260 bond; Perspex backing; polystyrene shoe (two lengths tested: 19 mm and 6 mm)
- 20 nominally identical probes: amplitude variation ±1 dB; pulse shape consistent
- Polystyrene shoe absorbs high frequencies (>15 MHz); sets upper frequency cutoff
- Focused probe: machined curved end of polystyrene delay line; demonstrates defect detection in steel plate
- 25 μm PVDF from alternative supplier (polarised under 2D tension): 8–10 dB more sensitive; brings theory/experiment agreement
- Discrepancy resolution: actual kt lower than nominal → revised calculation matches observed sensitivity
- Application: NDT research, thickness gauging, defect detection; practical off-the-shelf PVDF transducer design
