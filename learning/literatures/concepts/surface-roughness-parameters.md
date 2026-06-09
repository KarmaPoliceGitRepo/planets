# Surface Roughness Parameters
**Aliases:** Ra; Rq; Rz; Rsk; Rku; roughness average; RMS roughness; mean peak-to-valley height; skewness; kurtosis; surface texture; waviness; profilometry; Gaussian filter; cutoff wavelength; ISO 4287; ISO 13565

**Definition:** Surface roughness parameters quantify the deviation of a real surface from an ideal smooth form. Ra (arithmetic mean roughness) is the most common: mean absolute deviation from the mean line. Rq (RMS roughness, σ) is the standard deviation of heights; for Gaussian surfaces Rq ≈ 1.25 Ra. Rz (mean peak-to-valley) is more sensitive to outlier peaks and valleys. Rsk (skewness) describes asymmetry: negative for plateau-honed/ground surfaces (more valleys than peaks relative to mean). Rku (kurtosis) measures peakedness. Parameters are computed after filtering with a Gaussian (ISO 11562) or robust filter at a specified cutoff wavelength (λc). Waviness (W-parameters) uses a longer cutoff.

**Key relations:**
- [plateau-honing-parameters](plateau-honing-parameters.md)
- [asperity-contact](asperity-contact.md)
- [surface-metrology](surface-metrology.md)
- [film-thickness](film-thickness.md)
- [contact-mechanics](contact-mechanics.md)

**Discussed in:**
- [Surface Roughness Analysis — Bhushan](../notes/00-general-engineering-books/surface-roughness-analysis-bhushan.md) — comprehensive treatment of 2D/3D parameters, filtering, instruments
- [Malburg — Cylinder Bore Surface Texture](../notes/honing/malburg-cylinder-bore-surface-texture.md) — Ra, Rz, and plateau-hone Rk parameters for honed bores; robust filter recommendation
- [Saniman 2020 — Ultrasonic Roughness (Non-Gaussian)](../notes/grinding/saniman-2020-ultrasonic-roughness-non-gaussian.md) — Rsk and Rku characterisation of ground/non-Gaussian surfaces via ultrasonic scattering
- [Recent Trends Surface Metrology — Mathia](../notes/99-other-relevant-papers/recent-trends-surface-metrology-mathia.md) — overview of emerging 3D surface parameters and AFM, white-light interferometry
