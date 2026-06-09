# Low-Loss Transmission Line

- **Source:** LowLossTL.pdf
- **Drive link:** https://drive.google.com/file/d/1Yh0hei-7YRinVzH1ZpWsv0Chw3IWY1Zl/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 15, 2013
- **Coverage:** full

## Overview
A derivation note applying the low-loss approximation (R ≪ ωL, G ≪ ωC) to the general transmission-line propagation constant. Uses Taylor series expansion to simplify γ into approximate closed-form expressions for α (attenuation) and β (phase constant), and then derives the power loss along a low-loss line.

## Unique contribution
Provides an explicit derivation of the widely used approximate formulas α ≈ (1/2)(R√(C/L) + G√(L/C)) and β ≈ ω√(LC) for a low-loss line, and then works out the power balance showing PIN – PLoad = Ploss.

## Key concepts
- Low-loss condition: R ≪ ωL, G ≪ ωC
- Taylor expansion: √(1+x) ≈ 1 + x/2 for x ≪ 1
- Attenuation constant: α ≈ (1/2)(R√(C/L) + G√(L/C))
- Phase constant: β ≈ ω√(LC) (same as lossless case)
- Power on a lossy line with reflection: Pav = (|V0+|²/2Z0){e^(2αl) – |Γ|²e^(–2αl)}

## Methods / results / takeaways
- Under the low-loss condition, the square root in γ = √((R+jωL)(G+jωC)) factors as jω√(LC) × √(1 + R/(jωL) + G/(jωC)) ≈ jω√(LC)(1 + (R/jωL + G/jωC)/2).
- This gives α ≈ (R/2)√(C/L) + (G/2)√(L/C) and β ≈ ω√(LC).
- The velocity vp = ω/β = 1/√(LC) is the same as for a lossless line.
- Power loss Ploss = PIN – PLoad = (|V0+|²/2Z0) × {e^(2αl) – 1 + |Γ|²(1 – e^(–2αl))}, showing how both forward-wave attenuation and reflected-wave attenuation contribute.
