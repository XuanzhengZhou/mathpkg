---
role: proof
locale: en
of_concept: total-quotient-ring-of-tensor-product
source_book: gtm028
source_chapter: "I"
source_section: "14. Tensor products of rings"
---

By the Lemma, every regular element of $A$ is also a regular element of $A \otimes_k B$, hence invertible in the total quotient ring $K$ of $A \otimes_k B$. Therefore we can speak of the quotient ring of $A$ in $K$, and by I, §19, Corollary 3, this quotient ring is a total quotient ring of $A$. The same holds for $B$.

To prove linear disjointness: let $\{b_i/b\}$ be elements of the quotient ring of $B$ in $K$ (with $b, b_i \in B$, $b$ regular in $B$), and suppose they are linearly dependent over the quotient ring of $A$ in $K$. Multiplying through by the product of the denominators (which are regular in $A \otimes_k B$), we obtain a linear dependence relation with coefficients in $A$. But the $b_i$ (and $b$) are linearly independent over $k$ by construction, and hence over $A$ in $A \otimes_k B$, since the elements $1 \otimes b$ form an $A$-basis when the $b$ are $k$-linearly independent. Therefore the quotient rings are linearly disjoint over $k$.
