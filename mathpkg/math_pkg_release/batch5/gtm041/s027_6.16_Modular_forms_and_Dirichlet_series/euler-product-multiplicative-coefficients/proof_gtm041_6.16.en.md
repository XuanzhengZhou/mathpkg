---
role: proof
locale: en
of_concept: euler-product-multiplicative-coefficients
source_book: gtm041
source_chapter: "6"
source_section: "6.16"
---

**Proof of Theorem 6.19.** The multiplicative property
$$c(m)c(n) = \sum_{d \mid (m,n)} d^{2k-1} c\!\left(\frac{mn}{d^2}\right)$$
implies in particular for $m = p$ and $n = p^n$ that
$$c(p)c(p^n) = c(p^{n+1}) + p^{2k-1} c(p^{n-1})$$
for each prime $p$ and $n \geq 1$ (with the convention $c(p^0) = 1$). Using this recurrence, one verifies the formal power series identity
$$(1 - c(p)x + p^{2k-1}x^2)\left(1 + \sum_{n=1}^{\infty} c(p^n)x^n\right) = 1$$
for all $|x| < 1$. Indeed, multiplying the series and collecting coefficients of $x^n$ for $n \geq 2$ gives
$$c(p^n) - c(p)c(p^{n-1}) + p^{2k-1}c(p^{n-2}) = 0,$$
which is precisely the recurrence relation. The constant term is $1$, and the coefficient of $x$ is $c(p) - c(p) = 0$. Hence the product equals $1$.

Consequently,
$$1 + \sum_{n=1}^{\infty} c(p^n)x^n = \frac{1}{1 - c(p)x + p^{2k-1}x^2}.$$

Taking $x = p^{-s}$ and using the complete multiplicativity-like property encoded in the original identity, the Dirichlet series factors as
$$\varphi(s) = \sum_{n=1}^{\infty} \frac{c(n)}{n^s} = \prod_p \left(1 + \sum_{n=1}^{\infty} \frac{c(p^n)}{p^{ns}}\right) = \prod_p \frac{1}{1 - c(p)p^{-s} + p^{2k-1-2s}},$$
valid in the half-plane of absolute convergence. $\square$
