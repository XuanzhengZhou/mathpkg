---
role: proof
locale: en
of_concept: homomorphism-center-to-homotheties
source_book: gtm042
source_chapter: "6"
source_section: "6.3"
---

This is just a reformulation of Proposition 6 of Section 2.5. Since $\tilde{\rho}_i$ is an algebra homomorphism, and elements of the center of $C[G]$ commute with all elements of $C[G]$ (hence with all $\tilde{\rho}_i(g)$ for $g \in G$), their images under $\tilde{\rho}_i$ commute with all $\rho_i(g)$. By Schur's lemma, any endomorphism of the irreducible representation space $W_i$ that commutes with all $\rho_i(g)$ is a scalar multiple of the identity -- that is, a homothety. Therefore $\tilde{\rho}_i$ maps the center of $C[G]$ into the homotheties of $W_i$, and we obtain an algebra homomorphism $\omega_i$ into $\mathbb{C}$ by identifying each homothety with its scalar factor. The trace formula follows because the trace of a homothety $\lambda \cdot \text{id}_{W_i}$ is $\lambda \cdot n_i$.
