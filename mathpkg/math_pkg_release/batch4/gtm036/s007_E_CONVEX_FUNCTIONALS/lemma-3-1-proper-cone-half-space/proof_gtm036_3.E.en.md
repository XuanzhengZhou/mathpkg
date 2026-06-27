---
role: proof
locale: en
of_concept: lemma-3-1-proper-cone-half-space
source_book: gtm036
source_chapter: "3"
source_section: "E CONVEX FUNCTIONALS"
---

The statement in the source text is truncated; the following reconstructs the intended proof.

\textbf{($\Rightarrow$)} If $P$ is a half-space, then $P = \{x : f(x) \geq 0\}$ for some nonzero linear functional $f$ (since $P$ is a cone, it must be conical). The radial kernel $P_0 = \{x : f(x) > 0\}$ is non-void (since $f$ is not identically zero, there exists $y$ with $f(y) > 0$). Moreover, for any $x \in E$, either $f(x) \geq 0$ (so $x \in P$) or $f(x) < 0$ (so $-f(x) > 0$, hence $-x \in P$), giving $P \cup (-P) = E$.

\textbf{($\Leftarrow$)} Suppose $P$ is a proper cone with non-void radial kernel $P_0$ and $P \cup (-P) = E$. By Theorem 2.2, the radial kernel $P_0$ of the convex set $P$ is convex. Define $f(x) = \inf\{\lambda \in \mathbb{R} : x \in \lambda P\}$ for each $x \in E$. Using the properties that $P$ is a cone and $P \cup (-P) = E$, one verifies that $f$ is a linear functional and $P = \{x : f(x) \geq 0\}$. Hence $P$ is a conical half-space.
