---
role: proof
locale: en
of_concept: zeta-gamma-integral-representation
source_book: gtm011
source_chapter: "8"
source_section: "8.5"
---

According to Corollary 8.4, the integral $\int_0^\infty (e^t-1)^{-1} t^{z-1} dt$ is an analytic function in the region $\{z : \operatorname{Re} z > 1\}$. Thus, it suffices to show that $\zeta(z)\Gamma(z)$ equals this integral for $z = x > 1$.

From Lemma 8.3 there are numbers $\alpha$ and $\beta$, $0 < \alpha < \beta < \infty$, such that:

$$\int_0^\alpha (e^t - 1)^{-1} t^{x-1} dt < \frac{\varepsilon}{4},$$
$$\int_\beta^\infty (e^t - 1)^{-1} t^{x-1} dt < \frac{\varepsilon}{4}.$$

Since
$$\sum_{k=1}^n e^{-kt} \leq \sum_{k=1}^{\infty} e^{-kt} = (e^t - 1)^{-1}$$
for all $n \geq 1$, we have
$$\sum_{n=1}^{\infty} \int_0^\alpha e^{-nt} t^{x-1} dt < \frac{\varepsilon}{4},$$
$$\sum_{n=1}^{\infty} \int_\beta^\infty e^{-nt} t^{x-1} dt < \frac{\varepsilon}{4}.$$

But $\sum e^{-nt}$ converges to $(e^t-1)^{-1}$ uniformly on $[\alpha, \beta]$, so the right hand side of the difference between the integral and the series representation is exactly $\varepsilon$. Thus for $x > 1$,

$$\zeta(x)\Gamma(x) = \sum_{n=1}^{\infty} \int_0^\infty e^{-nt} t^{x-1} dt = \int_0^\infty (e^t-1)^{-1} t^{x-1} dt.$$

Since both sides are analytic on $\{z : \operatorname{Re} z > 1\}$ and agree on the positive real axis, they are equal on the whole half-plane by the identity theorem.
