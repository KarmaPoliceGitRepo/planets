# Foundations for Microwave Engineering — Introduction (Chapter 1)

- **Source:** Introduction.pdf (from "2001 - Foundations for Microwave Engineering - Robert E. Collin" folder)
- **Drive link:** https://drive.google.com/file/d/1i9epPop61QRvwBDut999_NehzBbmMetJ/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001 (2nd ed., McGraw-Hill / IEEE Press reprint)
- **Coverage:** full

## Overview
The introductory chapter of Collin's classic microwave engineering textbook. Surveys microwave frequency bands (300 MHz to 30+ GHz), the history and broad application space of microwaves (radar, satellite, terrestrial links, heating, scientific), and explains why conventional lumped-circuit analysis fails at microwave frequencies. Introduces waveguides, transmission lines, coupling methods, and the transition to field-based analysis.

## Unique contribution
Provides the definitive survey of why microwave engineering requires EM field theory rather than circuit theory, citing the physical argument about propagation time vs. signal period. Also gives a historical overview of microwave applications from WWII radar through modern MMIC circuits.

## Key concepts
- Microwave frequencies: 1–100 GHz (wavelengths 30 cm – 3 mm)
- Frequency band designations (VHF, UHF, SHF, EHF; radar bands L, S, C, X, Ku, K, Ka)
- Why lumped-circuit analysis fails: propagation delay comparable to signal period
- Transmission lines: two-conductor, coaxial, shielded strip
- Hollow-pipe waveguides: rectangular (most common), circular, ridge
- Surface waveguides
- Coupling methods: probe (electric), loop (magnetic), aperture
- Microstrip and coplanar transmission lines (compatible with solid-state devices)
- Resonant cavities replacing LC circuits (Q > 10⁴)
- MMIC (monolithic microwave integrated circuits)
- Scattering-matrix (S-parameter) formulation

## Methods / results / takeaways
- At frequencies where λ is comparable to circuit dimensions, Kirchhoff's laws fail and Maxwell's equations are required.
- Hollow-pipe waveguides support TEM, TE, and TM modes; TEM is the principal transmission-line mode; TE and TM are the waveguide modes.
- Resonant cavities achieve Q > 10⁴ vs. Q ~ 10–100 for lumped LC resonators.
- MMIC fabrication allows integration of transmission-line circuits and active devices (FETs) on a single GaAs chip; GaAs FETs operate usefully to millimeter-wave frequencies.
- Applications include: radar, satellite links (C-band 4/6 GHz, Ku-band 11/14 GHz), terrestrial microwave links (TD-2 system: 480 voice circuits at 3.7–4.2 GHz in 1948), microwave ovens (2.45 GHz, 500–1000 W), industrial heating (915 MHz, 2.45 GHz), and scientific instruments.
