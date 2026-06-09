# Ultrasonic Attenuation and Velocity in Three Transformation Products of Steel

- **Source:** Papadakis 1964 - grain size distribution from attenuation
- **Drive link:** https://drive.google.com/file/d/13XBBB8o.../view
- **Type:** paper
- **Author/Year:** E. P. Papadakis / 1964
- **Coverage:** full

## Overview
Companion paper to the transformation-products study above, extending the analysis to extract grain size distributions from measured frequency-dependent attenuation spectra using matrix inversion. Demonstrates that a distribution of scattering sizes fits the data better than a single effective grain size, particularly for complex microstructures.

## Unique contribution
Introduces a matrix inversion approach to extract grain size distribution p(D) from attenuation measurements at multiple frequencies, rather than assuming a monodisperse distribution. Shows that the method can distinguish bimodal distributions (e.g., large prior austenite grains coexisting with fine sub-grain features).

## Key concepts
- Grain size distribution
- Matrix inversion from attenuation
- Polydisperse scattering
- Lifshitz-Parkhomovskii formula
- Effective grain size
- Attenuation spectrum inversion

## Methods / results / takeaways
- Measured α(f) at 8–12 frequency points; inverted numerically with non-negative least squares to get p(D).
- Regularization needed to prevent oscillatory solutions; Tikhonov regularization applied.
- For fully pearlitic steel: distribution centered at colony size (~100 µm) with narrow width.
- For dual-phase and partially transformed microstructures: bimodal distributions recovered.
- Result validation: metallographic measurements of colony sizes consistent with extracted distributions within ~20%.
- Key limitation: ill-conditioned inversion; results sensitive to noise at high frequencies; regularization parameter must be chosen carefully.
