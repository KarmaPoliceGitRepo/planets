# Graphify input — Methods: Maths, Signal Processing & Tools (literature corpus)

## Overview
This corpus covers the mathematical and computational foundations underpinning ultrasonic measurement and structural health monitoring research: discrete/continuous signal processing theory (Fourier, wavelets, Kalman, Gaussian processes), applied mathematics (PDEs, linear algebra, tensor calculus, nonlinear dynamics), tool-chain skills (LabVIEW DAQ, MATLAB/Python DSP), and research-methodology hygiene (experimental design, error analysis). It exists to give the researcher a single reference layer across all supporting literature before diving into domain-specific acoustics or transducer material.

## Entities & Relationships

- **FFT (Fast Fourier Transform)** —efficient implementation of→ **DFT** : O(N/2 · log₂N) multiplications vs. N² for direct DFT; frequency resolution = f_s/N.
- **DFT** —associated with→ **spectral leakage + scalloping loss** : caused by implicit rectangular window when signal does not fit exactly in N samples; mitigated by windowing (Hann, Hamming, Blackman-Harris) at cost of main-lobe width.
- **Nyquist sampling theorem** —sets minimum rate for→ **alias-free reconstruction** : f_s ≥ 2 f_max; bandpass (subsampling) sampling exploits aliasing deliberately to downconvert, valid when f_s ≥ 2B (bandwidth), with SNR penalty ΔNF = 10 log(f₁/f₂) dB.
- **ToF estimation** —lower-bounded by→ **Cramér-Rao Lower Bound** : σ²_ToF ≥ 1/(SNR · 8π² · f_eff²); higher carrier frequency and broader bandwidth both tighten the bound.
- **parabolic interpolation on cross-correlation peak** —achieves near→ **CRLB** : when f_s > 2 × (noise-signal PSD crossing frequency); x16 upsampling before interpolation recovers accuracy at low f_s/f_c ratios.
- **Hilbert transform** —produces→ **analytic signal / instantaneous phase** : used for ToF zero-crossing methods, phase-based temperature compensation, and extracting instantaneous frequency (meaningful only for mono-component signals).
- **EMD (Empirical Mode Decomposition)** —decomposes into→ **IMFs (Intrinsic Mode Functions)** : adaptive sifting; each IMF has one extremum per zero-crossing and symmetric envelopes; basis is data-driven, not prescribed a priori (unlike Fourier/wavelets).
- **Hilbert-Huang Transform (HHT)** —combines→ **EMD + Hilbert spectral analysis** : produces time-frequency-amplitude representation with no a priori basis; completeness and orthogonality not guaranteed.
- **DWT (Discrete Wavelet Transform)** —implemented via→ **Mallat MRA filter bank** : iterated two-channel low-pass/high-pass filter bank with downsampling; approximation + detail coefficients at each level.
- **wavelet denoising** —applies→ **thresholding to detail coefficients** : hard threshold (set small to zero) or soft threshold (shrink by λ); universal threshold λ = σ√(2 log N) for white Gaussian noise; SURE threshold is data-adaptive.
- **temperature compensation (guided waves)** —addressed by methods→ **BSS / scale transform / DTW / Hilbert phase / OMP / physics model** : BSS/scale transform assume uniform time dilation (fails for dispersive waves, large ΔT); DTW allows non-uniform warping; Mariani (2019) separately compensates velocity change (time-warp) and residual phase shift.
- **TV regularization** —outperforms→ **bandpass filtering** for ultrasonic pulse echo denoising : SNR increase >400% vs. raw signal; MM (Majorization-Minimization) algorithm solves the non-differentiable TV objective efficiently.
- **Kalman-Bucy filter** —governed by→ **Riccati differential equation** : optimal linear recursive estimator for continuous-time state-space systems with Gaussian noise; dual of LQR problem.
- **Gaussian process regression (GPR)** —optimised via→ **log marginal likelihood** : hyperparameters {length-scale l, signal variance σ_f², noise variance σ_n²} tuned by gradient-based optimisation; provides calibrated predictive uncertainty.
- **Christoffel tensor** —eigenvalues give→ **seismic/elastic phase velocities** : T_ik = C_ijkl n_j n_l; three eigenvalues yield qP, qS1, qS2 velocities; applies Voigt notation (6×6) for the 4th-rank elastic stiffness tensor.
- **Neumann's principle** —constrains→ **tensor form of physical properties** : crystal point-group symmetry elements must be included in property symmetry; used to reduce independent elastic constants.
- **PDE classification** —determines solution method→ **separation of variables / Green's functions / characteristics** : wave eq. (hyperbolic) → d'Alembert/characteristics; heat eq. (parabolic) → Fourier series + separation of variables; Laplace eq. (elliptic) → Green's functions.
- **transfer function poles/zeros** —determine→ **system stability and frequency response** : all poles in left-half s-plane ↔ BIBO stability; complex poles near imaginary axis → resonance peak; Bode slope changes ±20 dB/decade per pole/zero.
- **LabVIEW G language (dataflow)** —implements→ **DAQ state machine / producer-consumer architectures** : state machine uses enum-driven case structure + shift register; producer-consumer decouples acquisition from processing via queue; action engine stores persistent state in uninitialized shift register.
- **TDMS file format** —used for→ **high-speed NI DAQ data streaming** : NI binary format with metadata; imports directly to Excel; preferred over ASCII for high-rate logging.
- **experimental error (random)** —reduces as→ **1/√N** with repeated measurements : standard error of mean = σ/√N; weighted mean weights each observation by 1/σ².
- **randomisation + blinding** —prevent→ **systematic bias in tribology experiments** : Watson 2019 audit: only 3.2% of tribology papers randomised samples, 2.2% blinded; ball-on-flat CoV between labs ≈49%, requiring ≥21 repeats for 5% SEM.
- **robust PCA (RPCA) orthogonal distance** —used as→ **damage-sensitive SHM feature** : OD = distance from data point to PCA subspace; RPCA is resistant to outlier contamination; temperature compensation applied directly to the RPCA-OD feature.
- **pulse superposition method (McSkimin 1962)** —requires→ **bond-layer phase correction** : bond layer introduces phase shift γ independent of T/P when operated at transducer resonance; accuracy ~few parts in 10⁵ for p=2.

