---
role: proof
locale: en
of_concept: tutte-subspace-iff-whitney-function
source_book: gtm054
source_chapter: "F"
source_section: "52"
---

The equivalence follows from the construction relating Tutte subspaces and Whitney functions. If $\mathcal{T}$ is a Tutte subspace over $\mathbb{F}$ for $\Lambda = (V, \mathcal{M})$, then the quotient map $\pi: \mathbb{F}^V \to \mathbb{F}^V / \mathcal{T}$ restricted to the standard basis vectors of $\mathbb{F}^V$ yields a Whitney function $w: V \to \mathbb{F}^V / \mathcal{T}$. The minimal nonempty supports of functions in $\mathcal{T}$ correspond under this map to the cycle structure encoded by $w$.

Conversely, given a Whitney function $w: V \to \mathcal{W}$ (where $\mathcal{W}$ is a vector space over $\mathbb{F}$), one constructs a Tutte subspace $\mathcal{T}$ as the kernel of the linear extension $\tilde{w}: \mathbb{F}^V \to \mathcal{W}$ defined by $\tilde{w}(h) = \sum_{x \in V} h(x) w(x)$. The minimal nonempty supports of functions in $\ker(\tilde{w})$ then coincide with the cycles of $\Lambda$, establishing $\mathcal{T} = \ker(\tilde{w})$ as a Tutte subspace for $\Lambda$ over $\mathbb{F}$.
