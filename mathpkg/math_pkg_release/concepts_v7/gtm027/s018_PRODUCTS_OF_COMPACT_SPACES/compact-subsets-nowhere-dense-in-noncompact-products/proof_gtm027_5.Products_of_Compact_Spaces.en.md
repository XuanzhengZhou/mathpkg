---
role: proof
locale: en
of_concept: compact-subsets-nowhere-dense-in-noncompact-products
source_book: gtm027
source_chapter: "5"
source_section: "Products of Compact Spaces"
---

# Proof: Compact Subsets are Nowhere Dense in Products of Infinitely Many Non-Compact Spaces

**Theorem.** If an infinite number of the coordinate spaces are non-compact, then each compact subset of the product is nowhere dense.

*Proof.* Suppose $\prod \{X_a : a \in A\}$ has a compact subset $B$ with an interior point $x$. Then $B$ contains a neighborhood $U$ of $x$ which is a member of the defining base for the product topology. Such a basic neighborhood is of the form

$$U = \bigcap \{P_a^{-1}[V_a] : a \in F\},$$

where $F$ is a finite subset of $A$ and each $V_a$ is an open subset of $X_a$. Equivalently, $U = \prod_{a \in A} U_a$ where $U_a = V_a$ for $a \in F$ and $U_a = X_a$ for $a \notin F$. For each index $a \notin F$, the projection $P_a[U] = X_a$. Since $U \subset B$, we have $X_a = P_a[U] \subset P_a[B] \subset X_a$, so $P_a[B] = X_a$. The projection $P_a$ is continuous, and the continuous image of a compact set is compact; therefore $X_a = P_a[B]$ is compact for every $a \notin F$.

The set $F$ is finite, yet by hypothesis infinitely many of the coordinate spaces $X_a$ are non-compact. This is a contradiction. Hence no compact subset of the product can have an interior point; that is, the closure of every compact subset has void interior. Therefore each compact subset of the product is nowhere dense. $\square$
