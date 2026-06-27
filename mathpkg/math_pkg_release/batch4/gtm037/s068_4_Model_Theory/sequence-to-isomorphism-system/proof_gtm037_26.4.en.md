---
role: proof
locale: en
of_concept: sequence-to-isomorphism-system
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

Given an $(n+1)$-sequence $\langle I_k : k \leq n+1 \rangle$ for $\mathfrak{A}$ and $\mathfrak{B}$, we construct an $(n+1)$-system of partial isomorphisms $\langle J_k : k \leq n+1 \rangle$ as follows. For each $k \leq n+1$, let $J_k$ consist of all finite partial functions $f : A \to B$ such that for some $(x_0,\ldots,x_{k-1}) \in {}^k A$ and $(y_0,\ldots,y_{k-1}) \in {}^k B$ with $x I_k y$, we have $f(x_i) = y_i$ for all $i < k$. Condition (4) of Definition 26.6 ensures that each $f \in J_k$ is a partial isomorphism. The back-and-forth condition (3) of Definition 26.6 translates directly into the extension property (iii) of Definition 26.9. The nesting condition (ii) follows from the construction, and nonemptiness (i) follows from the existence of at least one $I_k$-related pair of tuples.
