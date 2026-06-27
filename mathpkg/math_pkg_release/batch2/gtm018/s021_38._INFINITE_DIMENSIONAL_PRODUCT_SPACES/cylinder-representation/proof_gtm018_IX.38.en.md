---
role: proof
locale: en
of_concept: cylinder-representation
source_book: gtm018
source_chapter: "IX"
source_section: "38. Infinite Dimensional Product Spaces"
---

Let $J = \{1, \cdots, n\}$ and suppose $E$ is a $J$-cylinder. Define $A \subset X_1 \times \cdots \times X_n$ by

$$A = \left\{(x_1, \cdots, x_n) : (x_1, \cdots, x_n, \bar{x}_{n+1}, \bar{x}_{n+2}, \cdots) \in E\right\},$$

where $(\bar{x}_{n+1}, \bar{x}_{n+2}, \cdots)$ is any fixed element of $X^{(n)}$. The definition of $A$ is independent of the choice of the tail coordinates because $E$ is a $J$-cylinder: if $(x_1, \cdots, x_n, \bar{x}_{n+1}, \bar{x}_{n+2}, \cdots) \in E$, then for any other $(y_{n+1}, y_{n+2}, \cdots) \in X^{(n)}$ we have $(x_1, \cdots, x_n, y_{n+1}, y_{n+2}, \cdots) \equiv (x_1, \cdots, x_n, \bar{x}_{n+1}, \bar{x}_{n+2}, \cdots) \ (J)$, and since $E$ is a $J$-cylinder it follows that $(x_1, \cdots, x_n, y_{n+1}, y_{n+2}, \cdots) \in E$ as well. Thus $E = A \times X^{(n)}$.

Conversely, any set of the form $A \times X^{(n)}$ with $A \subset X_1 \times \cdots \times X_n$ is clearly a $J$-cylinder, since membership depends only on the first $n$ coordinates.

If $E$ is measurable, i.e. $E \in \prod_{i=1}^{\infty} \mathbf{S}_i$, then by 34.A the section $A = E(\bar{x}_{n+1}, \bar{x}_{n+2}, \cdots)$ belongs to $\mathbf{S}_1 \times \cdots \times \mathbf{S}_n$. Conversely, if $A \in \mathbf{S}_1 \times \cdots \times \mathbf{S}_n$, then $E = A \times X^{(n)}$ is a measurable rectangle in the generating class of $\prod_{i=1}^{\infty} \mathbf{S}_i$, hence measurable.
