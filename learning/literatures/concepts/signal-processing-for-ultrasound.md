# Signal Processing for Ultrasound (Applied)
**Aliases:** pulse-echo method; B-scan; A-scan; C-scan; baseline signal stretch; orthogonal distance; neural network defect detection; TOFD neural network

**Definition:** In pulse-echo ultrasonics, an A-scan is the raw time-domain waveform from a single transducer position; a B-scan stacks A-scans laterally to produce a depth-vs-position image; a C-scan maps amplitude or ToF at a fixed depth as a function of 2D position. The orthogonal distance from a reference curve (e.g., a Lamb-wave group velocity vs. frequency curve) is used as a damage index. Neural networks are trained on ToF diffraction (TOFD) or B-scan images to automatically classify or locate defects. Temperature compensation is essential before damage detection: even 1 °C shift can mimic a defect signal.

**Key relations:**
- related: [time-of-flight](time-of-flight.md)
- related: [structural-health-monitoring](structural-health-monitoring.md)
- related: [temperature-compensation](temperature-compensation.md)
- related: [split-spectrum-processing](split-spectrum-processing.md)

**Discussed in:**
- [TOFD Neural-Network Defect Detection](../notes/signal-processing/tofd-neural-network-defect.md) — neural-network classification of TOFD signals; feature extraction from time and frequency domains
- [Digital Signal & Image Processing (Blanchet)](../notes/signal-processing/digital-signal-image-processing-matlab-blanchet.md) — B-scan image processing; denoising and segmentation in 2D ultrasound
