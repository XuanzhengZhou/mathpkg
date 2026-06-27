---
role: proof
locale: en
of_concept: distribution-representation-via-convolution
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Representation of a Distribution Induced by Convolution

**Proposition 7.4.** If $F \in \mathcal{P}'$ and $u, v \in \mathcal{P}$, then

$$F_f(v) = F(\tilde{u} * v),$$

where

$$f = F * u.$$

*Proof.* Let $w = \tilde{u} * v$ and let $w_n$ be the corresponding sequence of Riemann sum approximants defined by (9), with $\tilde{u}$ replacing $u$. Then $w_n \to \tilde{u} * v$ in the sense of $\mathcal{P}$, so by continuity of $F$,

$$F(\tilde{u} * v) = \lim_{n \to \infty} F(w_n).$$

But

$$F(w_n) = (2\pi)^{-2} \sum_{m=1}^{n} n^{-1} v(2\pi m/n) F(T_{2\pi m/n} \tilde{u})$$

$$= \frac{1}{2\pi} \sum_{m=1}^{n} v(2\pi m/n) f(2\pi m/n) \frac{1}{2\pi n}$$

$$\to \frac{1}{2\pi} \int_0^{2\pi} v(x) f(x) \, dx = F_f(v).$$

The convergence of the Riemann sum to the integral uses the fact that $f = F * u$ is smooth (by Proposition 7.1), hence the Riemann sum of the product $v f$ converges to the integral. $\square$

This proposition establishes the duality: the distribution $F_f$ induced by the smooth function $f = F * u$ acts on test functions $v$ in the same way as $F$ acts on $\tilde{u} * v$.
