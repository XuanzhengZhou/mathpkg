---
role: proof
locale: en
of_concept: characterization-of-transpose
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

Let $y_2' \in \mathfrak{R}_2'$. Then $R_2(y_2')$ is the linear function $g_2(\cdot, y_2')$ on $\mathfrak{R}_2$. Applying the usual transpose $A^*: \mathfrak{R}_2^* \to \mathfrak{R}_1^*$, we obtain the linear function $f_1 = y_2' R_2 A^*$ on $\mathfrak{R}_1$ satisfying

$$f_1(x_1) = (R_2(y_2'))(x_1 A) = g_2(x_1 A, y_2')$$

for all $x_1 \in \mathfrak{R}_1$. Now applying $R_1^{-1}$ maps this linear function back to a vector in $\mathfrak{R}_1'$. Since $R_1$ is an isomorphism, there exists a unique vector $y_1' \in \mathfrak{R}_1'$ such that $R_1(y_1') = f_1$, i.e., $g_1(\cdot, y_1') = f_1(\cdot)$. But $y_1' = y_2' A'$ by definition of $A' = R_2 A^* R_1^{-1}$. Therefore

$$g_1(x_1, y_2' A') = f_1(x_1) = g_2(x_1 A, y_2')$$

for all $x_1 \in \mathfrak{R}_1$ and $y_2' \in \mathfrak{R}_2'$. This relation uniquely determines $A'$, since if two linear transformations $A_1', A_2': \mathfrak{R}_2' \to \mathfrak{R}_1'$ both satisfy the relation, then $g_1(x_1, y_2'(A_1' - A_2')) = 0$ for all $x_1, y_2'$, which by non-degeneracy of $g_1$ implies $y_2'(A_1' - A_2') = 0$ for all $y_2'$, so $A_1' = A_2'$.
