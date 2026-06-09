# Green's Function
**Aliases:** Green's function; fundamental solution; impulse response; propagator; influence function

**Definition:** The Green's function G(x, x') of a linear differential operator L is the solution to LG = δ(x − x'), where δ is the Dirac delta. By superposition, the solution to Lu = f is u(x) = ∫ G(x, x') f(x') dx'. Green's functions are the continuum analogue of the matrix inverse; they encode all modes of a system. For the wave equation, G is the retarded propagator describing causal wave emission. In ultrasonic modeling, Green's functions describe the response of a medium to a point force source, forming the foundation of elastodynamic boundary-element methods.

**Key relations:**
- related: [partial-differential-equations](partial-differential-equations.md)
- related: [transfer-function](transfer-function.md)
- related: [fourier-transform](fourier-transform.md)

**Discussed in:**
- [Linear PDE (Myint-U)](../notes/maths/linear-pde-myint-u.md) — Green's function method for boundary-value problems; examples for Laplace and wave equations
- [Kreyszig Advanced Engineering Mathematics](../notes/maths/kreyszig-advanced-engineering-mathematics.md) — Green's function as generalised solution to linear ODEs; Sturm-Liouville theory
