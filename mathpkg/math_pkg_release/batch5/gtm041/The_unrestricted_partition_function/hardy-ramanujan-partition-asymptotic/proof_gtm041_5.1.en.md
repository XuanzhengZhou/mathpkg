---
role: proof
locale: en
of_concept: hardy-ramanujan-partition-asymptotic
source_book: gtm041
source_chapter: "5"
source_section: "5.1"
---

The original proof by Hardy and Ramanujan [13] uses the circle method. Starting from Euler's generating function, one writes

$$p(n) = \frac{1}{2\pi i} \int_C \frac{F(x)}{x^{n+1}} \, dx,$$

where $C$ is a positively oriented contour enclosing the origin inside the unit circle. The circle method divides $C$ into arcs near roots of unity and approximates $F(x)$ on each arc using the Dedekind eta function transformation formula. The contribution from the singularity at $x = 1$ yields the dominant term $e^{K\sqrt{n}}/(4n\sqrt{3})$. The full circle method proof occupies most of Chapter 5 in GTM041, culminating in Rademacher's convergent series (Theorem 5.10).
