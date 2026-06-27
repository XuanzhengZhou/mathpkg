---
role: proof
locale: en
of_concept: theorem-9-involutorial-anti-automorphism
source_book: gtm031
source_chapter: "IX"
source_section: "12"
---
Let $h$ be the weakly hermitian scalar product obtained from Theorem 8, so that $h(y, x) = \nu \overline{h(x, yQ)}$ for some $\nu \in \Delta$ and semi-linear automorphism $Q$ with associated automorphism $a$. Since $\Psi^2 = 1$, iteration gives $h(x, y) = \nu h(x, y) \bar{\nu}$. Choosing $x, y$ with $h(x, y) = 1$ yields $\bar{\nu} = \nu^{-1}$.

If $\nu = -1$, then $h$ is skew hermitian and we are done. If $\nu \neq -1$, set $\tau = (\nu + 1)^{-1}$ and verify that $\tau^{-1}\bar{\tau} = (\nu + 1)(\bar{\nu} + 1)^{-1} = (\nu + 1)(\nu^{-1} + 1)^{-1} = \nu$. Define $s(x, y) = h(x, y)\tau$. Then $s$ is a scalar product whose associated anti-automorphism is $\alpha \mapsto \alpha^* \equiv \tau^{-1}\bar{\alpha}\tau$. Moreover,
$$s(y, x)^* = \tau^{-1}s(y, x)\tau = \tau^{-1}\bar{\tau}h(y, x)\tau = \nu h(y, x)\tau = h(x, y)\tau = s(x, y).$$
Thus $s$ is hermitian.

The converse is immediate: if $\mathfrak{R}$ has a non-degenerate hermitian or skew hermitian scalar product, then for any $A \in \mathfrak{L}(\mathfrak{R} \mid \mathfrak{R})$, its transpose $A'$ satisfies $A'' = Q^{-1}AQ$, and the mapping $A \mapsto A'$ is an anti-automorphism of $\mathfrak{L}(\mathfrak{R} \mid \mathfrak{R})$.
