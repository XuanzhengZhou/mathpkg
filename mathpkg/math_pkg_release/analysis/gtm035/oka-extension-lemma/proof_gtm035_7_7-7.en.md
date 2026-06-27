---
role: proof
locale: en
of_concept: oka-extension-lemma
source_book: gtm035
source_chapter: "7"
source_section: "7.7"
---
# Proof of Oka Extension Lemma

Fix $k$ and polynomials $q_1, \ldots, q_r$ in $z = (z_1, \ldots, z_k)$. Let $f$ be holomorphic in a neighborhood $W$ of $\Pi = P^k(q_1, \ldots, q_r)$. We need to construct $F$ holomorphic in a neighborhood of $\Pi' = P^{k+1}(q_2, \ldots, q_r)$ such that

$$F(z, q_1(z)) = f(z), \quad z \in \Pi.$$

**Proof.** Consider the map $u: \mathbb{C}^k \to \mathbb{C}^{k+1}$ given by $u(z) = (z, q_1(z))$. The image of $\Pi$ under $u$ is contained in $\Pi' = P^{k+1}(q_2, \ldots, q_r)$. Indeed, for $z \in \Pi$, we have $|z_j| \leq 1$ for $j = 1, \ldots, k$, and $|q_j(z)| \leq 1$ for $j = 1, \ldots, r$; in particular $|q_1(z)| \leq 1$, so $u(z) \in \Delta^{k+1}$, and $|q_j(z)| \leq 1$ for $j = 2, \ldots, r$, so $u(z) \in P^{k+1}(q_2, \ldots, q_r)$.

Let $\Sigma = u(\Pi)$. Consider the $(0,1)$-form on $W \times \mathbb{C}$ defined by

$$\Phi(z, z_{k+1}) = \frac{f(z)}{z_{k+1} - q_1(z)} \, d\bar{z}_{k+1}$$

in a neighborhood of $\Sigma$. Since $f$ is holomorphic, $\bar{\partial}f = 0$, and we have

$$\bar{\partial}\Phi = \frac{\bar{\partial}f}{z_{k+1} - q_1(z)} = 0$$

in a neighborhood of $\Sigma$. Thus $\Phi$ is a $\bar{\partial}$-closed $(0,1)$-form near $\Sigma$.

By Theorem 7.6 (the $\bar{\partial}$-problem on $p$-polyhedra), there exists a neighborhood $\Omega$ of $\Pi'$ and a smooth function $\chi$ on $\Omega$ such that $\bar{\partial}\chi = \Phi$ on some neighborhood of $\Sigma$ (after suitably extending $\Phi$ smoothly to a neighborhood of $\Pi'$ while preserving $\bar{\partial}$-closedness).

Now define

$$F(z, z_{k+1}) = f(z) - (z_{k+1} - q_1(z)) \chi(z, z_{k+1}).$$

Then, using $\bar{\partial}\chi = \Phi$, one verifies that $\bar{\partial}F = 0$ in a neighborhood of $\Pi'$, so $F$ is holomorphic. Moreover,

$$F(z, q_1(z)) = f(z) - 0 \cdot \chi(z, q_1(z)) = f(z), \quad z \in \Pi.$$

Thus $F$ satisfies the required properties. $\square$
