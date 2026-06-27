---
role: proof
locale: en
of_concept: degrees-divide-index-of-center
source_book: gtm042
source_chapter: "6"
source_section: "6.5"
---

(This proof is due to J. Tate.)

Let $g = |G|$ and $c = |C|$, and let $\rho: G \to \text{GL}(W)$ be an irreducible representation of $G$ of degree $n$.

If $s \in C$, then $\rho(s)$ commutes with all $\rho(t)$ for $t \in G$ (since $s$ is central). By Schur's lemma, $\rho(s)$ is a homothety. Denote it by $\lambda(s) \cdot \text{id}_W$. The map $\lambda: s \mapsto \lambda(s)$ is a homomorphism $C \to \mathbb{C}^*$.

Let $m \geqslant 0$ be an integer, and form the $m$-fold tensor product representation
$$\rho^m: G^m \to \text{GL}(W^{\otimes m})$$
of $m$ copies of $\rho$. By Theorem 10 of Section 3.2, this is an irreducible representation of $G^m = G \times \cdots \times G$.

For an element $(s_1, \ldots, s_m) \in C^m$, its image under $\rho^m$ is the homothety of ratio $\lambda(s_1 \cdots s_m)$. Consider the subgroup
$$H = \{(s_1, \ldots, s_m) \in C^m : s_1 \cdots s_m = 1\}.$$
Then $H$ acts trivially on $W^{\otimes m}$, so by passing to the quotient we obtain an irreducible representation of $G^m / H$.

The order of $G^m / H$ is $g^m / |H| = g^m / c^{m-1}$ (since $|H| = c^{m-1}$, as the product map $C^m \to C$ is surjective with kernel $H$). The degree of this representation is $n^m$.

By Corollary 2 to Proposition 16, the degree of an irreducible representation divides the order of the group. Applying this to $G^m/H$, we get $n^m \mid g^m / c^{m-1}$.

Thus $(g/(cn))^m \in c^{-1}\mathbb{Z}$ for all $m \geqslant 0$. This implies that $g/(cn)$ is an integer (since if a rational number has all powers lying in a finitely generated $\mathbb{Z}$-module, it must be integral over $\mathbb{Z}$, hence an integer by the rational algebraic integer property). Therefore $n \mid (G:C) = g/c$.
