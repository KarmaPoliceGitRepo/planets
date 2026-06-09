# Optimization of Equivalent Circuit Model for Piezoelectric Ultrasonic Transducer

- **Source:** 2018 - Optimization of Equivalent Circuit Model for Piezoelectric Ultrasonic Transducer - Mao.pdf
- **Drive link:** https://drive.google.com/file/d/1naUTzvOy21OYfb-qwkEY-Pa-pXvmoHUn/view
- **Type:** paper
- **Author/Year:** Dan-Dan Zheng, Yang Mao, Ziqiang Cui, Sheng-Hong Lv / 2018
- **Coverage:** full

## Overview
Proposes an optimised equivalent circuit model for PVDF piezoelectric ultrasonic transducers by combining Leach's controlled-source model (which replaces the transformer coupling) with lossy transmission line elements for the electrode and backing layers. The model is implemented in PSpice/OrCAD and validated against pulse-echo experiments on a PVDF transducer at ~8.27 MHz.

## Unique contribution
Extends Leach's controlled-source equivalent circuit (which eliminates the unphysical negative capacitance of Mason/KLM models) by adding explicit lossy transmission line sections for the silver electrode layers and backing. This makes the model structurally complete with no frequency-dependent elements, and gives higher accuracy in predicting centre frequency and bandwidth than either the controlled-source model or KLM model alone.

## Key concepts
- Controlled-source equivalent circuit (Leach 1994) for piezoelectric transducers
- Lossy transmission line model for acoustic propagation layers
- Mason model and KLM model comparison
- PVDF piezoelectric film transducer modelling
- Silver electrode layer effect on centre frequency
- Backing layer acoustic damping
- PSpice/OrCAD circuit simulation
- Pulse-echo validation

## Methods / results / takeaways
- Optimised model structure: controlled-source section (T4 + E1, F1, F2 + C0, C1, R1) for piezoelectric effect + lossy TL sections (T9, T11) for electrode layers + lossy TL section (T13) for backing
- Lossy TL parameters: R=2ραu, L=ρ/A, C=A/ρu², G≈0 (thermal conduction neglected)
- PVDF parameters: e33=0.06 C/m², ε=5, area=3×10⁻⁴ m², thickness=110 μm, u=2000 m/s, ρ=1800 kg/m³
- Experimental centre frequency: 8.27 MHz; KLM and optimised model both give ~8.27 MHz; controlled-source model gives 9 MHz (error from ignoring electrode layers)
- Electrode layer (6 μm silver) reduces centre frequency from theoretical 9 MHz to 8.27 MHz — confirms Brown (2000) observation
- Amplitude agreement: simulation ~2.7 V vs experiment ~2.6 V; faster decay in experiment attributed to adhesive bond layer (not modelled)
- Controlled-source model advantages: no transformer → more flexible analogy circuit choices; no frequency-dependent elements
