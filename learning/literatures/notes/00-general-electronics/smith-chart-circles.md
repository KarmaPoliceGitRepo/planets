# Circles on the Smith Chart

- **Source:** SmithChartCircles.pdf
- **Drive link:** https://drive.google.com/file/d/1PgswwzPU7j7XzZ-dsFSTbnh-p6wmO7nj/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 24, 2013
- **Coverage:** full

## Overview
A short derivation document showing the specific circle equations for constant normalized resistance and constant normalized reactance on the Smith chart, and explaining how the reflection coefficient traces a circle as the observation point moves along a lossless transmission line.

## Unique contribution
Explicitly works out the special cases for zR = 0, 1, ∞ and zI = ±1, ∞ to identify which circles appear as the outer boundary, the unit circle, the center point, and other prominent features of the Smith chart. Also shows that anti-clockwise rotation around the chart corresponds to moving half a wavelength toward the source.

## Key concepts
- Normalized load impedance: zL = ZL/Z0 = zR + jzI
- Constant-resistance circles: center (zR/(1+zR), 0), radius 1/(1+zR)
- Constant-reactance circles: center (1, 1/zI), radius 1/|zI|
- Reflection coefficient Γ = ΓR + jΓI
- Smith chart as a polar plot in the Γ plane
- Points above the real axis: inductive (+jX); below: capacitive (–jX)
- Anti-clockwise rotation = half wavelength travel toward generator

## Methods / results / takeaways
- zR = 0 → |Γ| = 1 (outer boundary, open/short circuit locus).
- zR = 1 → circle centered at (0.5, 0) with radius 0.5 (passes through Γ = 0).
- zR = ∞ → single point at Γ = +1 (open circuit).
- zI = 0 → real axis (purely resistive loads).
- Moving from load toward generator: Γ(z) = Γ0 exp[j2β(z–l)] traces a clockwise circle at constant |Γ|.
- Half-wavelength travel = 2β(z–l) = –2π = one full revolution around the chart.
