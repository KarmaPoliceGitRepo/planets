# Module 1 – Introduction to Transmission Lines

- **Source:** Module1 - Introduction to transmission lines.pdf
- **Drive link:** https://drive.google.com/file/d/1AloNWg3fc9fU2NCr6Z246MQGya4D6geb/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (56 pages) for UC Berkeley EE 142/242 introducing distributed transmission line theory. Covers the motivation for moving from lumped to distributed circuit models, derivation of the Telegrapher's equations, wave solutions, and reflections at load discontinuities.

## Unique contribution
Provides a first-principles derivation from lumped RLCG ladder models to the wave equation, and introduces the bounce diagram as a time-domain tool for tracking multiple reflections — a perspective not always emphasized in RF texts.

## Key concepts
- Transmission line
- Telegrapher's equations
- Characteristic impedance Z0
- Propagation constant
- Reflection coefficient Γ
- Bounce diagram
- Reactive terminations
- Forward and backward traveling waves
- Distributed circuit model
- Lumped vs. distributed circuits

## Methods / results / takeaways
- A transmission line must be treated as a distributed structure when the line length is a non-negligible fraction of the signal wavelength.
- The lumped-element ladder (R, L, C, G per unit length) leads to the Telegrapher's equations: ∂V/∂z = −(R+jωL)I and ∂I/∂z = −(G+jωC)V.
- Wave solutions are V = V⁺e^{−γz} + V⁻e^{+γz} with propagation constant γ = √[(R+jωL)(G+jωC)].
- Characteristic impedance Z0 = √[(R+jωL)/(G+jωC)]; for lossless lines Z0 = √(L/C).
- Reflection coefficient at load: Γ_L = (Z_L − Z0)/(Z_L + Z0); open circuit Γ=+1, short circuit Γ=−1, matched Γ=0.
- Bounce diagrams track the forward and reflected wave amplitudes at each reflection event in the time domain.
- Reactive terminations (capacitive or inductive loads) produce reflections that depend on frequency, leading to exponential transient waveforms.
