---
role: proof
locale: en
of_concept: type-three-zero-restriction
source_book: gtm035
source_chapter: "Chapter 19"
source_section: "19.10"
---

# Proof of Restriction of Type (3,0) Forms to Maximally Complex 3-Manifold

**Lemma 19.10.** Let $\alpha$ be a form of type $(3,0)$ defined on a neighborhood of a maximally complex real 3-manifold $M$ in $\mathbb{C}^3$. Then the restriction of $\alpha$ to $M$ is identically zero.

**Proof.** We need only verify this at the tangent space $T_x(M)$ at a single point $x \in M$. By a linear change of variable we may assume, by the maximal complexity of $M$, that

$$T_x(M) = \{(z_1, z_2, z_3) \in \mathbb{C}^3 : \operatorname{Im}(z_2) = 0, \; z_3 = 0\}.$$

We have $\alpha(x) = A \, dz_1 \wedge dz_2 \wedge dz_3$, since $\alpha$ is a $(3,0)$-form. Then the restriction of $\alpha(x)$ to $T_x(M)$ vanishes since $dz_3$ vanishes on $T_x(M)$, and this gives Lemma 19.10. $\square$
