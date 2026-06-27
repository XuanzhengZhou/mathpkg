---
role: proof
locale: en
of_concept: non-hausdorff-spaces-theorem
source_book: gtm036
source_chapter: "5"
source_section: "5.11"
---

Because a linear topological space is necessarily regular, it is Hausdorff if and only if $\{0\}$ is closed.

Let $F = \{0\}^{-}$. Then $F$ is a linear subspace of $E$ (as the closure of a subspace). By the existence of complementary subspaces in linear spaces (using Zorn's lemma), there exists a subspace $G$ of $E$ complementary to $F$, so that $E = G \oplus F$ algebraically.

The relative topology for $F$ is the trivial topology: only $F$ and the empty set are open. Indeed, any nonempty open set in $F$ must contain 0 (being a neighborhood in a linear topological space), but the only open sets containing 0 in $E$ intersect $F$ in all of $F$, because every neighborhood of 0 is dense in $F = \{0\}^{-}$.

The relative topology for $G$ is Hausdorff. To see this, it suffices to show $\{0\}$ is closed in $G$. Observe that $\{0\} = G \cap \{0\}^{-}$: the point 0 in $G$ is the intersection of $G$ with $F = \{0\}^{-}$. Since $\{0\}^{-} = F$ is closed in $E$, the singleton $\{0\}$ is closed in the relative topology of $G$. Because $G$ as a linear topological space is regular, it follows that $G$ is Hausdorff.

Now consider the linear projection $P: E \to F$ with null space $G$. Since every linear function to a space with the trivial topology is continuous (the inverse image of the unique nonempty open set is all of $E$), $P$ is continuous. $P$ is clearly a projection (idempotent) because $F$ is the range.

By the Lemma on Projections (5.10), $E$ is topologically isomorphic to $F \times G$ (where the order of factors is immaterial) under the map $x \mapsto (P(x), x - P(x))$. Here $G = \ker P$ has the Hausdorff relative topology, and $F = \operatorname{ran} P$ has the trivial topology.