## Glossary

- **SNR (signal-to-noise ratio)** — ratio of signal power to noise power, expressed in dB as 20·log₁₀(V_signal/V_noise); signal averaging over N trials improves SNR by √N.
- **ToF (time-of-flight, TOF)** — time taken for a signal to travel from transmitter to receiver; central measurement in ultrasonic ranging, velocity, and thickness sensing.
- **CRLB (Cramér-Rao Lower Bound)** — theoretical minimum variance of any unbiased estimator; for ToF: σ²_ToF ≥ 1/(SNR · 8π² · f_eff²).
- **DWT (discrete wavelet transform)** — multi-resolution signal decomposition via iterated filter banks; basis functions are compact-support wavelets (Haar, Daubechies); opposite of FFT in that it gives time-scale rather than time-frequency resolution.
- **IMF (Intrinsic Mode Function)** — elementary component from EMD: one extremum between zero-crossings, symmetric upper/lower envelopes; input to HHT for instantaneous frequency.
- **temperature compensation (TC)** — signal-processing correction for thermally induced changes in guided wave speed, phase, or amplitude; spectrum of methods from simple stretch (BSS) to physics-based models.
- **Lamb waves (guided plate waves)** — elastic guided waves in plate-like structures; symmetric (S) and antisymmetric (A) mode families; dispersive — velocity depends on frequency × thickness.
- **Voigt notation** — compact 6×6 matrix representation of the 4th-rank elastic stiffness tensor C_ijkl; exploits stress/strain symmetry; compliance Voigt matrix needs factors of 2 and 4.
- **Christoffel tensor (acoustic tensor)** — T_ik = C_ijkl n_j n_l; eigenvalues give phase velocities in direction n; eigenvectors give polarisations.
- **PSD (power spectral density)** — frequency-domain power distribution per unit frequency; estimated by Welch method (overlapping windowed segments, averaged periodogram).
- **Green's function** — PDE solution for a delta-function source; full solution = convolution of Green's function with the actual source distribution.
- **ARMA model (AutoRegressive Moving Average)** — parametric model combining AR and MA components; used to characterise transducer transfer function for inverse (compensation) filter design.
- **TDMS (Technical Data Management Streaming)** — NI binary file format for high-rate DAQ; stores time-stamped measurements with metadata; alias: .tdms.
- **Kalman-Bucy filter** — continuous-time optimal linear state estimator for state-space systems with Gaussian noise; gain K = PH'R⁻¹ where P obeys the Riccati differential equation.
- **GPR (Gaussian Process Regression)** — non-parametric Bayesian regression providing calibrated predictive uncertainty; hyperparameters optimised via log marginal likelihood.
- **error propagation (propagation of uncertainty)** — for y = f(x₁,…,xₙ), σ_y² = Σ(∂f/∂xᵢ)²σ_xᵢ²; independent errors combine in quadrature.
- **statistical power** — probability 1−β of detecting a real effect of a given size; depends on sample size, effect size, and significance threshold α.
- **DTW (Dynamic Time Warping)** — algorithm finding the optimal non-linear alignment between two time series by dynamic programming; handles dispersive signal distortion better than global time-stretch.
- **TV regularization (Total Variation, ROF model)** — penalises total variation of solution, promoting piecewise-smooth results; solved via MM algorithm; outperforms bandpass filtering for ultrasonic pulse-echo SNR.
- **subsampling (bandpass sampling, undersampling)** — sampling a bandpass signal below Nyquist for the carrier, exploiting aliasing to downconvert; minimum valid rate = 2B; SNR degrades as 10 log(f₁/f₂) dB.

