---
role: proof
locale: en
of_concept: dimension-inequality-regular-local-ring
source_book: gtm052
source_chapter: "I"
source_section: "5"
---

See Atiyah–Macdonald [1, Cor. 11.15, p. 121] or Matsumura [2, p. 78].

The proof proceeds by induction on $\dim A$. Let $d = \dim A$. Then by the definition of Krull dimension, there exists a chain of prime ideals $\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_d = \mathfrak{m}$. By Krull's principal ideal theorem, we can choose elements $x_1, \ldots, x_d \in \mathfrak{m}$ such that for each $i$, the ideal $(x_1, \ldots, x_i)$ has height $i$. The images of $x_1, \ldots, x_d$ in $\mathfrak{m}/\mathfrak{m}^2$ are then linearly independent over $k$, which yields the inequality $\dim_k \mathfrak{m}/\mathfrak{m}^2 \geq d = \dim A$.
