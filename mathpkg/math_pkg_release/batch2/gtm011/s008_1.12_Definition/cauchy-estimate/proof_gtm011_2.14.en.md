---
role: proof
locale: en
of_concept: cauchy-estimate
source_book: gtm011
source_chapter: "2"
source_section: "2.14"
---

For any $r < R$, Corollary 2.13 applies with $\gamma(t) = a + r e^{it}$, $0 \leq t \leq 2\pi$:

$$|f^{(n)}(a)| = \left| \frac{n!}{2\pi i} \int_{\gamma} \frac{f(w)}{(w - a)^{n+1}} dw \right|.$$

By Proposition 1.17(b),

$$|f^{(n)}(a)| \leq \frac{n!}{2\pi} \int_{\gamma} \frac{|f(w)|}{|w - a|^{n+1}} |dw| \leq \frac{n!}{2\pi} \cdot \frac{M}{r^{n+1}} \cdot 2\pi r = \frac{n! M}{r^n}.$$

Since this inequality holds for every $r < R$, letting $r \to R^{-}$ yields

$$|f^{(n)}(a)| \leq \frac{n! M}{R^n}.$$
