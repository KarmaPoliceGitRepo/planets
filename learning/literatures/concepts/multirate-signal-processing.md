# Multirate Signal Processing
**Aliases:** multirate signal processing; polyphase filter; polyphase filter bank; decimation; interpolation; subsampling; subsampling receiver; oversampling; equivalent time sampling; multiresolution analysis

**Definition:** Multirate signal processing processes signals at more than one sample rate within the same system. Downsampling (decimation) by integer M retains every M-th sample; a lowpass anti-aliasing filter must precede it to avoid aliasing. Upsampling (interpolation) by L inserts L−1 zeros then lowpass filters to reconstruct missing samples. The polyphase decomposition splits a filter into M parallel lower-rate filters applied to the interleaved input streams, reducing computation by M×. Polyphase filter banks implement critically sampled subband decomposition. A subsampling receiver under-samples a bandpass signal so that the desired IF band aliases to a convenient base-band position, allowing direct conversion at a modest sample rate.

**Key relations:**
- related: [sampling-and-aliasing](sampling-and-aliasing.md)
- related: [digital-filters](digital-filters.md)
- related: [fast-fourier-transform](fast-fourier-transform.md)

**Discussed in:**
- [LabVIEW DSP and Digital Communications](../notes/matlab-and-labview/labview-dsp-digital-communications.md) — polyphase decimation and interpolation; subsampling receiver implementation; multirate filter banks
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — multirate theory; polyphase identity; decimation filter design
