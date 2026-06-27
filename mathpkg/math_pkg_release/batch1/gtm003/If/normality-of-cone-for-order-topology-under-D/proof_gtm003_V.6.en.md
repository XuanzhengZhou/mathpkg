---
role: proof
locale: en
of_concept: normality-of-cone-for-order-topology-under-D
source_book: gtm003
source_chapter: "V"
source_section: "6"
---

By definition of the inductive limit topology, a $0$-neighborhood base for $\mathfrak{T}_O$ is given by all convex radial subsets $U$ of $L$ such that $V = U \cap (C - C)$ is of the form $V = \Gamma\{\rho_a[-a, a] : a \in H\}$, where $a \mapsto \rho_a$ is any mapping of $H$ into the positive reals.

We prove normality of $C$ via criterion (3.1)(c): if $x \in U$ and $y \in [0, x]$, then $y \in U$. Suppose $x \in U$ with $x \geq 0$. Then $x = \sum_{i=1}^{n} \lambda_i z_i$ where $\sum_{i=1}^{n} |\lambda_i| \leq 1$ and $z_i \in \rho_{a_i}[-a_i, a_i]$.

If $y \in [0, x]$, then $y \leq \sum_{i=1}^{n} |\lambda_i| \rho_{a_i} a_i$. By repeated application of condition (D) (the Riesz decomposition property), we obtain $y = \sum_{i=1}^{n} |\lambda_i| y_i$ where $y_i \in \rho_{a_i}[0, a_i]$. Hence $y \in V \subset U$, proving normality.

Since $C$ is normal, the dual of $(L, \mathfrak{T}_O)$ is $L^b = L^+$ by the regularity of the order.
