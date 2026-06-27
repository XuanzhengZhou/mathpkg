---
role: proof
locale: en
of_concept: transient-hitting-time-ratio-limit
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

Observe that $P_z[T > n] = P_z[n < T \leq \infty]$. Therefore
$$\lim_{n \to \infty} \frac{P_z[T > n]}{P_0[T > n]} = \frac{P_z[T = \infty]}{P_0[T = \infty]} = \frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)}, \quad x \neq 0.$$

From the renewal equation P1.2,
$$\sum_{n=1}^{\infty} t^n F_n(x,0) = \frac{\sum_{n=0}^{\infty} t^n P_n(x,0)}{\sum_{n=0}^{\infty} t^n P_n(0,0)}, \quad x \neq 0, \quad 0 \leq t < 1.$$

Letting $t \to 1$ and using P1.5,
$$F(x,0) = \sum_{n=1}^{\infty} F_n(x,0) = \frac{G(x,0)}{G(0,0)}, \quad x \neq 0.$$

Hence
$$\frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)} = G(0,0) - G(x,0) = a(x), \quad x \neq 0.$$
