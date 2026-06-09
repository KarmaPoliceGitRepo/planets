# Module 8 – Two-Ports and Power Gain

- **Source:** module8 - Two-Ports and Power Gain.pdf
- **Drive link:** https://drive.google.com/file/d/1JwDyqlSnGX-KJ0DVhURzU14CR6qF5ld1/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (26 pages) defining and relating the three RF power gain metrics — operating power gain Gp, available power gain Ga, and transducer gain GT — and deriving the conditions for maximum gain through simultaneous bi-conjugate matching.

## Unique contribution
Provides a clear side-by-side definition of Gp, Ga, and GT with the conditions under which each is maximized, and derives Gmax = |Y21/Y12| · (K − √(K²−1)), making explicit the link between stability and the maximum achievable gain.

## Key concepts
- Operating power gain Gp
- Available power gain Ga
- Transducer gain GT
- Bi-conjugate match
- Maximum available gain (MAG/MSG)
- Unilateral transducer gain GTU
- Rollett stability factor K
- Maximum stable gain (MSG)
- Simultaneous input/output matching
- Power wave formulation

## Methods / results / takeaways
- Gp = P_L/P_in (power delivered to load / power entering the two-port); independent of source impedance.
- Ga = P_avn/P_avs (available output power / available source power); independent of load impedance.
- GT = P_L/P_avs; depends on both source and load; GT ≤ Ga and GT ≤ Gp.
- Maximum GT (bi-conjugate match): simultaneously match input and output ports; requires K > 1 for a unique solution.
- Gmax = |S21/S12| · (K − √(K²−1)) when K > 1 (unconditionally stable); Gmax = MSG = |S21/S12| when K = 1.
- Unilateral approximation (S12 ≈ 0): simplifies matching since input and output are decoupled; error bounded by unilateral figure of merit U.
- Practical implication: maximizing gain by conjugate matching can push a conditionally stable device into oscillation at another frequency; always check stability circles.
