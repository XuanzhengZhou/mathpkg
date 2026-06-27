---
role: proof
locale: en
of_concept: determinant-expansion-identity
source_book: gtm023
source_chapter: "IV"
source_section: "§1. Determinant functions"
---

If the vectors $x_1, \ldots, x_n$ are linearly dependent, then by Proposition I (iii), $\Delta(x_1, \ldots, x_n) = 0$. A direct computation shows that the left-hand side also vanishes: each term $\Delta(x, x_1, \ldots, \hat{x}_j, \ldots, x_n)$ involves $n$ vectors containing $\{x_1,\ldots,x_n\} \setminus \{x_j\}$ together with $x$. Since $x_1,\ldots,x_n$ are linearly dependent, the collection of vectors in each term has at most $n$ vectors spanning a subspace of dimension at most $n-1$, hence is linearly dependent, making each determinant zero by Proposition I (iii). Thus the identity holds trivially in this case.

Now assume $x_1, \ldots, x_n$ are linearly independent, hence form a basis of $E$. Write $x = \sum_{k=1}^n \alpha_k x_k$. The right-hand side is $\Delta(x_1,\ldots,x_n) \cdot \sum_k \alpha_k x_k$. For the left-hand side, substitute the expansion of $x$:
\begin{align*}
\sum_{j=1}^n (-1)^{j-1} \Delta(x, x_1, \ldots, \hat{x}_j, \ldots, x_n) \cdot x_j
&= \sum_{j=1}^n (-1)^{j-1} \Delta\!\left(\sum_k \alpha_k x_k, x_1, \ldots, \hat{x}_j, \ldots, x_n\right) x_j \\
&= \sum_{j,k} (-1)^{j-1} \alpha_k \Delta(x_k, x_1, \ldots, \hat{x}_j, \ldots, x_n) \cdot x_j.
\end{align*}
By skew symmetry, $\Delta(x_k, x_1, \ldots, \hat{x}_j, \ldots, x_n)$ is zero unless $k = j$ (when $k \neq j$, the vector $x_k$ appears twice among the arguments). When $k = j$, moving $x_j$ from position $1$ to position $j$ in the argument list requires $j-1$ transpositions (each introducing a factor of $-1$), yielding $\Delta(x_j, x_1, \ldots, \hat{x}_j, \ldots, x_n) = (-1)^{j-1} \Delta(x_1, \ldots, x_n)$. Thus the double sum reduces to
$$\sum_{j=1}^n (-1)^{j-1} \alpha_j \cdot (-1)^{j-1} \Delta(x_1, \ldots, x_n) \cdot x_j = \Delta(x_1, \ldots, x_n) \sum_{j=1}^n \alpha_j x_j = \Delta(x_1, \ldots, x_n) \cdot x.$$
The identity is proved.
