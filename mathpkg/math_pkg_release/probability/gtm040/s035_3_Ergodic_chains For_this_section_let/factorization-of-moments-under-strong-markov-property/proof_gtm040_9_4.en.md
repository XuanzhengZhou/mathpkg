---
role: proof
locale: en
of_concept: factorization-of-moments-under-strong-markov-property
source_book: gtm040
source_chapter: "9"
source_section: "4"
---

$$M_\pi[t_i^r t_{i,j}^s] = \sum_{m,n} \Pr_\pi[t_i = m \wedge t_{i,j} = n] \, m^r n^s$$
$$= \sum_{m,n} \Pr_\pi[t_i = m] \, \Pr_\pi[t_{i,j} = n \mid t_i = m] \, m^r n^s$$
$$= \sum_{m,n} \Pr_\pi[t_i = m] \, \Pr_i[t_j = n] \, m^r n^s \quad \text{by the strong Markov property}$$
$$= \sum_m \Pr_\pi[t_i = m] \, m^r \left( \sum_n \Pr_i[t_j = n] \, n^s \right)$$
$$= M_\pi[t_i^r] \, M_i[t_j^s].$$
