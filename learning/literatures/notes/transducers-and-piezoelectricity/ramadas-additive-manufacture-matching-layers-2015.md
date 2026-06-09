# Additive Manufacture of Impedance Matching Layers for Air-Coupled Ultrasonic Transducers

- **Source:** Ramadas additive manufacture matching layers 2015
- **Drive link:** https://drive.google.com/file/d/1wTFg9xgbNJag7MzYI_k70fgmxK4MEVAG/view
- **Type:** paper (2015 IEEE International Ultrasonics Symposium, conference proceedings)
- **Author/Year:** S. N. Ramadas, M. Hunter, J. Thornby, C. P. Purssell, S. Leigh, S. M. Dixon / 2015
- **Coverage:** full

## Overview
Preliminary feasibility study demonstrating micro-stereolithography (μSL) as a fabrication method for impedance matching layers for air-coupled ultrasonic transducers. Uses a custom inverted μSL apparatus with PEG/DPPHA diacrylate resin loaded with hollow glass micro-balloons (density 0.125 g/cm³; diameter 120 μm) to reduce the cured ML acoustic impedance. Prints ML directly onto PZT ceramic at 200 kHz, characterises internal porosity by μ-CT, and compares acoustic performance against conventionally fabricated glued layers. Results show comparable or better sensitivity and bandwidth from the directly-printed μSL ML.

## Unique contribution
First demonstration of μSL 3D printing for acoustic matching layer fabrication in air-coupled transducers. Key advantage: ML can be printed directly onto the PZT ceramic surface, eliminating the bond layer (which is typically Z = 0.8–2.4 MRayl), a major source of parasitic reflections. Internal porosity characterised by μ-CT: 28% bulk porosity, consistent throughout; boundary porosity 18–24%. Sound speed: 1865 m/s → QWL at 200 kHz = 2.3 mm. The approach can in principle be extended to graded-impedance multi-layer profiles by varying filler ratio during printing.

## Key concepts
- μSL process: inverted DLP-based; layer thickness controlled by exposure time; 1088×612 pixel DLP; 10 mm diameter circular layers
- Photo-curable resin: PEG (polyethylene glycol diacrylate) + DPPHA (dipentaerythritol penta-/hexa-acrylate); 1:3 volume ratio (more viscous DPPHA to retard micro-balloon flotation)
- Glass micro-balloon filler: density 0.125 g/cm³; isostatic crush strength 250 psi; diameter 120 μm
- Maximum filler:resin mass ratio: 1:6 (above this, resin no longer curable)
- Maximum single-layer curable thickness: ~510 μm
- ML acoustic properties: v = 1865 m/s (measured); QWL at 200 kHz = 2.3 mm
- Optimum Z range for air coupling: 0.02–0.8 MRayl (geometric mean of PZT and air)
- μ-CT characterisation: XT H 320 LC, 200 kV, 5 μm voxel; porosity analysis in Volume Graphics Studio Max 2.2
- Porosity: 28% bulk (consistent); boundary: 18–24% (layer-layer interfaces visible but effect expected minimal)
- Prototype: PZ27 Ferroperm PZT ceramic disc at ~200 kHz; ML printed directly onto ceramic
- Reference transducer: identical PZT with conventional adhesively bonded ML
- Performance: consistent, comparable or better sensitivity and bandwidth vs conventional
- Surface dilation: laser interferometer (Polytec OFV-5000); direct print shows consistent characteristic similar to conventional

## Methods / results / takeaways
- Pressure measurement: Bruel & Kjaer microphone at 3 cm from transducer front face; Olympus 5077PR pulser
- Results: comparable performance to adhesively bonded ML; no systematic sensitivity deficit
- Ongoing work: optimising resin composition for target Z; graded impedance multi-layer designs
- Key limitation: maximum ML porosity limited by resin cureability; Z = 0.02 MRayl requires very high porosity (>95%) not achievable with this resin
- Application: robust, reproducible, low-cost ML fabrication; flow metering; NDE
- Funding: MC-IAPP European project SACUT (Grant 612118); Royal Society RG130286
