---
role: proof
locale: en
of_concept: gamma-residue-at-negative-integers
source_book: gtm011
source_chapter: "7"
source_section: "7.10"
---

From the shift formula (7.8),

$$(z+n)\Gamma(z) = \frac{\Gamma(z+n+1)}{z(z+1) \cdots (z+n-1)}.$$

As $z \to -n$, the numerator $\Gamma(z+n+1)$ approaches $\Gamma(1) = 1$, while the denominator approaches $(-n)(-n+1) \cdots (-1)$. Hence

$$\lim_{z \to -n} (z+n)\Gamma(z) = \frac{1}{(-n)(-n+1) \cdots (-1)} = \frac{(-1)^n}{n!}.$$

Since the gamma function has simple poles at $z = -n$ (from the product representation), this limit equals the residue:

$$\operatorname{Res}(\Gamma; -n) = \frac{(-1)^n}{n!}.$$
