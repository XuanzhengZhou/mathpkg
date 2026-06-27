---
role: proof
locale: en
of_concept: extended-chain-characterization
source_book: gtm040
source_chapter: "10"
source_section: "2"
---

We have
$$\nu_j = \sum_n \Pr[x_n = j] = \sum_{n,m,i} \mu_i^{E,m} P_{ij}^{(n-m)} = \sum_{m,i} \mu_i^{E,m} N_{ij} = \sum_i \mu_i^E N_{ij} = (\mu^E N)_j.$$
Taking $E = \{j\}$, we find $\nu_j = \mu_j^E N_{jj}$. Now $\mu_j^E$ is finite by (3) and strictly positive by (1). Hence $\nu_j$ is finite for all $j \in S$ if and only if all elements of $S$ are transient for $P$. The state $b$, if present, must be absorbing.
