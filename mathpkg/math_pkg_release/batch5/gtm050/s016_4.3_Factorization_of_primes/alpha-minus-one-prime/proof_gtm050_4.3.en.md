---
role: proof
locale: en
of_concept: alpha-minus-one-prime
source_book: gtm050
source_chapter: "4"
source_section: "4.3"
---

The first corollary follows from the main theorem because $N(\alpha - 1) = \lambda$ is prime. However, one can also prove directly that $\alpha - 1$ is prime:

Since $\alpha - 1$ divides $N(\alpha - 1) = \lambda$ but does not divide $1$, an integer is divisible by $\alpha - 1$ only if it is divisible by $\lambda$. Moreover, $\alpha \equiv 1 \pmod{\alpha - 1}$.

If $\alpha - 1$ divides $f(\alpha)g(\alpha)$, then $f(\alpha)g(\alpha) \equiv 0 \pmod{\alpha - 1}$. Using $\alpha \equiv 1 \pmod{\alpha-1}$, this gives $f(1)g(1) \equiv 0 \pmod{\alpha - 1}$. Since $f(1)g(1)$ is an integer, $f(1)g(1) \equiv 0 \pmod{\lambda}$. Because $\lambda$ is a rational prime, either $f(1) \equiv 0 \pmod{\lambda}$ or $g(1) \equiv 0 \pmod{\lambda}$, hence $f(1) \equiv 0 \pmod{\alpha - 1}$ or $g(1) \equiv 0 \pmod{\alpha - 1}$. Using $\alpha \equiv 1$ again, this gives $f(\alpha) \equiv 0 \pmod{\alpha-1}$ or $g(\alpha) \equiv 0 \pmod{\alpha-1}$, so $\alpha-1$ divides $f(\alpha)$ or $g(\alpha)$. Therefore $\alpha-1$ is prime.

If $h(\alpha)$ is any cyclotomic integer with $Nh(\alpha) = \lambda$, then because $\alpha-1$ divides $Nh(\alpha)$ and is prime, $\alpha-1$ divides one of the conjugates of $h(\alpha)$. Consequently, $h(\alpha)$ is a unit multiple of a conjugate of $\alpha-1$, which is itself a unit multiple of $\alpha-1$.
