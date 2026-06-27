---
role: proof
locale: en
of_concept: compactness-of-uniform-neighborhood
source_book: gtm027
source_chapter: "6"
source_section: "T"
---

# Proof: Compactness of Uniform Neighborhoods of Compact Sets

Let $U$ be a closed neighborhood of the diagonal in $X \times X$, let $A$ be a compact subset of $X$, and assume $\overline{U \circ U[x]}$ is compact for each $x \in A$.

First, $U[A]$ is closed: By 6.A, if $U$ is a closed entourage, then $U[A]$ is closed (the cross-section of a closed set is closed when $A$ is compact, or more generally when the projection is closed).

To show $U[A]$ is compact, we use the assumption on $U \circ U[x]$. For each $x \in A$, the set $\overline{U \circ U[x]}$ is compact. Since $A$ is compact, it can be covered by finitely many sets $U[x_1], \ldots, U[x_n]$. Then

$$U[A] \subset \bigcup_{i=1}^n U[U[x_i]] = \bigcup_{i=1}^n (U \circ U)[x_i].$$

Each $\overline{(U \circ U)[x_i]}$ is compact, and their finite union is compact. Since $U[A]$ is a closed subset of this compact union, $U[A]$ is compact.
