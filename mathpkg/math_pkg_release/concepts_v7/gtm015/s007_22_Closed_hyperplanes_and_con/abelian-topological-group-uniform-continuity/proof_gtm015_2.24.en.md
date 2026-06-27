---
role: proof
locale: en
of_concept: abelian-topological-group-uniform-continuity
source_book: gtm015
source_chapter: "2"
source_section: "24"
---

# Proof of Uniform continuity of inversion and multiplication in abelian topological groups

It is understood that $G$ is equipped with the uniformity $U = U_s(G) = U_r(G)$, and $G \times G$ with the product uniformity.

The uniform continuity of $x \mapsto x^{-1}$ is immediate from either (5.19) or (5.12). Thus $x \mapsto x^{-1}$ is a unimorphism of $(G, U)$.

Write $f(x, x') = xx'$. Let $V \in U$ be a symmetric entourage. For any $(x, x'), (y, y') \in G \times G$, one has

$$(xx')^{-1}(yy') = (x')^{-1}x^{-1}yy' = (x')^{-1}(x^{-1}y)y'.$$

Since $G$ is abelian, the left and right uniformities coincide, and the multiplication is uniformly continuous on each factor. More precisely, given $V$, choose a symmetric entourage $W$ such that $W \circ W \circ W \subset V$. Then if $(x, y) \in W$ and $(x', y') \in W$, we have $(xx', yy') \in V$. This shows $f$ is uniformly continuous.
