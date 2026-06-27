---
role: proof
locale: en
of_concept: bernoulli-polynomial-fundamental-identity
source_book: gtm059
source_chapter: "2"
source_section: "1"
---

The Bernoulli polynomials are defined by the generating function

$$
\frac{t e^{tX}}{e^t - 1} = \sum_{k=0}^{\infty} B_k(X) \frac{t^k}{k!}.
$$

From this definition one obtains

$$
\frac{t e^{t(X+1)}}{e^t - 1} - \frac{t e^{tX}}{e^t - 1}
= t e^{tX} \frac{e^t - 1}{e^t - 1} = t e^{tX}.
$$

Expanding both sides as power series in $t$ and comparing coefficients of $t^k/k!$, the left-hand side gives $B_k(X+1) - B_k(X)$, while the right-hand side gives $k X^{k-1}$. Hence

$$
B_k(X+1) - B_k(X) = k X^{k-1},
$$

which is equivalent to the stated identity. The second formula follows by applying the distribution relation repeatedly.
