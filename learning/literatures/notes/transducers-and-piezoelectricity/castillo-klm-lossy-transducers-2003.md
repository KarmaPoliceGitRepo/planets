# KLM Model for Lossy Piezoelectric Transducers

- **Source:** 2003 - KLM model for lossy piezoelectric transducers - Castillo.pdf
- **Drive link:** https://drive.google.com/file/d/1jvkI23mwqCLJ1g6aC069ueXcpWhqgK6q/view
- **Type:** paper
- **Author/Year:** Martha Castillo, Pedro Acevedo, Eduardo Moreno / 2003
- **Coverage:** full

## Overview
Extends the KLM transfer matrix model to include mechanical, dielectric, and piezoelectric losses in the transducer elements by introducing complex-valued material parameters. Implements the model using MAPLE for matrix calculations and LabWindows/C for a user interface. Validates against three transducers: one PZT-4 (negligible losses) and two PVDF (significant losses), comparing measured and simulated time-domain pulse-echo waveforms.

## Unique contribution
Shows that for PVDF transducers (high dielectric and mechanical loss tangents), losses must be explicitly included in the KLM model to correctly predict pulse duration and Q-factor. Demonstrates that dielectric losses have more influence on waveform shape than mechanical losses for PVDF, and that the backing impedance being higher than the PVDF impedance masks loss effects and shifts the resonance frequency downward. Provides the complete matrix formulation for the lossy KLM model.

## Key concepts
- KLM model with complex material parameters (lossy transducers)
- Mechanical loss tangent tan(δ_mec)
- Dielectric loss tangent tan(δ_elec)
- Complex Laplace variable p = jω + α/(2l) for mechanical losses
- Complex ε^S for dielectric losses in matrix N2 (C₀ only, not C', W)
- Transfer matrix cascade: N_e, N_m, N_f, N_1...N_8
- PVDF transducer modelling
- PZT-4 vs PVDF loss comparison

## Methods / results / takeaways
- Three transducers: A = PZT-4 (tan δ_mec=0.004, tan δ_elec=0.003), B = PVDF with low backing Z_b=2.58 MRayl, C = PVDF with high backing Z_b=5.2 MRayl
- Transducer A: losses negligible — measured and simulated waveforms agree without loss terms; large Q due to low backing impedance (2.58 MRayl vs ceramic 34.53 MRayl)
- Transducer B: dielectric losses (tan δ_elec=0.15) affect waveform more than mechanical losses (tan δ_mec=0.05); waveform requires both to match measured shape
- Transducer C: high backing impedance (5.2 MRayl > PVDF Z=4.51 MRayl) → backing acoustic Q dominates, masking internal losses; centre frequency shifts down
- Key implementation rule: complex ε^S used only in C₀ (matrix N2), NOT in C' or electromechanical coupling factor W — otherwise erroneous results
- Mechanical loss: introduced as p = jω + αl/2 in piezoelectric transmission line matrices (N5, N6); not applied to matching layers
- Software: MAPLE V4 for analytical matrix computation; LabWindows for virtual instrumentation interface; MATLAB for post-processing
