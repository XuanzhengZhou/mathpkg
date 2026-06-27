---
role: proof
locale: en
of_concept: discriminant-sign-formula
source_book: gtm007
source_chapter: "V"
source_section: "§1. Preliminaries"
---

Since $d(E) = \pm 1$, its sign is the same as that of the determinant of the Gram matrix over $\mathbf{R}$. By Sylvester\'s law of inertia, the real quadratic form has signature $(r, s)$, so its discriminant (over $\mathbf{R}$) has sign $(-1)^s$. Hence $d(E) = (-1)^s$.

Now $r + s = r(E)$ and $\tau(E) = r - s$, so $s = (r(E) - \tau(E))/2$. Substituting gives $d(E) = (-1)^{(r(E) - \tau(E))/2}$. Note that $r(E) \equiv \tau(E) \pmod{2}$, so the exponent is an integer.
