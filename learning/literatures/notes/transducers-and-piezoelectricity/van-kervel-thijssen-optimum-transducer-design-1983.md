# A Calculation Scheme for the Optimum Design of Ultrasonic Transducers

- **Source:** 1983 - A calculation scheme for the optimum design of ultrasonic transducers - van Kervel Thijssen.pdf
- **Drive link:** https://drive.google.com/file/d/1GqOb9MzIT2CGgd-Ti1hLqdN2uet404yO/view
- **Type:** paper
- **Author/Year:** S.J.H. van Kervel, J.M. Thijssen / 1983
- **Coverage:** full

## Overview
Presents a systematic matrix-based calculation scheme for the complete transfer function of a thickness-mode piezoelectric transducer, including backing, one or two quarter-wavelength matching layers, and electrical tuning. Uses the KLM model as the foundation and implements each transducer sub-unit as an ABCD transfer matrix, cascaded in series. Validated against a real clinical transducer and used to explore design optimisation for medical ultrasound applications.

## Unique contribution
Provides an analytical closed-form transfer function for the complete round-trip (pulse-echo) transducer response using transfer matrix cascade, enabling rapid simulation and exploration of design parameters. Demonstrates that treating the front half of the piezoelectric disc as a λ/4 layer (as in the KLM model) gives significant bandwidth improvement over previously proposed designs. Also clarifies the electrical source matching requirement: a series inductance neutralises C0 at resonance, improving sensitivity by ~30%.

## Key concepts
- KLM equivalent circuit (Krimholtz-Leedom-Matthaei 1970)
- Transfer matrix / ABCD two-port formalism
- Thickness-mode transducer transfer function
- Quarter-wavelength matching layers (single and double)
- Backing impedance effects on Q-factor and sensitivity
- Electrical source impedance matching
- Round-trip pulse-echo impulse response simulation
- Pulse duration, bandwidth, dynamic range optimisation

## Methods / results / takeaways
- Transfer function derived analytically as product of cascaded 2×2 transfer matrices for backing, piezo disc halves, λ/4 layers, and electrical port
- Simulation validated on clinical transducer: computed echo matches measured echo (except lens-related after-ringing)
- Backing effect: higher backing impedance → broader bandwidth but lower sensitivity; air backing maximises sensitivity, heavy backing shortens pulse
- Single vs double λ/4 layer: two layers halve echo duration and broaden spectrum; single layer Q = 2.4, double layer Q = 1.7 (from example)
- Electrical tuning: series inductance L = 1/ω₀C₀ neutralises static capacitance; without tuning, sensitivity drops 30%
- Optimal design requires defining a priority criterion (bandwidth, sensitivity, dynamic range) before optimising — trade-offs are unavoidable
- Desilets et al. formula Zc = (Z₀·Z_L)^(1/3) for single matching layer is validated within the KLM framework
