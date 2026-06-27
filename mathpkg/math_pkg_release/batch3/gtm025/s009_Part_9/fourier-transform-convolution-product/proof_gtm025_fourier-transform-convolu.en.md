---
role: proof
locale: en
of_concept: fourier-transform-convolution-product
source_book: gtm025
source_chapter: "21"
source_section: "§21"
---

For all $y \in R$,
$$\widehat{f * g}(y) = (2\pi)^{-\frac{1}{2}} \int_R f * g(x) \exp(-iyx)dx$$
$$= (2\pi)^{-\frac{1}{2}} \int_R (2\pi)^{-\frac{1}{2}} \int_R f(x-t)g(t)dt \exp(-iyx)dx$$
$$= \frac{1}{2\pi} \int_R g(t) \int_R f(x-t)\exp(-iyx)dx dt$$
$$= \frac{1}{2\pi} \int_R g(t) \int_R f(u)\exp(-i(t+u)y)du dt$$
$$= \frac{1}{2\pi} \int_R g(t)\exp(-iyt) \int_R f(u)\exp(-iyu)du dt = \hat{f}(y)\hat{g}(y).$$

We have used Fubini's theorem and (12.44).
