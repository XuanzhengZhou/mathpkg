---
role: proof
locale: en
of_concept: open-set-neighborhood-criterion
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof of Open Set Neighborhood Criterion

**Theorem.** A set $A$ in a topological space $(X, \mathfrak{J})$ is open if and only if $A$ contains a neighborhood of each of its points.

*Proof.* Let $U$ be the union of all open subsets of $A$. Then $U$ is an open subset of $A$, since the union of any family of open sets is open.

Suppose $A$ contains a neighborhood of each of its points. Then for each $x \in A$, there exists an open set $V_x$ such that $x \in V_x \subseteq A$. Hence each $x \in A$ belongs to some open subset of $A$, and therefore $x \in U$. This shows $A \subseteq U$. Since $U \subseteq A$ by definition, we have $A = U$, and consequently $A$ is open.

Conversely, if $A$ is open, then $A$ itself is an open set containing $x$ and contained in $A$, for each $x \in A$. Thus $A$ is a neighborhood of each of its points. $\square$

**Corollary.** A set is open if and only if it is a neighborhood of each of its points.
