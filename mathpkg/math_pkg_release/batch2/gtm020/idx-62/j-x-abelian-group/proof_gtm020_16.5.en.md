---
role: proof
locale: en
of_concept: j-x-abelian-group
source_book: gtm020
source_chapter: "16"
source_section: "5"
---

Let $S(\xi) \to B(\xi)$ and $S(\eta) \to B(\eta)$ be associated sphere bundles. The join $S(\xi) * S(\eta)$ is used to construct a representative for $S(\xi \oplus \eta)$. 

Define the join map $S(\xi) \times S(\eta) \times I / \sim$ where $(x, y, \theta)$ is identified appropriately. For $x \in S(\xi)$, $x' \in S(\xi')$, $y \in S(\eta)$, and $0 \leq \theta \leq \pi/2$, define fibre homotopies:

$$k_t(x \cos \theta, y \sin \theta) = (h_t(x) \cos \theta, y \sin \theta)$$
$$k'_t(x' \cos \theta, y \sin \theta) = (h'_t(x') \cos \theta, y \sin \theta)$$

These homotopies satisfy $k_0 = g'g$, $k_1 = 1$, $k'_0 = gg'$, and $k'_1 = 1$, proving that the join construction yields a well-defined group operation on $J(X)$ which is abelian.
