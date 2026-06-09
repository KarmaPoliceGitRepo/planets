# Wave Propagation in Isotropic Linear Elastic Solids — Lecture Notes

- **Source:** `Wave propagation in isotropic linear elastic solids_lectnotes helsinki uni.pdf` (Drive ID: 1CbIhzlYEnF-yKIGsW_8Y23hAtKEOQDsM)
- **Drive link:** https://drive.google.com/file/d/1CbIhzlYEnF-yKIGsW_8Y23hAtKEOQDsM/view
- **Type:** lecture notes (FoilTeX slides, ~35 pages)
- **Author/Year:** Unknown author, Helsinki University (undated)
- **Coverage:** full

## Overview
A compact but comprehensive set of FoilTeX lecture slides on wave propagation in elastic solids, fluids, and related media. Covers the classical theory of P- and S-waves in isotropic solids (Lamé equations), mode conversion at boundaries (Zoeppritz-style), guided waves in finite media (rods, plates), surface waves (Rayleigh, Love), fluid acoustics with viscosity and thermal relaxation, shallow-water dispersive waves, solitons, and shock waves. Also treats transversely isotropic media and wave propagation in inhomogeneous media via eikonal/Hamilton-Jacobi methods.

## Unique contribution
A self-contained, equation-dense overview tying together elasticity, acoustics, and nonlinear wave theory in a single short document. Useful as a reference map and formula sheet rather than a tutorial text.

## Key concepts
- **P-waves and S-waves:** CL = √[(λ+2μ)/ρ], CT = √[μ/ρ] (Lamé constants); wave equations from Navier equation
- **Transversely isotropic media:** five independent elastic constants (c11, c12, c13, c33, c44); quasi-P and quasi-S modes
- **Mode conversion at boundaries:** Zoeppritz-type amplitude equations for reflection/transmission at planar interfaces
- **Waves in finite media:** longitudinal rod velocity C = √[E/ρ], torsional C = √[G/ρ], flexural (Euler-Bernoulli beam, dispersive: ω ∝ k²)
- **Surface waves:** Rayleigh waves (speed ~0.92CT, elliptically polarized retrograde motion), Love waves (horizontally polarized shear in layered half-space)
- **Fluid wave propagation:** inviscid (pressure/bulk modulus), viscous Navier-Stokes (shear viscosity η, bulk viscosity ζ), thermal relaxation (coupled thermal-acoustic modes)
- **Attenuation in viscous fluids:** α ∝ ω²(4η/3 + ζ)/ρc³ — quadratic frequency dependence
- **Shallow-water waves:** dispersive with depth correction; gravity vs. capillary regimes
- **Nonlinear waves:** KdV equation (solitons: speed ∝ amplitude, stable shape); Burgers equation (shock waves with viscous dissipation)
- **Inhomogeneous media:** eikonal equation |∇τ|² = 1/c²; Hamilton-Jacobi / ray theory; WKB semiclassical approximation; wavefront tracking
- **Polytropic atmosphere:** sound speed c = √(γp/ρ); adiabatic lapse rate; stratified wave propagation

## Methods / Results / Takeaways
- Derivation begins from Newton's second law applied to a differential volume element → Navier equation of motion → Helmholtz decomposition into scalar (P) and vector (S) potentials
- Boundary conditions: continuity of normal stress and displacement (solid-solid), zero normal stress (free surface), zero normal displacement (rigid surface)
- For transversely isotropic media, the Christoffel equation gives three mode velocities as functions of propagation angle relative to the symmetry axis
- Rayleigh wave speed satisfies a cubic equation in (vR/CT)²; numerically ≈ 0.92CT for ν ≈ 0.3
- Love waves require a slower over-layer on a faster half-space; dispersive cutoff frequencies fn = nCT/(2H)
- Soliton solution to KdV: u(x,t) = A·sech²[(x – vt)/L] where v = c0 + A/3; amplitude and speed are locked
- Shock formation in Burgers equation: characteristics cross when gradient steepens; viscosity provides regularization at shock front

## See also
- `auld-acoustic-fields-vol1.md` — comprehensive treatment of elastic waves in solids (Auld 1973)
- `achenbach-wave-propagation-elastic.md` — Achenbach 1973 (djvu, unreadable)
- `brekhovskikh-waves-layered-media-1960.md` — layered media wave theory
