---
role: proof
locale: en
of_concept: inverse-of-unit
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

By definition, a unit is a cyclotomic integer $f(\alpha)$ with $Nf(\alpha) = 1$. Using the definition of the norm,
$$Nf(\alpha) = f(\alpha) \cdot f(\alpha^2) \cdot f(\alpha^3) \cdots f(\alpha^{\lambda-1}) = 1.$$
Since all factors are complex numbers and multiplication is commutative, we may rearrange to obtain
$$f(\alpha) \cdot \bigl(f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1})\bigr) = 1.$$
Thus $f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1})$ is the multiplicative inverse of $f(\alpha)$. This product is itself a cyclotomic integer because each conjugate $f(\alpha^j)$ is a cyclotomic integer and the set of cyclotomic integers is closed under multiplication.
