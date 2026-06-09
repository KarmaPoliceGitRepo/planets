# Measurements of Surface Texture Using Ultrasound

- **Source:** Gunarathne 2000 surface texture ultrasound
- **Drive link:** https://drive.google.com/file/d/1vetVxCNTHPpq6nYOghy5rJfKeg6h6G29/view
- **Type:** paper
- **Author/Year:** Gunarathne & Christidis, 2000 (IEEE Ultrasonics Symposium 2000, pp. 611–616; later extended to IEEE TIM 50(5), 2002)
- **Coverage:** full

## Overview
Develops an ultrasonic spectroscopic technique to measure a gross "surface texture coefficient" ST for materials. A 5 MHz broadband transducer irradiates a surface in oil at normal incidence. The frequency spectrum of the reflected signal is normalised to a smooth reference; a minimisation algorithm fits the normalised spectrum to a theoretical model (Kirchhoff/McCoy reflection coefficient as a function of ST) to extract ST. Applied to three aluminium reflectors (A, B, C) with different roughnesses and demonstrates good agreement between theoretical and practical results.

## Unique contribution
Introduces the surface texture coefficient ST (3D rms departure of surface profile over a transducer-equivalent disk area) instead of 1D Ra/Rq — acknowledging that the 3D scattered field is not equivalent to a 1D profile measurement. The minimisation-based spectral matching approach avoids single-frequency inversion artefacts. Targets applications including characterisation of mineral/crystalline deposits in pipelines and turbines (not just machined surfaces).

## Key concepts
- Surface texture coefficient ST (3D rms deviation)
- Ultrasonic spectroscopy for surface roughness
- Frequency spectrum of reflected pulse
- Minimisation algorithm (spectral matching)
- 5 MHz broadband transducer, normal incidence, oil immersion
- Kirchhoff reflection coefficient (frequency-dependent)
- 3D scattered field vs. 1D profilometer parameter
- Applications: pipeline deposits, turbine surfaces, automated inspection

## Methods / results / takeaways
- Setup: 5 MHz broadband transducer (12.7 mm diameter); oil immersion tank; normal incidence; target at fixed distance.
- Model: reflection coefficient ratio R_rough/R_smooth at frequency f = exp(−(2πf·ST/c)²) — same form as Kirchhoff with ST replacing Rq.
- Algorithm: FFT of received signal; normalise each frequency component by smooth reference; compute minimisation function FM(ST) = Σᵢ|theoretical(f_i, ST) − measured(f_i)|²; minimum of FM gives best-fit ST.
- Specimens: 3 aluminium reflectors A, B, C with progressively different texture.
- Result: minimisation function shows clear minimum for each target; ST values distinguish all three surfaces; good match between theoretical and measured normalised spectra.
- Limitation: ST is not directly comparable to conventional Ra/Rq (different dimensional scope); no cross-calibration with stylus; oil immersion not compatible with production environment.
- Note: IEEE TIM 2002 paper (same authors, same title, DOI 10.1109/19.963174) is the published journal version; this is the conference precursor.
