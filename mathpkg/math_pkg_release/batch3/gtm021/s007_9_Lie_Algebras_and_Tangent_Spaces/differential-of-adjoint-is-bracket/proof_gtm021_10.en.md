---
role: proof
locale: en
of_concept: differential-of-adjoint-is-bracket
source_book: gtm021
source_chapter: "10"
source_section: "Differentials of Morphisms"
---
We first treat the special case $G = \mathrm{GL}(n, K)$, $\mathfrak{g} = \mathfrak{gl}(n, K)$.

If $x \in G$, $\operatorname{Ad} x$ factors as $\operatorname{Ad} x = \sigma(x) \circ \tau(x^{-1})$, where $\sigma(x)(Y) = xY$ (left multiplication) and $\tau(x^{-1})(Y) = Y x^{-1}$ (right multiplication by $x^{-1}$).

Thus $\operatorname{Ad} x = \sigma(x) \circ \tau(\iota(x))$. Differentiating at $e$ using Proposition 10.1:
$$d(\operatorname{Ad})_e(X) = d\sigma_I(d(1)_e(X)) \circ \tau(e) + \sigma(e) \circ d\tau_I(d\iota_e(X)) = d\sigma_I(X) \circ \operatorname{id} + \operatorname{id} \circ d\tau_I(-X).$$

Now $d\sigma_I(X)(Y) = XY$ (left multiplication by $X$) and $d\tau_I(-X)(Y) = Y(-X) = -YX$ (right multiplication by $-X$). Therefore:
$$d(\operatorname{Ad})_e(X)(Y) = XY + (-YX) = XY - YX = [X, Y].$$

For a general algebraic group $G$, embed $G$ as a closed subgroup of some $\operatorname{GL}(n,K)$ (Theorem 8.6). The adjoint representation of $G$ is the restriction of that of $\operatorname{GL}(n,K)$, so the result follows from the special case by restriction to $\mathfrak{g} \subset \mathfrak{gl}(n,K)$.
