---
role: proof
locale: en
of_concept: gl-action-open-orbit-dimension-condition
source_book: gtm014
source_chapter: "III"
source_section: "§6"
---

% NOTE: Proof is incomplete in OCR source — cuts off at page break after first sentence.

The dimension of $\text{Hom}(V \circ V, W)$ is $n^2(n + 1)/2$ and the dimension of $G$ is $2n^2$. Note that an orbit of $G$ is diffeomorphic to some homogeneous space $G/H$ where $H$ is the stabilizer of a point. For an orbit to be open, its dimension must equal the dimension of the ambient space $\text{Hom}(V \circ V, W)$, which requires $\dim G - \dim H = n^2(n+1)/2$. Since $\dim G = 2n^2$, this forces $\dim H \leq 0$, meaning the stabilizer must be discrete.

The stabilizer $H$ of a generic element $C \in \text{Hom}(V \circ V, W)$ consists of pairs $(A, B) \in GL(V) \times GL(W)$ such that $B \circ C \circ A^{-1} = C$. A dimension count shows that for $n \geq 3$, the stabilizer always has positive dimension, so no orbit can be open. For $n = 1, 2$, explicit open orbits exist (corresponding to fold and cusp singularities respectively).

[The remainder of the proof is missing from the OCR source due to a page break in the original PDF scan.]
