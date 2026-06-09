# Near Field and Far Field
**Aliases:** near field; far field; Fresnel zone; Fraunhofer zone; near-field distance; Rayleigh distance; near-field length N; transition distance; Fresnel distance; near-field pressure oscillations

**Definition:** For a circular piston transducer of radius a and wavelength λ, the near field (Fresnel zone) extends to the Rayleigh distance N = a²/λ, where the on-axis pressure exhibits multiple maxima and minima from constructive/destructive interference of edge and central contributions. Beyond N (far field, Fraunhofer zone), the beam diverges regularly as a single main lobe with angular half-width θ_div ≈ λ/a. Beam amplitude in the far field follows a 1/r decay. Near-field complexity makes amplitude-based measurements unreliable close to the transducer; diffraction correction must account for the near-field phase shift when computing velocity from two-point TOF measurements.

**Key relations:**
- related: [diffraction-correction](diffraction-correction.md)
- related: [beam-focusing](beam-focusing.md)
- related: [piezoelectric-transducer](piezoelectric-transducer.md)
- related: [attenuation](attenuation.md)

**Discussed in:**
- [Near Field Fresnel Zone (range-measurement)](../notes/range-measurement/kelly-2003-nearfield-pressure-calculations.md) — analytical and numerical near-field pressure calculations for piston sources
- [Zemanek 1971 — Near-Field Vibrating Piston](../notes/range-measurement/zemanek-1971-nearfield-vibrating-piston.md) — classic near-field pressure maps for circular piston
- [Angular Spectrum Approach (range-measurement)](../notes/range-measurement/zeng-mcgough-2008-angular-spectrum.md) — near-to-far-field computation via angular spectrum decomposition
- [Schmerr & Sedov 1992 — Near-Field Model](../notes/range-measurement/schmerr-sedov-1992-near-field-model.md) — diffraction model bridging near and far fields
- [Olympus Transducers Technical Notes](../notes/range-measurement/olympus-transducers-technical-notes.md) — practical near-field distance formula and focus recommendations
- [Baggens 2015 — Impact-Echo Near Field](../notes/range-measurement/baggens-2015-impact-echo-near-field.md) — near-field effects in impact-echo Lamb wave measurement
