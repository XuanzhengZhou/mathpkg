---
role: proof
locale: en
of_concept: right-vector-space-via-anti-automorphism
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "6"
---

Define right scalar multiplication by $x \bar{\alpha} = \alpha x$ for $x \in \mathfrak{R}$, $\alpha \in \Delta$. We verify the axioms for a right vector space.

For the distributive law with respect to vector addition:
$$(x + y)\bar{\alpha} = \alpha(x + y) = \alpha x + \alpha y = x\bar{\alpha} + y\bar{\alpha}.$$

For the distributive law with respect to scalar addition:
$$x(\overline{\alpha + \beta}) = (\alpha + \beta)x = \alpha x + \beta x = x\bar{\alpha} + x\bar{\beta}.$$

For the associative law, using the anti-multiplicative property $\overline{\alpha\beta} = \bar{\beta}\bar{\alpha}$:
$$(x\bar{\alpha})\bar{\beta} = \beta(\alpha x) = (\beta\alpha)x = x\overline{\beta\alpha} = x(\bar{\alpha}\,\bar{\beta}).$$

Here we used that $\overline{\beta\alpha} = \bar{\alpha}\,\bar{\beta}$, which follows from the anti-automorphism property $\overline{\beta\alpha} = \bar{\alpha}\,\bar{\beta}$ (reversing the order). Thus the right scalar multiplication $x\bar{\alpha}$ satisfies all axioms.

For the dimensionality: if $\{e_i\}$ is a left basis with $x = \sum \xi_i e_i$, then $x = \sum \alpha_i e_i$ as a left combination. Applying the anti-automorphism, $x = \sum e_i \bar{\xi}_i$ expresses $x$ as a right linear combination of the same $\{e_i\}$. Since the anti-automorphism is bijective, linear independence is preserved in both directions, so $\{e_i\}$ is also a right basis.
