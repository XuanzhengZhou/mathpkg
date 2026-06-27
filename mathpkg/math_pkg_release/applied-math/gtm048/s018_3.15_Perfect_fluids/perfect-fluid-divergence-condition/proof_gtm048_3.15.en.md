---
role: proof
locale: en
of_concept: perfect-fluid-divergence-condition
source_book: gtm048
source_chapter: "3"
source_section: "3.15"
---

We compute the divergence of $\hat{T} = \rho Z \otimes Z + p(\hat{g} + Z \otimes Z)$. In index notation,
$$\hat{T}^{ij} = \rho Z^i Z^j + p g^{ij} + p Z^i Z^j.$$

The condition $\operatorname{div} \hat{T} = 0$ is $\hat{T}^{ij}_{\ \ ; j} = 0$:
$$(\rho Z^i Z^j + p g^{ij} + p Z^i Z^j)_{; j} = 0.$$

Expanding the covariant derivative:
$$Z^i_{\ ; j}(\rho Z^j) + Z^i(\rho Z^j)_{; j} + p_{; j} g^{ij} + p_{; j} Z^i Z^j + p Z^i_{\ ; j} Z^j + p Z^i Z^j_{\ ; j} = 0.$$

In coordinate-free notation, using the metric to raise and lower indices and converting covariant derivatives to the geometric objects:
$$\rho D_Z Z + (\operatorname{div} \rho Z) Z + \operatorname{grad} p + (Zp) Z + p D_Z Z + p (\operatorname{div} Z) Z = 0.$$

Grouping terms containing $Z$ separately from those orthogonal to $Z$:
$$\{(\operatorname{div} \rho Z) + p \operatorname{div} Z\} Z + \{(\rho + p) D_Z Z + \operatorname{grad} p + (Zp) Z\} = 0.$$

Now observe that the sum inside the second set of braces is orthogonal to $Z$:
- $g(D_Z Z, Z) = \frac{1}{2} Z g(Z, Z) = \frac{1}{2} Z 1 = 0$, so $D_Z Z \perp Z$.
- $g(\operatorname{grad} p + (Zp) Z, Z) = g(\operatorname{grad} p, Z) + (Zp) g(Z, Z) = Zp - Zp = 0$, so $\operatorname{grad} p + (Zp) Z \perp Z$.

Since the two braced expressions are orthogonal (the first is parallel to $Z$, the second is orthogonal to $Z$), their sum vanishing implies each vanishes individually. Therefore:

$$\operatorname{div}(\rho Z) + p \operatorname{div} Z = 0,$$
which is condition (a): $\operatorname{div}(\rho Z) = -p \operatorname{div} Z$.

And:
$$(\rho + p) D_Z Z + \operatorname{grad} p + (Zp) Z = 0,$$
which yields condition (b):
$$D_Z Z = -(\rho + p)^{-1}\{(Zp) Z + \operatorname{grad} p\}.$$

The hypothesis $\rho + p > 0$ ensures the coefficient $(\rho + p)^{-1}$ is well-defined.
