---
role: proof
locale: en
of_concept: injectivity-of-cartan-map
source_book: gtm042
source_chapter: "16"
source_section: "16.1"
---

The second assertion is immediate from Theorem 35: since every element of $R_k(G)$ becomes divisible by $p^n$ after multiplication by a sufficiently high power of $p$, the cokernel of $c$ is a $p$-group. That it is finite follows from the fact that both $P_k(G)$ and $R_k(G)$ are finitely generated free $\mathbb{Z}$-modules.

For the first assertion, note that $P_k(G)$ and $R_k(G)$ are free $\mathbb{Z}$-modules with the same rank, namely $\operatorname{Card}(S_k)$. An injective homomorphism between free $\mathbb{Z}$-modules of the same finite rank whose cokernel is finite must be injective: if $c(x) = 0$ for some nonzero $x$, then $x$ would be a torsion element, but $P_k(G)$ is torsion-free. Thus $c$ is injective.

Alternatively, the injectivity of $c$ follows from the injectivity of $e$ (Theorem 34): since $c = d \circ e$ (15.4a) and $e$ is injective, if $c(x) = 0$ then $d(e(x)) = 0$. But we also have the adjointness relation $\langle x, d(y) \rangle_k = \langle e(x), y \rangle_K$, and the bilinear forms are nondegenerate, forcing $x = 0$.
