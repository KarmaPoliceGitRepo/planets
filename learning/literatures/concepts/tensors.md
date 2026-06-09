# Tensors and Index Notation
**Aliases:** tensor; 2nd rank tensor; second-order tensor; 4th rank tensor; fourth-order tensor; Einstein summation convention; Kronecker delta; Levi-Civita tensor; dyadic product; double dot product; Voigt notation; stress tensor; velocity gradient tensor; metric tensor; Christoffel symbols; covariant derivative; Riemann curvature tensor; anisotropy; crystal preferred orientation

**Definition:** A tensor of rank n is a multilinear map whose components transform as T'_{i₁…iₙ} = A_{i₁j₁}…A_{iₙjₙ} T_{j₁…jₙ} under a change of basis (rotation matrix A). The Einstein summation convention implies summation over any repeated index; the Kronecker delta δᵢⱼ acts as the identity; the Levi-Civita tensor εᵢⱼₖ encodes the cross product and determinant. The dyadic (outer) product of two vectors gives a rank-2 tensor; the double-dot (full contraction) of two rank-2 tensors gives a scalar. Voigt notation compresses symmetric rank-4 elastic tensors into 6×6 matrices. The 4th-rank elastic stiffness tensor C_{ijkl} connects stress σᵢⱼ to strain εₖₗ via Hooke's law; symmetry reduces 81 independent components to at most 21. Covariant derivatives and Christoffel symbols extend derivatives to curved spaces; the Riemann curvature tensor measures intrinsic curvature.

**Key relations:**
- related: [vector-calculus](vector-calculus.md)
- related: [partial-differential-equations](partial-differential-equations.md)

**Discussed in:**
- [Tensors and Anisotropic Rocks](../notes/maths/tensors-anisotropic-rocks.md) — physical tensor definitions; 2nd and 4th rank examples; Voigt notation; crystal preferred orientation
- [Brannon Tensor Analysis (UoU)](../notes/maths/brannon-tensor-analysis-uou.md) — rigorous index-notation treatment; Einstein convention; Kronecker delta; Levi-Civita; Voigt
- [Brannon Tensor Analysis](../notes/maths/brannon-tensor-analysis.md) — expanded tensor calculus text; covariant/contravariant components; metric tensor
- [Grinfeld Tensor Analysis](../notes/maths/grinfeld-tensor-analysis.md) — tensor analysis for continua; Christoffel symbols; covariant derivative; Riemann curvature
- [Heinbockel Tensor Calculus](../notes/maths/heinbockel-tensor-calculus.md) — applied tensor calculus with worked examples; coordinate systems
- [Vector and Tensor Mathematics](../notes/maths/vector-tensor-mathematics.md) — concise reference sheet: dyadic product, double-dot product, index notation identities
- [Tensors Handout (CBE 6333)](../notes/maths/tensors-handout-cbe6333.md) — engineering-oriented tensor notation; stress and velocity gradient tensors
