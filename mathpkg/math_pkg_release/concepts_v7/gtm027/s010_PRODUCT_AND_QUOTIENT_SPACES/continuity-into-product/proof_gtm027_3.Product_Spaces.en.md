---
role: proof
locale: en
of_concept: continuity-into-product
source_book: gtm027
source_chapter: "3"
source_section: "Product Spaces"
---

# Proof of Continuity into a Product Space

**Theorem.** A function $f$ on a topological space to a product $\bigwedge\{X_a : a \in A\}$ is continuous if and only if the composition $P_a \circ f$ is continuous for each projection $P_a$.

*Proof.* If $f$ is continuous, then $P_a \circ f$ is always continuous because $P_a$ is continuous (as shown by $P_a^{-1}[U] = \{x : x_a \in U\}$ being a subbase element, hence open).

Conversely, if $P_a \circ f$ is continuous for each $a$, then for each open subset $U$ of $X_a$ the set

$$
(P_a \circ f)^{-1}[U] = f^{-1}[P_a^{-1}[U]]
$$

is open. It follows that the inverse under $f$ of each member of the defining subbase for the product topology is open, and hence $f$ is continuous (by condition (c) of Theorem 1). $\square$
