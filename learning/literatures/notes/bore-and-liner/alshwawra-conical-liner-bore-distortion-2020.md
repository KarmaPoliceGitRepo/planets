# Enhancing the Geometrical Performance Using Initially Conical Cylinder Liner in Internal Combustion Engines — A Numerical Study

- **Source:** Applied Sciences 10(11), 3705 (2020), doi:10.3390/app10113705
- **Drive link:** https://drive.google.com/file/d/1l4fjTLzQMhyoyq17d6nGlaz73Q-n7gUM/view
- **Type:** paper
- **Author/Year:** Alshwawra, Ahmad; Pohlmann-Tasche, Florian; Stelljes, Frederik; Dinkelacker, Friedrich (Leibniz Universität Hannover) / 2020 (Appl Sci 10(11):3705)
- **Coverage:** full

## Overview
ANSYS FEM numerical study proposing and evaluating a conical (and combined conical-elliptical) cold-state cylinder liner geometry for a Nissan CA18 gasoline engine (83 mm bore, 4-cylinder) to counteract thermal expansion in the fired state. The premise is that upper liner regions expand more than lower regions due to higher combustion heat, producing a taper; an inverse conical cold shape should deform to a straight cylinder when fired. Combined with an elliptical cold cross-section (from prior work) this simultaneously improves roundness. Results: conical liner reduces parallelism error ~3× (from ~12 µm to ~4 µm) and straightness error ~2× (from ~6 µm to ~3 µm); conical-elliptical liner additionally reduces roundness error from ~60–70 µm to ~10–15 µm.

## Unique contribution
First published study combining conical (axial shape correction) with elliptical (circumferential shape correction) cold-state liner geometry design; quantifies improvements to all three geometric indicators (roundness, straightness, parallelism) simultaneously; demonstrates >50% straightness improvement, 60–70% parallelism improvement, and 70–80% roundness improvement vs. standard cylindrical liner at the terminal cylinder.

## Key concepts
- Conical liner: cold-state taper (lower radius +5 µm) derived from inverse of computed cylindrical-liner fired deformation
- Elliptical cold cross-section: counteracts thermally-induced ovality; from prior work (Alshwawra 2019 IJER)
- Geometric indicators: roundness error (least squares circle), straightness error, parallelism error
- Fourier harmonic decomposition: orders 0–4; terminal cylinder shows 3rd-order in addition to 1st, 2nd, 4th due to asymmetric thermal load from adjacent cylinder
- ANSYS mechanical FEM; Nissan CA18 (83 mm × 83.6 mm); grey cast iron block and liner; aluminium head; 4000 rpm full load; validated vs Hitosugi et al. (1996, JSAE) measured data
- Liner thickness 1.6 mm; block clearance 80 µm; bolt pretension 80,000 N; coolant 80°C; wall temps 123–197°C
- Fired deformation up to 30 µm (upper > lower by ~5–7 µm depending on side)
- Parallelism error more directly influences friction than roundness error

## Methods / results / takeaways
- Baseline model: 1.5-cylinder section (terminal + half adjacent); validated against Hitosugi 1996 experimental data for deformation trends and values.
- Fired deformation: upper region always more deformed than lower; difference ~5 µm thrust/anti-thrust, ~7 µm front/rear; causes taper and parallelism error.
- Conical liner design: subtract fired-state deformation from cylindrical cold-state → conical cold shape with 5 µm increment at lower radius.
- Results for conical circular (cold): parallelism error → ~4–5 µm fired (vs ~12–13 µm for cylindrical); straightness → ~2–3 µm fired (vs ~6–7 µm); remaining top-region deviation from bolt pretension.
- Roundness error: conical circular fired → similar to cylindrical circular (60–70 µm); conical elliptical → 10–15 µm (vs 60–70 µm for circular liners).
- Parallelism/straightness independent of cross-section shape (circular vs elliptical); roundness strongly dependent on cross-section.
- Summary: conical liner targets axial shape; elliptical liner targets circumferential shape; combination addresses both.
- Friction implication: reduced parallelism → more uniform oil film → reduced friction; reduced roundness → reduced ring tension needed → reduced ring friction.
- Bore-liner relevance: design methodology for compensatory cold liner geometry to achieve near-ideal cylindrical shape in firing conditions; establishes quantitative benefits of geometric pre-correction for bore distortion reduction.
