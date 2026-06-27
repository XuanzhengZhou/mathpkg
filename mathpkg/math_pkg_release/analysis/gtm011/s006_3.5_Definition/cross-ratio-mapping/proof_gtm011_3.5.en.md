---
role: proof
locale: en
of_concept: cross-ratio-mapping
source_book: gtm011
source_chapter: "3"
source_section: "3.5"
---

First, verify that each formula defines a Mobius transformation. For the case $z_2, z_3, z_4 \in \mathbb{C}$:

$$S(z) = \frac{(z_2 - z_4)z - z_3(z_2 - z_4)}{(z_2 - z_3)z - z_4(z_2 - z_3)}.$$

The determinant condition $ad-bc = (z_2-z_4)(-z_4(z_2-z_3)) - (-z_3(z_2-z_4))(z_2-z_3) = (z_2-z_4)(z_2-z_3)(z_3-z_4) \neq 0$ since the three points are distinct. The cases where one point is $\infty$ are also Mobius transformations.

Now verify the action: $S(z_3) = \frac{z_3 - z_3}{z_3 - z_4} / \frac{z_2 - z_3}{z_2 - z_4} = 0$. $S(z_4)$: the denominator $z - z_4$ vanishes, so $S(z_4) = \infty$. $S(z_2) = \frac{z_2 - z_3}{z_2 - z_4} / \frac{z_2 - z_3}{z_2 - z_4} = 1$. The cases with a point at $\infty$ are verified similarly by direct substitution.

Uniqueness follows from the theorem that a Mobius transformation is uniquely determined by its action on three points: if $T$ also satisfies $T(z_2) = 1$, $T(z_3) = 0$, $T(z_4) = \infty$, then $S^{-1} \circ T$ fixes $z_2, z_3, z_4$, hence is the identity, so $T = S$.
