# Profiling High-Angle Surfaces Using TOF Ultrasound

- **Source:** Stanke & Liang 1990 profiling high-angle surfaces
- **Drive link:** https://drive.google.com/file/d/1UhAVc2rBe1p6XVNjkAibEgfA_BRbVUO3/view
- **Type:** paper
- **Author/Year:** Stanke & Liang, 1990
- **Coverage:** full

## Overview
Water-immersion study investigating TOF-based profiling of surfaces tilted at high angles relative to the transducer beam axis. Evaluates several TOF detection algorithms (threshold, centre-of-energy COE, zero-crossing) and identifies COE as the best estimator for maintaining accuracy on angled surfaces.

## Unique contribution
Systematic comparison of TOF estimation algorithms specifically for angled/high-curvature surfaces where waveform shape distortion becomes significant. The Centre-of-Energy (COE) definition is identified as the most robust and accurate TOF estimator — a finding transferable to air-coupled profiling.

## Key concepts
- TOF estimation algorithms
- Centre-of-energy (COE) TOF definition
- High-angle surface profiling
- Threshold detection
- Zero-crossing detection
- Water immersion ultrasonics
- Surface profilometry

## Methods / results / takeaways
- Experiment: water-immersion focused transducer scanning surfaces tilted 0–45° from normal.
- TOF estimators compared: threshold (first crossing), peak, zero-crossing, centre-of-energy (COE).
- COE definition: TOF = ∫t·|p(t)|² dt / ∫|p(t)|² dt — weighted centroid of pulse energy.
- COE showed least systematic error vs surface angle; threshold detection showed strong angle-dependent bias.
- Errors with threshold: >50 μm at 30° tilt; COE: <10 μm at same tilt.
- Physical reason: wave scattering from a tilted surface distorts the pulse leading edge asymmetrically; energy centroid is less affected.
- Directly applicable to air-coupled surface profilometry where surfaces are rarely perfectly normal to the beam.
