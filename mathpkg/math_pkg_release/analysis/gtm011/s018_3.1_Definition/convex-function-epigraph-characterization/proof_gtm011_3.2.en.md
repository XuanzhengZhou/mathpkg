---
role: proof
locale: en
of_concept: convex-function-epigraph-characterization
source_book: gtm011
source_chapter: "3"
source_section: "3.2"
---

Suppose $f: [a, b] \to \mathbb{R}$ is a convex function and let $(x_1, y_1)$ and $(x_2, y_2)$ be points in $A$. If $0 \leq t \leq 1$ then, by the definition of convex function,

$$f(tx_2 + (1-t)x_1) \leq tf(x_2) + (1-t)f(x_1) \leq ty_2 + (1-t)y_1.$$

Thus

$$t(x_2, y_2) + (1-t)(x_1, y_1) = (tx_2 + (1-t)x_1, ty_2 + (1-t)y_1)$$

lies in $A$, so $A$ is convex.

Conversely, suppose $A$ is a convex set. Let $x_1, x_2 \in [a, b]$ and $0 \leq t \leq 1$. Then $(x_1, f(x_1))$ and $(x_2, f(x_2))$ belong to $A$. Since $A$ is convex, the point

$$t(x_2, f(x_2)) + (1-t)(x_1, f(x_1)) = (tx_2 + (1-t)x_1, tf(x_2) + (1-t)f(x_1))$$

is in $A$. By definition of $A$, this means

$$f(tx_2 + (1-t)x_1) \leq tf(x_2) + (1-t)f(x_1).$$

Hence $f$ is convex.
