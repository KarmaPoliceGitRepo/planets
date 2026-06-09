# The Physical Basis of Dimensional Analysis

- **Source:** dimensionless analysis BOOK.pdf
- **Drive link:** https://drive.google.com/file/d/1XtK89svU1ybaEIK1YKL6eZWxulUaLOxE/view
- **Type:** book
- **Author/Year:** Ain A. Sonin, Department of Mechanical Engineering, MIT; 2001 (2nd edition; 1st edition 1997; distributed in MIT course 2.25 Advanced Fluid Mechanics since 1992)
- **Coverage:** partial (substantial extraction achieved; most of the core theory chapters read)

## Overview
A concise but rigorous MIT course monograph that explains dimensional analysis by tracing it back to its physical and philosophical foundations. Rather than simply presenting Buckingham's π-theorem as a computational recipe, Sonin derives it from first principles: starting with the definition of physical quantities (base vs. derived), the concept of dimension, dimensional homogeneity of physical equations, and the principle of absolute significance of relative magnitudes. The text covers physical quantities and equations, the four-step procedure of dimensional analysis, Buckingham's π-theorem, a detailed worked example (elastic ball impacting a wall), and a chapter on fixed-value independent quantities. The book concludes with cited and selected references.

## Unique contribution
Provides a philosophically grounded, mathematically careful derivation of dimensional analysis that is rare at the introductory level. It explicitly addresses confusions that arise in practice: the dependence of dimension on the choice of unit system, why dimensionless arguments are required for transcendental functions, the distinction between base quantities (physically defined) and derived quantities (numerically defined), and common pitfalls such as incomplete sets of independent variables and superfluous variables. The elastic ball impact example (finding imprint diameter as a function of ball diameter, velocity, density, elastic modulus, and Poisson's ratio) is worked through all four steps in complete detail, reducing 5 variables to 2 dimensionless groups.

## Key concepts
- Physical quantities (base vs. derived)
- Base quantity: comparison operation and addition operation
- Derived quantities of the first kind (power-law combinations of base quantities)
- Derived quantities of the second kind (defined via physical laws, e.g. F = ma)
- Dimension and dimensional homogeneity
- Principle of absolute significance of relative magnitudes
- Physical equations and unit-invariance
- Systems of units (SI, cgs, British Gravitational, British Engineering)
- Buckingham's π-theorem
- Dimensionless variables (Pi groups)
- Dimensionally independent subset
- Inspectional analysis vs. dimensional analysis
- Similarity and scale modeling
- Out-of-scale modeling conditions
- Independent vs. superfluous independent variables
- Fixed-value independent quantities and reduction of Pi groups
- Reynolds number, Froude number (as examples of Pi groups)

## Methods / results / takeaways
- **Physical basis:** A base quantity is defined by two physical operations: (1) a comparison operation (determining equality) and (2) an addition operation (defining what the sum of two samples means). Derived quantities are numeric constructs; their dimensions depend on the choice of unit system, not on any intrinsic physical nature—hence the same physical quantity (e.g. torque and energy) can have the same dimension, and the same physical law can be written with or without dimensional constants depending on the unit system choice.
- **Dimensional homogeneity:** Any physically meaningful equation must be dimensionally homogeneous (invariant under change of base unit sizes). This has three consequences: both sides must have equal dimension; all terms in a sum must share the same dimension; all arguments of transcendental functions must be dimensionless.
- **Four-step procedure:** (1) Identify a complete, independent set of n variables Q₁…Qₙ. (2) List dimensions; pick a complete, dimensionally independent subset Q₁…Qₖ (k ≤ number of base dimensions). (3) Form n−k dimensionless Pi groups by dividing each remaining variable by the appropriate power-product of the independent subset. (4) Express the dependent variable's Pi as a function of the n−k independent Pi groups.
- **π-theorem statement:** When a complete physical relationship is recast in dimensionless form, the number of independent quantities falls from n to n−k, where k is the size of the dimensionally independent subset. This can compress a 5-variable experimental programme into a 2-variable curve.
- **Elastic ball example:** d = f(V, ρ, D, E, ν) → Π₀ = d/D = f(ρV²/E, ν). Choosing {V, ρ, D} as the dimensionally independent subset yields two Pi groups, reducing five experiments-on-variables to a single two-parameter curve.
- **Fixed-value variables:** If some independent quantities are fixed (e.g. Poisson's ratio ν is a fixed material constant, or g is fixed in Earth experiments), those Pi groups drop out, further reducing the problem.
- **Pitfalls:** An incomplete set of independent variables invalidates the analysis; superfluous variables add unnecessary Pi groups; over-simplifying assumptions may exclude genuinely relevant variables.
- **Utility:** Dimensional analysis reveals similarity conditions for scale modeling, minimizes experimental effort, and provides the correct functional form prior to any solving or experimentation.
