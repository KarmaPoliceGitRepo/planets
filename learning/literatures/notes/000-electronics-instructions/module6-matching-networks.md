# Module 6 – Matching Networks

- **Source:** module6 - Matching Networks.pdf
- **Drive link:** https://drive.google.com/file/d/1ny9Ee58mx8nMVnZFPHdjC10wDpggka7P/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (33 pages) on the design of passive impedance matching networks. Covers L-match, Π-match, and T-match topologies, insertion loss due to finite component Q, multi-section matching for bandwidth improvement, and the tapered transmission line as the continuous limit.

## Unique contribution
Derives the insertion loss formula IL = 1/(1 + Q_loaded/Q_components) explicitly and shows how multi-section networks reduce Q per section, lowering loss and widening bandwidth — a quantitative design guide not always presented in this level of detail in RF textbooks.

## Key concepts
- L-match network
- Π-match network
- T-match network
- Insertion loss (IL)
- Component Q (inductor Q)
- Loaded Q
- Multi-section matching
- Bandwidth vs. Q trade-off
- Tapered transmission line
- Impedance transformation ratio

## Methods / results / takeaways
- L-match transforms Z_S to Z_L using two reactive elements; Q = √(Z_S/Z_L − 1) for Q > 1 transformations; bandwidth ∝ 1/Q.
- Insertion loss due to finite inductor Q_c: IL ≈ 1/(1 + Q_L/Q_c); to minimize IL, keep Q_L << Q_c by using low transformation ratios per section.
- Π-match and T-match each have an extra degree of freedom, allowing independent control of Q (and thus bandwidth) for a given transformation ratio.
- Multi-section (cascaded L-match) networks: each section transforms by a smaller ratio, so Q per section is lower and total insertion loss is reduced.
- Binomial and Chebyshev tapers provide optimized wideband matching with controlled ripple.
- Tapered T-line is the distributed limit of many cascaded L-sections; practical at microwave frequencies where lumped inductors are lossy.
- Practical rule: for high-ratio matching (e.g., PA output), use 3–5 sections; each section's Q should be kept below ≈ 3 to minimize loss.
