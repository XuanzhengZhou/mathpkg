---
role: proof
locale: en
of_concept: ratio-limit-for-transient-random-walk
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

Since $P_z[T > n] = P_z[n < T \leq \infty]$,
$$\lim_{n \to \infty} \frac{P_z[T > n]}{P_0[T > n]} = \frac{P_z[T = \infty]}{P_0[T = \infty]} = \frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)}, \quad x \neq 0.$$
From P1.2, $\sum_{n=1}^{\infty} t^n F_n(x,0) = \frac{\sum_{n=0}^{\infty} t^n P_n(x,0)}{\sum_{n=0}^{\infty} t^n P_n(0,0)}$ for $0 \leq t < 1$. Letting $t \to 1$ and using P1.5, $F(x,0) = G(x,0)/G(0,0)$. Hence $\frac{1 - \sum F_n(x,0)}{1 - F(0,0)} = G(0,0) - G(x,0) = a(x)$.
