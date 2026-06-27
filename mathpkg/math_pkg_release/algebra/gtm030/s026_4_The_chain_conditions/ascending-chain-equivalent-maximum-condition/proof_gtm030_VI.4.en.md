---
role: proof
locale: en
of_concept: ascending-chain-equivalent-maximum-condition
source_book: gtm030
source_chapter: "Chapter VI"
source_section: "4. The chain conditions"
---

**Proof.** The proof follows the same pattern as the equivalence of the descending chain condition and the minimum condition.

Assume the ascending chain condition holds and let $\{\mathfrak{N}\}$ be a non-vacuous collection of submodules. Select $\mathfrak{N}_1$ in the collection. If $\mathfrak{N}_1$ is maximal, we are done. Otherwise there exists $\mathfrak{N}_2$ in the collection with $\mathfrak{N}_1 \subsetneq \mathfrak{N}_2$. If $\mathfrak{N}_2$ is maximal, we are done. Otherwise, continuing in this manner we obtain a strictly increasing sequence
$$\mathfrak{N}_1 \subsetneq \mathfrak{N}_2 \subsetneq \mathfrak{N}_3 \subsetneq \cdots$$
By the ascending chain condition, this sequence must terminate. Hence some $\mathfrak{N}_r$ is maximal in the collection.

Conversely, assume the maximum condition and let
$$\mathfrak{N}_1 \subseteq \mathfrak{N}_2 \subseteq \mathfrak{N}_3 \subseteq \cdots$$
be an increasing sequence of submodules. The collection $\{\mathfrak{N}_i\}$ contains a maximal element $\mathfrak{N}_N$ by the maximum condition. Then $\mathfrak{N}_N = \mathfrak{N}_{N+1} = \mathfrak{N}_{N+2} = \cdots$, since otherwise some later term would strictly contain $\mathfrak{N}_N$, contradicting maximality. Thus the ascending chain condition holds.
