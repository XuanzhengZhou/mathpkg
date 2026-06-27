---
role: proof
locale: en
of_concept: integral-of-simple-function
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

We may suppose that the pairwise disjoint family $\{E_k\}_{k=1}^{n}$ covers $X$. Since $\inf\{f(x) : x \in E_k\} = \alpha_k$, we have $L(f) \geq \sum_{k=1}^{n} \alpha_k \mu(E_k)$. Now let $\{B_j\}_{j=1}^{m}$ be an arbitrary measurable dissection of $X$. Then\n\n$$\sum_{j=1}^{m} \inf\{f(x) : x \in B_j\} \mu(B_j) = \sum_{j=1}^{m} \sum_{k=1}^{n} \inf\{f(x) : x \in B_j\} \mu(E_k \cap B_j)$$\n\n$$\leq \sum_{j=1}^{m} \sum_{k=1}^{n} \inf\{f(x) : x \in E_k \cap B_j\} \mu(E_k \cap B_j)$$\n\n$$= \sum_{j=1}^{m} \sum_{k=1}^{n} \alpha_k \mu(E_k \cap B_j)$$\n\n$$= \sum_{k=1}^{n} \alpha_k \mu(E_k).$$\n\nThus we obtain $L(f) \leq \sum_{k=1}^{n} \alpha_k \mu(E_k)$ and hence $L(f) = \sum_{k=1}^{n} \alpha_k \mu(E_k)$.
