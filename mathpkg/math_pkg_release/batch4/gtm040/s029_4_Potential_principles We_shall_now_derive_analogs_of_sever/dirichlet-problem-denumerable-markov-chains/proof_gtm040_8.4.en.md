---
role: proof
locale: en
of_concept: dirichlet-problem-denumerable-markov-chains
source_book: gtm040
source_chapter: "8"
source_section: "4"
---

**Existence:** Set
$$\bar{h} = B^E \binom{h_E}{0}.$$
The product is defined, since $h_E$ is bounded and $B^E$ has row sums one. Then the restriction of $\bar{h}$ to $E$ is $h_E$ because $(B^E)_{ij} = \delta_{ij}$ for $i$ and $j$ in $E$. Moreover,
$$(I - P)\bar{h} = (I - P)B^E \binom{h_E}{0} = \binom{I - P^E}{0} \binom{h_E}{0} = \binom{(I - P^E)h_E}{0},$$
so that $\bar{h}$ is regular outside of $E$; associativity is justified in the triple product because $(I + P)B^E \binom{|h_E|}{0}$ is finite-valued.

**Uniqueness:** Let $k = \binom{h_E}{\bar{k}}$ be another such bounded function. Then $\bar{h} - k$ is a bounded function which is zero on $E$ and regular on $\tilde{E}$. By Lemma 8-40 applied to the chain $E^P$, which is absorbing by hypothesis, this function must be identically zero. Hence $\bar{h} = k$.
