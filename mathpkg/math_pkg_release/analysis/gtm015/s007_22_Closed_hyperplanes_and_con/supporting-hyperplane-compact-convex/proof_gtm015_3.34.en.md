---
role: proof
locale: en
of_concept: supporting-hyperplane-compact-convex
source_book: gtm015
source_chapter: "3"
source_section: "34"
---

# Proof of Existence of supporting hyperplanes for compact convex sets in locally convex spaces

Let $E$ be a locally convex, separated TVS over $\mathbb{R}$, let $A$ be a nonempty compact convex subset of $E$, and let $b \notin A$. Then there exist a continuous linear form $g$ on $E$ and a real number $\alpha$ such that $g \le \alpha$ on $A$, $g(a) = \alpha$ for at least one $a \in A$, and $g(b) > \alpha$.

Since $A$ is compact and $\{b\}$ is compact, and they are disjoint convex sets, by (34.1) there exist a continuous linear form $g$ and a real number $\alpha$ with $g \le \alpha$ on $A$ and $g(b) > \alpha$.

Since $A$ is compact, the continuous function $g$ attains its maximum on $A$. Let $\alpha$ be this maximum value. Then $g \le \alpha$ on $A$ with equality at some point, $g(b) > \alpha$, and $H = \{x : g(x) = \alpha\}$ is a supporting hyperplane.
