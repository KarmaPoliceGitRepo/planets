# Linear Algebra
**Aliases:** vector space; linear independence; basis; rank-nullity theorem; Cayley-Hamilton theorem; Jordan Canonical Form; minimal polynomial; Vandermonde matrix; eigenvalue; eigenvector; matrix; determinant; inner product; orthogonality; span

**Definition:** A vector space over a field F is a set closed under vector addition and scalar multiplication; a basis is a linearly independent spanning set and its cardinality is the dimension. The rank-nullity theorem states dim(im T) + dim(ker T) = dim(V). Every square matrix A satisfies its own characteristic polynomial (Cayley-Hamilton theorem); the minimal polynomial is the monic polynomial of least degree that annihilates A. The Jordan canonical form is the simplest basis in which a matrix is upper-triangular with eigenvalues on the diagonal and possible 1s on the superdiagonal. A Vandermonde matrix V_{ij} = xⱼ^{i−1} is invertible iff all xⱼ are distinct; it appears in polynomial interpolation and DFT formulations.

**Key relations:**
- related: [tensors](tensors.md)
- related: [regression-and-least-squares](regression-and-least-squares.md)
- related: [fast-fourier-transform](fast-fourier-transform.md)

**Discussed in:**
- [MA106 Linear Algebra](../notes/maths/ma106-linear-algebra.md) — core linear algebra: vector spaces, bases, rank-nullity, determinants, eigenvalues
- [MA251 Advanced Linear Algebra](../notes/maths/ma251-advanced-linear-algebra.md) — Jordan form; minimal polynomial; Cayley-Hamilton; rational canonical form
- [Beardon Algebra & Geometry](../notes/maths/beardon-algebra-geometry.md) — geometric approach; transformations; bilinear forms
- [Foundations of Mathematics (Stewart & Tall)](../notes/maths/foundations-of-mathematics-stewart-tall.md) — axiomatic foundations including vector spaces and field axioms
