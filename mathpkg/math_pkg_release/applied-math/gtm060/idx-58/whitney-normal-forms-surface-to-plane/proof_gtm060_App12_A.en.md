---
role: proof
locale: en
of_concept: whitney-normal-forms-surface-to-plane
source_book: gtm060
source_chapter: "Appendix 12"
source_section: "A. Singularities of smooth mappings of a surface onto a plane"
---

The proof of Whitney's theorem is based on the analysis of the rank of the derivative of a smooth map $f: M^2 \to N^2$. The singular set $\Sigma$ consists of points where the rank drops below 2. Generically, $\Sigma$ is a smooth curve on the source manifold, and the restriction $f|_\Sigma$ has generic singularities.

The key steps are:

1. **Transversality**: By Thom's transversality theorem, a generic smooth map has the property that its 1-jet extension is transverse to the submanifold of 1-jets of rank 1. This ensures $\Sigma$ is a smooth 1-dimensional submanifold.

2. **Fold points**: At a generic point of $\Sigma$, the kernel of $df$ is transverse to $T\Sigma$. In appropriate coordinates (using the preparation theorem), the map reduces to the fold normal form $(x_1, x_2) \mapsto (x_1^2, x_2)$. The image of $\Sigma$ is a smooth curve (the apparent contour), and points on one side have two pre-images while points on the other have none.

3. **Cusp points**: At isolated points on $\Sigma$, the kernel of $df$ becomes tangent to $\Sigma$. These are the cusp (or tuck) points, where the apparent contour develops a semi-cubical cusp $27x^2 = 4y^3$. In suitable coordinates the map becomes $(x_1, x_2) \mapsto (x_1 x_2 - x_1^3, x_2)$.

4. **Stability**: Higher-order degeneracies (where the kernel is tangent to $\Sigma$ to higher order) have codimension $\geq 3$ in the space of map germs, hence do not appear in generic 2-parameter families of mappings from 2-manifolds to 2-manifolds.

The proof that no other stable singularities exist relies on the classification of simple singularities of functions (Arnold's ADE classification) combined with the fact that for maps $M^2 \to N^2$, the singularity type is determined by the contact class of the generating family.

Full details can be found in Whitney's original paper (H. Whitney, *On singularities of mappings of Euclidean spaces. I. Mappings of the plane into the plane*, Ann. Math. 62 (1955), 374–410) and in Arnold's survey cited in the text (V. I. Arnold, *Singularities of smooth mappings*, Russian Math. Surveys 23:1 (1968), 1–44).
