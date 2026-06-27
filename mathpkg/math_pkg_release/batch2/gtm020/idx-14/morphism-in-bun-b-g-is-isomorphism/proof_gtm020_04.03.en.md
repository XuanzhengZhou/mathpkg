---
role: proof
locale: en
of_concept: morphism-in-bun-b-g-is-isomorphism
source_book: gtm020
source_chapter: "4. General Fibre Bundles"
source_section: "3"
---

Let $u: (X, p, B) \rightarrow (X', p', B)$ be a $B$-morphism of principal $G$-bundles. First, we prove that $u$ is injective. For this, we let $u(x_1) = u(x_2)$. Then $p(x_1) = p'u(x_1) = p'u(x_2) = p(x_2)$, so $x_1$ and $x_2$ lie in the same fibre. Since $p^{-1}p(x_1) = x_1G$, there exists $s \in G$ such that $x_2 = x_1 s$. Then $u(x_1) = u(x_2) = u(x_1 s) = u(x_1)s$. Since $X'$ is a free $G$-space, $u(x_1) = u(x_1)s$ implies $s = 1$, hence $x_1 = x_2$. Thus $u$ is injective.

For surjectivity: given $x' \in X'$, let $b = p'(x')$. Choose $x \in p^{-1}(b)$ in $X$. Then $p'u(x) = p(x) = b = p'(x')$, so both $u(x)$ and $x'$ lie in the same fibre of $X'$ over $b$. Since the fibre is a principal homogeneous $G$-space, there exists $s \in G$ with $x' = u(x)s = u(xs)$. Hence $x'$ is in the image of $u$, so $u$ is surjective.

The continuity of $u^{-1}$ follows because a continuous bijection between principal $G$-bundles over the same base is a homeomorphism. This completes the proof that every morphism in $\operatorname{Bun}_B(G)$ is an isomorphism.

Observe that in the proof we used only the fact that $X$ was a free $G$-space whereas $X'$ must be a principal $G$-space.
