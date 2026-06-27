---
role: proof
locale: en
of_concept: theorem-2-1-collaring-theorem
source_book: gtm033
source_chapter: "6"
source_section: "2"
---

# Proof of Collaring Theorem via Vector Fields

Using charts covering $\partial M$ and a partition of unity, one finds a $C^\infty$ vector field $X$ on a neighborhood $U \subset M$ of $\partial M$ which is nowhere tangent to $\partial M$ and which points into $M$ (in local coordinates).

Let $W \subset \partial M \times [0, \infty)$ be a neighborhood of $\partial M \times 0$ on which the flow $\eta$ of the vector field is defined. There is a $C^\infty$ embedding

$$h: \partial M \times [0, \infty) \rightarrow W$$

which leaves $\partial M \times 0$ pointwise fixed.

The required map $F$ is the composition

$$F: \partial M \times [0, \infty) \xrightarrow{h} W \xrightarrow{\eta} M.$$

Since $h$ is an embedding and $\eta$ is the flow of a $C^\infty$ vector field (hence a $C^\infty$ map), the composition $F$ is a $C^\infty$ embedding. By construction, $F(x, 0) = \eta(h(x,0)) = \eta(x,0) = x$ for all $x \in \partial M$, since $h$ fixes $\partial M \times 0$ pointwise and the flow satisfies $\eta_0 = \text{id}$.
