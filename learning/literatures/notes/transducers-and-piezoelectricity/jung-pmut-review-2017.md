# Review of Piezoelectric Micromachined Ultrasonic Transducers and Their Applications

- **Source:** Jung pMUT review 2017
- **Drive link:** https://drive.google.com/file/d/15yYegdBLZnRPxmuOcp_nyN1zZe_Gxfok/view
- **Type:** paper (Journal of Micromechanics and Microengineering 27, 113001, 2017)
- **Author/Year:** J. Jung, W. Lee, W. Kang, E. Shin, J. Ryu, H. Choi / 2017
- **Coverage:** full

## Overview
Topical review of piezoelectric micromachined ultrasonic transducers (pMUTs) from 2017, covering fundamentals, design strategies for improved coupling coefficient, materials, fabrication techniques, and applications. Reviews the four main ultrasonic transducer types (piezoceramic, piezocomposite, cMUT, pMUT), then focuses on pMUT improvements through: (A) device geometry (multielectrode, partially-clamped, 3D dome/curved); (B) piezoelectric materials (thick PZT by GSV, textured PZT on γ-Al₂O₃ seed layer, PMN-PT single crystal); (C) fabrication techniques (SiO₂ stress compensation, parasitic capacitance reduction via metal bridges). Applications: IVUS, rangefinders, fingerprint sensors, wireless power.

## Unique contribution
Comprehensive survey of pMUT coupling coefficient improvements up to 2017. Documents that conventional planar pMUTs have k²_eff = 1–5% (sol-gel PZT), but dome-shaped PNZT (13% Nb-doped PZT, e31,f = −23 C/m²) achieves 45% — the highest bending-mode pMUT to date. Introduces the thin-film effective piezoelectric constants e31,f and d33,f and explains why thin-film devices favour the 31-mode (|e31,f| > |e31|). Provides Table 1 comparing ZnO, AlN, PZT e31,f, d33,f, and figure of merit (e²31,f/ε₀ε33,f). Documents GSV (granule spray in vacuum) as a thick-film deposition method achieving 1–100 μm PZT at low annealing temperature (650°C).

## Key concepts
- pMUT structure: PZT or AlN thin film on Si/SiO₂ membrane; bending (31-mode); resonance at flexural mode
- Thin-film piezoelectric constants: e31,f = d31/(s₁₁ᴱ + s₁₂ᴱ) — larger magnitude than bulk e31; d33,f = e33/c₃₃ᴱ — smaller than bulk d33
- Sensing sensitivity: Gs ∝ e31,f/ε33,f
- Actuation sensitivity: Gt ∝ −e31,f
- Transducer figure of merit: e²31,f/ε₀ε33,f (GPa): ZnO=10.3, AlN=11.9, PZT=6–18
- k²_eff = (fa² − fr²)/fa² ≈ Cm/(C₀ + Cm)
- Coupling coefficients (Table 2): sol-gel PZT 1.2–5.3%; PNZT dome-shaped 45%; PMN-PT 0.65 kt (thickness mode)
- Conventional piezoceramic: Z_PZT = 33 MRayl, Z_water = 1.5 MRayl; T = 2Z₂/(Z₁+Z₂) ≈ 10% without ML
- Ideal single ML: Z_m = √(Z_p × Z_l) — same as bulk transducer formula
- Backing material: 2–10 MRayl recommended for imaging (bandwidth vs sensitivity tradeoff)
- IVUS pMUT array: 512 elements, 5 MHz, 26 volumes/s (60°×60°, 10 cm depth); demonstrated in porcine model
- AlN pMUT rangefinder: membrane 400 μm diam, 1 μm thick, f_r = 214 kHz; range 30–450 mm
- Fingerprint sensor: pMUT + CMOS, 2D pulse-echo of PDMS fingerprint model
- PMN-PT pMUT: d33 ≈ 2500 pC/N (4× PZT); 0.7×0.7 mm², 50 μm thick, f_r = 35 MHz; kt = 0.65; −6 dB BW = 34%
- Textured PZT: (100) orientation on γ-Al₂O₃(111)/Si → e31,f higher; 8×8 array, 1.8 MHz, 100 μm diam; 3.9 μV/kPa (vs 1.3 μV/kPa conventional)
- GSV process: 5 μm/min deposition rate; 8 μm PZT at 650°C; k² = 1.05% (no DC bias); center displacement 0.8 μm at 5 Vpp, 300.9 kHz
- Stress management: compressive SiO₂ layer (−300 MPa) compensates electrode (+600 MPa) and PZT (+100 MPa) tensile stress; 13% displacement improvement with 0.7 μm PECVD oxide cap

## Methods / results / takeaways
- Review scope: 2017 snapshot of pMUT field; 24 pages; 139 references
- Electrode design: partial clamping via octagonal cell with 4 bridges → k² improvement; multielectrode designs
- Parasitic capacitance: metal bridge connections for large arrays (32×32) remove inactive PZT from lead lines
- Wireless power: AlN-based pMUT demonstrated for implantable device energy transfer
- cMUT comparison: requires DC bias + AC; high sensitivity but complex electronics; pMUT needs no bias (especially AlN)
- Grating lobe challenge for array: not specifically discussed (more relevant to air-coupled applications)
- Key limitation: thin-film pMUTs have lower piezoelectric constants than bulk ceramics due to substrate clamping
- Application: medical imaging, cardiovascular imaging, fingerprint security, rangefinding, wireless power for implantables
