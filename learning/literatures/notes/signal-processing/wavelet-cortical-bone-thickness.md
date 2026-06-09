# Wavelet Decomposition for Cortical Bone Thickness Measurement Using Ultrasound

- **Source:** Wavelet decomposition processing method- Cortical bone thickness measurement using ultrasound sensor - (2014) Hassan.pdf
- **Drive link:** https://drive.google.com/file/d/12F5upmWijmYQEnrArfvq5_wavz5bnMYj/view
- **Type:** paper
- **Author/Year:** Hassan et al. / 2014
- **Coverage:** full

## Overview
Published in IEEE International Conference on Systems, Man, and Cybernetics (SMC) 2014. Uses 10-level DWT with Daubechies-2 (db2) wavelet on ultrasonic pulse-echo signals to extract cortical bone boundaries, then combines specific detail levels (D3+D4+D5) for thickness estimation.

## Unique contribution
Identifies the optimal combination of DWT detail sub-bands (D3+D4+D5 at 10 levels of decomposition with db2) for isolating the cortical bone echo from soft tissue clutter, achieving 4.1% average measurement error.

## Key concepts
- Discrete wavelet transform (DWT)
- Daubechies-2 (db2) wavelet
- 10-level decomposition
- Detail coefficient selection
- Cortical bone thickness
- Ultrasound pulse-echo
- Non-destructive measurement

## Methods / results / takeaways
- Problem: cortical bone echoes overlap with soft tissue echoes and reverberation; direct threshold-based picking is unreliable.
- DWT with db2 at 10 decomposition levels separates signal components by frequency/scale.
- Detail levels D3, D4, D5 found to contain the relevant bone-wall reflection energy; summed and envelope-detected to localise echoes.
- Peak-to-peak time in the reconstructed signal from D3+D4+D5 gives the ToF between anterior and posterior cortical surfaces.
- Average error: 0.152 mm (4.1%) vs. caliper measurement.
- Correlation coefficient: 0.9797 vs. caliper across the test sample set.
