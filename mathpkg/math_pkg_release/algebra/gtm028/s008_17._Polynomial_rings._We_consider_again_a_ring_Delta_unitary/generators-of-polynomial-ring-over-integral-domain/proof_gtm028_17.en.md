---
role: proof
locale: en
of_concept: generators-of-polynomial-ring-over-integral-domain
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** Suppose $S = R[x] = R[x']$ and $x'$ is transcendental over $R$. Then $x' = f(x)$ for some $f \in R[X]$ of degree $m$, and $x = g(x')$ for some $g \in R[X]$ of degree $n$. Then $x = g(f(x))$, so the polynomial $g(f(X)) - X$ vanishes at $x$. Since $x$ is transcendental over $R$, this polynomial is identically zero. The degree of $g \circ f$ is $mn$, so looking at the degree of $X$ (which is $1$) we must have $mn = 1$. Hence $m = n = 1$.

Write $f(X) = a_0 + a_1 X$ and $g(X) = b_0 + b_1 X$. Then $g(f(X)) = b_0 + b_1(a_0 + a_1 X) = (b_0 + b_1 a_0) + b_1 a_1 X = X$, so $b_1 a_1 = 1$ and $a_1$ is a unit in $R$.

Conversely, if $x' = a_0 + a_1 x$ with $a_1$ a unit, then $x = a_1^{-1}(x' - a_0) \in R[x']$, so $S = R[x']$. Furthermore, if $f(X) \neq 0$ has degree $m$, then $f(x') = f(a_0 + a_1 x)$ has degree $m$ in $x$ (since $a_1$ is a unit, the leading term $c_m a_1^m x^m$ is non-zero), and hence $f(x') \neq 0$. Thus $x'$ is transcendental over $R$.
