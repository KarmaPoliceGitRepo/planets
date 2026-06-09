# Focusing of Ultrasound Beams

- **Source:** Focusing of ultrasonic beams - HJGohari.pdf
- **Drive link:** https://drive.google.com/file/d/1jnwFstA-Q4jOLB0cScIyLhVBL7A40hjY/view?usp=drivesdk
- **Type:** thesis
- **Author/Year:** H. J. Gohari / ~1996–1997 (submitted to IEEE Ultrasonics Symposium 1996)
- **Coverage:** partial (large file; extraction covers all chapters but some figure detail and appendix source code are sparse)

## Overview
A graduate thesis (approximately 90 pages) that provides both a textbook-style derivation of acoustic wave propagation and focusing theory and an original simulation study comparing conventional spherically focused circular transducers with limited-diffraction (Bessel) beams for ultrasound imaging. The simulation software is developed in MATLAB and designed for integration into the Ultrasim simulator. The work covers wave equations, array transducer types, field calculations for unfocused and focused circular transducers, Bessel beam theory, bowtie Bessel beams, sidelobe reduction techniques, and direct comparison of Bessel and focused beams using an annular array transducer.

## Unique contribution
The thesis systematically compares Bessel beams and conventional focused beams produced by the same annular array transducer—not just theoretically but through matched simulations. It presents bowtie limited-diffraction beams (spatial derivatives of Bessel beams in one transverse direction) as a sidelobe-reduction approach that does not sacrifice frame rate, unlike the summation-subtraction method (which reduces frame rate to 1/3). Numerical results quantify the trade-off between lateral resolution, depth of field, sidelobe level, and aperture size across both beam types.

## Key concepts
- Acoustic wave equation (1D, 3D Cartesian, spherical, cylindrical coordinates)
- Rayleigh–Sommerfeld diffraction integral
- Fresnel / Fraunhofer near-field / far-field regions
- Focused circular transducer (spherically curved surface)
- F-number (FN = F/2a)
- Lateral beamwidth / focal diameter (jinc function)
- Depth of focus (sinc-function approximation, 6 dB → Lf = 9.68λ·FN²)
- Sidelobes / aperture apodization (Hanning weighting)
- Linear phased array, switched array, annular array, 2D array transducers
- Bessel beams / limited-diffraction beams (zeroth-order, nth-order)
- Scaling factor α (controls Bessel beam lateral resolution)
- Maximum depth of field Zmax = R/tan(θ) for finite aperture Bessel beam
- Summation-subtraction sidelobe reduction (frame rate penalty ×1/3)
- Bowtie limited-diffraction beams (m-th derivative of Bessel beam in y)
- A-mode, B-mode, M-mode pulse-echo imaging
- Image quality metrics: lateral resolution, axial resolution, contrast resolution, frame rate

## Methods / results / takeaways
- Focused transducer (reference case, Ch. 4): diameter 15 mm, 4 equal-area annular elements, 3.5 MHz, fixed focus F = 75 mm → Fresnel parameter S = 0.59; -3 dB depth of focus ≈ 79 mm, -6 dB lateral beamwidth ≈ 3.1 mm; first sidelobe 17.67 dB below mainlobe.
- Hanning apodization on same transducer: lateral beamwidth widens to 4.6 mm, first sidelobe drops to 25 dB below mainlobe — classic resolution-sidelobe trade-off.
- Bessel beam transducer (Ch. 5): diameter 50 mm, 10 rings (equal-area per Bessel zeros), 2.5 MHz, scaling factor α = 1202 m⁻¹; lateral -6 dB width ≈ 2.53 mm, predicted maximum depth of field Zmax ≈ 216 mm (from geometrical shadow formula). First sidelobe only 8 dB below mainlobe (vs. 17.67 dB for focused).
- Halving aperture to 25 mm: depth of field halves to ~100 mm; lateral resolution unchanged (α fixed). To restore depth of field, α must increase, which narrows the beam (1.82 mm).
- Frequency doubling (2.5 → 5 MHz, same aperture and α): depth of field doubles (~216 → ~430 mm); lateral resolution unchanged.
- Summation-subtraction: reduces first sidelobe from ~8 dB to ~14 dB below mainlobe, but requires 3 scan-lines per position → frame rate × 1/3.
- Bowtie Bessel beams (Ch. 5.5–5.6, 4th and 10th derivatives in y): sidelobes are angle-dependent; at φ = 0° very low sidelobes but wide beam; at φ = 45° sidelobes rise to ~6 dB (4th deriv) and ~3.4 dB (10th deriv) below mainlobe. Best lateral resolution near φ = 30° with sidelobes ~13 dB (4th) and ~8 dB (10th) below mainlobe. Frame rate is not reduced.
- Comparison (Ch. 6–7): annular array can produce both Bessel-like and focused beams; Bessel beams offer superior depth of field but suffer from higher sidelobes than focused beams; the step-wise annular array approximation of a Bessel beam requires choosing an appropriate scaling factor.
- Key practical gotcha: the lateral resolution–depth-of-field trade-off is inescapable for both beam types; increasing depth of field always costs lateral resolution unless aperture is enlarged.
