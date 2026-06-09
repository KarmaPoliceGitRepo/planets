# High-Frequency Acoustic Wave Measurements in Air

- **Source:** Fox high frequency air measurements 1983
- **Drive link:** https://drive.google.com/file/d/1tJ5grnJPSED6dLAClmIFSmRjaZGxqGyG/view
- **Type:** paper (1983 IEEE Ultrasonics Symposium, pp. 581–584)
- **Author/Year:** J. D. Fox, B. T. Khuri-Yakub, G. S. Kino / 1983
- **Coverage:** full

## Overview
Early paper developing 1 and 2 MHz PZT air transducers with single λ/4 silicone rubber matching layer (Z = 1 MRayl) and two rangefinder systems: (1) time-of-flight using zero-crossing counter, and (2) phase measurement using frequency sweep. Achieves 52 dB two-way insertion loss at 2 MHz; both ranging systems achieve ~0.5 mm accuracy at 2–40 cm range in transmission mode.

## Unique contribution
First demonstration of a computer-controlled phase measurement ranging system for air-coupled ultrasound. Phase system uses frequency sweep (nulling phase detector, HP-85 computer control) to measure range from zero-crossing spacing: r = p/2(n − m) wavelengths. Achieves 0.04 mm instantaneous accuracy and 0.004 cm (0.04 mm) averaged (11 sweeps) standard deviation in transmission mode. Identifies atmospheric turbulence and temperature drift as dominant error source in phase measurement (±200° phase fluctuations from air motion).

## Key concepts
- Transducer: PZT-5H + RTV-615 silicone rubber matching layer (Z=1 MRayl, single λ/4); focused and unfocused geometries
- Insertion loss: ~42 dB theoretical; 52 dB measured (difference due to mechanical Q of silicone + PZT damping)
- Optimal single ML for PZT-air: Z_opt = 0.08 MRayl — not achievable; silicone at 1 MRayl is closest practical
- KLM model used for transducer design
- Time-of-flight system: synchronous gate + zero-crossing counter; measures absolute path length directly
- Phase system: cw swept frequency; phase null spacing gives integer number of wavelengths in path
- Phase accuracy: 0.05° null determination; instantaneous 0.04 cm; averaged over 11 sweeps: 0.004 cm
- Atmospheric noise: ±200° phase noise from thermal gradients, fans, convection; limits practical accuracy

## Methods / results / takeaways
- Operating frequencies: 780 kHz and 1 MHz (time-of-flight), 780 kHz (phase)
- Time-of-flight (echo mode): range 2–10 cm; absolute accuracy ±0.04 cm; rms error 0.02 cm
- Phase measurement (transmission mode): range 0–40 cm; instantaneous ±0.04 cm; averaged ±0.004 cm
- Minimum range (echo): ~2 cm due to transducer ringing (several cycle pulse)
- Maximum range (transmission at 780 kHz): 40 cm path; 52 dB total loss
- Applications: robotic ranging, noncontacting profile measurement, inspection of transparent/multi-colored objects
- Follow-up: Yano et al. 1987 (lower insertion loss with new ML materials); Khuri-Yakub et al. 1988 (new design)
