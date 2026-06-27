---
role: proof
locale: en
of_concept: schwarz-inequality
source_book: gtm049
source_chapter: "VI"
source_section: "6.1"
---

The result is clear when $a = 0$. So assume $\|a\| \neq 0$. We have

$$\sigma(xa - b, xa - b) = \|a\|^2 x^2 - 2\sigma(a, b)x + \|b\|^2,$$

and since the left-hand side is never negative (by positive definiteness of $\sigma$), the substitution $x = \sigma(a, b)/\|a\|^2$ gives

$$\sigma(a, b)^2 \leq \|a\|^2 \|b\|^2.$$

Thus $|\sigma(a, b)| \leq \|a\| \|b\|$.

Further, equality holds if, and only if, $\sigma(xa - b, xa - b) = 0$, which by positive definiteness means $xa - b = 0$, i.e., $b = xa$. Hence equality holds precisely when $a$ and $b$ are linearly dependent.
