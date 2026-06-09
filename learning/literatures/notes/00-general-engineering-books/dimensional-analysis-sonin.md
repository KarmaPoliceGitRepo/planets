# The Physical Basis of Dimensional Analysis

- **Source:** dimensionless analysis BOOK.pdf
- **Drive link:** https://drive.google.com/file/d/1XtK89svU1ybaEIK1YKL6eZWxulUaLOxE/view
- **Type:** book
- **Author/Year:** Ain A. Sonin, Department of Mechanical Engineering, MIT; 2001 (2nd edition; 1st edition 1997; distributed in MIT course 2.25 Advanced Fluid Mechanics since 1992)
- **Coverage:** full (deep read)

## Overview
A concise (57-page) MIT course monograph that explains dimensional analysis by tracing it back to its physical and philosophical foundations. Rather than presenting Buckingham's π-theorem as a computational recipe, Sonin derives it from first principles starting from the physical definition of base quantities (comparison + addition operations), the principle of absolute significance of relative magnitudes (Bridgman), dimensional homogeneity of physical equations, and the logical consequences of that homogeneity for the form of any physical relationship. Covers: physical quantities (base vs. derived, first and second kind), units and dimensions, dimensional homogeneity, the four-step dimensional analysis procedure, Buckingham's π-theorem, a fully worked example (elastic ball impacting a wall with FEA validation), pitfalls (incomplete sets, superfluous variables, simplifying assumptions), and a generalization for problems with some fixed-value independent quantities.

