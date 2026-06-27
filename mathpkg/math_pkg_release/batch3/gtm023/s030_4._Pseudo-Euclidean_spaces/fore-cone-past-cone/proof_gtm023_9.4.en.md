---
role: proof
locale: en
of_concept: fore-cone-past-cone
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

The relation $z_1 \sim z_2$ defined by $(z_1, z_2) < 0$ is clearly symmetric (since $(z_1, z_2) = (z_2, z_1)$) and reflexive for time-like vectors (since $(z, z) < 0$).

\textbf{Transitivity:} Consider three time-like vectors $z_1, z_2, z_3$ and assume $(z_1, z_3) < 0$ and $(z_2, z_3) < 0$. Write the decomposition relative to $z_3$ (which is a time-like vector) as
$$z_i = \lambda_i z_3 + y_i \quad (i = 1, 2)$$
with $(z_3, y_i) = 0$. Then $(z_i, z_3) = \lambda_i (z_3, z_3)$, and since $(z_3, z_3) < 0$, the condition $(z_i, z_3) < 0$ implies $\lambda_i = -\frac{(z_i, z_3)}{|(z_3, z_3)|} > 0$ for $i = 1, 2$.

From the decomposition we also have $|y_i|^2 < \lambda_i^2$ for time-like vectors. Now compute
$$(z_1, z_2) = \lambda_1 \lambda_2 (z_3, z_3) + (y_1, y_2).$$
In the subspace $z_3^\perp$ the inner product is positive definite, so by the Schwarz inequality,
$$|(y_1, y_2)| \leq |y_1| |y_2| < |\lambda_1 \lambda_2|.$$
Since $(z_3, z_3) < 0$ and $\lambda_1 \lambda_2 > 0$, the first term $\lambda_1 \lambda_2 (z_3, z_3)$ is negative and its absolute value $|\lambda_1 \lambda_2| \cdot |(z_3, z_3)|$ dominates $|(y_1, y_2)|$. Hence $(z_1, z_2) < 0$, proving transitivity.

Thus $\sim$ is an equivalence relation. Since there are exactly two equivalence classes (because the space of time-like vectors is disconnected into two components related by sign change), we denote them $T^+$ and $T^-$, with $T^- = -T^+$.
