---
role: proof
locale: en
of_concept: corollary-6-6
source_book: gtm012
source_chapter: "3"
source_section: "6"
---

# Proof of Corollary 6.6: Distributions with Zero Derivative are Constant Functions

**Corollary 6.6.** If $G \in \mathcal{P}'$ and $DG = 0$, then $G = F_f$, where $f$ is a constant function.

*Proof.* Let $e(x) = 1$ for all $x$. Define the constant

$$f = \frac{1}{2\pi}\,G(e) \cdot e,$$

and set

$$H = G - F_f.$$

Then $F_f$ is the distribution corresponding to the constant function $f$, and

$$DH = DG - DF_f = 0 - 0 = 0,$$

since the derivative of any constant function distribution vanishes. Moreover,

$$H(e) = G(e) - F_f(e) = G(e) - \frac{1}{2\pi}\int_0^{2\pi} f \cdot 1\,dx = G(e) - f \cdot 1 = 0,$$

because $f = (2\pi)^{-1}G(e)$ as a scalar and $F_f(e) = f \cdot F_e(e) = f \cdot 1 = f$ (noting $F_e(e) = \frac{1}{2\pi}\int_0^{2\pi} 1\,dx = 1$).

Thus we have $H \in \mathcal{P}'$ with $DH = 0$ and $H(e) = 0$. By Lemma 6.5, the unique distribution $K \in \mathcal{P}'$ satisfying $DK = 0$ and $K(e) = 0$ is $K = 0$. Hence $H = 0$, and therefore

$$G = F_f,$$

where $f$ is constant. $\square$

*Remark.* This corollary shows that the kernel of the differentiation operator $D: \mathcal{P}' \to \mathcal{P}'$ consists precisely of the constant function distributions. This is the distributional analogue of the elementary fact that a function with zero derivative on a connected interval is constant.
