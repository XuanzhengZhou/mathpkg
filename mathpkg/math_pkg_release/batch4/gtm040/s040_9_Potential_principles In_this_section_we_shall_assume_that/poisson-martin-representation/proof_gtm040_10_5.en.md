---
role: proof
locale: en
of_concept: poisson-martin-representation
source_book: gtm040
source_chapter: "10"
source_section: "5"
---

Apply Corollary 10-22 to the $h$-process:
$$\int_{S^{h*}} K^h(i, x) d\mu^h(x) = 1$$
for $i \in S^h$. That is, $h_i = \int_{S^{h*}} K(i, x) d\mu^h(x) = \int_{S^*} K(i, x) d\mu^h(x)$ for $i \in S^h$.

If $i \in S - S^h$, then $N_{ij} = 0$ for all $j \in S^h$ by Lemma 10-24, so $K(i, j) = 0$ for such $i, j$. Since $K(i, x)$ is continuous on $S^{h*}$, $K(i, x) = 0$ for $i \notin S^h$ and $x \in S^{h*}$. Therefore $h_i = 0 = \int_{S^*} K(i, x) d\mu^h(x)$ for such $i$, completing the representation.
