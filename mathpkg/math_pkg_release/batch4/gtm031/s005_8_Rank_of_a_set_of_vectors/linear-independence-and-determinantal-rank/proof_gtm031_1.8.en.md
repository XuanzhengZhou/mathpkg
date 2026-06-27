---
role: proof
locale: en
of_concept: linear-independence-and-determinantal-rank
source_book: gtm031
source_chapter: "1"
source_section: "8"
---

Evidently the determinantal rank $\rho \leq n$. Also the $x$'s are linearly independent only if $r \leq n$. Hence we may assume that $r \leq n$.

Suppose first that the $x$'s are dependent, so that, say,
$$
x_1 = \beta_2 x_2 + \cdots + \beta_r x_r.
$$
Then $\alpha_{1j} = \beta_2 \alpha_{2j} + \beta_3 \alpha_{3j} + \cdots + \beta_r \alpha_{rj}$ for $j = 1, 2, \cdots, n$. Hence

$$
(\alpha) = \begin{bmatrix}
\sum_{k=2}^{r} \beta_k \alpha_{k1} & \sum_{k=2}^{r} \beta_k \alpha_{k2} & \cdots & \sum_{k=2}^{r} \beta_k \alpha_{kn} \\
\alpha_{21} & \alpha_{22} & \cdots & \alpha_{2n} \\
\cdot & \cdot & \cdots & \cdot \\
\alpha_{r1} & \alpha_{r2} & \cdots & \alpha_{rn}
\end{bmatrix}.
$$

Since the first row of any $r$-rowed minor is a linear combination of the other rows, each $r$-rowed minor vanishes. Hence $\rho < r$.

Conversely, suppose that $\rho < r$. It is clear that the determinantal rank is unaltered when the rows or the columns of $(\alpha)$ are permuted. Such permutations give that there exist scalars $\beta_1, \beta_2, \ldots, \beta_{\rho+1}$, not all zero, such that $\beta_{\rho+1} = \beta \neq 0$ and

$$
\beta_1\alpha_{1j} + \beta_2\alpha_{2j} + \cdots + \beta_{\rho+1}\alpha_{\rho+1,j} = 0 \quad \text{for } j = 1, 2, \cdots, n.
$$

Hence
$$
\beta_1x_1 + \beta_2x_2 + \cdots + \beta_{\rho+1}x_{\rho+1} = 0
$$
where $\beta_{\rho+1} \neq 0$. Thus the $x$'s are dependent. This completes the proof.
