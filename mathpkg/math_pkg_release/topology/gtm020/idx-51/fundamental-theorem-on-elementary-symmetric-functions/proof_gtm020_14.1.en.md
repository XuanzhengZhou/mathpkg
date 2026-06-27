---
role: proof
locale: en
of_concept: fundamental-theorem-on-elementary-symmetric-functions
source_book: gtm020
source_chapter: "14"
source_section: "1"
---

The proof proceeds by induction on the number of variables $n$ and on the degree. For a symmetric polynomial $P(x_1, \ldots, x_n)$, consider the polynomial $P(x_1, \ldots, x_{n-1}, 0)$, which is symmetric in $n-1$ variables. By induction, it can be expressed as a polynomial in $\sigma_1^{n-1}, \ldots, \sigma_{n-1}^{n-1}$. Then the difference $P - Q(\sigma_1^n, \ldots, \sigma_{n-1}^n)$ vanishes when $x_n = 0$, hence is divisible by $x_n$. By symmetry, it is divisible by each $x_i$, hence by $\sigma_n^n = x_1 \cdots x_n$. Factoring out $\sigma_n^n$ reduces the degree, and the induction on degree completes the proof. Uniqueness follows from the algebraic independence of the elementary symmetric functions.
