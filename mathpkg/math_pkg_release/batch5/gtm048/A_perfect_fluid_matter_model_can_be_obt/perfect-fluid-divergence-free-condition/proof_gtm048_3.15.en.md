---
role: proof
locale: en
of_concept: perfect-fluid-divergence-free-condition
source_book: gtm048
source_chapter: "3"
source_section: "3.15"
---

**Proof.** The condition $\operatorname{div} \hat{T} = 0$ is expanded in coordinates as follows:

$$\operatorname{div} \hat{T} = 0 \Leftrightarrow (\rho Z^i Z^j + p g^{ij} + p Z^i Z^j)_{;j} = 0,$$

where the semicolon denotes the covariant derivative. Expanding the covariant derivative:

$$\Leftrightarrow Z^i_{;j}(\rho Z^j) + Z^i(\rho Z^j)_{;j} + p_{;j} g^{ij} + p_{;j} Z^i Z^j + p Z^i Z^j_{;j} = 0.$$

Rewriting in coordinate-free notation using the covariant derivative $D$ along $Z$:

$$\Leftrightarrow \rho D_Z Z + (\operatorname{div} \rho Z) Z + \operatorname{grad} p + (Zp) Z + p D_Z Z + p (\operatorname{div} Z) Z = 0.$$

Grouping terms parallel and orthogonal to $Z$:

$$\Leftrightarrow \{(\operatorname{div} \rho Z) + p \operatorname{div} Z\} Z + \{(\rho + p) D_Z Z + \operatorname{grad} p + (Z p) Z\} = 0.$$

The sum inside the second set of braces is orthogonal to $Z$ for the following reasons. First, applying the metric compatibility of the connection:

$$g(D_Z Z, Z) = \frac{1}{2} Z g(Z, Z) = \frac{1}{2} Z(1) = 0,$$

since $Z$ is a unit timelike vector field (i.e., $g(Z, Z) = -1$ in the $(-,+,+,+)$ convention, or more generally $g(Z, Z)$ is constant). Second,

$$g(\operatorname{grad} p + (Z p) Z, Z) = g(\operatorname{grad} p, Z) + (Z p) g(Z, Z) = Z p + (Z p) \cdot (\text{constant}) = 0.$$

Thus the two components — one parallel to $Z$ and one orthogonal to $Z$ — must vanish independently. Setting the $Z$-parallel component to zero yields condition (a):

$$\operatorname{div}(\rho Z) + p \operatorname{div} Z = 0 \Leftrightarrow \operatorname{div}(\rho Z) = -p \operatorname{div} Z.$$

Setting the $Z$-orthogonal component to zero yields condition (b):

$$(\rho + p) D_Z Z + \operatorname{grad} p + (Z p) Z = 0 \Leftrightarrow D_Z Z = -(\rho + p)^{-1}\{(Z p) Z + \operatorname{grad} p\},$$

where the division by $\rho + p$ is justified by the hypothesis $\rho + p > 0$. ∎
