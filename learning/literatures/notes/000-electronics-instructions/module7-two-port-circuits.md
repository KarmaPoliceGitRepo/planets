# Module 7 – Two-Port Circuits

- **Source:** module7 - Two-Port Circuits.pdf
- **Drive link:** https://drive.google.com/file/d/1HgeuPeE58gR2qA8h91YMs7Ny999lp8ii/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (32 pages) systematically presenting the six two-port parameter families (Y, Z, H, G, ABCD, S), their interconversions, use in feedback topology selection, and the Rollett stability factor K for assessing unconditional stability.

## Unique contribution
Unifies all six two-port parameter families in a single reference document with conversion tables, and connects them directly to feedback topology choice (series-series → Z parameters, shunt-shunt → Y parameters, etc.) — a cross-cutting organizing principle that simplifies amplifier analysis.

## Key concepts
- Y-parameters (admittance)
- Z-parameters (impedance)
- H-parameters (hybrid)
- G-parameters (inverse hybrid)
- ABCD parameters (chain/transmission matrix)
- S-parameters
- Feedback topologies
- Loop gain T
- Rollett stability factor K
- Potential instability

## Methods / results / takeaways
- Each parameter family is suited to a specific feedback topology: Y ↔ shunt-shunt, Z ↔ series-series, H ↔ shunt-series, G ↔ series-shunt.
- ABCD matrices cascade by multiplication: useful for analyzing multi-stage networks and transmission line sections.
- Stability: the circuit is unstable if the loop gain T = −1 for any feedback. Root-locus analysis shows poles crossing jω axis.
- Rollett stability factor K = (1 − |S11|² − |S22|² + |Δ|²) / (2|S12S21|), where Δ = S11S22 − S12S21. K > 1 and |Δ| < 1 → unconditionally stable.
- Potentially unstable (K < 1): the device can oscillate for certain source/load impedances; stability circles on Smith Chart define safe operating regions.
- Converting between parameter sets is straightforward using standard tables; most CAD tools perform this automatically.
- Practical concern: devices that are "unconditionally stable" at one frequency may be unstable at another (especially at low frequencies where gain is high).
