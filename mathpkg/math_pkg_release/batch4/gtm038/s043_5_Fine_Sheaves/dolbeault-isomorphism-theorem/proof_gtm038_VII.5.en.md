---
role: proof
locale: en
of_concept: dolbeault-isomorphism-theorem
source_book: gtm038
source_chapter: "VII"
source_section: "5. Fine Sheaves (Theorems of Dolbeault and de Rham)"
---

**Proof.** All the hypotheses of Theorem 3.1 of Chapter VI are satisfied, so
$$
H^{p,q}(X) \simeq H_{q0}, \qquad H^q(X, \Omega^p) \simeq H_{0q}.
$$
Since $H^i(X, \mathcal{A}^{p,q}) = 0$ for $i \geqslant 1$ (the sheaves $\mathcal{A}^{p,q}$ are fine, hence acyclic), the $\delta''$-sequences are exact. Since the sequence
$$
0 \rightarrow \Omega^p \rightarrow \mathcal{A}^{p,0} \rightarrow \mathcal{A}^{p,1} \rightarrow \cdots
$$
is exact and the canonical flabby resolution functor $\mathfrak{W}$ is an exact functor, all sequences
$$
0 \rightarrow S_v \rightarrow A_v^0 \rightarrow A_v^1 \rightarrow \cdots
$$
are exact. Since all sheaves in these resolutions are flabby, the $\delta'$-sequences are exact. Therefore $H_{0q} \simeq H_{q0}$, and the theorem follows:
$$
H^{p,q}(X) \simeq H^q(X, \Omega^p).
$$
