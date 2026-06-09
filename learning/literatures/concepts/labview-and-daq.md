# LabVIEW and Data Acquisition
**Aliases:** LabVIEW; Virtual Instrument; VI; G language; NI-DAQmx; DAQ Assistant; GPIB; VISA; SCPI; NI MAX; PXI; TDMS; TDMS file; reentrant VI; action engine; LabVIEW functional global; state machine; event manager; producer-consumer architecture; highlight execution; breakpoint; error cluster

**Definition:** LabVIEW (Laboratory Virtual Instrument Engineering Workbench) is NI's graphical dataflow programming environment: programs are called Virtual Instruments (VIs); code is the block diagram written in the G language; the front panel provides the UI. NI-DAQmx is the driver library for National Instruments DAQ hardware; the DAQ Assistant auto-generates NI-DAQmx tasks. GPIB (IEEE 488) and VISA (Virtual Instrument Software Architecture) provide instrument control via SCPI command strings. PXI (PCI eXtensions for Instrumentation) is the chassis standard for modular instruments. TDMS is NI's high-speed binary data format. Key LabVIEW design patterns: state machine (explicit state variable and case structure); producer-consumer (two parallel loops with a queue); action engine (uninitialized shift register used as persistent state). Error clusters propagate error status without stopping; highlight execution and breakpoints are debugging tools.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [digital-filters](digital-filters.md)
- related: [sampling-and-aliasing](sampling-and-aliasing.md)

**Discussed in:**
- [LabVIEW Graphical Programming Cookbook](../notes/programming/labview-graphical-programming-cookbook.md) — action engine, state machine, producer-consumer, reentrant VIs; debugging tools
- [LabVIEW DSP and Digital Communications](../notes/matlab-and-labview/labview-dsp-digital-communications.md) — G-language DSP: FFT, FIR/IIR filters, windowing, spectral leakage, sampling, QAM
- [Data Acquisition Using LabVIEW](../notes/matlab-and-labview/data-acquisition-using-labview.md) — NI-DAQmx, DAQ Assistant, Arduino/LINX, GPIB/VISA/SCPI; TDMS logging
- [LabVIEW DSP](../notes/programming/labview-dsp.md) — FFT, FIR/IIR filter VIs; NI-DSP toolkit usage
