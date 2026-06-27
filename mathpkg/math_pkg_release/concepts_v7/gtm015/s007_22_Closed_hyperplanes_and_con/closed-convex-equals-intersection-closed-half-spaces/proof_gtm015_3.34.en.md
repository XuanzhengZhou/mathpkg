---
role: proof
locale: en
of_concept: closed-convex-equals-intersection-closed-half-spaces
source_book: gtm015
source_chapter: "3"
source_section: "34"
---

# Proof of Closed convex set equals intersection of closed half-spaces containing it

If $E$ is a locally convex TVS over $\mathbb{R}$ and $A$ is a nonempty closed convex set in $E$, then $A$ is the intersection of the family of all topologically closed half-spaces that contain it.

In view of Definition (30.1), given any $b \notin A$ we seek a continuous linear form $g$ and a real number $\beta$ such that $g \le \beta$ on $A$ and $g(b) > \beta$. Since $B = \{b\}$ is a compact convex set disjoint from the closed convex set $A$, applying (34.1) yields the existence of a continuous linear form $g$ and a real number $\beta$ with $g \le \beta$ on $A$ and $g(b) > \beta$. (In fact, (34.1) gives strict inequality: $g < \beta$ on $A$, $g(b) > \beta$.)

Thus the closed half-space $\{x : g(x) \le \beta\}$ contains $A$ but not $b$, proving the result.
