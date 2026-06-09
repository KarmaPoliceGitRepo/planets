# Determination of Absolute Material Nonlinearity with Air-Coupled Ultrasonic Receivers

- **Source:** Determination of absolute material nonlinearity with air-coupled ultrasonic receivers - (2017) David Torello.pdf
- **Drive link:** https://drive.google.com/file/d/1hYovhnuaM0V7OUAPV47akHPA2g0hB5eQ/view
- **Type:** paper
- **Author/Year:** D. Torello, N. Selby, J.-Y. Kim, J. Qu, L. J. Jacobs / 2017 (Ultrasonics 81, pp. 107–117)
- **Coverage:** full (deep read)

## Overview
An 11-page journal paper proposing a complete hybrid modeling and experimental framework for measuring the absolute acoustic nonlinearity parameter β using air-coupled piezoelectric receivers. The method combines the simplicity of contact piezoelectric transmitters with non-contact air-coupled detection, avoiding couplant variability and the optical complexity and cost of laser interferometry. A model-based calibration procedure converts the receiver's electrical output to absolute mechanical force, enabling quantitative extraction of β from second harmonic generation (SHG) measurements. Applied and validated on aluminum 2024 and fused silica specimens.

## Unique contribution
Provides the first complete calibration protocol for air-coupled receivers in SHG-based absolute β measurement. Rather than the self-reciprocity approach (impractical for air-coupled transducers due to very low SNR), a known reference specimen (Al 2024 with literature-established β) and a Multiple Gaussian Beam (MGB) propagation model are used to derive the force-to-voltage transfer function of the air-coupled receiver. This single calibration then applies to all subsequent measurements. The paper also explicitly models second harmonic propagation through the metal-to-air interface transmission (T ≈ 10⁻⁴), showing that the transmitted second harmonic generated in air by the fundamental wave is negligible and can be ignored.

## Key concepts
- Absolute acoustic nonlinearity parameter β
- Second harmonic generation (SHG)
- Air-coupled ultrasonics
- Nonlinear NDE / nonlinear ultrasound (NLU)
- Khokhlov-Zabolotskaya-Kuznetsov (KZK) equation
- Multiple Gaussian Beam (MGB) model
- Diffraction and attenuation corrections
- Model-based transducer calibration
- Nonlinear least-squares optimization
- Fatigue damage assessment
- Microstructural degradation monitoring

## Methods / results / takeaways

### Governing equations
- Relative β (uncalibrated): (A₂)_el / (A₁²)_el = β · x, where A₁, A₂ are electrical amplitudes at ω and 2ω.
- Absolute β: A₂ / A₁² = βk/(8) · 2x, requiring amplitude-calibrated measurements.
- KZK equation accounts for diffraction (transverse Laplacian term), dissipation (viscosity term), and nonlinear harmonic generation (third term) — Eq. (3) in paper.

### MGB model for multi-layer propagation
- Fundamental and second harmonic wave fields in the sample are modeled using Multiple Gaussian Beams (Eqs. 7–8), decomposing the source into N=15 Gaussian beam components (15 terms gives excellent convergence).
- At the metal-air interface, transmission coefficients T ≈ 0.985×10⁻⁴ (Al 2024/air) and 1.28×10⁻⁴ (fused silica/air): the ~80 dB insertion loss means higher-order transmitted harmonics (second harmonic of transmitted fundamental in air) are negligible.
- Transmitted fundamental and linearly propagating transmitted second harmonic are retained (Eqs. 9–10); all other components suppressed by T².
- Phase of transmitted wave: positive transmission coefficient means no phase flip at high-to-low impedance transmission (in contrast to the 180° phase flip of the reflection).
- Fig. 4 (rendered): contour maps of the computed wave fields in Al + 5 mm air column for both fundamental (ω) and second harmonic (2ω); the SHG buildup in the metal and the subsequent linear propagation in air are clearly visible.

### Transducer calibration
- Self-reciprocity calibration is impractical for air-coupled transducers (low SNR in pulse-echo through air).
- Instead: use MGB model with reference Al 2024 (well-characterized β) to predict the absolute pressure field at the air-coupled receiver face; integrate over receiver aperture to get predicted force; divide by measured voltage → force-to-voltage calibration function vs. frequency (Fig. 7 from paper: a smooth frequency-domain calibration curve).
- Receiver: Ultran NCT4-D13, center frequency 3.9 MHz, 12.5 mm diameter.
- Transmitter: Panametrics V106 (2.25 MHz, ½ inch) for Al; LiNbO₃ disc (2 MHz, ½ inch) for fused silica.
- Input: Agilent 33250A → Ritec SNAP 5000 amplifier → 1000 Vpp toneburst at 2.1 MHz, 12 cycles, 20 ms repetition rate.

### Signal processing
- FFT of steady-state portion of toneburst (treated as periodic) extracts amplitude and phase at ω and 2ω without windowing-induced amplitude errors.
- Hann windowing (preferred for relative β) is explicitly avoided here because it distorts amplitudes needed for absolute calibration.

