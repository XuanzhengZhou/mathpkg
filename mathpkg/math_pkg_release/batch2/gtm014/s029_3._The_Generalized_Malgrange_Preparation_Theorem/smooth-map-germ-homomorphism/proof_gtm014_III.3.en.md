---
role: proof
locale: en
of_concept: smooth-map-germ-homomorphism
source_book: gtm014
source_chapter: "III"
source_section: "3. The Generalized Malgrange Preparation Theorem"
---

It is easy to see that $\phi^*$ is well-defined: if $f_1 = f_2$ on a neighborhood of $q$, then $f_1 \circ \phi = f_2 \circ \phi$ on $\phi^{-1}$ of that neighborhood, which is a neighborhood of $p$ by continuity of $\phi$. The map $\phi^*$ is a ring homomorphism because $[(f+g) \circ \phi]_p = [f \circ \phi]_p + [g \circ \phi]_p$ and $[(fg) \circ \phi]_p = [f \circ \phi]_p [g \circ \phi]_p$.

If $\phi$ is a local diffeomorphism near $p$, then $\phi$ has a smooth local inverse $\phi^{-1}$ near $q$, and $(\phi^*)^{-1} = (\phi^{-1})^*$, so $\phi^*$ is an isomorphism.

Conversely, assume $\phi^*$ is an isomorphism. Then $\phi^*$ maps the maximal ideal $\mathcal{M}_q(Y)$ to $\mathcal{M}_p(X)$ (since $\phi^*(f)(p) = f(\phi(p)) = f(q)$), and similarly maps $\mathcal{M}_q^2(Y)$ into $\mathcal{M}_p^2(X)$. Hence $\phi^*$ induces an isomorphism

$$\mathcal{M}_q(Y) / \mathcal{M}_q^2(Y) \xrightarrow{\cong} \mathcal{M}_p(X) / \mathcal{M}_p^2(X).$$

By Lemma 3.3, this gives an isomorphism $T_q^*Y \cong T_p^*X$, so $\dim Y = \dim X = n$.

Choose local coordinates $x_1, \ldots, x_n$ on $X$ based at $p$ corresponding to a chart $\eta$. Since $\phi^*$ is surjective, there exist smooth functions $h_i$ near $q$ such that $[x_i]_p = \phi^*[h_i]_q = [h_i \circ \phi]_p$. Define

$$H: (\operatorname{dom} h_1 \cap \cdots \cap \operatorname{dom} h_n) \to \mathbf{R}^n$$

by $H(y) = (h_1(y), \ldots, h_n(y))$. Then $H \circ \phi$ agrees with the coordinate map $\eta$ near $p$. In particular, the Jacobian of $H \circ \phi$ at $p$ is the identity, so by the chain rule, $(d\phi)_p$ is injective. Since $\dim X = \dim Y$, $(d\phi)_p$ is an isomorphism. By the Inverse Function Theorem, $\phi$ is a local diffeomorphism near $p$.
