---
role: proof
locale: en
of_concept: complementary-module-via-derivative
source_book: gtm028
source_chapter: "IV"
source_section: "11. Different and discriminant"
---

Let $z$ be any element of $K'$. As $\{1, y, \ldots, y^{n-1}\}$ is a basis of $K'$ over $K$, we have $z = g(y)$ where $g(X)$ is a polynomial of degree $\leq n-1$ over $K$, uniquely determined by $z$. Denote by $y_i$ ($i = 1, \ldots, n$) the conjugates of $y$ over $K$.

By the Lagrange interpolation formula:

$$g(X) = \sum_i g(y_i) \frac{F(X)}{F'(y_i)(X-y_i)}.$$

[The right-hand side is a polynomial of degree $\leq n-1$ since $F(X)$ is a multiple of $X-y_i$. Its coefficients are in $K$ by Galois theory, and for $X = y_i$, its value reduces to one term — namely, to the result of substituting $X = y_i$ in $g(y_i) F(X)/F'(y_i)(X-y_i)$. An easy computation shows that $F'(y_i) = \prod_{j \neq i} (y_i - y_j)$, so $F'(y_i)$ is the value of $F(X)/(X-y_i)$ at $X = y_i$. Hence the value of the right-hand side at $X = y_i$ is $g(y_i)$.]

If we define the trace of a polynomial coefficientwise, this may be written as

$$g(X) = T_{K'/K}\!\left(z \frac{F(X)}{F'(y)(X-y)}\right).$$

Now take any element $z'$ in the complementary module $\mathfrak{C}$, and set $z = z' F'(y)$. By the division algorithm, all coefficients of $F(X)/(X-y)$ lie in $R'$. Hence all coefficients of $g(X)$ are in $R$, by the definition of $\mathfrak{C}$ and the choice of $z$. Thus $F'(y) z' = z = g(y)$ lies in $R'$. As this holds for every $z' \in \mathfrak{C}$, we obtain $F'(y) \mathfrak{C} \subset R'$.
