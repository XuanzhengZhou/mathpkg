---
role: proof
locale: en
of_concept: fractionary-ideal-prime-factorization
source_book: gtm028
source_chapter: "V"
source_section: "6"
---

Since a fractionary ideal $\mathfrak{a}$ may be written in the form $\mathfrak{b} \cdot \mathfrak{c}^{-1}$ where $\mathfrak{b}$ and $\mathfrak{c}$ are integral ideals (for example, if $\mathfrak{a} = (1/d)\mathfrak{b}$ with $d \in R$ and $\mathfrak{b} \subset R$, we take $\mathfrak{c} = Rd$) and since by definition we can express $\mathfrak{b}$ and $\mathfrak{c}$ as products of prime ideals, Theorem 10 shows that we can write $\mathfrak{a} = \prod_i \mathfrak{p}_i \cdot \prod_j \mathfrak{q}_j^{-1}$, where the $\mathfrak{p}_i$ and the $\mathfrak{q}_j$ are prime ideals in $R$. Thus $\mathfrak{a}$ is invertible, by Theorem 10. We may evidently assume that $\mathfrak{p}_i \neq \mathfrak{q}_j$ for all $i$ and $j$. If we have another factorization, uniqueness follows from Lemma 5 by multiplying both sides by the product of all denominators.

For the containment criterion: if $n_{\mathfrak{p}}(\mathfrak{a}) \geq n_{\mathfrak{p}}(\mathfrak{b})$ for all $\mathfrak{p}$, then $\mathfrak{a} \subset \mathfrak{b}$ since each local factor satisfies this. Conversely, if $\mathfrak{a} \subset \mathfrak{b}$, localizing at each $\mathfrak{p}$ gives the inequality.

For formula (2): the ideal $\mathfrak{a} + \mathfrak{b}$ is the smallest ideal containing both, hence at each $\mathfrak{p}$ the exponent is the minimum. For formula (3): $\mathfrak{a} \cap \mathfrak{b}$ is the largest ideal contained in both, giving the maximum. Formula (4) is immediate from the product representation.

Finally, since $\mathfrak{b}^{-1} = (R:\mathfrak{b})$ (Lemma 1), we have $\mathfrak{a} \cdot \mathfrak{b}^{-1} = \mathfrak{a} \cdot (R:\mathfrak{b}) \subset \mathfrak{a}:\mathfrak{b}$. On the other hand, $R = (R:\mathfrak{b})\mathfrak{b}$, hence $\mathfrak{a}:\mathfrak{b} = (\mathfrak{a}:\mathfrak{b})\mathfrak{b}(R:\mathfrak{b}) \subset \mathfrak{a} \cdot (R:\mathfrak{b})$. Therefore $\mathfrak{a} \cdot (R:\mathfrak{b}) = \mathfrak{a}:\mathfrak{b}$, and formula (5) follows immediately. Q.E.D.
