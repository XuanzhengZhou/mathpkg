---
role: proof
locale: en
of_concept: zero-divisors-in-tensor-products
source_book: gtm028
source_chapter: "I"
source_section: "14. Tensor products of rings"
---

Suppose $a \in A$ is not a zero-divisor in $A$, and let $a\xi = 0$ for some $\xi \in A \otimes_k B$. Write $\xi = \sum_i a_i \otimes b_i$, where $a_i \in A$ and the $b_i \in B$ are chosen to be linearly independent over $k$ (this is always possible by expressing $\xi$ in terms of a $k$-basis of the subspace spanned by the original $b_i$). Since the elements $1 \otimes b_i$ are linearly independent over $A$ in $A \otimes_k B$ (they remain independent after extending scalars from $k$ to $A$), we have

$$0 = a\xi = \sum_i (a a_i) \otimes b_i.$$

Linear independence of the $\{1 \otimes b_i\}$ over $A$ forces $a a_i = 0$ in $A$ for each $i$. Since $a$ is not a zero-divisor in $A$, we conclude $a_i = 0$ for all $i$, hence $\xi = 0$. Therefore $a$ is not a zero-divisor in $A \otimes_k B$.
