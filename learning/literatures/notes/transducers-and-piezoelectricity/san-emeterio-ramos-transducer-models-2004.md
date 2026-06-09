# Models for Piezoelectric Transducers Used in Broadband Ultrasonic Applications

- **Source:** 2004 - Models for Piezoelectric Transducers Used in Broadband Ultrasonic Applications - José Luis San EmeterioAntonio Ramos.pdf
- **Drive link:** https://drive.google.com/file/d/1NWBPl6gDk8lnBtvLnmhHCydsbB2wzgHh/view
- **Type:** paper (book chapter)
- **Author/Year:** José Luis San Emeterio, Antonio Ramos / 2004 (published 2008 in Springer book)
- **Coverage:** full

## Overview
Comprehensive chapter on one-dimensional electromechanical models for broadband piezoelectric transducers, covering the Mason, Redwood, and KLM equivalent circuits. Derives the ABCD transfer matrix formalism for cascaded networks (piezo element + matching layers + electrical matching) and provides computed emission, reception, and pulse-echo responses for a representative PZT transducer.

## Unique contribution
Provides a unified treatment of all three major equivalent circuits (Mason, Redwood, KLM) from the same 3×3 electromechanical matrix, demonstrating complete equivalence. Shows how KLM transfers naturally into cascade ABCD matrices for system-level broadband design. Derives and tabulates Desilets impedance formulae for one- and two-layer matching alongside Collins formulae.

## Key concepts
- Mason equivalent circuit (1948)
- Redwood equivalent circuit
- KLM equivalent circuit (Krimholtz, Leedom, Matthaei 1970)
- ABCD transfer matrix formalism
- Thickness extensional mode piezoelectric plate
- Acoustic matching layer design (Collins vs Desilets criteria)
- Emission and reception transfer functions
- Electrical tuning with shunt inductance
- Clamped capacitance C0

## Methods / results / takeaways
- 3×3 electromechanical matrix derived from piezoelectric constitutive equations + plane wave propagation
- All three circuits derive from the same matrix: Mason uses T-network + ideal transformer + negative capacitor; KLM places transformer at midpoint of transmission line + reactance X
- Collins single-layer formula: Zc = (Z0·ZL)^(1/2); Desilets formula: Zc = Z0^(2/3)·ZL^(1/3) — KLM-based, gives better impulse compactness
- Two-layer Desilets: ZC1 = Z0^(4/7)·ZL^(3/7); ZC2 = Z0^(1/7)·ZL^(6/7)
- Computed example: PZT at 1.093 MHz, ZB = 30 MRayl backing, ZL = 1.5 MRayl water — emission and pulse-echo transfer functions shown with and without matching layers and shunt inductance
- Parallel tuning inductance Lp cancels clamped capacitance, shifts and sharpens reception peak; distorted response at emission but global response acceptable
- Two-way (pulse-echo) response = product of emission × reception transfer functions when same transducer used for both
