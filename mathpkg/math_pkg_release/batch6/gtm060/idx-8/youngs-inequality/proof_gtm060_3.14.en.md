---
role: proof
locale: en
of_concept: youngs-inequality
source_book: gtm060
source_chapter: "3"
source_section: "14"
---

By definition of the Legendre transform, for any $x$ and $p$,

$$F(x, p) = px - f(x) \leq g(p),$$

since $g(p) = \max_x F(x, p)$. Rearranging gives Young's inequality:

$$px \leq f(x) + g(p).$$

For the classical case, let $f(x) = x^\alpha/\alpha$ with $\alpha > 1$. Its Legendre transform is $g(p) = p^\beta/\beta$ where $1/\alpha + 1/\beta = 1$, $\beta > 1$. Substituting into the inequality yields

$$px \leq \frac{x^\alpha}{\alpha} + \frac{p^\beta}{\beta}$$

for all $x > 0$, $p > 0$.
