# Smith Chart

**Aliases:** reflection coefficient chart; impedance chart; Smith chart; admittance chart; Y-Smith Chart; Smith Chart rotation

**Definition:** The Smith Chart is a graphical tool that maps the complex normalised impedance plane (z = Z/Z₀) into the unit circle of the complex reflection coefficient plane Γ = (z−1)/(z+1). Constant-resistance circles and constant-reactance arcs overlay the Γ plane, enabling rapid impedance transformations, matching network design, and transmission line analysis without complex arithmetic. Moving toward the generator (source) along a lossless transmission line corresponds to clockwise rotation on the chart at a rate of 2βl rad; a λ/4 section is a 180° rotation. The admittance chart (Y-Smith Chart) is the same chart rotated 180°, used for shunt elements. Resistance and reactance circles correspond to conductance and susceptance on the Y-chart.

**Key relations:**
- [reflection-coefficient](reflection-coefficient.md) — Γ is the Smith Chart coordinate
- [characteristic-impedance](characteristic-impedance.md) — impedances are normalised to Z₀
- [transmission-line](transmission-line.md) — rotation on chart represents travel along the line
- [quarter-wave-transformer](quarter-wave-transformer.md) — λ/4 rotation (180°) on Smith Chart
- [impedance-matching-network](impedance-matching-network.md) — matching network design on Smith Chart
- [standing-wave-ratio](standing-wave-ratio.md) — constant-|Γ| circles give constant VSWR

**Discussed in:**
- [Module 4: Smith Chart](../notes/000-electronics-instructions/module4-smith-chart.md) — construction, use for matching, stub tuning
- [Smith Chart Derivation](../notes/00-general-electronics/smith-chart-derivation.md) — mathematical derivation of circles and arcs
- [Smith Chart Circles](../notes/00-general-electronics/smith-chart-circles.md) — geometric properties; clockwise rotation rule
