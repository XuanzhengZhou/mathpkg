---
role: proof
locale: en
of_concept: cstar-homomorphism-automatically-continuous
source_book: gtm003
source_chapter: "VI"
source_section: "2"
---

With the remark about unitizations (Exercise 7), we may suppose $A$ and $B$ are unital and $\Phi(e_A) = e_B$. Since $\sigma(\Phi(x)) \subset \sigma(x)$ for any $x \in A$, we have $r(\Phi(x)) \leq r(x)$. For a self-adjoint element $h$, $r(h) = \|h\|$ (by 2.1(ii)), so $\|\Phi(h)\| = r(\Phi(h)) \leq r(h) = \|h\|$. For general $x$, $\|\Phi(x)\|^2 = \|\Phi(x)^*\Phi(x)\| = \|\Phi(x^*x)\| \leq \|x^*x\| = \|x\|^2$, establishing contractivity.

If $\Phi$ is injective, then $\Phi$ preserves spectra (otherwise $\Phi(\lambda e - x)$ would be invertible while $\lambda e - x$ is not, contradicting injectivity via the Gelfand transform arguments). Hence $\|\Phi(x)\| = r(\Phi(x^*x))^{1/2} = r(x^*x)^{1/2} = \|x\|$, so $\Phi$ is isometric.

Since $\Phi$ is isometric from $A/\ker \Phi$ onto $\Phi(A)$, the open mapping theorem gives that $\Phi$ is open onto its image. The image $\Phi(A)$ is closed in $B$ and satisfies the C*-identity, so it is a C*-subalgebra.
