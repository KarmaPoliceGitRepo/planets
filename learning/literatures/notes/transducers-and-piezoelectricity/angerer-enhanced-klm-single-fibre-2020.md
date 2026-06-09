# Enhanced KLM Model for Single-Fibre Piezocomposite Transducers

- **Source:** 2020 - Enhanced KLM Model for Single-Fibre Piezocomposite Transducers - Angerer.pdf
- **Drive link:** https://drive.google.com/file/d/1bbm9OZ5NPsgAwM-fTMd8jvs4kEsX4e-7/view
- **Type:** paper (conference, IEEE)
- **Author/Year:** Martin Angerer, Michael Zapf, Sylvia Gebhardt, Holger Neubert, Nicole V. Ruiter / 2020
- **Coverage:** full

## Overview
Extends the standard 1D KLM transducer model to a 2-spatial-dimension (2-SD) model by adding a coupled lateral transmission line in series with the axial (thickness mode) resonator, to account for both axial and planar (lateral) vibration modes in single-fibre PZT piezocomposite transducer discs (PTDs) for 3D ultrasound computer tomography (USCT). Uses a 4D brute-force parameter optimisation to find the best-fit model parameters, achieving 90.3% fit between simulated and measured electromechanical (EM) impedance.

## Unique contribution
First demonstration that a low-complexity 2-SD KLM extension (one additional transmission line + transformer for the planar mode) can capture both dominant vibration modes of a short-fibre piezocomposite (aspect ratio ~4:3), which the standard 1-SD KLM model cannot predict at frequencies above 3 MHz. Shows that data-sheet material parameters are insufficient for piezocomposite modelling — brute-force optimisation over 4 parameters is necessary, and the required parameter adjustments are physically interpretable.

## Key concepts
- KLM model extension for 2 spatial dimensions (2-SD model)
- Single-fibre piezocomposite transducer (PZT fibres in epoxy)
- Axial (thickness) and planar (lateral) vibration modes
- Electromechanical impedance prediction and fitting
- Brute-force 4D parameter optimisation
- k33, k31, sE33, backing impedance ZB as optimisation parameters
- Polysulfone-spun PZT fibres (Sonox P505, CeramTec)
- 3D USCT (ultrasound computer tomography) application

## Methods / results / takeaways
- 2-SD model adds a transformer Φ31(ω) coupled to a lateral transmission line of length = fibre radius, terminated with epoxy impedance ZL on both ends; integrated as a two-port series with 1-SD axial resonator
- Planar transformer ratio: Φ31(ω) = k31 × (r/2r)/(vsC0Z0)^½ × sinc(ω/2ωp)
- 4D brute-force search: 64 increments per parameter (total 64⁴ = 16.8M evaluations), fit metric = geometric mean of magnitude and phase fit, computation: 2.43 hours on desktop PC
- Best-fit parameters vs data-sheet: sE33 +11.8% (lower stiffness), k33 −9.9%, k31 −70.9%, ZB +84.5%
- Changes are physically interpretable: k33 reduction expected at low aspect ratio; high ZB due to epoxy embedding constraint; low k31 due to geometry boundary mismatch
- Final fit = 90.3%; remaining deviations above 3 MHz attributed to complex lateral mode resonance patterns in second-generation PTD (thinner disc)
- Enables individual assembly-step monitoring during manufacturing by comparing KLM predictions to impedance measurements
