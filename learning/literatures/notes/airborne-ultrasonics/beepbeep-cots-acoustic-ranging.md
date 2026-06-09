# BeepBeep: A High Accuracy Acoustic Ranging System Using COTS Mobile Devices

- **Source:** BeepBeep paper (Chunyi Peng et al. 2007)
- **Drive link:** https://drive.google.com/file/d/1WZ8cI6kxlrHOMUsQ079-gBOrr1CFqYWO/view
- **Type:** paper
- **Author/Year:** Chunyi Peng et al., 2007 (ACM SenSys 2007)
- **Coverage:** partial (large file, key sections extracted)

## Overview
Presents BeepBeep, a two-way acoustic ranging system using only speaker and microphone of COTS mobile devices (cell phones, PDAs). Uses an echo-based two-way protocol to cancel clock skew and software delays. Achieves centimetre-level accuracy in user-space software without real-time OS.

## Unique contribution
Solves the fundamental problem of clock skew and irregular software delays in COTS devices (which can sum to several milliseconds ≡ several feet of ranging error) by using a symmetric two-way exchange: each device emits and records the other's signal, then exchanges TOA information. The processing is pure user-space software, requiring no OS modification, custom hardware, or GPS-like infrastructure.

## Key concepts
- COTS acoustic ranging
- Two-way ranging protocol
- Clock skew cancellation
- Software-only user-space implementation
- TOA measurement
- Speaker/microphone as transducers
- Mobile device localisation
- SenSys 2007

## Methods / results / takeaways
- Protocol: Device A emits "beep"; Device B records arrival time, then emits "beep"; Device A records arrival. Each device locally timestamps both events. Distance = (sum of TOFs)/2, cancelling asymmetric delays.
- Key innovation: symmetric exchange eliminates need for hardware clock synchronisation.
- Implementation entirely in user-space; tested on commodity mobile platforms.
- Accuracy: centimetre-level (cm range) demonstrated at short-to-medium distances.
- Limitation: audible frequency signal — band-limited by commodity speaker/mic response; not ultrasonic.
- Applicable to any two devices with speaker + mic + data link (Bluetooth, WiFi, cellular).
- Contrasts with GPS/Wi-Fi localisation: no infrastructure needed, purely device-to-device.
