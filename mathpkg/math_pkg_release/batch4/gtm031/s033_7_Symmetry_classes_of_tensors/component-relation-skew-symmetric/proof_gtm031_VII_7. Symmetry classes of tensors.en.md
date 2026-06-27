---
role: proof
locale: en
of_concept: component-relation-skew-symmetric
source_book: gtm031
source_chapter: "VII"
source_section: "7. Symmetry classes of tensors"
---
Express the tensor $T$ in the basis $(e_1, \ldots, e_n)$ as $T = \sum \xi^{i_1 i_2 \cdots i_r} e_{i_1} \times \cdots \times e_{i_r}$. By the definition of skew-symmetry,
$$P(\sigma)T = \epsilon_\sigma T.$$
Applying $P(\sigma)$ to the component expansion gives
$$\sum \xi^{i_1 i_2 \cdots i_r} e_{i_1'} \times \cdots \times e_{i_r'} = \epsilon_\sigma \sum \xi^{i_1 i_2 \cdots i_r} e_{i_1} \times \cdots \times e_{i_r}.$$
This is equation (25). Now compare the coefficients of $e_{i_1'} \times \cdots \times e_{i_r'}$ on both sides. On the left, the coefficient is $\xi^{i_1 \cdots i_r}$ when the summand has indices $(i_1, \ldots, i_r)$ (before permutation). On the right, applying $\sigma^{-1}$ to the summation index (or equivalently, relabeling indices), we obtain that the coefficient of $e_{i_1'} \times \cdots \times e_{i_r'}$ on the right side is $\epsilon_\sigma \xi^{i_{1'} i_{2'} \cdots i_{r'}}$. Equating coefficients and using $\epsilon_\sigma^{-1} = \epsilon_\sigma$ yields $\xi^{i_{1'} i_{2'} \cdots i_{r'}} = \epsilon_\sigma \xi^{i_1 i_2 \cdots i_r}$, which is equation (26).
