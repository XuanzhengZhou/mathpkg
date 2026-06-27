---
role: proof
locale: en
of_concept: product-identity-characters-mod-m
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Let $W$ be the set of all $f(p)$-th roots of unity. The factorization
$$
\prod_{w \in W} (1 - wT) = 1 - T^{f(p)}
$$
is standard. For each $w \in W$, there are exactly $g(p)$ characters $\chi$ of $G(m)$ such that $\chi(\bar{p}) = w$ (since the map $\chi \mapsto \chi(\bar{p})$ from $\hat{G}(m)$ to $\mu_{f(p)}$ is surjective with kernel of size $\phi(m)/f(p) = g(p)$). Therefore
$$
\prod_\chi (1 - \chi(p)T) = \prod_{w \in W} (1 - wT)^{g(p)} = (1 - T^{f(p)})^{g(p)}.
$$
