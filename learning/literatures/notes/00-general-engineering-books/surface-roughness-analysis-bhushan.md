# Surface Roughness Analysis and Measurement Techniques

- **Source:** 2001 - Surface Roughness Analysis and Measurement Techniques 8403_PDF_CH02 - Bharat Bhushan.pdf
- **Drive link:** https://drive.google.com/file/d/1jy3-1X3RCM51k6cYOZ_Vx_Ic0o98ic3n/view
- **Type:** paper
- **Author/Year:** Bharat Bhushan (The Ohio State University), 2001 (CRC Press book chapter)
- **Coverage:** partial (large file, truncated extraction)

## Overview
Chapter 2 of a CRC Press reference work (likely the "Handbook of Micro/Nanotribology" or "Modern Tribology Handbook"), providing a rigorous treatment of solid surface structure, surface roughness characterisation theory, and a comprehensive survey of measurement methods from mechanical stylus profilometry through optical, scanning probe, fluid, electrical, and electron microscopy techniques. Both 2D profile and 3D surface map perspectives are covered. The emphasis is on quantitative characterisation suitable for tribological and precision engineering applications.

## Unique contribution
This chapter is notable for its breadth and depth in a single document: it unifies amplitude parameters (Ra, Rq, Rt, skewness, kurtosis), spacing/spatial parameters (peak density, zero-crossing density), statistical analyses (Gaussian/non-Gaussian distributions, autocorrelation, power spectral density), and fractal characterisation, then systematically links each to specific measurement instruments and their resolution limits. The comparative section on measurement methods (including accuracy, lateral resolution, vertical resolution, and applicable surface types) is particularly valuable for selecting appropriate metrology for a given application.

## Key concepts
- Surface texture (roughness, waviness, lay, flaws)
- Asperities (peaks) and valleys
- Ra (CLA / AA) — arithmetic average roughness
- Rq (RMS roughness) — standard deviation of heights
- Rt, Rp, Rv, Rz — extreme-value height descriptors
- Skewness (Sk) and kurtosis (K)
- Roughness grade numbers (N1–N11)
- Probability density function (PDF) and cumulative distribution function (CDF)
- Gaussian (normal) distribution of surface heights
- Kolmogorov-Smirnov test for Gaussianity
- Autocorrelation function
- Power spectral density (PSD)
- Fractal characterisation of surfaces
- Beilby layer (amorphous surface layer from forming)
- Surface oxide, adsorbed, and contaminant films
- Mechanical stylus profilometry
- Optical profilometry (phase-shifting interferometry, white-light scanning interferometry)
- Differential interference contrast (DIC) / Nomarski interferometry
- Angular distribution (AD) light scattering
- Speckle pattern correlation measurement
- Scanning probe microscopy (SPM/AFM/STM)
- Electron microscopy (SEM, TEM, replica techniques)
- Real area of contact
- Tribology: friction, wear, lubrication

## Methods / results / takeaways
**Surface structure**: Real solid surfaces have multiple zones — bulk material, work-hardened/deformed layer, Beilby (amorphous) layer, oxide/chemical film, adsorbed gas/hydrocarbon film, and occasional lubricant film. Each layer has distinct mechanical and chemical properties that affect tribological behaviour.

**Roughness parameters**:
- Ra = (1/L)∫|z − m|dx; Rq = √(1/L ∫(z−m)²dx). For Gaussian surfaces, σ ≈ 1.25 Ra.
- Skewness (Sk): third standardised moment — negative for surfaces with deep valleys (e.g., ground); positive for surfaces with high peaks.
- Kurtosis (K): fourth standardised moment — K = 3 for Gaussian; K > 3 (leptokurtic) for surfaces with occasional very high peaks; K < 3 for platykurtic surfaces.
- Height parameters alone are insufficient for complete characterisation; spacing parameters (peak density Np, zero-crossing density N0) and functional parameters are also needed.

**Surface statistics**: Gaussian distributions arise from cumulative stochastic processes (peening, lapping, electropolishing). Single-point (turning, shaping) and extreme-value processes (grinding, milling) tend to produce anisotropic, non-Gaussian surfaces. Gaussian test via probability paper plot or Kolmogorov-Smirnov test (significance threshold P = 0.01–0.05).

**Optical measurement highlights**:
- Angular distribution (AD) scattering: applicable only when σ << λ (roughly σ < 0.1 µm for He-Ne laser); vertical resolution < 1 nm; limited to optical-quality smooth surfaces.
- Speckle pattern correlation: degree of correlation between two speckle patterns from different illumination angles/wavelengths gives σ.
- Two-beam interferometry (phase-shifting): resolution < λ/100 vertically; height ambiguity when adjacent points differ by more than λ/4 — resolved by multi-wavelength or white-light scanning (coherence-peak) approach.
- White-light vertical scanning interferometry: measures fringe modulation envelope position to give absolute height; commercial systems from Wyko, Zygo, Phase Shift Technology.
- Nomarski/DIC interferometry: easy to use, vibration-insensitive, but measures surface slope (not height directly).
- Multiple-beam (Tolansky) interferometer: high reflectivity coating required; risk of scratching sample.

**Stylus profilometry**: Standard benchmark method; good lateral resolution limited by tip radius; convolves tip geometry with surface profile at fine scales.

**Fractal characterisation**: Surface profiles exhibit scale-invariant (fractal) statistical properties over many decades of spatial frequency, meaning classical parameters (Ra, Rq) are scale-dependent and cannot uniquely characterise a surface. Fractal dimension and related parameters provide scale-independent descriptors.
