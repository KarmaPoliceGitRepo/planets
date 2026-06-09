# Phase Unwrapping
**Aliases:** 2πn ambiguity removal; phase unwrapping; phase velocity dispersion; continuous phase

**Definition:** Phase unwrapping is the process of resolving the 2πn integer ambiguity in a wrapped phase spectrum to recover a continuous phase function. The DFT returns phases in (−π, π]; any phase change greater than π between adjacent frequency bins is assumed to be a wrap and is corrected by adding or subtracting 2π. Errors propagate when the true phase change between bins actually exceeds π (due to insufficient sampling or noise). In ultrasonic dispersion measurements, the unwrapped phase spectrum φ(ω) of the through-transmitted signal yields the phase velocity c(ω) = ωΔx/φ(ω), where Δx is the propagation distance.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [hilbert-transform](hilbert-transform.md)
- related: [time-of-flight](time-of-flight.md)
- related: [dispersion-curves](dispersion-curves.md)

**Discussed in:**
- [Hilbert Transform notes (Coffee Morning)](../notes/signal-processing/hilbert-transform-notes-coffee-morning.md) — instantaneous phase and its relationship to wrapped DFT phase
- [CW Ultrasonic Phase Velocity Formula](../notes/signal-processing/cw-ultrasonic-phase-velocity-formula.md) — phase unwrapping applied to extract continuous-wave phase velocity
- [Ting & Sachse 1978 — Dispersion](../notes/microstructure/ting-sachse-dispersion-1978.md) — phase unwrapping of broadband through-transmission spectra to obtain continuous phase velocity vs. frequency
- [Peters & Petit 2003 — Broadband](../notes/microstructure/peters-petit-broadband-2003.md) — broadband phase-velocity measurement using unwrapped FFT phase spectra
