# Lumped Circuit Model of Transmission Line and Telegrapher's Equation

- **Source:** TransmissionLineCircuitModel.pdf
- **Drive link:** https://drive.google.com/file/d/1_btAVc6jX05BqNWHJM5ZJiYQBxfK8Ugd/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 10, 2013
- **Coverage:** full

## Overview
Introduces the physical structure of a microstrip transmission line and motivates the lumped distributed-element circuit model (R, L, G, C per unit length). Derives the telegrapher's equations by applying KVL and KCL to a differential segment, then takes the limit as segment length → 0.

## Unique contribution
Provides the physical justification for each circuit element in the transmission-line model: shunt C from the parallel plates, series R from ohmic loss, shunt G from dielectric loss, and series L from current-induced magnetic flux. The derivation explicitly shows how the PDE pairs ∂V/∂x = –RI – L∂I/∂t and ∂I/∂x = –GV – C∂V/∂t arise from the circuit.

## Key concepts
- Microstrip line structure (ground plane, dielectric, signal trace)
- Distributed-circuit model: R (series resistance), L (series inductance), G (shunt conductance), C (shunt capacitance), all per unit length
- KVL on differential segment → ∂V/∂x = –RI – L∂I/∂t
- KCL on differential segment → ∂I/∂x = –GV – C∂V/∂t
- Second-order wave equations for V and I
- Telegrapher's equations in full form

## Methods / results / takeaways
- KVL around the loop of a segment Δx: V(x) – RΔx·I – LΔx·∂I/∂t = V(x+Δx). Dividing by Δx and taking Δx → 0 gives ∂V/∂x = –RI – L∂I/∂t.
- KCL at the shunt node: I(x) – GΔx·V(x+Δx) – CΔx·∂V/∂t = I(x+Δx). In the limit: ∂I/∂x = –GV – C∂V/∂t.
- Cross-differentiating and substituting yields the wave equations: ∂²V/∂x² = LC ∂²V/∂t² + (LG+RC)∂V/∂t + RGV (and the analogous equation for I).
- This model is valid when segment length Δx ≪ λ (quasi-static approximation); it breaks down at very high frequencies where field effects dominate.
