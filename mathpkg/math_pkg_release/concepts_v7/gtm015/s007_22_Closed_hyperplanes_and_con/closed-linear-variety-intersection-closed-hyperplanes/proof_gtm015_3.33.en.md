---
role: proof
locale: en
of_concept: closed-linear-variety-intersection-closed-hyperplanes
source_book: gtm015
source_chapter: "3"
source_section: "33"
---

# Proof of Closed linear variety is intersection of all closed hyperplanes containing it

We can suppose, by translation, that $\theta \in M$, i.e., that $M$ is a closed linear subspace of $E$. In view of (22.4), the theorem may be reformulated thus: assuming $a \notin M$, we seek a continuous linear form $f$ on $E$ such that $f = 0$ on $M$ and $f(a) \neq 0$.

Since $M$ is closed and $a \notin M$, there exists a neighborhood $A$ of $a$ with $A \cap M = \varnothing$. We can suppose $A$ is convex (by local convexity). Then the interior $\operatorname{int} A$ of $a$ is also convex (25.20), so we can suppose $A$ is open.

By the geometric form of the Hahn-Banach theorem ((28.4) if $\mathbb{K} = \mathbb{R}$, or (28.5) if $\mathbb{K} = \mathbb{C}$), there exists a continuous linear form $f$ on $E$ such that $f = 0$ on $M$ and $f$ is never $0$ on $A$ — in particular, $f(a) \neq 0$. Thus $a$ does not belong to the intersection of all closed hyperplanes containing $M$, proving that $M$ is exactly that intersection.
