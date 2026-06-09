# Contactless Energy Transfer Through Air by Means of Ultrasound

- **Source:** Roes 2011 contactless energy transfer via ultrasound
- **Drive link:** https://drive.google.com/file/d/1xBcRCftHgujBpd209uoZqh61Q6Yau4jm/view
- **Type:** paper
- **Author/Year:** Roes, Hendrix & Duarte, 2011 (IEEE ECCE 2011)
- **Coverage:** full

## Overview
Proposes acoustic energy transfer (AET) as a contactless power delivery mechanism using ultrasound in air. Calculates theoretical efficiency limit by modelling diffraction and attenuation losses separately. Optimal design: 7.86 cm radius transducer at 20.46 kHz over 1 m achieves 53% theoretical efficiency — about 26× better than comparable inductive CET. Measured peak efficiency 16%.

## Unique contribution
First rigorous analytical framework for AET efficiency optimisation in air, combining Rayleigh integral beam model with frequency-dependent air attenuation. Shows optimal frequency ~20 kHz for metre-range AET — directly useful for power delivery to mobile devices where EM coupling is impractical.

## Key concepts
- Acoustic energy transfer (AET)
- Contactless power transfer
- Rayleigh integral model
- Diffraction loss vs attenuation tradeoff
- Optimal frequency for AET
- Bending mode piezoelectric transducer
- Vibrating piston model
- Air attenuation
- Quarter-wave matching
- Comparison with inductive CET

## Methods / results / takeaways
- System: circular piston transmitter + receiver, R = 1 m separation.
- Optimal frequency: 20.46 kHz (balances increasing diffraction losses at low f vs increasing attenuation at high f).
- Optimal transmitter radius: 7.86 cm; receiver: 10 cm.
- Theoretical total efficiency: 53% (diffraction × attenuation).
- Including 10% transducer losses each end: ~53% → ~43%.
- vs inductive CET (same geometry): ~2% → AET ~26× better.
- Measurement: PX051 piezo benders (1.3 cm radius), 17 kHz; peak efficiency 16% at short distance.
- Spatial resonances observed (standing waves between transducer faces) — need impedance matching to suppress.
- Key insight: at kHz frequencies, diffraction dominates → larger aperture improves efficiency; at 100s kHz, attenuation dominates → lower frequency better.
- Output power 37 μW — too low for most applications; transducer design (high-power bending mode) is key challenge.
