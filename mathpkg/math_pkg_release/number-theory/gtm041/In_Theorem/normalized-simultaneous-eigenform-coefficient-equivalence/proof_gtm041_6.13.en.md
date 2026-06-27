---
role: proof
locale: en
of_concept: normalized-simultaneous-eigenform-coefficient-equivalence
source_book: gtm041
source_chapter: "6"
source_section: "6.13"
---

The equation $T_n f = \lambda(n) f$ is equivalent to the relation

$$\gamma_n(m) = \lambda(n) c(m) \tag{40}$$

obtained by equating coefficients of $x^m$ in the corresponding Fourier expansions. Since $f$ is a cusp form, so is $T_n f$; hence (40) is to hold for all $m \geq 1$ and $n \geq 1$.

Now $\gamma_n(1) = c(n)$ by formula (36), so (40) with $m = 1$ implies

$$\lambda(n) = c(n)$$

provided $c(1) = 1$. Substituting this back into (40) yields

$$\gamma_n(m) = c(n) c(m).$$

On the other hand, formula (34) gives the explicit expression

$$\gamma_n(m) = \sum_{d \mid (n,m)} d^{k-1} \, c\!\left(\frac{mn}{d^2}\right).$$

Thus (40) is equivalent to the multiplicative relation

$$c(m)c(n) = \sum_{d \mid (m,n)} d^{\,k-1} \, c\!\left(\frac{mn}{d^2}\right) \tag{39}$$

for all $m \geq 1$, $n \geq 1$, under the normalization $c(1) = 1$. Therefore $f$ is a normalized simultaneous eigenform if and only if (39) holds for all $m \geq 1$, $n \geq 1$.
