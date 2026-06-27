---
role: proof
locale: en
of_concept: uniqueness-of-representing-measure
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
By Lemma 10-39,

$$\mu^h(C \cap \bar{S}) = \Pr^h[x_v \in C \cap \bar{S}] = \int_S \Pr^{K(\cdot, x)}[x_v \in C \cap \bar{S}] \, d\nu(x).$$

But by Proposition 10-35,

$$\Pr^{K(\cdot, x)}[x_v \in C \cap \bar{S}] = \mu^{K(\cdot, x)}(C \cap \bar{S}) = \chi_{C \cap \bar{S}}(x).$$

Hence for all Borel sets $C \cap \bar{S}$,

$$\mu^h(C \cap \bar{S}) = \int_S \chi_{C \cap \bar{S}}(x) \, d\nu(x) = \nu(C \cap \bar{S}).$$

Since $\nu(\bar{S}) = 1$, we must have $\mu^h(\bar{S}) = 1$ and hence $\mu^h(C) = \nu(C)$ for all Borel sets $C$ in $S^*$.
