---
role: proof
locale: en
of_concept: degree-sum-and-character-sum-relations
source_book: gtm042
source_chapter: "2"
source_section: "2.4"
---

By Corollary 1 (multiplicity in the regular representation), the regular character $r_G$ decomposes as
$$r_G(s) = \sum_{i=1}^{h} n_i \chi_i(s)$$
for all $s \in G$, where $n_i = \chi_i(1)$ is the multiplicity of $W_i$ in the regular representation.

Taking $s = 1$, we have $r_G(1) = g$ and $\chi_i(1) = n_i$, so
$$g = \sum_{i=1}^{h} n_i \cdot n_i = \sum_{i=1}^{h} n_i^2,$$
which proves (a).

Taking $s \neq 1$, Proposition 5 gives $r_G(s) = 0$, so
$$0 = \sum_{i=1}^{h} n_i \chi_i(s),$$
which proves (b). $\square$
