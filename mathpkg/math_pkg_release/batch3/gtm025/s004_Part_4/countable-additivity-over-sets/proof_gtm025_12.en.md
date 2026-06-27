---
role: proof
locale: en
of_concept: countable-additivity-over-sets
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

Define $g_n = f \xi_{A_1} + \cdots + f \xi_{A_n}$. Then $|g_n| \leq |f| \in \mathfrak{L}_1$ and $g_n \to f \xi_A$ pointwise. By Lebesgue's dominated convergence theorem (12.30), $\int_A f d\mu = \lim_{n \to \infty} \int_X g_n d\mu = \lim_{n \to \infty} \sum_{k=1}^n \int_{A_k} f d\mu = \sum_{n=1}^{\infty} \int_{A_n} f d\mu$.
