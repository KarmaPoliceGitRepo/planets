# Analysis of the Impedance Resonance of Piezoelectric Stacks

- **Source:** Sherrit 2000 stack impedance analysis
- **Drive link:** https://drive.google.com/file/d/1WCZE8W-P6NboDO2v2SzTQByY4ECfljxV/view
- **Type:** paper (conference, IEEE Ultrasonics Symposium)
- **Author/Year:** S. Sherrit, S.P. Leary, Y. Bar-Cohen, B.P. Dolgin, R. Tasker / 2000
- **Coverage:** full

## Overview
Studies inversion techniques for determining complex material constants from the impedance resonance spectra of zero-bond-length piezoelectric stacks, based on Martin's (1964) admittance equation. Shows that in the large-n limit (n>8 layers), the acoustic wave speed approaches the short-circuit elastic constant s^E₃₃, while for n=1 or 2 layers it is governed by the open-circuit constant s^D₃₃. Validates using Smits' method and a modified Levenberg-Marquardt non-linear regression on both synthetic and real (Morgan Matroc PZT 4s) stack data.

## Unique contribution
Provides the asymptotic analytical equations for piezoelectric stacks in both small-n (1,2) and large-n (>8) limits, enabling direct material constant extraction. Demonstrates the transition from constant-D to constant-E acoustic wave speeds as layer number increases. Identifies the intermediate n=3 to 8 regime as having up to 6% error in coupling constant and 20% error at k₃₃=0.75 if using limiting equations — requiring full non-linear regression for accuracy.

## Key concepts
- Piezoelectric stack zero bond-length model (Martin 1964)
- n layers in mechanical series, electrical parallel — Mason equivalent circuit
- Constant-D vs constant-E acoustic boundary conditions
- Large-n limit (n>8): wave speed → v_D = 1/√(ρ·s^E₃₃) (constant E)
- Small-n limit (n=1,2): wave speed → v_D = 1/√(ρ/s^D₃₃) (constant D)
- Smits' iterative method for complex material constants from admittance
- Levenberg-Marquardt non-linear regression for arbitrary n
- k₃₃, s^E₃₃, d₃₃, ε^T₃₃ extraction from stack impedance

## Methods / results / takeaways
- Analytical admittance equation for general n (equations 1-7); reduces to Eq.8 (large-n) and Eq.10 (n=1,2) in limiting cases
- Error in using limiting equations: for n=3, errors up to 3% in coupling (6% at k₃₃=0.75); elastic constant errors up to 20% for k₃₃=0.75
- LM regression: converges to input values within numerical limits for synthetic data; robust to 10% random noise
- Morgan Matroc PZT 4s stack (nL=0.00501 m, A=1.9×10⁻⁴ m², density=7794 kg/m³, n=effective): extracted constants in good agreement with manufacturer specifications
- Note: small-signal resonance measurements constitute a baseline (linear, reversible regime); high-field quasi-static properties differ — dielectric and piezoelectric constants double near coercive field for soft PZT (Motorola 3203HD)
- Frequency dispersion of permittivity: low-frequency permittivity slightly higher than resonance value due to intrinsic material dispersion
