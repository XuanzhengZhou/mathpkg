---
role: proof
locale: en
of_concept: limit-interchange-nondecreasing-double-sequence
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

In the extended sense $\lim_i b_{ij} = L_j$ exists and so does $\lim_j b_{ij} = L_i^*$. Now $\{L_j\}$ is nondecreasing, for if $L_j > L_{j+k}$, then for $i$ sufficiently large $b_{ij} > L_{j+k} \geq b_{i,j+k}$, which is impossible because $b_{ij}$ is nondecreasing in $j$. Similarly $\{L_i^*\}$ is nondecreasing, so that $\lim_j L_j = L$ and $\lim_i L_i^* = L^*$ exist in the extended sense.

If $L \neq L^*$, we may assume $L^* > L$ and hence $L$ is finite. Then there exists an $i$ such that $L_i^* > L$. Hence

$$L_i^* > L \geq L_j \quad \text{for all } j \geq b_{ij} \quad \text{for all } j.$$

Thus $b_{ij}$ is bounded away from its limit on $j$, a contradiction. Therefore $L = L^*$.
