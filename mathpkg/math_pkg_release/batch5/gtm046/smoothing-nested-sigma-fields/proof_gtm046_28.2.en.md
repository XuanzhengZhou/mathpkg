---
role: proof
locale: en
of_concept: smoothing-nested-sigma-fields
source_book: gtm046
source_chapter: "VIII"
source_section: "28.2"
---

**Proof.** Let $\mathfrak{B} \subset \mathfrak{B}'$ be nested sub-$\sigma$-fields. For any $B \in \mathfrak{B}$,

$$\int_B E^\mathfrak{B}(E^{\mathfrak{B}'}X) \, dP = \int_B E^{\mathfrak{B}'}X \, dP = \int_B X \, dP = \int_B E^\mathfrak{B}X \, dP,$$

since $B \in \mathfrak{B} \subset \mathfrak{B}'$ and both $E^\mathfrak{B}$ and $E^{\mathfrak{B}'}$ are characterized by their indefinite integrals on their respective $\sigma$-fields. Because the indefinite integrals of the $\mathfrak{B}$-measurable functions $E^\mathfrak{B}(E^{\mathfrak{B}'}X)$ and $E^\mathfrak{B}X$ coincide on all $B \in \mathfrak{B}$, they are $P_\mathfrak{B}$-equivalent:

$$E^\mathfrak{B}(E^{\mathfrak{B}'}X) = E^\mathfrak{B}X \quad \text{a.s.}$$

This is the iterated conditional expectation property, also known as the tower property or the smoothing property for nested $\sigma$-fields.
