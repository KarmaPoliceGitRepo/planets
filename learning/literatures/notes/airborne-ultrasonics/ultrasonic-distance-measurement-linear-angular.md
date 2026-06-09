# Ultrasonic Distance Measurement for Linear and Angular Robot-Arm Positioning

- **Source:** Marioli et al. 1988 ultrasonic robot arm positioning
- **Drive link:** https://drive.google.com/file/d/1HJsW1ZtOKqyA6M_4zwQLsU_OhbfwhqQu/view
- **Type:** paper
- **Author/Year:** Marioli et al., 1988
- **Coverage:** full

## Overview
Describes a three-transducer (one TX, two RX) air-coupled ultrasonic system at 218 kHz for simultaneously measuring linear distance and angular orientation of a robot arm end-effector. Achieves angular accuracy of ±0.1° up to 200 mm range.

## Unique contribution
Demonstrates simultaneous linear and angular position recovery from a single ultrasonic burst using two spatially separated receivers. Provides early proof-of-concept for multi-transducer ultrasonic pose estimation applicable to robot arm feedback control.

## Key concepts
- Ultrasonic robot positioning
- TOF-based distance and angle measurement
- 218 kHz air-coupled transducers
- Multi-receiver geometry
- Angular accuracy
- Industrial robot feedback

## Methods / results / takeaways
- Configuration: 1 TX + 2 RX, separated by known baseline distance.
- Frequency: 218 kHz; transducers with matching layers.
- TOF to each receiver gives range; differential TOF gives angle.
- Angular accuracy: ±0.1° over 200 mm range.
- Linear accuracy: ~1 mm.
- Temperature compensation via thermistor; electronics based on threshold detection.
- Key limitation: threshold-based TOF detection is affected by amplitude variation (target reflectivity, angle of incidence); centre-of-mass or cross-correlation methods would improve robustness.
