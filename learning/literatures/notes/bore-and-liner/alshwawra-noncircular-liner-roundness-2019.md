# Increasing the Roundness of Deformed Cylinder Liner in Internal Combustion Engines by Using a Non-Circular Liner Profile

- **Source:** International Journal of Engine Research (IMechE), DOI: 10.1177/1468087419893897 (Epub 2019, published 2020)
- **Drive link:** https://drive.google.com/file/d/1qQR_fz_LOP-VjAgxNNDtffkJM2B2j2gR/view
- **Type:** paper
- **Author/Year:** Alshwawra, Ahmad; Pasligh, Henning; Hansen, Hauke; Dinkelacker, Friedrich (Leibniz Universität Hannover) / 2019 (Int J Engine Res; Epub 2019, online Dec 2019)
- **Coverage:** full

## Overview
ANSYS FEM study investigating the use of non-circular cold-state cylinder liner profiles (elliptical, half-circle-half-ellipse, non-symmetrical ellipse) to counteract thermally-induced bore distortion in a Nissan CA18 gasoline engine (83 mm bore, 4000 rpm full load). The hypothesis is that a liner with inverse-deformation cold-state cross-section will deform toward a circular shape under fired thermal and mechanical loads. Results: elliptical (EL) cold profile reduces roundness deviation by 75–85% (from ~59–60 µm to ~8–15 µm in fired state). Precursor to the combined conical-elliptical study (Alshwawra et al. 2020, Appl Sci).

## Unique contribution
First published study to validate the non-circular cold-state liner approach against experimental Hitosugi et al. (JSAE 1996) fired deformation data for a Nissan CA18; demonstrates that a simple elliptical cold profile achieves 75–85% roundness improvement in the fired state at the terminal cylinder; shows HCE and NSE profiles are less effective than full ellipse.

## Key concepts
- Non-circular cold-state liner profiles: EL (elliptical, 60.5 µm cold deviation), HCE (half-circle half-ellipse, 19 µm), NSE (non-symmetrical ellipse, 19 µm)
- Inverse-deformation approach: cold shape = -(fired deformation of circular liner) → fired shape ≈ circular
- ANSYS FEM; Nissan CA18 (83 mm bore, 83.6 mm stroke); cast iron block + liner, aluminium head; 4000 rpm full load
- Boundary conditions: inner wall 130°C; outer block = 80°C (coolant); bolt pretension 80,000 N; top deck restrained axially
- Grid independence: ~200,000 nodes selected; direct coupled thermal-mechanical solve
- Roundness error metric: least-squares circle → roundness deviation = max(R_circumscribed − R_inscribed)
- Terminal cylinder: highest deformation due to asymmetric thermal load from adjacent cylinder; up to 30 µm
- Circular liner fires to ~58–60 µm roundness error; EL liner fires to 8–15 µm
- HCE and NSE: only 25–30% improvement (40–48 µm fired roundness)
- Non-circular cross-section change does not alter deformation value or pattern significantly → additive correction

## Methods / results / takeaways
- 1.5-cylinder model (terminal + half adjacent) to capture asymmetric thermal effects.
- Validated against Hitosugi et al. 1996 experimental deformation at 10 mm and 90 mm from top; good trend and value agreement.
- All three non-circular profiles reduce roundness error vs circular baseline in fired state.
- EL: 59.8 µm → 15.3 µm at 10 mm, 8.1 µm at 90 mm (75–85% reduction).
- HCE: ~40–42 µm fired (25–30% reduction); NSE: ~45–48 µm fired (similar to HCE).
- EL gives higher-order residual deformation in fired state (not purely circular) but significantly lower deviation amplitude.
- Maximum deviation for EL in fired state at rear side due to adjacent-cylinder temperature gradient.
- Key finding: deformation value and pattern are approximately independent of cold-state cross-section shape → correction is additive → cold profile selection can target fired shape directly.
- Bore-liner relevance: establishes feasibility of non-circular liner geometry for bore distortion compensation; quantifies roundness improvement; basis for the more complete conical-elliptical study (Appl Sci 2020).
