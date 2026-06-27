---
role: proof
locale: en
of_concept: uniqueness-of-laplace-transform-distributions
source_book: gtm012
source_chapter: "6"
source_section: "§6. Laplace transforms of distributions"
---

# Proof of Uniqueness of the Laplace Transform for Distributions

**Corollary.** Suppose $F \in \mathcal{L}'$ and suppose $F$ satisfies a bound of the form

$$|F(u)| \leq K |u|_{k,a,M}, \quad u \in \mathcal{L}.$$

If $LF(z) = 0$ for all $z$ with $\operatorname{Re} z > a$, then $F = 0$.

*Proof.* If $LF \equiv 0$, then by the representation formula of Theorem 6.2,

$$F = D^{k+2} F_f,$$

where

$$f(t) = \frac{1}{2\pi i} \int_C e^{zt} z^{-k-2} LF(z) \, dz = \frac{1}{2\pi i} \int_C e^{zt} z^{-k-2} \cdot 0 \, dz = 0.$$

Thus $f \equiv 0$, which implies $F_f = 0$, and consequently $F = D^{k+2} 0 = 0$. $\square$
