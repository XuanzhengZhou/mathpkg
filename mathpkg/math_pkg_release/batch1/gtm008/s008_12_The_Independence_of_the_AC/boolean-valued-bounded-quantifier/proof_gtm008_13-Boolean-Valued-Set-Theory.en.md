---
role: proof
locale: en
of_concept: boolean-valued-bounded-quantifier
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

1. By definition, $(\exists x \in u)\varphi(x)$ is equivalent to $\exists x (x \in u \land \varphi(x))$. In the Boolean-valued semantics,
$$[\![(\exists x \in u) \varphi(x)]\!] = \sum_{x \in V^{(B)}} [\![x \in u]\!] \cdot [\![\varphi(x)]\!].$$
Since $[\![x \in u]\!] = 0$ for $x \notin \mathcal{D}(u)$ (up to equality), the sum reduces to $\sum_{x \in \mathcal{D}(u)} u(x) \cdot [\![\varphi(x)]\!]$.

2. Similarly, $(\forall x \in u)\varphi(x)$ is $\forall x (x \in u \rightarrow \varphi(x))$, and
$$[\![(\forall x \in u) \varphi(x)]\!] = \prod_{x \in V^{(B)}} ([\![x \in u]\!] \Rightarrow [\![\varphi(x)]\!]) = \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow [\![\varphi(x)]\!]).$$
