# Solving the Telegrapher's Equation by Klein-Gordon Equation (Frequency Domain)

- **Source:** SolvingTelegrapher_fdom.pdf
- **Drive link:** https://drive.google.com/file/d/1rJ4AVKvpvmDcz-KfmX_NIReAhzsiuFsb/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 12, 2013 (Reference: EqWorld)
- **Coverage:** full

## Overview
Derives the solution of the full time-domain telegrapher's equations (a second-order hyperbolic PDE with damping) by transforming them into the Klein-Gordon equation via the substitution F(x,t) = e^(–kt/2) u(x,t). Shows that the Klein-Gordon equation is solved by a family of solutions including trigonometric, exponential, and Bessel function forms.

## Unique contribution
Unlike the phasor approach, this derivation works in the full time domain and is valid for transient (non-sinusoidal) excitation. The connection to the Klein-Gordon equation is non-obvious and "genius" — it elegantly removes the first-derivative damping term.

## Key concepts
- Telegrapher's PDE: ∂²V/∂x² = LC ∂²V/∂t² + (RC+LG) ∂V/∂t + RGV
- Transformation: F = e^(–kt/2) u(x,t) with k = (RC+LG)/LC
- Klein-Gordon equation: ∂²u/∂t² = a² ∂²u/∂x² + (b + k²/4)u where a = 1/√(LC), b = –RG/LC
- General solutions of Klein-Gordon: trigonometric, exponential, and Bessel function families depending on parameter signs

## Methods / results / takeaways
- The damped wave PDE for V (or I) matches the general second-order hyperbolic PDE form ∂²F/∂t² + k ∂F/∂t = a²∂²F/∂x² + bF.
- Substituting F = e^(–kt/2) u eliminates the first-order time derivative, yielding utt = a²uxx – β²u (Klein-Gordon) where β² = –(b + k²/4).
- Klein-Gordon solutions include cosine/sine in x and t (propagating), exponential growing/decaying, and Bessel functions J0, Y0, I0, K0 for the general case.
- This method is powerful for transient analysis and for understanding the dispersion characteristics of the general lossy line.
