# Detection of Ultrasound Pressure Distribution for Remote Measurement of Haptic Surface Roughness

- **Source:** Kamigaki 2015 haptic roughness ultrasound
- **Drive link:** https://drive.google.com/file/d/1mTT6FPn77jnZ-frrB5WYBTMDdyneK6mb/view
- **Type:** paper
- **Author/Year:** Kamigaki, Nakatsuma, Oshima & Torigoe, 2015 (IEEE Sensors 2015)
- **Coverage:** full

## Overview
Proposes a remote non-contact method for measuring millimetre-scale surface roughness (haptic texture) using airborne ultrasound diffraction patterns. A 40 kHz coherent beam irradiates a surface from 310 mm away; the reflected spatial pressure distribution is scanned by a single receiver. The pattern is compared to a 2D diffraction model (slit aperture superposition). Measurement limit ~8.5 mm (wavelength); demonstrated on regularly patterned gratings with apertures 5–30 mm.

## Unique contribution
Frames airborne ultrasound roughness sensing as a diffraction problem rather than amplitude attenuation or scattering, enabling remote measurement from tens of centimetres. Targets haptic texture (millimetre-scale asperities perceptible by touch) — a regime where optical methods and conventional ultrasound roughness sensors are not designed to operate. Applicable to "haptic broadcasting" and remote surgery scenarios.

## Key concepts
- Haptic surface roughness measurement
- Airborne ultrasound diffraction
- Spatial sound pressure distribution
- 40 kHz transducer (NIPPON CERAMIC T4010A1)
- 2D diffraction model (slit superposition)
- Remote measurement 310 mm standoff
- Millimetre-scale surface profile
- Tactile texture characterisation

## Methods / results / takeaways
- Transducers: 40 kHz piezoelectric (NIPPON CERAMIC T4010A1); one transmitter, one receiver on 1-axis stage.
- Model: diffraction from apertures modelled as slit superposition with phase modulation e^{-j2kd} per profile height d.
- Samples: regularly-patterned apertures (slits) in flat plates; aperture widths 5, 6, 7, 10, 20, 30 mm.
- Stand-off: 310 mm from transducers to surface; burst waves (5 cycles) to isolate surface reflection.
- Results: spatial pressure distribution agrees with diffraction model for apertures ≥ 8.5 mm (λ at 40 kHz); 5 mm aperture (< λ) not measurable.
- Measurement limit: ~λ = 8.5 mm for 40 kHz; higher frequencies (larger k) would extend resolution.
- Future work: receiver array for 3D measurement; higher frequency for finer profile.
