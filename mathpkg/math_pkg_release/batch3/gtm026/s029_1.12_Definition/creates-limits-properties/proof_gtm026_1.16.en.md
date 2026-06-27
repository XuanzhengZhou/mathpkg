---
role: proof
locale: en
of_concept: creates-limits-properties
source_book: gtm026
source_chapter: "1"
source_section: "1.16"
---

**Proof.** (1) and (2) are straightforward consequences of the definition.

(3) The rightmost square in the diagram above is a pullback whenever the leftmost square is (consider the kernel pair of $iU$). It is now clear that the passage from $i$ to $iU$ is a well-defined function from monosubobjects of $A$ into monosubobjects of $AU$. It suffices to prove that this function is injective. To this end, let $i: S \to A$ and $i': S' \to A$ be monos and suppose there exists an isomorphism $f: SU \to S'U$ of subobjects. Then the rightmost square is a pullback diagram, so must lift to a pullback diagram in $\mathcal{A}$. As $\text{id}_{SU}$ and $f$ are isomorphisms in $\mathcal{K}$, $(\text{id}_{SU})^{-1}.f$ and $f^{-1}.\text{id}_{SU}$ are the desired $\mathcal{A}$-morphisms showing that $(S, i)$ and $(S', i')$ represent the same subobject of $A$. $\square$
