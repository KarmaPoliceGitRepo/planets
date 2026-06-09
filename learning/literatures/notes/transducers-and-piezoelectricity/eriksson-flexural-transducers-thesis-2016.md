# Development of Piezoelectric and Electrodynamic Flexural Transducers for Air-Coupled Ultrasonics

- **Source:** Erikson flexural transducers thesis 2016
- **Drive link:** https://drive.google.com/file/d/1EI_wNYJnlg4C7aFe5svvo_-OJIadIgBM/view
- **Type:** PhD thesis (University of Warwick, Department of Physics, September 2016)
- **Author/Year:** T. J. R. Eriksson / 2016
- **Coverage:** full

## Overview
PhD thesis developing piezoelectric flexural transducers (PFTs) and electrodynamic flexural transducers (EDFTs) for air-coupled ultrasonics (ACU). Covers thin-plate vibration theory (edge-clamped circular plate), FE modelling (PZFlex 2D axisymmetric), and experimental characterisation by laser generation/detection, laser vibrometer area scans, electrical impedance analysis, and directivity measurements. Demonstrates PFTs at 22–200 kHz using aluminium and titanium caps; EDFTs for low-frequency (below 40 kHz) applications; and flow meter prototype demonstrations. Also constructs 3×3 flexural phased array.

## Unique contribution
First systematic characterisation of the split (1,0) mode in edge-clamped flexural transducer caps, showing that three closely spaced peaks (1,0)a, (1,0)b, (1,0)c arise from the finite wall thickness causing the plate effective radius to vary between inner (r) and outer (R) radii. Derives that mode frequencies scale as h (plate thickness) and 1/a² (plate radius squared). Demonstrates EDFTs — voice-coil-driven metal cap transducers — as an alternative to PFTs for very low frequencies without PZT. Validates Rayleigh integral reconstruction of pressure field from laser-scanned surface displacement data.

## Key concepts
- Flexural transducer principle: PZT disc bonded to metal cap inner surface; d31 lateral strain causes bending (unimorph); resonance frequency set by cap geometry
- Mode frequencies (edge-clamped circular plate): ω = (λ_mn/a)² √(D/ρh); D = Eh³/[12(1-ν²)]
- Key eigenvalues: λ₀₀=3.196, λ₀₁=4.611, λ₁₀=6.306 for (m,n) = (0,0),(0,1),(1,0)
- Frequency scaling: ω ∝ h (thickness); ω ∝ 1/a² (radius squared)
- ProWave 400ET250 commercial 40 kHz transducer: (1,0) mode at 39.8 kHz; outer antinode amplitude 100% larger than theory due to PZT stiffening of centre
- Aluminium cap (h=0.5 mm, r=4.5 mm, R=5.5 mm): fundamental (0,0) ≈ 50 kHz; split (1,0) modes at 160, 180, 210 kHz
- 32 aluminium caps at 150 kHz nominal: ±35 kHz spread (46% of mean) due to dimensional tolerances
- Titanium cap (h=0.25 mm, r=5.2 mm, R=6.0 mm): f₀₀=(22.3±0.5) kHz, f₀₁=(43±1) kHz, f₁₀=(79±2) kHz — excellent consistency
- EDFT (Electrodynamic): voice coil + permanent magnet drives metal cap; no PZT; well suited for f < 40 kHz
- EDFT result: 3 designs tested; pressure output increases with magnetic field strength; biased vs non-biased configurations
- 3×3 flexural phased array: laser-cut acrylic or 3D-printed ABS baffle; each element independently driven; demonstrator for steering/focusing
- Matching layers: not used on flexural transducers (key advantage — eliminates adhesive bond failure mode)
- PZFlex FEM: 2D axisymmetric; validates mode frequency predictions within few percent for fundamental mode
- Equivalent circuit: Guan model (with Rs, Rp) used for systems with significant material losses
- Characterisation methods: Nd:YAG laser (1064 nm, 10 ns, 6 mm spot) for generation; IOS two-wave-mixer interferometer (1550 nm, 125 MHz BW) for detection; Polytec OFV-5000 for front face scans; Agilent 4294A impedance analyser

## Methods / results / takeaways
- Laser generation + interferometric detection of passive cap: establishes frequency spectrum before PZT bonding
- Identifies mode numbers by: (i) centre vs off-centre measurement comparison; (ii) FE model comparison
- Digital narrowband DSP filter applied to broadband displacement scan → single-mode shape extraction
- ACU applications covered: flow metering (transit-time, multi-path), NDE (pulse-echo, through-transmission, backscatter), proximity sensing
- Flow test rigs: elevated static pressure; air flow; water flow
- Flow results: flexural transducers viable for gas flow metering; at elevated static pressure, resonance frequency shifts slightly
- Array grating lobe problem for ACU: d > λ/2 inevitable due to large aperture requirements at low frequency
- Mitigation: random, binned, or Fermat spiral array patterns
- Warwick thesis WRAP URL: http://wrap.warwick.ac.uk/91284
- Application: robust low-cost ACU sensors for gas flow metering, NDE, proximity sensing
