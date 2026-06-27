---
role: proof
locale: en
of_concept: homogeneous-polynomial-common-zeros
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "2. p-adic equations"
---

*Proof.* The implication (b) $\Rightarrow$ (a) is trivial.

Conversely, if $x = (x_1, \ldots, x_m)$ is a nontrivial common zero of the $f^{(i)}$ in $(\mathbb{Q}_p)^m$, put
$$h = \inf(v_p(x_1), \ldots, v_p(x_m)) \quad \text{and} \quad y = p^{-h}x.$$
It is clear that $y$ is a primitive element of $(\mathbb{Z}_p)^m$ (since at least one component has valuation $0$), and since the $f^{(i)}$ are homogeneous, $y$ is a common zero of the $f^{(i)}$. Hence (a) $\Leftrightarrow$ (b).

The equivalence of (b) and (c) follows from the lemma on projective limits of finite nonempty sets. Consider the sets $D_n$ of common primitive zeros of the $f_k^{(i)}$ (the reductions modulo $p^k$) in $(A_n)^m$ for $k \leq n$. The natural reduction maps give a projective system; condition (c) says each $D_n$ is nonempty, and the lemma implies the projective limit (which is precisely the set of common primitive zeros in $(\mathbb{Z}_p)^m$) is nonempty. $\square$
