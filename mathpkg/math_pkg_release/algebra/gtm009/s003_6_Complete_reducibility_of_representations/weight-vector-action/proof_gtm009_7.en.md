---
role: proof
locale: en
of_concept: weight-vector-action
source_book: gtm009
source_chapter: "II"
source_section: "7"
---

For $v \in V_\lambda$, compute:
$$h.(x.v) = [h, x].v + x.h.v = 2x.v + \lambda x.v = (\lambda+2)x.v,$$
so $x.v \in V_{\lambda+2}$. Similarly,
$$h.(y.v) = [h, y].v + y.h.v = -2y.v + \lambda y.v = (\lambda-2)y.v,$$
so $y.v \in V_{\lambda-2}$.

This uses the commutation relations $[h, x] = 2x$, $[h, y] = -2y$ of $\mathfrak{sl}(2, \mathbb{F})$.
