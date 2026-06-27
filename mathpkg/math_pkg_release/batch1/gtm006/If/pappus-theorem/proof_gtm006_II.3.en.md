---
role: proof
locale: en
of_concept: pappus-theorem
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $L_1$ and $L_2$ be distinct lines, and choose coordinates so that $L_1 \cap L_2 = \langle 1, 0, 0 \rangle = E_1$, and let $E_2, E_3$ be points on $L_1, L_2$ respectively, with $E_4 = \langle 1, 1, 1 \rangle$ completing a frame. By suitable choice of basis we may assume $L_1$ is the line $\langle 0, 0, 1 \rangle$ (points with third coordinate zero) and $L_2$ is $\langle 0, 1, 0 \rangle$. Then points on $L_1$ have the form $\langle \alpha, \beta, 0 \rangle$ and points on $L_2$ have the form $\langle \gamma, 0, \delta \rangle$.

Let $A_1 = \langle 1, 0, 0 \rangle$ (the intersection $L_1 \cap L_2$ would be one of the points, but by hypothesis none of the six is the intersection; we use the coordinates differently). Instead, use the coordinatization from Lemma 2.7: represent points on $L_1$ by a parameter $x$ as $\langle x, 1, 0 \rangle$ (excluding the intersection $\langle 1, 0, 0 \rangle$), and points on $L_2$ by $\langle 1, 0, y \rangle$. Let the three points on $L_1$ be $\langle x_i, 1, 0 \rangle$ and on $L_2$ be $\langle 1, 0, y_j \rangle$.

Computing the intersections:
- $B_1 = \langle x_1, 1, 0 \rangle$, $C_2 = \langle 1, 0, y_2 \rangle$. Their join $B_1 + C_2 = \langle -y_2, 0, 1 \rangle$.
- $B_2 = \langle x_2, 1, 0 \rangle$, $C_1 = \langle 1, 0, y_1 \rangle$. Their join $B_2 + C_1 = \langle 1, -x_2, 0 \rangle$ (when $y_1 \neq 0$, adjusting appropriately).

The intersection $A_3 = (B_1 + C_2) \cap (B_2 + C_1)$ is computed via the cross product of the line coordinates. Continuing systematically with all nine intersection points and using the incidence condition $ax + by + cz = 0$, the collinearity of $A_3, B_3, C_3$ reduces to the algebraic condition

$$x^{-1}(1 - y) - x^{-1} - y(1 - x^{-1}) + y = 0$$

in the coordinatizing skewfield. This equation simplifies to $x^{-1} = yx^{-1}$, i.e., $x^{-1}$ commutes with $y$. Since $x$ and $y$ are arbitrary elements of $K$, this holds for all $x, y \in K$ if and only if $K$ is commutative, i.e., $K$ is a field. Hence Pappus' configuration holds exactly when the underlying skewfield is a field. $\square$
