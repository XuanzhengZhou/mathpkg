---
role: proof
locale: en
of_concept: invariant-neighborhoods-characterization
source_book: gtm027
source_chapter: "6"
source_section: "O"
---

# Proof: Characterization of Groups with Invariant Neighborhood Bases

Let $I$ be the family of all neighborhoods of the identity $e$ which are invariant under inner automorphisms (i.e., $U \in I$ iff $xUx^{-1} = U$ for all $x \in G$).

If $I$ is a base for the neighborhood system of $e$, then for each $U \in I$, we have $U_L = \{(x, y) : x^{-1}y \in U\} = \{(x, y) : xy^{-1} \in U\} = U_R$, because $x^{-1}y \in U$ iff $y \in xU$, and $xy^{-1} \in U$ iff $xy^{-1} \in xUx^{-1} = U$ (using invariance). Moreover, $U_L = U_R$ is invariant under both left and right translation: for any $a \in G$, $(ax, ay) \in U_L$ iff $(ax)^{-1}(ay) = x^{-1}y \in U$ iff $(x, y) \in U_L$; and similarly for right translation.

The family of all pseudo-metrics which are both left and right invariant and continuous on $G \times G$ then generates a uniformity whose entourages are precisely those invariant under both translations. This uniformity's topology equals $\mathcal{J}$ because the $U_L$ (equivalently $U_R$) for $U \in I$ form a base.

Conversely, if the family of left-right invariant pseudo-metrics generates a uniformity whose topology is $\mathcal{J}$, then for any such pseudo-metric $p$, $p(e, y) = p(x^{-1}ex, x^{-1}yx)$ (by invariance), so the $p$-balls about $e$ are invariant under inner automorphisms. Since these balls form a neighborhood base, $I$ is a base for the neighborhood system of $e$.
