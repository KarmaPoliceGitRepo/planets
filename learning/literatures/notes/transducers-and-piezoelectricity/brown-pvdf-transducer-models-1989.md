# Ultrasound Transducer Models for Piezoelectric Polymer Films

- **Source:** 1989 - Ultrasound transducer models for piezoelectric polymer films- Lewis F Brown.pdf
- **Drive link:** https://drive.google.com/file/d/1SHnjMEtRNYhIrCj6GpTWFM4ppfEUusBf/view
- **Type:** paper
- **Author/Year:** Lewis F. Brown, David L. Carlson / 1989
- **Coverage:** full

## Overview
Develops a five-step algorithm for determining the frequency-dependent piezoelectric and dielectric constants of PVDF and P(VDF-TrFE) films from air-loaded broadband impedance measurements. Incorporates these constants into a modified Mason's model with loss elements to accurately simulate both electrical input impedance and pulse-echo ultrasonic performance.

## Unique contribution
First systematic procedure for extracting complex material constants from low-Q piezoelectric polymers that accounts for their frequency-dependent dielectric permittivity and mechanical loss. Introduces a modified Mason's model with an explicit dielectric loss resistance Rd and a mechanical loss resistance Rm, validated against actual pulse-echo measurements of P(VDF-TrFE) probes.

## Key concepts
- PVDF and P(VDF-TrFE) material constants
- Complex dielectric constant and loss tangent
- Modified Mason's equivalent circuit for lossy piezoelectric polymers
- Frequency-dependent dielectric loss resistance
- Mechanical Q (low Q challenge for polymers)
- Five-step algorithm for polymer characterisation
- Electromechanical coupling coefficient kt
- Air-loaded impedance measurement

## Methods / results / takeaways
- Approach: measure broadband impedance (0.5–32 MHz) with HP4815A RF impedance meter on air-backed films; compute ε33 and tan δe at off-resonance frequencies; interpolate through resonance region
- Modified Mason's model: Rd = 1/(ωC0 tan δe) in shunt with C0; Rm added to mechanical branch to account for high mechanical loss of polymers
- Five-step algorithm: (1) determine fp from max imaginary admittance; (2) compute C0 and d from slope of reactance; (3) R determines mechanical Q; (4) compare with theoretical Rm; (5) set kt
- For 52-µm PVDF: Qm = 11.6, kt = 14.6% — confirmed against manufacturer specs
- Model deviates <1% from measured impedance over 0.5–32 MHz
- P(VDF-TrFE) pulse-echo waveforms from fused silica target: excellent agreement between model-predicted and measured waveforms
- Key: must account for cable capacitance, receiver gain, and receiver damping to get accurate pulse predictions
