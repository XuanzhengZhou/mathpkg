---
role: proof
locale: en
of_concept: uniqueness-of-power-series-coefficients
source_book: gtm012
source_chapter: "4"
source_section: "4"
---

# Proof of Uniqueness of Power Series Coefficients

**Statement.** Let $f$ be defined by a power series

$$f(x) = \sum_{n=0}^{\infty} a_n (x - x_0)^n$$

with radius of convergence $R > 0$. Then the coefficients $a_n$ are uniquely determined by the function $f$. Specifically,

$$a_k = \frac{f^{(k)}(x_0)}{k!}, \quad k = 0, 1, 2, \ldots$$

**Proof.** By Corollary 4.5, the function $f$ is infinitely differentiable on $|x - x_0| < R$, and the $k$-th derivative is given by

$$f^{(k)}(x) = \sum_{n=k}^{\infty} n(n-1)(n-2) \cdots (n-k+1) a_n (x - x_0)^{n-k}, \quad |x - x_0| < R. \tag{4.11}$$

Substituting $x = x_0$ into (4.11), every term of the series with index $n > k$ contains a factor $(x_0 - x_0)^{n-k} = 0$ and therefore vanishes. The only surviving term is the one with $n = k$, which gives

$$f^{(k)}(x_0) = k(k-1)(k-2) \cdots 1 \cdot a_k = k! \, a_k.$$

Solving for $a_k$ yields

$$a_k = \frac{f^{(k)}(x_0)}{k!}. \tag{4.12}$$

Since the right-hand side depends only on the function $f$ (not on the original choice of coefficients), the coefficients $\{a_n\}$ are uniquely determined by $f$, provided the radius of convergence is positive. $\square$
