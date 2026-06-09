# Impedance Transform: Series-to-Parallel Conversion

- **Source:** ImpedanceTransformSP.pdf (in General Notes folder)
- **Drive link:** https://drive.google.com/file/d/1xOeyRygBq14uo9olLSyn2Ee-ARIqSevM/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, November 24, 2013
- **Coverage:** full

## Overview
Derives the equivalence conditions for converting a series R-L circuit to a parallel R-L circuit (and a series R-C to a parallel R-C) at a given frequency. Shows that the two topologies have different element values but present the same impedance at the conversion frequency.

## Unique contribution
Provides explicit conversion formulas equating real and imaginary parts of Z for both R-L and R-C cases, making the series-to-parallel transformation a straightforward algebraic lookup. This is the foundation of Q-factor-based matching network design.

## Key concepts
- Series impedance: Zs = Rs + jXs
- Parallel impedance: Zp = Rp || jXp → Rp·jXp / (Rp + jXp)
- Q factor of the reactive element
- Series-to-parallel conversion for R-L: RS = RP·ω²L²P/(RP² + ω²LP²), LS = RP²·LP/(RP² + ω²LP²)
- Series-to-parallel conversion for R-C: RS = RP/(ω²CP²RP² + 1), CS = CP(ω²CP²RP² + 1)/ω²CP²RP²

## Methods / results / takeaways
- Rationalize Zp by multiplying by conjugate; then equate ReZs = ReZp and ImZs = ImZp.
- For R-L: the parallel resistance RP and parallel inductance LP can be found from the series RS and LS at a given frequency, and vice versa.
- The conversion is frequency-dependent: the same physical component has different equivalent values in series vs. parallel form at different frequencies.
- In narrowband matching network design, the Q-factor links the series and parallel conversions: Q = XS/RS = RP/XP = √(RP/RS – 1).
