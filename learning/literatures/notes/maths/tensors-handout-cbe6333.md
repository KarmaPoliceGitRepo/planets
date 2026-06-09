# Tensor Notation (CBE 6333 Handout 4)

- **Source:** TENSORS_Handout4_6333.pdf
- **Drive link:** https://drive.google.com/file/d/1P9-KCTOlqNmmKPM_g9igRJOApybhfaxV/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** R. Levicky, CBE 6333 course (transport phenomena)
- **Coverage:** full

## Overview
A 6-page handout from a transport phenomena / fluid mechanics course introducing tensor notation for engineers. Develops the summation convention, 2nd rank tensors, transpose, trace, addition/subtraction, direct product, single and double inner products, and provides the stress tensor and velocity gradient tensor as key physical examples.

## Unique contribution
Presents tensor notation from the perspective of it being required for physical laws to be reference-frame independent — a physical motivation rarely made explicit in purely mathematical treatments. The stress tensor example (σ_{ij} = stress in direction j on surface perpendicular to direction i) is immediately operational for continuum mechanics.

## Key concepts
- Summation (Einstein) convention
- 2nd rank tensor components
- Transpose A†_{ij} = A_{ji}
- Trace = A_{ii} (sum of diagonal)
- Direct (outer) product of tensors
- Inner (dot) product of tensors
- Double inner product (A:B = A_{ij} B_{ji})
- Stress tensor σ_{ij}
- Velocity gradient tensor ∇v
- Coordinate transformation of tensor components
- Dyadic notation

## Methods / results / takeaways
- The rank of the result of a direct product = sum of input ranks; inner product reduces rank by 2.
- S = n · σ gives the stress vector on a surface with unit normal n: S_j = n_i σ_{ij}.
- The double inner product A:B is a scalar: A:B = A_{ij} B_{ji}.
- Caution: different indices must be used for tensors in a direct product to avoid unintended contraction.
- The notations (component array, dyadic basis) are equivalent; preference varies by field.
