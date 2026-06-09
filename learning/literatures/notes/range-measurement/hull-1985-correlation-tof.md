# Digital Methods for Ultrasonic Time-of-Flight Measurement: Overlap, Phase-Slope, and Cross-Correlation

- **Source:** 1985 - Hull - correlation to find tof.pdf
- **Drive link:** https://drive.google.com/file/d/1gxPlcZNWQpUOPZqYQcVSxUxbLtq2inFN/view
- **Type:** paper
- **Author/Year:** D.R. Hull (NASA TM-83794) / 1985
- **Coverage:** full

## Overview
A NASA technical memorandum comparing three digital signal processing methods for pulse-echo ultrasonic velocity measurement: (1) peak-overlap, (2) phase-slope (FFT-based group delay), and (3) cross-correlation. Tests were conducted on metal and composite specimens.

## Unique contribution
Provides a direct empirical comparison of three TOF methods on real specimens, showing that cross-correlation yields the lowest random error for both metallic and attenuating composite materials, and explaining why each method performs as it does.

## Key concepts
- Time-of-flight (TOF) measurement
- Pulse-echo overlap method
- Phase-slope method (group delay via FFT)
- Cross-correlation method
- Digital signal processing for ultrasonics
- Attenuating materials (composites)
- Group delay

## Methods / results / takeaways
- **Overlap method**: Requires similar waveform shapes between echoes; peak matching. Sensitive to waveform distortion.
- **Phase-slope method**: Computes FFT of each echo, cross-multiplies (conjugate), takes angle of cross-spectrum; slope of unwrapped phase vs. frequency = group delay (TOF). Linear phase assumption.
- **Cross-correlation method**: Conjugate multiplication in frequency domain followed by inverse FFT; peak of resulting correlation gives TOF. Best for attenuating materials where waveform changes shape.
- Cross-correlation produced the lowest random error for both metal and composite samples.
- Phase-slope is intermediate; overlap method has the highest random error on composites.
- Practical recommendation: cross-correlation for general use, especially where frequency-dependent attenuation distorts waveform between echoes.
