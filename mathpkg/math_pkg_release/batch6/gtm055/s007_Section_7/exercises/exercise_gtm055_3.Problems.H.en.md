---
role: exercise
locale: en
chapter: "3"
section: "Problems"
exercise_number: H
---
Thus far we have employed the notion of the sum of a sequence of arcs $\{\alpha_1, \ldots, \alpha_n\}$ only when these arcs are chained. It turns out that a more general concept is also useful. If $\alpha_1, \ldots, \alpha_n$ are arbitrary arcs in $\mathbb{C}$ we introduce the formal sum $\alpha = \alpha_1 + \cdots + \alpha_n$ with the understanding that two formal sums $\alpha = \alpha_1 + \cdots + \alpha_n$ and $\beta = \beta_1 + \cdots + \beta_m$ are equal if (and only if) each $\alpha_i$ and $\beta_i$ can be partitioned into a chained sum $\alpha_i = \sum_{j=1}^{n_i} \alpha_{ij}$, $\beta_i = \sum_{j=1}^{m_i} \beta_{ij}$, in such a way that the two systems of arcs $\{\alpha_{ij}\}$ and $\{\beta_{ij}\}$ are pairwise equivalent except for order.

Show that if $\alpha = \alpha_1 + \cdots + \alpha_n$ is such a formal sum of rectifiable arcs, and if for each continuous function $f$ on $W$, where $W$ denotes the union of the ranges of the arcs $\alpha_i$, we define
$$\int_\alpha f(\zeta) \, d\zeta = \sum_{i=1}^{n} \int_{\alpha_i} f(\zeta) \, d\zeta,$$
then the mapping $f \mapsto \int_\alpha f(\zeta) \, d\zeta$ is a bounded linear functional on the Banach space $C(W)$.
