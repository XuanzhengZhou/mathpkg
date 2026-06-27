---
role: proof
locale: en
of_concept: different-computation-via-derivative
source_book: gtm028
source_chapter: "V"
source_section: "§11. Different and discriminant"
---

Since $\{1, y, \dots, y^{n-1}\}$ is a basis of $K'$ over $K$, any element $z \in K'$ can be written as $z = g(y)$ for a unique polynomial $g(X)$ of degree $\leq n-1$ over $K$. By Lagrange's interpolation formula:

$$g(X) = \sum_i g(y_i) \frac{F(X)}{F'(y_i)(X - y_i)},$$

where $\{y_i\}$ are the conjugates of $y$ over $K$. In terms of trace, this reads:

$$g(X) = T_{K'/K}\left(z \cdot \frac{F(X)}{F'(y)(X - y)}\right).$$

Now take any $z' \in \mathcal{C}$ (the complementary module) and set $z = z' F'(y)$. Then all coefficients of $g(X)$ are in $R$ by the definition of $\mathcal{C}$ (since $F(X)/(X-y)$ has coefficients in $R'$, and $z'F'(y) \cdot F(X)/(X-y) = zF(X)/(X-y)$ has trace in $R$). But $g(y) = z = z'F'(y)$, so $F'(y)z' \in R'$.

This shows $F'(y)\mathcal{C} \subset R'$, i.e., $\mathcal{C} \subset (F'(y))^{-1}R'$. The reverse inclusion is verified by a similar trace computation, giving $\mathcal{C} = R' \cdot (1/F'(y))$. Hence $\mathfrak{D}_{R'/R} = \mathcal{C}^{-1} = R' \cdot F'(y)$.
