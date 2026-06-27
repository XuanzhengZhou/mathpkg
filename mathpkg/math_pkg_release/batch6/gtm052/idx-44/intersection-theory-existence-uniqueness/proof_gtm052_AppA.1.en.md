---
role: proof
locale: en
of_concept: intersection-theory-existence-uniqueness
source_book: gtm052
source_chapter: "Appendix A"
source_section: "1. Intersection Theory"
---

There are two main ingredients in the proof of this theorem. One is the correct definition of the local intersection multiplicities; the other is Chow's moving lemma.

There are several ways of defining intersection multiplicity. We mention Serre's definition, which is historically most recent, but has the advantage of being compact. If $Y$ and $Z$ intersect properly, and if $W$ is an irreducible component of $Y \cap Z$, let $A$ be the local ring of the generic point of $W$ on $X$, and let $\mathfrak{a}, \mathfrak{b}$ be the ideals of $Y$ and $Z$. Then one defines

$$i(Y,Z; W) = \sum_{i \geq 0} (-1)^i \operatorname{length}_A \operatorname{Tor}_i^A(A/\mathfrak{a}, A/\mathfrak{b}).$$

Then using the reduction to the diagonal (A5) we reduce to the case of computing $\Delta \cdot (Y \times Z)$ on $X \times X$. This has the advantage that $\Delta$ is a local complete intersection. Since the intersection multiplicity is local (A6) we reduce to the case where one of the cycles is a complete intersection of Cartier divisors, and then repeated application of the normalization (A7) gives the uniqueness.

Some general references for intersection theory are Weil [1], Chevalley [2], Samuel [1], and Serre [11]. For discussion of some other equivalence relations on cycles, and attempts to calculate the groups $A^i(X)$, see Hartshorne [6].
