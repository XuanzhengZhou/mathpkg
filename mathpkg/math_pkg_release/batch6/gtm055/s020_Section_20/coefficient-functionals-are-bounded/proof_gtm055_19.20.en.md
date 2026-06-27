---
role: proof
locale: en
of_concept: coefficient-functionals-are-bounded
source_book: gtm055
source_chapter: "19"
source_section: "20"
---

The uniqueness requirement in the definition of a basis ensures that $\{x_n\}$ is linearly independent, so Proposition 19.7 applies. Hence the linear space $\mathcal{L}$ of all coefficient sequences of vectors in $\mathcal{E}$ is a Banach space in the norm $\|a\| = \sup_N \|\sum_{n=0}^{N} \alpha_n x_n\|$.

Define $\Phi: \mathcal{L} \to \mathcal{E}$ by $\Phi(a) = \sum_{n=0}^{\infty} \alpha_n x_n$. Then $\|\Phi(a)\| \leq \sup_N \|\sum_{n=0}^{N} \alpha_n x_n\| = \|a\|$, so $\Phi$ is bounded. Moreover, $\Phi$ is bijective (by the definition of basis: every $x$ has unique coefficients), hence a bounded bijection between Banach spaces. By the open mapping theorem (Corollary 13.5), $\Phi^{-1}$ is bounded.

The $n$th coefficient functional $\alpha_n$ is the composition of $\Phi^{-1}$ with the $n$th coordinate projection on $\mathcal{L}$, and each coordinate projection is bounded on $\mathcal{L}$ (as shown in Proposition 19.7). Therefore each $\alpha_n$ is bounded.
