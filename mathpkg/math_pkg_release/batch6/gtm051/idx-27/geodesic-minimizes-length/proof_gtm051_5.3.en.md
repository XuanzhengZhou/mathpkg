---
role: proof
locale: en
of_concept: geodesic-minimizes-length
source_book: gtm051
source_chapter: "5"
source_section: "5.3"
---

1. Without loss of generality $q \neq p$ and $L(c) = r_0 > 0$.

2. We may further assume that given any comparison curve $b(s)$, $s_0 \leq s \leq s_1$, then $b(s) \neq p$ for $s > s_0$. Introduce geodesic polar coordinates (5.3.1 (ii)) on $B_\rho(p) - \{p\}$. Here $(r, \theta) \in ]0, \rho[ \times \mathbb{R}$, and we may arrange it so that $\theta(c(t)) = 0$.

3. Suppose $b(s) \in B_\rho(p)$ for all $s \in [s_0, s_1]$. One proves the existence of differentiable functions $\theta: [s_0, s_1] \to \mathbb{R}$ and $r: [s_0, s_1] \to ]0, \rho[$ such that

$$b(s) = \exp_p(r(s) \cos \theta(s)e_1 + r(s) \sin \theta(s)e_2).$$

It follows that for $\epsilon > 0$ sufficiently small,

$$L(b \mid [s_0 + \epsilon, s_1]) = \int_{s_0 + \epsilon}^{s_1} \sqrt{r'(s)^2 + g_{22}\theta'(s)^2}\,ds \geq r(s_1) - r(s_0 + \epsilon) = L(c) - r(s_0 + \epsilon).$$

Since $r(s_0 + \epsilon) \to 0$ as $\epsilon \to 0$, we obtain $L(b) \geq L(c)$. Equality holds precisely when $\theta'(s) \equiv 0$ and $r'(s) \geq 0$ almost everywhere, which means $b(s)$ is a monotone reparametrization of the radial geodesic $c$.
