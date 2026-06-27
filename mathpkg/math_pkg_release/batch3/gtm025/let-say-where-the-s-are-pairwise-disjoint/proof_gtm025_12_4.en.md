---
role: proof
locale: en
of_concept: "let-say-where-the-s-are-pairwise-disjoint"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.4"
---

We may suppose that the pairwise disjoint family $\{E_k\}_{k=1}^{n}$ covers $X$. Since $\inf\{f(x) : x \in E_k\} = \alpha_k$, we have $L(f) \geq \sum_{k=1}^{n} \alpha_k \mu(E_k)$. Now let $\{B_j\}_{j=1}^{m}$ be an arbitrary measurable dissection of $X$. Then

$$\sum_{j=1}^{m} \inf\{f(x) : x \in B_j\} \mu(B_j) = \sum_{j=1}^{m} \sum_{k=1}^{n} \inf\{f(x) : x \in B_j\} \mu(E_k \cap B_j)$$

$$\leq \sum_{j=1}^{m} \sum_{k=1}^{n} \inf\{f(x) : x \in E_k \cap B_j\} \mu(E_k \cap B_j)$$

$$= \sum_{j=1}^{m} \sum_{k=1}^{n} \alpha_k \mu(E_k \cap B_j)$$

$$= \sum_{k=1}^{n} \alpha_k \mu(E_k).$$

Thus we obtain $L(f) \leq \sum_{k=1}^{n} \alpha_k \mu(E_k)$ and hence $L(f) = \sum_{k=1}^{n} \alpha_k \mu(E_k)$.
