# Operational Amplifier

**Aliases:** op-amp; operational amplifier; Op-amp; ideal op-amp; voltage feedback amplifier; OA

**Definition:** An operational amplifier (op-amp) is a high-gain differential voltage amplifier with very high input impedance and very low output impedance, used with external feedback to implement precise, well-defined signal-processing functions. The ideal op-amp has infinite open-loop gain A, infinite differential input impedance, zero output impedance, and infinite bandwidth. Real op-amps deviate from the ideal through finite gain-bandwidth product (GBW), input offset voltage, bias currents, and limited slew rate. In closed-loop inverting or non-inverting configurations, gain is set by external resistors. Op-amps are the fundamental building block of active filters, integrators, differentiators, summing amplifiers, and instrumentation amplifiers.

**Key relations:**
- [sallen-key-topology](sallen-key-topology.md) — op-amp is the active element
- [general-impedance-converter](general-impedance-converter.md) — two op-amps form a GIC
- [analogue-filter-basics](analogue-filter-basics.md) — op-amp is the heart of active filters
- [noise-figure](noise-figure.md) — op-amp input noise limits system noise performance

**Discussed in:**
- [Op-amp (Collin, Signals & Systems)](../notes/00-general-electronics/signals-systems-for-bioengineers.md) — ideal model, virtual short, gain derivations
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — op-amp as the active element in all filter topologies
