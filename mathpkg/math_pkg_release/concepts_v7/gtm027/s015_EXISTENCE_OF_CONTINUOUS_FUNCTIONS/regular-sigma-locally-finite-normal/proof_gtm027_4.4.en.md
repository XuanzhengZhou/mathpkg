---
role: proof
locale: en
of_concept: regular-sigma-locally-finite-normal
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Regular Space with Sigma-Locally Finite Base is Normal

**Lemma 19.** A regular space whose topology has a $\sigma$-locally finite base is normal.

*Proof.* If $A$ and $B$ are disjoint closed subsets of the space $X$, then there are open covers $\mathcal{U}$ and $\mathcal{V}$ of $A$ and $B$ respectively such that the closure of each member of $\mathcal{U}$ is disjoint from $B$, the closure of each member of $\mathcal{V}$ is disjoint from $A$, and both $\mathcal{U}$ and $\mathcal{V}$ are subfamilies of a $\sigma$-locally finite base $\mathcal{B}$.

Write $\mathcal{U} = \bigcup \{\mathcal{U}_n : n \in \omega\}$ and $\mathcal{V} = \bigcup \{\mathcal{V}_n : n \in \omega\}$ where $\mathcal{U}_n$ and $\mathcal{V}_n$ are locally finite families. Let

$$U_n = \bigcup \{W : W \in \mathcal{U}_n\}, \quad V_n = \bigcup \{W : W \in \mathcal{V}_n\}.$$

Because each $\mathcal{U}_n$ is locally finite, $U_n^{-} = \bigcup \{W^{-} : W \in \mathcal{U}_n\}$ and similarly for $V_n^{-}$. Now define

$$U = \bigcup_{n \in \omega} \left( U_n \sim \bigcup_{k \leq n} V_k^{-} \right), \quad V = \bigcup_{n \in \omega} \left( V_n \sim \bigcup_{k \leq n} U_k^{-} \right).$$

Then $U$ and $V$ are open sets (difference of an open set and a closed set), $A \subset U$, $B \subset V$, and $U \cap V = \emptyset$. This proves $X$ is normal.

