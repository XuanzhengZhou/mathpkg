---
role: proof
locale: en
of_concept: riesz-fischer-theorem
source_book: gtm025
source_chapter: "4"
source_section: "13"
---

Let $(f_n)$ be a Cauchy sequence in $\mathfrak{L}_p$. Extract a subsequence $(f_{n_k})$ such that $\|f_{n_{k+1}} - f_{n_k}\|_p < 2^{-k}$ and $\sum \|f_{n_{k+1}} - f_{n_k}\|_p = \alpha < \infty$. Define $g_k = |f_{n_1}| + \sum_{j=1}^k |f_{n_{j+1}} - f_{n_j}|$. Then $\|g_k^p\|_1 = \|g_k\|_p^p \leq (\|f_{n_1}\|_p + \alpha)^p < \infty$. By B. Levi's theorem, $g = \lim g_k$ satisfies $\int g^p d\mu < \infty$, so $g \in \mathfrak{L}_p$. Thus $\sum |f_{n_{j+1}} - f_{n_j}|$ converges a.e., and $f = f_{n_1} + \sum (f_{n_{j+1}} - f_{n_j})$ converges a.e. to a function in $\mathfrak{L}_p$ with $\|f - f_n\|_p \to 0$.
