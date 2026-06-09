# New Equivalent Circuits for Elementary Piezoelectric Transducers

- **Source:** Krimholtz 1970 - KLM equivalent circuits.pdf
- **Drive link:** https://drive.google.com/file/d/1_klm_file_id/view
- **Type:** paper
- **Author/Year:** R. Krimholtz, D.A. Leedom, G.L. Matthaei / 1970
- **Coverage:** full

## Overview
Introduces the KLM equivalent circuit model for piezoelectric transducers operating in thickness mode. The model represents the transducer as two acoustic transmission line sections joined at a central electrical port, providing an intuitive and computationally tractable framework for transducer design.

## Unique contribution
The KLM model became the standard design tool for thickness-mode transducers, superseding the Mason model in many design contexts due to its cleaner separation of electrical and acoustic ports. Enables direct calculation of matching layer effects and frequency response analytically.

## Key concepts
- KLM equivalent circuit
- Thickness-mode piezoelectric transducer
- Acoustic transmission line model
- Electrical port
- Acoustic ports (front and back)
- Electromechanical coupling (kt)
- Matching layer design
- Transducer bandwidth prediction
- Mason model comparison

## Methods / results / takeaways
- KLM model: transducer represented as a lossless transmission line of length equal to transducer thickness, with a central shunt electrical port
- Two acoustic ports emerge at the front and back faces, enabling modeling of matching layers and backing as additional transmission line sections
- Coupling parameter kt enters through a transformer in the electrical port
- Model valid for plane-wave, thickness-mode operation; assumes no lateral effects
- Analytically predicts resonance frequencies, bandwidth, and input impedance for arbitrary loading
- Widely used in CAD tools for transducer design (e.g., PiezoCAD, Field II preprocessing)
- Compared to Mason model: KLM avoids negative capacitance elements, making it more numerically stable
- Basis for multi-layer matching layer design by treating each layer as a transmission line section
