---
role: proof
locale: en
of_concept: cauchy-integral-differentiability
source_book: gtm038
source_chapter: "VII"
source_section: "3"
---

Let

$$P_c := \{z \in \mathbb{C}: z + c \in P\},$$

$$\gamma(w, c) := \mathrm{Ch}_f^{(P)}(w + c) = \frac{1}{2\pi i} \int_P \frac{f(z)}{z - w - c} dz \wedge d\bar{z}$$

$$= \frac{1}{2\pi i} \int_{P_c} \frac{f(z + c)}{z - w} dz \wedge d\bar{z}.$$

Because $\mathrm{Supp}(f) \subset P$, we have

$$\gamma(w, c) = \frac{1}{2\pi i} \int_{\mathbb{C}} \frac{f(z + c)}{z - w} dz \wedge d\bar{z}.$$

By known theorems on parametric integrals (see [22]), $\gamma$ is continuously differentiable with respect to $c$ and $\bar{c}$. Since $\gamma(0, c) = g(c)$, $g$ is differentiable. Applying formulas for the derivative of parametric integrals and the chain rule gives

$$g_{\bar{z}}(c) = \frac{1}{2\pi i} \int_{\mathbb{C}} \frac{f_{\bar{z}}(z + c)}{z} dz \wedge d\bar{z} = \mathrm{Ch}_{f_{\bar{z}}}^{(\mathbb{C})}(c),$$

$$g_{\bar{z}}(c) = \frac{1}{2\pi i} \int_{P} \frac{f_{\bar{z}}(z)}{z - c} dz \wedge d\bar{z} = \mathrm{Ch}_{f_{\bar{z}}}^{(P)}(c).$$

For $w \in H$ we also have

$$\mathrm{Ch}_{f_2}^{(B)}(w) = \frac{1}{2\pi i} \int_B \frac{f_2(z)}{z-w} dz \wedge d\bar{z} = \frac{1}{2\pi i} \int_{B-H} \frac{f_2(z)}{z-w} dz \wedge d\bar{z},$$

where the integrand is continuous and bounded on $B - H$, as well as holomorphic with respect to $w$. From the theory of parametric integrals it follows that $\mathrm{Ch}_{f_2}^{(B)}|H$ is continuously differentiable and

$$(\mathrm{Ch}_{f_2}^{(B)}|H)_{\bar{w}} = 0.$$

Therefore $g|H$ is continuously differentiable and $(g|H)_{\bar{z}} = f|H$.

**Remark.** If $\hat{B} \subset \mathbb{C}$, $B^* \subset \mathbb{R}^n$ are regions, $B \subset \hat{B}$ open and $f: \hat{B} \times B^* \to \mathbb{C}$ arbitrarily often differentiable, then it follows from the theory of parametric integrals that

$$\mathrm{Ch}_{f_2}^{(B)}(w, \bar{x}) = \frac{1}{2\pi i} \int_B \frac{f(z, \bar{x})}{z-w} dz \wedge d\bar{z}$$

is arbitrarily often differentiable on $B \times B^*$, and

$$(\mathrm{Ch}_{f_2}^{(B)})_{x_v}(w, \bar{x}) = \frac{1}{2\pi i} \int_B \frac{f_{x_v}(z, \bar{x})}{z-w} dz \wedge d\bar{z}, \quad (\mathrm{Ch}_{f_2}^{(B)})_{\bar{w}} = f.$$
