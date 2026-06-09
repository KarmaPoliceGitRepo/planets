# Foundations for Microwave Engineering — Transmission Lines and Waveguides (Chapter 3)

- **Source:** Transmission Lines and Waveguides.pdf
- **Drive link:** https://drive.google.com/file/d/1ea6Xpy-zA0jWC9OAb2MJqeUrIq9qfcJC/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001
- **Coverage:** partial (large file, truncated extraction)

## Overview
Chapter 3 of Collin's Foundations for Microwave Engineering, structured in three parts: (1) distributed-circuit model and wave analysis of transmission lines, (2) field analysis of transmission lines (including microstrip), and (3) rectangular and circular waveguide theory. The most mathematically intensive chapter in the book, covering both the circuit-model and field perspectives.

## Unique contribution
Provides the field-theory justification for the distributed-circuit model, showing how to calculate RLGC parameters from the electromagnetic fields. Covers microstrip's effective permittivity and introduces TE, TM, and TEM wave decomposition of Maxwell's equations for waveguides.

## Key concepts
- Distributed-circuit model (RLGC per unit length)
- TEM, TE, and TM wave types
- Ideal transmission line: V(z) = V+e^(–jβz) + V–e^(jβz)
- Characteristic impedance, propagation constant
- Microstrip line: quasi-TEM, effective permittivity εeff, W/h ratio
- Rectangular waveguide: TEm0 mode family, dominant TE10 mode
- Circular waveguide modes
- Cut-off frequency, group velocity, phase velocity in waveguides
- EM boundary-value problem formulation

## Methods / results / takeaways
- Parts 1, 2, and 3 are largely independent (except §3.7 needed for both 2 and 3), allowing selective study.
- In Part 1 (distributed circuit model), waves on ideal lines are treated without Maxwell's equations — useful for intuition.
- In Part 2 (field analysis), the actual fields solve for RLGC parameters; microstrip requires a quasi-static or full-wave solution.
- TEM waves (transmission lines) have no axial field components; TE waves have no axial E; TM waves have no axial H. Hollow-pipe waveguides cannot support TEM waves.
- Rectangular waveguide TE10 mode: cut-off frequency fc = c/(2a) where a is the wide-wall dimension; below fc the mode is evanescent.
- Phase velocity in a waveguide: vp = c/√(1–(fc/f)²) > c; group velocity vg = c×√(1–(fc/f)²) < c; vp×vg = c².
