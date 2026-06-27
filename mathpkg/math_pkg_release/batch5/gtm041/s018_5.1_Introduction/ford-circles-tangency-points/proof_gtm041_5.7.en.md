---
role: proof
locale: en
of_concept: ford-circles-tangency-points
source_book: gtm041
source_chapter: "5"
source_section: "5.4"
---

Write $\alpha_1$ for $\alpha_1(h, k)$. From the geometry of the Ford circles, the figure shows that

$$\alpha_1 = \left( \frac{h}{k} - a \right) + i \left( \frac{1}{2k^2} - b \right),$$

where $a$ and $b$ are the horizontal and vertical offsets of the tangency point from the center of $C(h, k)$.

To determine $a$ and $b$, consider the similar right triangles formed by the centers and the tangency point. By similarity,

$$\frac{a}{h - h_1} = \frac{\frac{1}{2k^2}}{\frac{1}{2k^2} + \frac{1}{2k_1^2}} = \frac{k_1^2}{k^2 + k_1^2},$$

so

$$a = \frac{k_1}{k(k^2 + k_1^2)}.$$

Similarly, for the vertical offset,

$$\frac{b}{\frac{1}{2k^2}} = \frac{\frac{1}{2k^2} - \frac{1}{2k_1^2}}{\frac{1}{2k^2} + \frac{1}{2k_1^2}} = \frac{k_1^2 - k^2}{k_1^2 + k^2},$$

which yields

$$b = \frac{k_1^2 - k^2}{2k^2(k_1^2 + k^2)}.$$

Substituting back and simplifying gives the stated formula for $\alpha_1(h, k)$. The formula for $\alpha_2(h, k)$ is obtained analogously. The statement that $\alpha_1(h, k)$ lies on the semicircle with diameter $[h_1/k_1, h/k]$ follows from the geometric construction.
