# Sing-Around Technique
**Aliases:** sing-around method; Forgacs oscillator; feedback oscillator technique; sing-around frequency; pulse repetition rate method; frequency-tracking technique

**Definition:** In the sing-around (Forgacs oscillator) technique, the received ultrasonic pulse re-triggers the transmitter after a fixed electronic delay, creating a feedback loop whose repetition frequency f = 1/(TOF + t_delay) tracks the transit time. Changes in sound velocity (from temperature, stress, or composition changes) manifest as frequency changes, giving ppm-level velocity resolution from simple frequency counting. Resolution ~1 part in 10⁶ in velocity is achievable. The method is sensitive to electronic delay drift and multiple-reflection contamination; differential designs with two cavities (reference + sample) cancel common-mode drifts.

**Key relations:**
- related: [time-of-flight](time-of-flight.md)
- related: [phase-velocity](phase-velocity.md)
- related: [pulse-superposition-method](pulse-superposition-method.md)
- related: [temperature-dependence-of-sound-speed](temperature-dependence-of-sound-speed.md)

**Discussed in:**
- [Sing-Around Technique (effect-of-stress)](../notes/effect-of-stress/mcskimin-andreatch-1967.md) — sing-around vs pulse-superposition comparison for TOE constant measurement
- [Sing-Around (speed-of-sound)](../notes/speed-of-sound/alers-fleury-1963-velocity-sound-magnetic-fields.md) — frequency-tracking sing-around for velocity under magnetic field
- [Acoustoelectric Transducer (method-resonance)](../notes/method-resonance/ultrasonic-spectrum-analysis-frequency-tracked-rf.md) — frequency-tracked resonance method related to sing-around principle
- [Physical Acoustics Vol 12](../notes/range-measurement/physical-acoustics-vol-12.md) — systematic review of high-precision velocity measurement techniques including sing-around
