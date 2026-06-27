---
role: proof
locale: en
of_concept: hahn-banach-via-seminorms
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Alternative proof of the Hahn-Banach theorem via seminorms and convex separation

Suppose $E$ is a vector space over $\mathbb{K}$, $p$ is a seminorm on $E$, $M$ is a linear subspace of $E$, and $g$ is a linear form on $M$ such that $|g(y)| \leq p(y)$ for all $y \in M$. We seek a linear form $f$ on $E$ such that $f|_M = g$ and $|f(x)| \leq p(x)$ for all $x \in E$.

We can suppose $g \neq 0$. As in the proof of (28.8), it is sufficient to consider the case that $\mathbb{K} = \mathbb{R}$.

Equip $E$ with the locally convex topology $\tau_p$ and let $A = \{x : p(x) < 1\}$; since $p$ is continuous for $\tau_p$ (37.5), $A$ is an open, nonempty convex set. If $y \in M$ and $g(y) = 1$, then $p(y) \geq |g(y)| = 1$, therefore $y \notin A$. Thus, setting $N = \{y \in M : g(y) = 1\}$, $N$ is a linear variety (in $M$, therefore in $E$) such that $N \cap A = \varnothing$.

By the 'geometric form' of the Hahn-Banach theorem (28.1), there exists a closed hyperplane $H$ in $E$ such that $H \supset N$ and $H \cap A = \varnothing$. Let $f$ be a linear form on $E$ such that $H = \{x : f(x) = 1\}$. Then $f$ vanishes on the linear subspace parallel to $H$, and from $H \supset N$ we deduce $f|_M = g$. From $H \cap A = \varnothing$ and the convexity of $A$, one obtains $|f(x)| \leq p(x)$ for all $x \in E$.
