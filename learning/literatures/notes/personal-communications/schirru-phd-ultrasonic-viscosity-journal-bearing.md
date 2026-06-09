# Development of an Ultrasonic Sensing Technique to Measure Lubricant Viscosity in Engine Journal Bearing In-Situ

- **Source:** Development of an Ultrasonic Sensing Technique to Measure Lubricant Viscosity in Engine Journal Bearing In-Situ - (2016) Michele Schirru.pdf
- **Drive link:** https://drive.google.com/file/d/1J84B8mMsygY81W7ObQppYVG0CTmSviRF/view?usp=drivesdk
- **Type:** thesis
- **Author/Year:** Michele M. Schirru, 2016 (University of Sheffield, supervisors: Prof. R. Dwyer-Joyce and Dr. M. Marshall)
- **Coverage:** partial (large file, truncated extraction)

## Overview
This PhD thesis develops and validates an ultrasonic technique for in-situ viscosity measurement of lubricating oil inside an operating engine journal bearing. The core idea is to exploit the interaction of shear ultrasonic waves with the solid-liquid boundary: shear waves reflect strongly off a liquid interface in a manner that depends on the liquid's acoustic impedance, which is a function of viscosity. The work spans theoretical modelling (Newtonian and non-Newtonian fluid models), bench-top aluminium-oil experiments, and integration into a motored engine journal bearing rig.

## Unique contribution
Schirru introduces a Maxwell-based viscoelastic ultrasonic model for non-Newtonian fluids that extends the classical Newtonian reflectance approach (equation analogous to a resistance-capacitance circuit). The Maxwell model adds a relaxation-time parameter, capturing the viscoelastic behaviour of real multigrade engine oils at high shear rates and elevated temperatures. The thesis also demonstrates the first in-situ viscosity measurement from a rotating journal bearing during motored engine operation, using a sputtered piezoelectric transducer bonded directly to the shaft.

## Key concepts
- Shear wave reflection at solid-liquid boundary
- Acoustic impedance (shear)
- Newtonian vs. non-Newtonian fluid ultrasonic models
- Maxwell viscoelastic model / relaxation time
- Greenwood model for viscosity
- Journal bearing lubrication / hydrodynamic film
- Stribeck curve
- Viscosity index, viscosity modifiers, base oils
- Piezoelectric transducers (PZT), sputtered thin-film transducers
- Reflection coefficient R; storage and loss moduli G', G''
- STAMINA (standing wave measurement) – related method
- Pulse-echo vs. continuous-wave ultrasonics

## Methods / results / takeaways
- **Ultrasonic principle:** Shear acoustic impedance of a liquid z_L = sqrt(ρ·η·ω) (for Newtonian fluids), so the reflection coefficient R at the solid-liquid interface encodes viscosity η. Measuring R gives η when density ρ and frequency ω are known.
- **Non-Newtonian extension:** The Maxwell model yields a complex shear modulus G* that modifies z_L. When the relaxation time τ → 0, the Newtonian result is recovered. At high τ (high-viscosity multigrade oils at low temperature), the Newtonian model underestimates viscosity; the Maxwell model corrects this.
- **Practical challenge:** R is close to 1 for low-viscosity oils at typical boundaries (e.g., aluminium-oil), making the method relatively insensitive. Matching layers or higher-impedance substrates improve sensitivity.
- **Journal bearing rig:** A sputtered PZT film on the shaft surface allowed real-time viscosity acquisition during bearing rotation. Shear wave signals were extracted via slip rings. Measured oil viscosity was consistent with conventional off-line viscometer readings at the same temperatures.
- **Temperature effect:** Viscosity drops strongly with temperature; the thermocouple calibration of ultrasonic wave speed was necessary to separate thermal from viscosity contributions.
- **Key models compared:** Newtonian (R² = f(η)), Greenwood (includes interfacial microstructure), Maxwell (viscoelastic). For low relaxation times all three agree; divergence appears only for highly non-Newtonian conditions.
