---
role: proof
locale: en
of_concept: abelian-valued-group-topology
source_book: gtm015
source_chapter: "8"
source_section: "Valued topological groups"
---

# Proof of Left and right value topologies coincide for abelian groups

Let $(G, |\cdot|)$ be a valued abelian group. The left-invariant metric is $d(x, y) = |x^{-1}y|$ and the right-invariant metric is $D(x, y) = |xy^{-1}|$. Since $G$ is abelian,

$$D(x, y) = |xy^{-1}| = |(xy^{-1})^{-1}| = |yx^{-1}| = |x^{-1}y| = d(x, y).$$

Thus the two value topologies (derived from $d$ and $D$) coincide.

To show compatibility with the group structure, we verify continuity of inversion and multiplication.

**Inversion:** $d(x^{-1}, y^{-1}) = |(x^{-1})^{-1}y^{-1}| = |xy^{-1}|$. Since $G$ is abelian, $|xy^{-1}| = |y^{-1}x| = |x^{-1}y| = d(x, y)$, so $x \mapsto x^{-1}$ is an isometry (hence continuous).

**Multiplication:** If $d(x_n, x) \to 0$ and $d(y_n, y) \to 0$, then

$$d(x_n y_n, xy) = |(x_n y_n)^{-1}(xy)| = |y_n^{-1}x_n^{-1}xy| = |(x_n^{-1}x)(y_n^{-1}y)|$$
$$\leq |x_n^{-1}x| + |y_n^{-1}y| = d(x_n, x) + d(y_n, y) \to 0.$$

Thus $(x, y) \mapsto xy$ is continuous. Therefore a valued abelian group, equipped with the value topology, is a metrizable topological group.
