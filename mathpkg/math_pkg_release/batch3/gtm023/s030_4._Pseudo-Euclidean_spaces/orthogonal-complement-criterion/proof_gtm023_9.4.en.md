---
role: proof
locale: en
of_concept: orthogonal-complement-criterion
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

Assume first that the inner product is non-degenerate in $E_1$. Let $x_1$ be a vector of $E_1 \cap E_1^\perp$. Then
$$(x_1, y_1) = 0 \quad \text{for all vectors } y_1 \in E_1,$$
and since the restriction of the inner product to $E_1$ is non-degenerate, we obtain $x_1 = 0$.

Conversely, assume that $E_1 \cap E_1^\perp = \{0\}$. Then it follows that
$$E = E_1 \oplus E_1^\perp$$
since $E_1$ and $E_1^\perp$ have complementary dimension.

Now let $x_1$ be a vector of $E_1$ such that
$$(x_1, y_1) = 0 \quad \text{for all vectors } y_1 \in E_1.$$
Every vector $y$ of $E$ can be written as
$$y = y_1 + y_1^\perp \quad y_1 \in E_1,\ y_1^\perp \in E_1^\perp,$$
whence
$$(x_1, y) = (x_1, y_1) + (x_1, y_1^\perp) = 0 \quad \text{for all vectors } y \in E.$$
Since the inner product on $E$ is non-degenerate, this implies $x_1 = 0$. Thus the restriction of the inner product to $E_1$ is non-degenerate.
