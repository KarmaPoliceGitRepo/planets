# Automotive Cylinder Bore Distortion — Accuracy of Ultrasonic Measurements

- **Source:** Shah_N (Dwyer-Joyce).pdf
- **Drive link:** https://drive.google.com/file/d/1hYHqaFBz5lXowwFT3vrqTV-irZzDK8y7/view?usp=drivesdk
- **Type:** thesis
- **Author/Year:** Nipam Shah, April 2018 (University of Sheffield MEng, supervisor: Rob Dwyer-Joyce)
- **Coverage:** full

## Overview
This MEng thesis investigates whether pulse-echo ultrasonic transducers can accurately measure deformation (distortion) of a cylinder liner sample under static and compressive loading. Distortion is described via a Fourier series in angle (harmonic orders). Experiments were conducted on an aluminium cylinder sample using bonded PZT transducers and a Tinius Olsen tensile testing machine at 0.5 mm and 1 mm applied displacements. A finite element model in ANSYS was built to validate the measured thickness changes.

## Unique contribution
Demonstrates both the capability and the current limitations of pulse-echo ultrasonics for cylinder bore distortion measurement. Static thickness measurement was accurate, but dynamic compression measurements did not correlate well with the FE model — although a linear deformation trend was observed, confirming the physics. A compression rig designed for temperature calibration of ultrasonic speed is described as future work.

## Key concepts
- Cylinder liner distortion / bore out-of-roundness
- Fourier series harmonic decomposition of bore profile
- Pulse-echo ultrasonic thickness measurement
- Time-of-flight (TOF)
- Acoustic impedance, attenuation, reflection coefficient
- Piezoelectric transducers (PZT / Lead Zirconate Titanate)
- Cross-correlation for TOF determination
- Finite Element Analysis (ANSYS) — mesh convergence, von-Mises stress
- Axis-crossing and band-pass filtering (MATLAB signal processing)
- Temperature effect on ultrasonic wave speed

## Methods / results / takeaways
- **Measurement principle:** Pulse-echo TOF gives thickness T = v·t/2 where v is the speed of sound in the material. Thickness change tracks deformation.
- **Static measurement:** Three bonded transducers (at 30°, 60°, 90° around the circumference) successfully measured sample thickness to good accuracy in the static (unloaded) case.
- **Under compression:** Signals from the tensile test machine showed a linear trend of thickness change consistent with FE predictions, but absolute values had poor correlation. Likely causes: transducer bonding quality, coupling variability during loading, and temperature-induced velocity changes.
- **FE model:** ANSYS model with mesh convergence study (von-Mises stress at 0.5 mm and 1 mm loading) confirmed expected deformation pattern. FE results served as the reference for evaluating ultrasonic accuracy.
- **Future work recommended:** (1) Improve transducer bonding and experimental rig; (2) Use STAMINA or resonant methods instead of pulse-echo; (3) Characterise stress and temperature effects on wave speed; (4) Build a dedicated temperature calibration rig.
- **Key finding:** Pulse-echo is viable for static bore thickness mapping but further development is needed for reliable in-situ dynamic distortion measurement during engine operation.
