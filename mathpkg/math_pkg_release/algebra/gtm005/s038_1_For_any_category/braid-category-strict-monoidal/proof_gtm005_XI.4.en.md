---
role: proof
locale: en
of_concept: braid-category-strict-monoidal
source_book: gtm005
source_chapter: "XI"
source_section: "4"
---

The operation of laying braids side by side is clearly associative, as placing braid $\alpha$ beside braid $\beta$ beside braid $\gamma$ yields the same result regardless of grouping. Formally, for any braids $\alpha \in \mathcal{B}(m, m')$, $\beta \in \mathcal{B}(n, n')$, $\gamma \in \mathcal{B}(p, p')$, we have
$$
(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)
$$
as braids on $(m+n)+p = m+(n+p)$ strings, since both sides represent the same spatial configuration of the three braids placed side by side.

The empty braid on $0 = \varnothing$ serves as the unit: for any braid $\alpha \in \mathcal{B}(m, n)$, laying the empty braid beside $\alpha$ on either side simply returns $\alpha$ itself. That is, $\alpha + \mathrm{id}_0 = \alpha = \mathrm{id}_0 + \alpha$.

Since both associativity and the unit laws hold strictly (as equalities, not merely up to isomorphism), the braid category $\mathcal{B}$ equipped with the tensor product $+$ is a strict monoidal category.
