---
role: proof
locale: en
of_concept: causal-relation-via-delta
source_book: gtm048
source_chapter: "6"
source_section: "6.0.12"
---

Define the function $u = 3(u^4)^{1/3}$ on $M$. Then
$$
du = (u^4)^{-2/3} \, du^4,
$$
so the Einstein-de Sitter metric can be rewritten as
$$
g = (u^4)^{4/3} \left\{ -du \otimes du + \sum_{\mu=1}^{3} du^\mu \otimes du^\mu \right\}.
$$
In view of the conformal invariance of the causality relation (cf. Section 5.0.1) and the behavior of the causality relation for Minkowski space (cf. Exercise 5.0.7), this yields
$$
x \leq z \iff 0 \leq \delta(x, z) \leq u z - u x.
$$
Thus
$$
x \leq z \iff 3\big\{ (u^4 z)^{1/3} - (u^4 x)^{1/3} \big\} \geq \delta(x, z).
$$