### Optimization algorithm
- Nonlinear least-squares fit: first fit fundamental scan (p₀, attenuation α₁); then second harmonic scan using those inputs → extracts β.
- Parameters obtained simultaneously: source pressure p₀, fundamental/SH attenuation (α₁, α₂), and β. Table 1 in paper lists fitted values.
- Attenuation corrections found nearly negligible for both Al and fused silica at these frequencies (< 10 MHz).

### Results
- **Fused silica**: measured β = 12.1 ± 0.5. Literature range 9.7–14 [refs 24, 30, 34, 46]. Excellent agreement; LiNbO₃ source eliminates source nonlinearity contamination.
- **Aluminum 2024**: measured β = 5.0 ± 0.3. Literature range 4–12 across various heat treatments. Value falls within range but has caveat: commercial Panametrics V106 contributes source nonlinearity to the second harmonic. Side-lobe amplitudes in second harmonic fits differ from model, attributed to source effects.
- Scan results (Fig. 8, rendered): 2D spatial scans comparing air-coupled receiver and laser LDV (Polytec OFV-534 + OFV-5000 controller) at fundamental and second harmonic — Al scans show good radial symmetry; fused silica SH scan shows slight asymmetry indicating minor misalignment of air-coupled receiver.
- Curve fits (Fig. 9, rendered): measured vs. model curves in x-direction for Al (fundamental: tight fit; SH: accurate main lobe, minor side-lobe discrepancy) and fused silica (fundamental: accurate; SH: very accurate fit). High variability near 5 mm in fused silica fundamental attributed to defects in reflective tape used for LDV.
- Method measures |β|, not signed β: fused silica is known to have negative β (SH out of phase with fundamental); the method correctly captures magnitude.

### Key gotchas
- Source nonlinearity from commercial transmitters contaminates absolute β in metals; use LiNbO₃ sources or custom single-crystal transducers to avoid this.
- Air-coupled receiver alignment is critical: even small tilt breaks radial symmetry of the SH scan, introducing systematic errors.
- The calibration is valid only if the air gap and boundary conditions are controlled (air-coupling is repeatable; liquid couplant is not).
- Future extension to Rayleigh surface waves discussed (requires adapting KZK to surface propagation).

## Figures

**Fig. 1 (p. 1 rendered):** Schematic of the experimental setup showing (a) contact configuration and (b) air-coupled configuration. The contact setup has both transmitter and receiver clamped to the specimen surface with couplant; the air-coupled setup replaces the receiver with the Ultran air transducer held 5 mm above the specimen exit face on a 5-axis scanning stage. The transmitter remains contact-coupled to the sample top face.

**Fig. 2 (p. 2 rendered):** Multi-layer MGB model schematic. Panels (a)/(c) show the beam decomposition and re-expansion at the metal-air interface for fundamental and SH fields respectively. Panels (b)/(d) show convergence of the N=15 Gaussian beam representation at the interface — both fundamental and SH fields are accurately captured.

**Fig. 4 (p. 6 text description):** Contour maps of wave fields in Al (27 mm) and adjoining air (5 mm). (a) Fundamental in Al shows beam spread with propagation; (b) fundamental in air shows further diffraction and attenuation with a characteristic bell-shaped amplitude decay; (c) SH in Al clearly shows buildup of SHG from zero at the transmitter face to maximum at the exit; (d) SH in air shows linear propagation of the transmitted SH component, with amplitude decreasing monotonically.

**Fig. 5 (p. 6):** Radial profiles comparing pressure in air column with received force at transducer at ω (solid) and 2ω (dashed). The received force (area-weighted integral over aperture) has a narrower effective apparent width than the pressure field, because the center of the beam contributes more force per unit area. This difference between pressure and force profiles must be accounted for in the calibration.

**Fig. 8 (p. 9 rendered):** 2D scan maps comparing air-coupled receiver (AC) and laser LDV results for both specimens. Al fundamental (a) and SH (e) by AC show strong radial symmetry; laser scans (b, f) confirm this is physical. Fused silica AC fundamental (c) is symmetric; SH (g) is asymmetric — mismatch with laser result (d, h) indicates alignment error in AC receiver for that specimen.

**Fig. 9 (p. 9 rendered):** Nonlinear curve-fit results in x-direction for Al (top row, a/b) and fused silica (bottom row, c/d). Fundamental fits (a, c) in red circles (with error bars) and blue curve fits agree very closely for both materials. SH fit in Al (b) matches main lobe but shows side-lobe discrepancy attributed to source nonlinearity. SH fit in fused silica (d) is accurate throughout; the clean fit reflects the lower source nonlinearity of the LiNbO₃ transducer.

**Table 1 (p. 10):** Fitted model parameters — p₀ (source pressure), α₁ (fundamental attenuation), α₂ (SH attenuation) for both specimens. Attenuation coefficients are extremely small (<< 1 Np/m), confirming that diffraction corrections dominate and attenuation corrections are nearly negligible at these frequencies.
