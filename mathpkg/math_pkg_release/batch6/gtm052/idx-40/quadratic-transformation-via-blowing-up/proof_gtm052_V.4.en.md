---
role: proof
locale: en
of_concept: quadratic-transformation-via-blowing-up
source_book: gtm052
source_chapter: "V"
source_section: "4"
---

Consider the variety $V$ in $\mathbf{P}^2 \times \mathbf{P}^2$ defined by the bihomogeneous equations $x_0 y_0 = x_1 y_1 = x_2 y_2$. The first projection $p_1: V \to \mathbf{P}^2$ identifies $V$ with $X'$ (the blow-up of $\mathbf{P}^2$ at $P_1, P_2, P_3$). This is a local question; on the open set $U \subseteq \mathbf{P}^2$ defined by $x_0 = 1$, with $U = \operatorname{Spec} A$ and $A = k[x_1, x_2]$, we have

$$p_1^{-1}(U) = \operatorname{Proj} A[y_0, y_1, y_2] / (y_0 - x_1 y_1, x_1 y_1 - x_2 y_2).$$

Eliminating $y_0$ gives $\operatorname{Proj} A[y_1, y_2] / (x_1 y_1 - x_2 y_2)$, which is exactly the blow-up of $U$ at the ideal $(x_1, x_2)$, i.e., at $P_1$. By symmetry, $V$ is the blow-up at all three points simultaneously.
