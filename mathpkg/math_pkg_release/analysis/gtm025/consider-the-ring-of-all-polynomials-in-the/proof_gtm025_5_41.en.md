---
role: proof
locale: en
of_concept: "consider-the-ring-of-all-polynomials-in-the"
source_book: gtm025
source_chapter: "Set Theory and Algebra"
source_section: "5.41"
---

It is obvious that $J$ is an ideal in $R[t]$. Exactly as in the proof of (5.22), we see that the definitions of addition and multiplication in $R[t]/J$ are unambiguous, and that $R[t]/J$ is a commutative ring with zero $J$ and unit $1 + J$.

To describe $R[t]/J$ more closely, suppose that $(a + bt) + J = (a' + b't) + J$. Then $[(a + bt) - (a' + b't)] \in J$, and so $(a - a') + (b - b') t = (t^2 + 1) p(t)$, for some $p(t) \in R[t]$. Comparing the degrees of these two polynomials, we see that $p(t) = 0$ and that $a = a', b = b'

have $a^2 + b^2 > 0$, and so $\frac{1}{a^2 + b^2}$ exists in $R$. It is clear that

$$[(a + bt) + J] \left[ \left( \frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2} t \right) + J \right] = 1 + J.$$

This shows that every nonzero element of $R[t]/J$ has a multiplicative inverse, and so $R[t]/J$ is a field. $\square$

(5.42) Definitions. The field $R[t]/J$ is called the complex number field or the field of complex numbers and is denoted by the symbol $K$. We write the coset $(a + bt) + J$ as $a + bi$; $a + bi$ is called a complex number. The number $a$ is called the real part of $a + bi$ and is written $\Re(a + bi)$. The number $b$ is called the imaginary part of $a + bi$ and is written $\Im(a + bi)$. The symbols $z = x + iy$, $w = u + iv$, $\sigma + i\tau$, $\alpha + \beta i$, etc., will be used to denote complex numbers. The complex number $a + 0i$ will be written as $a$ alone and $0 + bi$ as $bi$ alone. For $z = x + iy \in K$, the absolute value of $z$ is defined as $(x^2 + y^2)^{\frac{1}{2}}$ [the nonnegative square root!] and is written $|z|$. The complex conjugate of $z$ [or simply conjugate] is defined as $x - iy$ and is written $\bar{z}$.
