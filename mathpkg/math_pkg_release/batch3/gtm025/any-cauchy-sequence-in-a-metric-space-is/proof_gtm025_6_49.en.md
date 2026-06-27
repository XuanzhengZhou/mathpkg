---
role: proof
locale: en
of_concept: "any-cauchy-sequence-in-a-metric-space-is"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.49"
---

Let $(x_n)$ be a Cauchy sequence in a metric space $X$. Choose $n_0 \in N$ such that $n \geq n_0$

Conversely, suppose that $X$ has the decreasing closed sets property. Let $(x_n)$ be a Cauchy sequence in $X$. For each $n \in N$, let $A_n = \{x_m : m \geq n\}^-$. Then $(A_n)$ is a decreasing sequence of closed sets and, since $(x_n)$ is a Cauchy sequence, $\text{diam}(A_n) \to 0$. Let $\bigcap_{n=1}^{\infty} A_n = \{x\}$. If $\varepsilon > 0$, then there is an $n_0 \in N$ such that $\text{diam}(A_{n_0}) < \varepsilon$. But $x \in A_{n_0}$, so $n \geq n_0$ implies that $\varrho(x_n, x) < \varepsilon$.
