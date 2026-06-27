---
role: proof
locale: en
of_concept: h-product-lemma
source_book: gtm050
source_chapter: "4"
source_section: "4.3"
---

The lemma follows from the norm formula. For any integer $k$,

$$N(\alpha - k) = \prod_{i=1}^{\lambda-1} (\alpha^i - k) = \frac{k^\lambda - 1}{k - 1}.$$

This is derived from the factorization

$$(X - \alpha)(X - \alpha^2) \cdots (X - \alpha^{\lambda-1}) = X^{\lambda-1} + X^{\lambda-2} + \cdots + 1 = \frac{X^\lambda - 1}{X - 1}.$$

For $k = m^j$ where $j = 1, 2, \ldots, \lambda-1$, we have $k^\lambda \equiv 1 \pmod{p}$ (since $m^\lambda \equiv 1$), and $k \not\equiv 1 \pmod{p}$ (since the $\lambda$ solutions are distinct). Therefore

$$N(\alpha - m^j) = \frac{(m^j)^\lambda - 1}{m^j - 1} \equiv 0 \pmod{p}.$$

Since $N(\alpha - m^j) = \prod_{i=1}^{\lambda-1} (\alpha^i - m^j)$ and the norm is divisible by $p$, and $h(\alpha)$ is related to these factors (each conjugate $h(\alpha^i)$ divides the corresponding conjugate of the binomial), we obtain

$$h(m)h(m^2) \cdots h(m^{\lambda-1}) \equiv 0 \pmod{p}.$$
