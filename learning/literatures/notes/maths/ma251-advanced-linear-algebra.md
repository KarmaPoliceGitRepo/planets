# MA251 Algebra I: Advanced Linear Algebra (Warwick)

- **Source:** MA251 - Algebra I - Advanced Linear Algebra.pdf
- **Drive link:** https://drive.google.com/file/d/16-T6j1X1ns5wIegnFT2_Y6YaXqFUwo8O/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Derek Holt & Dmitriy Rumynin, University of Warwick (2009)
- **Coverage:** partial (large file ~1.2 MB, extraction truncated)

## Overview
Lecture notes for the Warwick MA251 module, a second-year algebra course building on MA106. The central topic is the Jordan Canonical Form (JCF) of a matrix, with the surrounding theory of minimal polynomial, Cayley-Hamilton theorem, Jordan chains, and applications to difference/differential equations. Also covers inner product spaces, bilinear forms, and dual spaces.

## Unique contribution
The JCF is developed from first principles via the invariant factor decomposition, with the Cayley-Hamilton theorem and minimal polynomial as prerequisites. Applications include computing matrix functions (e.g. matrix exponentials for solving linear ODEs) and long-run behaviour of linear recurrences.

## Key concepts
- Jordan Canonical Form (JCF)
- Cayley-Hamilton theorem
- Minimal polynomial
- Jordan chain and Jordan block
- Invariant factors
- Matrix functions (exp, sin, etc.)
- Inner product spaces
- Bilinear forms
- Dual space
- Difference equations and differential equations (linear)

## Methods / results / takeaways
- Every matrix over C is similar to a matrix in JCF; each Jordan block J(λ, k) has λ on diagonal and 1s on superdiagonal.
- Cayley-Hamilton: every matrix satisfies its own characteristic polynomial p_A(A) = 0.
- Minimal polynomial divides the characteristic polynomial; its factorisation determines the JCF block structure.
- Matrix exponential e^{At} solves the linear ODE system x' = Ax; computed via JCF decomposition.
- For a linear recurrence with characteristic roots, the general solution is a linear combination of terms λ^n * p(n) where p is a polynomial of degree (block size - 1).
