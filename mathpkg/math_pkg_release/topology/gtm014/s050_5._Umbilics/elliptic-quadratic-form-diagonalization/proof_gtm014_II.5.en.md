---
role: proof
locale: en
of_concept: elliptic-quadratic-form-diagonalization
source_book: gtm014
source_chapter: "II"
source_section: "5"
---

Take $\lambda = \left(\frac{a}{a-b}\right)^{1/4}$. Under the coordinate change $\bar{x}_1 = \lambda x_1$, $\bar{x}_2 = \frac{1}{\lambda} x_2$, we compute:

$$x_1 = \frac{\bar{x}_1}{\lambda}, \qquad x_2 = \lambda \bar{x}_2.$$

Substituting into the quadratic form:
$$a(x_1^2 - x_2^2) + bx_2^2 = a\left(\frac{\bar{x}_1^2}{\lambda^2} - \lambda^2 \bar{x}_2^2\right) + b\lambda^2 \bar{x}_2^2 = \frac{a}{\lambda^2}\bar{x}_1^2 + (b - a)\lambda^2 \bar{x}_2^2.$$

With $\lambda^4 = \frac{a}{a-b}$, we have $\frac{a}{\lambda^2} = a \cdot \frac{\sqrt{a-b}}{\sqrt{a}} = \sqrt{a(a-b)}$, and $(b-a)\lambda^2 = (b-a)\sqrt{\frac{a}{a-b}} = -\sqrt{a(a-b)}$. Thus:

$$\frac{a}{\lambda^2} = -(b-a)\lambda^2 = \sqrt{a(a-b)}.$$

Setting $\bar{a} = \sqrt{a(a-b)}$, the form becomes $\bar{a}(\bar{x}_1^2 - \bar{x}_2^2)$. Since $a(0) = 1$ and $b(0) = 0$, $\bar{a}(0) = 1$ and $\lambda(0) = 1$. Moreover, $\lambda$ depends smoothly on $z$ since $a$ and $b$ are smooth and $a-b > 0$ near $z = 0$ (by continuity, as $a(0)-b(0) = 1$).