## Key findings

- CRLB for ToF: σ²_ToF ≥ 1/(SNR · 8π² · f_eff²); higher carrier frequency and broader signal bandwidth directly reduce the minimum achievable ToF error. Each additional ADC bit adds ~6 dB SNR.
- Parabolic interpolation on the cross-correlation peak achieves near-CRLB ToF accuracy when f_s exceeds twice the noise-signal PSD crossing frequency; x16 upsampling prior to interpolation recovers accuracy at low f_s/f_c.
- Temperature induces two distinct effects on guided wave signals: (1) velocity change → time-axis scaling (addressed by BSS/scale transform/DTW); (2) independent phase shift (addressed by Hilbert-transform phase correction, Mariani 2019). Methods addressing only one effect leave residual error.
- DTW outperforms global stretch (BSS, scale transform) for large temperature variations (>20 °C), long propagation distances, or high frequencies where dispersion breaks the uniform-dilation assumption.
- TV and Tikhonov regularization increase ultrasonic pulse-echo SNR by >400% vs. unprocessed signals and substantially outperform bandpass filtering; the MM algorithm provides efficient iterative solution.
- Wavelet denoising: DWT with Daubechies-2 at 10 levels, summing detail levels D3+D4+D5, achieves 4.1% error for cortical bone thickness from ultrasound. Universal threshold λ = σ√(2 log N) works well for white Gaussian noise; SURE threshold is data-adaptive.
- Single-bit (delta-sigma) cross-correlation replaces multiply-accumulate with EXOR logic; implementable in simple digital logic/FPGA for low-cost ultrasonic ranging.
- Multifrequency AM ranging using the vernier principle (e.g., 44 kHz carrier, 4.4 kHz and 440 Hz modulation) resolves range ambiguity and achieves ~1% accuracy over several metres.
- Subsampling receiver SNR degradation: ΔNF(dB) = 10 log(f₁/f₂); a 16-QAM signal at 99 MHz dropped from 200 Msps to 100 ksps gave ~34 dB noise floor rise, matching the formula.
- Pulse superposition velocity measurement (McSkimin 1962): accuracy ~parts in 10⁵; bond-layer phase correction is essential and can be made temperature-insensitive by operating at transducer resonance frequency.
- Watson (2019) tribology audit: <5% of papers in top journals used randomisation, blinding, or statistical tests; ball-on-flat CoV between labs ≈49% (within lab ≈23%); ≥21 tests needed for 5% SEM. Recommended: pre-register, power analysis, p < 0.005 threshold.
- HHT/EMD advantage over Fourier/wavelets: adaptive, data-driven basis; no spectral leakage; meaningful instantaneous frequency for nonlinear signals. Caveat: completeness and orthogonality of EMD decomposition are not mathematically guaranteed.
- Gibbs phenomenon: Fourier series near jump discontinuities always overshoots by ~9%, regardless of number of terms retained.
- Christoffel tensor eigenvalues give elastic/seismic phase velocities in anisotropic media; P and S are strictly "quasi" (qP, qS) in anisotropic solids because particle motion is not exactly parallel/perpendicular to propagation.
- LabVIEW producer-consumer architecture decouples acquisition from processing, preventing buffer overflow at high DAQ rates; action engine pattern provides clean mutable shared state without global variables.

