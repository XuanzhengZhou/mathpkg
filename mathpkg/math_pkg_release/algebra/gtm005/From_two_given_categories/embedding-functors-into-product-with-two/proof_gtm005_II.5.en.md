---
role: proof
locale: en
of_concept: embedding-functors-into-product-with-two
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

Define $i_0, i_1: C \to C \times \mathbf{2}$ by $i_j(c) = (c, j)$. There is a natural transformation $\iota: i_0 \Rightarrow i_1$ with $\iota_c = (1_c, \alpha)$ where $\alpha: 0 \to 1$ in $\mathbf{2}$.

For any category $D$, functors $F, G: D \to C$, and natural transformation $\tau: F \Rightarrow G$, there exists a unique functor $H: D \to C \times \mathbf{2}$ such that $i_0 \circ H = F$, $i_1 \circ H = G$, and $\iota H = \tau$ (where $\iota H$ denotes whiskering).

Define $H(d) = (F(d), 0)$ if $\tau$ is treated differently — the standard construction uses $H: D \to C^{\mathbf{2}}$ defined by $H(d) = (\tau_d: F(d) \to G(d))$. This shows $C^{\mathbf{2}}$ represents the functor sending $D$ to the set of triples $(F, G, \tau)$.
