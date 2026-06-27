---
role: proof
locale: en
of_concept: symmetric-laurent-polynomial-representation
source_book: gtm020
source_chapter: "14"
source_section: "5"
---

Write $f(x) = \sum_m a_m x^m$. The condition $f(x) = f(1/x)$ implies $\sum_m a_m x^m = \sum_m a_m x^{-m} = \sum_m a_{-m} x^m$, so $a_m = a_{-m}$ for all $m$. Therefore, $f$ can be grouped as

$$f(x) = a_0 + \sum_{m \geq 1} a_m(x^m + x^{-m}).$$

By Proposition 5.1, for each $m \geq 1$ there exists a polynomial $f_m \in \mathbb{Z}[y] \subset R[y]$ such that $x^m + x^{-m} = f_m(x + x^{-1})$. Substituting:

$$f(x) = a_0 + \sum_{m \geq 1} a_m f_m(x + x^{-1}) \in R[x + x^{-1}].$$

This proves the proposition.
