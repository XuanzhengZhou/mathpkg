---
role: proof
locale: en
of_concept: normality-under-condition-D
source_book: gtm003
source_chapter: "V. Order Structures"
source_section: "6. The Order Topology"
---

By definition of the topology of inductive limit, a $0$-neighborhood base for $\mathfrak{T}_0$ is given by the family of all convex radial subsets $U$ of $L$ such that $V = U \cap (C - C)$ is of the form $V = \prod \{\rho_a[-a, a] : a \in H\}$, where $a \mapsto \rho_a$ is any mapping of $H$ into the set of real numbers $> 0$.

We prove the normality of $C$ via criterion (3.1)(c) by showing that $x \in U$ and $y \in [0, x]$ imply $y \in U$. If $x \in U$ and $x \geq 0$, then $x$ is of the form $x = \sum_{i=1}^{n} \lambda_i z_i$, where $\sum_{i=1}^{n} |\lambda_i| \leq 1$ (with $\lambda_i \in \mathbb{R}$) and $z_i \in \rho_{a_i}[-a_i, a_i]$ for $i = 1, \ldots, n$.

If $y \in [0, x]$, then $y \leq \sum_{i=1}^{n} |\lambda_i| \rho_{a_i} a_i$. By repeated application of condition (D), we obtain $y = \sum_{i=1}^{n} |\lambda_i| y_i$, where $y_i \in \rho_{a_i}[0, a_i]$ for $i = 1, \ldots, n$. Hence $y \in V \subset U$, as was to be shown.

The statement about the dual follows from Theorem 6.1 and the fact that when $C$ is normal, $L^b = L^+$.
