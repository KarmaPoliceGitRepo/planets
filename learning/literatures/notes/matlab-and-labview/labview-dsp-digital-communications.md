# LabVIEW Digital Signal Processing and Digital Communications

- **Source:** Cory Clark - LabVIEW Digital Signal Processing-McGraw-Hill Professional (2005).pdf
- **Drive link:** https://drive.google.com/file/d/1BWeZGTdbijuwYxKqQefymmKsSOu1s2p0/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Cory L. Clark (Motorola) / 2005
- **Coverage:** partial (large PDF; extraction covers through the start of Ch. 4 of 9)

## Overview
A hands-on practitioner's guide that shows how to implement real-world digital signal processing and digital communications systems using LabVIEW. The book assumes the reader already knows DSP theory and basic LabVIEW VI construction, and focuses on bridging that theoretical knowledge into working virtual instruments. It progresses from signal acquisition hardware through spectral analysis, digital filtering, multirate processing, signal generation, and ultimately the assembly and performance evaluation of a complete digital communication receiver.

## Unique contribution
Unlike generic DSP textbooks, this book is structured around LabVIEW as the implementation platform and explicitly compares it to MATLAB and C for signal processing work. It provides concrete worked examples with specific NI hardware (PXI-5660 RF Signal Analyzer, Acqiris DP240), demonstrates subsampling / bandpass-sampling theory with real captured 16-QAM spectra, and includes a complete VI reference appendix. The subsampling SNR derivation (with Eq. 2.1–2.2) verified against measured data at 200 Msps vs. 100 ksps is a notable practical contribution.

## Key concepts
- Virtual Instrument (VI) and sub-VI architecture in LabVIEW
- Conventional digital receiver vs. subsampling (all-digital) receiver
- Nyquist sampling theorem; bandpass (undersampling) sampling
- Subsampling factor n; alias placement; subsampling SNR degradation
- Analog-to-digital converter (ADC) noise floor; quantization noise
- Fast Fourier Transform (FFT) vs. Discrete Fourier Transform (DFT)
- Spectral leakage; scalloping loss; windowing functions (Hann, Hamming, Blackman-Harris)
- Zero-padding for FFT efficiency and spectral resolution
- FIR filters (windowed design, equiripple/Parks-McClellan); linear phase
- IIR filters
- Multirate signal processing; upsampling; downsampling; polyphase filters; halfband filters
- Pulse-shaping filter; raised cosine / excess bandwidth factor α
- Complex mixer; sinc function; chirp; Rayleigh fading channel model; AWGN
- Digital modulation: QAM, QPSK, PSK, GMSK, OFDM
- Symbol error probability; bit-error rate (BER); error vector magnitude (EVM)
- Channel estimation; channel coding; Viterbi decoder
- PXI platform; NI Scope; NI Tuner; Spectral Measurements Toolset (SMT)
- GPIB; soundcard acquisition; NI DAQmx analog sampling cards
- DLL / code interface node (call library function node)
- AdvFFT.vi; FreqAxis.vi; DFT frequency bin spacing Δf = f_s/N

## Methods / results / takeaways
- Two receiver architectures: (1) conventional heterodyne (requires hardware LO + IF filter, used with NI PXI-5660), and (2) subsampling all-digital (only the ADC; used with Acqiris DP240 at up to 2 Gsps, 1 GHz bandwidth).
- Valid subsampling rates are bounded by 2f_H/n ≤ f_S ≤ 2(f_H – f_L)/(n–1). The minimum possible rate is 2B (twice signal bandwidth), independent of carrier frequency.
- SNR degradation from undersampling: ΔNF(dB) = 10 log(f_1/f_2). A 16-QAM signal at f_C = 99.003 MHz measured ~34 dB noise floor rise when dropping from 200 Msps to 100 ksps — matching the formula closely.
- For a 16-QAM system with R_S = 4800 sym/s and α = 0.2, a symbol error rate of 10⁻³ requires ≈20 dB SNR.
- Aliased image frequency after subsampling: f_IF = rem(f_C, f_S) for even n; f_S – rem(f_C, f_S) for odd n. A carrier at exactly 99.000 MHz would alias to DC (causing spectral overlap); choosing 99.003 MHz places the IF at 3000 Hz.
- DFT computation: N² multiplications vs. (N/2)log₂N for FFT — a factor >10,000 for N=200,000.
- Spectral leakage control: choose window based on side-lobe attenuation vs. main-lobe width tradeoff. Blackman-Harris provides ~61 dB side-lobe suppression, visibly smoothing spectral estimates at the cost of ~5–7 dB peak attenuation.
- Incorporating C/DLL routines via the call library function node enables custom or optimized algorithms (e.g., FFT, DCT, wavelets) to be embedded directly in VIs.
- LabVIEW's G language advantages over MATLAB for communications work: no memory allocation/compilation, integrated instrument control, real-time data display; disadvantage: slower execution than stand-alone instruments.
