---
role: proof
locale: en
of_concept: additive-functor-preserves-direct-sum
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

The proof is joint with Proposition 16.2. Since $M$ is a direct sum with the given injections and projections, we have $\pi_j \iota_i = \delta_{ij} 1_{M_i}$ and $\sum \iota_i \pi_i = 1_M$. Applying the additive functor $F$ (which preserves addition and composition) gives $F(\pi_j)F(\iota_i) = \delta_{ij} 1_{F(M_i)}$ and $\sum F(\iota_i)F(\pi_i) = 1_{F(M)}$, which characterizes $F(M)$ as the direct sum of the $F(M_i)$ with the stated injections and projections. For the contravariant $G$, the composition reversal swaps injections and projections.
