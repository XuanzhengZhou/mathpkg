---
role: proof
locale: en
of_concept: closure-of-sums-of-two-squares-under-division
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

Suppose $p^2 + q^2$ divides $a^2 + b^2$. From the Brahmagupta-Fibonacci identity,
$$(a^2 + b^2)(p^2 + q^2) = (ap - bq)^2 + (aq + bp)^2.$$

Since $p^2 + q^2$ divides the left-hand side $(a^2+b^2)(p^2+q^2)$, it must divide the right-hand side. Therefore $p^2+q^2$ divides $(ap-bq)^2 + (aq+bp)^2$. Moreover, $p^2+q^2$ must divide either $pb+aq$ or $pb-aq$.

**Case 1:** $p^2+q^2$ divides $pb+aq$. Then from the identity it follows that $p^2+q^2$ must also divide $(ap-bq)^2$. Hence the equation can be divided by $(p^2+q^2)^2$, yielding
$$\frac{a^2+b^2}{p^2+q^2} = \left(\frac{ap-bq}{p^2+q^2}\right)^2 + \left(\frac{aq+bp}{p^2+q^2}\right)^2.$$
Setting $u = (ap-bq)/(p^2+q^2)$ and $v = (aq+bp)/(p^2+q^2)$ gives the quotient as $u^2+v^2$.

**Case 2:** $p^2+q^2$ divides $pb-aq$. Using the symmetric form of the identity,
$$(a^2+b^2)(q^2+p^2) = (aq-bp)^2 + (ap+bq)^2,$$
and the same argument applies with $u = (aq-bp)/(p^2+q^2)$ and $v = (ap+bq)/(p^2+q^2)$.

In either case, the quotient $(a^2+b^2)/(p^2+q^2)$ is expressed as a sum of two squares.
