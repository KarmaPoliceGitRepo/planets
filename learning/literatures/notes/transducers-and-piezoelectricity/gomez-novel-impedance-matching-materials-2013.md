# Novel Impedance Matching Materials and Strategies for Air-Coupled Piezoelectric Transducers

- **Source:** Gomez novel impedance matching materials 2013
- **Drive link:** https://drive.google.com/file/d/1HWO0f41Rs8_DRvYDBsW2onR3R6bRoEff/view
- **Type:** paper (2013 IEEE International Ultrasonics Symposium, conference proceedings)
- **Author/Year:** T. E. Gómez Álvarez-Arenas, L. Díez / 2013
- **Coverage:** full

## Overview
Reviews the ideal 8-ML λ/4 stack configuration for air-coupled 1-3 composite transducers and identifies the four main non-ideal features of actual transducers: (1) unavailability of ultra-low Z materials, (2) ML thickness fabrication constraints, (3) bonding/mounting difficulties (adhesive layers introduce Z ≈ 0.8–2.4 MRayl), (4) open-pore structure complications (Biot two-mode propagation). Proposes new rigid polymer foam (Es = 5 GPa, closed-cell, Z down to 0.05 MRayl, v > 640 m/s, α < 100 Np/m) as improved ML material. Introduces a design optimisation procedure that adjusts Z and t simultaneously (±50% in 10% steps) to compensate for non-idealities.

## Unique contribution
Introduces velocity (v) as a second design criterion alongside Z for ML materials, arguing that higher v at a given Z provides: (1) lower attenuation, (2) thicker (easier to machine) ML, (3) larger acceptable pore size, (4) more closed-pore structure. Demonstrates this with a figure of E* vs velocity for 50+ materials from the literature. Fabricates new rigid closed-cell polymer foams (Es = 5 GPa) achieving Z = 0.05 MRayl with v > 640 m/s — approximately 3× the velocity of conventional open-cell porous materials at the same Z. Also proposes a MATLAB-based optimisation routine that simultaneously varies Z and t of each intermediate ML to maximise fom.

## Key concepts
- Ideal matching: 8 MLs for PZT5A 1-3 composite at 1 MHz; fom increases up to 8 MLs then saturates
- Ideal ML impedances (Table I): Z₁=0.0014, Z₂=0.0044, Z₃=0.0139, Z₄=0.0441, Z₅=0.1400, Z₆=0.4420, Z₇=1.4000, Z₈=4.4200 MRayl
- Ideal ML thicknesses at 1 MHz: λ/4 ranges from 9 μm (Z₁) to 525 μm (Z₈)
- Lowest available Z: 0.01 MRayl (f < 200 kHz); 0.05 MRayl (f < 1 MHz)
- Non-ideal outer ML: reduces fom and limits the practical number of useful intermediate MLs
- Adhesive layer Z: 0.8–2.4 MRayl; thickness 10–100 μm (spray, spin, deep coating)
- Pore constraint: for Z < 0.3 MRayl, pore diameter must be < ML thickness/100
- Two-mode propagation (Biot): pore-space borne wave is highly attenuated; sealing pores at interfaces prevents mode conversion
- New materials: rigid polymer foam with Es = 5 GPa, closed-cell; Z = 0.05 MRayl, v > 640 m/s, α < 100 Np/m at 1 MHz
- Design procedure: select outer ML material → determine number of intermediate MLs from fom curve → calculate Z_n via Eq. 3 → MATLAB optimise Z and t within ±50% in 10% steps

## Methods / results / takeaways
- Figure of merit (fom): gain-bandwidth product; gain = max peak-to-peak signal; bandwidth at −20 dB; TX-RX mode
- Piezoelectric composites modelled: PZT5A 65% vol 1-3 at 0.25 and 1.00 MHz; PMN-PT 55% vol 1-3 at 1.00 MHz
- Prototype: PMN-PT 1-3 composite at 1 MHz; 3 ML using new rigid foam materials
- Measured sensitivity: −25 dBV (Tx-Rx, 17 mm separation); Olympus 5077 pulser at 200 V
- Compared to ideal 8 ML stack (theory only): 3 ML prototype shows similar bandwidth profile with some sensitivity loss
- SEM images show typical pore structure of new rigid foams (closed-cell network)
- Application: wideband air-coupled NDE; gas flow metering; composite inspection
- Reference: Gómez Alvarez-Arenas TUFFC 51(5), 624–633, 2004 (key prior paper on ML design)
