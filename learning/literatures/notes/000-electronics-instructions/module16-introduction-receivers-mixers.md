# Module 16 – Introduction to Receivers and Mixers

- **Source:** module16 - Introduction to Receivers and Mixers.pdf
- **Drive link:** https://drive.google.com/file/d/1xmF_4lMJm_2o0I2FzHyJfZzkc-qKvLhb/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (30 pages) introducing the RF receiver chain from antenna to baseband, motivating frequency translation via mixing, defining the image problem, and comparing superheterodyne and direct-conversion (zero-IF) architectures. Introduces the Hartley image-reject mixer.

## Unique contribution
Presents a balanced comparison of superheterodyne vs. direct-conversion architectures with quantitative treatment of image rejection ratio (IRR) impairments, and derives the IRR formula in terms of gain and phase mismatch of the I/Q paths — directly applicable to integrated transceiver specification.

## Key concepts
- Frequency translation / mixing
- Image frequency
- Superheterodyne architecture
- Direct-conversion (zero-IF) architecture
- IF (intermediate frequency)
- Local oscillator (LO) leakage
- Flicker noise at DC (zero-IF problem)
- DC offset
- I/Q imbalance
- Hartley image-reject mixer
- Image rejection ratio (IRR)

## Methods / results / takeaways
- Ideal multiplier mixer: output = RF·LO = cos(ωRF·t)·cos(ωLO·t) → desired IF at ωRF−ωLO and image at ωRF+ωLO (and vice versa).
- Image problem: the image frequency (ωLO ± ωIF) also down-converts to the same IF; must be filtered before mixing or rejected by I/Q cancellation.
- Superheterodyne: uses an off-chip image-reject filter before the first mixer; IF chosen to make the image filter feasible; high IF → easier image filter, harder channel filter; low IF → reversed trade-off.
- Direct conversion: LO = RF → image = desired signal (self-image problem avoided by I/Q); challenges include LO leakage to antenna, DC offset from LO self-mixing, and 1/f noise directly in band.
- Hartley image-reject mixer: uses 90° phase shifts and an adder to cancel image; IRR degrades with I/Q amplitude/phase errors.
- IRR ≈ 10·log[(δA/A)² + (δθ)²]/4 where δA is amplitude mismatch and δθ is phase error; 1° phase error → ~40 dB IRR limit.
- Modern solutions: digital I/Q calibration to correct mismatch; adaptive algorithms can achieve >60 dB IRR.
