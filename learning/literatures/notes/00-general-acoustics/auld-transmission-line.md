# Acoustic Plane Waves in Isotropic Solids — Transmission Line Model

- **Source:** Transmission line - BA Auld Acoutic fields and waves in solids.pdf
- **Drive link:** https://drive.google.com/file/d/12PfpjrFV6WLa18dkI8J6LyZbK-S4TtR4/view?usp=drivesdk
- **Type:** book
- **Author/Year:** B.A. Auld, 1973 (Chapter 6, Section D–E, "Acoustic Fields and Waves in Solids", Wiley-Interscience)
- **Coverage:** partial (excerpt covers §§ D and E of Chapter 6)

## Overview
Extracted chapter/section from Auld's classic two-volume textbook on acoustic fields and waves in solids. This excerpt covers the transmission line analog for acoustic plane waves in isotropic media, showing how the 1D acoustic equations for longitudinal and shear waves are mathematically equivalent to electrical transmission line equations. Includes treatment of damping (viscous) and plane-wave excitation by distributed body forces.

## Unique contribution
The transmission line analogy (negative stress ↔ voltage, particle velocity ↔ current, density ↔ inductance/unit length, inverse stiffness ↔ capacitance/unit length) provides an extremely powerful circuit-based intuition for acoustic wave scattering, transmission, and reflection. The Q values for single-crystal materials at 100 MHz and 1000 MHz are given (e.g., fused silica Q ≈ 3.9 × 10³ at 1 GHz), placing material loss in practical context.

## Key concepts
- Stiffness tensor for isotropic solids (C₁₁, C₁₂, C₄₄)
- Acoustic plane wave equations (particle velocity, stress)
- Transmission line analogy: voltage = -stress, current = particle velocity
- Characteristic impedance Za = √(ρ·C_jj)
- Complex wavenumber for lossy propagation: k = ω√(ρ/C_jj·(1 + iωη/C_jj))
- Acoustic Q (quality factor), viscous damping coefficient η
- Complex power flow (Poynting's theorem analog)
- Excitation by distributed body forces (normal mode decomposition)

## Methods / results / takeaways
The acoustic field equations in 1D decompose into three independent sets corresponding to P-wave (longitudinal, governed by C₁₁) and two independent S-waves (shear, governed by C₄₄). Each set is formally identical to the lossless/lossy transmission line equations, enabling the use of circuit techniques (impedance matching, ABCD matrices, Smith charts) for acoustic design. The characteristic acoustic impedance is Za = ρ·v_phase. Introducing viscous damping adds a conductance G per unit length to the shunt element. This model simplifies wave scattering at interfaces and is the basis for the Mason circuit model used in transducer design.
