# Ultrasonic Monitoring of Barrel Wear and Screw Status

- **Source:** Ultrasonic Monitoring of Barrel Wear and Screw Status.pdf
- **Drive link:** https://drive.google.com/file/d/1MYuihHom2Ig6o7n_iMNF4R3AQ9d6T7Iq/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** C.-K. Jen, Z. Sun, M. Kobayashi / 2004
- **Coverage:** full

## Overview
This paper from NRC Canada and McGill University presents a non-intrusive, in-line ultrasonic system for monitoring barrel wear, screw wear, screw misalignment, and screw deflection in a 30 mm Werner & Pfleiderer twin-screw polymer extruder. Four sensor types are evaluated across the pumping, mixing, and melting zones during LDPE and HDPE extrusion. The work demonstrates that ultrasound can track barrel/screw clearance in real time without halting production.

## Unique contribution
This is one of the first systematic comparisons of four different ultrasonic sensor configurations (sol-gel sprayed HT piezoelectric film, stand-alone HTUT, non-clad buffer rod, clad buffer rod) applied simultaneously to all three functional zones of a twin-screw extruder. It uniquely addresses screw deflection (transient positional variation) as distinct from misalignment (mean offset), and provides explicit measurement uncertainty budgets for both barrel thickness (±22.5 µm relative) and barrel/screw clearance (±18 µm relative) under realistic process conditions.

## Key concepts
- Ultrasonic pulse-echo mode
- Piezoelectric thick film transducer (sol-gel BIT/PZT)
- High-temperature ultrasonic transducer (HTUT)
- Buffer rod sensor (non-clad and clad)
- Barrel wear measurement
- Screw wear measurement
- Screw misalignment
- Screw deflection
- Barrel/screw clearance
- Time-of-flight (ToF) measurement
- Signal-to-noise ratio (SNR)
- Cross-correlation time-delay estimation
- Polymer extrusion (LDPE, HDPE)

## Methods / results / takeaways
- **Principle:** Ultrasonic longitudinal waves travel from an external sensor through the barrel wall into the polymer melt, reflecting from the inner barrel surface (L1) and from the screw flight (L2F). Barrel thickness is computed as `dB = vLB × tB / 2`; clearance to the screw is `dF = vLP × tP / 2`.
- **Screw deflection** is extracted as fluctuations of dF over time; screw misalignment is the mean offset after averaging out deflection.
- **Sensor 1 (sol-gel BIT/PZT film):** sprayed directly onto the adaptor surface, operates up to 600 °C, no couplant needed, center frequency ~10 MHz; demonstrated at pumping zone with HDPE at 200 °C / 1000 psi.
- **Sensor 2 (stand-alone HTUT, 5 MHz):** portable and mappable along barrel; used with silicone-oil couplant; distinguished 0.345 mm simulated screw wear clearly from echo time shift.
- **Sensors 3 & 4 (non-clad / clad buffer rods):** room-temperature UT + steel buffer rod + HT couplant; clad rod has higher ultrasonic performance and is more rugged; used at mixing zone and (clad only) at melting zone via barrel flange.
- **Barrel wear accuracy:** relative measurement better than 22.5 µm under ±0.5 °C / ±25 psi stability; absolute measurement ambiguity ~72 µm for 100 mm barrel.
- **Clearance accuracy:** relative better than 18 µm; SNR of screw echoes typically <20 dB, requiring dedicated signal processing.
- **Limitation:** low SNR at melting zone because unmelted pellets scatter ultrasound; clad buffer rod inserted via Dynisco-style thermocouple port offers an elegant access solution for sleeved barrels.
