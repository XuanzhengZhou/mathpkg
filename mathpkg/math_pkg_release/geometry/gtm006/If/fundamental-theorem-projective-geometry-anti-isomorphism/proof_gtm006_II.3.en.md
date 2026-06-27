---
role: proof
locale: en
of_concept: fundamental-theorem-projective-geometry-anti-isomorphism
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

The method of proof parallels that of Theorem 2.8 with the necessary modifications. Let $\beta$ be the isomorphism from $\mathcal{P}(V)$ (left vector space over $K$) onto $\mathcal{P}(W)$ (right vector space over $F$). Choose a frame for $\mathcal{P}(W)$ and its pre-image frame for $\mathcal{P}(V)$ as in Theorem 2.8. Coordinatize both planes. The isomorphism $\beta$ induces a bijection $\phi: K \to F$. Using geometric constructions for multiplication: the point $\langle x e_1 + xm e_2 + e_3 \rangle$ in $\mathcal{P}(V)$ maps to a point in $\mathcal{P}(W)$ whose coordinates yield $(xm)^\phi$. Because $W$ is a right vector space, the scalar multiplication acts on the right, so the geometric construction gives $(xm)^\phi = m^\phi x^\phi$, i.e., $\phi$ reverses the order of multiplication. Similarly, addition is preserved: $(x+b)^\phi = x^\phi + b^\phi$. Thus $\phi: K \to F$ is an anti-isomorphism of skewfields. The isomorphism $\beta$ is then induced by the semi-linear transformation sending the basis $g_i$ to $e_i$ composed with the anti-isomorphism $\phi$. $\square$
