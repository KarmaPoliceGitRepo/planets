# Dynamic Time Warping
**Aliases:** DTW; dynamic time warping; elastic distance; waveform alignment; signal warping; non-linear time alignment

**Definition:** Dynamic Time Warping (DTW) is an algorithm that finds the optimal non-linear alignment between two time series by minimising the total warping cost via dynamic programming. Unlike cross-correlation (which assumes a uniform shift), DTW allows a local time axis to be stretched or compressed, making it robust to non-linear deformations caused, for example, by temperature-dependent wave velocity changes in structural health monitoring. The warping path must satisfy monotonicity and boundary constraints; a Sakoe-Chiba band constrains the maximum warping to avoid degenerate paths.

**Key relations:**
- related: [temperature-compensation](temperature-compensation.md)
- related: [cross-correlation](cross-correlation.md)
- related: [structural-health-monitoring](structural-health-monitoring.md)
- related: [time-of-flight](time-of-flight.md)

**Discussed in:**
- [DTW Temperature Compensation](../notes/signal-processing/dtw-temperature-compensation.md) — DTW applied to align ultrasonic guided-wave signals under temperature variation; comparison with uniform stretch and cross-correlation
