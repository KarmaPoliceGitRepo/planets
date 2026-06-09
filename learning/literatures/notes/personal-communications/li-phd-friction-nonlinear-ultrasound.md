# Measuring Friction at an Interface Using Nonlinear Ultrasonic Response

- **Source:** Thesis_XL_2018.pdf
- **Drive link:** https://drive.google.com/file/d/16nZsrWg0DzFkBSjzNLO_c8wi4OIEK_Tz/view?usp=drivesdk
- **Type:** thesis
- **Author/Year:** Xiangwei Li, 2018 (University of Sheffield, supervisors: Prof. R. Dwyer-Joyce and Dr. M. Marshall)
- **Coverage:** partial (large file, truncated extraction)

## Overview
This PhD thesis develops an ultrasonic method for in-situ measurement of friction coefficient at a contact interface by exploiting Contact Acoustic Nonlinearity (CAN). When high-power shear ultrasound interacts with a rough frictional contact, stick-slip motion at the asperities distorts the waveform and generates odd-order harmonics (3rd, 5th, etc.) not present in the incident signal. The ratio of harmonic amplitude to fundamental encodes the friction coefficient and contact pressure. The work spans analytical derivation, 1-D finite difference numerical simulation, and experimental validation on aluminium-on-aluminium specimens.

## Unique contribution
Li provides the first systematic analytical and experimental investigation of shear-wave harmonic generation specifically due to Coulomb friction (stick-slip) at a compressed rough contact, as opposed to prior work focused on longitudinal-wave open/close ("clapping") nonlinearity. Two strategies are developed to extract friction coefficient from the measured A3/A1 harmonic ratio combined with the numerical look-up solution, and validated against sliding tribometer measurements.

## Key concepts
- Contact Acoustic Nonlinearity (CAN)
- Stick-slip friction / Coulomb friction
- Harmonic generation (odd harmonics: 3ω, 5ω)
- Shear wave nonlinear ultrasonics
- Clapping mechanism (longitudinal wave open/close nonlinearity)
- Reflection and transmission coefficient at contact interface
- Interfacial stiffness
- Finite difference method (1-D wave propagation)
- Piezoelectric element frequency response / multi-harmonic excitation
- High frequency nonlinear ultrasonic technique
- Fast Fourier Transform (FFT) signal processing
- Dimensionless contact stress ξ

## Methods / results / takeaways
- **Analytical model:** Treats the contact as a 1-D interface obeying Coulomb's law. Shear stress during slip is capped at μ·σ_n. This clips the transmitted/reflected waveform, generating odd harmonics. Only odd harmonics are produced because the clipping is symmetric (both tension and compression half-cycles clip equivalently for shear).
- **Numerical model:** 1-D finite difference simulation of wave propagation into a rigid wall with Coulomb friction at the interface. Results confirm that the third harmonic amplitude (A3) peaks at an intermediate contact pressure and decreases at high pressure (contact fully stuck, no slip → linear response). Harmonic generation is therefore favoured at low to moderate contact stress.
- **Effect of friction coefficient:** Higher μ shifts the nonlinear regime to higher contact pressures; A3/A1 increases with μ at fixed contact stress, enabling friction extraction.
- **Experimental setup:** Two aluminium cylinders compressed together; shear-wave PZT transmitter excited at 3.6 MHz (using a nominal 1 MHz element to access an odd harmonic of the element's resonance). Wideband receiver detects both fundamental and 3rd harmonic (10.8 MHz). Hanning window + zero-padding + FFT used for spectral analysis.
- **Challenge:** The PZT element itself generates harmonics (especially for low-frequency elements); a 5 MHz element was found to be cleaner. Careful frequency selection (excite at a resonance peak, receive harmonic at a spectral minimum of the element's own response) reduces instrument artefacts.
- **Friction coefficient extraction:** Two look-up strategies were developed mapping measured A3/A1 vs. numerical simulation curves at known contact pressure. Extracted μ values showed reasonable agreement with tribometer sliding results and published friction coefficient data for aluminium on aluminium.
