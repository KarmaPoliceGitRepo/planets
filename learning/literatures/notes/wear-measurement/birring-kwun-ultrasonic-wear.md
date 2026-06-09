# Ultrasonic Measurement of Wear

- **Source:** Birring_Kwun_ultrasonic measurement of wear.pdf
- **Drive link:** https://drive.google.com/file/d/12cLNWo-PjaCXyh_quH-EyHCXqIKnWv3E/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** A.S. Birring, H. Kwun / 1989 (Tribology International 22(1), pp. 33-37)
- **Coverage:** full

## Overview
A foundational paper from Southwest Research Institute that establishes the ultrasonic phase-comparison technique as a viable method for sub-micrometre wear measurement in diesel engine liners. Standard pulse-echo instrumentation (±1 ns timing accuracy, equivalent to ±3 µm) is insufficient for monitoring liner wear on the order of 1 µm after 80 hours of operation. The phase-comparison technique achieves theoretical accuracy of 0.015 µm by measuring the CW frequency shift required to maintain a fixed phase between echo and reference, but practical in-engine accuracy is limited to ~0.75 µm due to temperature and drift errors.

## Unique contribution
This is a primary reference in the ultrasonic wear measurement field — cited explicitly by Brunskill et al. (2015) as establishing that conventional ultrasound is "too inaccurate" for precision wear. It introduces the interferometric phase-comparison concept, derives the temperature correction equations, proposes the ferrite plug probe design for in-liner installation, and defines the specific error sources (temperature, drift, vibration) that later work aimed to overcome. US Patent 4711120 resulted from this program.

## Key concepts
- Phase-comparison technique
- Ultrasonic interferometry
- Continuous wave (CW) frequency synthesis
- Transit-time / time-of-flight
- Thermal expansion error
- Acoustic velocity temperature dependence
- Wear probe (ferrite plug with piezoelectric crystal + platinum RTD)
- Engine liner wear
- Phase detector
- Control probe (drift compensation)
- Lead metaniobate transducer
- Nth-echo sensitivity enhancement

## Methods / results / takeaways
- **Basic wear formula:** `d = vt/2`, `Δd = vΔt/2`. Standard ±1 ns accuracy → ±3 µm wear resolution; insufficient for 1 µm target.
- **Phase-comparison principle:** CW signal at same frequency as transducer is kept in fixed phase with returning echo by adjusting frequency Δf. Then `Δt/t = -Δf/f`. For 10 MHz and t = 5×10⁻⁶ s, accuracy in Δt = ±5×10⁻¹¹ s → theoretical Δd = 0.015 µm.
- **N-th echo enhancement:** using the Nth multiple reflection amplifies phase change by factor N, improving sensitivity by N.
- **Temperature errors:** temperature increase reduces acoustic velocity (Δv = αΔT) and increases specimen thickness via thermal expansion; both effects alter ToF and must be subtracted.
- **Lab validation:** grinding test on 0.90 cm iron disc; wear measured ultrasonically at 3–5 min intervals, compared to micrometer. Temperature monitored by platinum RTD bonded to same surface as transducer. Achieved ±0.75 µm accuracy in lab.
- **Probe design:** 10 MHz lead-metaniobate crystal soldered to 9 mm ferrite (97% Fe + 3% Si) plug screwed into a drilled hole in the liner wall. Ferrite is softer than liner (78 vs. 90 Rb) ensuring matched wear; also lower ultrasonic attenuation. Fine threads (~13 threads/cm) minimise differential thermal expansion effects between ferrite and cast iron.
- **Engine results:** errors increased substantially in running engine due to vibration and larger temperature gradients along plug. Requires: (1) taking measurements at consistent temperature after shutdown; (2) a non-wearing control probe to separate instrument drift.
- **Conclusion:** Phase-comparison technique suitable for liner wear monitoring if temperature and drift errors are controlled; in-engine system needed further development at time of publication.
