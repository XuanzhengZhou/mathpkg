---
role: proof
locale: en
of_concept: explicit-form-of-rth-compound
source_book: gtm031
source_chapter: "VII"
source_section: "7. Symmetry classes of tensors"
---
Since $e_i A = \sum \alpha_{ij} e_j$, we compute:
\begin{align*}
[e_{i_1} e_{i_2} \cdots e_{i_r}] A_0^r
&= \sum_{\sigma} \epsilon_{\sigma} e_{i_{1'}} A \times e_{i_{2'}} A \times \cdots \times e_{i_{r'}} A \\
&= \sum_{\sigma} \sum_{j_1, \ldots, j_r} \epsilon_{\sigma} \alpha_{i_{1'}, j_1} \alpha_{i_{2'}, j_2} \cdots \alpha_{i_{r'}, j_r} \, e_{j_1} \times e_{j_2} \times \cdots \times e_{j_r} \\
&= \sum_{j_1, \ldots, j_r} \left( \sum_{\sigma} \epsilon_{\sigma} \alpha_{i_{1'}, j_1} \alpha_{i_{2'}, j_2} \cdots \alpha_{i_{r'}, j_r} \right) e_{j_1} \times \cdots \times e_{j_r}.
\end{align*}
The inner sum is precisely the determinant of the $r \times r$ matrix $(\alpha_{i_p, j_q})$:
$$\sum_{\sigma} \epsilon_{\sigma} \alpha_{i_{1'}, j_1} \alpha_{i_{2'}, j_2} \cdots \alpha_{i_{r'}, j_r} = \det(\alpha_{i_p, j_q})_{p,q=1}^r.$$
When we express the result in the basis of antisymmetrized tensors $[e_{j_1} \cdots e_{j_r}]$ with $j_1 < \cdots < j_r$, each determinant appears as the coefficient. The terms where the $j$'s are not strictly increasing combine to form $[e_{j_1} \cdots e_{j_r}]$ up to sign, and the sum over all permutations of the column indices yields exactly the factor of $r!$ that cancels. Hence the coefficient of $[e_{j_1} \cdots e_{j_r}]$ (with $j_1 < \cdots < j_r$) is precisely the $r \times r$ minor $\det(\alpha_{i_p, j_q})$.
