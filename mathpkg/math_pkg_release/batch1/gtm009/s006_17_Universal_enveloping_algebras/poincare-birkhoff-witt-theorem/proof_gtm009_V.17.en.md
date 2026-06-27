---
role: proof
locale: en
of_concept: poincare-birkhoff-witt-theorem
source_book: gtm009
source_chapter: "V"
source_section: "17.4"
---
The proof is given in Section 17.4. Fix an ordered basis $(x_\lambda; \lambda \in \Omega)$ of $L$, which identifies $\mathfrak{S}$ with the polynomial algebra in indeterminates $z_\lambda$. For each sequence $\Sigma = (\lambda_1, \dots, \lambda_m)$, let $z_\Sigma = z_{\lambda_1}\dots z_{\lambda_m} \in S^m$ and $x_\Sigma = x_{\lambda_1} \otimes \dots \otimes x_{\lambda_m} \in T^m$. Call $\Sigma$ increasing if $\lambda_1 \leq \dots \leq \lambda_m$. The set $\{z_\Sigma \mid \Sigma \text{ increasing}\}$ is a basis of $\mathfrak{S}$.

The proof proceeds by constructing, for each $m \in \mathbb{Z}^+$, a linear map $f_m: L \otimes S_m \to \mathfrak{S}$ satisfying three properties $(A_m), (B_m), (C_m)$ (Lemma A). These maps are then used to define an action of $L$ on $\mathfrak{S}$, which extends to a representation of $\mathfrak{U}(L)$. By analyzing this representation on the vector $1 \in \mathfrak{S}$, one constructs an inverse to the natural map $\omega: \mathfrak{S} \to \mathfrak{G}$. Lemma B establishes that the representation maps the basis elements $z_\Sigma$ (with $\Sigma$ increasing) to linearly independent elements in $\mathfrak{G}$, proving that $\omega$ is an isomorphism. The detailed induction argument (Lemma C) verifies that the maps $f_m$ satisfy a consistency condition involving the Lie bracket, which is the technical heart of the proof.
