---
role: proof
locale: en
of_concept: quadratic-transformation-blowup
source_book: gtm052
source_chapter: "V"
source_section: "4"
---

Consider the variety $V$ in $\mathbf{P}^2 \times \mathbf{P}^2$ defined by the bihomogeneous equations $x_0 y_0 = x_1 y_1 = x_2 y_2$. Let $p_1: V \to \mathbf{P}^2$ be the first projection. We claim $p_1$ identifies $V$ with $X'$, the blowup of $\mathbf{P}^2$ at $P_1 = (1,0,0)$, $P_2 = (0,1,0)$, $P_3 = (0,0,1)$.

Since blowing up a point depends only on a neighborhood, we work locally on the open set $U \subseteq \mathbf{P}^2$ defined by $x_0 = 1$. Then $U = \operatorname{Spec} A$ with $A = k[x_1, x_2]$, and
$$p_1^{-1}(U) = \operatorname{Proj} A[y_0, y_1, y_2] / (y_0 - x_1 y_1, x_1 y_1 - x_2 y_2).$$
Eliminating $y_0$, we obtain the blowup of $U$ at the origin $(x_1, x_2) = (0,0)$. Thus $p_1$ is the blowup map. The second projection $p_2: V \to \mathbf{P}^2$ gives the identification with the second $\mathbf{P}^2$ blown up at $Q_1, Q_2, Q_3$, and the claimed relationships between exceptional curves and strict transforms follow from the defining equations.
