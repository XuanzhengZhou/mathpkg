---
role: proof
locale: en
of_concept: component-of-open-subset-is-open
source_book: gtm027
source_chapter: "1"
source_section: "S. Locally Connected Spaces"
---

# Proof of Component of an Open Subset of a Locally Connected Space is Open

Let $X$ be a locally connected topological space and let $U$ be an open subset of $X$. Let $C$ be a component of $U$ (with respect to the subspace topology on $U$).

For each point $x \in C$, $U$ is a neighborhood of $x$ (since $U$ is open and $x \in C \subseteq U$). Because $X$ is locally connected, the component of $U$ to which $x$ belongs is a neighborhood of $x$. But the component of $U$ containing $x$ is precisely $C$, since $C$ is a component of $U$. Hence $C$ is a neighborhood of each of its points.

For each $x \in C$, there exists an open set $V_x \subseteq X$ such that $x \in V_x \subseteq C$. Then

$$C = \bigcup_{x \in C} V_x$$

is a union of open sets and therefore open in $X$. Consequently, $C$ is also open in the subspace topology on $U$.

$\square$
