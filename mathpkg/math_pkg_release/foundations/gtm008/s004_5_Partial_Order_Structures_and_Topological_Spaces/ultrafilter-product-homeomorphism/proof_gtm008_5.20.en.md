---
role: proof
locale: en
of_concept: ultrafilter-product-homeomorphism
source_book: gtm008
source_chapter: "5"
source_section: "5"
---
For a given $i \in I$ and an element $a_i \in P_i$, let $\hat{a}_i$ be the element of $P$ whose $i$-th projection is $a_i$ and whose $j$-th projection is $1_j$ for $j \neq i$, i.e.,
$$\hat{a}_i(i) = a_i, \quad \hat{a}_i(j) = 1_j \text{ for } j \neq i.$$

For each $F \in \mathcal{F}$, define $F_i = \{a_i \in P_i \mid \hat{a}_i \in F\}$. Then $F_i$ is a filter for $P_i$ since $a_i \leq_i b_i$ implies $\hat{a}_i \leq \hat{b}_i$, and since $F$ is upward hereditary, if $a_i \in F_i$ and $a_i \leq_i b_i$ then $b_i \in F_i$. Furthermore $F_i$ is maximal: if $G_i$ is a filter properly containing $F_i$, then $\{p \in P : \exists a_i \in G_i,\; \hat{a}_i \leq p\}$ would be a filter properly containing $F$, contradicting that $F$ is an ultrafilter.

The mapping $\Phi: \mathcal{F} \to \prod_{i \in I} \mathcal{F}_i$ defined by $\Phi(F) = (F_i)_{i \in I}$ is the required homeomorphism. It is bijective and continuous with respect to the product topology because the basic open sets $N(\hat{a}_i)$ in $\mathcal{F}$ correspond to basic open sets in the $i$-th coordinate.
