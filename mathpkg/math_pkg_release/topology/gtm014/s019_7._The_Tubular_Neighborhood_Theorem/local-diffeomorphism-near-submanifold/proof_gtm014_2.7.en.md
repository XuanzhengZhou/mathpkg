---
role: proof
locale: en
of_concept: local-diffeomorphism-near-submanifold
source_book: gtm014
source_chapter: "2"
source_section: "7"
---

*Proof.* Since $df_x$ is an isomorphism for each $x \in X$, by the Inverse Function Theorem there exist open neighborhoods $W_i$ of $x$ in $Y$ and $W_i'$ of $f(x)$ in $Y'$ such that $f|_{W_i}: W_i \to W_i'$ is a diffeomorphism. Let $f_i$ denote this restriction and $f_i^{-1}$ its inverse.

Let $\{W_i\}_{i \in I}$ be a locally finite covering of $X$ by such neighborhoods. For each $i$, let $V_i = f(W_i)$ and note that $V_i$ is open in $Y'$. Define $F = \bigcup_{i \in I} V_i$, which is an open neighborhood of $f(X)$ in $Y'$.

For each $x \in X$, let $G_x = \bigcap_{i: x \in W_i} V_i$, which is an open neighborhood of $f(x)$ in $Y'$. Consider $H = \bigcap_{x \in X} G_x$ (or more precisely, shrink via a partition of unity).

For any point $y \in H \cap V_{i_1} \cap \cdots \cap V_{i_s}$, the local inverses agree:
$$f_{i_1}^{-1}|_{H} = \cdots = f_{i_s}^{-1}|_{H}$$
using the uniqueness of inverse functions and the fact that $f_{i_1}^{-1}(y) = \cdots = f_{i_s}^{-1}(y)$ since $f$ is injective on a neighborhood of $X$.

Define $\tilde{G}_x = H \cap G_x$, which is an open neighborhood of $f(x)$ in $Y'$ and satisfies $\tilde{G}_x \subset F$. Let $G = \bigcup_{x \in X} \tilde{G}_x$; this is an open neighborhood of $f(X)$ in $Y'$.

Now define $g: G \to Y$ by $g(y) = f_i^{-1}(y)$ if $y \in V_i$. The map $g$ is well-defined since $G \subset F$ and the local inverses agree on overlaps by the uniqueness argument above. Moreover, $g$ is smooth since locally $g = f_i^{-1}$ for some $i$.

By construction, $f \circ g = \mathrm{id}_G$, so $g$ is a diffeomorphism onto its image. Set $U = g(G) \subset Y$. Then $U$ is an open neighborhood of $X$ in $Y$ and $f|_U: U \to G$ is a diffeomorphism with inverse $g$. ∎
