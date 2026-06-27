---
role: proof
locale: en
of_concept: birkhoff-theorem-on-periodic-solutions
source_book: gtm060
source_chapter: "Appendix 9"
source_section: "E"
---

The proof proceeds by considering the Poincaré return map (or stroboscopic map) near the periodic solution. After reduction to a fixed point of a symplectic mapping, one applies the Birkhoff normal form theory: near a linearly stable fixed point, the symplectic mapping can be approximated to arbitrarily high order by an integrable normal form that is a rotation on invariant tori.

For each rational frequency vector in the normal form approximation, the corresponding invariant torus is foliated by periodic orbits. Applying the theorem on periodic points near invariant tori (from the generating function method), each such rational torus in the approximation gives rise to at least $2^n$ periodic points for the actual mapping, provided the normal form is close enough and the nondegeneracy condition holds.

Since there are infinitely many distinct rational frequency vectors accumulating near the frequency of the linearization, and each yields periodic points of different periods, we obtain infinitely many distinct periodic solutions accumulating near the original periodic orbit.

The key technical step is showing that the generating function $F(y) = S(X(f(y), y), y)$ is sufficiently nondegenerate for the iterated mapping $A^N$ for $N$ corresponding to each rational frequency. The nondegeneracy of the normal form and the linear stability guarantee that the Morse inequalities apply, yielding the claimed lower bound on critical points.
