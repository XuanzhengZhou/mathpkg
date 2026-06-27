---
role: proof
locale: en
of_concept: separable-implies-countable-chain-condition
source_book: gtm027
source_chapter: "1"
source_section: "N"
---

# Proof that Separable Spaces Satisfy the Countable Chain Condition

**Theorem.** A separable space satisfies the countable chain condition (ccc), but the converse does not hold.

*Proof.*

## Part 1: Separable $\implies$ CCC

Let $X$ be a separable topological space, so there exists a countable dense subset $D \subseteq X$.

Let $\mathcal{U} = \{U_\alpha : \alpha \in I\}$ be a family of pairwise disjoint, nonempty open sets. We must show $\mathcal{U}$ is countable.

Since $D$ is dense, each $U_\alpha$ intersects $D$: pick $d_\alpha \in D \cap U_\alpha$. Since the $U_\alpha$ are pairwise disjoint, the points $d_\alpha$ are distinct for distinct $\alpha$. Thus the map $\alpha \mapsto d_\alpha$ is an injection from the index set $I$ into the countable set $D$. Hence $I$ is countable, and $\mathcal{U}$ is a countable family.

## Part 2: CCC $\not\implies$ Separable (counterexample)

Consider an uncountable set $X$ with the co-countable topology: the open sets are $\emptyset$ and all subsets of $X$ whose complement is countable.

**$X$ is CCC:** Suppose $\{U_\alpha\}$ is a disjoint family of nonempty open sets. Each $U_\alpha$ has a countable complement. If the family were uncountable, then picking $x_\alpha \in U_\alpha$, the set $\{x_\alpha\}$ would be uncountable. But its complement would contain all $U_\beta$ for $\beta \neq \alpha$, which has countable complement — a contradiction. More directly: in the co-countable topology, any two nonempty open sets must intersect (their complements are countable, so the intersection of two co-countable sets on an uncountable $X$ is nonempty). Thus there cannot be two disjoint nonempty open sets, let alone uncountably many. So $X$ satisfies CCC trivially.

**$X$ is not separable:** Any countable subset $C \subseteq X$ is closed (its complement is co-countable, hence open... wait, in co-countable topology, countable sets are closed). The closure of $C$ is $C$ itself (since $C$ is closed). Since $C$ is a proper subset of the uncountable $X$, $C$ is not dense. Thus no countable subset can be dense, so $X$ is not separable.

## Additional Remarks

The Helly space (see Problem 5.M of Kelley) satisfies the first countability axiom and is separable, but fails to satisfy the second axiom of countability. There are more subtle examples of spaces that satisfy CCC but are not separable. $\square$
