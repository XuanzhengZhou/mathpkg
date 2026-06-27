---
role: proof
locale: en
of_concept: units-in-polynomial-ring-over-integral-domain
source_book: gtm030
source_chapter: "II"
source_section: "10"
---

Suppose that $f, g \in \mathfrak{A}[x_1, \dots, x_r]$ satisfy $fg = 1$. Using the iterated adjunction identity, view $\mathfrak{A}[x_1, \dots, x_r]$ as $\mathfrak{A}[x_1, \dots, x_{r-1}][x_r]$ and apply the known one-variable result: in a polynomial ring over an integral domain, if the product of two polynomials is a constant, then both factors are constants. Hence $f$ and $g$ lie in $\mathfrak{A}[x_1, \dots, x_{r-1}]$. By induction on $r$, $f$ and $g$ belong to $\mathfrak{A}$ and are units there. The converse is clear: any unit of $\mathfrak{A}$ remains a unit when regarded as a constant polynomial.
