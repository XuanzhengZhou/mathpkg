---
role: proof
locale: en
of_concept: baires-theorem-category-form
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC SPACES ONLY"
---

# Proof of Baire's Theorem (Category Form)

**Theorem.** The complement of a meager subset of a complete metric space is dense; equivalently, a complete metric space is not the union of a countable family of nowhere dense sets.

**Proof.** Recall that a subset $A$ of a topological space $X$ is *nowhere dense* iff the interior of its closure is void, and $A$ is *meager* (or of the first category) iff $A$ is the union of a countable family of nowhere dense sets.

Let $X$ be a complete metric space and let $A$ be a meager subset of $X$. We must show that $X \setminus A$ is dense, or equivalently, that no non-void open set is contained in $A$.

Let $\mathcal{U}$ be a disjoint family of open sets which is maximal with respect to the property: if $U \in \mathcal{U}$, then $U \cap A$ is meager. Such a family $\mathcal{U}$ exists because of the maximal principle (0.25). Let $W = \bigcup \{U : U \in \mathcal{U}\}$.

The proof reduces to showing that $W \cap A$ is meager, for if this is known then $A \cap W^{-}$ is meager because $W^{-} \setminus W$ is nowhere dense, and from the maximality of $\mathcal{U}$ it follows that $W^{-}$ contains every open set $V$ such that $V \cap A$ is meager.

To show that $W \cap A$ is meager, for each $U$ in $\mathcal{U}$ write $U \cap A$ in the form $\bigcup \{U_n : n \in \omega\}$ where each $U_n$ is nowhere dense. Then, because the family $\mathcal{U}$ is disjoint, the set $\bigcup \{U_n : U \in \mathcal{U}\}$ is nowhere dense for each non-negative integer $n$. Hence

$$W \cap A = \bigcup_{n \in \omega} \bigcup_{U \in \mathcal{U}} U_n$$

is a countable union of nowhere dense sets, and therefore is meager.

Consequently, if $X$ were meager, taking $A = X$ in the above argument would yield a contradiction (since $X$ is open and $X \cap X = X$ is meager, but $X$ contains open sets that are not meager unless $X$ is empty). Thus $X$ cannot be meager, and the complement of any meager set intersects every non-void open set, i.e., is dense. This completes the proof.
