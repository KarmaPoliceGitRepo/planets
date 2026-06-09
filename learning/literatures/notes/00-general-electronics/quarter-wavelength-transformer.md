# Quarter-Wavelength Transformer

- **Source:** QuarterWavelength.pdf
- **Drive link:** https://drive.google.com/file/d/1xTpiRTE0giaPvdOiHYHJa1JlPG9cE7ak/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 24, 2013
- **Coverage:** full

## Overview
A one-page derivation of the quarter-wave impedance transformer technique, showing how inserting a λ/4 transmission line section with chosen characteristic impedance Z' eliminates reflections between a source impedance Z0 and a real load ZL.

## Unique contribution
Provides the minimal clean derivation: starting from the general lossless input impedance formula, takes the limit as βl → π/2 (quarter wavelength), and arrives at the matching condition Z' = √(Z0 · ZL).

## Key concepts
- Quarter-wave transformer: ZIN = Z'² / ZL
- Matching condition: Z' = √(Z0 · ZL)
- Reflection coefficient Γ = (ZL – Z0) / (ZL + Z0)
- Match condition: Γ = 0 ↔ ZL = Z0
- Phase constant β = 2π/λ

## Methods / results / takeaways
- When βl = π/2 (l = λ/4), tan(βl) → ∞ and the general formula ZIN = Z' × (ZL + jZ' tan βl)/(Z' + jZL tan βl) simplifies to ZIN = Z'²/ZL.
- To achieve ZIN = Z0 (match condition at the source), the transformer impedance must be Z' = √(Z0 · ZL).
- This technique works for any real load ZL but requires a different Z' for each frequency, so it is inherently narrowband.
- It is the basis for the Collin broadband quarter-wave transformer designs and the Chebyshev stepped-impedance transformer.
