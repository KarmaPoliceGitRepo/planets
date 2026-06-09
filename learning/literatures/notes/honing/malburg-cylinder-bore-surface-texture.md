# Cylinder Bore Surface Texture Analysis

- **Source:** CylinderBoreNoBkgd.pdf
- **Drive link:** https://drive.google.com/file/d/16PJPbO1UlhfEunBiH54E2uDY9OXlww5Z/view?usp=drivesdk
- **Type:** slides
- **Author/Year:** Mark C. Malburg, Ph.D., Digital Metrology Solutions, Inc.; 2002
- **Coverage:** full

## Overview
A 33-slide presentation on the measurement and parameterization of plateau-honed cylinder bore surfaces. It explains why plateau honing is used, the trade-offs between smooth plateaus and deep valleys, instrumentation choices (skidless vs. skidded profilometers), filtering methods (traditional vs. robust), and three parameterization schemes: traditional (Ra, Rz, tp/Rmr), Rk-family (ISO 13565-2), and probability-based (ISO 13565-3). The deck is aimed at metrologists and process engineers who need to specify or measure honed bore surfaces.

## Unique contribution
The most focused metrological reference in the folder. It provides a side-by-side comparison of all three parameter families and explains precisely why the Rk method fails to model plateau honing well (especially in the valley region), making the probability model (Rpq, Rvq, Rmq) the recommended approach per ISO 13565-3. It also illustrates trailing-skid measurement artefacts with clear diagrams, a pitfall often overlooked in shop-floor settings.

## Key concepts
- Plateau honing (dual-texture surface: smooth plateaus + deep valleys)
- Surface functionality: friction/clearance (smooth plateau), wear/sealing (contact area), lubrication/debris retention (valley volume)
- Skidless profilometry vs. skidded (shop-floor) profilometry
- Trailing-skid artefacts (false depressions when skid rides over a peak)
- Traditional filtering vs. robust filtering
- Ra (average roughness — sensitive to plateaus)
- Rz (sensitive to valleys and pull-outs)
- tp / Rmr (material ratio / bearing ratio)
- Rk parameters (ISO 13565-2): Rk (core roughness), Rpk (reduced peak height), Rvk (reduced valley depth), Mr1, Mr2
- Bearing ratio curve (Abbott-Firestone curve) and the 40% window method for determining kernel
- Probability parameters (ISO 13565-3): Rpq (plateau RMS roughness), Rvq (valley RMS roughness), Rmq (plateau-valley transition bearing ratio)
- Normal probability paper analysis (bimodal decomposition of plateau + valley process)

## Methods / results / takeaways
- Plateau honing generates a surface that combines benefits of both a smooth surface (plateaus for low friction/contact) and a rough surface (valleys for oil retention).
- "Let the engine do it" (run-in) vs. engineered plateau honing — the latter is preferred for consistency and reduced break-in wear.
- Skidded instruments follow surface waviness and suppress it from the measurement; they also introduce spurious depressions when the skid rides over high peaks. Laboratory-grade skidless instruments are recommended for plateau hone specification.
- Ra is biased toward plateau levels (more data points there); Rz is biased toward valleys; tp is sensitive to valley width and number. The three parameters are highly interdependent — specifying one without the others leaves the surface under-constrained.
- Rk method: uses a 40% window on the bearing ratio curve to find the most horizontal (core) segment; derives Rpk and Rvk from the triangles above/below. Works well for the core but is acknowledged as a poor model for the valley region of plateau honing.
- Probability model: decomposes the surface as a superposition of two random textures (plateau-making process + valley-making process); fits two lines on normal probability paper to derive Rpq, Rvq, Rmq. This is the recommended characterization method (ISO 13565-3) for plateau-honed surfaces.
- A complete bore analysis ideally combines both 2D profile measurements and 3D area measurements.
