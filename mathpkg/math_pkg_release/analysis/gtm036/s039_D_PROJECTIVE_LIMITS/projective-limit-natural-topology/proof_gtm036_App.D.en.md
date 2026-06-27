---
role: proof
locale: en
of_concept: projective-limit-natural-topology
source_book: gtm036
source_chapter: "Appendix"
source_section: "D"
---

Recall that a projective limit $\varprojlim_{t \in A} F_t$ of a directed system of locally convex spaces $\{F_t, h_{st}: F_t \to F_s\}_{s \leq t}$ is defined as the subspace of the product $\prod_{t \in A} F_t$ consisting of those tuples $(x_t)_{t \in A}$ satisfying $h_{st}(x_t) = x_s$ for all $s \leq t$.

The natural topology on the projective limit is the relativization (subspace topology) of the product topology on $\prod_{t \in A} F_t$. This topology is precisely the weakest topology on the limit that makes each coordinate projection $\pi_t: \varprojlim F_t \to F_t$ continuous. But these coordinate projections are linear maps into locally convex spaces, so by definition this is exactly the projective topology on $\varprojlim F_t$ determined by the family $\{F_t, \pi_t : t \in A\}$.

Thus every projective limit, equipped with its natural (relative product) topology, is a space with a projective topology. This observation unifies the two concepts: projective limits are the principal source of projective topologies, and conversely every projective topology can be realized as a projective limit (see property (c)).
