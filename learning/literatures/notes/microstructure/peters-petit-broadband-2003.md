# Broadband Spectroscopy in Dispersive Media Using Automatic Phase Unwrapping

- **Source:** Peters and Petit Ultrasonics 41 357 2003
- **Drive link:** https://drive.google.com/file/d/1_5ceRFrhdtlfigIfPbmpL0FOAwPWb1l_/view
- **Type:** paper
- **Author/Year:** F. Peters, L. Petit / 2003
- **Coverage:** full

## Overview
A paper on broadband ultrasonic spectroscopy in dispersive media, presenting an automatic phase unwrapping algorithm based on cross-correlation time-delay estimation to avoid 2πn ambiguity in phase velocity measurements. Includes complete MATLAB implementation. Validated on polystyrene bead suspension at 700 kHz–8 MHz.

## Unique contribution
Provides a practical, automated algorithm for phase unwrapping in broadband dispersion measurements that is robust against phase jumps and requires no user intervention, plus a complete working MATLAB code — making the method immediately usable for laboratory measurements.

## Key concepts
- Automatic phase unwrapping
- Broadband spectroscopy
- Dispersion measurement
- Cross-correlation time delay
- Phase velocity extraction
- 2πn ambiguity
- Polystyrene suspension
- MATLAB implementation

## Methods / results / takeaways
- Algorithm: compute cross-spectrum between reference and transmitted signals; unwrap phase by ensuring continuity; divide by path length × frequency.
- Cross-correlation used for initial coarse time delay to set phase branch; fine unwrapping then applied frequency-by-frequency.
- Validated on polystyrene microspheres in water (700 kHz–8 MHz): phase velocity and attenuation measured; compared with ECAH scattering theory.
- Phase velocity accuracy: ±0.5 m/s (0.03% for water-based suspensions).
- Attenuation accuracy: ±0.01 dB/cm at 1 MHz.
- MATLAB code included in appendix; works for narrowband or broadband transducer pairs.
- Key insight: when using short pulses, unwrapping is straightforward; when using long tone-bursts or when attenuation varies strongly, ambiguity increases and cross-correlation seeding is essential.
