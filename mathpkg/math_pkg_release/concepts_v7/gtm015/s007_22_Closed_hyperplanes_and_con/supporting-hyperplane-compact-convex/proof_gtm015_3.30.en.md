---
role: proof
locale: en
of_concept: supporting-hyperplane-compact-convex
source_book: gtm015
source_chapter: "3"
source_section: "30"
---

# Proof of Existence of supporting hyperplanes for compact convex sets

Let $E$ be a real TVS and let $A$ be a nonempty compact convex subset of $E$.

(1) Every tangent hyperplane to $A$ is closed: by definition a tangent hyperplane is of the form $H = \{x : g(x) = \alpha\}$ where $g$ is a linear form and $g \ge \alpha$ (or $g \le \alpha$) on $A$, with equality attained at some boundary point. Since $A$ is compact and $g$ achieves its extremum, by (22.2) the hyperplane is closed iff the corresponding linear form is continuous. But any linear form attaining its maximum on a neighborhood of a point is continuous (the tangent hyperplane argument).

(2) If $z \notin A$ and $z$ is in the convex hull of $A$: Let $a \in \operatorname{int} A$ (if interior is empty, replace by affine hull). Consider $\varphi(\beta) = (1-\beta)a + \beta z$, and let $\beta_0 = \sup\{\beta : \varphi(\beta) \in A\}$. Then $b = \varphi(\beta_0)$ is a boundary point. By (30.11) applied to $A$ and a supporting hyperplane at $b$, there exists a closed hyperplane $H$ tangent to $A$ at $b$ such that $z$ lies in the open half-space opposite to $A$.

(3) For general $z \notin A$: The problem is solved by finding a suitable boundary point and applying (2), yielding a separating closed hyperplane.
