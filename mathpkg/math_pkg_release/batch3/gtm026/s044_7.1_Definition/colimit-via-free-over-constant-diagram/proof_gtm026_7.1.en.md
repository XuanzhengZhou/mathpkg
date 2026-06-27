---
role: proof
locale: en
of_concept: colimit-via-free-over-constant-diagram
source_book: gtm026
source_chapter: "7"
source_section: "7.1"
---

*Proof.* Compare the universal property of a free $(L, \psi)$ over $D$ with the definition of a colimit. In both cases, given any upper bound $(A, \Gamma)$ of $D$ (equivalently, any diagram morphism $\Gamma: D \to \tilde{A}$ in $\mathcal{K}^{\Delta}$), there exists a unique morphism $f: L \to A$ in $\mathcal{K}$ such that the appropriate diagram commutes. For a colimit, this means $\psi_i f = \Gamma_i$ for all $i \in N(\Delta)$. For a free object over $D$ with respect to $(\tilde{\cdot})$, this means the unique extension $\tilde{f}: \tilde{L} \to \tilde{A}$ satisfies $\psi \tilde{f} = \Gamma$ in $\mathcal{K}^{\Delta}$. Since $(\tilde{f})_i = f$, these two conditions are identical. Thus the two universal properties coincide. $\square$
