---
role: proof
locale: en
of_concept: dimension-bound-by-kernel-intersection
source_book: gtm023
source_chapter: "2"
source_section: "§1. Basic properties, 2.4"
---
Consider the linear mapping $\varphi: E \to \Gamma^r$ defined by
$$\varphi(x) = (f_1(x), f_2(x), \ldots, f_r(x)).$$
Then clearly $\ker \varphi = \bigcap_{i=1}^r \ker f_i = F$.

By the First Isomorphism Theorem, $E/F = E/\ker \varphi \cong \operatorname{Im} \varphi \subset \Gamma^r$. Since $\operatorname{Im} \varphi$ is a subspace of $\Gamma^r$, its dimension is at most $r$. Therefore
$$\dim E/F = \dim \operatorname{Im} \varphi \leq r.$$
