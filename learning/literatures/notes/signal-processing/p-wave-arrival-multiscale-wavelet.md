# Automatic P-Wave Arrival Detection with Multiscale Wavelet Analysis

- **Source:** 2003 - Automatic P-Wave Arrival Detection and Picking with Multiscale Wavelet Analysis...pdf
- **Drive link:** https://drive.google.com/file/d/1km_klNsvMkYhqPW_bguJGqgzqsoQAFGr/view
- **Type:** paper
- **Author/Year:** Zhang, Thurber & Rowe / 2003
- **Coverage:** full

## Overview
Published in Bulletin of the Seismological Society of America (2003). Presents the W-AIC picker, which combines the Akaike Information Criterion (AIC) autopicker with multiscale discrete wavelet transform (DWT) analysis to robustly detect and pick P-wave arrivals in seismic data, even in low-SNR conditions.

## Unique contribution
The W-AIC method applies DWT multi-resolution denoising before the AIC characteristic function, substantially improving pick accuracy for noisy records. Validated on Dead Sea Seismic Network and Parkfield HRSN datasets with reported accuracy of 81% within 0.2 s and 93% within 0.1 s respectively.

## Key concepts
- P-wave arrival picking
- AIC (Akaike Information Criterion) autopicker
- Discrete wavelet transform (DWT), multiresolution analysis
- Characteristic function
- Seismic noise reduction
- W-AIC picker

## Methods / results / takeaways
- AIC picker computes the AIC characteristic function from the seismogram; the global minimum marks the onset.
- W-AIC adds DWT-based denoising prior to AIC computation: the signal is decomposed into approximation and detail coefficients; high-frequency detail coefficients dominated by noise are zeroed/thresholded before reconstruction.
- Multiscale analysis allows selective suppression of noise at different frequency bands without distorting the onset.
- Dead Sea dataset (81 records): 81% of picks within 0.2 s of analyst picks.
- Parkfield HRSN dataset (108 records): 93% within 0.1 s.
- Method outperforms single-scale approaches at low SNR.
