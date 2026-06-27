---
role: proof
locale: en
of_concept: weierstrass-division-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "§1. The Weierstrass Preparation Theorem"
---

Uniqueness: Suppose $G = qF + r = q_1 F + r_1$. Then $(q-q_1)F = r_1 - r$. For fixed $z$, $r_1 - r$ is a polynomial of degree $\leq k-1$ in $w$ with at most $k-1$ roots. One shows that near $0$, $(q-q_1)F$ has at least $k$ zeroes as a function of $w$, forcing $r_1 = r$ and $q = q_1$.

Existence uses polynomial division via the Cauchy Integral Formula. Writing $P_k(w, \lambda) = w^k + \sum \lambda_i w^i$, one uses the identity:
$$\frac{1}{\eta - w} = \frac{P_k(\eta, \lambda)}{P_k(\eta, \lambda)(\eta - w)} = \frac{P_k(w, \lambda)}{P_k(\eta, \lambda)(\eta - w)} + \frac{\sum s_i(\eta, \lambda)w^i}{P_k(\eta, \lambda)}.$$
Then $q(w,z) = \frac{1}{2\pi i} \int_\gamma \frac{G(\eta,z)}{P_k(\eta,\lambda)(\eta - w)} d\eta$ and $r_i(z) = \frac{1}{2\pi i} \int_\gamma \frac{G(\eta,z)}{P_k(\eta,\lambda)} s_i(\eta,\lambda) d\eta$ via the Cauchy Integral Formula.
