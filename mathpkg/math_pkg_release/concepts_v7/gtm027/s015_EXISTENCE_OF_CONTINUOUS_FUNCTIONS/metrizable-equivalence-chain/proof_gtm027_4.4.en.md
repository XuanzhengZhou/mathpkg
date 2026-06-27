---
role: proof
locale: en
of_concept: metrizable-equivalence-chain
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Equivalence Chain for Metrizable Spaces

**Theorem 17 (Equivalence Chain for Metrizable Spaces).** For a topological space $X$, the following are equivalent:

(a) $X$ is regular, $T_1$, and has a countable base.
(b) $X$ is homeomorphic to a subspace of $[0,1]^\omega$.
(c) $X$ is separable and metrizable.

*Proof.* $(a) \Rightarrow (b)$: This is precisely the Urysohn metrization theorem (Theorem 16).

$(b) \Rightarrow (c)$: The cube $[0,1]^\omega$ is metrizable by Theorem 14 and satisfies the second axiom of countability (Problem 3.M). Hence each subspace is metrizable and satisfies the second axiom of countability, and is therefore separable.

$(c) \Rightarrow (a)$: If $X$ is metrizable and separable, then it is surely regular and $T_1$, and by Theorem 11 (separable pseudo-metric spaces are second countable) it satisfies the second axiom of countability.

Thus all three conditions are equivalent.

