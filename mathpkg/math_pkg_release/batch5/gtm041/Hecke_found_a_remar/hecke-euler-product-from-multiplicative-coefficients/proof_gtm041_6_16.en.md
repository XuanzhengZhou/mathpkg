---
role: proof
locale: en
of_concept: hecke-euler-product-from-multiplicative-coefficients
source_book: gtm041
source_chapter: "6"
source_section: "6.16"
---

The multiplicative property
$$c(m)c(n) = \sum_{d|(m,n)} d^{2k-1}c\left(\frac{mn}{d^2}\right)$$
implies for each prime $p$ and $n \geq 1$ the relation
$$c(p)c(p^n) = c(p^{n+1}) + p^{2k-1}c(p^{n-1}).$$

Using this recurrence, one verifies the power series identity
$$(1 - c(p)x + p^{2k-1}x^2)\left(1 + \sum_{n=1}^{\infty}c(p^n)x^n\right) = 1$$
for all $|x| < 1$. Indeed, expanding the product:
\begin{align*}
&(1 - c(p)x + p^{2k-1}x^2)\left(1 + \sum_{n=1}^{\infty}c(p^n)x^n\right) \\
&= 1 + c(p)x - c(p)x + \sum_{n=2}^{\infty}\left[c(p^n) - c(p)c(p^{n-1}) + p^{2k-1}c(p^{n-2})\right]x^n = 1.
\end{align*}

Taking $x = p^{-s}$, we obtain
$$\sum_{n=0}^{\infty}c(p^n)p^{-ns} = \frac{1}{1 - c(p)p^{-s} + p^{2k-1-2s}}.$$

Since the coefficients satisfy the multiplicative property, they are multiplicative in the sense that $c(mn) = c(m)c(n)$ when $(m,n)=1$ (taking $d=1$ in the identity). By multiplicative number theory, the Dirichlet series factors as
$$\varphi(s) = \sum_{n=1}^{\infty}\frac{c(n)}{n^s} = \prod_p \sum_{n=0}^{\infty}\frac{c(p^n)}{p^{ns}} = \prod_p \frac{1}{1 - c(p)p^{-s} + p^{2k-1-2s}},$$
whenever the series converges absolutely.
