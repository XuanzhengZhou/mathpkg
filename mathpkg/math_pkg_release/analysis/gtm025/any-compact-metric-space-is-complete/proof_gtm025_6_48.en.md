---
role: proof
locale: en
of_concept: "any-compact-metric-space-is-complete"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.48"
---

Let $X$ be a compact metric space and let $(x_n)$ be a Cauchy sequence in $X$. Then $(x_n)$ has a subsequence $(x_{n_k})$ converging to some $x \in X$. Let $\varepsilon > 0$ be given. Choose $n_0, k_0 \in N$ such that $m, n \geq n_0$ implies $\varrho(x_m, x_n) < \varepsilon/2$ and $k \geq k_0$ implies $\varrho(x_{n_k}, x) < \varepsilon/2$. Choose $k_1 \geq k_0$ such that $n_{k_1} \geq n_0$. Then $n \geq n_{k_1}$ implies $\varrho(x_n, x) \leq \varrho(x_n, x_{n_{k_1}}) + \varrho(x_{n_{k_1}}, x) < \varepsilon/2 + \varepsilon/2 = \varepsilon$. Thus $\lim_{n \to \infty} x_n = x$, and so $X$ is complete.
