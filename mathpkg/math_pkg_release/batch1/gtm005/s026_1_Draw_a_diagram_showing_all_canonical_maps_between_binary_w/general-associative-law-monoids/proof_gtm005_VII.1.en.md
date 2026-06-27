---
role: proof
locale: en
of_concept: general-associative-law-monoids
source_book: gtm005
source_chapter: "VII"
source_section: "1"
---

In a monoidal category $M$, for a monoid $(M, \mu, \eta)$, there is a unique map $\mu^{(n)}: M^{\otimes n} \to M$ for each $n \geq 2$ representing "$n$-fold multiplication", independent of bracketing.

Proof by induction using coherence: Define $\mu^{(2)} = \mu$. For $n > 2$, any bracketing can be reduced using $\alpha$ to a standardized form. The Coherence Theorem ensures all transformations between different bracketings commute, so the result of iterated $\mu$ is well-defined.

Formally: $\mu^{(n)}$ satisfies $\mu^{(m+n)} = \mu \circ (\mu^{(m)} \otimes \mu^{(n)})$ up to the associativity isomorphism. For strict monoidal categories this is an exact equality; in the general case, the coherence isomorphisms mediate the equality.
