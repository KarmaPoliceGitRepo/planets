# Field Patterns of Pulsed, Focused, Ultrasonic Radiators in Attenuating and Nonattenuating Media

- **Source:** 1982 - Field patterns of pulsed, focused, ultrasonic radiators in attenuating and nonattenuating media - (1982) MM Goodsitt EL Madsen.pdf
- **Drive link:** https://drive.google.com/file/d/1wh8rznrKrGE9lkl-lVyygZSPmVWavEnQ/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Mitchell M. Goodsitt, Ernest L. Madsen, James A. Zagzebski / 1982
- **Coverage:** full

## Overview
A 12-page JASA paper presenting a theoretical framework to calculate hydrophone voltage signals produced by pulsed, focused ultrasonic transducers in both attenuating and nonattenuating media, along with extensive experimental validation. The core approach is superposition of continuous-wave (CW) beams (Fourier components) to form pulsed waveforms, combined with a hydrophone response model that accounts for the finite receiver aperture and its frequency-dependent transfer function. Tissue-mimicking (TM) phantom material is used to represent soft-tissue attenuation.

## Unique contribution
This paper provides one of the first complete theory-experiment comparisons for pulsed, focused radiators in attenuating media. Prior work only addressed pulsed nonfocused transducers or used simulated (not real) pulse shapes. The efficient single-integral CW pressure expression (derived in a companion article) reduces computation from ~9.6 h (double integral, 96th-order Gauss quadrature) to 12 min per waveform on 1982 minicomputer hardware. The paper also systematically investigates edge waves, nonlinear effects, and the role of dispersion relations (Kramers–Kronig vs. measured) on waveform prediction accuracy.

## Key concepts
- Pulsed focused ultrasonic radiator / transducer
- Superposition of continuous-wave (CW) beams
- Rayleigh integral / focused piston model
- Complex wavenumber (attenuation + dispersion)
- Hydrophone response model (finite aperture, transfer function)
- Hydrophone-modified spectral content H(ω)
- Tissue-mimicking (TM) phantom material
- Attenuation coefficient (frequency-dependent, ~1.32 dB/cm/MHz)
- Kramers–Kronig relation (dispersion in attenuating media)
- Edge waves vs. direct waves (Tupholme decomposition)
- Nonlinear acoustic effects / second harmonic generation
- Focal region / center of curvature
- F-number / projected radius / radius of curvature

## Methods / results / takeaways
- Two medical focused transducers studied: 2.25 MHz and 3.5 MHz, both 19 mm diameter with long internal focus; driven by two pulsers (Panametrics 5052 and Unirad Sonograph II).
- Setup: scanning tank with alcohol-water mixture (sound speed ≈ 1570 m/s); Raytheon PVF₂ hydrophone (1.5 mm active diameter); Biomation 8100 at 100 MHz; PDP 11/34 minicomputer.
- Radius of curvature determined from directivity function measurement: 2.25 MHz → 11.0 cm, 3.5 MHz → 13.7 cm. Projected radius: 9.4 mm (3.5 MHz) and 9.14 mm (2.25 MHz).
- TM phantom: gelatin + graphite; attenuation α(f) = 1.32 dB/cm/MHz × f + 0.00145 f³·⁷; speed of sound ~1570 m/s, frequency-dependent per polynomial fit.
- Theory-experiment agreement: Vpp ratios and Vrms ratios within ~5–15% across on-axis, off-axis, attenuated, and unattenuated cases for both transducer-pulser combinations.
- Best H(ω) estimates obtained from hydrophone reference signals in the focal zone rather than at the center of curvature; the two choices differ in their high-frequency content.
- Theory fails (a) within ~1 cm of transducer face (CW approximation breaks down), (b) when pulse amplitudes cause significant nonlinear distortion. Reducing pulse amplitude via attenuating phantom restores agreement.
- Dispersion matters: measured c(f) polynomial gives best waveform shape; Kramers–Kronig gives adequate approximation; constant sound speed noticeably degrades predictions.
- Edge waves (direct wave + diffracted edge wave from transducer rim) are visible in theoretical predictions but masked experimentally by the rubber collar on the hydrophone.
- Practical takeaway: this modeling approach is applicable to ultrasonic dosimetry, transducer design for specific organs, and signal analysis for scattering from within patients.
