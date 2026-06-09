# Hilbert Transform and HHT — Coffee Morning Presentation Notes

- **Source:** Hilbert transform.docx
- **Drive link:** https://drive.google.com/file/d/1Kb_hIHJHYmvY0PAjPvkdA1FwRYmZXn6T/view
- **Type:** notes
- **Author/Year:** Unknown / undated
- **Coverage:** full

## Overview
Brief working notes from an internal "coffee morning" presentation demonstrating: (1) an FFT-based implementation of the Hilbert transform in MATLAB; (2) use of the Hilbert transform to extract instantaneous frequency; (3) an introduction to HHT (Hilbert-Huang Transform) with Intrinsic Mode Functions (IMFs) and the detrending/envelope concept. Includes worked MATLAB code.

## Unique contribution
Provides a practical, working MATLAB implementation of the Hilbert transform via FFT manipulation (rotating positive and negative frequency components), contrasted with MATLAB's built-in hilbert() function, with an application to instantaneous frequency extraction from real ultrasonic data.

## Key concepts
- Hilbert transform
- Hilbert-Huang Transform (HHT)
- Intrinsic Mode Function (IMF)
- Instantaneous frequency
- Instantaneous phase
- Empirical Mode Decomposition (EMD)
- Detrending / envelope
- FFT-based computation

## Methods / results / takeaways
- FFT-based Hilbert transform: take FFT of signal; multiply positive frequencies by −i (rotate by −90°) and negative frequencies by +i; take IFFT to obtain the analytic signal imaginary part.
- Instantaneous frequency: rate of change of phase angle of the analytic signal; plotted as dots alongside the phase angle time series.
- Issues noted: for broadband signals the Hilbert transform instantaneous frequency is not meaningful.
- HHT/EMD: decomposes signal into IMFs by iterative sifting (finding upper and lower envelopes, subtracting mean); each IMF is approximately mono-component.
- Detrending step: subtract mean of upper and lower envelopes from signal to obtain less noisy residual.
- MATLAB code provided for manual Hilbert computation and comparison with built-in hilbert() function.
- Data used: 9 mm steel, 10 MHz, 3 cycles.
