# Acoustic Wave Propagation in an Adhesive Bond Model with Degrading Interfacial Layers

- **Source:** Acoustic Wave Propagation in an Adhesive Bond Model with Degrading Interfacial Layers - (1992) Robert F. Anastasi And Mark J. Roberts.pdf
- **Drive link:** https://drive.google.com/file/d/1f7RYfQp4Q_IeJ3OeF9UNcJmA8v_drIm0/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Robert F. Anastasi, Mark J. Roberts (U.S. Army Materials Technology Laboratory) / 1992
- **Coverage:** full

## Overview
A U.S. Army Materials Technology Laboratory technical report (MTL TR 92-63) that examines adhesive bond quality using a five-layer model (adherend / interfacial layer / adhesive / interfacial layer / adherend) rather than the conventional three-layer model. Bond quality degradation is simulated by reducing the density of the thin interfacial layers. Both an analytical frequency-domain reflection coefficient method and a two-dimensional finite element method (FEM) are used and compared, demonstrating strong agreement at resonant frequency minima locations.

## Unique contribution
Introduces interfacial layer density as the degradation parameter (modeling real-world primer/oxide layer weakening) and pairs an analytical 1D input-impedance approach with a 2D explicit FEM to cross-validate results. The paper shows that resonant frequency minima shift downward and their spectral bandwidths narrow as bond quality decreases — both effects provide measurable NDE indicators. The FEM approach allows two-dimensional effects (mode coupling, aperture diffraction) to be assessed against the 1D model.

## Key concepts
- Five-layer adhesive bond model (adherend / interfacial layer / adhesive / interfacial layer / adherend)
- Interfacial layer density as bond quality parameter
- Reflection coefficient / input impedance method (Brekhovskikh)
- Resonant frequency minima (spectral depression)
- Spectral bandwidth as bond quality indicator
- Finite element method (FEM) for acoustic wave propagation
- Fast Fourier Transform (FFT) of time-domain FEM output
- Mode coupling (longitudinal-shear) in 2D FEM
- Normal incidence longitudinal wave
- Adhesion vs. cohesion failure

## Methods / results / takeaways
- **Analytical model:** Brekhovskikh input-impedance recursion applied to the 5-layer system; reflection coefficient computed in frequency domain for bond quality levels of 10%, 20%, 50%, 100% (percentage of full adherend or adhesive density in the interfacial layer).
- **FEM model:** 2D explicit time-stepping; spatial sampling of 8 nodes/wavelength; raised-cosine force excitation; results FFT'd and overlaid with analytical spectra.
- **Case 1 (interface modeled like adherend, f₀ = 15 MHz):** 100% quality bond resonance minimum at 15.00 MHz (analytical) / 14.93 MHz (FEM); degrades to 13.75 / 13.72 MHz at 10% quality.
- **Case 2 (interface modeled like adhesive, f₀ = 10 MHz):** 100% quality minimum at 12.50 MHz (analytical) / 12.40 MHz (FEM); degrades to 6.20 / 6.16 MHz at 10% quality (much larger shift, more sensitive).
- **Frequency error:** <2% between analytical and numerical across all quality levels, validating the FEM.
- **Bandwidth finding:** spectral depression bandwidth is proportional to bond quality — wider bandwidth indicates a stronger bond.
- **Practical takeaways:** Case 2 geometry (interfacial layer with adhesive-like initial properties) offers greater frequency-shift sensitivity to degradation and is better suited for NDE. Interfacial layer modeling is essential; a 3-layer model cannot capture adhesive failure.
