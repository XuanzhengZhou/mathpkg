---
role: proof
locale: en
of_concept: theta-homeomorphism-sphere-to-stiefel-v1
source_book: gtm020
source_chapter: "16"
source_section: "9"
---

We have
\[
\theta(\{x, -x\})e_n = e_n - 2(x \mid e_n)x = e_n - 2x_n x = (-2x_1 x_n, \ldots, -2x_{n-1} x_n, 1 - x_n^2).
\]

If $y = (y_1, \ldots, y_n) \in S^{n-1}$ and $y_n \neq 1$, there is a unique $x$ with $x_n > 0$ such that $\theta(\{x, -x\})e_n = y$. Specifically, from the formula above, one can solve for $x$ explicitly. The components satisfy
\[
y_i = -2x_i x_n \quad (1 \leq i \leq n-1), \qquad y_n = 1 - 2x_n^2.
\]
Since $y_n \neq 1$, we have $x_n^2 = (1 - y_n)/2 \neq 0$, and the condition $x_n > 0$ singles out a unique solution. Then $x_i = -y_i/(2x_n)$ for $1 \leq i \leq n-1$ is uniquely determined.

For $x_n = 0$, we have $\theta(\{x, -x\})e_n = (0, \ldots, 0, 1)$, which corresponds to the point at infinity in the stereographic projection.

Thus $\theta$ is bijective. Since $\theta$ is induced by the continuous action of $O(n)$ and the domain $\mathbf{R}P^{n-1}/\mathbf{R}P^{n-2}$ is compact while the codomain $S^{n-1}$ is Hausdorff, $\theta$ is a homeomorphism.
