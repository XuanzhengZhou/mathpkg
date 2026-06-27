---
role: proof
locale: en
of_concept: corollary-4-1-exact-sequence
source_book: gtm059
source_chapter: "5"
source_section: "4"
---

*Proof.* This follows directly from Theorem 4.1. The exact sequence $1 \to G_1 \to G \to \mathbb{Z}_p \to 1$ is the defining exact sequence of the semidirect product $G = G_1 \rtimes I$ with $I \cong \mathbb{Z}_p$, where the map $G \to \mathbb{Z}_p$ is given by restricting to $K_\infty$ and identifying $\operatorname{Gal}(K_\infty/K)$ with $\mathbb{Z}_p$ via the completion isomorphism $\operatorname{Gal}(K_\infty/K) \cong \mathbb{Z}_p$.

Since $I$ provides a splitting, the sequence is split exact. The descending filtration follows from the tower structure $K \subset K_1 \subset K_2 \subset \cdots$: each $G_n$ is the subgroup of $G$ fixing $K_n$, so $G/G_n \cong \operatorname{Gal}(M_\infty \cap K_n^{\text{ab}} / K)$, which corresponds to restricting the automorphisms to $K_n$. The fact that $G_n = G^{p^n}[G,G]$ follows from the description of the Galois group of the $\mathbb{Z}_p$-extension combined with the semidirect product structure.