## Unique contribution
Provides a philosophically grounded, mathematically careful derivation of dimensional analysis, rare at introductory level. Explicitly addresses confusions that arise in practice: why dimension depends on the choice of unit system (not on the quantity's intrinsic nature); why torque and energy can have the same dimension; why only power-law formulas represent derived physical quantities; why arguments of transcendental functions must be dimensionless; and why the result of dimensional analysis is independent of the choice of dimensionally independent subset and of the type of unit system. Chapter 4 proves a generalization of Buckingham's theorem for problems where some independent variables have fixed values, showing that the number of similarity parameters is reduced by (n_F − k_F) rather than trivially by n_F. The elastic ball worked example uses FEA data (Mark Bathe, ADINA 2001) to verify dimensionless collapse of data from three different materials.

## Key concepts
- Physical quantities (base vs. derived)
- Base quantity: comparison operation + addition operation (uniquely defining the property)
- Derived quantities of the first kind (power-law combinations of base quantities, Bridgman's principle)
- Derived quantities of the second kind (defined via physical law by choosing a unit, e.g. F = ma)
- Dimension and dimensional homogeneity
- Principle of absolute significance of relative magnitudes (Bridgman 1931)
- Physical equations and unit-invariance; three consequences of dimensional homogeneity
- Systems of units (SI, British Gravitational, British Engineering); dimension depends on unit system choice
- Buckingham's π-theorem (Buckingham 1914)
- Dimensionless Pi groups; dimensionally independent subset; number k of independent variables
- Inspectional analysis vs. dimensional analysis
- Similarity and scale modeling; out-of-scale modeling conditions
- Incomplete vs. complete set of independent variables; superfluous variables
- Fixed-value independent quantities: generalized π-theorem reducing parameters by (n_F − k_F)
- Reynolds number, Froude number (as examples of Pi groups)

## Methods / results / takeaways

### Physical basis (Chapter 2)
- A **base quantity** is defined by two physical operations: (1) a comparison operation (establishing equality A=B or inequality), and (2) an addition operation (defining C=A+B of same kind). Operations must obey identity, commutativity, associativity, and uniqueness laws. This allows comparison, addition, subtraction, multiplication by pure number, and division by pure number — but NOT products of different base quantities, roots, logs, etc. in purely physical terms
- **Derived quantities of the first kind**: a formula Q = α·A^a·B^b·C^c... satisfies Bridgman's principle (ratio of any two samples remains constant when base units change) if and only if it is a monomial power-law. This is the only valid form for a derived quantity — no other formula represents a physical quantity
- **Dimension**: the formula specifying how a quantity's numerical value changes when base unit sizes change. Same quantity (e.g. force) may have different dimensions in different unit systems; same dimension does not imply same physical nature (e.g. torque and work both have dimension ML²t⁻² in SI)
- **Dimensional homogeneity** (three constraints): (1) both sides of any physical equation must have the same dimension; (2) all terms in a sum must share the same dimension; (3) all arguments of transcendental functions must be dimensionless
- **Derived quantities of the second kind**: formed by choosing a force unit such that F = ma (not F = cma), making force a derived quantity of dimension MLt⁻². This does not mean force "is" mass times acceleration physically — it simply means the force unit is defined in terms of mass, length, and time units
- **Systems of units**: SI has 6 base quantities (length, time, mass, temperature, current, amount of substance, luminous intensity). In British Gravitational System (force, length, time as base), mass becomes derived (dimension Ft²L⁻¹, unit = slug = 32.2 lbm). In British Engineering System (all four: mass, length, time, force as base), Newton's law is F = cma where c = 1/32.2 lbf·s²·lbm⁻¹·ft⁻¹
- Key insight: the dimension of a derived quantity is a formula, not an "intrinsic nature." Two physically different quantities (torque and energy) can have the same dimension; a quantity can have different dimensions in different systems of units

### Four-step procedure (Chapter 3, Section 3.1)
1. **Step 1**: Identify a complete, independent set of n variables Q₁...Qₙ that determine Q₀. "Complete" means specifying all of them uniquely determines Q₀; "independent" means each can be varied without affecting the others. This is the most critical step — an incomplete set destroys the analysis
2. **Step 2**: List dimensions; identify a complete, dimensionally independent subset Q₁...Q_k (k ≤ number of base dimensions). Express dimensions of all remaining variables and Q₀ as products of powers of Q₁...Q_k (Eq. 3.3): [Q_i] = [Q₁^{N_{i1}} · Q₂^{N_{i2}} · ... · Q_k^{N_{ik}}]. Exponents N_{ij} found by inspection or by solving the linear system Eq. 3.4
3. **Step 3**: Form n−k dimensionless Pi groups (Eqs. 3.5, 3.6): Π_i = Q_{k+i} / (Q₁^{N_{k+i,1}} · ... · Q_k^{N_{k+i,k}}) for i=1,...,n−k, and Π₀ = Q₀/(Q₁^{N₀₁}...Q_k^{N₀k})
4. **Step 4**: By dimensional homogeneity, the dimensionally independent subset Q₁...Q_k must drop out of the relationship (Eq. 3.8): **Π₀ = f(Π₁, Π₂, ..., Π_{n-k})**. This is Buckingham's π-theorem: number of independent quantities reduced from n to n−k

### Elastic ball impact example (Section 3.2, Table 3.1)
- Dependent variable: imprint diameter d of a dyed elastic ball after impact with rigid wall
- Independent variables (n=5): D (ball diameter), V (impact speed), ρ (ball density), E (elastic modulus), γ (Poisson's ratio)
- Note: m (mass) is excluded because it is not independent of ρ and D; including both would be a superfluous variable error
- Dimensionally independent subset (k=3): {V, ρ, D} with dimensions Lt⁻¹, ML⁻³, L
- Pi groups (n−k=2): Π₁ = E/(ρV²), Π₂ = γ (already dimensionless)
- Result: d/D = f(E/(ρV²), γ)
- FEA validation (Table 3.1): data for alumina, aluminum, rubber with widely varying E, ρ, V collapse onto a single curve in d/D vs. E/(ρV²) space, with only slight γ dependence (from 0.22 to 0.47); confirms dimensional analysis
- Alternate subset {V, E, ρ} gives equivalent result (Eq. 3.18–3.19): confirms independence from choice of subset
- British Engineering System adds c (from F=cma) as an additional variable (n=6, k=4, n−k=2): same two Pi groups after incorporating c into E non-dimensionalization (Eq. 3.23); confirms independence from unit system type

### Pitfalls (Section 3.3)
- **Incomplete set**: omitting E gives d/D = f(γ) — independent of elasticity, mass, and velocity; clearly wrong
- **Superfluous variables**: adding g (gravity) gives extra Pi group gD/V²; not wrong, but wastes effort; only realized superfluous by experiment or physical insight
- **Simplifying assumptions**: completeness is relative to the scope of the problem; "g is irrelevant" is a deliberate, testable assumption; dimensional analysis cannot self-certify assumptions
- **Choosing the subset**: any complete, dimensionally independent subset gives the same result (proven via re-normalization, Eqs. 3.18–3.19)
- **Choice of unit system**: does not affect the final physical content; only the algebraic form of some Pi groups changes

### Fixed-value generalization (Chapter 4)
- If n_F of the n independent variables have fixed values in all cases of interest, and k_F of these are dimensionally independent, then the effective number of free similarity parameters is reduced from n−k to **(n−k) − (n_F − k_F)**
- Cable drag example: n=5 variables (L, d, V, ρ, μ); n_F=2 (ρ, μ fixed for sea water); k_F=2 (ρ and μ are dimensionally independent); reduction = (n_F − k_F) = 0. No simplification occurs because both fixed quantities are dimensionally independent
- Simplification only occurs when some fixed quantities are dimensionally dependent on the others (k_F < n_F); e.g. if Poisson's ratio γ were fixed (n_F=1, k_F=0), the elastic ball result would reduce to d/D = f(E/ρV²) with only one parameter
- The proof: dimensional analysis is performed on the set {variable quantities} ∪ {dimensionally independent subset of fixed quantities}, giving Eq. 4.6–4.7

## Figures

- **Fig. 2.1a** (p. 12): Cartoon showing the comparison and addition operations of **length**. Left panel: two vertical bars A and B shown side by side under a ruler to compare lengths (L_A = L_B). Right panel: A and B placed end-to-end; B then displaced to form C, with C = A+B (L_A + L_B = L_C). Simple, intuitive illustration of what "addition of lengths" physically means.

- **Fig. 2.1b** (p. 12): Cartoon showing comparison and addition of **mass** using a balance. Left: masses A and B on opposite pans of a balance in equilibrium (M_A = M_B). Right: A and B on same pan balanced against C (M_A + M_B = M_C). Gravitational mass comparison via balance pan.

- **Fig. 2.2** (p. 16, referenced): Measuring in terms of a unit — replicas of a unit and fractions placed end-to-end until equal to the quantity being measured; the count is the numerical value. Conceptual illustration of measurement as a physical process.

- **Fig. 3.1** (p. 39): Schematic of the elastic ball impact example. A spherical ball of diameter D moving at velocity V strikes a rigid flat wall; the circular imprint left on the wall has diameter d. Labels indicate D, V, d. Clean two-part diagram: ball approaching (left) and imprint result (right).

- **Fig. 3.2** (p. 44–45, Table 3.1 + plot): "Experimental" (FEA-computed) data for impacting balls — d/D plotted vs. E/(ρV²) — for three materials (alumina: E=366 GPa, ρ=3960 kg/m³; aluminum: E=69 GPa, ρ=2705 kg/m³; rubber: E=3.93 MPa, ρ=1060 kg/m³) with varying impact velocities and Poisson's ratios γ=0.22, 0.33, 0.47. All data points fall on a common curve in dimensionless form, confirming the similarity collapse predicted by dimensional analysis. The effect of γ is small given computational scatter; data approximately follow a single d/D vs. E/ρV² function.

- **Equations display** (p. 37): Explicit form of Steps 3–4: Π_i = Q_{k+i}/(Q₁^{N_{(k+i)1}}·Q₂^{N_{(k+i)2}}·...·Q_k^{N_{(k+i)k}}) and the final Buckingham result Π₀ = f(Π₁, Π₂, ..., Π_{n-k}) shown typeset in full, confirming the reduction from n to n−k variables.

- **Eqs. 3.18–3.19** (p. 48): Alternate formulation of the elastic ball result using {V, E, ρ} as independent subset instead of {V, D, ρ}; algebraically rewritten to show identity with original Eq. 3.13, confirming subset-independence of the result.

- **Table 2.1** (p. 29–30): Full SI system table: 7 base quantities (length, time, mass, temperature, current, amount, luminous intensity) with units; partial derived quantity table showing area, volume, frequency, velocity, acceleration, density, force, stress/pressure, work/energy, torque, power, charge — with defining equations, dimensions, SI units.

- **Table 2.2** (p. 31): Dimensions of mechanical quantities in three unit-system types: Type 1 (L, M, t base), Type 2 (L, F, t base — British Gravitational), Type 3 (L, M, F, t base — British Engineering). Shows how same quantity (e.g. mass) has dimension M in Type 1, Ft²L⁻¹ in Type 2, M in Type 3; force has dimension MLt⁻² in Type 1, F in Types 2 and 3; viscosity has dimension ML⁻¹t⁻¹ vs. FL⁻²t in the different systems.
