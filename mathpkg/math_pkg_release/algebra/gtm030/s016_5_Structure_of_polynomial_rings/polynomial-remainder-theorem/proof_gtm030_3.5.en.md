---
role: proof
locale: en
of_concept: polynomial-remainder-theorem
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

For each $k = 0, 1, 2, \ldots$, the following identity holds:
$$x^k - c^k = (x^{k-1} + cx^{k-2} + c^2x^{k-3} + \cdots + c^{k-1})(x - c)$$
$$= (x - c)(x^{k-1} + cx^{k-2} + \cdots + c^{k-1}),$$
where it is understood that for $k = 0$, the sum $\sum c^i x^{k-i-1} = 0$. Multiply the identity on the left by $a_k$ and sum over $k$ to obtain
$$f(x) - f_R(c) = q_1(x)(x - c)$$
where $f_R(c) = \sum a_k c^k$ and $q_1(x) = \sum a_k (x^{k-1} + cx^{k-2} + \cdots + c^{k-1})$.
