# Influence of Acoustic Impedance of Multilayer Acoustic Systems on the Transfer Function of Ultrasonic Airborne Transducers

- **Source:** Gudra multilayer transfer function 2002
- **Drive link:** https://drive.google.com/file/d/1bXEPPq5SF21IWkzIsfneYf-zAUurQRdS/view
- **Type:** paper (Ultrasonics 40, 457–463, 2002)
- **Author/Year:** T. Gudra, K. J. Opielinski / 2002
- **Coverage:** full

## Overview
Computer analysis of the influence of matching layer impedance on the transfer function of PZT airborne (air-coupled) transducers with 1, 2, and 3 quarter-wave matching layers. Derives transfer function from difference equations (Z-transform approach) for multilayer structure including back-face loading. Compares three matching criteria — Chebyshev (geometric mean), DeSilets (binomial), Souquet (quality factor equalization) — for 1–3 matching layers. Shows that Chebyshev gives widest bandwidth but lowest peak; DeSilets gives highest peak (narrowest band); back-face loading increases bandwidth at cost of amplitude.

## Unique contribution
Provides explicit closed-form transfer function (Eq. 2) for transducer with two matching layers as a rational function of delay-line exponentials, enabling direct frequency-domain analysis of multilayer impedance systems without Mason or KLM circuit simulation. Shows computed transfer functions for 12 combinations of matching criteria and backing impedances (ZB = 0 to 104.2 MRayl tungsten) — providing a design map for PZT airborne transducers.

## Key concepts
- Transfer function K(jω) = VC3(jω) / I(jω): ratio of radiation velocity to input current
- Single ML optimum impedances: Chebyshev: ZC1 = √(ZCZT) = 0.113 MRayl; DeSilets: ZC1 = (ZCZ²T)^1/3 = 0.0176 MRayl; Souquet: ZC1 = (2ZCZ²T)^1/3 = 0.0222 MRayl (for ZC=30 MRayl, ZT=0.427 kRayl)
- DeSilets gives highest transfer function at f₀ (17 dB above Chebyshev) but narrowest band
- Chebyshev: widest band but 17 dB lower peak
- Double ML: DeSilets increases both bandwidth and peak vs single; higher ripple
- Triple ML: further bandwidth increase with small loss of peak amplitude
- Back-face loading: higher ZB → broader bandwidth + undulation; ZB comparable to ZC → function maximum shifts in frequency
- Optimal backing: heavy backing (ZB ≈ ZC) for broadband; light backing (ZB = 0) for maximum amplitude

## Methods / results / takeaways
- PZT: ZC = 30 MRayl; Air: ZT = 0.427 kRayl; computed transfer functions plotted as a function of normalized frequency f/f₀
- Computer program: calculates KCn(jω) for arbitrary number of layers; Z-transform difference equation approach
- Matching layer impedances computed for each criterion and each number of layers
- Results presented as normalized frequency vs |K(jω)| curves for various configurations
- Application: design of airborne PZT transducers for NDE; backing material selection for pulse-shape control
