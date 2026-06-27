---
role: proof
locale: en
of_concept: implicit-function-theorem-surjective
source_book: gtm051
source_chapter: "0"
source_section: "0.5"
---

Let $dF_0$ be surjective. Decompose $\mathbb{R}^n = \mathbb{R}'^m \oplus \mathbb{R}''^{n-m}$ so that $dF_0|_{\mathbb{R}'^m}: \mathbb{R}'^m \to \mathbb{R}^m$ is an isomorphism. Define

$$\tilde{h}: U \subset \mathbb{R}^n = \mathbb{R}'^m \oplus \mathbb{R}''^{n-m} \to \mathbb{R}^n = \mathbb{R}'^m \oplus \mathbb{R}''^{n-m}$$

by $\tilde{h}(v', v'') = (F(v', v''), v'')$, where we identify $\mathbb{R}'^m$ on the right-hand side with $\mathbb{R}^m$. Then

$$d\tilde{h}_0 = dF_0|_{\mathbb{R}'^m} + \text{id}|_{\mathbb{R}''^{n-m}}$$

is bijective. By the inverse function theorem (0.5.1), $\tilde{h}$ has a local differentiable inverse $h = \tilde{h}^{-1}$ near $0 \in \mathbb{R}^n$. Then for $(y', y'')$ near $0$:
$$F \circ h(y', y'') = F(\tilde{h}^{-1}(y', y'')) = y'.$$
This proves the normal form. The local diffeomorphism $h$ rectifies the domain so that $F$ becomes the projection onto the first $m$ coordinates.
