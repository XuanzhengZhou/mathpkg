---
role: exercise
locale: en
chapter: "Problems"
section: "I"
exercise_number: 1
of_concept: separate-versus-joint-continuity
source_book: gtm027
---

# Exercise I.1 — Separate Continuity versus Joint Continuity

Let $X$ and $Y$ be topological spaces and let $f$ be a function on $X \times Y$. Then $f(x,y)$ is continuous in $x$ iff for each $y$ the function $f(\cdot,y)$ whose value at $x$ is $f(x,y)$, is continuous. Similarly, $f(x,y)$ is continuous in $y$ iff for each $x \in X$, the function $f(x,\cdot)$ such that $f(x,\cdot)(y) = f(x,y)$, is continuous. If $f$ is continuous on the product space, then $f(x,y)$ is continuous in $x$ and in $y$, but the converse is false.

(The classical example is the real-valued function $f$ on the Euclidean plane such that $f(x,y) = xy/(x^2 + y^2)$ and $f(0,0) = 0$.)
