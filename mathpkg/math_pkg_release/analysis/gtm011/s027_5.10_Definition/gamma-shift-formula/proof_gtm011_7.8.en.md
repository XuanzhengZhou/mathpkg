---
role: proof
locale: en
of_concept: gamma-shift-formula
source_book: gtm011
source_chapter: "7"
source_section: "7.8"
---

Apply the functional equation (7.7) repeatedly. For $n = 0$ the formula reduces to $\Gamma(z) = \Gamma(z)$. Assume the formula holds for $n$. Then

$$\Gamma(z + n + 1) = \Gamma((z+n) + 1) = (z+n) \Gamma(z+n)$$

by the functional equation. By the induction hypothesis, $\Gamma(z+n) = z(z+1) \cdots (z+n-1)\Gamma(z)$, so

$$\Gamma(z+n+1) = (z+n) \cdot z(z+1) \cdots (z+n-1) \Gamma(z) = z(z+1) \cdots (z+n) \Gamma(z).$$

Thus the formula holds for all non-negative integers $n$ by induction.
