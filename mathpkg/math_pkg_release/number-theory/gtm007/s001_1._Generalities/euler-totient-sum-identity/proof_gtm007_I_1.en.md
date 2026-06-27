---
role: proof
locale: en
of_concept: euler-totient-sum-identity
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

If $d$ divides $n$, let $C_d$ be the unique subgroup of $\mathbb{Z}/n\mathbb{Z}$ of order $d$, and let $\Phi_d$ be the set of generators of $C_d$. Since every element of $\mathbb{Z}/n\mathbb{Z}$ generates one of the $C_d$, the group $\mathbb{Z}/n\mathbb{Z}$ is the disjoint union of the $\Phi_d$. Thus

$$n = \operatorname{Card}(\mathbb{Z}/n\mathbb{Z}) = \sum_{d \mid n} \operatorname{Card}(\Phi_d) = \sum_{d \mid n} \phi(d).$$
