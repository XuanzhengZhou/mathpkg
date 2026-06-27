---
role: proof
locale: en
of_concept: functor-category-as-a-bifunctor
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

The assignment $[-, -]: \mathbf{Cat}^{\mathrm{op}} \times \mathbf{Cat} \to \mathbf{Cat}$ sending $(A, B) \mapsto B^A$ is a bifunctor. On morphisms: for $F: A' \to A$ and $G: B \to B'$, define $[F, G]: B^A \to B'^{A'}$ sending a functor $H: A \to B$ to $G \circ H \circ F: A' \to B'$, and a natural transformation $\alpha: H \Rightarrow H'$ to $G \alpha F$ with components $G(\alpha_{F(a')})$.

Functoriality: $[F', G'] \circ [F, G] = [F \circ F', G' \circ G]$ (note contravariance: $F: A' \to A$, $F': A'' \to A'$, so $F \circ F': A'' \to A$), and $[1_A, 1_B] = 1_{B^A}$. The identity and composition laws follow from those of functors.
