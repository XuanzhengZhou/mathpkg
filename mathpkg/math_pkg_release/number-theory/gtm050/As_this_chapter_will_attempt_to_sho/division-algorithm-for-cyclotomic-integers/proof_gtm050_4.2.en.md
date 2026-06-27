---
role: proof
locale: en
of_concept: division-algorithm-for-cyclotomic-integers
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

If there exists $g(\alpha)$ such that $f(\alpha)g(\alpha) = h(\alpha)$, then multiplying both sides by $f(\alpha^2)f(\alpha^3) \cdots f(\alpha^{\lambda-1})$ yields
$$h(\alpha) \cdot f(\alpha^2) f(\alpha^3) \cdots f(\alpha^{\lambda-1}) = g(\alpha) \cdot f(\alpha) f(\alpha^2) \cdots f(\alpha^{\lambda-1}) = g(\alpha) \cdot Nf(\alpha).$$

Thus $h(\alpha) \cdot f(\alpha^2) f(\alpha^3) \cdots f(\alpha^{\lambda-1})$ must be divisible by the ordinary integer $Nf(\alpha)$. This is a necessary condition.

Conversely, suppose this condition holds. By the criterion for divisibility by an integer, the coefficients of the product $h(\alpha) \cdot f(\alpha^2) f(\alpha^3) \cdots f(\alpha^{\lambda-1})$ are all congruent to one another modulo $Nf(\alpha)$, hence each is divisible by $Nf(\alpha)$ after an appropriate adjustment using $1+\alpha+\cdots+\alpha^{\lambda-1}=0$. Dividing through by $Nf(\alpha)$ yields a cyclotomic integer $g(\alpha)$ satisfying $g(\alpha) \cdot Nf(\alpha) = h(\alpha) \cdot f(\alpha^2) f(\alpha^3) \cdots f(\alpha^{\lambda-1})$. Since $f(\alpha) \neq 0$, we can divide by $f(\alpha)$ in the complex numbers to obtain $f(\alpha)g(\alpha) = h(\alpha)$, and the resulting $g(\alpha)$ will be a cyclotomic integer by the division step. Thus the condition is both necessary and sufficient.
