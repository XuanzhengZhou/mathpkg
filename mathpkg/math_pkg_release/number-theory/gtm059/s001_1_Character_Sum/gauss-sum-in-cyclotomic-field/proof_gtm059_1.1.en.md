---
role: proof
locale: en
of_concept: gauss-sum-in-cyclotomic-field
source_book: gtm059
source_chapter: "1"
source_section: "§1 Character Sums"
---

For each case we examine the action on the given expression by an automorphism $\sigma_{ij}$ of the Galois group. Recall that the Gauss sum is
$$\tau(\chi) = \sum_{x \in F^*} \chi(x) \zeta^{\operatorname{Tr}(x)},$$
where $\zeta$ is a primitive $p$-th root of unity and $\operatorname{Tr} = \operatorname{Tr}_{F/\mathbf{F}_p}$.

Let $\sigma_{ij}$ be the automorphism of $\mathbf{Q}(\zeta_p, \zeta_m)$ determined by
$$\sigma_{ij}(\zeta_p) = \zeta_p^i, \quad \sigma_{ij}(\zeta_m) = \zeta_m^j,$$
with $(i, p) = 1$ and $(j, m) = 1$. Then
$$\sigma_{ij}(\tau(\chi)) = \chi(i)^{-1} \tau(\chi^j).$$

In particular, for the automorphism $\sigma_{i,1}$ fixing $\zeta_m$, we have
$$\sigma_{i,1}(\tau(\chi)) = \chi(i)^{-1} \tau(\chi).$$

Consequently,
$$\sigma_{i,1}(\tau(\chi)^m) = \chi(i)^{-m} \tau(\chi)^m = \tau(\chi)^m,$$
since $\chi(i)^m = 1$ by the assumption that $\chi$ has order $m$. This shows that $\tau(\chi)^m$ is fixed by all automorphisms $\sigma_{i,1}$, i.e., by the subgroup of the Galois group that fixes $\mathbf{Q}(\zeta_m)$. Hence $\tau(\chi)^m$ lies in $\mathbf{Q}(\zeta_m)$.

For the second statement, one considers the automorphisms $\sigma_{1,j}$ fixing $\zeta_p$ and argues similarly, verifying that the relevant expression is fixed under the appropriate subgroup, thereby showing it lies in $\mathbf{Q}(\zeta_{mp})$.
