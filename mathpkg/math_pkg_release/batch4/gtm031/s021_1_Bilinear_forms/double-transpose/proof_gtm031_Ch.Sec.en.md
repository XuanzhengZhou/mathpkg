---
role: proof
locale: en
of_concept: double-transpose
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

From the characterization of the transpose, we have

$$g_1(x_1, y_2' A') = g_2(x_1 A, y_2')$$

for all $x_1 \in \mathfrak{R}_1$, $y_2' \in \mathfrak{R}_2'$. Similarly, the double transpose $A''$ satisfies

$$g_2(x_1 A'', y_2') = g_1(x_1, y_2' A')$$

for all $x_1 \in \mathfrak{R}_1$, $y_2' \in \mathfrak{R}_2'$. Comparing these relations, we see that $g_2(x_1 A'', y_2') = g_2(x_1 A, y_2')$ for all $x_1, y_2'$. By the non-degeneracy of $g_2$, this implies $x_1 A'' = x_1 A$ for all $x_1$, so $A'' = A$.

Thus if $A'$ is the transpose of $A$, then $A$ is the transpose of $A'$. In particular, if $A \mapsto A'$ and $A' \mapsto A''$ are the transpose correspondences, they are inverses of each other. This establishes that $A \mapsto A'$ is a bijection from $\mathfrak{L}(\mathfrak{R}_1, \mathfrak{R}_2)$ onto $\mathfrak{L}(\mathfrak{R}_2', \mathfrak{R}_1')$. The 1-1 property follows because if $A_1' = A_2'$, then taking the transpose again yields $A_1 = A_1'' = A_2'' = A_2$.
