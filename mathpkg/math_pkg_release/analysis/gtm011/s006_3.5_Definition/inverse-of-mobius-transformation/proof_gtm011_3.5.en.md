---
role: proof
locale: en
of_concept: inverse-of-mobius-transformation
source_book: gtm011
source_chapter: "3"
source_section: "3.5"
---

Let $S(z) = \frac{az+b}{cz+d}$ with $ad-bc \neq 0$, and define $T(z) = \frac{dz-b}{-cz+a}$. Compute $S(T(z))$:

$$S(T(z)) = \frac{a\left(\frac{dz-b}{-cz+a}\right) + b}{c\left(\frac{dz-b}{-cz+a}\right) + d}
= \frac{a(dz-b) + b(-cz+a)}{c(dz-b) + d(-cz+a)}
= \frac{adz - ab - bcz + ab}{cdz - bc - cdz + ad}
= \frac{(ad-bc)z}{ad-bc} = z.$$

Similarly, $T(S(z)) = z$. Hence $S^{-1} = T$.
