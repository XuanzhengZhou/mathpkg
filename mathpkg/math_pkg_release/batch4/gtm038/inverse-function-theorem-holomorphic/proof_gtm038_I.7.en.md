---
role: proof
locale: en
of_concept: inverse-function-theorem-holomorphic
source_book: gtm038
source_chapter: "I"
source_section: "7. Holomorphic Mappings"
---

**Theorem 7.4 (Inverse Function Theorem for holomorphic mappings).** Let $G \subset \mathbb{C}^n$ be a region, $f: G \to \mathbb{C}^n$ a holomorphic mapping, and $z_0 \in G$ a point with $\det J_f(z_0) \neq 0$. Then there exists an open neighborhood $U = U(z_0) \subset G$ such that $f|U: U \to f(U)$ is biholomorphic.

**Proof.** The complex Jacobian determinant $\det J_f$ agrees (up to a nonzero constant factor) with the real Jacobian determinant of $f$ viewed as a mapping $\mathbb{R}^{2n} \to \mathbb{R}^{2n}$. Indeed, the Cauchy-Riemann equations imply the complex and real Jacobians are related by a factor of $2^{-n}$. Since $\det J_f(z_0) \neq 0$, the real Jacobian is also non-vanishing. By the real inverse function theorem, $f$ is a local $\mathcal{C}^{\infty}$-diffeomorphism near $z_0$. The inverse mapping $f^{-1}$ is real differentiable, and because $f$ satisfies the Cauchy-Riemann equations ($f_{\bar{z}_v} = 0$), the chain rule and the fact that $J_{f^{-1}} = (J_f)^{-1}$ imply $f^{-1}$ also satisfies the Cauchy-Riemann equations. Hence $f^{-1}$ is holomorphic, and $f$ is locally biholomorphic.
