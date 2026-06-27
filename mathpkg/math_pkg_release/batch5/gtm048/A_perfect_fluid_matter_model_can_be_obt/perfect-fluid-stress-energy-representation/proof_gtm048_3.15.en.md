---
role: proof
locale: en
of_concept: perfect-fluid-stress-energy-representation
source_book: gtm048
source_chapter: "3"
source_section: "3.15"
---

**Proof.** Fix a $z \in M$ and let $(z, Z)$ be an instantaneous observer for whom $\hat{T}$ is spatially isotropic. By Exercise 2.1.12,

$$\hat{T}_z = a Z \otimes Z + b \hat{h},$$

where $a, b \in \mathbb{R}$ and $\hat{h}$ is physically equivalent to the projection tensor (Section 2.1.5). On the other hand, Section 3.5.1 gives:

$$\hat{T} = \sum \eta_A P_A \otimes P_A.$$

Comparing these two expressions for $\hat{T}_z$ at $z$ yields the relationship between the parameters. Therefore $Z = Z_z$ by uniqueness. Since this holds for all $z \in M$, the above expression of $\hat{T}_z$ implies

$$\hat{T} = \rho Z \otimes Z + p(\hat{g} + Z \otimes Z),$$

where $\rho$ and $p$ are the (not necessarily $C^\infty$) functions on $M$ such that, in the preceding notation, $\rho(z) = a$ and $p(z) = b$ at each $z \in M$.

Since $\hat{T}Z = -\rho Z$, the quantity $-\rho$ is the eigenfunction of $\hat{T}$ corresponding to $Z$ and is therefore $C^\infty$. Since $\operatorname{tr} \hat{T} = -\rho + 3p$, the quantity $(-\rho + 3p)$ is also $C^\infty$, and hence so is $p$.

The previous inequalities for $a$ and $b$ now give: $\rho > 0$, $\rho \geq 3p \geq 0$, and $\rho = 3p$ iff $m_A = 0$ for all $A = 1, \ldots, N$. This proves (b).

For part (c): (1) $\Leftrightarrow$ (3) follows from the condition $m_A = 0$ for all $A$. (2) $\Rightarrow$ (1) is trivial. If (1) holds, then in the notation above, $a = 3b$, which implies $m_A = 0$ for all $A$, hence (3) holds. Since (1) implies (3) and (3) holds at all points, (2) follows. ∎
