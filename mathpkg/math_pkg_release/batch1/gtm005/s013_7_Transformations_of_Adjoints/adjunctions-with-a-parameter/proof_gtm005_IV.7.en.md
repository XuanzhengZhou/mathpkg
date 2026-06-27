---
role: proof
locale: en
of_concept: adjunctions-with-a-parameter
source_book: gtm005
source_chapter: "IV"
source_section: "7. Transformations of Adjoints"
---

The condition that the adjunction be natural in $p \in P$ is the commutativity of the square
$$\begin{array}{ccc}
\hom(F(x, p), a) & \cong & \hom(x, G(p, a)) \\[4pt]
\hom(F(x, h), a) \downarrow & & \downarrow \hom(x, G(h, a)) \\[4pt]
\hom(F(x, p'), a) & \cong & \hom(x, G(p', a))
\end{array}$$
for every arrow $h : p \to p'$ in $P$.

This commutativity (for all $a$) states precisely that $G(h, -) : G(p', -) \to G(p, -)$ must be chosen as the conjugate natural transformation to $F(-, h) : F(-, p) \to F(-, p')$. By the theorem on conjugate natural transformations, given the natural transformation $F(-, h)$, there is a unique conjugate $G(h, -)$ making the square commute. This assignment respects composition in $P$ by the uniqueness of conjugate pairs, yielding a bifunctor $G : P^{\mathrm{op}} \times A \to X$ with the required naturality in all three variables.
