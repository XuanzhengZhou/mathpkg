---
role: proof
locale: en
of_concept: order-complete-vector-lattice-is-archimedean
source_book: gtm003
source_chapter: "V"
source_section: "Exercises"
---

Suppose $L$ is order complete and $x \leq n^{-1}y$ for all $n \in \mathbf{N}$ and some $y \in L$. Consider the set $A = \{n^{-1}y : n \in \mathbf{N}\}$. Then $\inf A$ exists in $L$ by order completeness. Since $x$ is a lower bound of $A$, we have $x \leq \inf A$. But $\inf A = 0$ (since $n^{-1}y \downarrow 0$ in any vector lattice by the Archimedean property of $\mathbf{R}$ acting via scalars). Thus $x \leq 0$, proving the order is Archimedean.
