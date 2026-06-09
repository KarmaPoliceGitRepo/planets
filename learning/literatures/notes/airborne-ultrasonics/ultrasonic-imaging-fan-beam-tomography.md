# Ultrasonic Imaging in Air Using Fan-Beam Tomography and Electrostatic Transducers

- **Source:** Ingleby & Wright 2002 ultrasonic imaging fan-beam tomography
- **Drive link:** https://drive.google.com/file/d/1ECmyg3c0a0pP_ekNHEjoyd4DpmxVPMDR/view
- **Type:** paper
- **Author/Year:** Ingleby & Wright, 2002 (Ultrasonics 40, 507)
- **Coverage:** full

## Overview
Employs air-coupled capacitance transducers (400 kHz, 300 kHz −6 dB BW) in a fan-beam tomographic configuration to image temperature fields, flow fields, and solid object locations in air. Uses filtered backprojection with a re-bin routine. Reconstructed temperatures within 4–9% of thermocouple measurements.

## Unique contribution
Extends parallel-beam acoustic tomography in air to fan-beam geometry, enabling imaging of temperature and flow fields with fewer source positions. First demonstration of fan-beam air-coupled acoustic tomography for thermometry with results quantitatively compared to thermocouple reference data.

## Key concepts
- Air-coupled tomography
- Fan-beam reconstruction
- Filtered backprojection
- Electrostatic / capacitive transducer
- Temperature field imaging
- Flow field imaging
- Speed of sound vs temperature
- Re-bin routine

## Methods / results / takeaways
- Transducers: convex-backplate electrostatic, 400 kHz, −6 dB BW 300 kHz; 100 V DC bias + 250 V spike.
- Geometry: fan-beam, 37 receiver positions at 5° intervals × 72 source positions (360°); 2664 waveforms.
- Scan time: ~8 h (automation via LabVIEW + stepper motors, 0.02° accuracy).
- Solid objects: located and sized accurately; Nylon 21 mm cylinder located at correct coordinates.
- Temperature: background accuracy 4–7%; above heat source 9%.
- Flow: horizontal velocity component of air jet (0.5 l/s nozzle) resolved; max velocity 8.6 m/s vs predicted 8.0–9.4 m/s.
- Key limitation: transducer size causes spatial averaging; temperature fluctuations during 8 h scan time-average.
- Speed-of-sound equation used: c = 331.31√(T/273.16) m/s.
