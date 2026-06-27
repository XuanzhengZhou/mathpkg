---
role: proof
locale: en
of_concept: subdifferentiability-theorem
source_book: gtm024
source_chapter: "I"
source_section: "§6. Alternate Formulations of the Separation Principle"
---

Let $f$ be a convex function on a convex set $A \subset X$ and let $x_0 \in \operatorname{cor}(A)$. Consider the epigraph $\operatorname{epi}(f) = \{(x, t) \in X \times \mathbb{R} : f(x) \leqslant t\}$, which is a convex set in $X \times \mathbb{R}$ with $(x_0, f(x_0))$ in its boundary. By the basic separation theorem, there exists a non-zero linear functional $(\phi, \alpha) \in (X \times \mathbb{R})'$ separating $\operatorname{epi}(f)$ from the point $(x_0, f(x_0) - 1)$. Normalizing so that $\alpha = -1$ (possible since $f$ is finite near $x_0$), we obtain $\phi \in X'$ such that $f(x) \geqslant f(x_0) + \phi(x - x_0)$ for all $x \in A$. Thus $\phi$ is a subgradient of $f$ at $x_0$, proving that the subdifferential $\partial f(x_0)$ is nonempty.
