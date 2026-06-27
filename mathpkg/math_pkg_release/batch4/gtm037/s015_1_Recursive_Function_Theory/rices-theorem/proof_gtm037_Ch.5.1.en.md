---
role: proof
locale: en
of_concept: rices-theorem
source_book: gtm037
source_chapter: "5"
source_section: "1. Recursive Function Theory"
---

Suppose $A = \{e : \varphi^1_e \in F\}$ is recursive. Let $a \in A$ and $b \notin A$. Now define

$$g(x) = \begin{cases}
a & \text{if } x \notin A,\\
b & \text{if } x \in A.
\end{cases}$$

Then $g$ is recursive. By the fixed-point theorem (5.16), choose $e$ such that $\varphi^1_e = \varphi^1_{g(e)}$.

If $e \in A$, then $\varphi^1_e \in F$ (by definition of $A$), hence $\varphi^1_{g(e)} \in F$, so $g(e) \in A$. But $e \in A$ also implies $g(e) = b \notin A$, a contradiction.

If $e \notin A$, then $\varphi^1_e \notin F$ and $\varphi^1_{g(e)} \notin F$, so $g(e) \notin A$. But $e \notin A$ implies $g(e) = a \in A$, also a contradiction.

Thus $A$ cannot be recursive.
