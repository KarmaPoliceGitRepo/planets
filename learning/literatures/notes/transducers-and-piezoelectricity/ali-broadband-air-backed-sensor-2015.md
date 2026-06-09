# An Approach to Design Broadband Air Backed Piezoelectric Sensor

- **Source:** 01 - 2015 - An Approach to Design Broadband Air Backed Piezoelectric Sensor - Mohamed GS Ali.pdf
- **Drive link:** https://drive.google.com/file/d/1j6qG9HRiexcysHwEsSYypODrq8vam_rO/view
- **Type:** paper
- **Author/Year:** Mohamed G.S. Ali, Nour Z. Elsayed, Ebtsam A. Eid / 2015
- **Coverage:** full

## Overview
Presents a discrete-time (z-transform) implementation of the Mason equivalent circuit for predicting the impulse and frequency response of multilayer air-backed PZT-5A transducers. Determines optimum matching layer impedances and validates against published four-layer experimental data.

## Unique contribution
Implements the Mason model directly in the discrete-time domain using z-transform, avoiding FFT/IFFT round-trips and allowing direct time-domain filter representation of all reverberation layers. Provides systematic optimisation of 1–3 quarter-wave matching layers for air-backed PZT-5A working into water.

## Key concepts
- Z-transform discrete-time transducer model
- Air-backed piezoelectric transducer
- Quarter-wave matching layer optimisation
- Goll–Auld binomial impedance formula for multi-layer design
- Bond line thickness effect on resonance
- PZT-5A impedance matching into water

## Methods / results / takeaways
- Model based on Mason equivalent circuit transformed to z-domain: transfer functions expressed as polynomial ratios, computed as recursive digital filters
- Air backing with no matching: -3 dB bandwidth = 0.31 f0
- Binomial impedance progression formula: ln(Zn+1/Zn) = C(N,n)/2^N × ln(ZRF/Z0)
- Optimum single layer: glass bead–epoxy (Z = 4.2 MRayl, v = 2300 m/s); bandwidth improves to 0.54 f0
- Optimum two layers: glass arsenic trisulphide (8.0 MRayl) + polystyrene (2.5 MRayl); bandwidth = 1.1 f0
- Optimum three layers: glass (14.6) + glass bead–epoxy (4.2) + methylplaten (1.85 MRayl); bandwidth = 1.4 f0
- Bond lines <10 µm (λ/200 at 5 MHz) have negligible effect on frequency response
- Back copper matching layer raises 3-layer bandwidth from 1.4 to 1.48 f0
- Good agreement with Mulholland et al. (2008) experimental four-layer data
