---
role: proof
locale: en
of_concept: product-identity-characters-mod-m
source_book: gtm007
source_chapter: "VI"
source_section: "3"
---

Let $W$ be the set of $f(p)$-th roots of unity. The identity $\prod_{w \in W} (1 - wT) = 1 - T^{f(p)}$ is well known.

For each $w \in W$, there are exactly $g(p)$ characters $\chi$ of $G(m)$ such that $\chi(\bar{p}) = w$ (this follows from Proposition 1: the character of the cyclic subgroup $\langle \bar{p} \rangle$ sending $\bar{p}$ to $w$ extends to $G(m)$ in exactly $g(p) = |G(m)|/f(p)$ ways). Hence
$$\prod_{\chi} (1 - \chi(p)T) = \prod_{w \in W} (1 - wT)^{g(p)} = (1 - T^{f(p)})^{g(p)}.$$

