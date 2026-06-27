---
role: proof
locale: en
of_concept: norm-and-trace-via-all-conjugates
source_book: gtm028
source_chapter: "I"
source_section: "11"
---
Let $\tau_1, \dots, \tau_n$ be the $n$ distinct $k$-isomorphisms of $K$ into a normal closure $K^\star$. Set $x_i = x^{\tau_i}$.

From §10, formula (10), if $K = k(x)$ then the field polynomial is the minimal polynomial and it factors as $\prod (X - x_i)$. In the general case, let $g(X)$ be the minimal polynomial of $x$ over $k$ and let $\nu = [K:k(x)]$ be the number of isomorphisms fixing $x$. Then $x$ has $m = n/\nu$ distinct conjugates, and by the tower formula for field polynomials,
$$f(X) = [g(X)]^\nu.$$

If $g(X) = \prod_{j=1}^{m} (X - y_j)$ where $y_j$ are the distinct conjugates of $x$, then each $y_j$ appears $\nu$ times among the $x_i$. Hence
$$f(X) = \prod_{j=1}^{m} (X - y_j)^\nu = \prod_{i=1}^{n} (X - x_i).$$

Since $f(X) = \det(XE - A) = X^n - T(x)X^{n-1} + \cdots + (-1)^n N(x)$, comparing with $\prod (X - x_i) = X^n - (\sum x_i)X^{n-1} + \cdots + (-1)^n \prod x_i$ gives
$$T_{K/k}(x) = \sum_{i=1}^{n} x_i, \qquad N_{K/k}(x) = \prod_{i=1}^{n} x_i.$$
