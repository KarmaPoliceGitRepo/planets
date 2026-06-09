# MIT 1.050: A New Introduction to Engineering Mechanics I (Course Notes, Chapters 1–7)

- **Source:** Course Notes Chapter 1–7 1.050.pdf (7 separate files in subfolder)
- **Drive link:** https://drive.google.com/drive/folders/1_1JTLWFuV1zxkdRbVRkfFiR6omO6lpxr
- **Type:** notes
- **Author/Year:** Franz-Josef Ulm (MIT), Fall 2009 Edition
- **Coverage:** full (all seven chapters read; each chapter is an individual PDF)

## Overview
Course notes for MIT 1.050 "A New Introduction to Engineering Mechanics I" by Prof. Franz-Josef Ulm. The course takes an unusual, thermodynamically grounded approach to engineering mechanics — using dimensional analysis, energy methods, and thermodynamics as the organising principles rather than force equilibrium alone. Seven chapter-files cover the full course arc from dimensional analysis through stability and fracture.

## Unique contribution
Distinctive pedagogical structure: begins with dimensional analysis and scaling laws (Galileo's monster problem, atomic explosion similarity), then develops stress and strength, deformation and strain, elasticity (energy approach via thermodynamics), energy bounds (foundational to FEM), and finally failure mechanisms (buckling, fracture, plastic collapse). Unusually rigorous thermodynamic motivation for elasticity — Helmholtz free energy and Clausius-Duhem inequality are used to derive constitutive relations rather than simply postulating Hooke's law.

## Key concepts
**Chapter 1 (Dimensional Analysis):**
- Buckingham Pi theorem
- Physical similarity
- Galileo's problem (animal bone cross-section scaling)
- Atomic explosion blast radius estimation
- Metabolic rate scaling (Barenblatt)

**Chapter 2 (Stress and Equilibrium):**
- Stress vector (traction) and Cauchy stress tensor
- Equilibrium equations (∂σ_ij/∂x_j + b_i = 0)
- Boundary conditions (static and kinematic)
- Moment equilibrium → stress tensor symmetry

**Chapter 3 (Strength Models):**
- Strength as a material threshold for stress
- Mohr-Coulomb strength criterion (cohesion + friction)
- Drucker-Prager criterion
- Failure envelopes in principal stress space
- Load-bearing capacity analysis

**Chapter 4 (Strain and Kinematics):**
- Strain gauge measurement
- Strain tensor (linearised): ε_ij = ½(∂u_i/∂x_j + ∂u_j/∂x_i)
- Compatibility conditions
- Rigid body motion (rotation vs. deformation)

**Chapter 5 (Elasticity: Energy Approach):**
- Thermodynamics of reversible processes (1st + 2nd laws)
- Helmholtz free energy density ψ
- State equations: σ_ij = ∂ψ/∂ε_ij
- Linear elasticity: ψ = ½λ(tr ε)² + με:ε (isotropic)
- Hooke's law derived from energy
- Lamé constants: E = μ(3λ+2μ)/(λ+μ), ν = λ/[2(λ+μ)]

**Chapter 6 (Energy Bounds):**
- Complementary energy and strain energy
- Minimum potential energy (displacement approach — upper bound)
- Minimum complementary energy (stress approach — lower bound)
- Virtual work principle
- Basis for finite element method

**Chapter 7 (Failure: Stability, Fracture, Collapse):**
- Buckling (elastic stability) — bifurcation at loss of convexity of potential energy
- Euler buckling: P_cr = π²EI/L²
- Fracture — Griffith energy release rate G; Irwin's K_I; fracture when G = G_c
- Plastic collapse — upper-bound mechanism analysis; work equation

## Methods / results / takeaways
- Dimensional analysis framework: any physical law f(Q₁,...,Q_n) = 0 with k fundamental dimensions can be reduced to a relation among n−k dimensionless groups (Pi theorem).
- Energy approach to elasticity: the state equations σ = ∂ψ/∂ε replace Hooke's law and naturally encode material symmetry; anisotropic materials described by up to 21 independent constants.
- Energy bounds (Ch.6): the finite element stiffness method provides an upper bound on stiffness (under-predicts compliance); stress-based methods provide a lower bound — bracketing the true solution.
- Fracture: crack propagates when potential energy released per unit crack area equals surface energy Γ_s. K_I = σ√(πa)·f(geometry); K_IC is the material fracture toughness.
- Plastic collapse: yield at critical cross-sections forms plastic hinges; the collapse load is bounded from above by the kinematic (mechanism) theorem: W_ext = W_int along any admissible collapse mechanism.
- Teaching note: this course is unusual in presenting Newton's laws of equilibrium before Hooke's law — treating strength as prior to stiffness in the logical ordering.
