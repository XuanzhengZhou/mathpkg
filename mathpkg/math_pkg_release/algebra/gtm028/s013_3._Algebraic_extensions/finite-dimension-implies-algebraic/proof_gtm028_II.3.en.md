---
role: proof
locale: en
of_concept: finite-dimension-implies-algebraic
source_book: gtm028
source_chapter: "II"
source_section: "3. Algebraic extensions"
---

Let $[K:k] = n < \infty$. For any $x \in K$, consider the $n+1$ elements
$$1, x, x^2, \ldots, x^n$$
in the $n$-dimensional vector space $K$ over $k$. These $n+1$ elements are linearly dependent over $k$. Hence there exist $c_0, c_1, \ldots, c_n \in k$, not all zero, such that
$$c_0 + c_1 x + c_2 x^2 + \cdots + c_n x^n = 0.$$
Thus $x$ satisfies a non-zero polynomial equation of degree $\leq n$ with coefficients in $k$, so $x$ is algebraic over $k$. Since $x$ was arbitrary, $K$ is an algebraic extension of $k$. Moreover, the minimal polynomial of $x$ divides the polynomial $\sum_{i=0}^n c_i X^i$, so its degree is $\leq n$.
