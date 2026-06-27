---
role: proof
locale: en
of_concept: normalized-simultaneous-eigenform-multiplicative-property
source_book: gtm041
source_chapter: "6"
source_section: "6.13"
---

The equation $T_n f = \lambda(n)f$ is equivalent to the relation

$$\gamma_n(m) = \lambda(n)c(m)$$

obtained by equating coefficients of $x^m$ in the corresponding Fourier expansions. Since $f$ is a cusp form, so is $T_n f$; hence this relation holds for all $m \geq 1$ and $n \geq 1$.

From (34) we have

$$\gamma_n(m) = \sum_{d \mid (n,m)} d^{k-1} c\left(\frac{mn}{d^2}\right).$$

When $m = 1$, formula (36) gives $\gamma_n(1) = c(n)$. Using this with the eigenfunction relation yields $\lambda(n) = c(n)$ if $c(1) = 1$, and therefore

$$\gamma_n(m) = c(n)c(m).$$

Substituting the expression for $\gamma_n(m)$ from (34), we obtain

$$c(m)c(n) = \sum_{d \mid (m,n)} d^{k-1} c\left(\frac{mn}{d^2}\right)$$

for all $m \geq 1$, $n \geq 1$. Conversely, if the Fourier coefficients satisfy this multiplicative property, then (34) shows that $\gamma_n(m) = c(n)c(m)$, which is equivalent to $T_n f = c(n)f$, so $f$ is a simultaneous eigenform with $\lambda(n) = c(n)$.

Therefore $f$ is a normalized simultaneous eigenform if, and only if, the multiplicative property holds for all $m \geq 1$, $n \geq 1$.
