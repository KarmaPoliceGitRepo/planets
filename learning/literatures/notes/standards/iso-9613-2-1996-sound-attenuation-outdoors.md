# ISO 9613-2:1996 — Acoustics: Attenuation of Sound During Propagation Outdoors — Part 2: General Method of Calculation

- **Source:** ISO 9613-2 - Acoustics - Attenuation of sound during propagation outdoors - Part 2 (general method of calculation).pdf
- **Drive link:** https://drive.google.com/file/d/1psEg5TTMCuyaewSK_SNSO58hQFsJq6TC/view?usp=drivesdk
- **Type:** datasheet
- **Author/Year:** ISO TC 43 / SC 1 / 1996
- **Coverage:** full

## Overview
An engineering method for calculating the attenuation of sound propagating outdoors, allowing prediction of community noise levels from sources of known sound emission. The method produces equivalent continuous A-weighted sound pressure levels under specified meteorological conditions (downwind or moderate temperature inversion) using octave-band algorithms from 63 Hz to 8 kHz.

## Unique contribution
Provides a unified, source-agnostic computational framework that combines five independent attenuation mechanisms — geometrical divergence, atmospheric absorption, ground effect, barrier screening, and miscellaneous effects — into a single additive formula. Bridges between source sound power data (ISO 3740 series) and community noise assessment (ISO 1996 series). Widely adopted in environmental noise modelling software.

## Key concepts
- Equivalent continuous A-weighted sound pressure level LAT
- Downwind propagation conditions (wind 1–5 m/s, ±45° from source to receiver)
- Octave-band attenuation A = Adiv + Aatm + Agr + Abar + Amisc
- Geometrical divergence Adiv = 20 lg(d) + 11 dB
- Atmospheric absorption Aatm (coefficient α, dB/km, per octave band)
- Ground factor G (0 = hard, 1 = porous/vegetated)
- Ground attenuation Agr (three-region model: source, receiver, middle)
- Barrier attenuation Abar (diffraction via Fresnel number, path length difference z)
- Meteorological correction Cmet (long-term average vs downwind)
- Image sources for reflections from vertical surfaces

## Methods / results / takeaways
The method models sound as point sources (area/line sources are discretised). Ground attenuation is the dominant effect for low sources near the ground; it is computed separately for source region (30hs), receiver region (30hr), and middle region, then summed. The empirical ground factor G ranges from 0 (pavement/water) to 1 (grass/vegetation), with the hard-ground case giving negative (amplifying) ground effect at certain frequencies. Barrier insertion loss uses the Maekawa equation modified for meteorological effects: Abar = Dz − Agr, capped at 20 dB (single diffraction) or 25 dB (double diffraction). Accuracy of the overall method is ±3 dB for d < 100 m and h < 5 m; ±1 dB for 100 m < d < 1000 m and h < 5 m. The method does not apply to aircraft in flight or to blast waves.
