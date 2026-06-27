---
role: proof
locale: en
of_concept: degree-of-sum-and-product
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

For the sum: write $f = \sum_{k=0}^n \alpha_k t^k$ and $g = \sum_{k=0}^m \beta_k t^k$ with $\alpha_n \neq 0$, $\beta_m \neq 0$. Then $f+g = \sum_{k=0}^{\max(n,m)} (\alpha_k+\beta_k)t^k$ where coefficients beyond each polynomial's degree are taken as $0$. Thus $\deg(f+g) \leq \max(n,m)$.

For the product: $fg = \sum_k \gamma_k t^k$ where $\gamma_k = \sum_{i+j=k} \alpha_i \beta_j$. The highest index with non-zero coefficient is $n+m$, and $\gamma_{n+m} = \alpha_n \beta_m \neq 0$ since $\Gamma$ is a field (no zero divisors). Thus $\deg(fg) = n+m = \deg f + \deg g$.
