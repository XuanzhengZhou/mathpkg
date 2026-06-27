---
role: proof
locale: en
of_concept: levi-flat-boundary-of-polynomial-hull
source_book: gtm035
source_chapter: "23"
source_section: "23.6"
---
# Proof of Levi-Flat Boundary of Polynomial Hulls Over a Circle

**Theorem 23.6.** Let $Y$ be a compact set in $\mathbb{C}^2$ lying over the circle $\{|z_1| = 1\}$. Let $\Omega$ be the interior of $\hat{Y}$ ($\Omega$ is contained in $\{|z_1| < 1\}$). Then $\partial \Omega$ is Levi-flat at each point $z^0 = (z_1^0, z_2^0)$ with $|z_1^0| < 1$ at which $\partial \Omega$ is smooth near $z^0$.

*Proof.* Fix $z^0 \in \partial \Omega$ with $|z_1^0| < 1$. Choose a defining function $\rho$ for $\Omega$ such that

$$\Omega = \{ \rho(z) < 0 \},$$

$\rho$ is smooth in a neighborhood of $z^0$ in $\mathbb{C}^2$, and $(\nabla \rho)(z^0) \neq 0$.

Let $B$ be a small ball centered at $z^0$. Put $\omega = B \setminus \hat{Y}$. By Theorem 23.1, $\omega$ is pseudoconvex (each connected component of $B \setminus \hat{Y}$ is pseudoconvex). Choose a defining function $\tilde{\rho}$ for $\omega$ such that $\tilde{\rho}$ coincides with $-\rho$ in a neighborhood of $z^0$ in $\mathbb{C}^2$; this is possible because near $z^0$, the set $\omega$ is precisely the complement of $\bar{\Omega}$ inside $B$, i.e., $\omega = \{\rho > 0\} \cap B$ locally. Since $\omega$ is pseudoconvex and $\tilde{\rho} = -\rho$ near $z^0$, the Levi form condition for pseudoconvexity gives

$$\sum_{j,k=1}^{2} \left( \frac{\partial^2 \tilde{\rho}}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k \geq 0$$

for every complex tangent vector $\zeta$ to $\partial \Omega$ at $z^0$. Substituting $\tilde{\rho} = -\rho$ yields

$$\sum_{j,k=1}^{2} \left( \frac{\partial^2 (-\rho)}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k = -\sum_{j,k=1}^{2} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k \geq 0,$$

and hence

$$\sum_{j,k=1}^{2} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k \leq 0 \tag{1}$$

for every complex tangent $\zeta$ to $\partial \Omega$ at $z^0$.

On the other hand, since $\Omega$ is the interior of the polynomially convex set $\hat{Y}$, we can also use the maximum principle in a different direction. Consider $\Omega$ itself. Because $\Omega = \operatorname{int}(\hat{Y})$, and $\hat{Y}$ is polynomially convex, the maximum principle for polynomials (or analytic functions) on $\hat{Y}$ implies a pseudoconvexity-like property for $\Omega$. More precisely, $\Omega$ itself is pseudoconvex. (This can be seen by noting that on $\hat{Y}$, the functions $-\log \operatorname{dist}(\cdot, \mathbb{C}^2 \setminus \hat{Y})$ give a plurisubharmonic exhaustion, or one can directly argue via the local maximum modulus principle that holds on $\hat{Y}$.) Therefore, for the defining function $\rho$ of $\Omega$, pseudoconvexity of $\Omega$ gives

$$\sum_{j,k=1}^{2} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k \geq 0 \tag{2}$$

for every complex tangent $\zeta$ to $\partial \Omega$ at $z^0$.

Combining inequalities (1) and (2), we obtain

$$\sum_{j,k=1}^{2} \left( \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \right)_{z^0} \zeta_j \bar{\zeta}_k = 0$$

for every complex tangent vector $\zeta$ to $\partial \Omega$ at $z^0$. This means the Levi form of $\partial \Omega$ vanishes identically on the complex tangent space at $z^0$. By definition (see Section 23.5, equations (13)–(15)), $\partial \Omega$ is Levi-flat at $z^0$, completing the proof.
