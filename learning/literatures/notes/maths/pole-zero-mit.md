# Understanding Poles and Zeros (MIT 2.14)

- **Source:** PoleZero MIT .pdf
- **Drive link:** https://drive.google.com/file/d/1RZLhFlst52eJMRIMWh_6uWemNgIisO1s/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** MIT Dept. of Mechanical Engineering, 2.14 Analysis and Design of Feedback Control Systems
- **Coverage:** full

## Overview
A 13-page MIT course note explaining poles and zeros of linear systems from the transfer function perspective. Covers the pole-zero plot, its relationship to the homogeneous (natural) response, system stability, and a geometric method for constructing Bode magnitude plots directly from the pole-zero diagram.

## Unique contribution
Provides a purely geometric (graphical) interpretation of the transfer function: every pole/zero corresponds to a vector in the s-plane, and the magnitude and phase of H(s) at any point follow from the lengths and angles of those vectors. A practical Bode-plot construction method using only break frequencies (radial distances from origin) is derived from this geometry.

## Key concepts
- Transfer function H(s)
- Poles and zeros of a rational function
- Pole-zero plot (s-plane)
- Homogeneous (natural) response
- Asymptotic stability (all poles in left-half s-plane)
- Marginal stability (poles on imaginary axis)
- Frequency response H(jω)
- Bode magnitude plot
- Break frequency
- Damping ratio ζ, natural frequency ωn

## Methods / results / takeaways
- A real pole in the left-half plane gives a decaying exponential; right-half plane gives unstable growth; imaginary axis gives undamped oscillation.
- Complex conjugate poles near the imaginary axis produce a resonance peak in the frequency response.
- Complex conjugate zeros near the imaginary axis create a notch (zero gain at the zero frequency).
- Bode construction: identify break frequencies as radial distances of each pole/zero from origin; slope changes by ±20 dB/decade per pole/zero at each break frequency.
- For second-order underdamped system: poles lie on a semicircle of radius ωn at angle ±cos^{-1}(ζ) from negative real axis.
