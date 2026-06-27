---
role: proof
locale: en
of_concept: inverse-function-theorem
source_book: gtm051
source_chapter: "0"
source_section: "0.5"
---

The proof of the Inverse Function Theorem relies on the Banach fixed-point theorem (contraction mapping principle). Consider the map $\Phi_x(y) = y - (dF_0)^{-1}(F(x + y) - F(x))$. For $x$ sufficiently close to $0$, this map is a contraction on a small ball around $0$, and its unique fixed point gives the local inverse. The differentiability of the inverse follows from the formula $(F^{-1})'(y) = (F'(F^{-1}(y)))^{-1}$.

More precisely: by translating, we may assume $F(0) = 0$ and $dF_0 = \text{id}$. Define $G(x) = x - F(x)$, so $dG_0 = 0$. By continuity of $dG$, there exists $r > 0$ such that $\|dG_x\| \leq 1/2$ for $\|x\| \leq r$. For any $y$ with $\|y\| \leq r/2$, the map $T_y(x) = y + G(x)$ is a contraction on the closed ball $\overline{B}_r(0)$, since $\|T_y(x_1) - T_y(x_2)\| = \|G(x_1) - G(x_2)\| \leq \frac{1}{2}\|x_1 - x_2\|$ by the mean value inequality. The fixed point $x$ satisfies $x = y + x - F(x)$, i.e., $F(x) = y$, so $F$ is surjective onto $B_{r/2}(0)$ and injective on $B_r(0)$. The inverse is continuous, and by the chain rule, differentiable.
