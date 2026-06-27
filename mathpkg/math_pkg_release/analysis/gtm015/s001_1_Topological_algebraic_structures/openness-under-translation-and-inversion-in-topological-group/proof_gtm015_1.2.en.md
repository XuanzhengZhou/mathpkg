---
role: proof
locale: en
of_concept: openness-under-translation-and-inversion-in-topological-group
source_book: gtm015
source_chapter: "1"
source_section: "2"
---

# Proof of Open Sets under Translation and Inversion in a Topological Group

Let $G$ be a topological group, $A \subset G$ a subset, and $U \subset G$ an open set. We may assume that $A$ and $U$ are nonempty (otherwise the sets in question are empty and trivially open).

Write $J(x) = x^{-1}$ for the inversion mapping. By Theorem 2.8, $J$ is a homeomorphism, so it maps open sets to open sets. Hence
$$U^{-1} = \{u^{-1} : u \in U\} = J(U)$$
is open in $G$.

For each fixed $a \in A$, left translation $x \mapsto ax$ and right translation $x \mapsto xa$ are homeomorphisms (Theorem 2.8), so $aU = \{au : u \in U\}$ and $Ua = \{ua : u \in U\}$ are open sets. Now:
$$AU = \bigcup_{a \in A} aU, \qquad UA = \bigcup_{a \in A} Ua.$$
Each $aU$ is open, and an arbitrary union of open sets is open; therefore $AU$ and $UA$ are open in $G$. $\square$
