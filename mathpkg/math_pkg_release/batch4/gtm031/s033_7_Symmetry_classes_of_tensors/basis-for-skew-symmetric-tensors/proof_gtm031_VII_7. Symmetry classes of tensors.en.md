---
role: proof
locale: en
of_concept: basis-for-skew-symmetric-tensors
source_book: gtm031
source_chapter: "VII"
source_section: "7. Symmetry classes of tensors"
---
In the expression $\sum \xi^{i_1 i_2 \cdots i_r} e_{i_1} \times \cdots \times e_{i_r}$ for a skew-symmetric tensor, any term with two equal indices among the $i_j$ has $\xi^{i_1 \cdots i_r} = 0$, so these terms can be dropped. For terms with all indices distinct, suppose $i_1 < i_2 < \cdots < i_r$ after reordering. By equation (26), the coefficient of any permutation satisfies $\xi^{i_{1'} i_{2'} \cdots i_{r'}} = \epsilon_\sigma \xi^{i_1 i_2 \cdots i_r}$. Summing over all permutations $\sigma$, the contribution from the orbit of $(i_1, \ldots, i_r)$ is
$$\xi^{i_1 i_2 \cdots i_r} \sum_{\sigma} \epsilon_\sigma e_{i_{1'}} \times e_{i_{2'}} \times \cdots \times e_{i_{r'}} = \xi^{i_1 i_2 \cdots i_r} [e_{i_1} e_{i_2} \cdots e_{i_r}].$$
Thus the tensors $[e_{i_1} e_{i_2} \cdots e_{i_r}]$ with $i_1 < i_2 < \cdots < i_r$ (lexicographically ordered) span the space. Their linear independence follows from the fact that different $r$-tuples of ordered indices produce basis elements with disjoint support in the tensor space, and the dimension is $\binom{n}{r}$.
