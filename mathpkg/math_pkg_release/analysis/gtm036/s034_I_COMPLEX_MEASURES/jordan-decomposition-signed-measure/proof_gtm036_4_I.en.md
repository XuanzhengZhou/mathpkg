---
role: proof
locale: en
of_concept: jordan-decomposition-signed-measure
source_book: gtm036
source_chapter: "4"
source_section: "I (Complex Measures)"
---
For a signed measure $\mu$, one defines the upper variation $\mu^+$ and lower variation $\mu^-$ by the standard Jordan decomposition for signed measures (see Halmos [4]). Specifically, let $P$ and $N$ be a Hahn decomposition of $X$ with respect to $\mu$; then for each $A \in \mathcal{S}$,
$$\mu^+(A) = \mu(A \cap P), \quad \mu^-(A) = -\mu(A \cap N).$$
Both $\mu^+$ and $\mu^-$ are positive measures, at least one of which is finite, and $\mu = \mu^+ - \mu^-$. The total variation is then
$$|\mu|(A) = \mu^+(A) + \mu^-(A) = \sup \sum_{r=1}^n |\mu(B_r)|,$$
where the supremum is taken over all finite partitions of $A$ by disjoint sets $B_r \in \mathcal{S}$.
