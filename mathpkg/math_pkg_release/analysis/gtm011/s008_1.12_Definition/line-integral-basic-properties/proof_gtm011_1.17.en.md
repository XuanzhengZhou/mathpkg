---
role: proof
locale: en
of_concept: line-integral-basic-properties
source_book: gtm011
source_chapter: "1"
source_section: "1.17"
---

The proof is left as an exercise (Exercise 1.18).

(a) The equality $\int_{\gamma} f = -\int_{-\gamma} f$ follows from the definition of the reversed path $-\gamma(t) = \gamma(-t)$ and the change of variables in the Riemann-Stieltjes sum.

(b) The inequality $\left| \int_{\gamma} f \right| \leq \int_{\gamma} |f| |dz|$ follows from the triangle inequality applied to the approximating Riemann-Stieltjes sums and passing to the limit. The second inequality $\int_{\gamma} |f| |dz| \leq V(\gamma) \sup_{\{\gamma\}} |f|$ follows from bounding each term in the sum by the supremum of $|f|$ on the trace and the definition of total variation $V(\gamma)$.

(c) The translation invariance follows by the change of variable $w = z - c$ in the Riemann-Stieltjes sums defining the line integral.
