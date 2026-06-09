# Robust PCA
**Aliases:** robust PCA; RPCA; principal component analysis; low-rank plus sparse decomposition; MM algorithm; Orthogonal Matching Pursuit; OMP

**Definition:** Robust PCA decomposes a data matrix M into a low-rank component L and a sparse component S: M = L + S, solved via convex relaxation (minimise nuclear norm of L plus L1 norm of S). Unlike classical PCA, it tolerates a fraction of arbitrarily corrupted entries. In structural health monitoring, the low-rank component captures temperature-driven baseline variation (which is approximately rank-1 or rank-2), while the sparse component isolates structural damage. The MM (Majorise-Minimise) algorithm is a general iterative framework for optimising difficult objective functions by replacing them with simpler surrogates.

**Key relations:**
- related: [structural-health-monitoring](structural-health-monitoring.md)
- related: [temperature-compensation](temperature-compensation.md)
- related: [regularisation](regularisation.md)

**Discussed in:**
- [Robust PCA — Temperature and Damage Detection](../notes/signal-processing/robust-pca-temperature-damage-detection.md) — applies RPCA to separate temperature and damage signals in guided-wave SHM; MM algorithm for optimisation
