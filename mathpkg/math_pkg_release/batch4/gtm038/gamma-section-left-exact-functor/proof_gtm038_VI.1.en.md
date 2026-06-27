---
role: proof
locale: en
of_concept: gamma-section-left-exact-functor
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---

Since $\hat{\Gamma}$ is exact (see Theorem 1.1), it is clear that $\varphi_*$ is injective and $\psi_* \circ \varphi_* = 0$.

Now let $s \in \Gamma(X, \mathcal{S})$ with $\mathbf{O} = \psi_*(s) = \psi \circ s$. We must show that there exists $s' \in \Gamma(X, \mathcal{S}')$ with $\varphi_*(s') = s$.

Since $\hat{\Gamma}$ is exact, there exists a generalized section $s' \in \hat{\Gamma}(X, \mathcal{S}')$ with $\varphi_*(s') = s$. It remains to show that $s'$ is continuous (hence a true global section).

For every point $x \in X$, by exactness of the original sequence of sheaves, there exists a neighborhood $U(x)$ and an element $s^* \in \Gamma(U, \mathcal{S}')$ with $(\varphi \circ s^*)(x) = s(x)$. Therefore there is a neighborhood $V(x) \subset U$ with $\varphi \circ s^*|_V = s|_V$.

Since $\varphi$ is injective (as a sheaf morphism), it follows from
$$\varphi \circ s^*|_V = \varphi \circ s'|_V$$
that $s^*|_V = s'|_V$. Thus $s'$ agrees with the continuous section $s^*$ on the neighborhood $V(x)$, so $s'$ is continuous at $x$. Since $x$ was arbitrary, $s'$ is continuous on $X$, hence $s' \in \Gamma(X, \mathcal{S}')$.

This proves $\operatorname{Ker} \psi_* = \operatorname{Im} \varphi_*$, establishing left-exactness of $\Gamma$.
