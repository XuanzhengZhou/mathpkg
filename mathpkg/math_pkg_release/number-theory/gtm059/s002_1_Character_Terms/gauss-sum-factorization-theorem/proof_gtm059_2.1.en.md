---
role: proof
locale: en
of_concept: gauss-sum-factorization-theorem
source_book: gtm059
source_chapter: "2"
source_section: "1"
---

We compute the order of $\mathfrak{P}$ in the ideal factorization of $S(\chi\chi^{*-1})$:

$$\operatorname{ord}_{\mathfrak{P}}(S(\chi\chi^{*-1})) = \operatorname{ord}_{\mathfrak{P}}(S(\chi\chi^{*-1})) = \operatorname{ord}_{\mathfrak{P}}(\chi\chi^{*-1})$$

by Theorem 2.1. On the other hand, the isotropy group of $\chi$ in the Galois group $G$ consists of the powers $\{\sigma^k \mid k = 0, \dots, n-1\}$ where $\sigma$ is a generator of the decomposition group. Hence in the ideal $\mathfrak{p}^{p(\chi^*)^*}$ the prime $\chi(\chi^*)^*$ occurs with multiplicity

$$\sum_{k=0}^{n-1} \frac{\sigma^k}{q^{k-1}}.$$

The result then follows from Lemma 1 which provides the summation formula for $t(k) = (p-1)\sum_{j=0}^{n-1} k/q^{j-1}$, establishing that the two factorizations coincide. The lemma is proved by noting both sides are $(q-1)$-periodic and using a congruence modulo $q-1$.
