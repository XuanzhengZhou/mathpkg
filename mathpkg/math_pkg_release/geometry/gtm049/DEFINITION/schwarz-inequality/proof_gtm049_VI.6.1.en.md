---
role: proof
locale: en
of_concept: schwarz-inequality
source_book: gtm049
source_chapter: "VI"
source_section: "6.1"
---

The result is clear when $a = 0$. Assume $\|a\| \neq 0$. Consider the quadratic expression in $x$:
$$\sigma(xa - b, xa - b) = \|a\|^2 x^2 - 2\sigma(a, b)x + \|b\|^2.$$
Since the left-hand side is never negative (positive definiteness of $\sigma$), the discriminant of this quadratic must be non-positive:
$$4\sigma(a, b)^2 - 4\|a\|^2 \|b\|^2 \leq 0,$$
which yields $\sigma(a, b)^2 \leq \|a\|^2 \|b\|^2$. Equality holds if and only if the quadratic has a double root, i.e., $\sigma(xa - b, xa - b) = 0$ for some $x$, which by positive definiteness means $b = xa$.
