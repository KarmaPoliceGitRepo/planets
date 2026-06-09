# Oscilloscope and Probe

**Aliases:** oscilloscope; DSO; digital storage oscilloscope; scope probe; ×10 probe; probe compensation; effective bandwidth (DSO); Equivalent Time Sampling; ETS; box averaging; loading effect

**Definition:** A digital storage oscilloscope (DSO) samples an input voltage waveform in real time or equivalent-time, displays it, and provides measurements. Key specifications: bandwidth (−3 dB frequency, equal to sample rate/2 as a practical limit); sample rate (typically 4–5× the bandwidth for accurate capture); vertical resolution (ADC bits); memory depth. A ×10 passive probe attenuates the signal 10× and has a bandwidth-limiting RC network; probe compensation (trimmer capacitor) must be adjusted so R₁C_c = R₂C_L for flat frequency response. The loading effect: a probe presents ~10 MΩ ‖ ~10 pF to the circuit, loading high-impedance nodes. Equivalent Time Sampling (ETS) extends bandwidth for repetitive signals by interleaving samples shifted by picoseconds between trigger events.

**Key relations:**
- [transmission-line](transmission-line.md) — probe cables are transmission lines; unterminated ends cause reflections
- [analogue-filter-basics](analogue-filter-basics.md) — probe RC network is a first-order filter
- [s-parameters](s-parameters.md) — VNA is a high-frequency alternative to oscilloscope for frequency characterisation

**Discussed in:**
- [Oscilloscope Tutorial](../notes/data-sheets/oscilloscope-tutorial.md) — bandwidth, sampling, triggering, probe compensation, ETS, box averaging
- [Oscilloscope Probes](../notes/00-general-electronics/oscilloscope-probes.md) — probe circuit model, loading effect, compensation trimmer procedure
