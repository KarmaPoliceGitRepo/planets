# Automatic Defect Detection in Industrial Ultrasound Images Using a Neural Network

- **Source:** 1996 - Automatic detection of defects in industrial ultrasound images using a neural network...pdf
- **Drive link:** https://drive.google.com/file/d/1y5bb0maHlH8bxQhPlSUOPk51hXO-iWEV/view
- **Type:** paper
- **Author/Year:** Lawson & Parker / 1996
- **Coverage:** full

## Overview
Published in SPIE Vol. 2786 (1996). Describes an MLP neural network approach to automatically segment TOFD (Time-of-Flight Diffraction) B-scan ultrasonic images to detect industrial weld defects, replacing labour-intensive manual interpretation.

## Unique contribution
Uses local area descriptors (variance, mean, maximum, minimum pixel values over a neighbourhood) as features fed to an MLP, with binary shape analysis applied post-classification to reduce false alarms. Includes TOF correction for probe geometry.

## Key concepts
- TOFD (Time-of-Flight Diffraction)
- B-scan imaging
- MLP (Multi-Layer Perceptron) neural network
- Local area descriptors (texture features)
- Binary shape analysis
- TOF correction
- Non-destructive testing (NDT)

## Methods / results / takeaways
- TOFD produces B-scan images where defect signatures appear as hyperbolic arcs.
- Feature extraction: a sliding window computes variance, mean, max, min over a local neighbourhood at each pixel.
- MLP trained on labelled images classifies each pixel as defect or background.
- Post-processing with binary shape analysis (erosion/dilation morphology) removes isolated false-positive pixels.
- TOF correction compensates for lateral-wave arrival time to align B-scan with true depth.
- Demonstrated on real weld inspection data; reduces operator workload significantly.
