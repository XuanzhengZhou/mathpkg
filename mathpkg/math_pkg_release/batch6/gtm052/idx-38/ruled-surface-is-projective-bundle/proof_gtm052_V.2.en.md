---
role: proof
locale: en
of_concept: ruled-surface-is-projective-bundle
source_book: gtm052
source_chapter: "V"
source_section: "2"
---

Given a ruled surface $\pi: X \rightarrow C$, then by definition $\pi$ has a section $\sigma$. Let $D = \sigma(C)$. Then $D$ is a divisor on $X$, and $D.f = 1$ for any fibre. By Lemma 2.1, $\mathcal{E} = \pi_*\mathcal{L}(D)$ is a locally free sheaf of rank $2$ on $C$. Furthermore, there is a natural map $\pi^*\mathcal{E} = \pi^*\pi_*\mathcal{L}(D) \rightarrow \mathcal{L}(D)$ on $X$. This map is surjective. Indeed, by Nakayama's lemma, it is enough to check this on any fibre $X_y$. But $X_y \cong \mathbf{P}^1$, and $\mathcal{L}(D)|_{X_y}$ is $\mathcal{O}_{\mathbf{P}^1}(1)$. By (II, 7.12), the surjection $\pi^*\mathcal{E} \rightarrow \mathcal{L}(D)$ defines a morphism $X \to \mathbf{P}(\mathcal{E})$ over $C$, which is an isomorphism since it is an isomorphism on each fibre.

For the converse, note that $\mathbf{P}(\mathcal{E})$ is a $\mathbf{P}^1$-bundle over $C$, and the natural map $\mathcal{E} \to \mathcal{O}_{\mathbf{P}(\mathcal{E})}(1)$ gives a surjection $\mathcal{O}_C \to \mathcal{E} \otimes \mathcal{L}^{-1}$ for some invertible sheaf $\mathcal{L}$ on $C$, which by (II, 7.12) corresponds to a section of $\mathbf{P}(\mathcal{E})$ over $C$.

For the uniqueness statement: If $\mathbf{P}(\mathcal{E}) \cong \mathbf{P}(\mathcal{E}')$ over $C$, then pulling back $\mathcal{O}_{\mathbf{P}(\mathcal{E}')}(1)$ gives a line bundle on $\mathbf{P}(\mathcal{E})$ which must be of the form $\mathcal{O}_{\mathbf{P}(\mathcal{E})}(n) \otimes \pi^*\mathcal{L}$ for some $n \in \mathbf{Z}$ and $\mathcal{L} \in \operatorname{Pic} C$. Since it has degree $1$ on fibres, $n = 1$, and by (II, 7.9) we have $\mathcal{E}' \cong \mathcal{E} \otimes \mathcal{L}$.
