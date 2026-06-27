---
role: proof
locale: en
of_concept: T-alpha-proper-orthochroneous
source_book: gtm023
source_chapter: "XI"
source_section: "§5. Application to Lorentz-transformations, 11.18"
---

**Properness.** To show $\det T_{\alpha} = 1$, let $\alpha(t)$ ($0 \leq t \leq 1$) be a continuous family of linear transformations of $C$ such that

$$\alpha(0) = \iota, \quad \alpha(1) = \alpha, \quad \text{and} \quad \det \alpha(t) = 1 \quad (0 \leq t \leq 1).$$

Such a family exists by the result of sec. 4.36 (the special linear group $\operatorname{SL}(2, \mathbb{C})$ is path-connected). Consider the continuous function

$$\det T_{\alpha(t)} \quad (0 \leq t \leq 1).$$

Since $T_{\alpha(t)}$ is a Lorentz transformation for each $t$, its determinant is $\pm 1$. At $t = 0$,

$$\det T_{\alpha(0)} = \det T_{\iota} = \det(\operatorname{id}_S) = 1.$$

By continuity, $\det T_{\alpha(t)} = 1$ for all $t \in [0,1]$, hence $\det T_{\alpha} = 1$.

**Orthochroneity.** To prove $T_{\alpha}$ is orthochroneous, observe that

$$T_{\alpha} \iota = \alpha \circ \tilde{\alpha}.$$

Since $\alpha \circ \tilde{\alpha}$ is a positive selfadjoint transformation, it lies in the forward light cone. Computing the inner product with $\iota$:

$$\langle \iota, T_{\alpha} \iota \rangle = \langle \iota, \alpha \circ \tilde{\alpha} \rangle = -\frac{1}{2} \operatorname{tr}(\alpha \circ \tilde{\alpha}) < 0,$$

which shows $T_{\alpha} \iota$ is in the same connected component of the light cone as $\iota$. Hence $T_{\alpha}$ preserves the causal structure (fore-cone and past-cone).
