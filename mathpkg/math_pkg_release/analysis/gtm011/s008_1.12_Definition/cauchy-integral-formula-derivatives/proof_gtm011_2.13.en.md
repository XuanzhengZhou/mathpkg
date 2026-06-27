---
role: proof
locale: en
of_concept: cauchy-integral-formula-derivatives
source_book: gtm011
source_chapter: "2"
source_section: "2.13"
---

From Theorem 2.8, $f$ has the Taylor expansion $f(z) = \sum_{n=0}^{\infty} a_n (z - a)^n$ with $a_n = f^{(n)}(a)/n!$ for $|z - a| < R$. Comparing with the coefficients obtained in the proof of Theorem 2.8,

$$a_n = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{(w - a)^{n+1}} dw,$$

where $\gamma(t) = a + r e^{it}$, $0 \leq t \leq 2\pi$ for any $r < R$. Therefore,

$$f^{(n)}(a) = \frac{n!}{2\pi i} \int_{\gamma} \frac{f(w)}{(w - a)^{n+1}} dw.$$

Since the integral is independent of $r$ (as can be shown by Cauchy's theorem), the formula holds for any $r$ with $\bar{B}(a; r) \subset G$.
