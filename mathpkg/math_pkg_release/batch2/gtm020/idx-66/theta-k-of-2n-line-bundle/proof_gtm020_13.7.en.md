---
role: proof
locale: en
of_concept: theta-k-of-2n-line-bundle
source_book: gtm020
source_chapter: "13"
source_section: "13.7"
---

By the multiplicative property (13.4), $\theta_k(2n\zeta) = \theta_k(2\zeta)^n$. From (13.6), $\theta_k(2\zeta) = (2r+1) + r(\zeta-1)$. Therefore $\theta_k(2n\zeta) = [(2r+1) + r(\zeta-1)]^n$.

Using the binomial theorem and the relation $(\zeta-1)^2 = -2(\zeta-1)$, all higher powers $(\zeta-1)^m$ for $m \geq 2$ can be reduced. Specifically:
$$
(\zeta-1)^2 = -2(\zeta-1), \quad
(\zeta-1)^3 = 4(\zeta-1), \quad
(\zeta-1)^n = (-2)^{n-1}(\zeta-1)
$$

This implies $[(2r+1) + r(\zeta-1)]^n$ expands to $(2r+1)^n + a(\zeta-1)$ for some coefficient $a$. To determine $a$, substitute $\zeta-1 = -2$ (which corresponds to $\zeta = -1$, the sign representation). Since $\zeta^2 = 1$, this substitution is consistent, yielding $1^n = (2r+1)^n - 2a$. Solving gives $2a = (2r+1)^n - 1 = k^n - 1$, hence the stated formula.
