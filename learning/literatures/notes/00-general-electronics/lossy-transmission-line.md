# Lossy Transmission Line

- **Source:** LossyTL.pdf
- **Drive link:** https://drive.google.com/file/d/11tMwL2LwyPQoguCbCEVbxfakTR1jmPYL/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 15, 2013
- **Coverage:** full

## Overview
A derivation note giving the input impedance formula for a general lossy transmission line (α ≠ 0), showing that it differs from the lossless case by replacing tan(βz) with tanh(γz) where γ = α + jβ.

## Unique contribution
Demonstrates how the general lossy input impedance Z0·(ZL + Z0 tanh γl)/(Z0 + ZL tanh γl) reduces from the same Γ-based formalism used in the lossless case, making the connection between the lossless (tan) and lossy (tanh) formulas explicit.

## Key concepts
- Complex propagation constant: γ = α + jβ, α ≠ 0
- Lossy reflection coefficient: Γ(z) = (V0–/V0+) e^(2γz) = |Γ| e^(2αz) e^(j2βz)
- Input impedance: ZIn(–l) = Z0·(ZL + Z0 tanh γl)/(Z0 + ZL tanh γl)
- Hyperbolic functions: cosh and sinh replace cos and sin from the lossless case

## Methods / results / takeaways
- The key distinction from lossless: Γ(z) grows exponentially with e^(2αz) toward the source, so |Γ| is not constant along a lossy line.
- The input impedance derivation parallels the lossless case but uses e^(–γz) ± e^(γz) → 2 cosh / 2 sinh, yielding the tanh form.
- At z = –l (input to line of length l): ZIn = Z0·(ZL + Z0 tanh γl)/(Z0 + ZL tanh γl).
- As α → 0, tanh(γl) → j tan(βl), recovering the lossless result.
