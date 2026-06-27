---
role: proof
locale: en
of_concept: lemma-product-map-continuity
source_book: gtm027
source_chapter: "5"
source_section: "Compactification"
---

# Proof of Continuity of the Induced Product Map

**Lemma 23.** If $f$ is a function on a set $A$ to a set $B$ and $f^*$ is the map of $Q^B$ into $Q^A$ defined by $f^*(y) = y \circ f$ for all $y$ in $Q^B$, then $f^*$ is continuous. (Here $Q = [0,1]$ is the closed unit interval, and $Q^A$, $Q^B$ carry the product topology.)

*Proof.* A map into a product space is continuous iff the map followed by each projection is continuous (Theorem 3.3). For each $a \in A$, let $P_a: Q^A \to Q$ be the projection onto the $a$-th coordinate. We compute:

$$P_a \circ f^*(y) = P_a(y \circ f) = (y \circ f)(a) = y(f(a)) = P_{f(a)}(y),$$

where $P_{f(a)}: Q^B \to Q$ is the projection onto the $f(a)$-th coordinate. Thus $P_a \circ f^* = P_{f(a)}$, which is a projection and therefore continuous (projections are continuous in the product topology). Since this holds for every $a \in A$, the map $f^*$ is continuous. $\square$
