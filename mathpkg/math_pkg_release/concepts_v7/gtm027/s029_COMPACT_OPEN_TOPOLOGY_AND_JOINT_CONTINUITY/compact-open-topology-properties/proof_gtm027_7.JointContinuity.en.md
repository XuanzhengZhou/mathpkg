---
role: proof
locale: en
of_concept: compact-open-topology-properties
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Theorem 7.4 — Properties of the Compact-Open Topology

The compact-open topology $\mathcal{C}$ on $F$ has as a subbase all sets of the form $W(K, U) = \{f \in F : f[K] \subset U\}$ where $K$ is a compact subset of $X$ and $U$ is an open subset of $Y$.

**$\wp \subset \mathcal{C}$:** For each $x \in X$ and each open subset $U \subset Y$, the set $W(\{x\}, U) = \{f : f(x) \in U\}$ belongs to $\mathcal{C}$ because the singleton $\{x\}$ is compact. Since the family of all such sets forms a subbase for the pointwise topology $\wp$, we have $\wp \subset \mathcal{C}$.

**(Hausdorff):** If $Y$ is Hausdorff, then $(F, \wp)$ is Hausdorff by Theorem 3.5 (product of Hausdorff spaces is Hausdorff). Since $\wp \subset \mathcal{C}$, any disjoint $\wp$-neighborhoods of two distinct members of $F$ are also $\mathcal{C}$-neighborhoods. Hence $(F, \mathcal{C})$ is Hausdorff.

**(Regular):** Assume $Y$ is regular and the members of $F$ are continuous. To show $(F, \mathcal{C})$ is regular, it suffices to prove that each subbasic neighborhood of each $f \in F$ contains a closed neighborhood. Suppose $f \in W(K, U)$ with $K$ compact and $U$ open in $Y$. Then $f[K]$ is compact, and since $Y$ is regular, by Theorem 5.10 there exists a closed neighborhood $V$ of $f[K]$ with $V \subset U$. Clearly $f \in W(K, V) \subset W(K, U)$. It remains to show $W(K, V)$ is closed. Indeed, $W(K, V) = \bigcap_{x \in K} \{f : f(x) \in V\}$, and each factor $\{f : f(x) \in V\}$ is closed in the pointwise topology (hence in $\mathcal{C}$), making $W(K, V)$ closed.
