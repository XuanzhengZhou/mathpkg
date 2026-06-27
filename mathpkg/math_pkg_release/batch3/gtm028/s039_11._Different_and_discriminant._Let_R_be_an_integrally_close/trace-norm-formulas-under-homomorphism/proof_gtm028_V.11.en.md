---
role: proof
locale: en
of_concept: trace-norm-formulas-under-homomorphism
source_book: gtm028
source_chapter: "V"
source_section: "§11. Different and discriminant"
---

Let $f(X)$ be the field polynomial of $x$ relative to $K$: $f(X) = X^n + a_1 X^{n-1} + \cdots + a_n$ where $n = [K':K]$. Since $x$ is integral over $R$ and $R$ is integrally closed, the coefficients of the minimal polynomial of $x$ over $K$ belong to $R$, and as $f(X)$ is a power of this minimal polynomial, the $a_i$ also belong to $R$.

Set $\bar{a}_i = h(a_i)$ and $\bar{f}(X) = X^n + \bar{a}_1 X^{n-1} + \cdots + \bar{a}_n$. Then $T_{K'/K}(x) = -a_1$ and $N_{K'/K}(x) = (-1)^n a_n$, so:

$$h(T_{K'/K}(x)) = -\bar{a}_1, \quad h(N_{K'/K}(x)) = (-1)^n \bar{a}_n.$$

Consider the factorization $\bar{f}(X) = \prod_i [\bar{f}_i(X)]^{e_i}$ where $\bar{f}_i(X)$ are the field polynomials of $h_i(x)$. The vector space $R'/R'\mathfrak{p}$ decomposes as a direct sum of invariant subspaces under the multiplication-by-$x$ map. Computing characteristic polynomials in this decomposition yields the claimed formulas for the trace (sum of roots) and norm (product of roots with multiplicities).
