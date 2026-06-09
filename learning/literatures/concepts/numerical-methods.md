# Numerical Methods and Optimisation
**Aliases:** numerical methods; finite difference; finite element method; FEM; optimization; gradient descent; iterative solver; root finding; Newton-Raphson; curve fitting; interpolation; extrapolation; fixed point; MM algorithm; ARMA model identification

**Definition:** Numerical methods approximate the solutions of mathematical problems (ODEs, PDEs, optimisation) that lack closed-form solutions. Finite difference methods replace derivatives by difference quotients on a grid. Finite element methods (FEM) discretise a domain into elements and minimise a weighted residual (Galerkin), producing sparse linear systems. Optimisation algorithms seek minima of objective functions: gradient descent follows the negative gradient; Newton-Raphson uses Jacobian information for faster convergence. Fixed-point iteration solves x = g(x) by repeated application of g. The MM (Majorise-Minimise) algorithm replaces a difficult objective with a simpler surrogate at each iteration.

**Key relations:**
- related: [regularisation](regularisation.md)
- related: [partial-differential-equations](partial-differential-equations.md)
- related: [regression-and-least-squares](regression-and-least-squares.md)

**Discussed in:**
- [Kreyszig Advanced Engineering Mathematics](../notes/maths/kreyszig-advanced-engineering-mathematics.md) — numerical methods chapter: interpolation, finite differences, ODE solvers, root finding
- [Stroud Advanced Engineering Mathematics](../notes/maths/stroud-advanced-engineering-mathematics.md) — worked numerical examples; Newton-Raphson; numerical integration
- [Robust PCA — Temperature and Damage Detection](../notes/signal-processing/robust-pca-temperature-damage-detection.md) — MM algorithm applied to robust PCA optimisation
