# Design of Ultrasonic Transducers with Multiple Acoustic Matching Layers for Medical Application

- **Source:** 1987 - Design of ultrasonic transducers with multiple acoustic matching layers - Inoue.pdf
- **Drive link:** https://drive.google.com/file/d/10ZYw79SVUC8_99iua9EdfSaTl8aA1PhP/view
- **Type:** paper
- **Author/Year:** Takeshi Inoue, Masaya Ohta, Sadayuki Takahashi / 1987
- **Coverage:** full

## Overview
Presents a transducer design method for multiple acoustic matching layers based on multiple-mode filter synthesis theory. Shows that a transducer with n matching layers acts as an (n+1)-mode resonator. Uses iterative optimisation to find the characteristic impedances and thicknesses of matching layers (single to fivefold) that minimise insertion loss and ripple. Validates with a PbTiO₃ disk transducer with triple matching layers achieving 88% fractional bandwidth at −6 dB with 3.2 dB round-trip insertion loss, and a 3.5 MHz triple matching layer linear array probe.

## Unique contribution
First synthesis-based design theory for transducers with more than two matching layers, exploiting the structural analogy between the transducer system and multiple-mode resonator filter theory. Establishes that selecting z₁ (first layer impedance) too large causes sharp cutoff with passband ripple — a key practical guideline. Shows how design values evolve from single to fivefold layers and confirms that bandwidth increases diminish beyond triple layers.

## Key concepts
- Multiple acoustic matching layers (1–5 layers)
- Multiple-mode filter synthesis theory
- Inverse-L type circuit representation of transducer
- Image impedance Z_02 design criterion
- Mason equivalent circuit for piezoelectric layer
- PbTiO₃ ceramic (k_t=0.53, Z₀=34.9 MRayl)
- Triple matching layer design (z₁=14.2, z₂=4.1, z₃=1.9 MRayl at α_h=1.18)
- -6 dB fractional bandwidth vs number of matching layers
- Round-trip insertion loss (RTIL)

## Methods / results / takeaways
- Resonance mode structure: n matching layers → (n+1)-fold mode resonator; phases of odd/even resonances differ by π
- Design table (PbTiO₃ to water): single (z₁=4.5 MRayl) → 51.9% BW; double (z₁=8.5, z₂=2.4) → 75.3%; triple (z₁=14.2, z₂=4.1, z₃=1.9) → 89.5%; fourfold → 91.7%; fivefold → 95.4%
- Iterative optimisation required for n≥3 to find impedances; avoid excessively large z₁ to prevent passband ripple
- Matching layer thicknesses: set to α_h × λ/4, with α_h=1.18 for triple layers (slightly above λ/4)
- Triple layer disk transducer (PbTiO₃, 15 mm dia, 0.625 mm thick): measured 88% BW, 3.2 dB RTIL, <1 dB passband ripple — good agreement with theory
- Materials: matching layer 1 = borosilicate glass (z=14.2 MRayl), layer 2 = glass-epoxy composite (z=4.12 MRayl), layer 3 = urethane resin (z=1.92 MRayl)
- 3.5 MHz linear array probe with triple layers: resolves 1-mm-spaced nylon fibres at 13 cm depth; superior to double layer probe
- Key design rule: if z₁ is too large, cutoff becomes sharp with ripples; avoid overshoot
