---
role: proof
locale: en
of_concept: multivariate-symmetric-laurent-polynomial
source_book: gtm020
source_chapter: "14"
source_section: "5"
---

The proof proceeds by induction on the number of variables $n$, applying Proposition 5.2 successively. For $n = 1$, this is exactly Proposition 5.2. Assume the result holds for $n - 1$ variables. View $f \in R[\alpha_1, \alpha_1^{-1}, \ldots, \alpha_n, \alpha_n^{-1}]$ as an element of $S[\alpha_n, \alpha_n^{-1}]$ where $S = R[\alpha_1, \alpha_1^{-1}, \ldots, \alpha_{n-1}, \alpha_{n-1}^{-1}]$. The invariance condition $f(\ldots, \alpha_n) = f(\ldots, \alpha_n^{-1})$ means, by Proposition 5.2 applied over the ring $S$, that $f \in S[\alpha_n + \alpha_n^{-1}]$. The coefficients of $f$ as a polynomial in $\alpha_n + \alpha_n^{-1}$ lie in $S$ and inherit the invariance property for each of the remaining variables $\alpha_1, \ldots, \alpha_{n-1}$. By the induction hypothesis, these coefficients belong to $R[\alpha_1 + \alpha_1^{-1}, \ldots, \alpha_{n-1} + \alpha_{n-1}^{-1}]$. Hence $f$ belongs to $R[\alpha_1 + \alpha_1^{-1}, \ldots, \alpha_n + \alpha_n^{-1}]$.
