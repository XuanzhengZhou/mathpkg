---
role: proof
locale: en
of_concept: holomorphic-continuous
source_book: gtm038
source_chapter: "I"
source_section: "1. Power Series"
---
**Proof.** Let $f$ be a holomorphic function on a region $B$, $\mathfrak{z}_0$ a point in $B$. Let the power series $\sum_{v=0}^{\infty} a_v(\mathfrak{z} - \mathfrak{z}_0)^v$ converge to $f(\mathfrak{z})$ in a neighborhood $U$ of $\mathfrak{z}_0$. Then there is a $\mathfrak{z}_1 \in U$ with $z_v^{(1)} \neq z_v^{(0)}$ for $1 \leq v \leq n$ and $P_{\tau(\mathfrak{z}_1 - \mathfrak{z}_0)}(\mathfrak{z}_0) \subset U$. Now let $0 < \varepsilon < \min_{v=1, \dots, n} (|z_v^{(1)} - z_v^{(0)}|)$. From Theorem 1.1 the series converges uniformly on $U'_{\varepsilon}(\mathfrak{z}_0)$. For each $v \in \mathfrak{J}$ one can regard $a_v(\mathfrak{z} - \mathfrak{z}_0)^v$ as a complex-valued function on $\mathbb{R}^{2n}$. This function is clearly continuous at $\mathfrak{z}_0$ and consequently the limit function is continuous at $\mathfrak{z}_0$. $\square$
