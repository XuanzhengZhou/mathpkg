---
role: proof
locale: en
of_concept: van-kampen-trivial-intersection
source_book: gtm057
source_chapter: "V"
source_section: "3"
---

**Corollary (3.3):** If $G_0$ is trivial and $G_1, G_2$ are free with bases $\{\alpha_i\}, \{\beta_j\}$, then $G$ is free with basis $\{\omega_1\alpha_i, \omega_2\beta_j\}$.

*Proof.* Let $H$ be free on $\{x_i, y_j\}$ with maps $\psi_1(\alpha_i) = x_i$, $\psi_2(\beta_j) = y_j$. Since $G_0 = 1$, $\psi_0 = 1$ and $\psi_0 = \psi_1\theta_1 = \psi_2\theta_2$ trivially. By the van Kampen theorem, there exists $\lambda: G \to H$ with $\psi_i = \lambda\omega_i$. The sets $\{\omega_1\alpha_i, \omega_2\beta_j\}$ map to the free basis of $H$, so they freely generate $G$. Thus $G$ is free with the union as a free basis.
