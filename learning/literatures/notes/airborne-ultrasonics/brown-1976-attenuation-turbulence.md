# On the Attenuation of Sound by Turbulence

- **Source:** Brown 1976 attenuation turbulence
- **Drive link:** https://drive.google.com/file/d/1M5MyFwVfAPEOdOYqJxONHbopDDKdDltp/view
- **Type:** paper
- **Author/Year:** Brown & Clifford, 1976 (Journal of the Acoustical Society of America, 60(4), 788–794)
- **Coverage:** full

## Overview
Presents a theory for excess attenuation of sound by atmospheric turbulence based on turbulence-induced beam broadening (rather than scattering). The key insight: attenuation is not intrinsic to the medium but depends on geometry (beamwidth, path length, beam orientation). The beam expands due to refractive index fluctuations; any receiver smaller than the broadened beam sees reduced intensity. Derives excess attenuation A_e from forward-propagation theory (Tatarskii, Yura). Qualitatively agrees with observations; A_e ≈ 10 log(1 + 1.56 k^(12/5) D₀⁻² [∫ds(L-s)^(5/3) C_n²(s)]^(6/5)).

## Unique contribution
Resolves the controversy over excess attenuation by attributing it to beam spreading rather than scattering loss — proving that excess attenuation is experiment-geometry dependent, not a property of the medium. Explains why ground-based transmitters experience ~5× higher excess attenuation than elevated transmitters over the same path (turbulence near the transmitter matters most due to (L-s)^(5/3) weighting).

## Key concepts
- Excess attenuation of sound by turbulence
- Turbulence-induced beam broadening (not scattering)
- Forward propagation through turbulence
- Refractive index structure parameter C_n²
- Wave structure function D_w(ρ, L)
- Excess attenuation A_e = 10 log(1 + D_t²/D_f²)
- Path-weighting asymmetry: turbulence near transmitter dominates
- Atmospheric boundary layer profiles of C_n² and C_v²

## Methods / results / takeaways
- Model: beam expands due to turbulent phase fluctuations; ⟨I⟩/I₀ = D_f²/D² = 1/(1 + D_t²/D_f²).
- Turbulent beam spread: D_t² = 2.51 ∫₀^L (L−s)^(5/3) C_n²(s) ds (from Yura).
- A_e = 10 log(1 + 0.48 k^(12/5) D₀⁻² L^(6/5) C_n²^(2/5)) for constant C_n².
- Key result: path weighting factor (L−s)^(5/3) means turbulence near the transmitter (s near 0) contributes most.
- Atmospheric profiles: C_n² peaks near ground; C_T² and C_v² profiles for unstable daytime boundary layer given.
- Comparison with Delsasso & Leonard 1953: theoretical α_e agrees within scatter for 125–1000 Hz.
- Frequency dependence: A_e ∝ f^(2/5) under logarithm — appears as ~cube-root for typical magnitudes; much weaker than ordinary attenuation.
- Excess attenuation: typical values 1–8 dB/km for 4 kHz at km paths; significant but not dominant.
- Limitation: beam broadening model not valid if receiver smaller than inner scale of turbulence; assumes narrow-angle scattering (λ < l₀).
