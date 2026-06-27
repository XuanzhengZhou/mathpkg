---
role: proof
locale: en
of_concept: implicit-function-theorem-injective
source_book: gtm051
source_chapter: "0"
source_section: "0.5"
---

Let $dF_0$ be injective. Then there exists a direct sum decomposition $\mathbb{R}^m = \mathbb{R}'^n \oplus \mathbb{R}''^{m-n}$ such that $dF_0: \mathbb{R}^n \to \mathbb{R}'^n$ is an isomorphism. Define

$$\tilde{g}: U \times \mathbb{R}''^{m-n} \to \mathbb{R}^m = \mathbb{R}'^n \oplus \mathbb{R}''^{m-n}$$

by $\tilde{g}(x, y'') = F(x) + y''$, where we identify $F(x) \in \mathbb{R}'^n \subset \mathbb{R}^m$. Then $d\tilde{g}_{(0,0)}$ is bijective: $d\tilde{g}_{(0,0)}(X, Y'') = dF_0(X) + Y''$, since $dF_0$ maps onto $\mathbb{R}'^n$ isomorphically, and $Y''$ accounts for the $\mathbb{R}''^{m-n}$ component.

By the inverse function theorem (0.5.1), $\tilde{g}$ has a local differentiable inverse $g = \tilde{g}^{-1}$ near $0 \in \mathbb{R}^m$. Then for $x$ near $0$:
$$g \circ F(x) = g(\tilde{g}(x, 0)) = (x, 0).$$
This proves the statement. The local diffeomorphism $g$ rectifies $F$ to the standard injection. This is a direct consequence of the inverse function theorem applied to the auxiliary extension $\tilde{g}$.
