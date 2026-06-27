---
role: proof
locale: en
of_concept: fourier-uniqueness-theorem
source_book: gtm025
source_chapter: "21"
source_section: "§21"
---

Let $h = f - g$. Then $\hat{h} = 0$. By (21.43) and (21.45.a),
$$h(x) = \lim_{n\to\infty} (2\pi)^{-\frac{1}{2}} \int_R \hat{h}(y) \exp(-|y|/n)\exp(ixy)dy = 0$$
for every Lebesgue point $x$ of $h$. Since almost every point is a Lebesgue point, $h = 0$ a.e., so $f = g$ a.e.
