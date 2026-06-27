---
role: proof
locale: en
of_concept: mobius-group
source_book: gtm011
source_chapter: "3"
source_section: "3.5"
---

Let $S(z) = \frac{az+b}{cz+d}$ and $T(z) = \frac{\alpha z + \beta}{\gamma z + \delta}$ be two linear fractional transformations. Then

$$(S \circ T)(z) = S(T(z)) = \frac{a\left(\frac{\alpha z + \beta}{\gamma z + \delta}\right) + b}{c\left(\frac{\alpha z + \beta}{\gamma z + \delta}\right) + d}
= \frac{a(\alpha z + \beta) + b(\gamma z + \delta)}{c(\alpha z + \beta) + d(\gamma z + \delta)}
= \frac{(a\alpha + b\gamma)z + (a\beta + b\delta)}{(c\alpha + d\gamma)z + (c\beta + d\delta)},$$

which is again a linear fractional transformation. The identity map $I(z) = z = \frac{1 \cdot z + 0}{0 \cdot z + 1}$ is a Mobius transformation ($1 \cdot 1 - 0 \cdot 0 = 1 \neq 0$). Every Mobius transformation has an inverse that is also a Mobius transformation (as shown in the inverse formula). Composition of functions is associative. Hence the set of Mobius transformations satisfies all group axioms under composition.
