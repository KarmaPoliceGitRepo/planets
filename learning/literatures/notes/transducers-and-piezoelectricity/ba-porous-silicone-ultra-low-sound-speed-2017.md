# Soft Porous Silicone Rubbers with Ultra-Low Sound Speeds in Acoustic Metamaterials

- **Source:** Ba porous silicone ultra low sound speed 2017
- **Drive link:** https://drive.google.com/file/d/1Md3rInMYcjI8phNub8bvPrDueq9bLo2R/view
- **Type:** paper (Scientific Reports 7, 40106, 2017)
- **Author/Year:** A. Ba, A. Kovalenko, C. Aristégui, O. Mondain-Monval, T. Brunet / 2017
- **Coverage:** full

## Overview
Reports complete ultrasonic characterisation of soft porous silicone rubber materials (emulsion-templated, pore size 1–30 μm) at porosities φ = 0–35%. Finds extraordinary result: longitudinal sound speed cL drops from 1110 m/s (φ=0) to 38.5 m/s (φ=35%), while transverse speed cT remains nearly constant (~15–17 m/s). Explains using Kuster-Toksöz (KT) single-scattering long-wavelength model, which gives identical results to the more complex Waterman-Truell multiple scattering model in this quasi-static limit.

## Unique contribution
Demonstrates experimentally that soft porous silicone rubber with only 1% porosity achieves cL = 165 m/s — a 6.7× reduction from the dense material. The mechanism is the huge ratio K₀/G₀ ≈ 4000 for silicone rubber (K₀ = 1.2 GPa, G₀ = 0.3 MPa): air pores reduce K (and hence cL ∝ √K) dramatically while barely affecting G (and hence cT ∝ √G). Aerogels require >90% porosity to reach similar cL values. Provides analytical closed-form KT expressions for both sound speeds.

## Key concepts
- Silicone rubber matrix: ρ₀ = 1040 kg/m³, K₀ = 1.2 GPa, G₀ = 0.3 MPa (G₀ << K₀)
- cL₀ ≈ √(K₀/ρ₀) = 1075 m/s (elastomeric: K >> G so cL ≈ √K/ρ); cT₀ = √(G₀/ρ₀) ≈ 17 m/s
- KT model (K): K ≈ 4G₀(1−φ)K₀ / (4G₀ + 3K₀φ) → K decreases sharply with φ due to 3K₀ >> 4G₀
- KT model (G): G ≈ G₀·3(1−φ)/(3+2φ) → weak porosity dependence
- KT model (ρ): ρ ≈ (1−φ)ρ₀
- cL(φ): cL ≈ cL₀ / √(1 + 3K₀φ/4G₀) — strong drop because 3K₀/4G₀ ≈ 3000
- cT(φ): cT ≈ cT₀ / √(1 + 2φ/3) — weak drop (factor <1.5 over 0–35% porosity)
- Attenuation: αL = 30f^1.4 Np/m (φ=0); rises to 78×10³ f^1.4 Np/m (φ=35%); power law exponent n ≈ 1.4–1.6

## Methods / results / takeaways
- Synthesis: water-in-PDMS emulsion templating; platinum-catalysed polyaddition; room-temperature curing; pore size controlled by emulsion droplet size (1–30 μm)
- Samples: 35 mm diameter disks, two thicknesses δd = 1.5 mm; dry mass/volume for density
- Longitudinal: immersion transducers (Olympus V301, 25 mm); contact pressure coupling (no fluid infiltration)
- Transverse: shear transducers (Sonaxis CMP79); note: pure shear mode not achievable at φ=0% (too attenuated)
- Phase velocity from FFT phase difference between two thicknesses; attenuation from FFT amplitude ratio
- cL results: 1110 → 165 → 60 → 53 → 38.5 m/s for φ = 0, 1, 12, 19, 35%
- cT results: ~15–17 m/s (nearly constant across φ = 1–35%)
- KT model agrees excellently with both cL and cT; same result as Waterman-Truell
- Application: ultra-slow resonators for acoustic metamaterials; Mie-type monopolar/dipolar resonances at low frequencies; negative acoustic index materials
