---
role: proof
locale: en
of_concept: stickelberger-index-k-even
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

The proof uses the lattice index formalism. Decompose the group ring $R \otimes \mathbb{Q}$ according to the idempotents $e_\chi = \frac{1}{|G|} \sum_{\sigma \in G} \chi(\sigma) \sigma^{-1}$ associated to characters $\chi$. The Stickelberger element $\theta_k$ acts diagonally on each $\chi$-component by multiplication by $B_{k,\chi}/k$.

The index $(R : S_k)$ equals the absolute value of the determinant of multiplication by $\theta_k$ on $R$, which factors as $\prod_\chi |B_{k,\chi}/k|$ over all characters. Accounting for the relation between even and odd characters and the normalization factor $N^{\varphi(N)/2}$ (coming from the conductor in the definition of generalized Bernoulli numbers) yields the stated formula.

The precise computation uses that $\deg(\theta_k) = 0$ for $k$ even and the multiplicative property of indices in lattice chains.
