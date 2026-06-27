---
role: proof
locale: en
of_concept: d10-submatroid-and-projection-matroid
source_book: gtm054
source_chapter: "X"
source_section: "50"
---

Recall that $\Lambda_U = (U, \mathcal{M}_U)$ where $\mathcal{M}_U = \{M \in \mathcal{M} : M \subseteq U\}$, and $\Lambda_{[U]} = (U, \mathcal{M}(\pi_U[\mathcal{E}]))$ where $\pi_U(S) = U \cap S$ and $\mathcal{E}$ is a collection of subsets from which $\mathcal{M}$ is generated.

For $\Lambda_U$: The collection $\mathcal{M}_U = \mathcal{M} \cap \mathcal{P}(U)$ satisfies the cycle axioms of a matroid (conditions B15) restricted to $U$, since the cycle exchange property is preserved under intersection with a subset.

For $\Lambda_{[U]}$: Let $\mathcal{E}$ be the collection of cycles of $\Lambda$. Then $\pi_U[\mathcal{E}] = \{U \cap M : M \in \mathcal{M}\}$. The set system $(U, \mathcal{M}(\pi_U[\mathcal{E}]))$ satisfies the matroid axioms because $\pi_U$ preserves the essential structure needed for the cycle exchange property.
