---
role: proof
locale: en
of_concept: semidefinite-with-zero-value-is-degenerate
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Consider a vector $x_0 \neq 0$ such that $\Phi(x_0) = \Phi(x_0, x_0) = 0$. By the Schwarz inequality for positive semidefinite bilinear functions, we have for all $y \in E$:

$$\Phi(x_0, y)^2 \leq \Phi(x_0) \Phi(y) = 0 \cdot \Phi(y) = 0.$$

Hence $\Phi(x_0, y)^2 \leq 0$, which forces $\Phi(x_0, y) = 0$ for every $y \in E$. By definition of the nullspace, this means $x_0 \in E_0$. Since $x_0 \neq 0$, the nullspace $E_0$ is nontrivial, so $\Phi$ is degenerate.
