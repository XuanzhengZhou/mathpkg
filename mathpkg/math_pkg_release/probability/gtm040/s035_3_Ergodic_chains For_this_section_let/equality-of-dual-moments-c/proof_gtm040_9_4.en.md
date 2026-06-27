---
role: proof
locale: en
of_concept: equality-of-dual-moments-c
source_book: gtm040
source_chapter: "9"
source_section: "4"
---

For the equality of distributions, we compute

$$\alpha_i \Pr_i[t_0 = m] = \sum \alpha_i P_{ik_1} P_{k_1k_2} \dots P_{k_{m-1}0}$$
$$= \sum \alpha_0 \hat{P}_{0k_{m-1}} \dots \hat{P}_{k_2k_1} \hat{P}_{k_1i},$$

where each of the sums is taken over the denumerable number of sequences $k_1, \dots, k_{m-1}$ with each $k_j$ different from $0$. Hence for $m > 0$,

$$\sum_i \alpha_i \Pr_i[t_0 = m] = \alpha_0 \sum \hat{P}_{0k_{n-1}} \dots \hat{P}_{k_2k_1}$$
$$= \alpha_0(1 - \hat{H}_{00}^{(m-1)}) = \alpha_0(1 - \bar{H}_{00}^{(m-1)}) \quad \text{by Lemma 9-69}$$
$$= \sum_i \alpha_i \Pr_i[\hat{t}_0 = m] \quad \text{by symmetry.}$$

Multiplying through by $m^r$ and summing on $m$ yields $c_0^{(r)} = \hat{c}_0^{(r)}$.
