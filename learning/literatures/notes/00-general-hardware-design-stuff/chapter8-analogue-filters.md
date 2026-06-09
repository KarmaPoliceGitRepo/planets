# Analog Filters (Chapter 8 — Basic Linear Design)

- **Source:** Chapter8 - Analogue Filters.pdf
- **Drive link:** https://drive.google.com/file/d/1VSJ20N0UeMQ8hfRYiwxpf3B3z7VSNwR_/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Analog Devices (Basic Linear Design series); approx. 2000s
- **Coverage:** partial (large PDF ~143 pages; text extraction stopped mid-Section 8.6 around page 8.76; Sections 8.7 Practical Problems and 8.8 Design Examples not captured)

## Overview
This is Chapter 8 of Analog Devices' *Basic Linear Design* reference book, providing a comprehensive treatment of analog filter design. It moves from first principles (transfer function, poles/zeros, s-plane analysis) through the major standard filter approximations (Butterworth, Chebyshev, Bessel, elliptic, etc.) and then to active and passive circuit topologies for realizing those approximations. Frequency domain and time domain behaviour are treated in parallel throughout. The chapter is aimed at practicing electronics engineers who need to select, design, and implement analog filters without getting deeply into the underlying mathematical proofs.

## Unique contribution
This chapter serves as a self-contained, single-reference engineering handbook for analog filter design. Its particular strength is the combination of (a) normalised design tables and response curves for 2–10 pole variants of every major approximation (Butterworth, five Chebyshev ripple levels, Bessel, linear phase with equiripple error, Gaussian to 6 dB and 12 dB, elliptic, inverse Chebyshev, maximally flat delay with Chebyshev stop band), and (b) detailed worked frequency-transformation examples (LP→HP, LP→BP, LP→notch using Geffe's algorithm) alongside explicit design equations for each active topology. The pairing of theory, response curves, design tables, and circuit equations in one place is the key practical utility.

## Key concepts
- Transfer function H(s), poles and zeros, s-plane
- F0 (cutoff frequency) and Q (quality factor), damping ratio α = 1/Q
- Passband, stopband, transition band, passband ripple (Amax), minimum stopband attenuation (Amin)
- Filter order and the –20 dB/decade per pole rolloff rule
- Butterworth (maximally flat) response
- Chebyshev response (equiripple passband); 0.01, 0.1, 0.25, 0.5, 1 dB variants
- Bessel filter (maximally flat group delay / linear phase)
- Linear phase with equiripple error (0.05° and 0.5° variants)
- Transitional filters: Gaussian to 6 dB and 12 dB
- Elliptic (Cauer) filter — ripple in both bands, fastest transition
- Inverse Chebyshev — monotonic passband, ripple in stopband
- Maximally flat delay with Chebyshev stop band
- Group delay and nonlinear phase distortion; envelope delay
- Impulse response and step response; overshoot, ringing
- Low-pass prototype normalisation and denormalisation
- LP→HP, LP→BP, LP→notch, LP→all-pass frequency transformations
- Geffe algorithm for LP→BP pole conversion
- All-pass filter for phase equalisation
- Single-pole RC section (active and passive)
- Passive LC ladder (full and half sections, m-derived sections)
- General Impedance Converter (GIC)
- Active inductor, Frequency Dependent Negative Resistor (FDNR)
- Sallen-Key (VCVS) topology — low-pass, high-pass, band-pass
- Multiple Feedback (MFB) topology — low-pass, high-pass, band-pass
- State variable filter
- Biquad filter
- Dual Amplifier Band-Pass (DABP)
- Twin-T notch, Bainter notch, Boctor notch
- First and second order all-pass sections

## Methods / results / takeaways

**Filter type selection trade-offs:**
- Butterworth: best all-round compromise; no ripple in either band; moderate transition steepness and transient response.
- Chebyshev: sharper amplitude rolloff at the cost of passband ripple and poorer step/impulse response (more ringing). Higher ripple → steeper roll-off.
- Bessel: best phase linearity (constant group delay) and transient response; worst amplitude discrimination.
- Elliptic: shortest possible transition region for a given order; ripple in both pass and stop bands; worst transient response.
- Inverse Chebyshev: monotonic passband, ripple stopband; intermediate transient performance; steepest rolloff in the transition band.
- Linear phase with equiripple error: extends linear phase further than Bessel into stopband; slight overshoot in step response.
- All-pole filter ranking by amplitude discrimination (best→worst): Chebyshev > Butterworth > Bessel.
- Same ranking reversed for time domain (best transient → worst): Bessel > Butterworth > Chebyshev.

**Pole Q and peaking:** For a two-pole low-pass section, Q > 0.707 causes passband peaking; Q < 0.707 produces earlier and gentler rolloff.

**Frequency transformations (key results):**
- LP→HP: replace s with 1/s; capacitors ↔ inductors in passive, resistors ↔ capacitors in active (frequency-setting elements only); add n zeros at origin.
- LP→BP (narrowband, < 2-octave separation): use Geffe algorithm. Each LP pole pair splits into two BP sections (order doubles); Q_BP = F0/BW; resonant frequency is geometric mean of the two band edges. Worked example: 3-pole 1 dB Chebyshev at BW=0.5 Hz, F0=1 Hz → three sections at FBP1=0.803, FBP2=1.245, FBP3=1 Hz with section Q values 9.07 and 4.43.
- LP→notch (narrowband): QBR = F0/BW; each LP pole pair → two notch sections plus imaginary zeros at F0 (the notch frequency is the geometric mean of the two section frequencies). Worked example: 3-pole 1 dB Chebyshev, BW=0.1 Hz, F0=1 Hz → section Q values 36.8 and 4.45.
- Single-frequency notch Q requirement: Q = (ω0/B)·√(10^(0.1A) – 1) where A is required attenuation in dB and B is the bandwidth.

**Active topologies:**
- Sallen-Key: op amp used as amplifier (not integrator); highest frequency capability for a given op amp; noninverting; low component spread; Q very sensitive to gain setting; difficult to tune due to component interaction. Special case: gain=2 gives equal R and equal C values.
- Multiple Feedback (MFB): op amp as integrator; inverts phase (adds 180° shift); higher component spread than Sallen-Key; limited to Q < ~20 before op-amp gain-bandwidth becomes a constraint (rule: open-loop gain should exceed filter response including Q peaking by at least 20 dB). F0 tunable via R2 (variable); Q tunable via R5.
- FDNR: derived from passive LC prototype via 1/s transformation; no op amps in signal path (lower noise); more components than active alternatives.

**Phase and time domain:**
- Each pole contributes 45° phase shift at the cutoff frequency, and 90° total shift far above it.
- Group delay = –dφ/dω; constant group delay requires linear phase; Bessel achieves this best in the passband.
- Nonlinear phase distorts complex waveforms (overshoot, ringing, envelope delay in AM signals).
- Rise time × bandwidth = constant for step response; impulse response amplitude × bandwidth = constant.
- Increasing filter order increases amplitude discrimination but also degrades transient response.
