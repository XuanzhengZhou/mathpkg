---
role: proof
locale: en
of_concept: counting-zeros-theorem
source_book: gtm011
source_chapter: "IV"
source_section: "7.2"
---

Since the zeros of an analytic function are isolated, we can write

$$f(z) = (z-a_1)(z-a_2)\cdots(z-a_m)g(z)$$

where $g$ is analytic on $G$ and $g(z) \neq 0$ for any $z$ in $G$. Applying the formula for differentiating a product gives

$$\frac{f'(z)}{f(z)} = \frac{1}{z-a_1} + \frac{1}{z-a_2} + \cdots + \frac{1}{z-a_m} + \frac{g'(z)}{g(z)}$$

for $z \neq a_1, \ldots, a_m$. Now integrate both sides over $\gamma$. Since $\gamma \approx 0$ in $G$ and $\frac{g'}{g}$ is analytic on $G$ (because $g$ never vanishes), Cauchy's Theorem implies $\int_{\gamma} \frac{g'(z)}{g(z)} dz = 0$. By the definition of the winding number,

$$\frac{1}{2\pi i} \int_{\gamma} \frac{1}{z-a_k} dz = n(\gamma; a_k)$$

for each $k$. Summing over $k = 1, \ldots, m$ yields the desired formula.
