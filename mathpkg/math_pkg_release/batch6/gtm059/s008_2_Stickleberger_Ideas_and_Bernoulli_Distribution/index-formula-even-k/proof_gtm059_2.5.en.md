---
role: proof
locale: en
of_concept: index-formula-even-k
source_book: gtm059
source_chapter: "2"
source_section: "5"
---

First observe that since $\deg \theta$ and $\deg \theta'$ vanish for even $k$, we have $R_{k,\chi} \cap R_{0,\chi} = R_{k,\chi} \cap R_{0,\chi}$. By Theorem 2.1 (the intersection theorem), we conclude that $R_{k,\chi} \cap R_{0,\chi} = R_{0,\chi}$.

The index is computed by writing $R_{k,\chi} + R_{0,\chi}$ as a direct sum and evaluating the determinant of the multiplication-by-Bernoulli map. The computation reduces to evaluating the generalized Bernoulli sum

$$
B_{k,\chi} = f^{k-1} \sum_{a=1}^{f} \chi(a) B_k(a/f),
$$

which gives the stated formula after accounting for the power of $N$ arising from the level.
