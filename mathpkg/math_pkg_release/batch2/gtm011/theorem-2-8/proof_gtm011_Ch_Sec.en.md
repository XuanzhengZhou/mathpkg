---
role: proof
locale: en
of_concept: theorem-2-8
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $0 < r < R$ so that $\bar{B}(a; r) \subset B(a; R)$. If $\gamma(t) = a + re^{it}, 0 \leq t \leq 2\pi$, then by Proposition 2.6,

$$f(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(w)}{w-z} dw \quad \text{for} \quad |z-a| < r.$$

But, since $|z-a| < r$ and $w$ is on the circle $\{\gamma\}$,

$$\frac{|f(w)| |z-a|^n}{|w-a|^{n+1}} \leq \frac{M}{r} \left( \frac{|z-a|}{r} \right)^n$$

where $M = \max \{|f(w)|; |w-a| = r\}$. Since $\frac{|z-a|}{r} < 1$, the Weierstrass $M$-test gives that $\sum f(w) (z-a)^n / (w-a)^{n+1}$ converges uniformly for $w$ on $\{\gamma\}$. By Lem

holds for $|z-a| < R$; giving that the radius of convergence of (2.10) must be at least $R$.
