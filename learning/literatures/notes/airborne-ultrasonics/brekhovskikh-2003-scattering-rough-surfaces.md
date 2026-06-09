# Scattering of Sound at Rough Surfaces (Chapter 9, Ocean Acoustics)

- **Source:** Brekhovskikh 2003 scattering rough surfaces
- **Drive link:** https://drive.google.com/file/d/1J0zo30GKuhHu-DFI6Wi1IiJ49iU1WlTB/view
- **Type:** book
- **Author/Year:** Brekhovskikh & Lysanov, 2003 (Fundamentals of Ocean Acoustics, 3rd ed., Chapter 9; Springer)
- **Coverage:** partial (large file; Chapter 9 extracted, possibly full chapter)

## Overview
Chapter 9 of the standard ocean acoustics reference textbook, covering theoretical methods for sound scattering at randomly rough surfaces (ocean surface and bottom). Presents: (1) Rayleigh parameter definition; (2) Method of Small Perturbations (MSP) for small-height, small-slope roughness; (3) Kirchhoff (tangent-plane) approximation for large smooth roughness; (4) statistical characterisation of scattered field; (5) coherent and diffuse components; (6) backscattering strength. The content is the ocean acoustics framing of the same physics used in ultrasonic roughness measurement.

## Unique contribution
Authoritative textbook treatment of rough surface scattering physics relevant to all ultrasonic roughness measurement methods in this folder. Provides rigorous derivations of the Rayleigh parameter P = 2kσcosθ₀, the MSP first-order scattered field, and the Kirchhoff approximation coherent and diffuse intensities. The ocean context (surface waves, bottom roughness) does not diminish its value as a reference derivation source for general rough-surface scattering theory.

## Key concepts
- Rayleigh parameter P = 2kσcosθ₀ (P < 1 → specular; P ≫ 1 → diffuse)
- Method of Small Perturbations (MSP) / perturbation theory
- Kirchhoff / tangent-plane approximation
- Coherent and diffuse (incoherent) scattered field components
- rms roughness σ and surface correlation function
- Scattering cross-section and backscattering strength
- Pressure-release and rigid boundary conditions
- Phase difference Δφ = 2kσcosθ₀ per scattering point

## Methods / results / takeaways
- Rayleigh parameter derivation: phase difference along ray ACD vs mean plane = 2k·ζ·cosθ₀; rms phase difference = P = 2kσcosθ₀; P→0 as θ₀→π/2 (grazing) — scattering vanishes and reflection becomes specular.
- MSP: expand boundary conditions at rough surface z = ζ(r) in Taylor series about mean plane; results in virtual source distribution at z = 0 radiating scattered field; first-order result used for small ζ and small slopes.
- Kirchhoff approximation: assume local plane-wave reflection at each surface facet (tangent-plane assumption); valid when radius of curvature ≫ λ and illuminated area ≫ λ²; gives coherent component I_c = I₀·exp(−P²) and diffuse component.
- Coherent intensity: I_c ∝ exp(−(2kσcosθ₀)²) — Gaussian decay with Rayleigh parameter squared.
- Diffuse intensity: depends on surface correlation function; for Gaussian correlation C(r) = σ²exp(−r²/l²), diffuse pattern Gaussian in angle.
- Backscattering: treated for both pressure-release (air-water surface) and rigid (ocean bottom) boundaries.
- Note: this is the ocean acoustics version; the same equations appear in the ultrasonic roughness papers (Sukmana 2005, Saniman 2016, etc.) but applied to solid surfaces in air or water — same physics.
