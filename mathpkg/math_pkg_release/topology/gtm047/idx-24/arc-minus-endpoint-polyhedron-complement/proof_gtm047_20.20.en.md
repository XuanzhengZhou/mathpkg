---
role: proof
locale: en
of_concept: arc-minus-endpoint-polyhedron-complement
source_book: gtm047
source_chapter: "20"
source_section: "20"
---

Let $C^3 = \bigcup_{i=1}^{\infty} C_i^3$, where for each $i$, $C_i^3$ is a 3-cell, $C_i^3 \cap C_{i+1}^3$ is a 2-cell equal to $\operatorname{Bd} C_i^3 \cap \operatorname{Bd} C_{i+1}^3$, and for $i > 1$, $C_i^3 \cap A$ is unknotted in $C_i^3$. We choose the sets $C_i^3$ so that $\lim \delta C_i^3 = 0$; this makes $C^3$ a 3-cell.

Let $D^3$ and $P_0 P_1$ be as in Theorem 1; let

$$D_1^3 = \{ P = (x, y, z) \mid P \in D^3 \text{ and } 1 \leqslant z \leqslant 2 \},$$

and for $i > 1$ let

$$D_i^3 = \{ P = (x, y, z) \mid P \in D^3 \text{ and } 1 / (i+1) \leqslant z \leqslant 1 / i \}.$$

Then there is a homeomorphism

$$h: C^3 \leftrightarrow D^3,$$

such that for each $i$,

$$h(C_i^3) = D_i^3, \quad h(C_i^3 \cap A) = D_i^3 \cap P_0 P_1,$$

and $h(Q) = P_0$. (The construction is straightforward.)

Now $h^{-1} f h$ is a mapping $C^3 \rightarrow C^3$, $A \rightarrow Q$, giving a homeomorphism $g: C^3 - A \leftrightarrow C^3 - \{Q\}$ which is the identity at each point of $\operatorname{Bd} C^3 - \{Q\}$. We define $g$ to be the identity at $Q$ and at each point of $\mathbf{R}^3 - C^3$. Now $g$ is a homeomorphism $\mathbf{R}^3 - A \leftrightarrow \mathbf{R}^3 - \{Q\}$.
