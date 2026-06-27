---
role: proof
locale: en
of_concept: action-angle-transformation-is-canonical
source_book: gtm060
source_chapter: "10"
source_section: "50"
---

Consider the differential $1$-form $p \, dq$ on $M_f$. Since $M_f$ is a null manifold (Section 49), the $2$-form $\omega^2 = dp \wedge dq$ is identically zero on $M_f$. Therefore the $1$-form $p \, dq$ is closed on $M_f$. By Stokes' formula,

$$S(x) = \int_{x_0}^{x} p \, dq\big|_{M_f}$$

does not change under deformations of the path of integration. Thus $S(x)$ is a "multiple-valued function" on $M_f$, with periods equal to

$$\Delta_i S = \int_{\gamma_i} dS = 2\pi I_i.$$

Now let $x_0$ be a point on $M_f$ where the $n$ variables $q$ serve as local coordinates on $M_f$, so that the submanifold $M_f \subset \mathbb{R}^{2n}$ is given by $n$ equations of the form $p = p(I, q)$ with $q(x_0) = q_0$. In a simply connected neighborhood of $q_0$, a single-valued function

$$S(I, q) = \int_{q_0}^{q} p(I, q) \, dq$$

is defined. Using $S$ as the generating function of a canonical transformation $p, q \to I, \varphi$:

$$p = \frac{\partial S}{\partial q}, \quad \varphi = \frac{\partial S}{\partial I}.$$

To verify that these formulas yield a canonical transformation both locally and "in the large" in a neighborhood of $M_f$, we compute the periods of the angle variables:

$$\Delta_i \varphi_j = \Delta_i \frac{\partial S}{\partial I_j} = \frac{\partial}{\partial I_j} \Delta_i S = \frac{\partial}{\partial I_j} 2\pi I_i = 2\pi \delta_{ij}.$$

Thus the coordinates $\varphi$ are multi-valued with periods that are integral multiples of $2\pi$, and the transformation preserves the canonical $2$-form. Consequently, the problem of integrating a canonical system with $2n$ equations when $n$ first integrals in involution are known is solved by quadratures, which proves the last assertion of Liouville's theorem.
