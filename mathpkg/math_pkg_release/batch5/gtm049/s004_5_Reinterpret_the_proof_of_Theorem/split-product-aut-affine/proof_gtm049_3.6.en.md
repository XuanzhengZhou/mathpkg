---
role: proof
locale: en
of_concept: split-product-aut-affine
source_book: gtm049
source_chapter: "3"
source_section: "3.6"
---

For part (i), the non-trivial part is the proof of condition (1) for a split product: every element of $\operatorname{Aut} \mathcal{A}(V)$ can be uniquely written as the product of a semi-linear isomorphism (acting as an element of $S(V)$ via $f \mapsto \mathcal{A}(f)$) and a translation.

This follows from Theorem 5: any affine isomorphism $\alpha \in \operatorname{Aut} \mathcal{A}(V)$ determines a semi-linear isomorphism $g$ of $V$ onto $V$ with respect to some field automorphism $\zeta$ (when $\dim V \geq 2$) or a field bijection (when $\dim V = 1$). After composing with the inverse of the affine map induced by $g$, one obtains an affine isomorphism that preserves directions, i.e., a translation. The uniqueness of the decomposition follows from the uniqueness of $g$ in Theorem 5.

The isomorphism $S \cong S(V)$ via $f \mapsto \mathcal{A}(f)$ is the semi-linear analogue of the natural embedding of the general semi-linear group into the affine automorphism group. The isomorphism $T \cong V$ via $v \mapsto \mathcal{A}(t_v)$ sends a vector to the translation by that vector.

For part (ii), restricting to affinities means restricting to those affine isomorphisms whose associated field automorphism is the identity. Thus $S(V)$ is replaced by $\operatorname{Aut} V$ (the general linear group), yielding the split product decomposition of the affine group $\operatorname{Af} \mathcal{A}(V)$ as the semidirect product of $\operatorname{Aut} V$ and the translation group $V$.

The verification of condition (2) for a split product -- that the projection onto the first factor is a homomorphism -- is left as an exercise.
