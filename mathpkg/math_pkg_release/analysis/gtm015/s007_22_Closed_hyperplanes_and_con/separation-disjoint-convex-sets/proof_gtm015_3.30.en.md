---
role: proof
locale: en
of_concept: separation-disjoint-convex-sets
source_book: gtm015
source_chapter: "3"
source_section: "30"
---

# Proof of Separation of disjoint convex sets by a closed hyperplane

Let $E$ be a real TVS, $A$ and $B$ nonempty convex sets with $A \cap B = \varnothing$, and suppose $A$ is open.

Let $D$ be the set of all differences $a - b$ ($a \in A, b \in B$). Since $A$ is open, so is $D = \bigcup_{b \in B} A + (-b)$; moreover, since $A$ and $-B$ are convex, so is $D = A + (-B)$ (25.10). The condition $A \cap B = \varnothing$ means that $\theta \notin D$.

Thus $D$ is a nonempty, open convex set disjoint from the linear subspace $M = \{\theta\}$. By Corollary (28.4) of the geometric form of the Hahn-Banach theorem, there exists a continuous linear form $g$ such that $g > 0$ on $D$, that is, $g(a) > g(b)$ for all $a \in A, b \in B$. Setting $\alpha = \sup_{b \in B} g(b)$, the hyperplane $H = \{x : g(x) = \alpha\}$ separates $A$ and $B$.

(1) $H$ separates $A$ and $B$ by construction.
(2) $A$ lies strictly to one side: since $g(A)$ is open in $\mathbb{R}$ (as $g$ is open on the open set $A$) and $g(A) \subset (\alpha, \infty)$, we have $g(x) > \alpha$ for all $x \in A$.
(3) If $B$ is also open, then $g(B)$ is also open and $g(B) \subset (-\infty, \alpha)$, so $g(x) < \alpha$ for all $x \in B$, giving strict separation.
