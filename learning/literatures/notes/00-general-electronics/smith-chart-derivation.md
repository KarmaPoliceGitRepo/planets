# Smith Chart Derivation

- **Source:** SmithChartDerivation.pdf
- **Drive link:** https://drive.google.com/file/d/1-vrl21frk0ZpL6PBwKUBVn60pfeFMTK0/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 15, 2013 (updated October 28, 2014; credits Phillip H. Smith 1905–1987)
- **Coverage:** full

## Overview
A step-by-step algebraic derivation showing how the normalized load impedance zL = zR + jzI maps to two families of circles in the complex Γ plane, forming the Smith chart. Both the constant-resistance circles and the constant-reactance circles are derived by completing the square.

## Unique contribution
Shows the algebra behind the Smith chart from first principles, making it clear that the Smith chart is simply a conformal mapping of the impedance half-plane onto the unit disk in the Γ plane, with circles mapping to circles.

## Key concepts
- Normalized load impedance: zL = ZL/Z0, Γ = (zL–1)/(zL+1)
- Expressing zL in terms of ΓR and ΓI
- Constant-resistance circle: center (zR/(1+zR), 0), radius 1/(1+zR)
- Constant-reactance circle: center (1, 1/zI), radius 1/|zI|
- Completing the square technique

## Methods / results / takeaways
- Starting from zL = (1+Γ)/(1–Γ), rationalize to get zR and zI in terms of ΓR and ΓI.
- The equation for constant zR rearranges (by completing the square) to (ΓR – zR/(1+zR))² + ΓI² = (1/(1+zR))², a circle centered at (zR/(1+zR), 0) with radius 1/(1+zR).
- The equation for constant zI rearranges to (ΓR – 1)² + (ΓI – 1/zI)² = (1/zI)², a circle centered at (1, 1/zI) with radius 1/|zI|.
- All resistance circles pass through Γ = +1 (open circuit) and the reactance circles all pass through Γ = +1 as well.
- The result is the familiar Smith chart pattern: resistance circles decrease in size toward the right; reactance arcs are tangent to the outer circle.
