---
role: proof
locale: en
of_concept: self-adjoint-spectrum-is-real
source_book: gtm003
source_chapter: "VI"
source_section: "2"
---

Suppose $\lambda = a + ib \in \sigma(x)$ with $b \neq 0$. Then $a e - x + ib e$ is not invertible. Consider $\|(a e - x + it e)y\|^2$ for $t \in \mathbf{R}$. Running a variant of the standard proof: since $x$ is self-adjoint, $\|(x - \lambda e)y\| \geq |\operatorname{Im}(\lambda)| \|y\|$ for all $y$ (by expanding the C*-identity). If $\operatorname{Im}(\lambda) \neq 0$, this gives a lower bound, implying invertibility via the Neumann series—contradiction. For the second claim, if $\lambda \in \mathbf{R} \cap \rho(x)$, then $(\lambda e - x)^{-1}$ commutes with the involution, since $(\lambda e - x)^* = \lambda e - x$ (self-adjointness of $x$).
