# High Strain Survivability of Piezoceramics by Optimal Bonding Adhesive Design

- **Source:** 2018 High Strain Survivability of Piezoceramics (Sensors 2018, 18, 2554)
- **Drive link:** https://drive.google.com/file/d/1sC0mNcI5onTf_eSfsmgQldN8_QvNC1Ex/view
- **Type:** paper
- **Author/Year:** Sun, Wang, Qing, Wu / 2018 (Sensors 18(8), 2554; Xiamen University / Dalian University of Technology)
- **Coverage:** full

## Overview
Investigates how adhesive layer properties (shear modulus and thickness) affect strain transfer from a host structure to a bonded PZT piezoceramic sensor, with the goal of increasing PZT survivability at high tensile strain levels. Develops a 1D analytical shear-lag model, validates with 3D FEA (Abaqus), and experimentally demonstrates that properly optimised adhesive allows PZT sensors to survive host strains up to 4000 µε (well above the PZT elongation limit of ~1100 µε).

## Unique contribution
Demonstrates for the first time that increasing adhesive thickness and reducing adhesive shear modulus can reduce strain transfer coefficient by >44% (theory) / 36% (FEA), enabling PZT sensors to remain operational at host strains 3–4× their failure limit. Derives explicit strain transfer coefficient formula as a function of shear lag parameter.

## Key concepts
- PZT piezoceramic sensor; strain survivability; SHM
- Shear lag effect; adhesive layer; strain transfer coefficient
- Electromechanical impedance (EMI) for SHM damage detection
- APC851 PZT material; Hysol EA9395/9396 adhesive
- Crawley uniform strain model
- Guided wave SHM; Lamb waves
- PZT d31-type piezoelectric effect

## Methods / results / takeaways
- 1D analytical model (Crawley basis): strain transfer coefficient Tε = [ψ/(ψ+α)] × [1 - cosh(rx)/cosh(rl)], where r² = (Ga/ha)(1 + α/ψ)/Ep·hp; ψ = Eb·hb/Ep·hp.
- Strain transfer coefficient increases with adhesive shear modulus, decreases with adhesive thickness; scales with Ga/ha ratio.
- Theory: max Tε = 89.4% (Ga=2000 MPa, ha=25 µm) → min 45.3% (Ga=500 MPa, ha=175 µm). 44.1% reduction achievable.
- FEA (circular PZT disk, 6mm dia, 0.25mm thick): max strain at PZT center; 36.4% reduction achievable.
- Experiment: Hysol EA9395 (Ga=1900 MPa) at 25 µm thickness → PZT fails above 2000 µε; same adhesive at 125 µm thickness → PZT survives up to 4000 µε.
- Lower modulus Hysol EA9396 (Ga=1050 MPa) also maintains survivability at 4000 µε.
- Conclusion: optimal adhesive = lower shear modulus + greater thickness; alternatively replacing PZT center material with a high-elongation material of similar modulus reduces strain concentration.
- Note: peripherally relevant to bore-liner topic as PZT sensors are used for ultrasonic OFT measurement in engine bore applications (e.g., mills-avan studies). Strain survivability directly limits where PZT sensors can be bonded on engine structures.
