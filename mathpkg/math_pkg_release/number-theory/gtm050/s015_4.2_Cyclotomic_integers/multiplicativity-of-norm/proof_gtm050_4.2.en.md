---
role: proof
locale: en
of_concept: multiplicativity-of-norm
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

Let $h(\alpha) = f(\alpha)g(\alpha)$. By definition,
$$Nh(\alpha) = h(\alpha) \cdot h(\alpha^2) \cdot h(\alpha^3) \cdots h(\alpha^{\lambda-1}).$$

Substituting $h(\alpha^j) = f(\alpha^j)g(\alpha^j)$ for each $j = 1, 2, \ldots, \lambda-1$, we obtain
$$Nh(\alpha) = \prod_{j=1}^{\lambda-1} f(\alpha^j)g(\alpha^j) = \left(\prod_{j=1}^{\lambda-1} f(\alpha^j)\right) \cdot \left(\prod_{j=1}^{\lambda-1} g(\alpha^j)\right) = Nf(\alpha) \cdot Ng(\alpha).$$

The rearrangement of factors is justified by the commutativity of multiplication of complex numbers. Thus the norm is multiplicative.
