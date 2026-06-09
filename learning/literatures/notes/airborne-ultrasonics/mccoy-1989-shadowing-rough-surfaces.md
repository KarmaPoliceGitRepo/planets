# Shadowing by Randomly Rough Surfaces

- **Source:** McCoy 1989 shadowing rough surfaces
- **Drive link:** https://drive.google.com/file/d/1pC1eCP-4Zwx4cgjKsWRbpme8H5MfdbRq/view
- **Type:** paper
- **Author/Year:** McCoy, 1989 (Journal of the Acoustical Society of America, 86(4), 1523–1529)
- **Coverage:** full

## Overview
Develops a rigorous computational framework for incorporating shadowing into statistical wave-scattering models for randomly rough surfaces. Argues that the Beckmann approach (which uses an ensemble-averaged shadowing function Pc(θ)) implicitly assumes statistical independence of the shadowing process and the surface-scattered field — an assumption that cannot be justified. Identifies the correct conditional probability functions that should replace Pc(θ) for the coherent field and spatial coherence function mappings.

## Unique contribution
Shows that the commonly accepted Beckmann shadowing function Pc(θ) is fundamentally incorrect as a direct correction factor because it assumes statistical independence between the shadowing function and the surface reflection geometry — both of which depend on the same rough surface realisation. Derives the correct conditional probability functions Ps(hr, h'r, θ) required for rigorous shadowing incorporation in coherent field and coherence function scattering models.

## Key concepts
- Acoustic scattering from randomly rough surfaces
- Shadowing function (Beckmann approach critique)
- Conditional shadowing probability Ps(hr, h'r, θ)
- Coherent component of scattered field
- Spatial coherence function
- Statistical independence assumption failure
- Kirchhoff (semigeometric) scattering model
- Random rough surface statistics

## Methods / results / takeaways
- Key critique: Pc(θ) = <σ(x,θ)> (unconditional average of shadowing indicator) is inappropriate because the shadowing function and surface field are not statistically independent.
- Correct measure for coherent field: Ps1(hr, θ) — conditional probability that one of a pair of rays intersects the surface, given a reflection point at height hr.
- Further approximation (Beckmann recovery): breaks into Ps2(θ) by assuming statistical independence — shown not to be justifiable.
- Coherence function mapping: requires a 4-ray shadow probability function Ps1(hr1, hr2, θ).
- Practical implication: existing Beckmann-based shadowing corrections are approximations whose accuracy depends on how weakly the shadowing function correlates with the surface field statistics.
- Application: relevant to ultrasonic roughness characterisation models using Kirchhoff scattering theory at steep angles where self-shadowing is significant.
