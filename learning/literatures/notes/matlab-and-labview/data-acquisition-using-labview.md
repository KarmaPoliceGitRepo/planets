# Data Acquisition Using LabVIEW

- **Source:** Behzad Ehsani - Data Acquisition using LabVIEW-Packt (2016).pdf
- **Drive link:** https://drive.google.com/file/d/1fu2Py3gANsxvoc9I_eee1HNJwDJlbCFl/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Behzad Ehsani / 2016 (Packt Publishing)
- **Coverage:** partial (large PDF; extraction covers chapters 1–6 of 11 in detail; chapters 7–11 titles visible from TOC only)

## Overview
A practical, project-oriented introduction to data acquisition (DAQ) using LabVIEW 2013 Professional for Windows. Aimed at engineers, scientists, and experienced students, it guides the reader from LabVIEW installation and basic VI construction through instrument communication buses (serial, GPIB, USB), automated code generation with the DAQ Assistant, manual DAQmx programming, debugging techniques, and real-world event-driven programming patterns. Later chapters (seen only via TOC) address real-time deployment, networked/distributed DAQ, alternative DAQ software, non-NI devices, and Arduino-based microcontroller integration.

## Unique contribution
Unlike purely theoretical treatments, this book uses affordable and widely available hardware (NI USB-6008, Arduino Uno, Tektronix TDS 2022 oscilloscope, Korad KA3005P programmable power supply, Parallax ultrasonic sensor) to demonstrate realistic DAQ workflows end-to-end. It emphasizes the non-trivial aspects of driver installation and hardware recognition (NI MAX), demonstrates SCPI command construction and verification for third-party instruments, and gives explicit cautionary notes about hardware safety when software debugging tools pause or stop a running DAQ loop.

## Key concepts
- LabVIEW G language; graphical programming environment; dataflow execution
- Virtual Instrument (VI); sub-VI; Front Panel; Block Diagram
- While loop; For loop; Case Structure; Shift Register; Event Manager; State Machine
- DAQ Assistant (express VI) vs. manual NI-DAQmx functions
- NI-DAQmx: Create Channel, Timing, Start, Read, Clear task functions
- TDMS file format; logging; data verification
- Serial communication (RS-232, 1-wire, 3-wire); USB; FTDI converters
- GPIB (IEEE 488.1/488.2); GPIB-USB-HS adapter; Passport option (HP Agilent)
- SCPI (Standard Commands for Programmable Instruments) command sets
- VISA (Virtual Instrument Software Architecture); VISA Configure Serial Port; VISA Write/Read
- NI MAX (Measurement & Automation Explorer); device recognition; driver installation
- VI Package Manager (VIPM / VIPM JKI); third-party driver distribution
- Arduino Uno (ATmega328); LINX firmware; LabVIEW Interface for Arduino toolkit
- NI USB-6008 DAQ (8 SE / 4 DIFF analog inputs, 12-bit, 10 kS/s)
- NI myRIO-1900; embedded real-time deployment
- GPIB-ENET / Conet ENET100; distributed/networked DAQ
- Measurement Computing DASYLab; Tera Term terminal emulator
- Debugging: broken wire / broken arrow; highlight execution; breakpoints; probes; custom probes
- Error cluster (Status, Code, Source); error wire for enforcing execution order
- Waveform Graph; Gauge; indicator/control creation from wire
- PWM; duty cycle; distance measurement (Parallax ultrasonic sensor)
- Simultaneous multi-channel acquisition (NI DAQ + Arduino Uno)
- Project-based LabVIEW development; standalone executable; LabVIEW Runtime Engine

## Methods / results / takeaways
- **DAQ Assistant shortcut:** Drag the DAQ Assistant express VI to the Block Diagram; it auto-launches a configuration wizard, auto-selects hardware channels visible to NI MAX, and auto-generates the underlying NI-DAQmx code. Good for prototyping but lacks fine-grained control needed for production.
- **Manual NI-DAQmx sequence:** Create Channel → Timing (N Samples / Continuous) → Start → Read (inside while loop) → Clear — mirrors the open/use/close pattern common in file I/O and instrument drivers.
- **USB-6008 triangular wave capture:** Signal generator (FG085) set to 10 kHz, 3 V amplitude; DAQ AI0 in differential mode, ±5 V range, 1000 samples at 1 kS/s. Logged to TDMS file, which opens directly in Excel.
- **Oscilloscope staircase capture:** Tektronix TDS 2022 connected via GPIB-USB-HS; verified with `*IDN?` query returning device ID string before any VI runs. Oscilloscope temporarily locks out front-panel buttons during remote control — important operational constraint.
- **SCPI power supply stepping:** KORAD KA3005P controlled over virtual serial (USB); commands OUT1, VSET1:\<V\>, VSET1? (query), OUT0. Blank array elements appear between valid readings because the for loop runs faster than the power supply stabilizes — fixed by adding a read delay and filtering empty strings via Case Structure.
- **Debugging hierarchy:** (1) Broken arrow — type mismatch or unwired required input, shown immediately; (2) Highlight Execution — slows VI, shows moving data dots on wires with live values; (3) Breakpoints — pauses execution at selected wire; (4) Probes — opens separate window showing concurrent wire values during run. Key safety caveat: stopping LabVIEW does not stop connected hardware; high-voltage/high-current supplies can keep driving loads, and serial ports may remain open requiring hardware reset.
- **Driver hunting is a core skill:** Most real DAQ work begins with finding, installing, and verifying the correct NI or third-party LabVIEW driver. FTDI USB-serial adapters (Windows/Mac/Linux/Android) and VI Package Manager are the two primary mechanisms for extending hardware support.
- **Production patterns:** Use State Machine or Event Manager architecture; move hardcoded values to input files; initialize and cleanly shut down all ports in separate states; handle initialization errors before entering the main acquisition loop.
- **Bus speed reference:** USB 1.1 = 1.5 MB/s; USB 2 = 60 MB/s; USB 3.0 = 625 MB/s; Thunderbolt 3 = 40 GB/s. GPIB transfer rate is significantly higher than RS-232 serial.
