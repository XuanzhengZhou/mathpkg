---
role: proof
locale: en
of_concept: "let-and-be-any-nonnegative-functions-on-if"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.5"
---

Write $f = \sum_{j=1}^{m} \alpha_j \xi_{A_j}$ and $g = \sum_{k=1}^{n} \beta_k \xi_{B_k}$, where $\bigcup_{j=1}^{m} A_j = \bigcup_{k=1}^{n} B_k = X$.

Then $f + g = \sum_{j=1}^{m} \sum_{k=1}^{n} (\alpha_j + \beta_k) \xi_{(A_j \cap B_k)}$. Thus by (12.4) we have

$$L(f + g) = \sum_{j=1}^{m} \sum_{k=1}^{n} (\alpha_j + \beta_k) \mu(A_j \cap B_k)$$

$$= \sum_{j=1}^{m} \sum_{k=1}^{n} \alpha_j \mu(A_j \cap B_k) + \sum_{k=1}^{n} \sum_{j=1}^{m} \beta_k \mu(A_j \cap B_k)$$

$$= \sum_{j=1}^{m} \alpha_j \mu(A_j) + \sum_{k=1}^{n} \beta_k \mu(B_k)$$

$$= L(f) + L(g).$$
