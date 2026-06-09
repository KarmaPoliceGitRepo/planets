# Alternatives to the Discrete Fourier Transform

- **Source:** Alternatives to the discrete fourier transdorm - Carnegie Mellon University.pdf
- **Drive link:** https://drive.google.com/file/d/1zxLMuqIvnDoq0anWvw5EJB-8pye40ukD/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Doru Balcan, Aliaksei Sandryhaila, Jonathan Gross, Markus Püschel — Carnegie Mellon University
- **Coverage:** full

## Overview
A conference paper proposing a large family of alternative Fourier transforms, each of which converges to the DTFT as signal length grows, but with different associated signal extensions and convolution operations. The construction uses the algebraic signal processing (polynomial algebra) framework and the Beraha-Kahane-Weiss theorem on the asymptotic zero distribution of polynomial sequences.

## Unique contribution
Proves (via Theorem 1 / Corollary 1) that any polynomial sequence of the form q_n(x) = sum of a_i(x) x^{i*n} has zeros that converge to the unit circle. Each such sequence defines a valid alternative Fourier transform with Vandermonde structure, enabling O(n log^2 n) fast computation. The DFT (from p_n = x^n - 1) is merely one special case.

## Key concepts
- Discrete Fourier Transform (DFT)
- Discrete-time Fourier Transform (DTFT)
- Polynomial algebra C[x]/p(x)
- Vandermonde matrix
- Chinese Remainder Theorem
- Signal extension and boundary condition
- Beraha-Kahane-Weiss theorem
- Algebraic signal processing theory
- Circular convolution vs. general convolution

## Methods / results / takeaways
- Every polynomial algebra C[x]/p_n(x) with pairwise-distinct zeros defines a linear Fourier transform via evaluation at those zeros.
- The DFT arises from p_n = x^n - 1 (zeros = n-th roots of unity on the unit circle; boundary condition = periodic extension).
- Theorem 1: for sequences of the form in eq. (5), the limits of zeros are exactly the unit circle (plus finitely many extra points inside/outside from roots of a_0 and a_k).
- Fast algorithms: all these transforms are Vandermonde matrices; O(n log^2 n) algorithms exist.
- Experimental results confirm spectra converge for n = 80 across four example polynomial families.
