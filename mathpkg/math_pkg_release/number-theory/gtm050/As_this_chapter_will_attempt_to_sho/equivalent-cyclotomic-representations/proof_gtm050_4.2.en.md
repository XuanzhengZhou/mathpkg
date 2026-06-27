---
role: proof
locale: en
of_concept: equivalent-cyclotomic-representations
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

If $f(\alpha)$ and $g(\alpha)$ differ by $c \cdot (1 + \alpha + \cdots + \alpha^{\lambda-1})$ for some integer $c$, then by the relation $1 + \alpha + \cdots + \alpha^{\lambda-1} = 0$ (proved earlier), they are equal as cyclotomic integers.

Conversely, suppose $f(\alpha) = g(\alpha)$ as cyclotomic integers. Let $h(X) = f(X) - g(X)$ be the polynomial with integer coefficients. Since both $f$ and $g$ have degree at most $\lambda-1$, so does $h$. The equality $f(\alpha) = g(\alpha)$ means $h(\alpha) = 0$ in the complex numbers. Consider the polynomial $X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1$, which is the minimal polynomial of $\alpha$ over the rational numbers. Since $h(X)$ has rational (indeed integer) coefficients, degree less than $\lambda$, and vanishes at $X = \alpha$, it must be divisible by the minimal polynomial. Hence $h(X) = c \cdot (X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1)$ for some rational $c$. Comparing leading coefficients and using that $h$ has integer coefficients, $c$ must be an integer.