## Gotchas

- **Instantaneous frequency is only meaningful for mono-component signals.** Applying Hilbert transform directly to broadband signals gives physically meaningless instantaneous frequency; EMD decomposition into IMFs is needed first.
- **DTW is not always better.** For small temperature variations (<20 °C) or short propagation distances, BSS/scale transform is computationally cheaper and comparably accurate; DTW overhead is only justified when dispersion makes uniform stretch a poor assumption.
- **Bond-layer phase correction is mandatory for CW resonance velocity measurements.** Even a "thin" bond layer introduces a measurable frequency shift; ignoring it (as Bolef-Menes or Ringermacher approximations do) causes systematic velocity error, especially for small dv/dT or dv/dP measurements.
- **Spectral leakage vs. resolution trade-off.** Windowing reduces leakage but widens the main lobe and reduces amplitude accuracy (scalloping loss); Blackman-Harris gives ~61 dB sidelobe suppression but causes ~5–7 dB peak attenuation — do not compare peak amplitudes across different window choices without normalisation.
- **Quantisation noise model breaks for non-uniform quantisers.** Orfanidis's noise model (variance = Δ²/12, white) assumes uniform ADC; oversampling reduces in-band noise by 10 log₁₀(M) dB, noise shaping improves further — but only if ADC non-linearity is below the noise floor.
- **Parabolic interpolation error dominates below the CRLB threshold.** When f_s < 2 × f_intersection (noise-signal PSD crossing), interpolation bias exceeds the CRLB; upsampling (x16) before interpolation is required.
- **Systematic errors do not average out.** Unlike random errors (which reduce as 1/√N), systematic biases (calibration offsets, bond layers, environmental drift) must be identified and corrected separately; inspect residuals for curvature or non-zero intercepts.
- **Stopping LabVIEW does not stop connected hardware.** High-voltage/high-current supplies, serial ports, and GPIB instruments can remain active after a VI stops; hardware must be explicitly cleared/closed in the VI's error-handling path, and physical safety measures should not rely on software shutdown.
- **EMD completeness and orthogonality are not guaranteed.** The sifting process is empirical; IMF decompositions are neither provably complete nor orthogonal, making rigorous uncertainty quantification on HHT spectra difficult.
- **Voigt compliance matrix factors of 2 and 4.** When converting elastic stiffness C_ijkl to Voigt notation, off-diagonal compliance entries must be multiplied by 2 or 4 (depending on index position) to preserve the correct stress-strain relationship — a common source of numerical error.
- **Significance threshold p < 0.05 is likely too permissive.** Watson (2019) and the replication-crisis literature advocate p < 0.005; with typical tribology CoVs of ~23–49%, underpowered studies (median n=1 in the audit) produce unquantifiable false-positive rates.
- **ARMA-based inverse filter assumes stationary, linear transducer response.** If the transducer coupling or temperature changes between calibration and measurement, the compensation filter becomes invalid; re-calibrate regularly.
