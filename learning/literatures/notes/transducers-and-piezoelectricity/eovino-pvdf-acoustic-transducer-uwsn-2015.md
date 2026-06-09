# Design and Analysis of a PVDF Acoustic Transducer Towards an Imager for Mobile Underwater Sensor Networks

- **Source:** Eovino PVDF acoustic transducer UWSN 2015
- **Drive link:** https://drive.google.com/file/d/1OK_ztTdsZ30FQL5xe1fHjvQejFf08R5-/view
- **Type:** thesis (UCB/EECS-2015-154, MS thesis, UC Berkeley, May 2015)
- **Author/Year:** Benjamin T. Eovino / 2015
- **Coverage:** full

## Overview
MS thesis proposing and evaluating a thickness-mode PVDF acoustic transducer for underwater wireless sensor networks (UWSNs). Compares direct (Mason circuit) analysis against COMSOL Multiphysics FEM for both hydrophone (1D) and projector (2D axisymmetric) configurations. Key device: 100 μm PVDF film with patterned electrodes on insulating substrate; operates at quarter-wave resonance ~5 MHz. Shows that PVDF achieves comparable hydrophone sensitivity to commercial Tonpilz PZT transducers (predicted −202 dB re 1V/μPa), and characterises when 1D approximation breaks down vs full FEM.

## Unique contribution
Establishes a clear rule of thumb: 1D lumped-parameter analysis is valid for projectors only when r/L > 15–17 (active radius to thickness ratio), beyond which agreement with FEM is within 5% on electrical admittance. Shows that for r = 100 μm (r/L = 1), errors in beam pattern at 1–3 MHz are severe. Provides COMSOL model parameters for PVDF (Y = 3 GPa, ν = 0.4, ρ = 1780 kg/m³, εr = 10, d31 = 23 pC/N, d33 = −33 pC/N). Demonstrates that insulating substrate (rather than silicon) eliminates POSFET need and reduces parasitic capacitance at small scales.

## Key concepts
- Thickness-mode PVDF transducer: resonance at f₀ = c/(4L); c = √(Y/ρ · (1−ν)/((1+ν)(1−2ν))) = 1980 m/s (plane-strain); f₀ = 4.95 MHz for L = 100 μm
- PVDF properties: Y = 3 GPa, ν = 0.4, ρ = 1780 kg/m³, εr = 10; d31 = 23 pC/N, d33 = −33 pC/N; Z ≈ 2.64 MRayl
- Mason circuit: 1D lumped model; predicts OCVS = −202 dB re 1V/μPa (on par with Tonpilz PZT Teledyne Reson TC3027)
- KLM vs Mason: both equivalent; Mason used here for simplicity
- Parasitic capacitance problem: small PVDF → low C₀ → output voltage divided by cable + amplifier input capacitance
- POSFET solution (Swartz & Plummer 1979): on-chip FET gate modulated directly; but complex to fabricate
- Proposed solution: insulating substrate + patterned electrodes; eliminates substrate shunt capacitance without FET fabrication
- 1D validity: projector beam pattern agrees with FEM when r/L > 15; for r/L < ~5 (MEMS-scale), use FEM
- Electrical admittance: within 5% of 1D model for r/L > 17; parasitic resonance at 5.5 MHz present even for large r

## Methods / results / takeaways
- COMSOL physics: acoustic-piezoelectric interaction (pressure acoustics + solid mechanics + electrostatics)
- Hydrophone model: 1D geometry; periodic continuity BCs on sides; plane wave source (1 μPa)
- Projector model: 2D axisymmetric; perfectly matched layer (PML) at boundary; radius r swept parametrically
- PVDF sound speed in plane-strain: cPVDF = 1980 m/s → f₀ = 4.95 MHz for 100 μm
- OCVS: Mason predicts 7.6×10⁻² mV/Pa = −202 dB re 1V/μPa; COMSOL agrees to < 0.1%
- Projector beam pattern: r = 2.5 mm at 1 and 3 MHz — excellent 1D vs FEM agreement; r = 100 μm — large error at 1 and 3 MHz
- Inactive PVDF ring: reduces off-axis radiation (cross-talk suppression) without degrading on-axis TVR
- Admittance: parasitic lateral resonance at 5.5 MHz for all r; treated as artifact of finite geometry
- Application: mobile UWSN arrays for ocean monitoring; passive (hydrophone, low power) + active (projector, high resolution) dual-mode operation; depth-robust (no cavity, no blowout risk)
