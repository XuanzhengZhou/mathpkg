---
role: proof
locale: en
of_concept: quasi-regular-units-isomorphism
source_book: gtm030
source_chapter: "2"
source_section: "3"
---

Assume $\mathfrak{A}$ is a ring with identity. Define the mapping $\varphi: \mathfrak{Q} \to \mathfrak{U}$ by $\varphi(z) = 1 - z$, where $\mathfrak{Q}$ is the group of quasi-regular elements and $\mathfrak{U}$ is the group of units.

**Well-defined:** If $z \in \mathfrak{Q}$, there exists $w \in \mathfrak{A}$ such that $z \circ w = z + w - zw = 0$. Then:
$$(1 - z)(1 - w) = 1 - z - w + zw = 1 - (z + w - zw) = 1 - 0 = 1.$$
Similarly, $(1 - w)(1 - z) = 1$. Hence $1 - z$ is a unit with inverse $1 - w$, so $\varphi(z) \in \mathfrak{U}$.

**Homomorphism:** For $z_1, z_2 \in \mathfrak{Q}$:
\begin{align*}
\varphi(z_1 \circ z_2) &= 1 - (z_1 + z_2 - z_1 z_2) \\
&= 1 - z_1 - z_2 + z_1 z_2 \\
&= (1 - z_1)(1 - z_2) = \varphi(z_1)\varphi(z_2).
\end{align*}

**Injectivity:** If $\varphi(z_1) = \varphi(z_2)$, then $1 - z_1 = 1 - z_2$, so $z_1 = z_2$.

**Surjectivity:** If $u \in \mathfrak{U}$, let $z = 1 - u$. Then $u = 1 - z = \varphi(z)$. To verify $z \in \mathfrak{Q}$: since $u$ has inverse $u^{-1}$, let $w = 1 - u^{-1}$. Then:
$$z \circ w = (1 - u) + (1 - u^{-1}) - (1 - u)(1 - u^{-1}) = 2 - u - u^{-1} - (1 - u - u^{-1} + 1) = 0.$$
Thus $\varphi$ is onto.

Therefore $\varphi$ is a group isomorphism $\mathfrak{Q} \cong \mathfrak{U}$.
