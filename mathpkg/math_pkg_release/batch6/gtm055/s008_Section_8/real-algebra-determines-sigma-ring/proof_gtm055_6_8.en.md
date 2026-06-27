---
role: proof
locale: en
of_concept: real-algebra-determines-sigma-ring
source_book: gtm055
source_chapter: "6"
source_section: "8"
---

Sketch (see Problems T, U): Let $\mathbf{S} = \{E \subseteq X : \chi_E \in \mathcal{A}\}$. Verify $\mathbf{S}$ is a $\sigma$-ring. The key step: for any open $U \subseteq \mathbb{R}$, the Weierstrass approximation theorem gives polynomials $p_n$ converging pointwise to $\chi_U$. For $f \in \mathcal{A}$, $p_n \circ f \in \mathcal{A}$ (since $\mathcal{A}$ is a real algebra), and the limit is $\chi_{f^{-1}(U)}$. Thus $f^{-1}(U) \in \mathbf{S}$, proving $f$ is $\mathbf{S}$-measurable. The complex case uses Stone-Weierstrass with polynomials in $\lambda$ and $\bar{\lambda}$.
