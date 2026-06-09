# Module 3 – Scattering Parameters

- **Source:** module3 - Scattering Parameters.pdf
- **Drive link:** https://drive.google.com/file/d/1iq8STcOSYunD405ui3SIjZ1dmmD0Mv6-/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (57 pages) introducing S-parameters as a network description suited to RF/microwave frequencies where voltage and current are difficult to measure directly. Covers S-matrix definition, measurement procedure, conversion to/from Z/Y parameters, signal flow graphs, and Mason's Rule for gain calculation.

## Unique contribution
Provides a complete treatment of signal flow graphs and Mason's Rule alongside S-parameters, enabling closed-form gain expressions for cascaded networks without matrix inversion — a practical tool used extensively in amplifier and system design.

## Key concepts
- Scattering parameters (S-parameters)
- S-matrix
- Incident and reflected wave amplitudes (a, b)
- Port matching condition
- Signal flow graphs (SFG)
- Mason's Rule (non-touching loop rule)
- Transducer gain GT
- Z-to-S parameter conversion
- Two-port network
- Matched termination

## Methods / results / takeaways
- S-parameters defined via traveling wave amplitudes: a_i = (V_i + Z0·I_i)/(2√Z0), b_i = (V_i − Z0·I_i)/(2√Z0).
- S_ij measured by driving port j with a wave and measuring b_i while all other ports are terminated in Z0 (no reflections from other ports).
- S11 = input reflection coefficient; S21 = forward transmission gain; S12 = reverse isolation; S22 = output reflection coefficient.
- Z-to-S conversion: S = (Z/Z0 − I)(Z/Z0 + I)^{−1}.
- Transducer gain: GT = |S21|²(1−|ΓS|²)(1−|ΓL|²)/|(1−S11ΓS)(1−S22ΓL) − S12S21ΓSΓL|².
- Signal flow graphs represent the signal paths in a network graphically; Mason's Rule gives the overall gain as a ratio of path products and loop products.
- Key advantage: S-parameters measured at RF without open/short terminations that would cause instability.
