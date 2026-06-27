---
role: proof
locale: en
of_concept: change-of-basis-for-bilinear-form
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

Let $(u_1, \dots, u_n)$ be a second basis in $\mathfrak{R}$ with $u_i = \sum_j \mu_{ij} e_j$ where $(\mu) \in L(\Delta, n)$, and let $(v_1', \dots, v_{n'}')$ be a second basis in $\mathfrak{R}'$ with $v_k' = \sum_l f_l' \nu_{lk}$ where $(\nu) \in L(\Delta, n')$. Then by bilinearity,

$$g(u_i, v_k') = g\!\left(\sum_j \mu_{ij} e_j, \sum_l f_l' \nu_{lk}\right) = \sum_{j,l} \mu_{ij} \, g(e_j, f_l') \, \nu_{lk} = \sum_{j,l} \mu_{ij} \beta_{jl} \nu_{lk}.$$

Thus the matrix of $g$ relative to the new bases is $(\mu)(\beta)(\nu)$, where $(\beta)$ is the matrix relative to the original bases.
