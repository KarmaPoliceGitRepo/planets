# One-Dimensional Pressure Transfer Models for Acoustic–Electric Transmission Channels

- **Source:** 2015 02 - One-dimensional pressure transfer models for acoustic–electric transmission channels - KR Wilt.pdf
- **Drive link:** https://drive.google.com/file/d/1s8yjHy7lguTDPuihbhoH8wpXqzCnLLpt/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Wilt, Lawry, Scarton, Saulnier / 2015
- **Coverage:** full

## Overview
A Journal of Sound and Vibration paper presenting a 2×2 traveling-pressure-wave transfer matrix framework for modeling multilayer piezoelectric-based acoustic–electric transmission channels — systems that convey electrical power or data through a solid barrier (e.g., a pressure vessel wall) using ultrasonic waves. Each mechanical layer (solid, fluid, or transducer) is represented by a 2×2 matrix relating forward and reverse pressure waves at its two faces. These matrices are cascaded to obtain a complete channel model. Piezoelectric transducer behavior is incorporated as a two-port (one electrical + one mechanical) element, and the electrical interface is made compatible with standard ABCD (transmission-line) parameters.

## Unique contribution
Unlike prior force-velocity analog (ABCD) acoustic transfer matrix models, this formulation works entirely with traveling pressure waves, giving cleaner physical interpretation of forward/reverse wave components and simplifying the incorporation of ultrasonic beam spreading (diffraction loss) as a layer-specific correction. Backing impedance of a transducer is handled via a reflection-coefficient boundary condition, collapsing the second mechanical port cleanly.

## Key concepts
- Acoustic transfer matrix / transfer matrix method
- Traveling pressure wave decomposition (forward/reverse)
- Acoustic impedance mismatch / reflection coefficient at interface
- Piezoelectric transducer modeling (pressure-wave domain)
- ABCD / transmission-line parameters
- Ultrasonic beam spreading / diffraction loss
- Acoustic–electric power/data transmission channels
- Backing reflection coefficient
- Multilayer acoustic system
- Piezoelectric coupling constant h₃₃, compliance c^D₃₃

## Methods / results / takeaways
- Each homogeneous elastic or fluid layer is represented by a 2×2 matrix; matrices multiply sequentially across the stack. Interfaces between domains with differing reference impedances are handled by impedance-matched transformation matrices.
- Beam spreading (near-field to far-field diffraction) is modeled as an amplitude loss factor applied within applicable fluid domains using piston-source theory.
- The piezoelectric model yields a 2×2 EPM matrix relating [V, I] to [p⁺_eff, p⁻_eff]; inverting and reordering provides the receiving transducer model (M̃PE).
- Electrical output is compatible with microwave-style ABCD parameters, enabling direct connection to electronic networks.
- The model reproduces measured frequency-domain transfer characteristics of a realistic steel-barrier channel (with transmitting and receiving PZT disks on each side) without the heavy computational cost of FEM.
- Practical note: at least 140 W at ~67 % efficiency has been demonstrated with such channels; the model guides design without full FEM.
