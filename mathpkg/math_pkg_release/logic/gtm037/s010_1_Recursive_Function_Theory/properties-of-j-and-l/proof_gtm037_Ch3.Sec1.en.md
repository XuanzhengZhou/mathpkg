---
role: proof
locale: en
of_concept: properties-of-j-and-l
source_book: gtm037
source_chapter: "3"
source_section: "1"
---

**(i) and (ii)** are obvious from the definitions.

**(iii)** Choose $x$ such that $a = x^2 + \text{Exc}\,a < (x + 1)^2$. Since $\text{Exc}(a + 1) \neq 0$, it is clear that $\text{Exc}(a + 1) = \text{Exc}\,a + 1$. Furthermore, $x^2 \leq a < (x + 1)^2$ and $x^2 \leq a + 1 < (x + 1)^2$, so $x = [\sqrt{a}] = [\sqrt{a + 1}]$ and hence $La = L(a + 1)$.

**(iv)** Note that

$$((a + b)^2 + b)^2 \leq J(a, b) < ((a + b)^2 + b)^2 + 2(a + b)^2 + 2b + 1 = ((a + b)^2 + b + 1)^2.$$

Hence $\text{Exc}\,J(a, b) = a$, and (iv) holds.

**(v)** From the above inequality, $[\sqrt{J(a, b)}] = (a + b)^2 + b$, so

$$LJ(a, b) = \text{Exc}\left[(a + b)^2 + b\right] = b.$$

**(vi)** Suppose $J(a, b) = J(c, d)$. Then by (iv) and (v),

$$a = \text{Exc}\,J(a, b) = \text{Exc}\,J(c, d) = c,$$
$$b = LJ(a, b) = LJ(c, d) = d.$$

Thus $J$ is injective.
