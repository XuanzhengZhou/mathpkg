---
role: proof
locale: en
of_concept: behavior-of-fp-under-s
source_book: gtm041
source_chapter: "4"
source_section: "4.6"
---
The proof of Theorem 4.6 relies on Lemma 2 and the definition of the Hecke operator $f_p$.
From the definition
$$f_p(\tau) = \frac{1}{p}\sum_{\lambda=0}^{p-1} f\left(\frac{\tau + \lambda}{p}\right),$$
one applies $S\tau = -1/\tau$ and separates the term with $\lambda = 0$ from $\lambda = 1,\ldots,p-1$.
The term $\lambda = 0$ gives $\frac{1}{p}f(-1/p\tau) = \frac{1}{p}f(p\tau)$ (using automorphy of $f$ under $S$).
For $\lambda = 1,\ldots,p-1$, Lemma 2 provides a factorization $T_\lambda S = V T_\mu$ with $V \in \Gamma_0(p)$,
which allows the remaining sum to be re-indexed and expressed in terms of $f_p(\tau)$ and $f(\tau/p)$.
