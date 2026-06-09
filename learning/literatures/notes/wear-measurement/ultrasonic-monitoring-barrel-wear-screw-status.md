# Ultrasonic Monitoring of Barrel Wear and Screw Status

- **Source:** Ultrasonic Monitoring of Barrel Wear and Screw Status.pdf
- **Drive link:** https://drive.google.com/file/d/1MYuihHom2Ig6o7n_iMNF4R3AQ9d6T7Iq/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** C.-K. Jen, Z. Sun, M. Kobayashi / 2004
- **Coverage:** full

## Overview
This paper presents ultrasonic methods for real-time, in-line monitoring of barrel wear, screw wear, screw misalignment, and screw deflection in polymer extrusion. Four sensor types are evaluated on a Werner & Pfleiderer 30 mm twin-screw extruder running LDPE and HDPE: sol-gel sprayed high-temperature (HT) piezoelectric thick-film transducers, stand-alone HTUTs, and air-cooled buffer rod sensors with either non-clad or clad rods. All approaches are non-intrusive to the extruder and non-destructive to the polymer.

## Unique contribution
This is one of the first papers to demonstrate simultaneous, real-time measurement of barrel wear, screw wear, screw misalignment, and screw deflection under actual extrusion conditions at all three key zones (pumping, mixing, melting). It compares four sensor types directly and quantifies measurement accuracy in terms of temperature and pressure uncertainty effects, reporting barrel thickness accuracy of ~22.5 µm under stable conditions and barrel/screw clearance accuracy of ~18 µm.

## Key concepts
- Ultrasonic pulse-echo thickness measurement
- Sol-gel sprayed HT piezoelectric transducers (BIT/PZT)
- Buffer rod sensors (clad and non-clad)
- Barrel wear (δdB)
- Screw wear (δdF_screw)
- Screw misalignment (δdF_malgn)
- Screw deflection (δdF_defl)
- Barrel/screw clearance measurement
- Time-of-flight (TOF) measurement
- Signal-to-noise ratio (SNR) in ultrasonic monitoring
- Cross-correlation for time delay measurement
- Twin-screw extruder monitoring
- High-temperature ultrasonic coupling

## Methods / results / takeaways
- Barrel wear is computed as δdB = dB0 − vLB·tB/2, where vLB ≈ 6000 m/s in steel and tB is the time delay between consecutive barrel echoes.
- Screw/barrel clearance dF = vLP·tP/2; screw wear is isolated from misalignment and barrel wear via a multi-term equation requiring measurements at multiple axial locations.
- Sol-gel BIT/PZT films operate up to 600°C without couplant, but require high-temperature oven processing of the barrel; risk of altering nitrided barrel microstructure.
- Stand-alone HTUTs (up to 250°C continuous) and buffer rods (room-temperature UT + cooling) offer portability for mapping wear along the barrel.
- Clad buffer rods outperform non-clad in SNR and are compatible with thermocouple access holes (Dynisco geometry).
- Low SNR (<20 dB) for screw echoes (vs. >30 dB for barrel echoes) limits real-time automation; dedicated signal processing or pattern recognition is needed.
- Temperature uncertainty of ±2°C introduces ~72 µm absolute uncertainty in barrel thickness; relative measurement under stable conditions is ±3 µm.
- Screw deflection is detectable as transient fluctuations in the measured clearance dF.
