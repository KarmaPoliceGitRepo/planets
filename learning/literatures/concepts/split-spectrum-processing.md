# Split-Spectrum Processing
**Aliases:** SSP; split-spectrum; coherent noise reduction; grain noise suppression; frequency diversity

**Definition:** Split-spectrum processing (SSP) is a signal-processing technique that divides a broadband ultrasonic signal into multiple narrow-frequency subbands, processes each subband independently, and then combines the results to reduce coherent (grain) scattering noise while preserving the deterministic flaw echo. Because grain scattering is frequency-dependent and random in phase, the subband signals have uncorrelated noise; recombination via polarity thresholding, minimisation, or product algorithms suppresses the noise more effectively than a single-band approach. SSP improves detection of small reflectors in coarse-grained or highly scattering materials.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [digital-filters](digital-filters.md)
- related: [spectral-leakage-and-windowing](spectral-leakage-and-windowing.md)

**Discussed in:**
- [Newhouse — Split-Spectrum Processing (1982)](../notes/microstructure/newhouse-split-spectrum-1982.md) — original SSP formulation; polarity-thresholding and product combination methods; experimental results in austenitic steel
