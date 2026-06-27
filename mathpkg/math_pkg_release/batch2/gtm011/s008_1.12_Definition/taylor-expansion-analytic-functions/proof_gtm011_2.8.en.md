---
role: proof
locale: en
of_concept: taylor-expansion-analytic-functions
source_book: gtm011
source_chapter: "2"
source_section: "2.8"
---

Let $0 < r < R$ so that $\bar{B}(a; r) \subset B(a; R)$. Let $\gamma(t) = a + r e^{it}$, $0 \leq t \leq 2\pi$. By Proposition 2.6 (Cauchy Integral Formula),

$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w - z} dw \quad \text{for} \quad |z - a| < r.$$

For $|z - a| < r$ and $w$ on the circle $|w - a| = r$, we have $|z - a|/|w - a| < 1$. Hence the geometric series expansion holds:

$$\frac{1}{w - z} = \frac{1}{w - a} \cdot \frac{1}{1 - \frac{z - a}{w - a}} = \sum_{n=0}^{\infty} \frac{(z - a)^n}{(w - a)^{n+1}}.$$

Substituting this into the Cauchy integral gives

$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \sum_{n=0}^{\infty} \frac{f(w) (z - a)^n}{(w - a)^{n+1}} dw.$$

For $w$ on $\{\gamma\}$, let $M = \max \{|f(w)| : |w - a| = r\}$. Then

$$\frac{|f(w)| |z - a|^n}{|w - a|^{n+1}} \leq \frac{M}{r} \left( \frac{|z - a|}{r} \right)^n.$$

Since $|z - a|/r < 1$, the Weierstrass $M$-test implies the series converges uniformly for $w$ on $\{\gamma\}$. By the lemma on uniform convergence and line integrals, we may interchange summation and integration:

$$f(z) = \sum_{n=0}^{\infty} \left( \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{(w - a)^{n+1}} dw \right) (z - a)^n.$$

By Corollary 2.13 (which follows from the theorem itself), the coefficient equals $f^{(n)}(a)/n!$, giving the Taylor expansion. Since $r < R$ was arbitrary, the expansion holds for all $|z - a| < R$, and the radius of convergence is at least $R$.
