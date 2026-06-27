---
role: proof
locale: en
of_concept: levi-flat-from-analytic-disk
source_book: gtm035
source_chapter: "23"
source_section: "23.5"
---
# Proof of Levi-Flat Boundary from Embedded Analytic Disk

**Theorem 23.5.** Let $\Omega$ be a region in $\mathbb{C}^2$ and fix $z^0 \in \partial \Omega$ with $\partial \Omega$ smooth near $z^0$. Assume that there exists an analytic disk, $z = f(\lambda)$, with $f(0) = z^0$, which is contained in $\partial \Omega$, and $\frac{df}{d\lambda}(0) \neq 0$. Then $\partial \Omega$ is Levi-flat at $z^0$.

*Proof.* Let $\Omega$ be given by $\{\rho(z) < 0\}$ with $\rho$ smooth in a neighborhood of $z^0$. Then

$$\rho(f(\lambda)) = 0, \quad |\lambda| < 1,$$

since the analytic disk lies entirely in $\partial \Omega$. Differentiating with respect to $\lambda$, we obtain, writing $f'_j = df_j/d\lambda$,

$$\frac{\partial}{\partial \lambda}\bigl(\rho(f(\lambda))\bigr) = \sum_{j=1}^{2} \frac{\partial \rho}{\partial z_j}(f(\lambda)) \, f'_j(\lambda) = 0.$$

Evaluating at $\lambda = 0$, this gives

$$\sum_{j=1}^{2} \frac{\partial \rho}{\partial z_j}(z^0) \, f'_j(0) = 0.$$

Thus $f'(0) = (f'_1(0), f'_2(0))$ is a complex tangent vector to $\partial \Omega$ at $z^0$, by the definition of the complex tangent space given in Section 23.1.

Next, differentiate the equation

$$\sum_{j=1}^{2} \frac{\partial \rho}{\partial z_j}(f(\lambda)) \, f'_j(\lambda) = 0$$

with respect to $\bar{\lambda}$. Since $f'_j(\lambda)$ is holomorphic in $\lambda$, we have $\frac{\partial}{\partial \bar{\lambda}} f'_j(\lambda) = 0$. Hence

$$\frac{\partial}{\partial \bar{\lambda}} \left( \sum_{j=1}^{2} \frac{\partial \rho}{\partial z_j}(f(\lambda)) \, f'_j(\lambda) \right)
= \sum_{j,k=1}^{2} \frac{\partial^2 \rho}{\partial \bar{z}_k \partial z_j}(f(\lambda)) \, \overline{f'_k(\lambda)} \, f'_j(\lambda) = 0.$$

Evaluating at $\lambda = 0$ yields

$$\sum_{j,k=1}^{2} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} f'_j(0) \, \overline{f'_k(0)} = 0.$$

Note that we have interchanged the order of the indices in the Hessian to write it in the standard Levi form notation; the equality holds because the mixed partials commute for a smooth ($\mathcal{C}^2$) function $\rho$.

Since $f'(0) \neq 0$ by hypothesis, $f'(0)$ is a nonzero complex tangent vector to $\partial \Omega$ at $z^0$. The equation above shows that the Levi form

$$L(\zeta) = \sum_{j,k=1}^{2} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k$$

vanishes on the nonzero complex tangent vector $\zeta = f'(0)$.

This means that the Levi form is degenerate: it can take both positive and negative values (or is identically zero) on the complex tangent space. In particular, the Levi form cannot be strictly positive definite nor strictly negative definite. Therefore $\partial \Omega$ is Levi-flat at $z^0$, by the definition of Levi-flatness given in equations (13)–(15) of Section 23.5. More precisely, both inequalities

$$\sum_{j,k} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k \geq 0 \quad \text{and} \quad \sum_{j,k} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k \leq 0$$

hold for all complex tangent vectors $\zeta$ — the first because the disk in $\partial \Omega$ shows the form cannot be strictly positive, and the second follows by symmetry considering the complement $\{-\rho < 0\}$. Hence the Levi form vanishes identically on the complex tangent space, establishing Levi-flatness.
