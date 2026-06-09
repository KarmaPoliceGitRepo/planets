# Lateral Displacement Measurement Using Air-Coupled Ultrasound Transducers

- **Source:** Matsuya 2015 lateral displacement measurement
- **Drive link:** https://drive.google.com/file/d/1k4JZ-82FeXKaWF9J8pt0sWeItkmvjG5A/view
- **Type:** paper
- **Author/Year:** Matsuya, Matsumoto & Ihara, 2015 (Mech. Eng. Journal Vol. 2 No. 1)
- **Coverage:** full

## Overview
Proposes a lateral displacement measurement method using 3 air-coupled 400 kHz transducers exploiting the Gaussian far-field intensity profile. Steel wire target; accuracy ±0.5 mm over ±15 mm range at 250 mm distance. Applicable to building structural health monitoring during earthquakes.

## Unique contribution
Exploits the Gaussian far-field beam profile of air-coupled transducers to measure lateral (not axial) displacement from the amplitude ratio of two adjacent transducers. Provides simple closed-form equations for extracting displacement from log-ratio of signals, without requiring beam scanning.

## Key concepts
- Lateral displacement measurement
- Air-coupled ultrasound 400 kHz
- Gaussian far-field beam profile
- Intensity ratio method
- Structural health monitoring (SHM)
- Near-field/far-field transition
- Building earthquake damage assessment

## Methods / results / takeaways
- Transducer: JPR-10C 0.4K 14×20 mm rectangle, 400 kHz; near-field length N = 55.6 mm.
- Geometry: 3 transducers side-by-side (17 mm interval), target (ϕ4 mm steel cylinder) at Y = 250 mm.
- Method: x₀ = A·ln(I₁/I₂) + B, where A and B are calibration constants from Gaussian σ and transducer spacing.
- Accuracy: ±0.5 mm over ±15 mm displacement range.
- Operating in far field (Y > N = 55.6 mm) essential for Gaussian approximation to hold.
- Beam spread angle: α = 7.18°; beam diameter at 250 mm ≈ 63 mm (sufficient overlap between adjacent transducers).
- Extension to wider range: add more transducer pairs; 2D measurement possible with 2D array.
