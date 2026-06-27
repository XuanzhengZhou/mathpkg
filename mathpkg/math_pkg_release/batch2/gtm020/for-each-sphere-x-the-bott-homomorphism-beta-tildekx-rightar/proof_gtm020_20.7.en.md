---
locale: en
of_concept: for-each-sphere-x-the-bott-homomorphism-beta-tildekx-rightar
role: proof
source_book: gtm020
source_chapter: 20. General Theory of Characteristic Classes
source_section: '7'
---

We begin by proving the Bott map $\beta$ is an isomorphism for $X = S^{2k}$ and the integrality statement, both by induction on $k$.

For this, we consider the following diagram:

$$\tilde{H}^*(S^{2k}, Z) \xrightarrow{\text{ch}} \tilde{H}^*(S^{2k+2}, Z) \xrightarrow{\text{cup with } u} \tilde{H}^*(S^{2k+2}, Q)$$

Here $u \in H^2(S^2, Z)$ is the canonical generator. The above diagram commutes since $ch(\gamma - 1) = u$. The bottom two horizontal arrows are isomorphisms. If ch factors through $\tilde{H}^*(S^{2k}, Z)$ by an isomorphism, then $\beta$ is injective, and, by (9.5), $\beta$ is bijective. If $\beta$ is an isomorphism, then ch factors through $\tilde{H}^*(S^{2k+2}, Z)$ by an isomorphism. Since the induction starts at $k = 1$, the integrality theorem holds.

Since $\tilde{K}(S^1) = [S^0, U]_0$ and $U$ is connected, and since $\beta$ is an epimorphism, we have $\tilde{K}(S^{2k+1}) = 0$ for all $k$.

10. Comparison of $K$-Theory and Cohomology Definitions of Hopf Invariant

10.1 Let $f: S^{2n-1} \rightarrow S^n$ be a map, and form $C_f$, the cell complex, with one 0 cell, one $n$ cell, and one 2$n$ cell. From the sequence of spaces $S^{2n-1} \xrightarrow{f} S^n \rightarrow C_f \rightarrow SS^{2n-1} = S^{2n}$ there are the following isomorphisms in integral cohomology: $H^n(S^n) \leftarrow H^n(C_f)$ and $H^{2n}(C_f) \leftarrow H^{2n}(S^{2n})$. There are well classes $c_n \in H^n(S^n)$ such that $ch_n \beta_n = c_n$ for $n$ even where $ch_n$ is the $n$th component of ch. In this way there are two classes $a^* \in H^n(C_f)$ and $b^* \in H^{2n}(C_f)$ with $ch_n a_f = a^*$ and $ch_{2n} b_f = b^*$ for $n$ even. The cohomology Hopf invariant $h_f^*$ is defined by $(a^*)^2 = h_f^*b^*.$ By (graded) commutativity of the cup product, $h_f^* = 0$ for $n$ odd. The main result of this section is contained in the next proposition.
