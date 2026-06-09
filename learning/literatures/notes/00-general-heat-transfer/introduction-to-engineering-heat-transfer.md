# Introduction to Engineering Heat Transfer

- **Source:** Introduction to engineering heat transfer.pdf
- **Drive link:** https://drive.google.com/file/d/1hWO6V4J2ju0P9RZ5Z7JP8mXWxE88-Gfy/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** MIT / circa 2000s (aerospace engineering course notes, Part 3 of a larger set; references Lienhard and Incropera & DeWitt texts)
- **Coverage:** partial (large file, truncated extraction — body text retrieved covers HT-1 through approximately HT-65+; all major sections appear present)

## Overview
A set of course notes (labelled "Part 3") from an MIT aerospace engineering subject providing a structured introduction to the three heat transfer modes — conduction, convection, and radiation — with emphasis on practical estimation methods for aerospace applications. The notes proceed from first principles through dimensionless analysis to engineering applications such as fins, heat exchangers, transient cooling, and radiation between surfaces.

## Unique contribution
These notes are pedagogically distinctive for their explicit "Muddy Points" (MP) sections scattered throughout each topic, where common student confusions are addressed directly. The aerospace framing (turbine blade cooling, thermocouple errors in hot flows) gives concrete motivations for otherwise abstract derivations. The treatment of the Reynolds analogy as a bridge between momentum and heat transfer is unusually prominent for introductory notes.

## Key concepts
- Three heat transfer modes: conduction, convection, radiation
- Fourier's Law of heat conduction
- Thermal conductivity (k)
- Thermal resistance circuits (series and parallel)
- One-dimensional steady conduction: slabs, cylinders, spheres
- Convective heat transfer coefficient (h)
- Reynolds analogy (linking skin friction to heat transfer)
- Biot number (Bi = hL/k) — ratio of external convection to internal conduction resistance
- Nusselt number (Nu)
- Prandtl number (Pr)
- Reynolds number (Re)
- Stanton number (St)
- Fin analysis (extended surface heat transfer)
- Lumped-capacitance / transient heat transfer
- Heat exchanger effectiveness; NTU method
- Counterflow vs. parallel-flow configurations
- Radiation: blackbody, emittance, absorptance, Kirchhoff's law
- View factors / shape factors
- Stefan-Boltzmann law
- Grey-body radiation; radiation between parallel planes
- Thermocouple temperature measurement error

## Methods / results / takeaways
- **Conduction:** Fourier's Law q = -k(dT/dx); thermal resistance R = L/(kA) for a slab. Composite slabs, cylindrical shells, and spherical shells treated via resistance circuits. Thermal conductivity table provided for common metals (Al ~200 W/m·K) and non-metals.
- **Convection:** heat flux q = h(T_wall - T_fluid). Reynolds analogy: St·Pr^(2/3) = c_f/2, relating heat transfer coefficient to skin friction; valid for Pr near 1 and for both laminar and turbulent boundary layers.
- **Biot number significance:** Bi >> 1 → convection resistance negligible, temperature drop mainly in solid; Bi << 1 → nearly isothermal solid, temperature drop mainly in fluid (lumped-capacitance regime).
- **Dimensionless correlations:** Nu = f(Re, Pr) for forced convection over cylinders and flat plates; Nu = C·Re^m·Pr^(1/3) forms common. Pipe flow: Dittus-Boelter equation referenced.
- **Fins:** energy balance on a differential fin element yields a 2nd-order ODE; solution gives exponentially decaying temperature profile; fin efficiency η = tanh(mL)/(mL) where m = sqrt(hP/kA).
- **Transient cooling:** lumped-capacitance model valid when Bi < 0.1; solution is (T-T∞)/(T_i-T∞) = exp(-t/τ) where τ = ρcV/hA.
- **Heat exchangers:** NTU-effectiveness method; counterflow achieves highest effectiveness for given NTU. Log Mean Temperature Difference (LMTD) also covered.
- **Radiation:** Stefan-Boltzmann: q = εσT^4. Total emittances tabulated for various surfaces. For two parallel grey planes: q/A = σ(T1^4-T2^4)/(1/ε1 + 1/ε2 - 1). View factor algebra and the reciprocity relation covered.
- **Thermocouple errors:** radiation exchange between thermocouple junction and duct walls can cause systematic reading errors; higher flow velocity (higher h) reduces this error via the Reynolds analogy.
