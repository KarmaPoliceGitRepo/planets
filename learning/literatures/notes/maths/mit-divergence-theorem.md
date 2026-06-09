# MIT 18.02SC: V10.2 The Divergence Theorem

- **Source:** MIT18_V10.2 The Divergance Theorem.pdf
- **Drive link:** https://drive.google.com/file/d/1yVZPEP64kYcXcm5PF6UFtIY-oX9MyDkS/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** MIT OpenCourseWare, 18.02SC Multivariable Calculus, Fall 2010
- **Coverage:** full

## Overview
MIT course note from 18.02SC providing a formal proof of the Divergence Theorem for a vector field F over a closed surface S bounding a region D. The proof is component-by-component: first shows the theorem for F = P(x,y,z)k, then assembles the general result. Relies on the vertically-simple surface decomposition.

## Unique contribution
Complements the Lady proof (same theorem) with a cleaner notation from the MIT 18.02 course, emphasising the iteration technique for the triple integral. Together the two proofs offer two slightly different pedagogical angles on the same result.

## Key concepts
- Divergence theorem
- Vertically simple region
- Flux integral
- Surface area element dS
- Component-wise proof strategy

## Methods / results / takeaways
- For F = Pk: triple integral ∂P/∂z dV equals surface flux via the relation P(x,y,h) - P(x,y,g) after iteration.
- The surface area element for z = h(x,y) gives P k · dS = P(x,y,h) dx dy on the upper surface.
- General case: add the three component results (4), (4'), (4'') for M i, N j, P k.
- Domains not bounded by a simple surface can be cut into simpler pieces; inner faces cancel.
