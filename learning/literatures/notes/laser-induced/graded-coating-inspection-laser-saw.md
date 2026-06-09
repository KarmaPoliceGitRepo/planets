# Graded Coating Inspection Using Laser Generated Surface Acoustic Waves

- **Source:** Graded coating inspection using laser generated surface acoustic waves  - OO Balogun (2004).pdf
- **Drive link:** https://drive.google.com/file/d/1w5Z6Cku8CWPaUGvK09zwWmxupIVPOhFl/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Oluwaseyi O. Balogun, Todd W. Murray / 2004
- **Coverage:** full

## Overview
A conference paper (AIP, RQNDE Vol. 23) presenting a theoretical model for laser generation of ultrasound in functionally graded materials (FGMs). The authors model graded coatings as multilayer systems and investigate how surface acoustic wave (SAW) dispersion behavior depends on the depth-dependent elastic property profile, then develop an inversion algorithm to recover those profiles from measured dispersion data.

## Unique contribution
Extends laser-SAW theory explicitly to FGMs by combining a power-law composition profile with a modified rule of mixtures (MROMs) formulation for layer elastic properties, and demonstrates that a simple downhill simplex inversion can recover the power-law exponent and stress-strain transfer parameter from simulated dispersion data with good accuracy (recovered n ≈ 0.98 vs. target 1.0).

## Key concepts
- Functionally graded materials (FGMs)
- Surface acoustic waves (SAWs)
- SAW phase velocity dispersion
- Transfer matrix method (Hankel/Laplace domain)
- Rule of mixtures / modified rule of mixtures (MROMs)
- Power-law composition profile
- SAW inversion / downhill simplex algorithm
- Multilayer coating model
- Mullite/SiC material system

## Methods / results / takeaways
- Graded coating modeled as a stack of homogeneous isotropic layers; elastic properties of each layer computed via MROMs using a power-law volume fraction.
- Time-domain and frequency-domain SAW responses computed using the transfer matrix method in Hankel/Laplace space with numerical inverse transforms.
- Numerical results for a mullite/SiC system (coating thickness 30–40 µm, frequency range 0–600 MHz) show: 4 layers are sufficient to represent continuous gradation; SAW velocity is insensitive to property variations at spatial scales below ~5 µm.
- Through-thickness elastic modulus variation of 10–50% produces measurable changes in dispersion; the power-law exponent (n = 1/5 to 5) strongly shapes both dispersion curves and time-domain waveforms.
- Inversion on simulated noisy data recovered n = 0.98 and Q = 879 GPa vs. targets of 1.0 and 1000 GPa — confirming feasibility.
- Key practical limit: technique probes only near-surface region (penetration depth ≈ wavelength), so absolute depth resolution depends on frequency range.
