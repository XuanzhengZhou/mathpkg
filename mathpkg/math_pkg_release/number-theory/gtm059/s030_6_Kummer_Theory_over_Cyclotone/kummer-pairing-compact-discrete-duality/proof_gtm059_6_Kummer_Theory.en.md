---
role: proof
locale: en
of_concept: kummer-pairing-compact-discrete-duality
source_book: gtm059
source_chapter: "6"
source_section: "Kummer Theory over Cyclotomic Z_p-extension"
---

Let $K_{\infty} = \bigcup K_n$ be the cyclotomic $\mathbb{Z}_p$-extension. For each finite layer $K_n$, let $G_n$ be the Galois group of the maximal $p$-abelian extension of $K_n$, and let $A_n$ be the $p$-primary subgroup of the ideal class group of $K_n$.

By class field theory, there is a Kummer pairing at each finite level:
$$G_n \times A_n \to \mu_{p^{\infty}}.$$

This pairing is compatible with the norm and extension maps as $n$ varies. Specifically, the natural maps $G_{n+1} \to G_n$ (restriction) and $A_n \to A_{n+1}$ (extension of ideals) satisfy the compatibility condition required for taking limits.

Forming the projective limit $G = \varprojlim G_n$ and the direct limit $A = \varinjlim A_n$, the Kummer pairing extends to a pairing
$$G \times A \to \mu_{p^{\infty}}$$
which is a compact-discrete duality. Here $G$ carries the projective limit topology (making it a compact $\mathbb{Z}_p$-module) and $A$ carries the discrete topology.

The pairing is $\mathbb{Z}_p$-bilinear and non-degenerate on both sides by the properties of the Kummer pairing at finite levels. The result follows from Chapter 5, Theorem 4.4.

We also note the additional property: for $g \in G$,
$$\langle g^{p^n}, A \rangle = \langle g, p^n A \rangle$$
which shows that multiplication by $p^n$ is compatible with the pairing structure. In particular, $g^{p^n} \to 1$ in the projective limit topology, making $G$ a torsion $\mathbb{Z}_p$-module (a torus module over $\mathbb{Z}_p$).

Furthermore, the direct limit satisfies
$$\varinjlim A_n / p^n A_n = \varinjlim A_n = A$$
when restricted to representative ideals prime to $p$.
