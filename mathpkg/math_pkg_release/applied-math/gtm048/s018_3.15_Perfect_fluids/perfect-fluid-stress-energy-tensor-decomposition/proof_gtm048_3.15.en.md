---
role: proof
locale: en
of_concept: perfect-fluid-stress-energy-tensor-decomposition
source_book: gtm048
source_chapter: "3"
source_section: "3.15"
---

Fix $z \in M$ and let $(z, Z)$ be an instantaneous observer for whom $T$ is spatially isotropic. By Exercise 2.1.12,

$$\hat{T}z = a Z \otimes Z + b \hat{h},$$

where $a, b \in \mathbb{R}$ and $\hat{h}$ is physically equivalent to the projection tensor (Section 2.1.5). On the other hand, Section 3.5.1 gives:

$$\hat{T} = \sum_A \eta_A P_A \otimes P_A.$$

Comparing the two expressions at $z$:

$$\sum_A \eta_A P_A \otimes P_A = a Z \otimes Z + b \hat{h}.$$

Therefore $Z = Z_z$ by uniqueness of the eigenvector decomposition. Since this holds for all $z \in M$, the expression for $\hat{T}z$ implies

$$\hat{T} = \rho Z \otimes Z + p(\hat{g} + Z \otimes Z),$$

where $\rho$ and $p$ are the (not necessarily $C^\infty$) functions on $M$ such that, in the preceding notation, $\rho(z) = a$ and $p(z) = b$ at each $z \in M$.

Since $\hat{T}Z = -\rho Z$, the quantity $-\rho$ is the eigenfunction of $\hat{T}$ corresponding to $Z$ and is therefore $C^\infty$. Since $\operatorname{trace} T = -\rho + 3p$, the combination $(-\rho + 3p)$ is also $C^\infty$, and hence so is $p$.

The inequalities for $a$ and $b$ (coming from the quasi-gas assumptions and Exercise 2.1.12) now give: $\rho > 0$, $\rho \geq 3p \geq 0$, and $\rho = 3p$ iff $m_A = 0$ for all $A = 1, \ldots, N$. This proves part (b).

This also proves that in part (c), (1) $\Leftrightarrow$ (3): if $\rho(z) = 3p(z)$ at some $z$, then $a = 3b$ at that point, which implies $m_A = 0$ for all $A$, hence (3). And (3) $\Rightarrow$ (1) is immediate from the characterization of $\rho = 3p$. The implication (2) $\Rightarrow$ (1) is trivial. If (1) holds, then in our notation $a = 3b$, which implies $m_A = 0$ for all $A$, hence (3). So (1) $\Rightarrow$ (3) $\Rightarrow$ (2), completing the cycle of equivalences.

Part (a) — that $\hat{T}$ is normal — follows from the fact that its decomposition $\hat{T} = \rho Z \otimes Z + p(\hat{g} + Z \otimes Z)$ satisfies the normality condition (each term commutes with the metric structure in the appropriate sense).
